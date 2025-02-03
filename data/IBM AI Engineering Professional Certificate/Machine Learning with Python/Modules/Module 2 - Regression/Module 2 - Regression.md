

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=fa6b477446eeac99c71872238c3ee97061f0323a9bdb669ca2340ca5675c2f4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=ac4224b8a2971e5ac4636c88fd1b2bb79ad1597bc73813071688e9978ddf9c5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=9592ab69d5cf74e3093d308ace594ff46b66dd243a2a8c530d80ebd0cfac1429&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=08eb2e9622523de5907d6ccf78d21181ade6e848652d74e903ba3ee7779c2a33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=1e68278d62a06070c2c31f362053c7b1a781117eef312fa647f098f7e1c98886&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=0df7aa737e02650e33ec832879a67b2c454d24d1e27a820ef39bd51029aef70c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=d0adf2ddd6181fc4c9d28718c86a03319c53e233aa258fdf4a69f67139ca23ee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VVBDBIR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU2wwem5yzcHEjDVznEVAnV9iAhE8fv5gg2Oq%2BLTJAaAiEAwhSY%2FqH5YlNYlGYUnT%2BBHD3qXuPW2bQtxBdIy8Ht3hsq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL%2FpW%2FZF2dWBwbcU3ircA05bFSq%2BLaC2dORv0g6QbcspBZAqfmQGQFg0NJb%2FuQJpjQ8Wk2WHUf69afYQegK1%2FfE0UT%2FigU2L249dPsAQCwZIBWGXZyOw4adIuUH2u0aTMWa9ypfr8Wj3Ek7e3ZwVsgZ4PFcn%2FYEpaNfekAVH3yHmZwBrwd38McOrAgkrum6EF%2BVP2%2FZ4kKzz3FiQsWsZpzkuTYNRQP8Ie5KLxbksiFYONLqiWhPy9IIgUlbsmxwxcS6K7m4g%2FG%2F5lP4orukDwqSrGfhIYrb53dRDnpPS2rLbULbAnZXyCenCaZR4%2FKSW5d16%2FJxpf%2FGv2qlsOunXnemgvUG2jHxRTGvyhJ1HwF5dy2N3np6OOLJr6DUkzMtWzc2eiXCFNhbd74zIyQGzkozZ%2BCiZbzm%2FlDomhNtEZtYVGOiVyg2ziXTvKEVUBcxSleTZXjGldK%2BbUCDzkWi2Swn6QBKaySxRjEIm0tj%2BYPhh5x7NOnGaFTSmMBkm5oh0KRval2BvZfBM77iJQGAx1Yk%2FsUphum6lrsri7ApEfvrvyzcRYEv5%2FtNLXgedBNNgPRueHGLpEXjANFMMApAPjMF3gkDBvq%2BGL4eiRZkdi4nHi9kyM2zFxNrSwqQSITRXL4XziZBeRMwwS0VJMLLzgb0GOqUBl3ctJ6i9istxx5RcsD%2FLsqPJAOT%2FqrJa6UHVB5DbuUOrM6rFNjqmftuxuQFPOOG8WsIUMAqMwvzYGjgjhWGbA7DeS6fxMa5MPgmg8eGb6z%2BKM5uotZPVu3dgpplXAbHmxSSLeAP8WT13489%2BOOpyQIhYKDCJepBd7IlCLTWa2ygJFKy5eXI1n8icSCiPpOtWB7N5bXTcL1bg%2F6onHxbg93elpApt&X-Amz-Signature=cf542e46c74dd027543e96b734d1daeb01cc1b7426dc0b25ea7611a3a56753eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OI36VUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCG12DcotVVzE8K6HlG1ccP5BivJzRmK0bZnh60xo7NZAIhAKYzru70maxdW0mG%2FKxRL9kCBUVF9qtUqzuikV6AVOihKv8DCBEQABoMNjM3NDIzMTgzODA1IgyYs932JOP0hofbWfAq3ANYiHAeBqsri1jJcA0zAanJ%2BeqyaS2lIWihIcz9%2Flml1J4%2B%2BkJRKFYAhDlMrFyB20eX1MsmluHyQZTt0dF6amfLHtcSUdoPRXAvxBSt8ZMFQjmDsYHu%2F9Xa7iy8xm5r0oqbhbwK9%2B1hJhrCUK1fFq9NWValb%2BfRKJx3ZqSyRHXD4sVqwfBVznkDDRSFGtyI1rFKEYQLaM%2BwVgHZdc7MFRvAWSBQ7LVR1dwv%2FmH7CE%2BV0ZihMPemOqM3D7OLXMs%2BJY1GgrmWLkN0%2FtNELrp3A9RF96bE54R%2B5nOBe1HR9RNDnq%2BYLjja9oSi4nXUIB%2FSH0Aem2JyHD6yFLa7Fx6srhbu9v4WQHBDOKK0U5pcrPGI3IF2RIFqsp1cn6VN%2BBIJwgun8d4RbXsjmJ2FlCY9U1D5cKeLj8PDoTw17KnWHjIti36nt7upNvywUvAL3wG2NmMXJWBXvuvFF5INPbfGuMieRYmQuxj1xI5NG3qe%2BJdy9bqn3Vgk7Cwu9XTT%2BPokYiJ1%2B2g8jf%2FzbnMZ3TX9d2gl2jEndN7Ib7Ut6YC1FJTaZRzDeZ3wNclYijjtwyeQ2XJ4BSg3ox%2BAsbvA70YBlv7EimaGlSOF2EhE%2FF3xlHqSFo0ay3I2cns0qR0%2FKzDS84G9BjqkAb6xQD8aupyTUANvfXfc8h6VFAnPk1YCT3p7BQwEGp%2BTtveXBpt9eJWR0mZ6gbySwLpFps%2FEXFBvY3cWU8u%2FI6C4IC9E0nw%2B3PELm6D55PnGneQTGNbsRh5EoHmy%2BOI%2Bs7vXsd0me7gtL3S%2FhGu5L5inwVp0bnbxxhTxeXaTShwAJAesGSlmrECaCfrUgrWSgMhbG4xHHknJa4wH240VoLBFInJd&X-Amz-Signature=27828bc2f27b1f59c7ec037a3f61b5556842f795623abe283926595993a3bf5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQNTPWHL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqQJDEPDIkh9VaQ%2BlIsn1wjE4oCJcdNzYU6Q8g8hULnAiAvmaqJ7kYEmkMHLzQC912SBmvAh5ekMOwZOhTrpo3EGSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMdfEJ%2BPNFSLBgVMbMKtwDOV2v00mgNStcNJ06Um%2BUpfRGiAw1DNY136E%2Fu585%2BKTecL1vJQWeJl8tSFDt7K2qig4ycSVvE2hgN3HsV47wOmfluCw5%2BwjFX106N%2FlBOE9%2BWq38IHkYpDPu6DpJraDzsHKXXQGTEbUeeuQkAPb%2FOUqe5VWrrf3vypVTPo3P47H5BpXArTearRdrOp%2F4ApZjls6aBzxOvgTswjHwCy0%2BLe%2B0eLFMEEGYonOeF5I1tWaOlkJN%2FKs9VJW94iut5gxxntZeXnBEtTDppH9By5dh4Pp%2FmZyFu4%2BXinNeflN%2FeLsLrm1gdkleBd9Bvy5to%2FHMd23W%2B5F3OrVe%2FY2l97Hb%2F4k9FpnSYZB1lSxzFKSptYsVCeSOtdD%2Bv3cZRha5CRPXJxk%2F35kw5XUJ4OB%2BpXxZLdqETYf3YLCWMu5jMoCmqD9Mo1fImPjTdG3HM3lW5OTpsdihM5u12FoSljSlV0S4uql4HChMVlPIxSsq0nanIIvPEAg8UUB%2B%2F8CIPyv2gK6SC2E83qTMU%2FTUXs5z82nt2g5C58AkbplDZRKyBPdCZaNCGfcNdKVWochvXTnjfw77%2Bg04MCkPYIL3RsS6o5z%2FJvLwEOel7TSpW0LQ2euk4lTjNG24PdQByy61rPQwivSBvQY6pgEuOySy5%2FTLrHiDoxDJHp52s4N%2FMafRWcQ%2FFerCrEsOZ%2BZayAzhc2LHXdxh%2Fkjg1Nu9hUR8nl4cX2Cz0nK8O2upUet7YjECWMcINCDz7jt6HzNU4NR3yHAeEFbUwPe6aexQsmXI0QpD7OhqhTjL4Hzj%2FF7vP%2Be5hE%2B6bLxkMEtux5Xt3BgmaEj5FX1Ct%2BOiJSRmID5reuobRM0VVjiXcr9TngfDAsYQ&X-Amz-Signature=47a673603e5a07ca1686229812121d2ab25af1ba4fb5cc1d0a037bf6d862bc95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A57RB3E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEwYRA27KO3yRF%2BhKW8h0a0kWaW6m7o0dey8SEI95RhAiBN6E0P%2Ba3nm497XrXhnBmsUouqv75IDgBtzvFU4ejJDir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMhYEMxPi0Pc9oFAPhKtwDVeBCdxmbwgw9qGUpr%2Fy41rAz1V16zCWI4ARIfF3av9WEKEuK8s%2FBVB3sNG4z%2FVWUpv7TQFqp2S5XJ97mXYghhPvRCgHyYWnP%2BVJc79GQwW4%2FKSrlPV%2FqWtZbBkVZ9Vx8U%2FD8wnVRs0wot7SnFoS53n8RKavsRaj8QaAFz97%2FPJRADCagZBKS6I6Qe%2Ft8at0DPV6gniXINPImYeJFXd0I%2F4Y8ef2zMRM0bdsf5tZWEJR2gwDKeCj7m9FmVEe2knKa43hXf90%2Bj8kadlLZ%2Bh3eGXmmuf%2BiFsYl5cj4xyMI8zkZNi405MfOl8gm94W%2BkuXaK9%2B8MoBOtFKSj%2BCAaTKQaKls%2BQkoJ%2Far7NhibuRfoZ7CMYrfQDzAU8F%2BBAJjOMzRryL6mkI3X2xW7Ddf6zRj26gPbq7gc4RdO4uXmrt8lL7FY7Q%2BeXB8qXogfb%2FWjsQH2C%2BIXGUZuab%2FOWqTFcvu8zm%2BrPrVCR3uIvnBlA0WqkH4%2BToLPcExj%2B3JtGI1E5qZkPH0FQQqa16K18mzSYs3LiMswqZKr4IaY45La1nCaWIjzPCSJbMpc8SkfHzLAOKZpQZU7qdvRagnB%2BmUDJUWcYaGp6wswoV6UTABR%2BvZmAop4isIotfKrb0zlw8wjfOBvQY6pgEEtH0%2BTM%2B0gCQ%2FQ%2FJpH8mDleOhywG2WsPEsQBS7cyRiJHM0WyMhNy1R5IqZVdnvwXq%2B6y922SX73GYSGwtAPvjOosL8xhqNINxgp8GZl8UMtfB5Zt5rnx%2FY1lAlTzNg6RqeWD2enw%2F341POpzzzMFLbERuJ%2Ft2cFpEvwZFAk3aFPIEjTKiM%2FBM0eLwnC76i0lLFpxTThXDDz3xL67%2BedwED79HzSac&X-Amz-Signature=369107e2cc967f465a72acbea262b6a02a3234cbb22b235917f81a762728481a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A57RB3E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEwYRA27KO3yRF%2BhKW8h0a0kWaW6m7o0dey8SEI95RhAiBN6E0P%2Ba3nm497XrXhnBmsUouqv75IDgBtzvFU4ejJDir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMhYEMxPi0Pc9oFAPhKtwDVeBCdxmbwgw9qGUpr%2Fy41rAz1V16zCWI4ARIfF3av9WEKEuK8s%2FBVB3sNG4z%2FVWUpv7TQFqp2S5XJ97mXYghhPvRCgHyYWnP%2BVJc79GQwW4%2FKSrlPV%2FqWtZbBkVZ9Vx8U%2FD8wnVRs0wot7SnFoS53n8RKavsRaj8QaAFz97%2FPJRADCagZBKS6I6Qe%2Ft8at0DPV6gniXINPImYeJFXd0I%2F4Y8ef2zMRM0bdsf5tZWEJR2gwDKeCj7m9FmVEe2knKa43hXf90%2Bj8kadlLZ%2Bh3eGXmmuf%2BiFsYl5cj4xyMI8zkZNi405MfOl8gm94W%2BkuXaK9%2B8MoBOtFKSj%2BCAaTKQaKls%2BQkoJ%2Far7NhibuRfoZ7CMYrfQDzAU8F%2BBAJjOMzRryL6mkI3X2xW7Ddf6zRj26gPbq7gc4RdO4uXmrt8lL7FY7Q%2BeXB8qXogfb%2FWjsQH2C%2BIXGUZuab%2FOWqTFcvu8zm%2BrPrVCR3uIvnBlA0WqkH4%2BToLPcExj%2B3JtGI1E5qZkPH0FQQqa16K18mzSYs3LiMswqZKr4IaY45La1nCaWIjzPCSJbMpc8SkfHzLAOKZpQZU7qdvRagnB%2BmUDJUWcYaGp6wswoV6UTABR%2BvZmAop4isIotfKrb0zlw8wjfOBvQY6pgEEtH0%2BTM%2B0gCQ%2FQ%2FJpH8mDleOhywG2WsPEsQBS7cyRiJHM0WyMhNy1R5IqZVdnvwXq%2B6y922SX73GYSGwtAPvjOosL8xhqNINxgp8GZl8UMtfB5Zt5rnx%2FY1lAlTzNg6RqeWD2enw%2F341POpzzzMFLbERuJ%2Ft2cFpEvwZFAk3aFPIEjTKiM%2FBM0eLwnC76i0lLFpxTThXDDz3xL67%2BedwED79HzSac&X-Amz-Signature=3c1ca1a11023643ecc94c62326fdfe58e8a5135cf55122a481372810b8265367&X-Amz-SignedHeaders=host&x-id=GetObject)
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
