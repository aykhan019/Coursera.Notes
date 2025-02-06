

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=07b20e4af1f846e24e7fcffe07abb2d27d5dfa662cd2cd6c64e6783ad2c633f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=894625f316d8f75ad6e2fad65d5015f0cf264354005acdd5acdd5961c71f8bce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=c28f2ca55593ab032faa18ff0afe78e01f125904798396d5a70a517928bd53f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=a4f5262a7e80de08b26954e7179e33547841f69e2c599e1e42388c496dfdaa90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=1f3e5e70113e8592421ddc5e42a61f33cd890000d230145427d7d776e4661e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=c2f3f1d6d8763f8a7d852be8cbb3ba5344e6e377c200e76b8019676f604ae392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=0140506a1e3536800652b2958356e2172518d48b26d01bb205c9f24477ba6545&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSERW56R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC9VjkWl%2BagJB%2F2lU8AEVdQuEwBIuGD8N79wXCYmg4jYgIgQnesv1lPDzXc6hQ1N2h46YorPhJnnxXIqW9dFuqr96wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH%2F5tAMp8LrlCgBSgCrcA6P1XiPb3CKqsXgG6yH2pOwlCJmLJeT7%2BzCgvw9E9l%2FKhxQeHgNgfAXvXdxnRMmWUGxXFIDAILYLgSfX0Cs5ToS8xmJq2yflSBEr5gxRgeviNwkTDgWN170XfRxCgoL40GJDao5xs%2BdCUdsuwSQfVe0XfybWGEVHww1vkNeQamKDmoic%2FXiJZ4ombbBMeKlgEO1RLGA%2B45zcsgZ7jXvdQgdTBLvDJxj8wvxJ3GANknPjKbQSPhs%2F8Nt12hu4L3c3lKHq%2BQ9OVZDhi0HJeBQwy5jRiuDzfWAdHYMuEoqprq5pKWXSN0jQ8NB0OPT5RXNJUvnaHYV3aMCghfKaOfFG5FoShJaYeRJffSirWzrx%2Bi%2F3u6eWKyYCErKXZdwhbb4xvd%2FUV5syAGeeLNiXYRQrlmCCmhKbvfkyYh2iW1YdF2awYUaCS8u%2FPryei0bopOtdCwTPKYOUNCjtHsPL24ST0jy07WHMq5ePVMuL5ZOLhMPuVkqoilzR%2F%2FmN6Im3u7uhGFzQqsSZjuRRUUnJzRwVFILqY9j%2B1FA2E5IUQNWWxOcx3B7JVzmyi4Ihx3a3Et35T0bnWqpc1nIGYC4kpRkoSNuH8z4No4JpPHWUOmyKpZJMmkUS0kgxfvEM%2B9SBMPibk70GOqUBLc8FPGSQy%2FtSBnKSyZVm4K2o4cmHK9uQUQ%2BXmkg%2Fn6b%2FhWmL4pWJwjYJYNWbkF0c7C01PCJzl5s2jg8qO8t%2FWjY86YAy38GurQwJ%2Bd7ZdRFu2yLVGfwa0edFHG10wOV6uNrbB1r70pUgNnewfw8WY89xk7g%2B0jUms1hFrUSoDgihGzAaJQTxCQBBQEcmKssYhaxej3x0wYGr8LOZJ4E3BkDfw7Gd&X-Amz-Signature=adf9c8c6a592320aa298625268c32d4bae047f4c2c457a8301fb4d4fd68eb7cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR5Q72HS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCx2S3c%2FY%2FpSqzosLx%2BuNJdzvGNYGa7QNbhRMk0NsWXqQIgU0tqTYH5qDzsw%2Bgw4DG9JQKg4D3hE1m7iInH%2BdqK9tcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDPdlY8wkh3bPsRW4eSrcA%2BnLJDE9VkkCm%2BfywD%2Bf8UR1By%2F3QoJA7etnbrV6ZX0kR9yT2uE5uYw1RZCsxvPFh%2Fouim94jOTVLjh%2FMw%2F4%2B%2FyE2%2FD5tU03poJFg8%2FRVwfbf5vrq0UcjrRwyVh2xbpjQWo4mgdVbM%2BMmNZ7KYtBWY0pdXQ2DY%2BWu%2BCEbAu0QnbgNWPcIRXiGNGhdumYzuqjGab6CxH4KmE2%2B8efuCQM%2FIjrNYeLz18n9Zoy0dbhDbixA%2BeBG8FzfNkKn5XdWJKl6FA8UFM%2BMmOCymRy5htNMpRqgn14wqHybUVpv7rIYbPVBW8XC3ZhKS%2BL6i4t1J0Mya8VXsR09EGi40W%2FADaggDsPC1k9dFgETs1fXxf9J7HeiHHPmvaVPMrw1jTPwLuDIZuFHEjtuqSTSdGPGfzThnUzAL6IXkts8N%2FQMMB3WjkVFBZ3PpmYDwZp2StmLrzyf%2FjParPNL7gdl0KaeBF1FqR09xiWO6byEPKa4h3jRt7UgD9EJsL2B5YplrcUdGLezmkAqCb95ERBqVGZMsc1hT0F3CcoEKtyIUEoT45xlK5oLfjub%2Fvllb9ihvtNDz2xH%2Ff2YLDuU%2FCKRn5a9W6HM%2BhN6TuPfouNq%2B1hmewmtxgELYWws6BAUfu5U3n5MKqck70GOqUBayGQ1pFcU0QZPAXGhPE52YlnOd0cuQAAHIamj2cOa%2F3zLMlB8zJUFIKaKVjwbnNTLlLWAgSRd0lq9fSsPS9sKqHMhGVRhNIibJtMnlsm%2Fyg9VA98VkUkE%2FqOEIH43gu1zsiWBwPBqjx6u4Ko%2BE9jzDtNEDiAII8y63LtC8J%2B1kvHy0wCXY%2Ftgz5zURu8bM4pLFZtHIMD9jR%2FGSyRrpJkmUoFlXtQ&X-Amz-Signature=a3ef91598e5e3950066f058926dfb23768b5694dc1575071ea96c03fa3b8cc3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WG2ANRE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCZuMafl64tJ3IrI3IlNUmnamvXe40fmKe9fBGPvDuKSwIgJNGhSgnJsSG8QHxen96cqD9hkQY5Qb0X5Fq%2FXzQyz5wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDEJWkvTw%2BCt60xP6ISrcA2aRP1Z2ANCu5%2BabKDrfWHyNQ1Sp9jWvs4z6TVY6YdfIhmqNXSoSZrvKqQ6oml6BDJZYFrBnjPjLqrPhyzZQUvINTItSCAVntzcDt6%2FiXJie4qaQtHt%2FQ7xyi5F8JMvFIx76Pkna1PMT5DSfUEZu%2BxzDanqbntZUC05Dp%2FRVFGXLA0H9gzemXkug1N8rlz0oPmInZ2VGr%2BixXt7ocAbjXcLlkph5jFUFkS3UUaF%2FbHKuBVKGmuBffAEWo9kR43hfRo2pa48SF92lTYSsw9ys4iPll90z7l7TcV9s5n6JyXBKcYggDxNtPBKyspFyIPr%2Fd8bQJJ%2F345EOmH137l%2FFbdV26JSCmJbxEl3vdKsaMRPDuDgsdjSnmHM9h3vZDDO%2F06kvS8gG%2FhDVVgduiUcMAQ3M5WdJv3n1jzSHHEBRXQ1jJWB%2BDqRJMDajrT4indMVK7My6O3c%2By3RpDq36FYAD%2FmVlNL4%2B09fiWCpoqHHw6TOgaHFOVpsM44KZGoDgQfjnLI5yjhN1JrsttJQTvNrJSg7jOI4UXVFd7SBVz2ptJzDGZECuvhrxrD6FyRBo1ZvoubIWMeaavYgT9wtgVXYP94YXLhh5E7begjtX17YSSRNvbIBLS23E4WQbY%2FPMO%2Bbk70GOqUBHbJbMueteW4KtJN%2FwxnZ7Y3CBTtPXi8mjdvA1ETe4ENqhTIO5b94QYIeBUtktdB%2BwEA7ub4uC%2Bz7D7zRJrFd48mnbq0hErRZl8QLW6Kk7QvhYTQKBZximN7mgvMJgwHF3vfq6m9csSZQ8HwdWcAx0kb01tM922yhdFLyQNfQZc%2FkjJRTw6FLCYmHm1kGVCZ8XzhowNHzdCOLtaAfcg4%2B5z0qxu%2B8&X-Amz-Signature=edfe0da8a3b69bcb597ad7a5cf04d2f98c681c7fb5f18d9064852ce7b25b914b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WJ7FR2W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDCLJhllqzaGZAjYy6uLla6iBbnkbo7KtW250xQKCUJCQIgCtPB7QKVPhJswAkffH1%2BsPVpflwvverhEUPR3WBbJCAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDME%2BCry2Do9iz9JpbCrcA3rRt1OgNvDPX%2FP7VUkpm%2BZJiiEvmbhQbLaF1xbIzN5%2BUOv4xQH%2BxSJODX0ADOoqnjhhu3ql1GeSVU6KVs%2BMbFjSyalIlCHV%2BwiQqMR0P7Mjf5JZj1GfthX3P4JBXCha7L8etTGfA%2Fcv%2BdYVtpa%2BSvf9fahpysvrNy3Ws%2BaJsFJDw6CW6Bqek%2FkzsA0nBMilGbdDB3KP4dZdyFLityJZ%2BcKBey54juX9u9qYfvIZfn%2FVoR3N1DO%2F7vbHymI%2B0WRpQxxI1%2FMc90uNCq%2FBYvuCxiXA0fol8YdcHNCV0Gs%2F072ENoOIeiQvgM6yuqxMmIvW1dixC%2BRLzfz2V5RrYD73OU5R68QCOwKyxzzeCqRo8%2BgeZplmWP7NeLxOf7%2BnIw5faGVz%2F15mWD0dn%2BrzeWjG2SOfEqWEDU2wk9cZ9SZdyelEEWQlOEDmq6EGX1JzcbudxQFTAHiy7GxYhlwRFMNNsePaXb0TMeF2rhWOnANUdioAoyqmXR%2BcTxQ8bwrp34PWkgg4Fe3w87LxcImckHCR10f%2FNeJmtK5Vir9dUsh97GqN30ey8rL%2FIZtc2AMpdtUQ8nbfUQ%2BQrEwpFTgErcjEKecDxwQv5G8RMgYXU4yK0Mi%2FcTt%2Btea8%2FbG31fHxMMOck70GOqUB7A4coJMq811vWETOcC0xJR%2BCXPxH1WjgQM%2FCyoX%2FVgmzg%2Bvkn%2BBmJw%2Bfak6hWYUPqgxdhGwa5WaerL6UNkXYTG9VPqsqdcCU2o1vTCWG2rcJB9KCqfOEccxYWa8JPcTtTOKdItRxp3s1NMZKtsonOriGkImIfbvdfd1EdeBM8yQjz5%2Fij4yTUKjV7LM5Ykm5WJD0e2oZypFdhRxsvDNnMDDCT8eg&X-Amz-Signature=9f4028e15a6dfebc084a6c197d5f8eb616c3a6603a3ef6506cdf98bf56f3ae84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WJ7FR2W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDCLJhllqzaGZAjYy6uLla6iBbnkbo7KtW250xQKCUJCQIgCtPB7QKVPhJswAkffH1%2BsPVpflwvverhEUPR3WBbJCAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDME%2BCry2Do9iz9JpbCrcA3rRt1OgNvDPX%2FP7VUkpm%2BZJiiEvmbhQbLaF1xbIzN5%2BUOv4xQH%2BxSJODX0ADOoqnjhhu3ql1GeSVU6KVs%2BMbFjSyalIlCHV%2BwiQqMR0P7Mjf5JZj1GfthX3P4JBXCha7L8etTGfA%2Fcv%2BdYVtpa%2BSvf9fahpysvrNy3Ws%2BaJsFJDw6CW6Bqek%2FkzsA0nBMilGbdDB3KP4dZdyFLityJZ%2BcKBey54juX9u9qYfvIZfn%2FVoR3N1DO%2F7vbHymI%2B0WRpQxxI1%2FMc90uNCq%2FBYvuCxiXA0fol8YdcHNCV0Gs%2F072ENoOIeiQvgM6yuqxMmIvW1dixC%2BRLzfz2V5RrYD73OU5R68QCOwKyxzzeCqRo8%2BgeZplmWP7NeLxOf7%2BnIw5faGVz%2F15mWD0dn%2BrzeWjG2SOfEqWEDU2wk9cZ9SZdyelEEWQlOEDmq6EGX1JzcbudxQFTAHiy7GxYhlwRFMNNsePaXb0TMeF2rhWOnANUdioAoyqmXR%2BcTxQ8bwrp34PWkgg4Fe3w87LxcImckHCR10f%2FNeJmtK5Vir9dUsh97GqN30ey8rL%2FIZtc2AMpdtUQ8nbfUQ%2BQrEwpFTgErcjEKecDxwQv5G8RMgYXU4yK0Mi%2FcTt%2Btea8%2FbG31fHxMMOck70GOqUB7A4coJMq811vWETOcC0xJR%2BCXPxH1WjgQM%2FCyoX%2FVgmzg%2Bvkn%2BBmJw%2Bfak6hWYUPqgxdhGwa5WaerL6UNkXYTG9VPqsqdcCU2o1vTCWG2rcJB9KCqfOEccxYWa8JPcTtTOKdItRxp3s1NMZKtsonOriGkImIfbvdfd1EdeBM8yQjz5%2Fij4yTUKjV7LM5Ykm5WJD0e2oZypFdhRxsvDNnMDDCT8eg&X-Amz-Signature=7ba3003fb8d92ada826f3f104cda8b17245a529b85f6a1a29dfca6c1636da802&X-Amz-SignedHeaders=host&x-id=GetObject)
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
