

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=8bcaea9af4edd6edd0074b5b2efd7de80fd688dd0aa907ded353f41c9a8b4883&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=c54cd7299858d388e18a7f7219e1738718b886c627d82dc4345d71847208ceb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=4c8e297c1ca8f940aed37f5d2cb92fcedcb7cff47f8eaef40559e9e288d93608&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=8b531e9530b961845ea0418881d38f5c7cf9ab32877a05c44566abe00498098f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=861cfb19fb6ae4827521c9f6cf01ee7665b3acf908755abd0f15915dc3ff06cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=70f389b5003d495097a275e7d2b61db719fd998187011ccb345469c697e6eddd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=b8665ffe7f1816c10e72e5dc0ec3b3df258a7fa112420c15de354efdc935aa56&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHENW4RQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC2wUKvDtojPNJV4xnKtTI0OxNKhhALN2O2m6IC1vy7mgIgFOmwm29okXh0C4u9oUUe%2FXOfJX7%2BuNgdHjsCrF3arOAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDEMJWIWwhT9uxnQa0yrcA5PKrYjjhMVEQm8s%2FbY3juBsO6jHB6x18K5Sy5GiDu3Q0OlLwJIFAGNEYXMHk1m4D%2B0bZtL536KFbVsQaZVsdV8lV44vDs%2FY43xxnT1%2FyW1SDKpJo5Y6nwHe8ml71FtgurI036KMtUUfdFwawns0I3afymMDpVrLJhgCK3oerS%2FtLoelvqX%2Fmz%2FJPpwutrSMdQkPkb6Z%2FEAkH021KA%2FBmwrVzRFRR3hbnByE24id5OC48oqGEcOC5OPYyG0a%2B4SrKjTY9cLWH0C8zRFd4YyaqZ3HdbLXNPo0WXOSKweqOSR0h8Xh3x6tQIB%2BNHnmUdSdZyBa7x%2FR8GKoLmH0LyYY9I4TAZiV%2FayqHSZnN%2BIeQnySANA%2BqzYVCHu6OtQM7ifaYa9MMkgfxcoaQpcMPidDxiD6d0q%2FU0kQSPwPSSqDwPWZTjapuNdE%2Bzg%2Bl8I7it7xu4opMfK3UsKilY8RIhIi5AtDZobRz2SdLj%2BbetBMOTxybZfvVkyZ%2BSu0bG%2B1HVf2yu7bXgTZliPKJ1QF7CwE4ISEJ0Dv3vZ3kJp48GranLqQyyMnHLbL0CVDsEAWgSHdHM9ISzjmrbxM9XvWaokOsv2PBTS%2BwEYaSFoBoz9RF2UPU8mfLovkoof1IHZdMMX3hL0GOqUBTjQb4PSHj%2B%2FKGF%2BPhELhC%2B5ZcU43S80qboa5LU8yOxzdaakz%2BCPjdGqaGuUZmntkmpqhAXbiwP%2Ffvkg9I%2FbAxwgSIoAUcmgmM0TIfVkgEKWN6J1Pujgw2GRMnFoxeVsp7%2FZH3pJaCFyDwKLC6HpwqUm1WJQ18PGh65CmpOxyIrHZGvtegu0SAuVE4xQnVwdqG4BdjSrUedsEttpLlY0tb2X5wXFV&X-Amz-Signature=4e8a61f037c5229704c1143a073f30cb3555d1466c4ba307c915224ce644df2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSDLQPPY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDF6NgvVsAajazZKfMNJ%2BHF8MZPrhN4lMMR63Rg99raeAIhAJQ2l5msTI3UZIubTNMhYdbrENdX3%2BSWWxBIa8QsoKzIKv8DCB8QABoMNjM3NDIzMTgzODA1Igz9OCc%2BJWGM9Ho2sAQq3AOE0C8H4xXZDQXzCQPHPznp4gs6Pk5xCRcz3jLHNvnOmMAnLoJIvTJkDU%2BrPId%2BljaF1Yq7TjiT51%2FuNXoelkhkEmjCfNOC3Z9qUdSyG52m%2BOz3ipHbXjJbdX5ZmmuQlhtO2Kndsi%2Fbi77lA6TVXuLcw0%2FfWRjMiafasulZAwVLtTMkB3UAi2IPCJXdxyBsMAiO2d2YQXhRt8NISTCho7SIrlJjSpYk8DsLOLoSnyq00M3GB2ToRvk311aFXg8cujPsG%2FDDjmlq7%2BQiQA0fEJYwiKXcN9XVCBGE4mY8Ils2h8T3Hbjx1%2BbLxdViDNHmaNKH0G6xrb1rZfLKVylMM7r%2FUncPnL1SFpW3XF7dZTw52pVRGUnusarYUeuH3%2FE9GQDah%2FgNxebaFK2ej1JaizeXFKqV3DHtGTbmzGueVcUtQ2jIkF%2FTTPlUScsPuczjc3H1U1aaw5CGefsLtUpGTSfFBnxT1DXtErgoBLL45MhNMeZS3DdKWq9tCtrebeYT4lRrHTZu%2FmckE2BzJxg%2F9UUwR1M2kBvtv%2FhjcTfvj4bOaKtTTNBDwgTU94PmWZfIXjaapTgD%2BMDxfUDmSUmPll%2BvgWxeYRxVtpLsI5MTo4rDNBSSQGWx5%2FAa%2B%2BztRDCc94S9BjqkAcRhIGd28AgmuRLA4OivZj%2BUHlJbqbwgA2VSlJwhQMr%2FIgj8HLt3UGctV0P9f3%2FdUHeLxJFjYCkdeH83kB9uHVw9u3Zg6oeasXYH9chHjyi%2FKdGkhwFkaog2Ff9iU8P%2F1bKsiInS%2Br84VUKR%2FEw6cELBPs%2FbGVVwNH9Qk9imKKKQlr8EkIs231VvV6Ft68IvLwsT4iZnn57O7436%2BffUCU1rO1yL&X-Amz-Signature=fee2e73c8bcca4c802978d8ce3965c112a0e4835fbb87f4c3d016b1b4a4dbf93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7FHXUEG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDjridS0QQKnPH5ue157VMCMPvpaLLGgH%2FlDL0zDojbWwIhAJ2DbKL0eK15txSLww3W9TfUrUvzcdKGPVmt33hDiHdQKv8DCB8QABoMNjM3NDIzMTgzODA1IgxXh1gvpmh2m21GN4oq3AOOSpViqw4pKvKsc%2B2lb%2BgtGa8aOhQtFguvki0ZfgdUcIBVOV7jNFa%2BeuIcEPQ5NObBUvAMK7TMYmBh7J98SVxFdMtXQxyxUmNYuMpVRLs2erPaxqeP2AM0cOIUzDbpDnb1clx49RZivArvqrgWxDC5ceReDH9qjMzaNUfLMwvavMd6hPKtN%2BoQqMrQ9BqsoJwQ%2BSVSqIdExVli%2BZLpQYMNHNzs9NQdeKD%2BCYCqfh81f6v4DhUrJLicF1lam%2BOCxBy7OUPDmrG9iu0%2B9XTtNDfhEJL6gcQI5S2CRwrUi1sjeEunMlBQNNdTMkenjFuo6esk9xciD2YMabGxje5GJNXBMzB7CMzYSOIngy1GOwJTOnHE8lm84tpKm%2BkKeY0PYIQPB3CYHhptT1113%2BVQX85Jnyz%2FDw5XVdglMiRT%2B%2F2EZj474z%2BkigZSoGekZyiox4UpZ7cqqtMcpwF1%2BRlJ3oU6g23ziLkC4gTL%2BBqhzXL5fLcdoiNJDlUdheCwfmioMas6Hc60fF7H29SnENLcVL7tu60abqp6n7IpTaTrnNiT8SZi5Nh%2FZIV%2FvOTxaezJWOfFgklKifXnJfhOIcFm7MamdNyamTHZMUPBfg5wZ7lxZnji8Ej1bkC5zP6x5DCR94S9BjqkAWekO%2F%2B1xBn0Nxu%2B5AR1X%2FZI%2BaWmxsdiYNtEy0iAuk6f%2FRhrpc4wyhBqOz1ruE7iRzCxkZsRm0i%2BhT2tX3TNvL7uUndWs1NFI%2F9ROTvVrn1zzbOPjsALijOhUu00NwOc1Awmd1udCu%2FCxDoVAweDR5r%2BTzmajoLorm0Aet0KPE8uaSCI%2BPn8egWuuScbSnahGJX86cWimd7aZVFZ1DJsWem%2F7DsR&X-Amz-Signature=36396abf134430ba2d08f41f00b88f2c8e6038d4ae229f1c26de4f434c22c6c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAF2LU72%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC0UbC3B4MMkeW27Wr8ojjoZ8AOBWoFUdoXTa%2BQ1jQjmgIgZ7kE0tMxKkMz8z65jwKH2uUcyWtdwfFlq3R63Iq0VS0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDFqhJLRI3S4oaBGKKircA4x7hW5VA71vM9pOlHT7gzxVSPpX9%2F8mx2zTPdOgp%2BtI%2FZMlsz%2Bqif09zs2OOgGobhxKPMPR4hbu292McMduaVMR6qm5xkmPnXHQXdDRXVB7h7WdZeoJ5nPi4ZrY6Q0WeE7pdRcGfODfc17ArSCVe6A869t3CYOFzx%2BohYp%2FWCpYzo2yQzBDNl1yRKOWqBiAA%2FrzBbZu3pdV0fG9dEX4dpbqfAl0Wl6PV%2BraeTPErZ1zn0jV%2FZ57sxNIzfx2wpJWChXkKfnYbbGT0RxY43ioXG2ssJkyQVc9zMBsfaOblD04MHQwoIxV7iKx5lCZqYUXqma7QAnbhsBECdzRfrM0BrFKXBPGzEt7NYgqafhWditKDJwQ5JAENgZ7%2BEQtFafBAJOwJ5Ru2zgPux2Pk0g39lQ1DHYnWnqr%2FgM%2F%2Bjd0pYbl00%2FlKRN%2BJC7GKaggpbwYlh8vWYECcPxHKCHiT9p3odf%2FZTTwSvQyvvBmeaXPuptwoPDy2MnKYKlNhuO5ftQ0eBs8HSHHicr%2FJcm9b7C%2Ftgk2T1iNaPel3FvgWSWkwUXyBgIl3f59v0rUDw2EMzemoeND5pAkr1rJluYotVkXQNKHWg1k2GMZsGI6U1nPUDMEUlOJiVlkL5LbxojOMI%2F3hL0GOqUBG1i6NsCtIOLBJStyUoEPxAKb1mvIpMyt6SoTlcrzCMiZeCOdGlS027dzsITTN6LCMcRC24EY6HfwrcqR3%2FODnH1gF47vZ51xp0spqnwFhUkas%2FNmTouYXZWAcnH9z706ldDOiciTZ8mF9Xo80RM3MvfLAx0WiQgUrgMAtI1YRGUwPn3nL1DfrwIkOyFtY0ncjrIMHNToM6drpwhcR5SuvtbrSTJt&X-Amz-Signature=bcba394cb776ed4673c05aa4c266338ddede7c93b7f0c7db2b5bc282f83d7c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAF2LU72%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC0UbC3B4MMkeW27Wr8ojjoZ8AOBWoFUdoXTa%2BQ1jQjmgIgZ7kE0tMxKkMz8z65jwKH2uUcyWtdwfFlq3R63Iq0VS0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDFqhJLRI3S4oaBGKKircA4x7hW5VA71vM9pOlHT7gzxVSPpX9%2F8mx2zTPdOgp%2BtI%2FZMlsz%2Bqif09zs2OOgGobhxKPMPR4hbu292McMduaVMR6qm5xkmPnXHQXdDRXVB7h7WdZeoJ5nPi4ZrY6Q0WeE7pdRcGfODfc17ArSCVe6A869t3CYOFzx%2BohYp%2FWCpYzo2yQzBDNl1yRKOWqBiAA%2FrzBbZu3pdV0fG9dEX4dpbqfAl0Wl6PV%2BraeTPErZ1zn0jV%2FZ57sxNIzfx2wpJWChXkKfnYbbGT0RxY43ioXG2ssJkyQVc9zMBsfaOblD04MHQwoIxV7iKx5lCZqYUXqma7QAnbhsBECdzRfrM0BrFKXBPGzEt7NYgqafhWditKDJwQ5JAENgZ7%2BEQtFafBAJOwJ5Ru2zgPux2Pk0g39lQ1DHYnWnqr%2FgM%2F%2Bjd0pYbl00%2FlKRN%2BJC7GKaggpbwYlh8vWYECcPxHKCHiT9p3odf%2FZTTwSvQyvvBmeaXPuptwoPDy2MnKYKlNhuO5ftQ0eBs8HSHHicr%2FJcm9b7C%2Ftgk2T1iNaPel3FvgWSWkwUXyBgIl3f59v0rUDw2EMzemoeND5pAkr1rJluYotVkXQNKHWg1k2GMZsGI6U1nPUDMEUlOJiVlkL5LbxojOMI%2F3hL0GOqUBG1i6NsCtIOLBJStyUoEPxAKb1mvIpMyt6SoTlcrzCMiZeCOdGlS027dzsITTN6LCMcRC24EY6HfwrcqR3%2FODnH1gF47vZ51xp0spqnwFhUkas%2FNmTouYXZWAcnH9z706ldDOiciTZ8mF9Xo80RM3MvfLAx0WiQgUrgMAtI1YRGUwPn3nL1DfrwIkOyFtY0ncjrIMHNToM6drpwhcR5SuvtbrSTJt&X-Amz-Signature=3fb1bc9889c43d502e2ec911a637064c3acc1a3f207752f3986b750e2da765fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
