

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=faa981e7ef4031217ca6efcda08f347a8733dc58ec7c4e94b2795e8fbb4da8ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=029be287cf83637ca5875d51a000e4283a8c47936e7e0c54ab9ef58393b8eac7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=94be259c09dfdcf7747dcaf3f92d859a054d06af114b6216523936dcfd1ee783&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=80bf21d7535f615f095f5f0aeeaa089b43ccce776f7cb07e1b16769243823a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=ba603119c40aa20dab5e583866b181c62c00059ab1a428e17acba95205dc3ed1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=7ec6ea3c05b5ca543338d5d067db5318b5fe73ed5d1c9c5cf57cba5ee9cc5ed2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=debb74380da26fc2042c86075fe871852749dde980f66305ee165edb84e78e95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ILR2AS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQD4d5oGPGjWFCKe3YTLNoJFTRy57NYOdYwDeIxSgXTlPQIgT5Qoped44qZ7dgN1hMMRLOL7H7Y5ILpBts1He2RE86Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDOK0l9DsX9XLdhneECrcA2L2HU8BEiim7InelDQqH24rg5byY%2BMNzSf6Jwwa8Ay88m%2FsXAV%2FuVONyXJL3ux%2B3otAyUapELGD056U3%2BBLJq5Vi8EanN5QlJQS8a7D0fk9g4mhqT6tDdpW8JX8K%2FalO6NphAscS4Pq67zo3EbGX%2F8Jeep94HkLi156VotE1ME4UCbvC6xNbLcz5lp4I2LO8mfFnQqTE0BKL7j%2FUP6%2F1e%2BcQxROEHX9aE%2FIETg8JYQnOu0S%2B%2FaGawn7R17Xgl9Bch7U4R%2F%2FI0fJT2TIUCNoyjfhzobeq%2BkYn0ChymIE2NCsM9%2BAcLq%2Fyz2aZ3kohZoiQxYbT2fri9inv3gn16D5bYKWqO8NIdFLkkwxPif5qrKiJ2aygc9YP2w4YUcQez1UoFKvtg8v1Jk1Vu4Y0ckneqFKV%2BtmsF5wSs%2FNp4xY1tLGx%2F%2F84bMNRLpN4p%2BN8kCc9sGsRXjVemVytb1WOFHHvY3IA7m4bVU0PotCqJ3Wqs2L%2BJTJg4K%2BrIN%2B%2BUhVz1vk%2F%2FgfAK3rQDAGn0N4XUDxAH8xfs0RZxRP8Y4Ra38ptM51ukTcyTzPVgc6Tt%2FFrS7T7f1k1O%2BTuicaqE%2FrjWujKpYntulRLSAUG%2Fg77m4ZWfoZvlJC9R8X6AS9dv3fMLqilr0GOqUBYM9Cov83ptOwyMUWikT%2FnUMvDl%2BHi0Cntq%2BGTFkThnnlRSaaAYCGefwrLhGRJGXQ%2FWSb9XPVmQZEg%2BYH6gAAY%2FjS5LgRwWl20QYdmsDIG2t0KtJFHlymiXKzxUTLt26XKYFUn%2Fz31m%2FIQ0P0fS4GCM51zUYKsKPoFaYpBdzNvVxdKnGGoGZuyO062Wi%2BRdJL%2F9XObKqbGrOg7yKbjzpww2xkKlqP&X-Amz-Signature=da71f6aa4670fabed7a632aa5db478d424940d83907457f37899caedbb604516&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OS5OSE3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDMNlBUjZItgH86ek3HLPE4HnmH4k%2FBBkUXCHNVlunxeAiEA3I89ovnbAh%2F%2BTKkK9JC3qFD1fYa89SSlN%2FZ7TF5l8hYq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIFVDhkZo%2BIqgHEFXCrcA2aKtKsjZeV6PwB%2FPe%2BovgSNei7fjEaIiqxGgcRs3H95NNArTi%2FZbCURdjyaJv35X%2FjCasgj0cV5EE4ZCxvf04%2FIAeucH5Q8Jsu6mTDAkF1mnsa0mphk73FQEiW1orHKVouzTN7ei1rZgNmxJ4ZkPEDh2ciSHfWVF9rjlAr4MDEr7D%2FvxI%2BTXHp67NHMycngHNqeaGrKda0fzSEa%2BOrPd4yaTqGON%2Bop5MN1LjdSuZDSVyT8kKDWPcFdP02%2FA5eO8lnPm5zY7UWqyK9zjyCOa2t96dkL06SO53EQvg%2Fd%2Bjqb9Nx6hwdiUFpYSCZFLyKVXHr4FKC4%2B8JzgegcO%2F1UOUOb%2FfthMcjUTjfUNBq38O6LYS0OApc9KqiVqeeRl3dhtc%2FQVT5lZqj%2BFepnii04KYJ8ffaMX75PBeYdhGAixZRXeDM5xFYOMf5gS3%2FHY0MQuIuAl%2BtFVhUk93neKy7DnVwIcimO3B6bPH8s1YssUCyT6APKuFDTNGLXjIcoO0xJ9wSrAgZ28uSznaAYoAwyAmYSl3%2FbuX6XbxgYX%2Bf4bawNU%2Fx9q9XCGdKBz0cEpYeIn9f77UsiG4kcPzqGnGXXxIIzTM65cwQaNndWszq17PxCO6RxjqNTfkuWjjPbMM%2Bilr0GOqUBzeIk8dIJPdP8tp0VhRij1iXcRyMdfMvh0r4nk9ceFh0I%2FLrIDGpxRPuBg4HvVl65WywREnY0qMA1vvanAED2%2FwubX%2B%2BboizPqKlJ34HhnU2gwcQJqsXf2cIYCNBXg5btGeObiDUEdEZdP9aCzyXru3bBz0EnC3pfF0ydTKwR%2BfAPmubi8fxftdUFGDa6MqpxUuRCaVch%2FIf9%2BH%2BRTXMMJaIY3USI&X-Amz-Signature=fcb7cb0aed388582727466c24cbd028067f30b060a0600fe9c8a9c3409de58d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664BJSCDZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQCZwMjl%2FxuqLpSlNOqVWfBTDPSXS8pTrs1BDnKISOvRxQIgB61K0P%2BUF%2FkhpblukUV%2BZxUCVvLku4khi0wL01CP4Qoq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDBmv1G2z7s8rl36mSyrcAwkg%2FkuVphpMbE6JMU2s45Ln43Yn79FBR%2BBRzI2WAnMtUvFwKrzgZcHE%2BrwIcsmGN0OM40kcJOO9%2FyTyR7gw9SQ2WxuJa3HXaMuQcQMzAmmX5Mbd36P1a7or73XD8MAabPJF2qbtD%2BUl9Lc%2F4nc4%2Fn9NgDv530b4gVaNxxVRZf7x3b%2BVa%2BolxJiYZc9lbK0owusfqkPL4GBFA2kMaJReLdAj%2F0Y1kEPNHSudS%2FLbSSVTdLGKeveDmmKtYGDzlMmDEzSulcZAdmSz9aG%2BTzX6AfEIhvr1Ec2cbHi2357AKvoiMS3C%2BPzTEjWB%2B4ZoRyBPoAHXqsM3i1Mydf7SoXjBG%2Bd%2BAJzVb5ndquJzOrxI6CDggCm9V95EmMlMnidItUik68KGi%2FMZv2oimmg1n7r1UpENBtdc3HUK9MQ9fR1FBfZ5%2BES9RBAU13Ni70NEsDUVW6Zra1DRQbA%2BXe2TeUPtC5ciDZ5bFjzj1CVWiRAhxoJ8KsjOKwKq2mhz%2FfLxt2KPS5Elie%2FCxR7D%2BAApvZGKBXS1XdiCSvCsytiQW29BoMtbJ1OZiwsE8edr3cSTJ6nMsay3dyk9aFLkZs2h6OsrJrk%2FZTcMvJ5XABKnkZLoT26IbKPZW1C%2BvOkEzia1MJChlr0GOqUBATqrN3QiJujkHPG9fTlvD4NYE6AvuW1rm8wjEbhIeoY3JNkpwnk4xb1WGFSg2XRRI%2F6dSjLKldn3V7%2F7SjaoPDczYWUyZpJyMe7F9SaaRDL80LxwfRxRIRP4tOLSen5DdHR%2Fxi9CqhmYHROavoC7PFG7NRfZh9fM09CEMTvlF0KR2eG60jgB%2BBzGdDCoRJ6Wz1%2Bp6wPpNiXn24hH8RwDZIC8jhCM&X-Amz-Signature=9ae87332103e89f998325777ae9c4b367aa2f25ae1b31d214a02510bfff73040&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYDJH7Z6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIEPwj03jAxfbHGctBTvtHqfT%2BCULTfgUa%2B8LgiXUekXIAiEAmBard9%2BOGITH4mTuxLIQCydoNrqwvmZkKn8QIOiqJVMq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDLBREF39WfgvGhDIiCrcA%2FYWHE1yYod6DsnVKFn3yPFpfl1OzQH%2FpEg2vizqCOyjC576C%2B2TH7Xy3URuycz5h8SPbJWyc3GoY9LB%2Fcp63Cp6TVtSReDCCT8s2yFKptr4QFhBkM%2BkUYYx1Ol33WcYL7QqphMUjW%2F6uj26xWnmmQen39%2BQgys6cwC61sHrL7q%2BRpjkWn8v8gYVL9UNoSm6S9in4O8QIjCcvtoRSytC%2FSrM59%2FnrjuWpW%2BLXosiKMd9pMpDwK5CkegAFg4sMpoaYS9tL9%2BteIjMSXZtifM%2FHPErtk2EPAMCRDWr1q%2B%2F9c%2BDKyoZwUHL04ySYCMFraQLlrgvO1vbSPH0YXFwRdXAt6mCCpvlBn8nLqYrHLNTnT7L52TmKfwXFpaM3kxI9ccANrynYV3925BA4zkO9N06pgoyp11zUZP%2Fq0wCBpXVjXvXcJKSD54A44z%2FqOliQ1JfMNKPFr4Um5NPJOxg0ISIspsPByEqYWQtBHo6ygc7G1AdwAlSPA0%2BF5eV5zmUVK%2FVDZa%2FYuI77rd%2B2n2kD5HQlfJ1XUVGXYWH1Srw%2Ff40KdjTOT5y45IZqkd4Vfcxrq3Dq39em%2FNBL3DOKnMF1gpZmXZh7KfMmeZ9CBX%2B8mNBJ28Sex0mXXD86WvBj9%2FhMKGhlr0GOqUB6vwxgtW5jGuGk9QeoiNyLlhPkKArYfcuFCZ0fk%2B08ZbdPD%2FNWSYO2MM9f8rUNrIRkcJRO2ScpbeeJ4AgQxHuL49Ct7YUD%2FNNp59pXfHh4gc4nCW6%2FYWLTN1p8zJ4rxM6YgrquhSVAcLS26uK76z7n47rjhnDCttgMXv69gibCZj9e0fSsi%2Fuzczqtob%2BWKPghSr86B4ZNlQuYZRBzKkKH0bavw6m&X-Amz-Signature=96bc21cb1af32ef3af1c584994222c3f494610f90dc9651e0b20c63b8a2fa3e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYDJH7Z6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIEPwj03jAxfbHGctBTvtHqfT%2BCULTfgUa%2B8LgiXUekXIAiEAmBard9%2BOGITH4mTuxLIQCydoNrqwvmZkKn8QIOiqJVMq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDLBREF39WfgvGhDIiCrcA%2FYWHE1yYod6DsnVKFn3yPFpfl1OzQH%2FpEg2vizqCOyjC576C%2B2TH7Xy3URuycz5h8SPbJWyc3GoY9LB%2Fcp63Cp6TVtSReDCCT8s2yFKptr4QFhBkM%2BkUYYx1Ol33WcYL7QqphMUjW%2F6uj26xWnmmQen39%2BQgys6cwC61sHrL7q%2BRpjkWn8v8gYVL9UNoSm6S9in4O8QIjCcvtoRSytC%2FSrM59%2FnrjuWpW%2BLXosiKMd9pMpDwK5CkegAFg4sMpoaYS9tL9%2BteIjMSXZtifM%2FHPErtk2EPAMCRDWr1q%2B%2F9c%2BDKyoZwUHL04ySYCMFraQLlrgvO1vbSPH0YXFwRdXAt6mCCpvlBn8nLqYrHLNTnT7L52TmKfwXFpaM3kxI9ccANrynYV3925BA4zkO9N06pgoyp11zUZP%2Fq0wCBpXVjXvXcJKSD54A44z%2FqOliQ1JfMNKPFr4Um5NPJOxg0ISIspsPByEqYWQtBHo6ygc7G1AdwAlSPA0%2BF5eV5zmUVK%2FVDZa%2FYuI77rd%2B2n2kD5HQlfJ1XUVGXYWH1Srw%2Ff40KdjTOT5y45IZqkd4Vfcxrq3Dq39em%2FNBL3DOKnMF1gpZmXZh7KfMmeZ9CBX%2B8mNBJ28Sex0mXXD86WvBj9%2FhMKGhlr0GOqUB6vwxgtW5jGuGk9QeoiNyLlhPkKArYfcuFCZ0fk%2B08ZbdPD%2FNWSYO2MM9f8rUNrIRkcJRO2ScpbeeJ4AgQxHuL49Ct7YUD%2FNNp59pXfHh4gc4nCW6%2FYWLTN1p8zJ4rxM6YgrquhSVAcLS26uK76z7n47rjhnDCttgMXv69gibCZj9e0fSsi%2Fuzczqtob%2BWKPghSr86B4ZNlQuYZRBzKkKH0bavw6m&X-Amz-Signature=df263b4a43ae7408dbb468aa05362d226a05401cc5fa2a96fe402c95c1cb8b77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
