

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=24f1c8487e769c1a4a2a3feeaae62e903370999a4503c7661ad25322aae1aa27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=56b73a93a6ee644169e8a39de7cbe2cf2ef62b36b1c920a396e82d4f10ed70d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=2a9d1ed6f94ad45d10f4c7cb155ff5a75b654329ea32783642c0c74f27fc5402&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=b856d23ad9c1a82b1e2fc4d73ed1a0f6b480020674b00d37351aebf3e5aa9d82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=fdee9a223e9608f5a4f2ad621ffa0ca7fcd834e6ec2b09093525239c7d6acdfe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=6eb495f383bcfe951f7a3e949d48d2c9cadb279d03c19959a27e0d5e5d7a1f95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=f255f902e513ce1f2d2ce9e776e6df1b6182715f02439cc668cd9aaebfc6b256&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5SKVHTF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEjZzMe7lBKV1cMaCcSTzrAAOQSmhWVFyWFQ8c9VuOwnAiEAow%2BLTZU7ls2Dp8AE8BZWI7zeMcqtD90UHVqb2MXu6uEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMC4tM%2BO8qODFvMKhyrcA0kEX1DVaZr0R6x2vuZzuW5n%2BTo1dERpMnshrm7vEhp7TeVvpLSQnAyeppWSy4sZZ20TIf2Wo0Kph3fGxOHrcz0GfmueZJqHxqWY1b%2Bb4dL2B4bE2cg6pgyaZJqGOuYGc3kbWkjXHWYKjf%2BQl18iEqZcIXtyePKv90sECixKNs6SCh9XdlD0UP44GXLd2YLbN0VKcHICx%2Bwd2Q1SbkPy%2BJeO7%2FUdjvC8jTmLUE%2FVoNhIwQPA8bFOVgwZl0lK4YzlOwZYPJfNH3tUmOWOixpcxl13DaTk2s%2F7xpLDgiCPmA4iT6Ieqn%2FyOyAzx5OU5FukUQo7YNTYaageTtFq5tmlJWinUzpzZGzNWFp02%2BscvjiokZvDViNyRJZ9Ggz2iwfUku4q3TpRwmW8L2vpnC2CtXJS1BZNQuX0jprpJsQPxLus1FNG5xQ888x56%2B68CKQ46WBw5ILwGlnXrTgpUb084928Zw68OOkavxvMhFehPabyS6gybR84PkX0WngB2db7pTs9C%2BsWX6X5VEWpt8xeQrpA7MxfjbttvEDSV2eiYbKt%2FfoOEa5XNP2XQH8kpFsJXP%2FhyKnrb%2B%2Bd1FgpkYxFIfip5wT4SiiqmMN5bV66Xv5T1XOZ5550I9bQJ7g0MLu4lL0GOqUBCpsLR%2BZaZLjuRD1KnePQWU8aeoDbsiNPyVWUe%2F2%2FCHUwwHoQ1iO80RZuwZj80OT%2B6%2BJbFOLKBc9%2BClYKGgSUoIjj4oRGw0mmeN0kN8zVffzhf2%2FU%2F%2F0GumtEIqNNZ5YT8dD73lTq1xgpFe%2BPJyOWrtlT0BfYMpgt%2BhMwgtNiyNUfoWU%2BF%2Ber8%2BBclr3ELuNOFtj9FbtZ%2B2ydkUV%2FapUtpPCEXRbu&X-Amz-Signature=755fc66240dfc3638b2307b18d523d9bee69f5cdf8c69572c424907e51f563a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3MGO5EY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDuOZoGeBYHHgQp8pJFITyx5yT6XxPN7tCqJqSxT%2BMxogIhAMUvEJIwR2Q3LvHIQEfsXQBaQtSrWXRUyK3bAahSTJilKv8DCGYQABoMNjM3NDIzMTgzODA1IgxRP3eCbzEQ1lLc%2FYQq3AMDCj%2BciUjsc9DHBOb90QprZwHAEzXJXmqiM0pyi1rcpc62Q3M%2BSHuSNYsjz%2BOYHEYl4T5aLx%2BrgpoEK0niMaDL3UqiHD15cb0feCEi2eCjJ%2FC%2FjkzINc1zHxPS3iJRPFOfq%2FycqOV9FPgu%2FE%2BU%2BYQfMtcNytc95OXJYQhFNDBCMKwlOUPk5Kdjw08hsX5frG9xqF1VElgZ3MRCZ4zlTPnPju0zIz25dta4jKGeE2Iemv%2Bkv7RxBkyvyElegMODUGbGyhJ51lgp3GT9lpXnYzBHo%2F8y2ac2miqbb%2BUecQCpyPj1Bl9DraDAx5WyIkvVlK7dAit17%2BmiJ70bBNqZDZ8KnABGJU3EaGe9ur4ZQmluNB0ip2xvcIYrNYVt%2FOchm6YXRh98AAPcVvHcIaYOnIpcTyp4b9ymeWUzozD4PmsZYHi6Wg5o1AyXwM5gJuYK5JllCQxg6DgFOaWO5CO5wfU6LAH617wHloa%2FdyjlP62VHoD9WpX4rNSBwpuLneZuLYjG2ZOc8U2KrYU2QAyI5s15sMoLYYMtr1GNZziumS3%2BozRTOd2ZMB1S44ifn6m%2BB%2FsEiNxM2tksF8oYGv5k8Dt%2BY3M294dYWPHkGmz330qrLwyJ2keWeKaYMRqKUTDKuJS9BjqkAdRxVvRA8Izuo1vC9Td6r8mBVbu7%2F%2BhZLgXKLBjXMUh142Z90D3FqmN5cmBxELlgpJTE3H2%2BY6qdKCx7gXT%2BSBy0xSLEVfy%2FL54LR%2BA9hYpSgxXQq2HHRvPf75O25hI9qp0WB8VByM70Ibf1toDtu5FeBovHbT%2FNBy7sMJtePi8eIGhXJGAsocPAPvB9J9h5MAR8De4XFBfRrVnwQdB9Nwltmyb9&X-Amz-Signature=12ec4204fa1a3ca9a39c01e8244e95420fe0c3c60d591d3d1debf9175f0bcb83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWEOYZ3Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDv9Cm2At%2FgivdPB8o1M%2FYJc4wGpzYhLnk69I4qQqCukAiEA0ZA1BiSGfewD65x2H5beq84ApHPWsLvPb2hamV4Bj0Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMtGwq%2BfaR3xFRlzESrcA1n%2BbMKLJ46KuTMhbNt9yPOWlsYMxw5jMlPtoHaSuU1vRSRqnRoHx75f93mA89zfd6wM%2FbmO39r6AcYv9daAtrf02gBmKQx7prOb14ENSjCyIuxtchlxWx4hxPvCAFJgaJdXuy7B%2FYEfEpo%2BwAc4QxW7BczZEfEsdwJQicgXC%2BAOwwahgT%2BxII4qyde36znseRbonZ3b6FPGnInF9CaPLIfl4504Rx0qYljLpuwJUPHcyZP32e0NWtv%2FD2jHDdv9qt%2FSPY7p5su3oRmL0oO9OXp4V117PS%2FzebOSEcrS0HT2fPLfR1O9Oe7aWpWwtVoG8IWAF732RZEN5SlypytKQ6TTGmwRmK8dCsJ6kKZoBAYZ%2Fj2euktRW5%2FMufbCzCXtWyidamupB0VAU%2BWhCce89UQW64jePlp3ePKb8ApJOYQ8%2FROJzggxqlSjwrjjxWVMG347%2BlVMTDRADsIbtpHHkqc4EuJMt5fqZefjwuMUhEZoA6ccUaf7Xgwb6Px821kOcbfnRMvCZMAAz5ZOfJHY6s%2BL4%2FQCVqxbvoca2Pz21i6ZFCyq2ReQpVPSQ3xBu2WIMNHgX7XvRTdeJ1y68gFJi6z33UwJOsh%2FbZ9bQBEuvKrJ2Lz9rO4AMG6%2FLgoKMPe3lL0GOqUB%2BsvaiTDxv8rypYxdSUsC2y5afFHhUpz9FzCx%2FqBeAgL4QTvkADVKIFqC341jaO%2FH%2FZsthYaPyrKG2ouXDoX8dmGM2xM99x1uRHYNnt%2B%2FlOjS%2BAmaSvC31M9eSl%2Fj4wJO1%2B609SlbSG4iHSsPJIvI2g7EysUnaswwE29o0hguTocrh6NfPSum5kM%2BX696lX1upVFD8wKtjFx6TmKaDvZRmL9Ue6jg&X-Amz-Signature=e272068929fa21b90c79d4d8506c745dee7439b8ca4120f002ea1ffbe44f4ad8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGGVCGH5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHV3JJX%2Fm5QyNL56pL7lcqUBZXzb3nW%2FIbCNY9FzX0sVAiEAtnBNeqMaqLMnhQI0vGTdyYPwA7q2xFvJwyaSu%2FcTYO8q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHFroUMYq2%2FkxPIQhSrcA5WQKdo6TaisFUlgJo%2FqUXGvxCRBUGYQe%2FpUKr1KmzVJcOrQkUFrmdg41HiHaouUWxVn6i333eSvMaZobr8upt0JVaa8jUZNmjEpdOubRk2SsC%2Bh%2FCCmp00F2sdWsSLe1eQdIJ89hRCbB5zemuaaYXGMEAqc1tqOLzWC5qFJSwX81%2FGbvmvCQRq5Z8lzqG4RhFuQrRs0owapMtjoRAbFJLX6DAXr39%2Ba06oWV0yjSn5aRpKU7VFdAQo0CO13rX1IKukTMWKvsjz2uz4xkOrSDF1GUf246JDJE8Pw7NMpBXzXUbUINqdPCFUBllYaa06uDv%2FdXoHneiPplrlIpWuCt7zWtV%2Fml%2B5N81wEcIBVMuHHkpce%2BeQWv7ZLPanuuJJG5NEqb3fq%2ByZUCJppzRvIreD7C2EVXXiStHNDdEcLfqVeuB5I9XDoarO%2FjlClHMDI%2FVk58SijNjk%2F3%2BmcftT%2BV9fkAIetMPkp%2FdAOrj0TzThBxa%2BjMVwqAgYSY215Rwvt7utxC%2B%2F2k4uyBPPKSgXziUymacq1vkos0NjWpEqwTzbSF4ZveztJ7XIAJKyGILfELNDe6zaPFRCHvgKz%2FLWnIaaNePA0lb5CzrD8bAxxF92AavSXGAL9Z6LriaCUMPy3lL0GOqUBmfLhuXJLdNv9rE3OZ5k9IQvwrkRtW9iJ3kSWlkarRnS3DzXFlDz%2F0XxMAHkiWYK92kpUAoMBlTWObgj2FIloHlkfyfN6srfVc4JvgqIlafrH9KnFlzcyu91eHBEymTzxAy5oW9LsBy9f6cLjtdHWT4%2BchVBKS9%2F%2B%2F50lEtmrehQfaVCrTD025J8uvQJ6UsIGIuBGkHzaCihMD8DbsG9lYH0qMXJ5&X-Amz-Signature=dc100e2b69cfbe08ff4d791d4f725a389905bbe0e3f6f76c313bda353ffd14f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGGVCGH5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHV3JJX%2Fm5QyNL56pL7lcqUBZXzb3nW%2FIbCNY9FzX0sVAiEAtnBNeqMaqLMnhQI0vGTdyYPwA7q2xFvJwyaSu%2FcTYO8q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHFroUMYq2%2FkxPIQhSrcA5WQKdo6TaisFUlgJo%2FqUXGvxCRBUGYQe%2FpUKr1KmzVJcOrQkUFrmdg41HiHaouUWxVn6i333eSvMaZobr8upt0JVaa8jUZNmjEpdOubRk2SsC%2Bh%2FCCmp00F2sdWsSLe1eQdIJ89hRCbB5zemuaaYXGMEAqc1tqOLzWC5qFJSwX81%2FGbvmvCQRq5Z8lzqG4RhFuQrRs0owapMtjoRAbFJLX6DAXr39%2Ba06oWV0yjSn5aRpKU7VFdAQo0CO13rX1IKukTMWKvsjz2uz4xkOrSDF1GUf246JDJE8Pw7NMpBXzXUbUINqdPCFUBllYaa06uDv%2FdXoHneiPplrlIpWuCt7zWtV%2Fml%2B5N81wEcIBVMuHHkpce%2BeQWv7ZLPanuuJJG5NEqb3fq%2ByZUCJppzRvIreD7C2EVXXiStHNDdEcLfqVeuB5I9XDoarO%2FjlClHMDI%2FVk58SijNjk%2F3%2BmcftT%2BV9fkAIetMPkp%2FdAOrj0TzThBxa%2BjMVwqAgYSY215Rwvt7utxC%2B%2F2k4uyBPPKSgXziUymacq1vkos0NjWpEqwTzbSF4ZveztJ7XIAJKyGILfELNDe6zaPFRCHvgKz%2FLWnIaaNePA0lb5CzrD8bAxxF92AavSXGAL9Z6LriaCUMPy3lL0GOqUBmfLhuXJLdNv9rE3OZ5k9IQvwrkRtW9iJ3kSWlkarRnS3DzXFlDz%2F0XxMAHkiWYK92kpUAoMBlTWObgj2FIloHlkfyfN6srfVc4JvgqIlafrH9KnFlzcyu91eHBEymTzxAy5oW9LsBy9f6cLjtdHWT4%2BchVBKS9%2F%2B%2F50lEtmrehQfaVCrTD025J8uvQJ6UsIGIuBGkHzaCihMD8DbsG9lYH0qMXJ5&X-Amz-Signature=dc2749fe8d461ebdced0f378a5fb6e20800cf5f1f3dfdf6a9d41c2275c71731c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
