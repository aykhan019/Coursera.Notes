

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=cdf40ec55ff78a87ebf383f3f77b60fabe529538f60564585bebd703b7a194cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=020b4ea21c68f22eb7caccab0793be94734c6e31f3bb2a0b5a040e095a40a392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=fd8b413471e1fd4643bc49675832979d1a32c2dfd17a3153f779a8e69e9f24c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=c7bda4b854644091766d199f5e3536e898dadf77dc4c6db77b0fa04d0cdca9f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=15b50072372854f873674f8786801442836afc08978f91894fb022e20b092067&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=2e455ef91f9f42efe0e59c9c570da9b20d00140e6a3ae01e7ef9f4bbd1b58228&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=94908c8696af4ec03c8ecef2e7f2b7ce0fb35f64dd6a8525827d9017d650e033&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K4O2H3P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBSFVEvMcgxkj4eitCv5IPW2erd20krKgjsZapMwr%2B2IAiEAxtJUgiKrg4waxY1qbZgzG2CKqz9JNUTE%2FOtjbRWUSW0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDAjTrxohBM16uEZ8oyrcA%2BIKc3ueSPnnrCNk5JKQLp%2B2XAinG%2Fz7c%2FkmJ%2B%2F38ucb%2BqrGtjde0cGNr%2FKwTzkK5EqaYowPr5RlTtZElu01ZHjwuZqv43uTGgF%2BvpJC18NSQv5%2F3UG53RTuxYQxE6FBbwA2UhAwT8dkk%2BRnM9NBpaENjPPUGkfLzN1Hft14J6ndHwARSkaXMS8zDw9bBm6GuOJpAunogcUFj2e6EHb4%2FA3qLiyi8nCjKF6Cv5RfZ%2Fuw4K5180l8bSLGOVo3shZOE00%2BcK9efJZFU3%2F%2FnWeO327blzmvXSoqHEyv0qhrxfrO7vgRap%2FRaowwiM40jzF0VA8qDEStOCqUxgp0gtWxRr6QLVuHwHp0amppUyR8x9OnHfrdPwmJ6htPFows2SSboaGQYxHbfmsVTchCtU3ZiM2OH0Z7DGu3m%2FtJOqzJ5ets%2F5AQgeFZmoZxWRxoaYp0R65ofXkkYW1hhkatO8alAM8k3lmd6BfhL%2BhAK3%2BQL4vQDvEcTM4IGFVP8IMG2KehNErnaFGRBE%2FANArABWUB5A%2FavftSxkny6uTuwzQRzHWZmh%2Fjwcovl3YPgcEngAbM%2BR2la85CIwfWPTyOxIO9JxmtkJl7rCWoKAMskpZJfhVDRxDh7b0Mqqf44YHZMLSUhb0GOqUBUAO0XMqNjw2%2FmIUhAMeh20hrisjeo1iS4MeKJsHxvh%2FODVBk5e97CTwEQyKW2olnWXvyXDRGR4czOBiolZdzLXjexUSOMmFAn5j72%2FUXmbhDxAmtoMqMRm80dSgcnHk6euxsVhK0iptk41yIaIZhDfejWjjRnh5oNvCZX4pRj3PVRS2UVI2s6Q8RaApoHkOvL43V4PSp72OjKjGs6UCbU%2FHyqFvq&X-Amz-Signature=50cf88b9debe3d849b1b44a55e66091311f51b0e47de80ffed5cb236d365e1d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2UMQP4S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGfG70s8mkfRjb%2F8bin2iKSaRqaB8gz5QJRrFP%2BNNjSFAiEAwUzNn5lvWWTQO%2FijaDWw1S6AEhvFbvBOUSbYeo%2FrypYq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNK27h8wySXVG%2F2ZyCrcA6Rigj75MDQd4ehh8MD9sBohgJrmpasRNIh4UupOEhh2l24CJiTuDCn%2BpjOAN1FA5jHKQGhj86rRVpYUWKeH8be6vtrqXL3EzSyr3DjgRFCF9Dy3LQtUOOIH1qtRe%2B6di%2B1Ck%2FXsVbvCcnLzaYtBgsHORvEfdZgsvj%2BceW2%2FTVD%2BIDOxFAumu%2FqaDjKQDx0ByeX97oRu3WvGicnVS5VcEdZnEd8BzaBTGdZ9J0EFm5RQvMbXsx4iAHTSfmaZhBjRFfjaNQJ4PrFqt2dlCKTdg%2BEEqc6SHoct3lH0uXxCUxukSQ3bp1avG2%2F%2FW9BSdiSP91cdR9tzg3nnrv%2FekuuqN5i%2Ft8nVs7ieiBNVayhTIx5jLYctAxY5jLVxVhxuHwXvW63JRg2tl0%2B8QVauRpg7pL4wtFlxAmeRD5EYKaysCJ0R17t8rq62uu0Gcb4oWt9v2l6sVYo888A9gDO%2FMle%2FP2zVMXU%2Fe8%2B0Iwf7k9TmBYu9My3qbaTzgQu0gycP%2B9%2FzPzgBh9WYNwbgNOKa11Qjnqo8KNgpYPFqivBqPpYO7KT%2BcLStl3sf6rntfO9PA6A4ixNk68%2FFcGjpGgTK62iWiX8SMXnc9h2ZtligzZF6DGC2uJzNtqqRB1Z4zzeWMNiThb0GOqUBVSImilA%2BaGAt1sgvhB%2BQJXocAOcMjJxfxXOaDUapi3q8zeYm2PUIA2a5p25KhrpVBcX3dn6YFhR3S%2BGgoqcPmzUW4GpiqYfWK8AV5mxbN65q0ky%2Bonu5w6XKhNtfGSzqO6isI87tuowfa9qGLw7ZBeYWxpw70WTc7Log0O3rn8zy6gFe8z1Kfhd8gNNp7DNbbXXSt8gUr%2BN9ib3I%2Fae%2Fkj%2FO9IKd&X-Amz-Signature=29103d2a813bd194ce6399ec44aa1ec34dc9528d23e3d8f1b1e1e7d3a034b890&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW422HIH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIHAuuFh5CdG24%2Bttr85tJGiwN8%2F8VDtxlp5n7N0uWUeaAiB0faY6S2gMfhoAekXzNzPWiFqz7H9eUx7grXqd%2B1XIvCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMgt%2B27oI2AqUB2ZUDKtwDEMHbg%2BONyDAvfmrMOc0w%2FS85EUTpfFxkaPqWAzSmMtE0XlNN%2Fi9mwT0lEjk8SCa3Ajdb0edV%2Fzy0rfcWeE3SkKcl30FyAJ%2ByuHAkD%2Fp5Upx0Ex7cn%2Bb%2FHlLuwnorHwz%2FPfpYEhWgyfzPQy7ZjGh1RVNs4RBDBb%2FNvhcr2TTtyaJV5m2dMPu8OzLQ7mrSJpfNb%2ByNjuPpWgqguZJsCzdUggLyOUCpce0aPospqo%2FobyZftDL9P%2BZjUKpvNxoYYE5enZUGIMYZZKCRxmZ4uqp4EpdsLAnvoQASYHKs0h8cg40svRgeIHRIwzSVEdjVfzFARV%2BjUTC53fh5cpLRWSMdgWvikS%2FV3hwKTLZyByo0JePwkwnpSfXUOZzPaOgPkHxA%2BM8MHZxk%2FwS89aIo8CDA84bzFbw2hcMYI7a2rVwdqEI8TzLtqoknFgLoXY13WTdSiLM6O3vH5u4i7jItjWmTVYGzL0CPKQfx8SiRoAJ7xU5jLPCvi8Ma8KjuNiPfA%2FsLmgw%2FlLWM9Fol%2Bjz6CYtw2QCgQgcNiYZL0p2fyZkB9W0Ofh%2FVYo0Jtl%2FOS6o9LE69dPmohCXTGjNQ8LGsUmDKL1WcyDUF0ghz%2B2%2FJN5I%2FJdpfSZM0GdLCGj8gCsgw3ZSFvQY6pgFetzHQtzkMrpOFZl%2FDZODtjHvxx7SmUsAuHl8rEKlWooFrhy5IesrosAv2V8ua8Z90baUFAUauSpa5ne%2B6EFoh8mJEB05scxfMHUAnCv8mGiTh%2B1dGcn%2BBeEGBU9r%2FE0kX%2Bx%2BGjYdnApWP1BVZGx73Td7UlbtMI0HMS3%2BGTwE9EPgmYKh2Q8%2B57cW6VjcrNnRkBz%2FpRkS1nGxCWe6L5ywQ0EZ10KDi&X-Amz-Signature=84d88d32b048bf9a0cc9bc5b960e61473c18ad198ddedd0401886fd20b5616f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5E6C7OM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDbhO9GnTK80UoGiHs8mngnEG3mvVZSYPPoFbSO%2B%2Fr9vgIgS0YQdw3Q36aPAch2Hc%2Bt8C0weZwV2FCfJO9rWDOA%2BFoq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDM9%2FFzrvGawldOmTQircA3hezHymEtv1420SCD89VAHq1g8HGqxBssE623UmMlTGsG6xXpDQEPW3AxftYGl8e0TDPY%2FTUB0Ih393ICdyzs7vFirpcsVJ7DdAUlxu%2F8z%2BUY7xQffisGUc7xSVJVf2Urz9MVSotcxhPa8Kc1kMO%2B8Rhc2mwI06cw2eE3ZFWxPS0XFevpRzlA03S%2FpPfBg5FgnmfoCaBUB0GSziyZvM9GmxPXeIkrOFB0hzbGx8DRT9eBB8wuXVLHgNYiBopS1ohajqGmkDqwFj%2BmIZlsIRIt8k%2FoUG1tZRbXx1o3h8xHePP62luNDbrsVdPle%2BSY2OaW%2FmyoEzVtWVdGxs99ZHzjNcniWAWM122nkFaXa5rD9ajhUgrgbDNUxpGlKJ0AFcw4TDRqNjvKDJaVew%2FNw0Re1M10EMS2Fnu1UK31OW6lDzxyxXF7k7LBToOebpVDuvte0txbOIB4HFdbaK1Wd9krSnUUucswiHT504u%2FD20jU1QPsbMhD9k3SGyrK%2FdHkiUI3hiJ9t%2BI0EkfBct7t%2BKR1q1suZaVmi5BOuCdfr9EQX98N2nsOiXCFOwP8pSKWdo658cW5PcPT8Rj9nLPpjiwi77EH3kGeFm48moLg6vmGVYRz1%2BXwQW0XsFYTOMNmThb0GOqUBnuhcJg%2BHE6q%2BmeVhJ3E%2FNUqufCq7gG5NU%2FZZ5Bs3K1jTLO1M6J0kqaOmPrByIY%2BPKAbYMvcc%2FzV%2Ft%2F4mxVzfmLw9hQ89cudugmDs6SrWHVGKzteKNcWPsSCWqUI74E9fZ97KnRLgnK2ZjyaKm3V85uhw7luF%2FA7w7ytNvVCE2VrZ8YLm2DrnXFQy5FcY40YWDAwrDpcHcymzCbHFQ6qcRG47PwLp&X-Amz-Signature=b9c37e5850b3985a45d5d7e62adeca4ee1a57c28a427ab99458173faad801cce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5E6C7OM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDbhO9GnTK80UoGiHs8mngnEG3mvVZSYPPoFbSO%2B%2Fr9vgIgS0YQdw3Q36aPAch2Hc%2Bt8C0weZwV2FCfJO9rWDOA%2BFoq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDM9%2FFzrvGawldOmTQircA3hezHymEtv1420SCD89VAHq1g8HGqxBssE623UmMlTGsG6xXpDQEPW3AxftYGl8e0TDPY%2FTUB0Ih393ICdyzs7vFirpcsVJ7DdAUlxu%2F8z%2BUY7xQffisGUc7xSVJVf2Urz9MVSotcxhPa8Kc1kMO%2B8Rhc2mwI06cw2eE3ZFWxPS0XFevpRzlA03S%2FpPfBg5FgnmfoCaBUB0GSziyZvM9GmxPXeIkrOFB0hzbGx8DRT9eBB8wuXVLHgNYiBopS1ohajqGmkDqwFj%2BmIZlsIRIt8k%2FoUG1tZRbXx1o3h8xHePP62luNDbrsVdPle%2BSY2OaW%2FmyoEzVtWVdGxs99ZHzjNcniWAWM122nkFaXa5rD9ajhUgrgbDNUxpGlKJ0AFcw4TDRqNjvKDJaVew%2FNw0Re1M10EMS2Fnu1UK31OW6lDzxyxXF7k7LBToOebpVDuvte0txbOIB4HFdbaK1Wd9krSnUUucswiHT504u%2FD20jU1QPsbMhD9k3SGyrK%2FdHkiUI3hiJ9t%2BI0EkfBct7t%2BKR1q1suZaVmi5BOuCdfr9EQX98N2nsOiXCFOwP8pSKWdo658cW5PcPT8Rj9nLPpjiwi77EH3kGeFm48moLg6vmGVYRz1%2BXwQW0XsFYTOMNmThb0GOqUBnuhcJg%2BHE6q%2BmeVhJ3E%2FNUqufCq7gG5NU%2FZZ5Bs3K1jTLO1M6J0kqaOmPrByIY%2BPKAbYMvcc%2FzV%2Ft%2F4mxVzfmLw9hQ89cudugmDs6SrWHVGKzteKNcWPsSCWqUI74E9fZ97KnRLgnK2ZjyaKm3V85uhw7luF%2FA7w7ytNvVCE2VrZ8YLm2DrnXFQy5FcY40YWDAwrDpcHcymzCbHFQ6qcRG47PwLp&X-Amz-Signature=9a139460c4f26f87126abfc5c81bc09739384d339009252a2bc9fee81e5a194d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
