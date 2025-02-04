

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=f95f8c2744309c9df159855b28af099f69ec2e8ad72f0bd6503b4a99ba4b7ae9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=0693a82aca020afb3d5607dffb4aaf9e752ef210fb408c5132cf2d5b6f729aac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=9b34e1458ce9644c65b259cb92ef3acd66dd85c9e6bebe43fc8039f40274578f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=15b6de73fae2852ebb57e71f8770003fde7d215a05bcf07e4514320e2ab68199&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=4d171f5d59d4961e79d60bbe3283936083e8819bb78c7dbfc158f5ed034251ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=2b633b7d6d22f913e72190faefa4ad3ef9a29308a5c5fcdfdd9064baf1f01eee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=aebeb55962e43bd97d478095a2dfd7f80d855e17b70fecdaa0b6c130bf2d4727&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ERMUFMO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB0ErY648TQHz7gidNKBPDX8shLxkt%2FQqK4f%2BWj2O%2FtyAiBtWrXrREZEEzrQIbjPAA9PXeZVV8pTk%2F4w5NzLMWA00yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMc30NZSQv48sqwWLJKtwDDnjWvqaTNU3S6vn%2BGyJ%2BPQABqoBW9u23nModeYiMbC7bpmaj2HyKd4ueNR6cAS%2BugZrQ2fFB8fg1Vj7MX1zp%2FXkUxR%2B9oi9wygpJf1fSAswOqhduLHgDmn1917MdEIepg%2FXQsg%2BKo%2FQhlzXQu96KAs3ClnUTymHwKLI1Omk7wMQOkbLTz2xuVSaew7GMfXmJCyXDPfuKTcyk8wWsTRtlP090fUT2bXmMYTNwRI5ux4hDAI6HEDhV3t2lFMQ76kUvoyEq7IVucV%2FCCsez20I1FMDjCUewIxxecHGxMhh2WMtqHTgDVU%2Fmea9c6ifHPiwLomPUFjDdRV6QjXUWuVjWdWx0yhPOhuTFNZ85GqlYLwybNMZ1NwCaBy8Yr9UBEoRQPSfxzvZ0Rg4ZMfpYd%2FOjNDJVVrcfZgKvsND%2B6dk9upZinc7zOIFhkDbbulhqS%2FMdQy767EGET9M9QcY%2BsrrI6Q%2BkrT1yZvsStcILSy2wHQuTfuYkDKWBq7z0oAt%2FUpADGSngh2VRYZKfhQyfZg1biYcinc2rKdT4hl3tDgzvYOPj4Zk8upIR5ebTz2e2%2FbYjTg2f0rp%2BTZMdFK49HfYn%2FAlMBloi9UnNmMLbRQAXO24lbjyMWZbuLJ6lhVQwjc2FvQY6pgHtcHboBXoq%2BLtxTYknptPRpLr4z8z2rvx6IZIwcTYthCMZA0nCkLngGisSp8b%2BzpKBOGYqySr3o2Pfe4CuYLkg58473GKPJAUUVxxNbTcNKIguYSuWakuumfBxYMSBq9D0r98stPW5pl4gkPb0TdMlq1zswdE4cHq0DNmdSUUo9OgyOWAsvNV3aKAYs2ASWf5imE56vrZOY%2BMRxJaAo%2FYORwitALmr&X-Amz-Signature=bfcf835007aaf8814a9e6a38bf3d551cb02ee1469363f3327b2bfcac06f5798a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K6ND6ER%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIDHsqewi2VTofwOzzC9uK3soEG%2FLY7S0OtTr2XvNZ%2BfaAiBvexCDH0rDKlAfdL92uVjbOkDQ7ck5wyPvEUuyFyTGtSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMOzX6w4zWAwiwRUVQKtwDeCHxGK7fOlpeUBbpDC9RdHoWAczna0syj0WBZKuZyJJIVKuD49X0plYbQz0yeB78U%2FoVruTQVJHl2ByfZOYRENkGuQQbJefA%2B73u86ap2rxeeLcArFCNfPuFkwUjL5rg9fl5wPA4K6m%2BXLSfonhRCLUgm%2BpyJ8oHqxyayAzVqctUGov8mqqSohr%2F28ShgdxfEDqZDAB6ENTb%2B7%2BpgeaZyrzMa7IfkyfD9%2Fx5vogP36EbLRrY9gqBUsaQT%2B7nYtOfa2N4%2BJbyIECrFgrHasjtaa%2BnW8XaAj0kiSOW9T1eqMTtyoHRCnYRWHUa2YVb%2Bhn0HetjXwcOmPsEORYFVKZO7pf%2B9sDOKo%2B9jOy45qFJ27uHxZE%2Blsm5yF15DmKJqMLevCCawjy7dh9qh%2F7kV9ucIP%2FwdgSq5l9rnSNP5ckXkyXY6DTrA9gnNMWTdwvIA0jIWh%2Fw5gjFkp984hyawnKK7%2F8NCXudHAWaPfteAiXgGDd2oeNtLunQ%2Bjp9df28phG5yYhmcB5DOKtImVUuYgj%2FsvlK%2FhD2e1S%2BKGqN8psrkNyMf5jcBy%2BBGJ0zxEOU1iq679OKlGKFFtM9nbTaGbzObFsIwMIfQo4x2f%2BllbPpgAYi1rlsQdivY5LuwUkw78yFvQY6pgEXF%2FbWGlrOLDTE8b1oM%2BliucoIZXnwhRMteXOtj3u84kkDoHvJ0drCP%2FfxdjwlIMNAqsAhisbqX0i8A28Y4kMeyfdDSye1P3OW4JJ4qSxIrV2SfnaUEU%2FFEr8fmeNu1IHhmgYZM%2FZIWfIaecomSB103EoCGu4RUp02raRClCOGptwP8ZyaHp8rzZutKU%2BezMpvyOywK6mN%2BnbLul6lfoABRuktk4ac&X-Amz-Signature=088a6a1762361bd363feeae0be6f4fb4451118987011926c6ce0ff8e61667f45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT5XG4OJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIHyTKu07McbMxIGr6kfhZqjSLnbFU5jObKh0VPq82UUlAiEA37nDL7mWZOy%2BCRyh8M6skJjP0GEVpsez64Y5WoUnx6Eq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDNw0Co7mK2nqIGnKdircA2nvxg4EPtrI2aGargtI%2BMoim1VRzkTulynQhLZ%2B3IfP8RgQvQ7DAoOlqsDu8TqOkQCdkHip682hg3f6VC7GaZ3u53GNOSwOhnNqV70GryG2rkhFOu2Xo8DemC6PFxiIziThJ5BFt4vvYxqPyKzXPQ26ZaxVcStHOqhP9e2Qe6oIvRgSVgWKCr2FfAG5YOliq%2BuV3iLCRjLhED18ux2JUohvHxcH0HSG8r8uJrcQwa0sNCue9oZw%2B9QFtgHPASnJAzGQgwB%2BIwNIBISSL%2Fzp2gyll0EZHWAfSxQvRDLF3NDKUdCYk2LdSVDviBjAwZqIBUMxWFkKb1wbZBtnMbriSInB5LQO3IWK0GeQ5sA8S68JnBH7q2LozUA1pae3yY7jKLPdG26pTNbIxMYvq2H3zropt9Xh8Tr2dITT9HM8FMISvgrjaS5d45My%2F5K9%2FJXYZfUYqVkbQvmPw6X0CUzfjcaQl%2B%2F9qMsmm%2BEEAIXwOMHKI7HHDg9wclUWV1AiVsVzfSWrTxN0fQusO1R5TyxiKZRSs7BNKFsTxLRXgYY5MRZ0w4g9BozB3dGkAysv1I9Ygihj%2FGJJAuhxfHU3jpI6f0%2B7Uw5rTMDtJNZPP36c%2Bn5zGoQH75pZFvxJUd%2B3MKDNhb0GOqUBG%2FKygKMS%2BrzHuMX7JRifskHw6FCPmWtL%2F819y7qd%2FEcgkk7sMWpCO8i7g6A7QcwEKpRmfQ0ls9CEeiA0TCkYhXUaVDXIXg%2B1bbhUZ2ZZcixp2C7ROqmsGF8phwoZefI7BCqe7gFPJwRRoKcUiScWjnoPBYoJKjcoRRtdmVrS6Vlpxt%2Fcba6hzoqXwlNOiEVssujBLYYru684Y916YFCqOtej4Xeh&X-Amz-Signature=73d92f304aa3d97695f4718c087655b591cc42c85e7dd413e080d2cc0ed0269c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634LV5GPJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIEBBUOvb6moHUWNN97wYyOMdynTNzLWlu43IA82DBvNzAiEAyFE%2BfWQ6ZIV4tfFk%2FgE5Jgdos6I5xbC9cMeFr3ErCGMq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDIXJqcr1Z3bcHqeGdircA8JkRYPhMpX9VvmyUD938R%2BMhXVMSOMgAf5S7%2F93UZ4f0bnJBOss%2FpMnuW72FLy2LGvdnUiGct0UtEq2McJp%2B2ApBV2yndSrJdFz5ZPdREt01PHGFc9SiYapnqxlAoSY9OGxjhDBrUhLSPVKPlxCcSB2FhSPUAHHC8P1lxE%2BLBA4Vy6%2FSwJwwk5WrIREBHH6Vbd23BQN%2BoftGht4FTjaJbloOsKqM37Fw%2BufQiivghJPLwTOiVtsJjut1UkEjXWZtAmIr0BPr0uOXCy8%2Fkj%2BXpLzY7pDKl9aO49TSQFtt27p7e%2BMA%2F3xYJo9Zs9NIrJlA7qlEpXc%2B0y5nb%2BN5zm7usj7cUz9D9%2BVhQfqUna5Nzc7hEo17d%2BRwKGk9atux6oRXqESNcgCrpD5x27kL97vacYF54fVD4VqeUOnZPjYkCMu5mTmzToRyRwGMy8ZoTlc1VLzbjCH0nFCIIiqLR2Yj%2Ba0xll2aA4tCU2AnWY%2F4tjucRWBI%2BqF4ZsJAzM84yR%2FhWIdXwxStkuoa2YvzOxXwgZCU%2FKVoSXx6D7uhp6UbbRG8y%2Fqmkdul5njYdBnacTZQ1duZ8QipRFaCzVSQLGA1JPQlrxLP0KdpJX0X9bl4C9XX1LobgG%2BZRWVpPdxMOvMhb0GOqUBt%2FkkGP9CdlMcovtQD8CSeUJzO2jfU6r55BgzAksmOJ%2B0R77E0hluOakxmNCjAaN5rV4NWMC6AEieXwjL7eibjWd5%2FkCDCGgGuwAd5C%2F3IvWGoJ38obD0WaCP4pmFNd2Ehnp7cVv9S%2BYsvAjGrAHCLbCYVw1uRbb8xnxWpnz53%2BDNsvQu%2B3sZeq0asgw7nLyDYWQhJBIJHR3ar20SqcjqME7M9YOx&X-Amz-Signature=c279c6d953194e0bfa86834b549561f0e6a4377c81847a493e48229404a7e77b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634LV5GPJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIEBBUOvb6moHUWNN97wYyOMdynTNzLWlu43IA82DBvNzAiEAyFE%2BfWQ6ZIV4tfFk%2FgE5Jgdos6I5xbC9cMeFr3ErCGMq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDIXJqcr1Z3bcHqeGdircA8JkRYPhMpX9VvmyUD938R%2BMhXVMSOMgAf5S7%2F93UZ4f0bnJBOss%2FpMnuW72FLy2LGvdnUiGct0UtEq2McJp%2B2ApBV2yndSrJdFz5ZPdREt01PHGFc9SiYapnqxlAoSY9OGxjhDBrUhLSPVKPlxCcSB2FhSPUAHHC8P1lxE%2BLBA4Vy6%2FSwJwwk5WrIREBHH6Vbd23BQN%2BoftGht4FTjaJbloOsKqM37Fw%2BufQiivghJPLwTOiVtsJjut1UkEjXWZtAmIr0BPr0uOXCy8%2Fkj%2BXpLzY7pDKl9aO49TSQFtt27p7e%2BMA%2F3xYJo9Zs9NIrJlA7qlEpXc%2B0y5nb%2BN5zm7usj7cUz9D9%2BVhQfqUna5Nzc7hEo17d%2BRwKGk9atux6oRXqESNcgCrpD5x27kL97vacYF54fVD4VqeUOnZPjYkCMu5mTmzToRyRwGMy8ZoTlc1VLzbjCH0nFCIIiqLR2Yj%2Ba0xll2aA4tCU2AnWY%2F4tjucRWBI%2BqF4ZsJAzM84yR%2FhWIdXwxStkuoa2YvzOxXwgZCU%2FKVoSXx6D7uhp6UbbRG8y%2Fqmkdul5njYdBnacTZQ1duZ8QipRFaCzVSQLGA1JPQlrxLP0KdpJX0X9bl4C9XX1LobgG%2BZRWVpPdxMOvMhb0GOqUBt%2FkkGP9CdlMcovtQD8CSeUJzO2jfU6r55BgzAksmOJ%2B0R77E0hluOakxmNCjAaN5rV4NWMC6AEieXwjL7eibjWd5%2FkCDCGgGuwAd5C%2F3IvWGoJ38obD0WaCP4pmFNd2Ehnp7cVv9S%2BYsvAjGrAHCLbCYVw1uRbb8xnxWpnz53%2BDNsvQu%2B3sZeq0asgw7nLyDYWQhJBIJHR3ar20SqcjqME7M9YOx&X-Amz-Signature=0201e059ba632f5ade431f21ad0cc6ec3c891dcaec7653e18e45d158cac0c678&X-Amz-SignedHeaders=host&x-id=GetObject)
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
