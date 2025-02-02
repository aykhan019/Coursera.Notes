

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=d832ed8b955c7218813439187a0edf40c818cc5c179cec6958394c27ca54a66b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=a84adcf35b77a94c0b079dab9e9e1124a93a17c0baf58d50684829fbbc31b6c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=b718b65dc39075a5df1c71a64a019794b9eb2dccbda3fffa9720846f4e21b80e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=f6f8c85b36ee1dbe91686d77729fcfbb113c26ecae967a7e6dacbc68c93db21f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=12b52e41d07a14c543fe9d24ab0381cc5c5a1b1738e56ceebb0c616cf173efdd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=70bed5ed2c28bb6c332aa41f34dd3922615b2a8b933a5f8dc10570ecf1750e0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=449d9e0ae0ff7bcfbf1cf85157898789937e3c10fe84960e518670852e125a66&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3R6ZLKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFG%2BEVBFNQJR83GTF%2BWxjYjeg3R3j4%2BQp1aVh%2FN2bjL1AiEAhRha9w7y%2FcPaLxD9CLj5kwsdr4TmbJxVvI4%2B8w7n%2BXMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf1DUzfPoSvjLMsTyrcA38dByKO8wjVHTls5rr8mTC3y1oM3fplXhbMIiQQhmmO5yKTb1X39AjnDafTh3LfvwSljb4SAi7rUg%2BRjba3KwMwHojQtG9KFt4T1O6snB%2B4qxQErgF4mcZdM7EPnutMFU3T4jWR65AwaPT0kMu85ORkoZp2xdl9MCfUnb9F0ve7Ag244zyJm4o%2BcYYCFw678%2BY9wFNnJkGNpg7gJLB2%2FAeJ0iSW6AQv%2BNY6Kt3UCP6pycobVtmqpnpYjTh1uqw%2FqOgq8a8WTmL%2F8Tox%2BB8UfNk65PKkPGGe3EPXEdd5TPE8WC5dTdWKyYh1IRCCEtE8DubZrQVvsQmPY%2F872oL5J5rhvuG6HjLtizJ0enwaL%2BgqfFUYsQaWqVLIaB0nNRmIsHFzY1VxIjpwIXSx5m22RMjljThHQ%2BTdxeQFpbtPWc9CsdVqL9zJMvjDMt70bOVWP1YiCzikFa%2Fo5aVX%2BRjrdQbOYvocbgC%2FbpFjJSP%2FCTuDx8R%2FOL26Zr7T9rIp%2BKJmxsRlQibGGfCWlFN3DKa%2BQY1IWteHSEXBsu3qPUURAiYyOH5zXir5EvUk2E0f%2FB7%2FfqF%2FymldmucyTg3gdkbOWA6zzbdZT4jc49WIenDZUvR22n5H%2BWcmyqR2JtIeMPmb%2FLwGOqUBPryvwITC2gfAFXK8B%2BMOsEUDmGNU7XAiTjcvuYHqBKrJuRHdMM6k711UVvfTSGEBO60vKmmozOKFOkwOa5sBWogK%2BJI2WxZS3hmYut93%2FoUBgT%2BBmeX9G2y11RSH1zoMCtOgicaDQWQrhtytR6PNqWXIt9vnLkbn5BrMSEFvcLSyaNQk47BEMVj9SkV%2BDRlx4nzgtsSFZOZ7YIHxMm4L5dBcnnDb&X-Amz-Signature=610ad6a884d76adbc7a349e22e18b841d838ddcb94d172b23ae2bb9b89d30190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZE7GUGA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr5mwj09%2F08whA1TBVQZIHMrU6Ab4HCZe6WZxizOFmfAIhAJJauWtGCnLLRAbUYXoWTRijbELQJzGI7336CgDkgA3hKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr8gp4AtkUrCeMj%2FAq3ANKNVtz%2FIS%2Fi532MfqL%2BBGIm4A698Z1l821xAIlT5nughgXETKxCV43K4s%2B3z19tNfJ6ZDproeekMMhKHE0hkIC6NiQpVU47PP7K4qH5OtyHTBJDf0dmmsrL7BHU9X7Uq%2Bkk5T0GV9Tt1hmYXTzQ%2BL7FdJbeuhCvR7fZOqdnIGroBamOVPn6CWEcWKE%2Bqb5ukNsTxH3OKr4qpuDAi0hxYFix8WWmKheCQiCKto8GrpUQm%2BCHq%2B8OpPC8Xsqmw419Cy%2Fj4W7vMwpteV41M1op2HOO4ElC5V5k7T6VIMibimkgDW3EJriLQ%2FAP%2FZiFBcg%2BYApqQ3qeclRxYAEOAw4eBAAlSz0Zo3slbBiG5yk0iQEcHcPOG%2FKbV2KnHz19dFzrBHnS4wg1Y00ca1zuvz9pe2CQnOYEcSJN0lk81obPuWFqMn6mz2aAg8jCMY8l5vIlLB0atvGkS7UKk9FGUOLOLQ7ZoUFTCoIsEAcU4Aa3hNBuBfe8dgrqANDN6%2F433S%2Fjq5g1GVXCO7rbxOl0hzSkJiVXjOrVijzdKZWmmELIScxQO2uUvkr0rKDaoiLDBqjpSEBCT2I0Qrjq71C%2FeBKYxgM%2B12UHkZzlYrzfK1RsD1Bm0M%2FwvbKN20LvhgW9jDLnPy8BjqkAb1jfy4Rp2bYLqNLfqgXRv3VzUUOZmNNdmOLYoEgUb78ooyxYWu0WSycWbvf%2F2sJZZmGgdFSlFMybNQK5CEHWB%2FK5HvUDX5tUQmoFWlxrsR%2FMk2N8G1yPfY8duVeY2VOaOTgNUuRAtiTE17maf6jD%2F5n9ZJ4PPTcFRJ7pG4Fhru%2BS2Xw71MK6vqp1IKR1r55deRPloKXwMQ6D3abdSqFB0zn1Oau&X-Amz-Signature=aa503cdc1cf144e292e84f2a59f9c15f1c461453c5e4492ee78776222e8704f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4XFCXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FnIVUjCDcmIkr4zpvYQVbe43WFSIHnRWAKwFOQIXWaAiBy2aPuYYyIOhU3cylrnqPBwJCcCMUbFoEFpZB5vJhvhCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7N0EMOHd2a0t7UdAKtwDnmoCkn5GeOQgamaMoTYiev6o3LaK3rhTpF6PdegxqguN4os2mb1pDHYn6DWVYKgcBZDwbgWm4of%2B2HYxlT05XwhKJCMyXAVT8DA0%2BtCAlopxXPY5B41owk873GPM%2BRz90iDB%2Fj5Ss%2BgJe7YTuMD8WcjDM%2BcPzDdy5J67pNc4RJYzc%2Fj8xPXcz40sDkoPXnfzf7aYnWmQZy1F1x91egbtut%2BDgaPlZfQw28RvTuTF0FwqNkG%2FvnJ4VppfJqGZdRREEiCbjc1celebHxxhRCx0fa5bn7AmBegdPMPR9jmpZ5QeGSsgk7UxSEj0cmGTvTV7rZKrEcb5zgH2l1XXZNBmoRdghytCfyCJIJBTW2mq6wt9%2B1ggSBUYjg2qrlb%2F9zCZ4EtC137lrC2P7qiLHhH1CHqgFI4L5iRf03Epxq7cOmxtSPfm4mu8S00YaWV3IMGomqESygXJyVVHax5qLTKZxrUMehEShAtdnszR%2BDDizpTfNwdmotS3LyAPRItoM4tu%2BCq7abl0oIwar4UDpt3Q2kDSQamXHJU8p6W9bflRizCFGmJ5PpUc04XWKVN43W4GHvp%2BrG7iHbm6%2F3Os1H%2F%2BT%2BPok9i9wPcb78TrBXk0t6x%2B412b1YXy1NHw6bUwppz8vAY6pgFpo1RyY2g5EUYCr3McZDba2TjNND%2BH4c4%2FSh%2BLuz4r7y9mY34u48X1sVa%2B7GyN0YLhPZ%2F5I9aEvPAdCnwWUcj9WYO0j5tZqn5ZTBxbZXa6eVAbnqF9N6xFcdrCSg4sImQLcRCCyWOtL1p%2FyENdQrF3a7GS9Va6x3gOeHxPu%2F05OZ%2Fyavmqw%2F3O15cBY9PBy5Xp%2B%2BAhJT9f9MXmsHSgo7fmrNK%2BtGFG&X-Amz-Signature=ed3dbc8c45877144bd07af2dfb55390795e7190703967e97238a1b529533f86e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q52XWFD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F37KrdLFCj13%2BzYWI9buyxxN9evCaoR31E5I%2FNTcu%2BAiBM812g36F3xddAD47ZcGJLjVb6xj%2BoSdoBX2Dh2gBsWyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOXBP4%2BTPE%2Bv8PdA5KtwDD54CT4sXpKrllazJ1R1ymIvURlyJThCJNkg8ny%2BBGbdTSqRoG6XN0pWnj2nDJcmmcCl5lvzmnnDs3t25Xb1sA4AJMp5TjTSiIv1xT2r866%2Bb0%2FKEQz4GXGKgaEh%2F80Ed69FzZLdWhUkwjJ9Ea21fYJPJx31HnGh8F8IznJOrhO1CHidUb9qdV8ODfWmpz15VhhFpL9XD5vuwYoND4YX4h14CstDZsl6mUNsEwudosXJh0MCkiukVZUGIZ7jiCx5fukX9N01vUuxpEfGnNBIf2ay4Kt5hcavHvr9dooZGG55PVOZB8ERDK8R%2B%2F6d0hHbX7hplzFLu2jUPkttMySQCTPQplUrlrzx3hZGvMalCRizfSCMBAABqQV37III%2B5TWgfnPUfHxfa4RWUHPs9SpASP5KEmc7wiAOm3jaqYAoSbPk0Ua7MB7OGcZAwDXkCYrh%2ByqBQfow4gXsHxNy1bBkcSfVW0foXWjJJURi%2FSleRm%2FgNBI8aLNSYBOhLmTx1vhxGxHa7BMXp%2F%2FOwXe%2FEmkUbTwBADAlFF4tObKc6nrzknNp4YagAJJcMz2z%2FUTWaLMVbUKy9Hm6NqR1qkOIeyWpxHjkamdJvy66xAobA95U4ND1FHtkMIxyK5IXr44wo5z8vAY6pgERsxdB7rwQ3%2B0xRcz3DfmkC4t%2B5CMSjo9gXTn86N2Je7KD1DaTMCbElYe%2B7IeSXVnI%2FpdMOSMEyeYygTrAAtcta0FWvKssqhcr9%2BGM3Z5YfMWPU8Jkraxp0lUgOKCgpwoTsGbFu4krqdIoyrY9BUJWUssNKf%2BCVxeJOuKCa1jXzAYc5tdpc6qyrD3s0ghf0Y8oTcmZMtIuOpYWtjtNECW1YkWjSbhh&X-Amz-Signature=5a3566d2a4a02af6ff3fe915fb1b2965ab254fa778e76c5533d519935679cd6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q52XWFD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F37KrdLFCj13%2BzYWI9buyxxN9evCaoR31E5I%2FNTcu%2BAiBM812g36F3xddAD47ZcGJLjVb6xj%2BoSdoBX2Dh2gBsWyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOXBP4%2BTPE%2Bv8PdA5KtwDD54CT4sXpKrllazJ1R1ymIvURlyJThCJNkg8ny%2BBGbdTSqRoG6XN0pWnj2nDJcmmcCl5lvzmnnDs3t25Xb1sA4AJMp5TjTSiIv1xT2r866%2Bb0%2FKEQz4GXGKgaEh%2F80Ed69FzZLdWhUkwjJ9Ea21fYJPJx31HnGh8F8IznJOrhO1CHidUb9qdV8ODfWmpz15VhhFpL9XD5vuwYoND4YX4h14CstDZsl6mUNsEwudosXJh0MCkiukVZUGIZ7jiCx5fukX9N01vUuxpEfGnNBIf2ay4Kt5hcavHvr9dooZGG55PVOZB8ERDK8R%2B%2F6d0hHbX7hplzFLu2jUPkttMySQCTPQplUrlrzx3hZGvMalCRizfSCMBAABqQV37III%2B5TWgfnPUfHxfa4RWUHPs9SpASP5KEmc7wiAOm3jaqYAoSbPk0Ua7MB7OGcZAwDXkCYrh%2ByqBQfow4gXsHxNy1bBkcSfVW0foXWjJJURi%2FSleRm%2FgNBI8aLNSYBOhLmTx1vhxGxHa7BMXp%2F%2FOwXe%2FEmkUbTwBADAlFF4tObKc6nrzknNp4YagAJJcMz2z%2FUTWaLMVbUKy9Hm6NqR1qkOIeyWpxHjkamdJvy66xAobA95U4ND1FHtkMIxyK5IXr44wo5z8vAY6pgERsxdB7rwQ3%2B0xRcz3DfmkC4t%2B5CMSjo9gXTn86N2Je7KD1DaTMCbElYe%2B7IeSXVnI%2FpdMOSMEyeYygTrAAtcta0FWvKssqhcr9%2BGM3Z5YfMWPU8Jkraxp0lUgOKCgpwoTsGbFu4krqdIoyrY9BUJWUssNKf%2BCVxeJOuKCa1jXzAYc5tdpc6qyrD3s0ghf0Y8oTcmZMtIuOpYWtjtNECW1YkWjSbhh&X-Amz-Signature=0a83e1d10c9fd7d6f713f3422857ca380df67a7c108c1fbb8755ce1cec34ac56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
