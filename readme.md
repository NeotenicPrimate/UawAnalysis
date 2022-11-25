<p align="center">
    <img src="./img/uaw-logo.webp" width="400" height="300">
    <br><br>
    <h1 align="center">Analysis Team</h1>
</p>


Objectives 🚀
============

The objective of this repository is to analyze the available data to inform the Uaw bargaining teams accross our 10 campuses
- Berkeley
- Davis
- Irvine 
- Los Angeles
- Merced
- Riverside
- San Diego
- San Francisco
- Santa Barbara
- Santa Cruz

Our two goals is can be stated as follows:
- Base Salary Increase
- Yearly Salary Increase

There are two ways we can implement the **Base Salary Increase** and the **Yearly Salary Increase**:
- Standardized
- Localized

> A Base Salary Increase without a Yearly Salary Increase will cause salaries to fall behind the cost of living over time. <br>
> A Yearly Salary Increase without a Base Salary Increase will cause salaries to lag behind the cost of living over time. <br>

Definitions 📖
===========

Base Salary Increase
--------------------

**Salaries must match the current cost of living**. <br>
A one time increase of the current salaries to reflect accurately the cost of living.

Yearly Salary Increase
----------------------

**Salaries must be adjusted yearly to reflect the corresponding increase in cost of living**. <br>
A yearly recurring percent increase in salary to reflect the the corresponding yearly increase in the cost of living.

Standardized Increase
---------------------

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

Localized Increase
------------------

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

Analysis 📈
========

By how much does the **Base Salary Increase** and **Yearly Salary Increase**?

UC Housing
----------

- This analysis can be found [here](https://github.com/NeotenicPrimate/UawAnalysis/blob/main/analysis/uc_housing.ipynb).

U.S. Bureau of Labor Statistics
-------------------------------

- This analysis can be found [here](https://github.com/NeotenicPrimate/UawAnalysis/blob/main/analysis/usbls_api.ipynb).

Summary 📎
=======

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

Current Numbers 📋
===============

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

Todo 📌
====

- [ ] Find alternative measures to quantify the cost of living accross campuses (e.g., CPI, 2BDR)
- [ ] Compare local v. standardized adjusted cost of living

