

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=16c4f89ed19e3d4b941756f49f5344d6e49a6100023b3900f4a739547a5404a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=cc05bf3ea1ba9c8d2ec949e27a8907bc1b36cd715527ba8185b408d75fe1bf80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=467064f5e989e27f813ec83047d1bcd86f026efe70cf27c7bb27e7f1cde55fc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=f0280e6bc6f559f7cd7c574d6688ed3482aa0c9424deea85cb6d9c832d142e43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=d806b9aff8dbf78ff677e6a572f3dbb59eef35556edc3085081213593574ee04&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=b4217e2d69fa73fe5b856c1f8bef8016d5f257801b7cca2ed4dacc875ddc18aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=78e183ba654b67670b1c046175a710f3e66e3a4721f1db54c901dac22a394a25&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCNH5U76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDur3ne1MSXjHpK0JYVq7lBp1JIlAnYIk1AWzHYe%2Bna5wIge22FxCCHEHMguY%2FqrWsFbAFlDDiD29FiGSRepveXVE8qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNm8HCzacbvnMxoqCrcA4Zm0v2yEckumNqX0p5bnHunsot3i%2FuH5mf1RfNZM9y4Cknj%2BkK9hr7Sd7MEhIlBUcrfc3CBD5omUz2Yo8ANcPTtkQvASMescpVD3DnxYmtLDB8v5HbW%2FZjG2FHN5uvJ73DZb%2B2DHBUaxijDu4qrxs8zOpZJQ2v1dYvUXPF8o67zCevSkMsNQaJ0qb3F8eUqixsH8NmSMf%2BCTGRasul92sATWVaq02EVHLA%2FgSUf%2BAd7fW%2BOWWh1uRqGMyBS3c5cziLeGp1KUGyh11mkm3iWzfBRoN08D3fi2gBvmYPrHh64Ko0TtfuulIuo6Tg6XaAYpj8JVlcoH25z4QBm9K9tPck6bFifosfALYO61qrsFj%2FBZNGSRh5V14uXalM1lXduWj9E7m%2FIDnMpmdaDyLk%2BGHiow3HRj6gFDLII7OgEp5UVKKI2YmxeC01gk5YyA43uODxJbTCkrsQ0BaiTKkDLlPRPFSZZVRf3cDO5Ls61X73%2BwTFWQg0hyJ8ElKPo1mNmSzE5xh2Ir78Yvid4%2FehydBGfEvQO9qcH%2FU8mgZREH%2F4oyaJr2O3RAQ%2FxUC%2B9%2F82Wrx%2FOZgFupBR1drFkfSUBYnat6vYuF2AUjrqdC1mEDbf6oUw8KQzQ3Wg00d0NMK6a8rwGOqUBH6J8PdRppnB76%2FcCioG1Tpm98t8MzA8HvPUszqFZdZjRVXVlS7OuMgZQ8eg1RBkqam0jv0ga2pmnm186mOB8j7KY2oKdXMjo1MnL49TPXDHSi%2FAuz1PRKu%2FTqAxUceiUUIhijPQi17Ai4rAb9Mm4g%2BsAuGjhSty9hp4tVAzRKIu%2FXo8fkK%2BTk6QK0jIyR07dJv2OtiDmWJLDvDaUuG5GZ5%2B6Eqpo&X-Amz-Signature=2fe2196ac04719130067b92d8e04049b73c0bad19efad83268d8979799943797&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTNFTES6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlraA3G5Pkyid4wJezlYLg9kK8ou1bjgVe7sZ0L3sVggIgI57sp7xm%2BUH3lAAFAv6ZQ8rxS6MUASyWT4hu5gWyVWgqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHPiKqCOGxvIK3kS0SrcA3s5IY89TUaY3Sm4HRsG6wi1aTFUrFmWNYyAhGOiZ4%2FDr%2F2qoE4UfVWZJ%2FnK%2BwP8HYvBHtua0XI02tXBQSA6b7ChfAkkHYR8TilongRRNZSmdpjb2nNuvkJPc%2FwEoBEyPRIA%2BsEsa0CBwyjFfSZpznxXMlElaM%2FAJCPzthxRLyw%2BEYYcBx9cpn9Il6lACxRbVPVAJIWt04MicBIAg32%2BOBoQWmXAbQI1W4o6hrVcprA%2BV3zPiXj8cgSmmshPVCID1IqygXXIoq%2FyXsgzWdw556CP5M6iPbhvgPH8LoXP%2FcDkYFwIPclwdEmRRz1oRdx8P2T9kEkWJLhQKZfpko1tH1ZMMkyIbwxlM5p6N0IUd2Y0PlijzcOS%2BgzFcX47rKflkAAZ91pL4IApLTvg0LaJB2EoMyMfWN5FOmrA9RQ7d72N2MWfvqzu%2BJwI%2FcJ3PnK7wNs4KoUL0roWj%2BmAe%2BHjbBhUnXQMbiFANuWTybEQckyTaKWw%2Fon51q2AmmBciyVt5W63jAl1nWDUDv1Oxw23xiKDdyhjk5CLDGEFhPzj3SmHnCV9qwlOeCB39vnhQPiQcD7DTzJMnZ3yG%2FflIRw74m8XjxNSV2OYoMu%2BbSKxQCKNzmG4illmQTY%2BXKPtMN2a8rwGOqUBMHBKofwTyvjLKhm3hH0R1rqPj22FFsYLJaIzLzqV3Tq3T6udR09bpbd9WSkr0D4eL0QXkaekncopfuQYqb1Tcx1SJzbwX5f8d%2BP5yuOqB0lWDPSQKxmcrF1oPZYUXqJzlpF78D9NZUHZ66pxPjs76QgHs4R%2ByYFmooiPW9%2Bfd5nxIW%2BBKsyk%2F5ZjDNEUWjhr%2FH5%2BU8%2FvSFKZUaABtNyBO3gp0M4w&X-Amz-Signature=14df098c17956428dc642a3659b8ed3f83107e5fd252102361c20bba985d12a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2LRKEKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FT7gtisz%2Fihh8XEVx0CWvmBLnV6DvOSwAh3p7NnTgwgIhAJ%2FTlDYuCBNf6ah1cM09jzazdhkgfdMQezQoYSqVDXbCKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx851P9PRHb5LxzMioq3AMWdqs9dkfmmqOJXLNhdIKX7ByBlD5CyKFbz6yj%2FRVlartLBEzpI9nLkZcvWspJ5%2F93liT6TX%2FgbM23i6KsDUfbzG%2BXLk6J9p%2FyrO175YJmMQrIU8WhX2u8zCGiaZNYpq7%2FJyJU8yfLYBPiDMsMnP9wGCyJGafj242cz%2Fuf%2F9OJwBzLRn9VwFTGuYhuLMqTVFODpMltBKg0vU6PiHVVJvD%2BbZhjKo%2BxzWqW37qDhs48zmH%2BW3jPm%2FKXJnnEa3m%2Bfzz3wcIHdSblND2dzBaSFJsa8PdtHcy%2FErtWUZIskKT%2FuwfMRpxjifdwvdhLK1NA3S%2FJjuJw9LQwLp%2FfHo0Ax86ErxBtIku3qcxZsVsgfyYWUgFFEZ8kVgXTRNL9FAvAMko2HeqI1KevBomAiwArqsiGT4Ym0S2GYYtxJMI6u1qCl%2F%2FhBtgXjwATsB8aeWXKbC%2FvaOpE%2B%2BENvlAm15%2FA1R6krqj%2Be3DnCX0WFp3k3yia7%2FypQU0aQ8TyCcXiACEwpQbFKZKpNSWBfuEMermu8O8GWgunY2vp5cDA0NZlQsvf8bB27RqPAOf4WhPy%2F8SLRvfgdJylFERBahKRBXg2Lg%2BAGIPykRGqiECcSmNbvmE9aTYSYs0%2FrG9cyFT%2BFDDFmvK8BjqkAQcjpxiPlqwRN6Zv%2B9LWNNU05ZhUmtaoDX7ccQMXraUM7EcA7mIq05fEuFYDtqx629F%2FTFFuPcylEanc%2BqredJeQ16OH2KFhADtUE%2B4LVy6eGZzfM345wjEWLcZcmH2tWbpfWDLwDyZTNf8JbjZ37y%2F7gMzU4NrknO0VRfcBHObF12bnKYGJIOaCtrU59zkKC0GOZLycmqXBcS3znpwdeAQD9gKf&X-Amz-Signature=117094be56bc473765f9b835229f56a8adf7f697e23e589eb4ec59c87d7326b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMETSN4E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZ5ORyPZi4G%2BzN7%2FCAVejvrGsH6t0sK19ROvG5ausmOAiEA48xdPCDnAgtO0SHhxznMlUpQg0YjzGlrII7zEJbZXvUqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHG5AgHp%2BBaL%2BJn54CrcA6ieLEBxFq2jxguO3TpL3KCJ0nnmRnN2L1We4W7vmm8mUjQsHRT%2BQH7aO9P%2BaffTIqa8CkDM21PFwDZBfnkcziIoHF6zYN7rSuIXaUjIZcRzW93BCCh0gpIWTwaVcUGruU%2BD6aoZyU9AmAj0FWNILgslk0tG2%2B711lnnA5yMod%2FbVFu0rsqddnlxXucPFXodGKIJI%2FtvkLNfL5X0QSm6OMZ3yF9QYaH7U6jXvkS7wsa63YZPehBLMG9nvHxGWbx8pkdgENu%2FwFRKvdqanJsd3Vn4Sy1QHPXqCuIz%2BsdXKjtnY50%2Fzdfza9fRFerP9VYXFD8WVXAFcnSUm4%2BQvreW74XybwGK69bb4BwMhNvTltrHsi7aiCSJDEqCHiPKc32X5znYxYkrGowDqxNCH8aR7DlfE2r5tSpd%2FH8h0FOdkfaMmqU5EFDjh%2Bm%2FOr9KdJhoyRS%2Fb%2BRXlMQRCaz3YC88Jf191CLPlPQJzSDHjywaoQfQaL5h5PfF7%2F%2FSS7w3n9XJf4FDYDXtQQDDBJohxHHe8B%2BXGI30HfzxWkfLidTIZXLvJd5cYcfV4aL0mOSyLyr4lwxujDwYMkGh67H6q7JRCVzvLQAKjPHhL7wyEv9FWVzjUYK%2BufHKsE%2FmFJaTMMqa8rwGOqUBQUcNF%2FQgxPpLtLqYOMjDtOZETfx2Qu2VEYd2%2FT8UlXYltNTBMrzZsksMMNEWjqgUX9LTpMIUFHT7A57uiqMs3gDMU%2BOGSbBA6RDHD%2FeOWwxFMQtmYKEOyjc8dXl3KXkESzcrzf1BTHxvI4gUW8YOpGCoNnYfHZOrXur1mR%2F8PsXkSd7i3agGuaBcdlA54DGc4lC4mCc9Rk0NKEOB0v7SN8wKxOAK&X-Amz-Signature=d6f66c541b71ee8af82299670b982b7dfc2959aff645315c5379aa5c5f4718a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMETSN4E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZ5ORyPZi4G%2BzN7%2FCAVejvrGsH6t0sK19ROvG5ausmOAiEA48xdPCDnAgtO0SHhxznMlUpQg0YjzGlrII7zEJbZXvUqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHG5AgHp%2BBaL%2BJn54CrcA6ieLEBxFq2jxguO3TpL3KCJ0nnmRnN2L1We4W7vmm8mUjQsHRT%2BQH7aO9P%2BaffTIqa8CkDM21PFwDZBfnkcziIoHF6zYN7rSuIXaUjIZcRzW93BCCh0gpIWTwaVcUGruU%2BD6aoZyU9AmAj0FWNILgslk0tG2%2B711lnnA5yMod%2FbVFu0rsqddnlxXucPFXodGKIJI%2FtvkLNfL5X0QSm6OMZ3yF9QYaH7U6jXvkS7wsa63YZPehBLMG9nvHxGWbx8pkdgENu%2FwFRKvdqanJsd3Vn4Sy1QHPXqCuIz%2BsdXKjtnY50%2Fzdfza9fRFerP9VYXFD8WVXAFcnSUm4%2BQvreW74XybwGK69bb4BwMhNvTltrHsi7aiCSJDEqCHiPKc32X5znYxYkrGowDqxNCH8aR7DlfE2r5tSpd%2FH8h0FOdkfaMmqU5EFDjh%2Bm%2FOr9KdJhoyRS%2Fb%2BRXlMQRCaz3YC88Jf191CLPlPQJzSDHjywaoQfQaL5h5PfF7%2F%2FSS7w3n9XJf4FDYDXtQQDDBJohxHHe8B%2BXGI30HfzxWkfLidTIZXLvJd5cYcfV4aL0mOSyLyr4lwxujDwYMkGh67H6q7JRCVzvLQAKjPHhL7wyEv9FWVzjUYK%2BufHKsE%2FmFJaTMMqa8rwGOqUBQUcNF%2FQgxPpLtLqYOMjDtOZETfx2Qu2VEYd2%2FT8UlXYltNTBMrzZsksMMNEWjqgUX9LTpMIUFHT7A57uiqMs3gDMU%2BOGSbBA6RDHD%2FeOWwxFMQtmYKEOyjc8dXl3KXkESzcrzf1BTHxvI4gUW8YOpGCoNnYfHZOrXur1mR%2F8PsXkSd7i3agGuaBcdlA54DGc4lC4mCc9Rk0NKEOB0v7SN8wKxOAK&X-Amz-Signature=bd04be9aabddb10bea1015729cd203d45c59a992dbe7f6b389a78fbfa4f2feda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
