

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=11473adb7d142c751715eb4b66ec6d322e21ff3ca805ea3b7aade7a91265c056&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=cd77b19b2e7737a39701269ca1cda4f3ee3b31fc628b79cb8df7a679e5ef5b60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=eff90269bb87bd4f85b0c13b8ce554a184daec99438eb6df0e68aa023d04e89a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=b9ae1388d6cfb60c3bee64a9ae5a6eac0851395bd9d69b7f793c5522d6953796&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=6e7da82b0693f77429834d69bd2730d59f032e1ba5959e9908cf3328415fd52b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=17c6871e659cd56522871f344bac6af781287ebf3830c5f805a8af5134a25a54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=a474a49d91a0d9b74d9453b74d0a3a04be8ddf347e0d9472774bbc074937fc1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QEGDT3F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6c4IK5x5gtlJ11IYud2CZ6LBz3D%2FsRzvqQvkh%2FzzHzAIgdNmrCgj5OreX8YJsDCmkl3GcCffiyETc%2FLpQheEVsrUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP%2B1sTu4poQdkGlGLCrcA6Qenz7kobGx0ErGP7avRceOszqLMmJlyGs1GeLNyOG8KUyXnxgOi4hMou7zOANMV%2BgeJzdH85cGNOhQ9%2FySInh84oWAmDfpmay2AVyCkOkNtDYLIopobY698yR943aT71TVW5Cgdlq67NO4TpSRZfwycQ%2Fk7sub4FiIuN5wKbSHsMs0kuFVwQYD3iFN5rmH2BPAwn2dHgKPztYPQmXyQu4waxAnBaqtX7fMq3sw67Ra7U2fPoyx8gcts1gJUIntyBpg3UA%2B3SusYQYqso7eJKYS1itE%2FD4eN2akLkzOElQ6DNvoetOP2zf9mqK%2BXdr7Yu0aUwTF5%2F39QV6FL9FiJN7Yr0MQJxi%2FXTSsDcA%2BCGq2Zi7AVJTlUWM1aDpdD4CXgY4PqWDkNJgkgMGBLq9hisXjB6r5MCpKpp8K3TyHfjWnyxg%2F%2BfYhKHRBgKEEFPrN%2B800Tzad0Ms8b2UCWeF0xeT33kIGgdEOLbHexrOAhudcjXK2P0RlaQT2nAEOXg5wYlKm5R4K2IVxtLNxZZAmFTieWteDA%2FJZ7o1uqvKNR3WIW8JzKwBxYFsZYkvhuyLfWjOTYwIkt5n9SOAVOp6t%2Bsh4b8shkRQDNjXYcVQhIBG8XjOzfI1G2G%2BOXftjMNm%2Bhr0GOqUBY1c1LKGqDf4AEH1o6VoxsCVWFGwzbEN9f249Q26x5LXb0spdFd8ZkIejUFOpmX2%2FCGoCa5tdiFTokJ6b6mMWDzU2uYGg%2FNJOyEWkhMnGTEK%2BcOa%2BFytgAaTmSWHIgTx9ePl13OiDazIa%2BOMe4%2BupWbN2p5r4RcOwVDhW0JCgqHvUDQKccdVTm5q8ALaq5Hxy5eKocD%2Fg4eee3QIoJy1Hyol6x1v6&X-Amz-Signature=141c24ed5a2f62e6153d35cd2f47b239c4ca8fb71cca92da9dfbf6d5d1ae29e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOSDFPKH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFnbZwyswUE%2BnM4LAjJ9VPtGjk%2B5hkWvTI%2B6CaA5%2BXjNAiEAu4LM3SuqJms88HR5JLs6%2BatxDeHHWvPxXVj3aS11hLgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDIqMpGopqddFkUunlSrcA2k3zMvsugknEvXBK44R9XC5cWZZUwKfxPvNeUL5MEHeWJK1rpJN%2BQsrpmy2wK9VKPhg8Xg4Fv9zRRMqGliv69Q120mosgyNpJ3T0lRfWspA%2BIfGdGgSVimVYrO8o%2BLFql8tch0HzIHo5s68DiC9xds9Q0EpLwnPcoLROfwqCtInwJxN8VLvmbkf3nSRHv4stDE8%2FC%2FyDM1AuaN51WBCdCJ5OjdQ6jWobINxKOWu7zLTC3Rbi9KvG10dNsFKf1%2FwtTQNCBl3AwvPsjLzYNmpwXFXaX3438xPdTW1NvzVpS5m5Lxqbwxswze4jkIJ7ifwuqVUj8zENiHfItB6%2BEAVLFYw9bY7%2BJnrH8NlVUFxFDUwSEcDIMEbHLdAmHlZ4pdiMc7ToP7pCkzPowXJxrCeJ%2FC%2BvkUIj%2Boqz6AT%2FLlQaFOFRaSJ%2F4%2FtJEBbQlMJ%2FbWsYZ3u2F0rjill0dydDLxPFYbojAZFqR9xbuis4XcndijvNTYBnQ8KDipxsEPJbEPT95oXLMAc8K951AnZjxEvV9zLoUL6K2GXjapUd51dLdV9L5r1JBSTsY1nk1VjAJXb%2B0xX%2BXpqsWLf21QXnlbtp3w5Pba8vuWlK%2FRGFpJvkGwYZb%2BR782IfJ0uvQ0oMO2%2Bhr0GOqUBAWlDtihJg%2BDh5OtixPGXAH%2FrqLyCz6ZgXoMR1ZI4APAit%2FeNYYzWgxJ20w8Fz4RDBhqw5xr5ywj5JR2SxrGMNVMYyooU3mbQVb5WAqRJdV%2FWmp%2FGuZLU3Q%2FTGNq%2Bm2tGRMNxCQfM6apl2KEqJd9OBT9J0ZJTt12ncWT8vN0X98dyroQpVDCrYldyiuw%2F78z%2BeCXfDe8azJTyr0DFN2y8XChCFenM&X-Amz-Signature=21b20431b1105bb85cdb4e2b12ebd4fafb77f46bb17e636b6ecaef511988ad1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667THQ6Z2P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDG5jyE8gWPTkjwvmCTDx5%2BOVZEC4RP6cWQJJ3hiFwe5AiEAi3bo2wE0COL3GLONd98Pno10g4fXzsk7tiKFgmmasVsq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDBvm03vEftnWDc8HGSrcA5MrQEfjJfLAgb1uwJAPdOoJxT%2Fjv5Ebg54UbLQkPj5lmmx7LfJnGu0C295vIKpX2FGDCoE2FZY5RKy%2BUSCHAviRPayC2ATdGbRBE2svK7R5SnGYfzjjNNbKvpLneoBI9B7%2FGYhrxNn115HUJij%2FzQcu%2FL1tqyx9xpcsdI%2F%2BWAyMfNNQuNp0iq2MJTMH0ujz0xiM%2BMHAfbehGol6yBGBvC%2Beg1VcRsYO4IqCnxsj8ltzQ4RaHuPvlpcl0bN5xLjObSW3h6a4TMzzVYGxUrmJsOFcoV9Gl39K12JAqW7cXB1ddYjD%2B841yT5KPP0ER7ME%2FevU0fBWQ4A7xcg1h67v40%2Bb5KSjqEjG4NW%2FduuDNcwVBBFwzdBEWNJjR7aK5rbrhp7kbciFQ4yDrvGd3y7sr9AEqtk4nZEygZNs4w3%2F1zJsAS%2BJcGebI6%2B3LmNJHJE1Wdm0xPJqh%2BUqc66XPp4Kc7EXxWF77nbjpwcptVeX9tTPrRYYCOA9tabCgD509eK1h56EbS7ApO62t4Y46uCRjK%2Fkps5mcqKLizHVcrLnf2UCcVKJuc3FQigZYWly3HRrcxMnE%2BCBZm0Jpjb7xdtJqCB31DIkJOLhDFug8%2F5P459BK4KK2adweWQROgnzMLK%2Bhr0GOqUBGdqFGbtwngoSXrd%2FskrclypxE0W8%2FL%2BEclFaGizWdyM8KQSr20Xp1Hzk7gXVU%2BySejk3c9b6s0eZjoozqMD%2BcdJuNkkjhl8lHQ9V7WnfK2LXnXkugIAb4lawpn9aBdHRsHkuZawV1p9xQHdl%2B6a9ydJAUGL4OjLjmumlnlfRMQsYXd7KlQ9v8qFcBopkgQmD8ESv3CasxA6BlrGTF1CDs2dZX2J6&X-Amz-Signature=9aac61e9a9c420db63eaef480a961773b6aa389f0b4edc5cf8efc97949943ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQYKSDP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCELH61oZokWC2MX2u9qQZc%2BTZVxkGpFsGykqX08l0jTgIgHunU%2FUq37XarUDG0tq7QjQD97CmRtVPRaSM%2Ffh%2B0wpIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAzIpeFzBMao9tXMICrcA%2FKfoQwMx8de%2BnasE5WFTJ1TBotH7x5WyUc1vwiEN03nG5XCwWgQn2N5MPhdlT4ciOZSImoZNCxMIBt%2B1ENjWH9SQuN769izCZBxDNCwC7EXXBdcrQn8foR6GLLYzZP%2FGCEO4I5HsKBA58y1RFVOAHnNC9ieoBayS3B2SLrfkg6M0QAORX%2FkHFkoTKBvxfWAE5PSfjpHv0xibgeYySzs5oHTQjBGB8nTAYUjFT7KfIAum38WJkf0fWppJY7WuFSW1i7NifmuU6%2Bgxq74dPCllnB0Hiux9BrypP5eibgvl14dwiFTmpEuYYCvx99y8cSEheBT3QeDMEjbIONs2jXlQO%2FNxr7JCAaaQTEdi2har%2FId6QyRoWvn%2Fyc7dB0Zx4RbBCyC4WC%2FhyqCy7LNK1%2BcXr7VdWAmNStxjQ2knLPSEs0FwL2RdzvbH4dH43QQBUdTl0830YOj%2BAcN7Cu0clTwbCulOdJZHvgdga33NGXG1Gv9thfmnHDbLjJyHt8KYdW1lFyBlqs7ABo748M%2FszDRWsXZDdYFc0DmadOuoaDQl6%2FJmfw%2FhavELwa21pK9zRDNHZxtHkYPSkbkyN5gNrZ1mTxeKFzr1GpDuhXOEnEg4DINbbwi7k1f2u7vHc0tMIq%2Fhr0GOqUBFu1toWg6ZcB%2FSMO8rfl97WwlfnN1kDDDjllphf7mrH2J9uI0qHGqUhz9YJm2J3VBK4kuG7WCG9IXXStMyIAc3OTc19D0HnslJEtdjmAtd9y2fZzyA8G4Tp37h62gdmbK4y4oJCvSkJO4t9Dv%2BCiMdljG9xM8OKhIekA5qbh7mXm6WdvbS9Nl9GUH7SfqRl9AK4e%2F1nKhctMQcgGh3WOtoZt72muL&X-Amz-Signature=a42e0a2e5d031bbd7095aa43e14b1fc15bf40130203bdda366fbaa08bf480bd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQYKSDP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCELH61oZokWC2MX2u9qQZc%2BTZVxkGpFsGykqX08l0jTgIgHunU%2FUq37XarUDG0tq7QjQD97CmRtVPRaSM%2Ffh%2B0wpIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAzIpeFzBMao9tXMICrcA%2FKfoQwMx8de%2BnasE5WFTJ1TBotH7x5WyUc1vwiEN03nG5XCwWgQn2N5MPhdlT4ciOZSImoZNCxMIBt%2B1ENjWH9SQuN769izCZBxDNCwC7EXXBdcrQn8foR6GLLYzZP%2FGCEO4I5HsKBA58y1RFVOAHnNC9ieoBayS3B2SLrfkg6M0QAORX%2FkHFkoTKBvxfWAE5PSfjpHv0xibgeYySzs5oHTQjBGB8nTAYUjFT7KfIAum38WJkf0fWppJY7WuFSW1i7NifmuU6%2Bgxq74dPCllnB0Hiux9BrypP5eibgvl14dwiFTmpEuYYCvx99y8cSEheBT3QeDMEjbIONs2jXlQO%2FNxr7JCAaaQTEdi2har%2FId6QyRoWvn%2Fyc7dB0Zx4RbBCyC4WC%2FhyqCy7LNK1%2BcXr7VdWAmNStxjQ2knLPSEs0FwL2RdzvbH4dH43QQBUdTl0830YOj%2BAcN7Cu0clTwbCulOdJZHvgdga33NGXG1Gv9thfmnHDbLjJyHt8KYdW1lFyBlqs7ABo748M%2FszDRWsXZDdYFc0DmadOuoaDQl6%2FJmfw%2FhavELwa21pK9zRDNHZxtHkYPSkbkyN5gNrZ1mTxeKFzr1GpDuhXOEnEg4DINbbwi7k1f2u7vHc0tMIq%2Fhr0GOqUBFu1toWg6ZcB%2FSMO8rfl97WwlfnN1kDDDjllphf7mrH2J9uI0qHGqUhz9YJm2J3VBK4kuG7WCG9IXXStMyIAc3OTc19D0HnslJEtdjmAtd9y2fZzyA8G4Tp37h62gdmbK4y4oJCvSkJO4t9Dv%2BCiMdljG9xM8OKhIekA5qbh7mXm6WdvbS9Nl9GUH7SfqRl9AK4e%2F1nKhctMQcgGh3WOtoZt72muL&X-Amz-Signature=b62f83932c398ccc94bdb95a3923c1a30156d7691f0c393a2d7603e87e2da16f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
