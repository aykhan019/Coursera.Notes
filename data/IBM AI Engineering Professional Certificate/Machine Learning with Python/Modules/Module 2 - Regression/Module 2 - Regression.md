

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=754b678d171e3b9cf84c7d5cc63b40aefb71769e4ec98dcf741fb4a881149dfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=f82e691f92b71ab9d89681785df8097ba430faf8b13150c45a8e29c44f458191&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=63275804988b32c1e07e2773fd06333afe3d503e20553689379def2fae1f29ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=ee0a30d1e0b6417deff7908d4fe9c886f2c460a467d1bccb52913ae171fe098d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=7c4bafc152d6c1aac54e0efa9efc6daa710acd4e2d641c1d96fc67905187ca83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=8a7cd9a60af31e5253e88278d9be49c7cfae1e22a1fa78d02436b74abddf1714&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=8b2bbfb2fce4b270fe6d7b2ec9f3914761fb47a305724d8a748a10eef14c3654&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVVI6VZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFT3NefFiwSq5%2Bp1Lblq3vCLldqjxHshbiAJfb7ID8OqAiA%2F10u1JAXFmfsme0HSRSOXZsfJMKtpmSx07fHH3OdqKCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMuQwx1N8X0sXngTcQKtwDvBj1HlxJKxtFeiktWmr%2FdmGz0DtP5q0j5%2F8YSm70%2Fnsd0YzC9cllJm6D4%2BeRB52hFnC6HFHy2Z6PH2UPV8P79p5qXIKg9ct4TShdg9y7AePFEHAyrQuW8pE0F4LFG4ky1HsyCJnCtZr4PKAZwNY86mIogsCvyOsWkn5UerI0p8w5IzZtZOjBeBC8B8VuQCBEJtjjDx6lPR%2Fr3GtxBzG3HKjGQj7LOuZ%2Fko%2FkZHK2KVsTN1BcH%2FrFmLBsTy6jX9YvqOQsH7yIhUlqHWAHhTcCxYNSRvzJHBe4%2BVFGpUxhzvi0ITCVW4cToAxeb9q3f0oE5n9SsgjmSBocEG0jf45R9V%2FuxJtJB0g1HGI8n1O6kjXVFg8LyoX0xg8%2Ft2wOwlMv7%2B5OcYZL%2FhQPoThYiByZ2chM8PXI6sQD25dQ8eBKmnPKFt96QFPsZjWhsKGxwuJLj94Jlb3NwFudTa4B6eMUQ9Qk3uzW28z%2Fgv40EsGtN6QPnDPYtYIPOwG4r0RarBeblVqrm8m7C2dgWQl4eK2B7YZ1QWPyB4wWwZzozEud1NiP5yTeqPA%2BP3c42IGnuVeQWpLe5QJ8bofg6bpO1iIAhcceoBu%2BsQ8ZwbTiN7CqapXcmB4RMSPJAprxFRsw1dGTvQY6pgHtvnEJTz6ls%2BiYpIeX%2FfpSHNxuAVIWFXapXO7kypXSsl7Ygwabz61zrU4UHanYINSAUSFqQcBbeEhLWhRZl75tlJrssFCVblMho4Q4liVJmzQ58NjcUSBJqsffTd4NehIi2ySuJXuHoLsLz4%2BNZrC7rZvbgbz7OUQsscI7KcxRRqYDqb%2FrUyx2I58uXbXOYNuT3JC5Ybh4uDLcvNEoYqiAZDaajsbE&X-Amz-Signature=a2938ffe497c1abfecd4d59fd671fcbc3a1b9ca4f1cde982e1601471ea8b5abb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPEP4HV2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCb8tIX7s1BNpn80WGlkdUgxFQSCfv1bEtuqzGa92C9DAIhANDKwFq7OoS44CZp0qlS1S3DH%2FrrgC8jPT%2B4PbQFSvFvKv8DCGIQABoMNjM3NDIzMTgzODA1IgwrBYAHOu2rgQ0ulhYq3APailSSPz%2FrVejFbqPsQZHoxQlbxCDFpKn5ApHOE3gMkKkCRih27hIcjbnY3wZwzlPseqrWJEKPoimYJFOekqhsISewQsrNMf%2BfxXSoWAbBuyl4vGGn%2B8b8GY2KV4moue3vaHDuLYGkuUoYsT%2By%2Bk9FtLteFvawcFKUa1O0zW3mnPm6xAHbvMHXPbDZwBDuxywt6NYbpAuco4%2F9%2BvtcAnz%2FasadmYkNmatQjqPL06Ievl2aRU7Yaq2Vka1rMLFApVMTJoijCRFHNa%2BH09SkqGQDraBYxNx56EdclIiKpnnql%2BQtSr%2FRV%2FiUx0pnZ2AMK7CDKtXUirAczkI2bZUNo3O5nM0oUV4689FTlY5HozYw%2FO9X53uuWXoCRiEetxzyJM95ykm8xq9EZZjRl0m7d7AsQoQKrHk5%2FoGrq2j6JzNk%2BGBTG%2F8QCLKHmi99pUo1Bs6nE2%2FqFaPASLr2YoOOAOi0Yb5gj4zhKOLz%2FQXCoVsCPciDL1opEtzzRhPBgHf6U6qgo6br3oVEEQen%2Fjgs55zV%2F4RYr%2BOvtjciDj0il%2F6gHPAY88D2mea0mOB7a9WgZKNfDjZVl5z%2FVPgpKcMPB%2B2k0WvAK9KJBYH3lZxCQ3KM5i1eAIuaORuwqppHZzCn0pO9BjqkAbCwsnz0V4JS4qu4hu8SD1lh5EqPEccc8vByMW33cNgnljcrWJr4MZsjvYeik0YI9yNjQBEN6DvMlvp%2F%2FAd99oDCWTAYZRzlrgeJdITjNWPSExs5Xq7hmK%2BWLqSelMBHf1xzHMiYBocKa2%2Bj%2FKkV2zSiMtWz%2FoSuRElemNyZ1WWDcgW8RNHA7tlcDmi9klHE054zT3voR1qB8PuB24UqTtQutq5s&X-Amz-Signature=a91ffca9a918938e90040c5785d6e4b4edf9b86944de21ccac5e25e83941e743&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DD7LCDU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDA%2BPoEd2k7a6CCbngCpBzPnNB5xLlNI%2F8ZgJ84iDLZfwIhAMe8Rnr43MQOuEi47Vakgh22R72lxxHsoPxSpVCkt6LQKv8DCGIQABoMNjM3NDIzMTgzODA1IgxLe0b61IeiNtgocrQq3AOIsFdT%2BpZaTAhx5nMcxu1c6nOY1J1yAM6W5GK2jmk7WoyoEO4fEr5bbxuEa%2BiZ%2F1N04yTUYDFcJYjcwfzHWyikVcIS%2BcG9rC6NV71sK1mm0m5gzGTEvafEOBI2z6jqfEHdZA4n6oxTCA4vcBsSUTqG3AZkyFEkNAZb8K8EZivVfDL9j2WkVUcJd2MDWacWKVhui9YwNBvIuUJBADchco1N0brusnTarnkbkr8qyjD8fcq27K2CqetCiqqz6QjY%2BGk00psJ4Zr5dtSnu3Atj05lk4u6sMkEqTVRz%2FFegmEizgsTs3j9Xg6j4aAZdV%2BNyzAtKR3PFG4xQiGcODoaBlJLhoPtToqzGQk9nYhafTlpUXVCh6abSXykEPFutNqiQHVspwDoAqc9Honhm9Vluaj6E%2BmKvmpmBORgntv19N4ZdH3olSrCP4cecbUqjkFgAIE1JTcE6LdDZJPfnWhQ9KTEdK3MaK3o6%2F2Qg2XP8ul4Z4XPlNlp4mLBDq7OYRJxtbYSEqGFDwOui8XNbDpMHiNumBq1yAEbQe4tt85BbodYoIquEGdT79C2goCf3vy60x2lDDiwC1%2BtUVOftzk47PyqAshW%2FZ2gmPPVGPpCVReJqnqUtxs26sHrto2IBTDV0ZO9BjqkAadSq5oW%2BWavKvNcUZT%2FYTjlbXdNlHKV69%2FZPRptZQfTg%2BFl1IxBLP8DDZRzEIE0DyIOLEnOsW7UDhuhaABvvvJhAXMY7zmiEoGrCywDR700dTytNgbXyLRA%2FLkz7r%2FdpChwqu1ozk3Q6fM%2BozAMt6gaNh5QlxY4loOPTxdFStc2QXnVxMKF8kaoaHWoyZm7hHtY6Fd8IakSycvgLhAl2LgDX%2F0v&X-Amz-Signature=8ef2cd41f72ac9d0c0e9bd4bd5440d3300f1934f22ec49336a35478412bac91b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DI2TIOI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIG%2FT6q1bODICbgS6f0fVgH7bV7zPesU3rPaQFee%2F8VSBAiEAgh8fakqPZ9citNHbqIMRozYcKJV4Vp0tioPFhCVzFH4q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJwz74hKAhuwqbBoNyrcA492zrA8SXvweYfmi8Q4zv7kGz1VevB%2B0Ll5pQdyU%2FEx3Zo2zoEqXjzIQFrugBk7s57S4qBq90DMNgNXxwcdEjfZf27t1WR81DghboIDvlcHM9DXHu0dilRPGsQkyICHn7YsH6P8b2fcpvSWOVMQFH4BO2iTP6R5HGHjaBWRv%2FEYzD2T335u4Yh%2Bm5jT4l%2FhAkCbpx68tYc4UL1QV5huVHovG%2BLs%2Fb74fv%2FfcAydR%2FyZYsaP04AWGRviAM1abJ65H1JAL6FVErCdXyMcSYrG7dmT%2FWS3%2B4Fkvh%2FsmNXMnkxpy7Ir4JP2pFJzctCdv2dhXE58Vrs1ZAUCvLfqSzjOYFQePrnBn4T%2Fe%2BgzVUDJV%2B7JpUXoAnPV3wn%2BHQhvZAbN%2FFg2MdPqGZ6LscnnNjYCXnSeY1kn6mz8saXFYydGZGGgBlpYMTa4i4MMskpHReWEtv0ZJ7dv5bBPDoJ2wUjVUsB6fSyWtfYOHStCliTaL4o94zM9J%2BM5yikNllBedZC9%2FTsVXIGhWy9h5udiSqu%2FYjO01XxYwWtDUiWT2hLd8qSNoQgR9PiD4llNzCoUbIgUhQN0bMVZ0bztXM3e31PuAfSpB5Fus0%2BPYBZOk0iyWtgPVqHRMkJEIxulryrMMLXRk70GOqUB%2BktjpJWqosYkYZaEaz%2BEt%2Fsrx0JApYBOyaKAFefcMPAZcJimRn4%2BeAkmdoBduX3xxXBTUl%2FPk3flbiYkHEHBJUYmjtI%2FxSrvPzojGVF5Z24bSlnffQKfTOVkfvgfdW3MDPITQ7SLGyuAluXeSVNCZ4YbySCVeTv6CbtveBEE8T7ya%2BKzQeVzqvMiUuaxh3ymUw1p3j2sc5C97soFrQiOk8vyNjRZ&X-Amz-Signature=27f65e41b01f41f6ea5004002e169570071f306f339131109e1f7ebd728565d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DI2TIOI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIG%2FT6q1bODICbgS6f0fVgH7bV7zPesU3rPaQFee%2F8VSBAiEAgh8fakqPZ9citNHbqIMRozYcKJV4Vp0tioPFhCVzFH4q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJwz74hKAhuwqbBoNyrcA492zrA8SXvweYfmi8Q4zv7kGz1VevB%2B0Ll5pQdyU%2FEx3Zo2zoEqXjzIQFrugBk7s57S4qBq90DMNgNXxwcdEjfZf27t1WR81DghboIDvlcHM9DXHu0dilRPGsQkyICHn7YsH6P8b2fcpvSWOVMQFH4BO2iTP6R5HGHjaBWRv%2FEYzD2T335u4Yh%2Bm5jT4l%2FhAkCbpx68tYc4UL1QV5huVHovG%2BLs%2Fb74fv%2FfcAydR%2FyZYsaP04AWGRviAM1abJ65H1JAL6FVErCdXyMcSYrG7dmT%2FWS3%2B4Fkvh%2FsmNXMnkxpy7Ir4JP2pFJzctCdv2dhXE58Vrs1ZAUCvLfqSzjOYFQePrnBn4T%2Fe%2BgzVUDJV%2B7JpUXoAnPV3wn%2BHQhvZAbN%2FFg2MdPqGZ6LscnnNjYCXnSeY1kn6mz8saXFYydGZGGgBlpYMTa4i4MMskpHReWEtv0ZJ7dv5bBPDoJ2wUjVUsB6fSyWtfYOHStCliTaL4o94zM9J%2BM5yikNllBedZC9%2FTsVXIGhWy9h5udiSqu%2FYjO01XxYwWtDUiWT2hLd8qSNoQgR9PiD4llNzCoUbIgUhQN0bMVZ0bztXM3e31PuAfSpB5Fus0%2BPYBZOk0iyWtgPVqHRMkJEIxulryrMMLXRk70GOqUB%2BktjpJWqosYkYZaEaz%2BEt%2Fsrx0JApYBOyaKAFefcMPAZcJimRn4%2BeAkmdoBduX3xxXBTUl%2FPk3flbiYkHEHBJUYmjtI%2FxSrvPzojGVF5Z24bSlnffQKfTOVkfvgfdW3MDPITQ7SLGyuAluXeSVNCZ4YbySCVeTv6CbtveBEE8T7ya%2BKzQeVzqvMiUuaxh3ymUw1p3j2sc5C97soFrQiOk8vyNjRZ&X-Amz-Signature=72f9a6e5d7a9ea3f43b8c353e991c30be4f7159ccdf5031d3c6d4343ab591860&X-Amz-SignedHeaders=host&x-id=GetObject)
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
