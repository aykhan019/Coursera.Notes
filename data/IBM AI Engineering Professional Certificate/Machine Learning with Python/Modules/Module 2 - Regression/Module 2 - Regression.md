

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=06485d34699f62bdbc6489b4fb2220ff4417930c191d0787337abd49bbf2cf17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=bf512d93da42f258252fb0834e1bc494520697a330d0cd2110d02ac2728271b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=0b5a073cae8132769e3a1e5eb3abcb2995e037a23b9c180499e61fad07fd709b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=781643c345e2a730b0028c9a429310a906440e8e43b167e3df9eb5579a503c82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=e2efe0633d24421690e5cde5a64a2fb4e5d208af6d220f4565e42335b3ba5428&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=1d18c45913353c874e094877c39d4b9e92ee18e256bdc692b2efa88894ef590a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=a8a167151d1470c76091b4603d5ea828269b6e6acef59f2a02e5f4043d0095ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZKK4PD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK8ZpkaieIbTgxbZH02BDSy6Ag8fxN4xJjFI2Cyt9Q1wIgQLUzP1R1wY6N3EGefxOji8qzHkqrO7NOapDivJrEspMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6tAC88mVS%2BwOdTsCrcA%2BPvvqXQbQGsoSDW7Y8n%2B0U19rKgsRVNP0hRZmItQnfvkNQNYI%2BblfqNdVcvh8sSlrjXXbmUGrocwlN0rG%2F2vsyD6MtdBshPlbflj6mVa8upDeNpvWo6JQIZKtQpN%2Bvy5qZf35lS75Q4FzpCriYCyJsczoVahPM4LeSZoe1M1qtP43OmopIVn9pwyd8TDGg8Oims8eGkhhmOEGslJBPLLok6nWNkzS5v4oIU6s4SjV7Bq2SqXQ%2FsBdH7JLDEM3RqCOwvkD9n0PUa62xCswMjsAWv884tKiYloY2wwrFjHsf7jjXePVuhB%2BNEpSIcE0ZOiS2aS3dOBqLIn6nNRi5KEZkyJ7DkdfQeN5pwg1mQ5aKtUSwy5fvoD6gMlVjpw5leqHg5zLqjENIxbTCMF8ua51lWvYb6ARaYQA4s2vEeF2SufKZXX%2FzjXzGe%2Bvcr66M0FFFAj1GoPb%2Bo%2Fd3FGGBcPz6UBbLdVhkM2qh%2Ft6aTkUY0WRH0zIrfLZEZCm6ZCTJceahpjEKmztpu0OekYqp5rymg%2FTVG3N8%2FTQu4BD8uV%2FOGf%2BnIU3Y3b61Qi2t%2FaPQ6pZN3LdQId3amovUc3fOj8KqwgUQoaCiJbcurx6PacRkqlarrabWwVGXHdbDkMPal6b0GOqUBe%2Fnc9ali0fwZ8X%2FxGPqT3LBYqZ5dFnOFwABE%2BwB7N5UrqeQLli%2B6osDxmY%2BXu2ReW8ny%2FCXmnUDIO6shQ9zGxscpkKL%2BL60n1HnrQoIUYj5IoHQt2XSrPmQNMtw4kLUf97QlwMgRFu0uWEKq1yIIfReLc6PBoJTWEELREZimuRvW3IDmQkx%2F6ne1mtMCVkVaGh2z2KGWp988zE4BkBQBYu7LK1Cb&X-Amz-Signature=923a59331c333664d8b8d8422ff4bdc1a97537c21eff6231e0dc8fca31a6c138&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KEZBQWL%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8%2FpnIjWhHW3RFsfTx1iuu2d2GLqLekULpNh2bl9TF%2BAiEAggT8WWlsfBSaWwR%2FVOd9mhnBSXgHvhaMD2LaTsJRUU8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7WJymRdwpVeGaTcircA3myU%2FemTqZkQO3U95IqrqUOgUpkSM0v8bZ8hnA6OnSbD7nUamjDQ71y%2B0Z%2FzUT0aaNYyzZBpOk%2BXI7xZU3lN4i57AUohrgPSUx7fPVMvAPPqyIwy4KWDamYj1rLnF785We67Re0etbl09TzH0Qt01Z03g91pHUNkQgccqnPLSFPGXzn7%2B9DwlXntAHom%2FfS2A7y9Ryf1nPCk%2BeNH%2FJPFlq029qEEH3waOApfV0a558OF8kCKxVghO7J4Vco%2FjBcC5mrWrY0%2BAd8LU%2B%2FnQP1YAThlTpika4SXnjaYStBb5DdYwAXgt0Ge3X9%2BYthgDazYJSCPYM7S0lJsXrjCwwxTxglyPMaLk8rh1Jn%2BGn2c3tyoHzfbpSOiQvzBAk97e0BMWm5Kf8Dg%2BYHSmMotM9ZrgTJsXvbFXELtOKCkgHkgB%2B5ZDxZEMqMRRdJ1OOxVvlOK16Rar4uFmPRsQ69sl7oS106hIqjIfJTzWgsami7Mt3stT8WkkDCc%2B0MuspJlTzvAHXvcLUiLpCDsKslW16jP%2FXJ2Sx6u8URIanRyjhCTDv2RtTkVLQpaA3XgxWPvSmGpFM63%2FpYp2JgKiIqzFPnqqtXLT8yk5VjpkDnqL%2F4Bfx5BdHrZGTYfpwRJUomMIWr6b0GOqUB76SPHKGV8OZha6x91hmiWA8TT%2BuJWyQpLjIomGeucqxRRD9Rw0m1ZvkPozFsO63vW8PgK1LaeVA%2BJO8m1MsjtK3y8V6WqHMmyLPfm0l8fRd0kFNbxyEEQyPY6hgDkHM26MPB9mkZ%2B6HuJ5waIeXWPo8KhcKif%2B7OP2MmkcXOgYbX8iQlKOK759s0z1CVEa3nEjZXj8yWTS77jk1hCVdyRTP4bt%2Fp&X-Amz-Signature=ac915f91642e79d4a0b5d9d241e4c338547b8a1c82a690bdce98fe48e12e8e57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWFHEHIA%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXPkX87v8h8MkwNABT5yyHbVeVSNEZAw26G6x53dZEYAIhAJfoedHtzuz0kOKVq9awtVFmgth%2FJEkbq4XujDmRkI1EKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZD7J97MWRTJKqnAYq3APiAfP%2Fw6V8LMw49Uzs1hCMgf7quoYzlSNuKD8DeI1lnKiQ0KgA6%2BK0JAyD807K1r87CrfM6gMcC4YJBtce1IdbiYXOiYh4L%2BkaUcL4xyXQcEfhPDlcC7QfJsDair6czJpI0gjgnKKbBoLksECwqngFJes1ZomLFvYTbuOO8Tk0NQEdBfvke44bNdYw71Wl0Ffd0tMwmwBXBv4oz80pdPQ2XEWXHPo%2FT6uRYL8WHp12jxzgBSTduPFrCwC%2B7YydQUJhCt2FQ0EfUnQ4Wf4sWKWr50kKSt5zsTz9t%2FdLAH1ixKFfLCbZqk%2BFHbz66oRabfkjGH%2FVAVT9%2FI5%2FMKwaOrxXtY%2Fus%2BDHVS5BI8hnpTWnxFILygxjySJwCmdjvBNhruTrssExzDeyM72vv9rKjlThv1aOGx8GKMtpDJheybAU2X5sjQQMFKmcsZkmmXgAkwCuh60WRHYleiYp35pcmR2LvyOlNn4O%2BJiZc%2Brxi4N9TB9K24I2tUbrE3XrFVF3gQmdpUF2oS4JKAWTew%2B2uzf61E0LUPoM96%2BWDT6FbloNz%2BwMoOVE0b%2FM4pd5ODSeOYQ1w9C%2BVdsnAronqZQmLtyhMH0yFv%2BlQ3v1MBbrtxfytMZfu9Z5Tc56b95HbTDiqOm9BjqkAQtKvZVhAcO%2FAJirNMmgwzkBlCWuxz4JaSYRfDfQdi%2BxOkk9ZMI0fBA%2FFIwV7hL1xxPTh9u87dPCHADvEX0vi8CTisJiB0lNe8WNuITuxbdwuZ0iKwiWdFoV%2FZmylJpBQVuW44PgG%2BIc8vW%2F5edizOzASif%2FpUPp3717xa7QDHbSnPjtfk8Jz%2BQ3N1vMXmf%2BAKcfmHzZ2A8Qpl8iwEPH1LQHfuNs&X-Amz-Signature=707bea12bdc638755bd2af6ed22670b8746a80e68c6138f0eef7b9360c96b6db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7P752VT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvB62DWura0QTL6ZeFEUay6f4iyQ07dtkUAN%2FD0YLyZAiEApHqubQ9%2BHOnzauMr6xOayDJ%2B2QmUm8GoQ1yIYfQ7wn0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfz5ZNcFmWEdNJyWSrcA9mmBSTuTvz%2F9CGnvKG%2BtM6%2Fj29VKr%2F3%2BAaKVSOIwzJf1OJFzQX3z9dZwd2HFNwWABZU%2BEYAZgU7P24hnKHLVL%2FSsOzTDxPt34B9VujhD0IgMqfXsAq%2FWVrZB%2BxWLy9xEtZ3D8NjBGgIZHasOvNZcBvDqJaj%2FiE5WQgz2689a3hasTC6pvD4Zc%2BWPCENTqjpcGZrOmF0yKoZ4%2FtLjdW6YDZwHrHwNdrxWjZYsrOHhs2UbdEemxMxYKPobZVPEe1ZAHy%2B0tNKQxx0zxRPNbvNPfyp5883HpO77nDNwji1pdxXTcosG4dKZCb6V7F0%2FoNUb7WtC0vCcOjWLunMFeXiS1EcPWc7CFemXS1SuExo2eYHu2jYfMC4iRFwEzUDURpKWT1G%2FzGYUrom3D5AwVYB7gpKNeNflkwFdAH0nly%2FVowAN%2BkbuD4hYuO9jm2YvrlC8sAQkVvdw9W%2BHbIBeN9P80auQyHMa7WT4zQh0FSx21wePwM%2FKdeqBo9PgJHwQZ%2FkyJhjKLvQrzyzAsjtc4ZXeedIU7oGrfE6o6qCbyJa0YBIQRjsmOAtEqu1%2F8VaizSY5Fe8ON9e7nfB9Pg%2BANo8Wj2UnUWPHQQ8NZSBO26ZUxR5OO5HaDrKV%2FV3UoMvMK%2Bt6b0GOqUBf2rXemCCVxp5QjO1pc19iRWgheANO9OSTlJ%2FfgEjsoSkma0%2B8YVfw2pqk0M38KM54Sr1XmgZIhAYnwem7m2pKkam2wHt5ruJmzu8BjyLyzS%2FXAm3%2F2SP5sbk%2FL1e%2FK2fabdG0slV3d6sqTjRMFbWVP3uhCGpDHHH7W5V5Y7A%2BWCkm7heBbufRJVi%2Bnjiz4xFc7Yt8hM1uVH%2Fc5CSn%2FRsbkq8IEqi&X-Amz-Signature=8a40e623abe96950330cdd467f1709ddc50e622e79a95c6a84dedf6e3af66a3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7P752VT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvB62DWura0QTL6ZeFEUay6f4iyQ07dtkUAN%2FD0YLyZAiEApHqubQ9%2BHOnzauMr6xOayDJ%2B2QmUm8GoQ1yIYfQ7wn0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfz5ZNcFmWEdNJyWSrcA9mmBSTuTvz%2F9CGnvKG%2BtM6%2Fj29VKr%2F3%2BAaKVSOIwzJf1OJFzQX3z9dZwd2HFNwWABZU%2BEYAZgU7P24hnKHLVL%2FSsOzTDxPt34B9VujhD0IgMqfXsAq%2FWVrZB%2BxWLy9xEtZ3D8NjBGgIZHasOvNZcBvDqJaj%2FiE5WQgz2689a3hasTC6pvD4Zc%2BWPCENTqjpcGZrOmF0yKoZ4%2FtLjdW6YDZwHrHwNdrxWjZYsrOHhs2UbdEemxMxYKPobZVPEe1ZAHy%2B0tNKQxx0zxRPNbvNPfyp5883HpO77nDNwji1pdxXTcosG4dKZCb6V7F0%2FoNUb7WtC0vCcOjWLunMFeXiS1EcPWc7CFemXS1SuExo2eYHu2jYfMC4iRFwEzUDURpKWT1G%2FzGYUrom3D5AwVYB7gpKNeNflkwFdAH0nly%2FVowAN%2BkbuD4hYuO9jm2YvrlC8sAQkVvdw9W%2BHbIBeN9P80auQyHMa7WT4zQh0FSx21wePwM%2FKdeqBo9PgJHwQZ%2FkyJhjKLvQrzyzAsjtc4ZXeedIU7oGrfE6o6qCbyJa0YBIQRjsmOAtEqu1%2F8VaizSY5Fe8ON9e7nfB9Pg%2BANo8Wj2UnUWPHQQ8NZSBO26ZUxR5OO5HaDrKV%2FV3UoMvMK%2Bt6b0GOqUBf2rXemCCVxp5QjO1pc19iRWgheANO9OSTlJ%2FfgEjsoSkma0%2B8YVfw2pqk0M38KM54Sr1XmgZIhAYnwem7m2pKkam2wHt5ruJmzu8BjyLyzS%2FXAm3%2F2SP5sbk%2FL1e%2FK2fabdG0slV3d6sqTjRMFbWVP3uhCGpDHHH7W5V5Y7A%2BWCkm7heBbufRJVi%2Bnjiz4xFc7Yt8hM1uVH%2Fc5CSn%2FRsbkq8IEqi&X-Amz-Signature=c290d5da09e36398343e6dca5cf816f21b0c96d0f179de7f3b1bf24e126388cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
