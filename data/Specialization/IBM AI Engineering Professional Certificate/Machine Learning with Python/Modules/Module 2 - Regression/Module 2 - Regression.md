

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=65a63a1f04505e9667a722afcb257632204285472c8d812ae550334b84189db5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=4070ba4f8552234390ecea06f9656260acdb76d97f97bfe028c7387c19b4dff9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=5f88ab5cee1c0022aabaa25e3f3838eaf79422c910120234fe499d43e6652a20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=fbfabff7159ce14e93023f123e4b75cf1bbb1dca338e6b1290730bad880c05dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=2283d47012e05b1d917f8d597ee8023a4166f2eee972e028f46a298645a52b42&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=3d8f2817f79a8dd4ab6cc0bfafd6eb9f88e761ed0dfd795146e91c5a598ccbcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=3b6e8dc3d4f45fb9f57598164bd739cca5dcf206f039312c461eb25f2f679411&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDJH436P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICw7%2BXViX6aQvC2%2F96wmCtp06L2QkD5Z40ZFLiWWU4iRAiBMG7byET4tbHcA506RToMAhZXvMOK7%2F4Qdk5PasthDgiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyfD6TTbe%2FRUPdv2KtwDdcvKYgfth4CZWdyx4ZZY6jDAlfg2zdkPMMBvcAW%2BtUX%2B2a62aeVq924LBL86eM9HQf7YjtSN0XJ%2BvzXJPqzLwBE9wUz8AQXe74Eqfz56FuuusjnAcijcxuLeFvykCJn4o1ixZaOeHS%2FIBlY6u4fU3ns4c9hJMTMIYABtMKb89KRSyxaogofmTdQshZ5cti2R%2BZqKp2LUK54ILtKAfO7qXwJA%2BcHEXAW6ln8BXXFivtBGS6XOTdfsfWSp%2BoF%2FsgZUnZ3xMxBt72s1fXLsW33gyLj%2BHq%2FL4M%2FNjFJ0pH7ruArkoPPN3c91hpnzEYI1Z1zxxnTnennNdr3XsX3MW6niHcTpp1iBetZXHv%2Fn62aZfku3rLozEzJCd%2B161z7VZsjMJnPXa9NVdpcP6FBtI2NerdwpPeTfbpr9aNO9ZcXOyoFGCSq3kd1ZGMjF1icGsQ07RmjMFUS8roCeuoOjhLstGikDGHogs9enznhhrfSFwPcNTKP0pVtu9vXXpFXiS3R9VjOs9EHieRDsBbVZJq1bYhWbLGILRpWY0gkeg2fLEqEf5dlA5NX03tTJORASfGm2dceYstYdk8QNzHWz5XQMPvEbRKkReCoOBOc9x2%2FhAoxP5gdOMhYGbY%2FZibowhpHnvAY6pgFDHvykT4c8Mmp9rKu5DRpDPdPacoFzWhCJWQzQqDesRZ10BLdGheZ9E2UkgNa5bhJWcigRoY6zEGiSqFcVVxxefrBh4QbEsInvulzpRXAw2Bsc7o2Oiwzz3mm4dLHcR6gMn27nm%2F4GIzb%2B1p33pPHePy0Vlu4ENYZo%2FytQ%2F9uRWdJ3ZnHnbTizXKgYo6lhzfyDG13ebIf39i96%2BLQrHF5%2BUXgwvFn%2F&X-Amz-Signature=37a3fb2f56c61da2617f6d7fe305e7dc6631542bb34195bfc9847e68541116de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ2SCEJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQD9o49uROuRbWtI5F%2BN1vjkwGhUb%2B5D%2B6gQEwsVrtS1EgIgJ3kmIgRZVLduuuiqBkGUogy6jOzkF4R1MoyDzcGGllIqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcbWhq2r3znPC76eCrcA3fnOORcsJGRjYZgpkRhNJWlbKSNKEbW9%2F%2FqND%2Fts8bU9FT9RHxxautUs4n91DFWIzkGIZE6FntXQfZxh0Guk1AahcHUIg8g5VJev17HtD4vuQK6rY0jsSWwB%2FK5ZmRzxyKk6KhM0WaoLrV18OMGwzA4FyKDGyhBOOolujaT9mGp0lDEBtgruT2HgmiWtCHxqsYk8v%2BmyB%2Fe4AzRysuSzxbPVp0AKwqrgadsX5Bu5gPal63n%2FNNk8TG35UOfpcOygwF7IrXTfvm5g4BivIq0zZoIwpt5jF1THorEGpuZXM5mNptMzShsPZK1bOcFXgVcOGyqL%2BdI3mU0Fa%2BBELSFn%2BoPqEfLDHEDHbivZvgtClvlGf8fNl7o2wSHGJfbdP2RHpRZ%2FUKggXjTofFcYbCq%2FwhTaKD%2FreW4W%2Fg351Wqilt6Ftl1LUYK1CHg5CD0rDC%2F3dJeMyLw1KRcJY0J%2B27xstGWESumLMz6y00jLjI3t31%2FYklLW%2FDQlQmLmF1O%2F5TGZzWh4D5onGCVUJ5EAbzxI4vbZoGwL0ADd3Tb%2Ff%2Fsok3fsxTvpEgACvHh7IFGCH8Lf5GNtpydv9XENIRz1gtjhK7b573qdapUJvalruAv83OzZ8KSGM0wk2dBWAVfMI6Q57wGOqUBgoSa7N0rBYljQgRJRcPJ9CQNFIIwp61%2BJ61GLt0MoklEKOm%2BJqqwl%2FY9RP3Pb2qXjQpeCaf3qpO0U7lN8%2F6FK67NuhKLmbWtZx94r5QpJIgZOqu4ktaDu9Ahjj%2BXxkH6aJvC%2Bw5IinUpqyC%2B7tI9AYa8eAY%2FwJRyFOAYVY8KbhWZwJoOWoGpOZ2j1Jubqe99bgAa2QMV4BGuV61OciCrCelL4olU&X-Amz-Signature=8eb643d5273dc47daaed62cf10e3b9164ea6accbfa7293e07b1b64681ea726de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAE7Q5PR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDnMu5UoWFiNZ1vtH9HGinl0gQJH7sGiIQPYoycPw8A%2FQIgVaEOK86wJmDWIoC6q9QMV60oqIkvCsPIKyN%2BwIsjTToqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuv0yRZtmJuM5B3iyrcA4JxopYmFKrWGnI4kbivIvO%2Fhf07zBdBeso%2FCMWKxQ6YEUNfR8ZS0RuIGFXypoFX2r8CGtIxE8xXiWowlqFN5ywOr8Uo9VVp7omYPCiq3iMPtjYSMnDgss2dL1owEa7Y8QDIUwN3d56x2yu80iC7%2Fg0O41CI5fBjeksAyBr7naKYflV4rmWDLHg92%2BtAqUvps%2B4hdpLqXcRD3lZ3iro7qSXexyHGwfhqrNWyhIxymIzchuODQEZVDzW2pV2q1DmI8zU7%2F753whk1VcKySrYzMl4EZYh4i0pgkN7xxyVsI1Sy2XOmeo7dOHHRQZcL5Cm2aGu7U%2F8tEFt%2FYPQKgD4sUYtXULWXRh1hyWxLtfXxbo03R%2FwqLmx0I4oxnPuiCImTNwku8XJ5nUu2nnCRplCCrKLH2savQYeSKTxGQFWAEDjTBr0eVk5LBePN%2BWlCgXZxH3GAWJs01lDOFYazV4CBVMTulvwfb8ITHn066RlgxFIrnABCale8miFPRrDzwVP3BvuCxAMidH6LOzdpwGKaf%2B5bXf3YOgdMDZ4roBskfGD5Gccbvlgs04WuwdFYAKjIYJsBN5%2FySEWGd7RwRZnkJAAtV5hRWK8MA5Eo1leJa8NMDf5VKqVQXPcnicZqMNmQ57wGOqUBuW9Lx5dtR%2FxDkNT3jbxrCaGM8DGMKW2237EseVN0TLTxCevPnrLtg3LfRfbkZpFwBzixOsHkEi1CvGIRDOkIecGhzhoY0fYDp7PRksChgDNAxXBhdeRo16kLh84x3Q5rxj8y9UYQsabN1IwSrO5lBcz1frKQs6zFgy%2FWciO8C3tI4II5vjdugJ3Ht6czX8PyNWp1gQqVthJyzo%2B%2B8%2BfYMoPlQLgo&X-Amz-Signature=1ceee9a92158a1794af70d4d5059b4a8d812e1939a6c4bb1dcba708c04bcb442&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPBYLADI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQC2%2BQ937d2Hm9RJX8s76L96S%2Fmi0EsX4KpYSSt7wVCUeQIhAKiVFlkblsGuBc%2FrgQAfrho19uWfx3hOhotpoUCWiNaMKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxP%2FCOLDYM3iwnIaPEq3AN7hT3fAK3FOCUKWReEvrOeGgt6sq8D830ydtc1Fsk8Vsw3TKUP%2Fk4zcgyBvA8RT6IFjP%2FZ7vETdFmZfCj59I%2FeiMZ0rlWHRdqYnkStPT1omEW9drWiZUNVzeBPwtLGJoB0GPqTGQcCEQixATmOW%2FMPAbVw8mYZdIkd8%2BFeX6qdg92UGHMTcsfwBRCOFDyJvBliDNu9HOHo02tv%2BrjmQ2uowxOS5egcIQ5y%2FZEVcT8NN8aSCOnxa0%2FI3rTbCEJt0AFVe9I%2FJBlQvYUAXH1EWdP9K%2FRYKVpRCBT58XRORlN8ywIpQyvbz0rng8vKyDXWgY1mKBzynnBQGwunw6fdyxcQmwK48oPZeCoxYaCTIAEjDET6mE09fsAS7DuGnqtrgHlgwwH9TYPUeNmTQOhj3lWcc9h%2BBbmi%2BUycEiZ3%2Fq2jJFDfQwaQguFT6eo%2FNYu5LOQC%2BCgLWCPoJMD7J1P4REcSxyDmjrpAK20Sl8TYbCk2oRp9IJaVc4iTD8bhs2dpQH98FeVsVZaDFsU4%2FNCSG1flGF1xvn2Uv1v762CIkcK691OuY2CK%2B1Hw8MDO%2BjCxEbNL0UOaRGkLXvfqpnRghVnn5fAWop2TRl4DCm4ip2XETGDRMBO9NmQNNLcYWTCGkee8BjqkAeKAm7POLVhd2YxYOxcY8OXhs12NnsBpyp4focyGChfhRrXOutR17P02hxLo14CAkb6p%2BCIjkGHfvw%2Fthw7qr8BTrIK4dFvqEZ%2FuKhV27COT%2B1Rw5NeA%2Fka1Tg6B67U0uj2Zil5uvRAWnGjTElcczGK3skJ3BhSUlEQ8XyUykfyWzOkBWqWxpUVoEcuRZYSKW%2Fut9UOHOUksufFHkWy2IzqNpRNH&X-Amz-Signature=53f04d2b0ee85c44e8e4eef8c97b6613c53b18e49d1342032e18f4159b2c5e2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPBYLADI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQC2%2BQ937d2Hm9RJX8s76L96S%2Fmi0EsX4KpYSSt7wVCUeQIhAKiVFlkblsGuBc%2FrgQAfrho19uWfx3hOhotpoUCWiNaMKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxP%2FCOLDYM3iwnIaPEq3AN7hT3fAK3FOCUKWReEvrOeGgt6sq8D830ydtc1Fsk8Vsw3TKUP%2Fk4zcgyBvA8RT6IFjP%2FZ7vETdFmZfCj59I%2FeiMZ0rlWHRdqYnkStPT1omEW9drWiZUNVzeBPwtLGJoB0GPqTGQcCEQixATmOW%2FMPAbVw8mYZdIkd8%2BFeX6qdg92UGHMTcsfwBRCOFDyJvBliDNu9HOHo02tv%2BrjmQ2uowxOS5egcIQ5y%2FZEVcT8NN8aSCOnxa0%2FI3rTbCEJt0AFVe9I%2FJBlQvYUAXH1EWdP9K%2FRYKVpRCBT58XRORlN8ywIpQyvbz0rng8vKyDXWgY1mKBzynnBQGwunw6fdyxcQmwK48oPZeCoxYaCTIAEjDET6mE09fsAS7DuGnqtrgHlgwwH9TYPUeNmTQOhj3lWcc9h%2BBbmi%2BUycEiZ3%2Fq2jJFDfQwaQguFT6eo%2FNYu5LOQC%2BCgLWCPoJMD7J1P4REcSxyDmjrpAK20Sl8TYbCk2oRp9IJaVc4iTD8bhs2dpQH98FeVsVZaDFsU4%2FNCSG1flGF1xvn2Uv1v762CIkcK691OuY2CK%2B1Hw8MDO%2BjCxEbNL0UOaRGkLXvfqpnRghVnn5fAWop2TRl4DCm4ip2XETGDRMBO9NmQNNLcYWTCGkee8BjqkAeKAm7POLVhd2YxYOxcY8OXhs12NnsBpyp4focyGChfhRrXOutR17P02hxLo14CAkb6p%2BCIjkGHfvw%2Fthw7qr8BTrIK4dFvqEZ%2FuKhV27COT%2B1Rw5NeA%2Fka1Tg6B67U0uj2Zil5uvRAWnGjTElcczGK3skJ3BhSUlEQ8XyUykfyWzOkBWqWxpUVoEcuRZYSKW%2Fut9UOHOUksufFHkWy2IzqNpRNH&X-Amz-Signature=1ebadd45bbe7dd45658140b38a61bfc2971466e298a21765ff892ae9c1df6723&X-Amz-SignedHeaders=host&x-id=GetObject)
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
