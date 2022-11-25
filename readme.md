# Uaw Analysis

### Objectives

The objective of this repository is to analyze the available data to inform the Uaw bargaining teams accross our 10 campuses: Berkeley, Davis, Irvine, 
Los Angeles, Merced, Riverside, San Diego, San Francisco, Santa Barbara, and Santa Cruz.

Our goal is can be stated as follows:

1. **Salaries must match the current cost of living**

This will henceforth be refered to as **Base Salary Increase** :pushpin: <br>
A one time increase of the current salaries to relect accurately the cost of living

2. **Salaries must be adjusted yearly to reflect the corresponding increase in cost of living**

This will henceforth be refered to as **Yearly Salary Increase** :pushpin: <br>
A yearly recurring percent increase in salary to reflect the the corresponding yearly increase in the cost of living

If the first condition is met but the second condition is not met, salaries will not keep up with the increasing cost of living and we will just be kicking the bottle down the road. <br>
If the second condition is met but the first condition is not met, salaries will be chasing the increasing cost of living but will never catch up.

This poses the questions:
- How do we implement the **Base Salary Increase** and **Base Salary Increase**?
    - **Standardized**

    The same **Base Salary Increase** and **Yearly Salary Increase** are applied to all campuses based on an aggregate cost of living index agreed upon by both parties

    - **Localized**

    Different **Base Salary Increase** and **Yearly Salary Increase** are applied to different campuses based on cost of living indices agreed upon by both parties

- By how much does the **Base Salary Increase** and **Yearly Salary Increase**?
    - See [[analysis]]

Thus, the questions that follow are:

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
        <td rowspan=1></td>
        <td rowspan=1></td>
    </tr>
    <tr>
        <th rowspan="1">Standardized</th>
        <td rowspan="1"></td>
        <td rowspan="1"></td>
    </tr>
</table>

Let's define each of these terms.

### 1. Base Salary Increase

A one time increase of the current salaries to relect accurately the cost of living

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

A yearly percent increase in salary to reflect the the corresponding yearly increase in the cost of living

<table>
    <tr>
        <th>Current Yearly Increase</th>
        <td> None </td>
    </tr>
    <tr>
        <th>Proposed Yearly Increase</th>
        <td> 
            <b>1.</b> Index based yearly change <br>
            <b>2.</b> 7% yearly <br>
            <b>3.</b> 7% first year, 3% subsequent years <br>
        </td>
    </tr>
</table>

For each of thes two possible options:

### 1. Standardized

The same **Base Salary Increase** and **Base Salary Increase** are applied to all campuses based on an aggregate cost of living index agreed upon by both parties

**Pros**:
- Ease of implementation

**Cons**:
- Campuses benefit differentially

### 2. Localized

Different **Base Salary Increase** and **Base Salary Increase** are applied to different campuses based on cost of living indices agreed upon by both parties

**Pros**:
- To each according to their need

**Cons**:
- Difficulty of implementation

#### Todo

- [ ] Find alternative measures to quantify the cost of living accross campuses (e.g., CPI, 2BDR)
- [ ] Compare local v. standardized adjusted cost of living

