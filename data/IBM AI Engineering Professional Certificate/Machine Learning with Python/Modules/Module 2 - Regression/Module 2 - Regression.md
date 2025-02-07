

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=bf741c111d27cdc6c6d27933db32b5412527eebe8a6ee5e66593afbc83f039a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=21498b6cf8e9bdf56daf1bab692514a27f6e5d34ccffe81e7a594687ef3c1a4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=73c725b219d0a14e199c682d8c4c8c29d84ed460b1aeeaa606ccfc2136bba4c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=5e20fe4ff2ad85bac248c27a9a4f12c1ab0e57b67761ac31fc93f23e0d503ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=a17cf3a76b6f8ba09b95006576e387eeb68c44294042bde5cfdee95649f2685e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=b830103402ab912f036ca7760e70add7790374a41e97faaa5e2d7d7f5c69a915&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=bd0bfee04f03102482ac83422e406f6c80b28842cd23c10e08c57dca8b922cd8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCEEVFEA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBQCin8OXYLJK2clsrX1yD%2BBnI%2B8BXcukXk1Uw9dgZc7AiBaAu7l5Xo0JED%2Fjaaz47y7jHwfgMG9%2BmCO4p8wgkbn7yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMh6cgcIDGCeSz3ibNKtwDMZBDkNuA7YkEybKU%2FFKL2fi6l8nklghpZMf%2Fn0r0TyilQ4GPNZQ%2FhLQVYXfvFgDKxxi3HI42IRRnEA2kGmlWaMtDKHYaRlG7JlVPGX8XkcL9ly7a897va%2FDo4%2Bl26RAG5DwWvxdqfrdgXDzErltXV5zd5bvUHmUbwzIUq%2FYQxQ1h9AhVlBsx%2BzwSuFsTydFaKHAB2eAv4hXkCzpfopby54ug02g%2FOHbH1bMFaBqJQFIy5Uci%2B%2F2Ev25ch6fghZXYq%2BjaukxaIm8hhVxE8sOlqyHRo7jOp5m%2F%2F2%2Fj4MVQ%2Be9w3OGVbsXELKJT753p4zA5gpkvB%2BgwSXNw7yp%2FOiVqlNPf0apa5NFDnA472i9iArBqclEyQc8ieyqAVUxslU3O0BjNb18BBnGXZF0GecXyrorNiAVef44jZcppCu7dR2fzAPRW4JSCQxOFFaxebJWaIYd8d3YnB2RJiU0K4p2FTOvk7wv1fq6u2CAW452gxuZMPl88q5E9tmtK0IBBIHuphlChL1Mt2CiglBlwa84Yx7EMJmHGLRQrYbpsKY%2FMTZDEHQL6uhPHnzR033a6lE%2FgCT%2Bf4vELhmFu9GpWZirI0oOt7AwlHJOGsKlYg3WVthNhHQR%2FkdmMa9nuopQw5ZmZvQY6pgHl0zf23s53pEJRUipCGwKDsDxWMCRGrT3Y3RXAJdNQ9PamJ7k%2F7f8bjnXZfDskHdo6fgYLs%2FmhaTf9n96oEygo1dNNN7Tk%2FynqpdAjvjuZaG4xaxBvbsueHYtxqpd1pRBRHJa%2FutIb0xs2OdOe38oSFmgr7NOoVQ%2BhvHSMIgypSMIgDg8fLWBWDHdXEGOuKkfbpMIHxiP1DxZZRtQq44KRslw0T54G&X-Amz-Signature=015fa305076076f33885889d86b0f90ba63cff26c06a320ba4f6f9b4ddf6cdb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQFVWKKT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCKD8cHfnMyoSGMNac%2Fnsr%2B7NMSsFUd53%2F6lPLJzOJfMgIhAOk25pI%2FQKfG1fsfqQwPK9gUzPdFUw6I2b6uIuXs3UdxKv8DCHsQABoMNjM3NDIzMTgzODA1IgyZjwTj%2FBSl7tS368Mq3AM%2FTXtwRQEhPUWocmiIo8YqwttABn89di1Ijv2gd0In6iA3gRFGKIQJOQFvRKSlTekHJVUR%2BD%2FGRDg9j6h047WFD%2BO2d0Ctlg7gjBPiuA%2FCzMEg%2BrhDuWng324WcTYbzmA7r9bN5MKudqXHFanybA0yBZSlreHBTbcQBhdGJpN%2BTUK1Fyyr9tB%2Fsz%2Fcq%2B64oPoLQLbZhJ8sRR28C7o2AHwRJikNcbIh%2FlcckP%2Fl0RpgmhyD3m1gLCw8u0Da%2BmHVQF2MvTDkir3ZAGqZgnx8D2IRWoeVHlvzEyXKS4pVvi4U%2BoLTNKEAqT%2Fzqf2cUyKq4mWDuaO9TDZmpqVCoNClJSpe3%2Fo6h6MUMuSsIjPZyuMKLsjI6AsG0pjrW7V7FshUn7cipG4fAX8Us4d8Oa5CzFB%2BeLhROdhl13gtdoELZYgH48VT9t8rY8o8BEm8QYzkERJz9zejutrrTweB0ZoUZTBW1qia1N%2Bq2crG5u7RdeZTOB%2BAWos53VNksTLCKidfmoc3XLm1v8jdAEHceMoSeuROlINUyQ85ASRwo4KdaNbj09cwbo5kPB4ux%2FlAVLTQmBllnfcuIi3C4Haix%2FRvnyP3swtcVFWjlRX89QKohhfF%2BkOf8YyynaHbvCOIrDDWmZm9BjqkAZQ1qLokHRCWcbGC65Z6miAnbZrbdFysL8fk%2FzUUjuRYltt5L%2FlFETHtDaq0G98Kx%2F2npLeqGOclV9sTUN8kW2tXJDVRpdmjB2l28iyeDBIXpVc4%2BIRVpe6w5kv%2F2CClW2p7zRSAXe9gvmbpcqFW%2BGUTDSkb4UvkpJ6z1VXrm3neiEq93QUKtRATEl%2BpSNpLo%2BjmU9Kld9ad7lXXj7T2PprsrawN&X-Amz-Signature=9ee479f84ff4149a33f5ed3b48880ad686333cffc8c6882f46b3fb529667107d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBOALQZE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFXyWWsl8AIjLjovbWeuEXTRChMq%2F%2Fsmf1ytWTq2XUyjAiEA5%2BTfCuJORAt%2F3qZf0oAaAxF2aFs11YAqmaEF%2BfY5stsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDOuYEo%2FwJUVeQScDVircA7RAk2dvmjztiJ8xzbczsgfpGUkGoF7eOmvNB%2BDvXWG9eZ1jVUaRHIlkIscqxtR%2BLRIWl9AZuKc2AuUx0SQ0oxtqNFY07%2Bvjev91k9aZ9phg2FDc4lcGHspPYH%2Ff%2F%2BSf%2BfLH2vE7zqY0W2NGoTWjLFyeBpV24nmBfHv0y78ZChWcEecl%2B0pBAkHHl9zdVhkMmKtxlsZH%2B%2BUZTSNG8PVmoxagnf72hmATZLsA0gZA%2FO3FvG4yoL8TwKep0oC8n5h4TPbTquh%2Bbv3Q7tH9m5CiUROXwujYTu1tYAq4sdoBU%2FNt5cW71Q2GFGZNeI91DP0doK4xC2U7Yl9jeQVy1pLUMNUJNq3Hj4W6LYfUeh7fOZwvazqzVv%2BUTP%2BWPqxPEwrzorLna%2Bna1PB1tLYF39bOtoS%2BpPzroXgEjT%2Fy0KpptLBPhPWqypsEjZqx9xhEhH4babAHVaKOf9iHJN0DEdQc%2FpLq0ztTfuI191FhM8xeJf3kJmwyge2%2B96z75ls6ON4ttvP0rpqz%2FCH5OQwyFlEECCc9U5dkGjYAKvcTmJ7uoWgnIXl3LsCVeit9AxwHwAX3wbY9aaVZrEkT4J5GGH5yWrKI%2BRXc%2BZhcWGl3vYTs86q21f4DDlJiEzXzOYIHMMyZmb0GOqUB1n8K6YK22wHP0XCYHEoXBuBfOg%2FnzU2KdXy1jdZnYLPNry%2F7H%2FCmwzDRjDXn69TxOANSvcYH4sZ%2BmR%2BBtM0rl%2Bc29Lx2Wq1KITNJWDB8Bf9CTRiTuc3puSTOpl2A8gvKHxgoaNFSchh%2FXrCGlg5ch6MZ%2BsP63Rsb23Bc9%2FQah2FPx1qg38N9f%2FV6DRPkOWcSFJAwu%2FzOwq%2BNPo2%2FYOjD9WO1d7hW&X-Amz-Signature=030289d5305537ac11d73f89cfdc9fa70d5193080e2167c6260acee0446e8f07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YAANQ5M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFskJ3st0%2BS6lSgAcba8KFZIukrrfhZ3PdC73tOP50DeAiEA%2F8oeHi6ksug8F1nGWRV8Jb9uIyhLRmv9Y6xY%2BX82Dggq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBFlMXfQFQBYM42V2yrcAw08eYPojesQ5LlRlCtQ1AvkIJcwUqjm2aGTdfpmj9p3PDp00PInKqIbuGK3IHy4Cscp15wqtLclWVGQNsytSk6kepemVvlB41cOFUtwdRvntps5MFODraYCskI%2Ba4jZLr%2BGavZTsG%2Fv5ioIR%2Flo815HYbpi0O068AcYBaph%2Bp6EXSNMs%2FmIcTrNj8oaA6UH%2BOnFEwTolz4rvXjmtvpc%2FCtDljM7WIH2QfNG8T2lEtdBiWBk9KDQlu8OiH4y6HzX3j38siOaWwBcDR7HH33PrqYjQDz2MLWZf%2Fc65fwt7I2mmk7F46Jpu%2FP7UfyfcU5yv%2Fg8lkLbVZXtYazv7VG8mJV53WeLV8KhGtG1g2UcDFNsKNSC%2FmkA3GVGlQ7qDL4WJkpfBb78zPkPYYNsEugvFsblckYjaCKZtB4jvtPmL3kNPllRWZp7ztazdLRED4oD%2FvB%2FvF7MdKZAMtvsHCgsT6Rpl%2B7h7CzSapbzBfvV2I5TxnGhy%2BB8s0tPR6vYY6Q2ToNjj1evD9rSVFlqonZPTv7E6tiXB%2BI9NgBbQ3Ur3N5OOzHJ1lHa6oGmkFnHVJYwXGklpg%2Bq27lI9%2BSrKdvHjcMtNkidHveaxRN%2FriPfj4mwA3ss9UTpIw5UxBKeMLiZmb0GOqUB1plj9eFQHwyK7%2BQryGPN5jh6cD8Ko%2Ff1UxHIapxKLlWmiuBSiZKLxbpADCsjhLICgZARTu60DHWaoFRXNBpgs4ZTvhTqBHOgYcr8T4MFHHyBviEhM6eb7hn1qFayy77kaJcT4VlddVxUDbMh3B%2Fj93KBB5XJlzlcp%2BSiF2eqL2oLSGeFy6p9xuarVOyCqXQHJ1ck1KpdrTWEtS0mY%2FxNEq%2F5JOTk&X-Amz-Signature=5d14cf19f792ca0c353943ae33323fa73cc5803fabcc9bebe7ae0ffb34ed5a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YAANQ5M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFskJ3st0%2BS6lSgAcba8KFZIukrrfhZ3PdC73tOP50DeAiEA%2F8oeHi6ksug8F1nGWRV8Jb9uIyhLRmv9Y6xY%2BX82Dggq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBFlMXfQFQBYM42V2yrcAw08eYPojesQ5LlRlCtQ1AvkIJcwUqjm2aGTdfpmj9p3PDp00PInKqIbuGK3IHy4Cscp15wqtLclWVGQNsytSk6kepemVvlB41cOFUtwdRvntps5MFODraYCskI%2Ba4jZLr%2BGavZTsG%2Fv5ioIR%2Flo815HYbpi0O068AcYBaph%2Bp6EXSNMs%2FmIcTrNj8oaA6UH%2BOnFEwTolz4rvXjmtvpc%2FCtDljM7WIH2QfNG8T2lEtdBiWBk9KDQlu8OiH4y6HzX3j38siOaWwBcDR7HH33PrqYjQDz2MLWZf%2Fc65fwt7I2mmk7F46Jpu%2FP7UfyfcU5yv%2Fg8lkLbVZXtYazv7VG8mJV53WeLV8KhGtG1g2UcDFNsKNSC%2FmkA3GVGlQ7qDL4WJkpfBb78zPkPYYNsEugvFsblckYjaCKZtB4jvtPmL3kNPllRWZp7ztazdLRED4oD%2FvB%2FvF7MdKZAMtvsHCgsT6Rpl%2B7h7CzSapbzBfvV2I5TxnGhy%2BB8s0tPR6vYY6Q2ToNjj1evD9rSVFlqonZPTv7E6tiXB%2BI9NgBbQ3Ur3N5OOzHJ1lHa6oGmkFnHVJYwXGklpg%2Bq27lI9%2BSrKdvHjcMtNkidHveaxRN%2FriPfj4mwA3ss9UTpIw5UxBKeMLiZmb0GOqUB1plj9eFQHwyK7%2BQryGPN5jh6cD8Ko%2Ff1UxHIapxKLlWmiuBSiZKLxbpADCsjhLICgZARTu60DHWaoFRXNBpgs4ZTvhTqBHOgYcr8T4MFHHyBviEhM6eb7hn1qFayy77kaJcT4VlddVxUDbMh3B%2Fj93KBB5XJlzlcp%2BSiF2eqL2oLSGeFy6p9xuarVOyCqXQHJ1ck1KpdrTWEtS0mY%2FxNEq%2F5JOTk&X-Amz-Signature=d6936b87cbb6662cc136dac68ef031f08ff40b226fe3866ec937a5bd914f0c86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
