<p align="center">
    <img src="./img/uaw-logo.webp" width="400" height="300">
    <br><br>
    <h1 align="center">Analysis Team</h1>
</p>

<h3>&nbsp;&nbsp;Contents :books:</h3>

- [Objectives](#objectives)
    - [Base Salary Increase](#base-salary-increase)
    - [Yearly Salary Increase](#yearly-salary-increase)
    - [Standardized Increase](#standardized-increase) 
    - [Localized Increase](#localized-increase)
- [Analysis](#analysis)
    - [UC Housing](#uc-housing)
- [Current Numbers](#current-numbers)
- [Todo](#todo)

---

<h3>&nbsp;&nbsp;Objectives</h3>

The objective of this repository is to analyze the available data to inform the Uaw bargaining teams accross our 10 campuses
- Berkeley
- Davis
- Irvine, 
- Los Angeles
- Merced
- Riverside
- San Diego
- San Francisco
- Santa Barbara
- Santa Cruz

---

Our two goals is can be stated as follows:

<h3>&nbsp;&nbsp;Base Salary Increase</h3>

1. **Salaries must match the current cost of living**.

    A one time increase of the current salaries to reflect accurately the cost of living.

<h3>&nbsp;&nbsp;Yearly Salary Increase</h3>

2. **Salaries must be adjusted yearly to reflect the corresponding increase in cost of living**.

   A yearly recurring percent increase in salary to reflect the the corresponding yearly increase in the cost of living.

> If the first condition is met but the second condition is not met, salaries will not keep up with the increasing cost of living and we will just be kicking the bottle down the road. <br>
> If the second condition is met but the first condition is not met, salaries will be chasing the increasing cost of living but will never catch up.

---

There are two ways we can implement the **Base Salary Increase** and the **Base Salary Increase**

<h3>&nbsp;&nbsp;Standardized Increase</h3>

The same **Base Salary Increase** and **Yearly Salary Increase** are applied to all campuses based on an aggregate cost of living index agreed upon by both parties

<table>
    <tr>
        <th>Pros</th>
        <th>Cons</th>
    </tr>
    <tr>
        <td>Ease of implementation</td>
        <td>Campuses benefit differentially</td>
    </tr>
</table>

<h3>&nbsp;&nbsp;Localized Increase</h3>

Different **Base Salary Increase** and **Yearly Salary Increase** are applied to different campuses based on cost of living indices agreed upon by both parties

<table>
    <tr>
        <th>Pros</th>
        <th>Cons</th>
    </tr>
    <tr>
        <td>To each according to their need</td>
        <td>Difficulty of implementation</td>
    </tr>
</table>

---

<h3>&nbsp;&nbsp;Analysis</h3>

By how much does the **Base Salary Increase** and **Yearly Salary Increase**?

1. Based on the [UC Housing Data](#uc-housing)

- [Here](https://github.com/NeotenicPrimate/UawAnalysis/blob/main/analaysis/uc_housing.ipynb)

---

Thus, to summarize, our questions are:

1. Should the **Base Salary Increase** be **Localized** or **Standardized**?
2. Should the **Yearly Salary Increase** be **Localized** or **Standardized**?
3. What should the **Base Salary Increase** be?
4. What should the **Yearly Salary Increase** be?

Our option can be visualized as follows:

<table>
    <tr>
        <th rowspan=2 colspan=2></th>
        <th colspan=2>Base Salary Increase</th>
    </tr>
    <tr>
        <th colspan=1>Localized</th>
        <th colspan=1>Standardized</th>
    </tr>
    <tr>
        <th rowspan=2 colspan=1>Yearly Salary Increase</th>
        <th rowspan=1>Localized</th>
        <td rowspan=1> <p>&#128204;</p> </td>
        <td rowspan=1> <p>&#128204;</p> </td>
    </tr>
    <tr>
        <th rowspan="1">Standardized</th>
        <td rowspan="1"> <p>&#128204;</p> </td>
        <td rowspan="1"> <p>&#128204;</p> </td>
    </tr>
</table>

<h3>&nbsp;&nbsp;Current Numbers</h3>

### I. Base Salary Increase

<table>
    <tr>
        <th>Current Net Salary</th>
        <td>$24,000</td>
    </tr>
    <tr>
        <th>Current Gross Salary</th>
        <td> <p>&#128204;</p> </td>
    </tr>
    <tr>
        <th>Proposed Net Salary</th>
        <td> $54,000 </td>
    </tr>
    <tr>
        <th>Proposed Gross Salary</th>
        <td> <p>&#128204;</p> </td>
    </tr>
</table>

### 2. Yearly Salary Increase

<table>
    <tr>
        <th>Current Yearly Increase</th>
        <td> None </td>
    </tr>
    <tr>
        <th>Proposed Yearly Increase</th>
        <td> 
            <b>1.</b> Index based yearly increase <br>
            <b>2.</b> Fixed 7% yearly <br>
            <b>3.</b> Fixed 7% first year, fixed 3% subsequent years <br>
        </td>
    </tr>
</table>

<h3>&nbsp;&nbsp;Todo</h3>

- [ ] Find alternative measures to quantify the cost of living accross campuses (e.g., CPI, 2BDR)
- [ ] Compare local v. standardized adjusted cost of living

