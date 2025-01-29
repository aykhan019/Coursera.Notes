

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=3e8181a580c77632295e2d6f458172f1def6cb940b4e4df807545f0d2afc5024&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=5b0ae3f95a2a13c8ed70e4ca59f4f7c9139e432ac68ab8d86debcdfc47ef7a62&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=e615d58c829fe943c63669e0964e5e8464fb02cea3e6a06852a0d383cf62c664&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=7b3e889391de2c457ca025769c8d41a5277e911058b7abc5f3bd6c0be5159e15&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=dd6a2d724ce1346c56da989285d67911fd08fda1d2d0735905614f74f3fbd3ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=692b00155a8bc0d58148548e76aa8c6d24623b85086a26ddc529ac310715ad3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=b664a64eba64c6bc31cc1cbaaa5e0440da31d6c621102b3bd087cff8af104e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVEGMU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rb0cb%2FhEOJVcSaHwSNiO2m8HG60zPURoSbyKgMH7tAIgC7KA1tcNdfzzMtED2528axCVIzZny1FlfrMxFlGrmq0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCee05iz%2FWpMUYv1SrcAxXA2J8Nt1hGxRhYpSGeOshXPQiL13HE7i9epQCh%2FuJc4GstuMt1G6%2F6r9CK%2BIT7OM10TXe5XH2LY5bVAbci2ZMblbkssOSrpwa5tEvBrZUqRhkCsoZk0b4hLfTi2nVJ2QUuucIFZEy4f0aC3%2BhVco%2Ftie7gIolWX0f6Xhxutap7mH%2BXZXiu3mO7cPhvxZz38mno5psNWCimMPi2ZmLCmw7hOB0sJPmagDlYAzkFpCggwj52Cf%2BITgFJn81MIoTPFCgoZPfw404C0bS%2BthNTyAAekJb3EgPq5Ey5oMYZ0GuuzbghlhysX2ohtYDUpoeaTk0d5Ki7a8hG%2B7vDGR4pLdNpwmu0mFYOxDS8PfFddk5PKiFys0ld3JDSX44F5OtflypMK%2Bz9qXIBcgtf8dbxsDT2q1VPKWhPGX37GwSTqH68DNXx9gtidVy9Mzuv7Gbh4gG%2BNyVER6XwYGWCsAf0%2F8eBwwPe0h1YL80TP4VC2L9QQ4QfEWM5ZUovouDhce%2F0kM%2BsPGkyvzIQQL7VRpNckcktgEVOv82H6XwVpWnTRcKon4nWfum8hYL8H%2F0uhnQgjzwDm5leirIVpOrMYz%2FV4hpM6H2y%2FtvQh1N%2FeJfYGR14UPS%2FZiv8HGJkV1PXMN%2F06bwGOqUBZm0MEbsMpxW6FV9DxqUJr%2BJ1q8fBsVi33mgW1xbWY6nlRRt%2Bnxn153csQQLDrO1L%2BhHGg4JriJV5FgEpftoXW513fPoHc7a3odBLe3fcIen1qRejBCrddfBm5BNMg4J24nIgv0jAD75oTEAfVirdzNRSTJmW4bapqMefmSOdO3o53MXh6jyb9uBxT7ZCVZsDXqP5M1U43Pi%2BWslp4DbsQpOIaap4&X-Amz-Signature=a7555238be6d27bd72ff6bb6a3ae7d39e185c101283cd03356ffb3b090baf12a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPHM23KI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHm1OP4baQOvIhHNauFnRGEBHodLLmN%2BTlaAVrTogqngIgHAywa2HlaH8RiIgtdBc9u1xAY3j9hTH6jjuYhrPZd6sqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnFjpp9Muiejd7kPircA7V3NpYt4%2BW2iDO86B1kTO7%2BouxsBjauvjFOmE%2BmW9io1yxSIr3Yq4edehfEWY77bZDDxSRNIsTh2z5fTPGhK77kqR4B4qzKc2n9Fy%2FC4QqknV4RRaMZEyaCyC5elJXkEqd81nRjc6sDAjg9FOWwiuuj%2BGO0RdzJuXK0f4LwsMMyrQU2Z10sK5Ba5goFkBFfX2MTRPWuU5vphsVmHdxcDkPBqLDSX8fLao39%2FYudZyUioUFsqjX%2F3psgs8DfFDAsAuQe2zX%2F2T9dj9m%2BFh8GhJkARLwDaGsG4tqnCxnNgOOpOKfTyZ2mFm%2Fakd6Uy3SVyEzAFbqVOCYV4S8LbGrBJAPedodv3Yuh7jSHZe62dGt9%2BpaF%2B66EuQFJyQKk835%2BBDZEIpVXBfQjKGdLJ5FgDqSkfytVWz705tcw08nM6Fx8Kc3FLUlkyEktvCy%2BTLgTeHD8BFU8ZuNw1XKrxiTcy3rn2Hp%2BV1zZPVUgnIhXV%2FCFfCYT1WzNvyxQV218u1jVn4JEku%2F6zqKV3iBlpzH%2F6N%2BlZ67obXoZNYih5FpXCdQ%2B84HTvYMHIRuME9UrGZTnr6beifuF5oCHPaZlgtLe0%2BWNVsXVuJmj5mQmTe%2BmCeWhrPuESsgnD8xOJcw3MIz16bwGOqUB6BzlAlYwTXCGvFQyJLCiy5Vwf0IflzInH0ykbfyxQ6A%2FCzQyHX6gC6bM%2BgHTAijx91F4MYf%2FoAFa97tYqs9ZZYu6xEYIoU9F%2F2r2DHZyZ7tuTujaoPRr3z%2FnQ96XR8J1dlXZMHr5xfz4lKEzDXnNU9pI8MXsS0mzuKoFjj63Xly2IHveLjevdgV572gYtwQiGwgjKhAJNRicF%2B%2FkCjJRcyWEeXJz&X-Amz-Signature=1438435d2f3f6de0ffd95abd844b8aab970175d89b5474ff9dd8c9d8f74687ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ECATIWQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICIOj8R3SLg4WwpvuLIRczGGK9Ia0N83HUjBF7kzldZ9AiEAv8TVPrHuN0ZVG2gkvbUiEs7j5AvZeT9PS7fpeaVdIM4qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsgJfPovYUBdzCV%2FircAy4K3Zte9iVCs%2BhLbUASu9anWY6BQ4hQgbFL47LJq91N4vBoM6co3xV0ymF1xnOk2r1YTEkTlgt48OWy1SX33ti96I6C%2Bj4uH%2FP1kPSF%2F3uia9A5ZT5omZW8FH0Wp3DtBTbhSMSLCl3RR3z%2F3siFgQP7uj%2Bm8L3OZjtHr4DuA1Ls2P%2FxO%2BJQS7uzUeUG6Cj0K1e2VEpOXhldEXABcVSywxReJ7V4ER3c5bjhNgQDmq4FXzvRw8zzN77M7cyVyPirRQkDaXF1vr9nD%2Fu5dVkJPPKGgx9gHlGk2vSN7D272ZG9bvfxVzNRNyfHKfx6wb11tAgyTrdDH9Iy4bxfEoSXZXAYnn5Z1Z1LPGjA4fLhD5EK4AhYgytHjvhEpLnPyJr1P9orAgS5bTrzJ9brtUjs0MvtAQOS3lEmAiwTDSxk5TGmf9T%2F9yFXM%2FK4uJ4aUfMzv7ctPqe5%2F%2Bc1dlmHpkmCQ4e9c%2FAsno2%2F57QwJL70aXDBapWQ6Pah2iIDEApCJ75fQKExxpxV1hKDcbV%2Fgqzr4QkFW5ci8EzUB%2B8NlGlYkAzKfON4otjfBOx%2BCZMIHKOiwfkHiLq7nm3uFW1weaR%2FD98M%2FeWw1HiOO5axggP6RjSIpfch5dEy27lBEnK7MP706bwGOqUBjr1nUm2sKDyBFEkog4Wn0K194kBKXBf0ZsooXlAgUDsKSrAeqoZghVR4zaMjb61wkAVluZDyC%2B3SAadZ2DWvJekRzfu0Vct0zpYEvI2pnyweE0GoaKZWquntObhSB6Gjh8zF%2BFEHpSquZRsQQs%2BPhWobx4loZq1Wezsz5%2FB%2F71MY4TpSc6CcUOHJbRd25NIvBJKR%2Fkx0hk0%2FdCQCYeDDdms8ymYL&X-Amz-Signature=b97ab505cf6968eb6bd7f72e40a0014d50b9b605ab095ad219f2ead13c078cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEBP7PTX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDz%2FIjEKySgjQdCAzcqVdCEZTAyZRyK%2BPiG8yoNQqup2AIgXAy030OL%2FCr%2FsyiTM%2FILuomVLKqRApriGEQzwbVkInQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIWzSgBxhfwFOEJ%2FyrcAw9ZcXcC0Z1ctZrbX9X%2Fmc4MN58b1TaFF74lPPY065fotdDoyqRXekfnVjRtLsxbhcsKGGmHlD%2BKjFkKUHCt5d%2FK0ImUA7PaEGqHssO9Y0Nat0rs%2Fqz6xzBSdGURd9VZlohcXnNNP13pSoXD3lDjZ3%2BLd99XbHhCfoK9efTuVrR27lA%2F7SMvJ8r6dnTAq8IIURDGGCbns8SizYV%2ByTLCTlkcPv8dmI%2BwJBI9d8B6ksIi9MfdIK5RVoU224JUgP%2F46EDzNPERVOdJcobEZNuRBNQbb6v7JXWF%2BNdLFw1gvQL20f4b5UsCtKKpI4YgW1ztKFkVQlheW0CG5fyA2hYk5mlyCveVMWqNfBhVg38UluJmK3VigZTKKwKgJPCrdbInCQ8OM9pK6I%2Bc3qKMQ2b90KNnhXtcDy%2F4BMdEsBrGyxO7GbZxEzFLwLJy6UJJsWEuL7E%2FcW4B4YNlQzpvh16X20Pbg1X17ojO%2FDHfxbiIrT57oLvb7yYnC0U9b2krf%2F8hzMEZcbcG17Mdmnm7fGni7xm17MQVijGULSp81pC3%2F3CzGzH%2BIdZazeKy5guvs5QZes%2B18%2BQOiLxbxzBui1hQeOL1%2Bp9ccFASO0f98b0nH%2B7odLK1jEsPJPD9TFVjMOr06bwGOqUBQ%2B%2FhjZbXepD4WeD8lHkHaU3YPZlPUbLFVk3wPVs8ZVQP5HbmE9StkuM%2FS3zwUorUaMzwYRWpRZMaoHR2UOzEDXs2vZ9JBYQ9ON4KROqw3jRAOZfFsPtP88u8aPTsgBlAqt35Tn1f6ZsLHi4iv2mZMBMZ7svHCRM1f6%2FSs%2BkgKXr9fIonNzujFAvvA5AHbC0jan4GwVpiYidimWc%2FqJ1zbleIvITQ&X-Amz-Signature=27904d8136157b5e76b8587561b5e916d02aa821b543f7100fe15f7eaa77eb7e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEBP7PTX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDz%2FIjEKySgjQdCAzcqVdCEZTAyZRyK%2BPiG8yoNQqup2AIgXAy030OL%2FCr%2FsyiTM%2FILuomVLKqRApriGEQzwbVkInQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIWzSgBxhfwFOEJ%2FyrcAw9ZcXcC0Z1ctZrbX9X%2Fmc4MN58b1TaFF74lPPY065fotdDoyqRXekfnVjRtLsxbhcsKGGmHlD%2BKjFkKUHCt5d%2FK0ImUA7PaEGqHssO9Y0Nat0rs%2Fqz6xzBSdGURd9VZlohcXnNNP13pSoXD3lDjZ3%2BLd99XbHhCfoK9efTuVrR27lA%2F7SMvJ8r6dnTAq8IIURDGGCbns8SizYV%2ByTLCTlkcPv8dmI%2BwJBI9d8B6ksIi9MfdIK5RVoU224JUgP%2F46EDzNPERVOdJcobEZNuRBNQbb6v7JXWF%2BNdLFw1gvQL20f4b5UsCtKKpI4YgW1ztKFkVQlheW0CG5fyA2hYk5mlyCveVMWqNfBhVg38UluJmK3VigZTKKwKgJPCrdbInCQ8OM9pK6I%2Bc3qKMQ2b90KNnhXtcDy%2F4BMdEsBrGyxO7GbZxEzFLwLJy6UJJsWEuL7E%2FcW4B4YNlQzpvh16X20Pbg1X17ojO%2FDHfxbiIrT57oLvb7yYnC0U9b2krf%2F8hzMEZcbcG17Mdmnm7fGni7xm17MQVijGULSp81pC3%2F3CzGzH%2BIdZazeKy5guvs5QZes%2B18%2BQOiLxbxzBui1hQeOL1%2Bp9ccFASO0f98b0nH%2B7odLK1jEsPJPD9TFVjMOr06bwGOqUBQ%2B%2FhjZbXepD4WeD8lHkHaU3YPZlPUbLFVk3wPVs8ZVQP5HbmE9StkuM%2FS3zwUorUaMzwYRWpRZMaoHR2UOzEDXs2vZ9JBYQ9ON4KROqw3jRAOZfFsPtP88u8aPTsgBlAqt35Tn1f6ZsLHi4iv2mZMBMZ7svHCRM1f6%2FSs%2BkgKXr9fIonNzujFAvvA5AHbC0jan4GwVpiYidimWc%2FqJ1zbleIvITQ&X-Amz-Signature=227f04b4ac279496d01cbcee38b35f033323d0d07f94881aae9de6f66f624fd4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
