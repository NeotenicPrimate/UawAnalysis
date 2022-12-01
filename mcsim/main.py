import numpy as np
import pandas as pd
from scipy.stats import norm, skewnorm
import polars as pl
import csv

class RentChangeDist:
    def __init__(self, data, k):
        self.data = data
        self.k = k

    def draw_skewed(self, a):
        df_avg_cost_change = pl.concat([
            self.data.select((pl.all().exclude('Year').pct_change() * 100).mean().round(2)),
            self.data.select((pl.all().exclude('Year').pct_change() * 100).std().round(2))
        ], rechunk=True)
        campus = df_avg_cost_change.columns[self.k]
        loc = df_avg_cost_change[campus][0]
        scale = df_avg_cost_change[campus][1]
        sample = skewnorm.rvs(
                a=a,
                loc=loc, 
                scale=scale, 
                size=1, 
            )
        return sample[0]

class WageModel:
    def __init__(self, a, bw, alp_rng, stepwide_alp, h, beta_rng, r, 
                 yf, y_max, d, y_grad, S_tot, rep):
        self.a = a
        self.bw = bw
        self.alp_rng = alp_rng
        self.stepwide_alp = stepwide_alp
        self.h = h
        self.beta_rng = beta_rng
        self.r = r
        self.yf = yf
        self.y_max = y_max
        self.d = d
        self.y_grad = y_grad
        self.S_tot = S_tot
        self.rep = rep

        wages = []
        for k in range(len(self.bw)):
            wages.append(list(self.a*self.bw[k]))
        self.wages = np.array(wages)

    def _getrent_flat(self, t, k):
        # Draw numbers stupidly from a flat distribution, just for testing
        return np.random.randint(1600,4000)*12
    
    def _alpfromrent(self, t, k, R):
        if type(self.alp_rng) == list:
            return None
        else:
            return self.alp_rng

    def _checkbeta(self, beta, k):
        #print('beta for campus',k,'before constraints:',beta)
        if len(self.beta_rng) == 1:
            if beta < min(self.beta_rng):
                beta = min(self.beta_rng)
            elif beta > max(self.beta_rng):
                beta = max(self.beta_rng)
        elif len(self.beta_rng) > 1:
            if beta < min(self.beta_rng[k]):
                beta = min(self.beta_rng[k])
            elif beta > max(self.beta_rng[k]):
                beta = max(self.beta_rng[k])
        else:
            beta = self.beta_rng
        return beta

    def _betafromrent(self, t, k, R):
        # Note, alp_rng must be static to use this!
        beta = (R - self.r*self.bw[k]*(self.alp_rng+1) - self.r*self.h[k]) / (self.r*self.h[k])
        return self._checkbeta(beta,k)

    def runsim(self, outfile, tstep=1, tfinal=5, static_alp=True, verbose=True):
        # csv writer for output
        writer = csv.writer(outfile)
        #line = [self.rep,0]
        for k in range(len(self.bw)):
            line = np.concatenate(([self.rep,0,k],list(self.wages[k]),[self.h[k]]))
            writer.writerow(line)
        # Load the rent data
        df_rent = pl.read_csv('rentdata.csv')
        if verbose:
            print('time',0,'-------------------------------------------------')
            print('wages:',pd.DataFrame(self.wages))
            print('housing stipends:',self.h)
        for t in np.arange(0+tstep, tfinal, tstep): 
            beta_arr = []
            for k in range(len(self.bw)):
                #line = [self.rep,t]
                if static_alp:
                    # Include a breakpoint to check that alprng is a static number
                    # Increase wages
                    alp = self.alp_rng
                    if self.stepwide_alp:
                        self.wages[k] = self.wages[k] * (alp + 1)
                    else:
                        self.bw[k] = self.bw[k] * (alp + 1)
                        self.wages[k] = self.a * self.bw[k]

                    # Increase housing stipend
                    #beta = self._betafromrent(t,k,R)
                    # Draw % increase from a distribution fit to housing market data
                    beta = RentChangeDist(df_rent,k).draw_skewed(a=0)/100
                    beta = self._checkbeta(beta,k)
                    beta_arr.append(beta)
                    self.h[k] = self.h[k] * (beta + 1)
                #line = np.concatenate((line,[k],list(self.wages[k]),[self.h[k]]))
                line = np.concatenate(([self.rep,t,k],list(self.wages[k]),[self.h[k]]))
                writer.writerow(line)

            if verbose:
                print('time',t,'--------------------------------------------------')
                print('alpha=',alp)
                print('betas:', beta_arr)
                print('wages:')
                print(pd.DataFrame(self.wages))
                print('housing stipends:',self.h)

