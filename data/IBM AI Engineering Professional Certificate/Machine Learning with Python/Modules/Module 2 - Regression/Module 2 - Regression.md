

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=726dd21b7ff92e6b7cd49ce5d2017839868cb6045fba7aba947d15c1da797c44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=bd8791e1980307db19f374d7c0feb2987f5fc535e54546ea910e2240fb845b82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=0bee47e9f0c3337ac44159a6a4332796d255c3352298c8eee59f1c9f07f41116&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=d2a6e35e33c9d9783c74a8028ee302232846356c6513a441100537659f256d56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=fe8721b98ebd286393df6a37183952fe78396d70e84bb002909ed9ae1bda27fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=c9cda667edba0d31b2786c64a3ae38bb97e31b099d8a623b2adefd2266082144&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=a04abae39a2197f8a933474701c00ced3d813dd75e567931fecbdd3fcc3d5bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZCSSU2Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAE%2FUswLn26UXEqo7V94oojhmqklcASb7oTuqfxbMpDEAiAlcysc6ubhZ4u%2F9wnoXmI8Q4W29u3E4AH1M7hyTN%2BRoir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM83rVZSxNwM9eql5wKtwDAUtUr9widcHSgMxiFyMaIPGWkw8Eh3yhXegos%2BUdAtsZLoCkBr64krgUqLlccH4HCqHuMagSG15MOGT7%2FHIptm6HMwDfGnhSplMMGnSpUPDE%2Fke1No1UKNgxDjzY8PFa0U5EG82R6ZwGUUyiRD2A%2BTea0HPCRHhgbB6NZt9TPHfwjCjiMCWDUWcteorQh3yUARGWt1CN0MNRu%2F9M7F0no%2FZSUSoweC3%2FPu2S4y5NmduIGJ3VhfdUig%2B%2Fj4az7idfqr%2F3agxm%2Fu8lXYHyBy7GGk0KzDL1SpIQeG7W%2BiTrwj%2BU82g39oUfStcJ4cjotdM33vFV5G2DrcnZ1qmS3FfQaj2pnsxSHL7fFhD%2B6v3FB4fn74vV2Bd2pH2V%2BDUfg0bGuuy2GbUWVyzxGBCeUDpsqxvusNO%2BMqhF8L4gl7aQ4efT7ho2T95nua3xCm1Y92CElOkOXfWBun4EDq%2B0ZbPNb7PapEaAazp6XDt0bW59wyEOuD3yhlzqtBS6f0ZXn9Wd2zl%2BE8we6%2BKka9UcOjAFS94J07G%2B6S4HxJOgdn1t0anrSnqjX1O99H%2FC2NMuG38rMDLzosEs8Q%2BTmh8EX1T6%2B0CjqEHwrwMcNh6%2FSCRclLQ%2FKGzXHLPBU2FQ48kwl7iUvQY6pgER8yBYvDoBZ7QJ9zerU4Iu7nu995%2FQVVzH9Sc6BJcLDEqDqsu2yIk%2BVS%2FUjRMIT5tHL%2F2T3n3XN%2FgZ3%2BgqEQAqacgJZq%2FB4piy%2BwUab3sYuh8%2BaAVwbWrbsU%2BpmmK37bMYk%2BQyq25RkTxSEfOrPMZlzRlF8%2F3wr32aiy%2B%2BOqHr6dj9a0hlbNtcG%2BA8PLEs9%2FBJwjqZeDrCf%2FVi%2BHNkQanMgtxdwAZM&X-Amz-Signature=c76a9198caa00bbbf30cd0a047a11fd00a386fc7ba46c53b02996e5311476c60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHNDZX27%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIH2vxdFz6nqGST6fgavUSXODdc9leREvZQ9%2BjLF513UCAiBH7VZkJ0Ra4bXTTg8Sq24lNIo4wpCX%2BdnkhQiwR0Mt3yr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMzj1Vts0byN5z7kMLKtwD6EkKwCbaOXYfQZd3wBWf2GpQyv2wbzzwb1qwVhkc734VzGTZV7Dd0KeWWU4neZVw2EiromSt0Lu5L4VmJ5j%2F72kTo2Se5tPFG2V5%2BptrHInqA5SGmFw5TSwVNsLkxNkyAA9opshlpDbmQYYjrDfJgGClywFLeVwpNGNKRYxXRvcgdmO%2FNIDFNHfH2tFoMMgzcPQszIujjPZjV50lU%2F5kBwUqc6fu8cmWJAYtjUHqzdivuhlz1UqOrw%2B2PYpMcNN5NcvhQDrQTy4Ril13CB0I0FMcTwqo2lSUtdwcykGDL45ZKYRTlQ6vB%2FAcvdEBISRPowfk0azYx8P9oLtSqrYpJNqJ%2BuZGcUBCLUm%2BTMCqx8SCBvqQDBVzeoJnDs%2Bqlkrn%2By6YM49Z1jgUFvGJFqhXLujcvqw41QYeeW8cICD47LYeFHZCyJpeSLDi18KAhOgZXXgYgD4ASR8IZ9ujLqoZoDeMEac2tZ4YfhTFVknX%2FLVqzvLL2baLgb73NpoqEFpvWOnxhfxpTb2%2B0qI%2B3QE09tog0b%2Ba11JJyTwaWmP1byNDcKwDZ%2ByK49BGmqkSCn4oalA%2Bm4zKbAg7xTTDKRj%2B1X53laVnFvojxz42r%2FONZTiJryP8roRbTHosWVkwwriUvQY6pgEpx56EFYDpTY2xeML6x6pUCWVXK0CfrPLsCZ%2Bq1uy6nR9PwOMFg3KOpA3K7lhM%2FtWOwJr7BXYPfnuOLlNTvvBdiHViaIexwyrTYjST3Ig7Npbz2739dlqEXONU%2FS4qkpnnO6k7hAfa0B96qXdzZo0BFzFHRSuE4D8VfJLPbZ3opUwtC4eNa8tZZQeRM1MtSyOunX5ztma4GUzrI3p0PaVtzH0WzA%2Bu&X-Amz-Signature=bee62979198bebff6cae71f828a5142081a8659ed2e128fce657714ae90f6943&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSX6QMSP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIBVTAS3Myx%2Bd9SoAIxZsMsoVfxNx7Mgyo5W6pUXhcCdFAiB6S5JWvsNCEfulVe7xGefWN4Yu4dftzgClRMasi2zv7yr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMA8%2FcxkoJtoiMk6u%2FKtwD0tzgtMVNdFKq5MhRniX9kOIWoSxg36bG7EQLXUGOfWUtyhkkOVxIzrhH3hqFWK78hBx0DHL8aB%2FlNTcdsZBOmC3p7ZUuLJJJQ9Sy%2BCvLtS0lUEj%2BvKRKHhDqNy1xGkswkfiGzW3s796p4hOVyrAE0f6SC9Pvj5gduHF66ha4oNg318VmdiODEFsK1nzaN%2Ft0JXk94ELX5K6p2nVVglyOuizg2DQH31NnrN%2FvjgOWjCndcK0X0lMi6EYDneSAXH61A0k%2FjqwPfZr%2BPHvmvOuK4I18pCnnPH%2BbCMDu2AZkX%2FrIVZzn%2FhvPWuoDRznq1nPvS4d9GCgEg0Upl%2FBS%2Fj6p6Q2GxiUU0ON0mRhW%2FVViivfivuqdTDiS1wvSWkef87Ww4%2FJq5myPsKSgfySXPDbQSS4IXQygCd%2B3YXAdxwDUijD7RGytQvLU%2F8AZ5HEHNqAPQ8ttvd0%2BYEb6BVps8%2BgyRc0p6DOl%2FDXo65diibNcF9EUUjZpCKvUl2mq26WKM0FR8jiozW3EAiaW04Xq%2FiLVSeKrn5W%2BG8wG9e5yVs3FBKh%2BV0%2F2Qu3m211LZ%2BpoBUSZdr8KRuBUfO1wSVccqT4DcBrfUmmD9h03TrUE1WhufGaKU%2BZ%2Bp%2BMDyLIKqYMw5beUvQY6pgHHh52dZr5JFAm2u9wkt2uLfYVaqLwkE5KrXQzV%2FBgNXfihYdhLH7JlEXJgsrWuTLJi8ms38kPdsF31zoK9h2%2BuJgMdc4JNGgzUko5I3j7eyVHlPKmK2K4nXMCRR8MKCbZtYFgbyABbnmLD2miU5ZwqkNd5uc9y%2BIPCtPdd%2FpGhT1vn6gju5YfeEF%2BD4xprv8aCK9gdFx5V%2BrZiHo9Iy6ZDwoQc4waT&X-Amz-Signature=49cc76e5992ddbfe5b48063c304ea7f87c4924ee3e4a414f94f4f1844ca188ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WQYDVU5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIGzFec1NVGUvjYbcI3Mb4YwOsNr5A2FDynvj%2BoRCg4feAiEAonbWAYvGhLSFDVH0lWnkqOPEEmLqGU%2BbOKL5dtjb%2FgQq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDAwBcWIzsnyFXZ6%2BxircAwuUGnOvxQ3Zwr3qxqNNcAKQ%2BvfW5iJQ%2B3s5S23vSn0nZfpb%2BZk64o4ZhPBIjs027g8t4%2B9b3DWXeT4wI6fTUAaUJFGI6Bqp%2FudlqUrwiBvIAqmFsZFyejw2tWYss1PITb2lejIekPcmRwBYWVI%2FXacST0TJgKCHlESliUoMvcdurGYZEuh%2Brf%2FJTUUans48LmY%2F1xTmhoE5fdg4JvAWibu57W0iZDI3n%2FNrF9WoYKi7CcZ8bX%2BlKZWwy6ZKjaAD%2FGcsdo50cfskjFI%2BHuLxbxJdirQ5pe27Ypirq9%2BDu7Hnd15Wf%2FE4nLiaT%2BrIz9qVH58OKTOqoRwsU%2Blsi09wopFT1eYdbqimBoNboOVY51QmxL3NtikYROgs3SzbgUe5YeKdaSXNRvvG2BPDhikYoaDN28QZeKXVN3bmk%2FY4WL5upWyZA9Y0zRffujle88ZKAR57i4bb32qUBfbsWFzY3HIi20nIdRhfU5Z1ueTKRKeYMbP2ydVltsicb1VLGeHzFt%2FUyGaltMRN1biD7ub90jMYmDe%2B5juef2jYzvfBheL%2FIwuNcup9PdNGUZ93CWKJIbpUsP%2FIuSBd4ItdGnsqKZUgSraIoRfeMEWm9frYVexBK61xUYooA1tMjBcCMPu4lL0GOqUBfanjyYVvw7FOu1cbR7gkk%2Fn6s8b%2Fdou3dcFAx9LqHja98fyilzbB5RwI72LAhSMmGtxr824nxzYtWXiFv%2Fa0VKfwiatPRcVfCwmauLvh7TNa638M9SB0%2FklO4i9DcZJvPxZQCAn6C%2F0jW01MqyfzEnBudfW70L630jizGs4mdhRmUN%2FZVOFc2epG29LMqAKr36BfEXISFHS2SBkOI%2FbaJisFGl4V&X-Amz-Signature=17041bf10ebd48f7d92b4926781975f53d676fe487af54f62188501d71741fae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WQYDVU5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIGzFec1NVGUvjYbcI3Mb4YwOsNr5A2FDynvj%2BoRCg4feAiEAonbWAYvGhLSFDVH0lWnkqOPEEmLqGU%2BbOKL5dtjb%2FgQq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDAwBcWIzsnyFXZ6%2BxircAwuUGnOvxQ3Zwr3qxqNNcAKQ%2BvfW5iJQ%2B3s5S23vSn0nZfpb%2BZk64o4ZhPBIjs027g8t4%2B9b3DWXeT4wI6fTUAaUJFGI6Bqp%2FudlqUrwiBvIAqmFsZFyejw2tWYss1PITb2lejIekPcmRwBYWVI%2FXacST0TJgKCHlESliUoMvcdurGYZEuh%2Brf%2FJTUUans48LmY%2F1xTmhoE5fdg4JvAWibu57W0iZDI3n%2FNrF9WoYKi7CcZ8bX%2BlKZWwy6ZKjaAD%2FGcsdo50cfskjFI%2BHuLxbxJdirQ5pe27Ypirq9%2BDu7Hnd15Wf%2FE4nLiaT%2BrIz9qVH58OKTOqoRwsU%2Blsi09wopFT1eYdbqimBoNboOVY51QmxL3NtikYROgs3SzbgUe5YeKdaSXNRvvG2BPDhikYoaDN28QZeKXVN3bmk%2FY4WL5upWyZA9Y0zRffujle88ZKAR57i4bb32qUBfbsWFzY3HIi20nIdRhfU5Z1ueTKRKeYMbP2ydVltsicb1VLGeHzFt%2FUyGaltMRN1biD7ub90jMYmDe%2B5juef2jYzvfBheL%2FIwuNcup9PdNGUZ93CWKJIbpUsP%2FIuSBd4ItdGnsqKZUgSraIoRfeMEWm9frYVexBK61xUYooA1tMjBcCMPu4lL0GOqUBfanjyYVvw7FOu1cbR7gkk%2Fn6s8b%2Fdou3dcFAx9LqHja98fyilzbB5RwI72LAhSMmGtxr824nxzYtWXiFv%2Fa0VKfwiatPRcVfCwmauLvh7TNa638M9SB0%2FklO4i9DcZJvPxZQCAn6C%2F0jW01MqyfzEnBudfW70L630jizGs4mdhRmUN%2FZVOFc2epG29LMqAKr36BfEXISFHS2SBkOI%2FbaJisFGl4V&X-Amz-Signature=6194caa3c78dcf37ab052f4d83ccfa5256e68501ead0077b355fa524faf7ae97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
