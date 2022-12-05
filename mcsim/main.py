import numpy as np
import pandas as pd
from scipy.stats import norm, skewnorm
#import polars as pl
import csv
import sys

class RentChangeDist:
    def __init__(self, data, k):
        self.data = data
        self.k = k

    def draw_skewed(self, a):
        self.data = self.data.loc[:, self.data.columns != 'Year']
        df_avg_cost_change = pd.concat([self.data.pct_change().loc[1:].mean(),
                                       self.data.pct_change().loc[1:].std()])
        campus = df_avg_cost_change.keys()[self.k]
        loc = df_avg_cost_change[campus][0]
        scale = df_avg_cost_change[campus][1]
        sample = skewnorm.rvs(
                a=a,
                loc=loc, 
                scale=scale, 
                size=1, 
            )
        return sample[0]

class Rates:
    def __init__(self, **kwargs):
        self.k = kwargs['k']
        self.meth = kwargs['meth']
        self.alp_rng = kwargs['alp_rng']
        self.beta_rng = kwargs['beta_rng']
        self.rate = None
        self.rent_data = kwargs['rent_data'] 
        self.skew = kwargs['skew']
        #self.rate_timeseries = kwargs['rate_timeseries']
    
    def _setrate(self, meth):
        dist = RentChangeDist(self.rent_data, self.k)
        if meth == 'rent change skewed':
            self.rate = dist.draw_skewed(a=self.skew) 
            
        # Yet to implement other methods 

    def getrates(self):
        self._setrate(self.meth)
        if hasattr(self.alp_rng[self.k], '__len__') and hasattr(self.beta_rng[self.k], '__len__'):
            sys.exit("alpha and beta can't both be dynamic for a given locality")
        elif hasattr(self.alp_rng[self.k], '__len__'):
            alp = self.rate 
            beta = self.beta_rng[self.k]
        elif hasattr(self.beta_rng[self.k], '__len__'):
            alp = self.alp_rng[self.k]
            beta = self.rate
        else:
            beta = self.beta_rng[self.k]
            alp = self.alp_rng[self.k]
        return alp, beta, self.rate

