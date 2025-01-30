

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=ddddcececb8bbc58489a2375601c0eeaeae3a29be01d609ebc82e0085f41b8b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=a7a5600bc691f773326f4b94c57ac8f51858ae1f429a1a81e0d11f961dd69395&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=a82894100e99a63301f59cfa27401a38dceb5ae199da3b4c41d901123ce62352&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=44eb50b39735fd46dc3376411c243eacec35f0f868198f5b4ac8ebb6ba084bd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=faca0dd4bd7a275cc27b978a22ea0ff903d203a31ba02ed2df6a1da3e42435e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=ac6f48c48ec5407ff78c7bc5d37da0748c77830e414d6da4a6947ba10a622f53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=bfe9f27fa3dbd3b726ee695f8228c9b68da73b37d680717e235b2ce28fe02048&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2VFNATL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHroyEG4WB%2F2vosrpYGABVVTZuot%2BBturML020wiaTBVAiEAmWp5ghF0CCWRMcJa%2BWajRbmIjgDqIoY6rVID%2FZavTqMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2g8HrdpzEgr6KwFyrcA%2Bqy2dNpMgGmdS7lX4NEWHEB1sMaVpW4%2FxnEzApQUw70iS0vCLBCdsR8rCFUSL2KxK%2Fh34%2BhCQhEtLolCFyWJ2fQY58AAd%2Fkdg3OtApNQqeg9QCTCx4EN08Z05Bmnynmfx4NteA7MeTdqch%2FcinsyE%2FmfvBsQx6B3BDhlzPBH0aOvanCjpbdC9YaQmusp0K0Ibhq%2F0O6Z1Ua3sypWr5zQK9oKQspDRZha4NZxHSomDxmIpkA8TPXhIguMVMimvkeanGO2EtJLFULMiiS5slpnCiKLVk2Thn8pRfTUlBxSNpJc1jmtYfAOrkw%2BooPQUHK01q1RjB%2FZYIr9IfBgqn1e%2F6l7XSKFLrDfDq6LsBvS1zGzPFlS3gwavKHnTGhQS9eWaXzB%2FwPE6k5zVYen%2BA%2Fg6Hbph8DQZH%2Fjq%2FREO4cwEFmTTrnM9%2FEsH0W%2BWsg%2F958eYw34FJTCEsqiaUXEIL23B939LaJ7g0%2FmfBdy1n4cReQqJ0oLloegEvflgiCJihx5mK7UPy3PobTsF5CA0yAV0PCnZK5PdRX8W2zD96cqnru9tz56eZvhB0n3pGwSVeiTUAMKRdW7%2FSVo1vJ2rFRh71IHkEguTGmMYiIdaGgDKTclLx7LiYDDOw81wWDMMD877wGOqUBshI3PlaigzpSb7HrIdctO16VxiRt177otdGKkMewvCMeZt36iwm0h%2BeiB3tPxie5r8jvsQ4b9hbMvQfwyFAfuX1WRZDvjRN7fW0B2U3hqLwPvcfDONEMHWY1gWkLaAjqvXMwPg5M%2BnpiK2SRCgrOZPgzt5fgrf5SsB386q3xkuDgFU7pSFyKerOPeBiEuYP7s%2F4qaWcGV6SSGME4zIq1NgTXLaXZ&X-Amz-Signature=8af8381f07e6f4a7f615b49346d37338aaf8b0ab1e5337a56362d72fb1e39a98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHZUAYKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqkOBACvFbZwR%2F6EcNxV2%2BAraMc4pgn3me0Tqh1vvBFAiBfF406q7mpHld41XUCxPo7RhpEimpspe7ojJTayfETgiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoIby0w4uC%2FZMZJKCKtwDx%2B1YqwaxnhvaukS1FihOVJeH%2BvICmXUdx1zq8tcWwlX03PPLNFc6j4rVQlpExjYJaBUUjGoefaRDqW%2F%2FdtkzlCp2Ko4gWUqRmH86yccMcx317c1vn%2BcKRhUj%2FYt0iW0mfwQ37T3UZpjY5BZvc2NRmk4xKTzhxZYbfWC2sfyTz0q79vLHxso5dUBxLkn80AMUoOFJsUb5Bc3mFjpEdaEKTDlFWSZgMJ3CaiEfA7p%2FS5xNzToocSVWyC6oc1ASsJWZnI3i5vmzbOT%2BVBF84z8y50IqBWNYGEfvhfsVgj%2BkeLVlIZy9TrtRniXK6EfwYP6mWeZh5SFCL5KJSLxJbxxJ2coxrQDX5MCvKlnqusRko%2BQruqSlekMFY%2FVTyGjjsux2sUlUdEC%2FaCjF9M1n2pY4X4enjqCAzwjHEmsM3jJht4dAC3FOpHnphktCGUUOldYrwV1l%2B7yhTi6x7dAjxtyQA3WbqpQzQW9yYkATowJnAz5MREk9ziF6v41Rdole%2FCo9sFIJ3FXArDSKNJDnCo79fpN%2F3vyWfAkmR5xHDG7S0dfODMEqA%2ByyUgbJ56IdoHRErSeBZ0VRRM399a6NphYGqGuRP7Y9JabyKU4IXufcIyoXIz6DxKH0qebokkIw4%2FzvvAY6pgHMqLN7C2GQJdPObo5d5nCZZbj4uhXeV0LPqKh7DF1LXEYcECp%2BCM%2BxcqDkVhQWEF2NrT9Bkv4XpI2qsN31xBqOnRhpye88NbgP8htTuBWfRUDhv8GfVbg0Y4NRNK5OpMDqtybOyLny%2B6SSzuMjJuCVNuAaQN02lDcQk9ioT7AJdZX8GKLk4DiFdYYOMIWxUIJIFOsH3XPrFiZsNIb%2BprzeGU2gP2Tg&X-Amz-Signature=fc3493758bbe8fd43ba0571daec93aa062778fde2af4913642069afa7daa2682&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMXJ27Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICxLJ7YOKbcTYJeLnr8fa%2BlWUrNBFBZT%2BHJkI0dgtW82AiBohlFcQGXoB2Nzc5aalT1viAGNrH7I%2BOnakaiMpUF%2BFSqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYIh2Y9h9o6vPo%2Fm4KtwD5g%2B%2BI7lS7Qu%2BvKYJ1b6yM3B2gLk7Z7FgsW12qdbZBTDoCg3vU5%2FPzsFWQZ6wSOBN4xDQGWZ%2FRpuwipBJzpFCzqZ7h0ZYpUJQL7Z%2BWygscy%2BMaHoXmegc71lO5iU8RFHPMLaPRfvouZ0Xrc7YJYMq%2BPz3o%2Fn7J7C00h4yszoZSGmGanYmBDAEiTQtX1mKGJAFaL61S3iaNx3I8KnUcfxN4vvwP8In4V%2Be7tZHq6pUvfqAuPOuqV6hyIm91YqPtpIPebJKfApMSpsbmJSaUVf2QXaeO%2B3KztwLAmUoPGljs9qEvK4oyfgYuR2eb2mSYNy5vH5edYhz5xCNNoQjOEzYYcfjzPAsMPqgvdIWG1c1KW42qBpq%2B9AHZhL4UmWmTl%2B54q5KfYfVdobEHv%2F1x8nsL3wo9Ry%2FW%2FJ2HyaOB7p6pYq5EmVTd3sncoXN1F7lQhV%2B78Yo8LV02vqsJALbhqVkKQt0LyXjb36rlxZO5aHvkhYLONfHgfpz0iAowcGfGJOLAVVJEzF2AaWBus6UypS1RnrHVNQQa9us%2FeFCY9kSUkFxi4BG2rpOlgYDauMmtqFnLgN%2FZ5Fb5fJMKwzYX22OcfnnFQVNHZj7IFogCQb270A%2B%2BReLnvuIkgb6lFEwpP3vvAY6pgHlellKsKuPg5Az5huvr6m5fGDaK3yqlECCVrrheIh2FzFonKotloTocE6g0wqkjdhj77EiQDxpobFj1uKNvtfqSDE1%2FmiFDeO5rIcfXUytZVh%2BT%2Fs4WWZHX2qP8xZ4iVdnCzfdxoWvuPC2KUiFtKBRK4VBYWeAj8BjQqlDDty2xfnxe2NOpQrFC2xMyeArwzt2hLxEVTbdOUwUOHmlPltILJ1%2BqMHk&X-Amz-Signature=609177aae41df959f34163be4ef954e52ef4e37d6b2793dfe53a1a1784a013a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5PEAHKU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbVCct2m28c5e03qvn7iOl4ds5jZBkGjURm8MnHNJKAiBVW4XvdTSh%2F6Nu8J0C9yYwcV4dB%2BCSRDVY2YKoNI7AjCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv6nnO%2FQuUnDj0YC%2BKtwDgxMy0NzxoUsVa6Ac6%2Fw01hpX9zBkh7%2B9Ibc6Cz2vMAAIMiohDuk2gxpikvcq2Mo3Z6eweIHgRjy4wZX8N4lRjneNWW8xZx9eNPD%2FCzzmOedVVnRHUDTgKaw%2Fo8%2BWKVA0aW4aHYaHM6pXk8Rq61Lnp8YcW4q8wS5Zp5OL55%2BkQmd9sc4vPiKbwAMUM8xR6SdWxjuRZVx911Qux3GAE0nJcf35qSUiylhCDlq72s5bTeTTgm%2Fu6HI53OMNpDAVA4UPB8N2DrYhLEH8HVHBZQ9sufz1gaLCapQ5CaXIGM21vePBmRq1I41wRV93q0EYG6KHtWUXUiVB9CdLtJs%2FWiwp1ljHb%2B1qR3mM278KX83l3z7Kse89J3aqCDSjpyUYIfsOuv0sSUD8sIsxj7%2FtnACffB0CT4mlx0EeEEUpzMIDu1XSfehYqyrRGNeSczakMjX1DSRWa73SSvzMTuf%2FGm6bgrY8Ert4uUchkh7xMuFoIui8PK%2FYiSiJCl96zw4m2ga0ED7LfM%2BiE4AkE6kda8ifq8AqDiWGdiHPvZJhr2w2vMpA3A957lkfLnfZkQgl2Tp4Ef%2FCOzs493yfj0xFmm9dZMP2kdJfLdvTeezxslPH%2Fyt7E%2FWAlSkKhpU1YnUwg%2F3vvAY6pgGka1F0RvOadpKkWl%2FbYDBfpWs8qJKoMxCGIcAM3ldROTgMtOCfzQ1RnnrDHWKfdj%2FWXtsPXQYd6zT1OkvGkPeLRTqjjK3y7e7MOhxeki5XK%2Bs1CNWx%2F4ZzIbgmzeW0mgE%2BGbMvoOKKzKjNUwGBY8q6%2B4hodtvsznxC9hivjoTiwVDbOdfwHAI5kUn%2FJxqFLODYy1fcV4IV7sD1zpKv8v81zcUiKbLr&X-Amz-Signature=9deddd43aaee204980ff86841a6149bd25345b07a93ff6515cbbbf1da47f0894&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5PEAHKU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbVCct2m28c5e03qvn7iOl4ds5jZBkGjURm8MnHNJKAiBVW4XvdTSh%2F6Nu8J0C9yYwcV4dB%2BCSRDVY2YKoNI7AjCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv6nnO%2FQuUnDj0YC%2BKtwDgxMy0NzxoUsVa6Ac6%2Fw01hpX9zBkh7%2B9Ibc6Cz2vMAAIMiohDuk2gxpikvcq2Mo3Z6eweIHgRjy4wZX8N4lRjneNWW8xZx9eNPD%2FCzzmOedVVnRHUDTgKaw%2Fo8%2BWKVA0aW4aHYaHM6pXk8Rq61Lnp8YcW4q8wS5Zp5OL55%2BkQmd9sc4vPiKbwAMUM8xR6SdWxjuRZVx911Qux3GAE0nJcf35qSUiylhCDlq72s5bTeTTgm%2Fu6HI53OMNpDAVA4UPB8N2DrYhLEH8HVHBZQ9sufz1gaLCapQ5CaXIGM21vePBmRq1I41wRV93q0EYG6KHtWUXUiVB9CdLtJs%2FWiwp1ljHb%2B1qR3mM278KX83l3z7Kse89J3aqCDSjpyUYIfsOuv0sSUD8sIsxj7%2FtnACffB0CT4mlx0EeEEUpzMIDu1XSfehYqyrRGNeSczakMjX1DSRWa73SSvzMTuf%2FGm6bgrY8Ert4uUchkh7xMuFoIui8PK%2FYiSiJCl96zw4m2ga0ED7LfM%2BiE4AkE6kda8ifq8AqDiWGdiHPvZJhr2w2vMpA3A957lkfLnfZkQgl2Tp4Ef%2FCOzs493yfj0xFmm9dZMP2kdJfLdvTeezxslPH%2Fyt7E%2FWAlSkKhpU1YnUwg%2F3vvAY6pgGka1F0RvOadpKkWl%2FbYDBfpWs8qJKoMxCGIcAM3ldROTgMtOCfzQ1RnnrDHWKfdj%2FWXtsPXQYd6zT1OkvGkPeLRTqjjK3y7e7MOhxeki5XK%2Bs1CNWx%2F4ZzIbgmzeW0mgE%2BGbMvoOKKzKjNUwGBY8q6%2B4hodtvsznxC9hivjoTiwVDbOdfwHAI5kUn%2FJxqFLODYy1fcV4IV7sD1zpKv8v81zcUiKbLr&X-Amz-Signature=ba2108879c24b5cc0f7e18376c63cf80e957cbf96e0a27b06cebf655c31a2d54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