class WageModel:
    # Initialize
    def __init__(self, **kwargs):
        self.a = kwargs['a']
        self.bw_0 = kwargs['bw_0']
        self.stepwide_alp = kwargs['stepwide_alp']
        self.h = np.array([h for h in kwargs['h_0']])
        self.r = kwargs['r']
        self.yf = kwargs['yf']
        self.y_max = kwargs['y_max']
        self.d = kwargs['d']
        self.y_grad = kwargs['y_grad']
        self.S_tot = kwargs['S_tot']
        self.rent_data = kwargs['rent_data']
        self.R = self.rent_data.loc[len(self.rent_data)-1:, self.rent_data.columns != 'Year'].values.tolist()[0]
        # Assume the rental data is monthly, we want it yearly
        self.R = np.array(self.R)*12
        self.rho = None
        self.rep = kwargs['rep']
        self.meth = kwargs['meth']
        self.alp = None
        self.beta = None
        self.rate_timeseries = kwargs['rate_timeseries']
        self.alp_rng = kwargs['alp_rng']
        self.beta_rng = kwargs['beta_rng']
        wages = []
        for k in range(len(self.bw_0)):
            wages.append(list(self.a*self.bw_0[k]))
        self.wages = np.array(wages)
        self.skew = kwargs['skew']

    def _checkranges(self, rate):
        if hasattr(rate, '__len__'):
            # If the rates are defined for each locality, check each one
            if len(rate) == len(self.bw_0):
                new_rate = []
                for k_rng in rate:
                    # Only allow either static single numbers or dynamic [min,max] range
                    if hasattr(k_rng, '__len__') == False:
                        new_rate.append(k_rng)
                    elif hasattr(k_rng, '__len__') and (len(k_rng) == 2):
                        new_rate.append(k_rng)
                    else:
                        sys.exit('Local rates should either be static or only have min and max')
                rate = new_rate
            # If a global range has been set, use it for each locality
            elif len(rate) == 2:
                rate = [rate for i in range(len(self.bw_0))]
            # If not a global range or defined per locality, something is wrong
            else:
                sys.exit('Rates must be definied globally or for each locality')
        else:
            rate = [rate for i in range(len(self.bw_0))]
        return rate

    def _getrent_flat(self, t, k):
        # Draw numbers stupidly from a flat distribution, just for testing
        return np.random.randint(1600,4000)*12
    
    ######## If implemented, these should be moved to the Rates class
    #def _alpfromrent(self, k, R):
    #    if type(self.alp_rng) == list:
    #        return None
    #    else:
    #        return self.alp_rng

    #def _betafromrent(self, k, R):
    #    # Note, alp_rng must be static to use this!
    #    beta = (R - self.r*self.wages[k][0]*(self.alp_rng+1) - self.r*self.h[k]) / (self.r*self.h[k])
    #    return self._checkbeta(beta,k)
    ########

    def _rangeconstraint(self, t_i, k):
        if self.rate_timeseries:
            # If rate can be within some range for k, constrain rates within min/max
            if hasattr(self.alp_rng[t_i][k], '__len__') or hasattr(self.beta_rng[t_i][k], '__len__'):
                if hasattr(self.alp_rng[t_i][k], '__len__'):
                    if self.alp < min(self.alp_rng[t_i][k]):
                        self.alp = min(self.alp_rng[t_i][k])
                    elif self.alp > max(self.alp_rng[t_i][k]):
                        self.alp = max(self.alp_rng[t_i][k])
                elif hasattr(self.beta_rng[t_i][k], '__len__'):
                    if self.beta < min(self.beta_rng[t_i][k]):
                        self.beta = min(self.beta_rng[t_i][k])
                    elif self.beta > max(self.beta_rng[t_i][k]):
                        self.beta = max(self.beta_rng[t_i][k])
            # If rate is constrained to a single number, do nothing
            else:
                pass
        else:
            # If rate can be within some range for k, constrain rates within min/max
            if hasattr(self.alp_rng[k], '__len__') or hasattr(self.beta_rng[k], '__len__'):
                if hasattr(self.alp_rng[k], '__len__'):
                    if self.alp < min(self.alp_rng[k]):
                        self.alp = min(self.alp_rng[k])
                    elif self.alp > max(self.alp_rng[k]):
                        self.alp = max(self.alp_rng[k])
                elif hasattr(self.beta_rng[k], '__len__'):
                    if self.beta < min(self.beta_rng[k]):
                        self.beta = min(self.beta_rng[k])
                    elif self.beta > max(self.beta_rng[k]):
                        self.beta = max(self.beta_rng[k])
            # If rate is constrained to a single number, do nothing
            else:
                pass

    def runsim(self, outfile, tstep=1, tfinal=5, static_alp=True, verbose=True):
        # csv writer for output
        writer = csv.writer(outfile)
        #print('self.R(t=0) = {}'.format(self.R))
        for k in range(len(self.bw_0)):
            line = np.concatenate(([self.rep,0,k], list(self.wages[k]), [self.h[k]], [self.R[k]]))
            writer.writerow(line)

        col_names = ['step {}'.format(i) for i in range(len(self.a))]
        if verbose:
            print('time',0,'-------------------------------------------------')
            print('wages:')
            print(pd.DataFrame(self.wages, columns=col_names))
            print('housing stipends:',self.h)
            print('rental costs:', self.R)

        ### Main for loop ###
        
        # If the wage and rent rates of change are not time dependent, set them here
        if self.rate_timeseries == False:
            self.alp_rng = self._checkranges(self.alp_rng)
            self.beta_rng = self._checkranges(self.beta_rng)
        for t_i, t in enumerate(np.arange(0+tstep, tfinal+tstep, tstep)): 
            # If rates are time dependent, set them here
            if self.rate_timeseries:
                self.alp_rng[t_i] = self._checkranges(self.alp_rng[t_i])
                self.beta_rng[t_i] = self._checkranges(self.beta_rng[t_i])
            # Make arrays to store the rates in
            alp_arr = []
            beta_arr = []
            rho_arr = []
            # Loop over the localities
            for k in range(len(self.bw_0)):
                # Draw and constrain the wage and rent change rates 
                if self.rate_timeseries:
                    rates_k = Rates(k=k, meth=self.meth, skew=self.skew, rent_data=self.rent_data,
                                    alp_rng=self.alp_rng[t_i], beta_rng=self.beta_rng[t_i])
                    self.alp, self.beta, self.rho = rates_k.getrates()
                else:
                    rates_k = Rates(k=k, meth=self.meth, skew=self.skew, rent_data=self.rent_data,
                                    alp_rng=self.alp_rng, beta_rng=self.beta_rng)
                    self.alp, self.beta, self.rho = rates_k.getrates()
                self._rangeconstraint(t_i, k)
                alp_arr.append(self.alp)
                beta_arr.append(self.beta)
                rho_arr.append(self.rho)
                # Increase wages
                if self.stepwide_alp:
                    self.wages[k] = self.wages[k] * (self.alp + 1)
                else:
                    self.wages[k][0] = self.wages[k][0] * (self.alp + 1)
                    self.wages[k] = self.a * self.wages[k][0]
                # Increase housing stipend
                self.h[k] = self.h[k] * (self.beta + 1)
                # Increment rental costs
                self.R[k] = self.R[k] * (self.rho + 1)
                # Make array of strings to write and write to output
                line = np.concatenate(([self.rep,t,k], list(self.wages[k]), [self.h[k]], [self.R[k]]))
                writer.writerow(line)

            if verbose:
                print('time',t,'--------------------------------------------------')
                print('alphas:',alp_arr)
                print('betas:', beta_arr)
                print('rhos:', rho_arr)
                print('wages:')
                print(pd.DataFrame(self.wages, columns=col_names))
                print('housing stipends:',self.h)
                print('rental costs:', self.R)

