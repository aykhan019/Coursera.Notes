

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=c46f2ad514272c35f45d12aac140cdabb5fe343cd11692d65ae82e5e0a5bbd57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=b886bd927578a53b7d4a962d1479203f385ce38b0ab89ea59ae0d704044db3d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=a6af98cff1dcdc997b9826edafee6d3c78c1a5cb52bcaf9565dd9ee2ac652517&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=3b486af70246664c1c31eb01be48d70407b3a4601e2a5c1ab7836669b140e60b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=44dae650be0ed0618ac5f1f4a6b1f88cdc8c879ecf50c8d7d29b7c7d0e68755a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=2fbb9b44343a1a8c0da01c6a50ad018933db16e31b2607510e37c20d4b54a206&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=0d56dd76a1713b1bcc7c2561eb6e089dd1d87b23c3903d60b105026291932bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIPT7OA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJFMEMCHydNmyJfep%2FRQuwpXtgg5q8SheT5c1Ssl6xtjRrtpnMCIBH9uhb6m77QgxOwtYqLXXPvT6hIyQPBhw85nOONhILpKv8DCDYQABoMNjM3NDIzMTgzODA1Igz73RU10aPhM4%2BgbrEq3AOJNAH%2FIqaZ%2BjGiNW%2BVwzcsgYsWRKFC88RTwFNcW8WmtG66ZfHO0C4uQsAUB%2BeMLrqtLFvMxl0xNS82aPC26fYCOVHbkMz7SQGQW9ihmy7IqiEA3qiQnDb4roXKHlEHEhJrMyuQ13v2PCCGNe06%2FRtcVStpkXfvtZlbPyNBsMS%2FyEBQKo5l%2BYlnDockMJTr0u5ik6i6mMROdoc%2F2vS%2FQSP4zS58SFohEXu9%2Bo0fxCviDXISmdLneE%2FBbEo9fNcI5pUJIQ5ODhmJ%2BiZnEE21vUIbkhPQ97Yu8pSKeXGKEQcSzwT2RjHQjsSJ%2BE%2BSQkA4y0d%2Bcl8w88Mcj%2BiSi6kIWEsjBqYT1PkOBcc15P5yfaU1mqUlp9ThXolJe%2Btoh%2Bta5VPJLrakjVz6%2FajgUJRKCZMl6AR14CyF0Pw%2FWD9xq9eN7WUfbP8Zh3DpAv08wiG4aozGa5cHK0u3YeSGk4aByXC875ZULjH4%2BnMyb7MxroVTzSPlm5z%2Ff5UG%2FwM6WQG7TU1ckOSFAWBk9zInfO1%2FSEYMIGamhxiG8FGq6CfuFer%2BWY6TOk6Z0jlpaSjtcmHLgF0gysUWtQPNKIYYm5VWC4iV04B%2FX1YzcxQe4dV20XbGCtWfKRqn1WF%2BcT%2BUFTD1%2FIm9BjqnASqBSB7sEGGStxNZs6QoQ%2F03I3uQ1s2ulPH%2BOOqmyyqSxe0Rs9sHDkOvY0f2er3fLl68YhqaKEeVKSTf%2BGH9aAkc22srDDshfaIycjGj2APcjfloCXXuVLpjfupMVNkBv3RRPQkL8mk%2Fb2G%2Fc3BfuZE0R9hBSS57arQrHU1UmK%2BzDxNOi3SmT3RxQPcdwkM6IPkZlW6Wz9GsUVvRFecZTrGcTw%2FwQckv&X-Amz-Signature=2dc0d696bc94015eab1b2350776f879f7054a86fc52aa096e25208e2e1f061d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PO6ES2Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQD%2Bmh%2FAbCV%2BZ37Z8Nns8PFs4YKJZRcriyz6iuG34iQ4owIgUkkSHqk3pkF5DzDQbp9jNPtYbcBBVePuzq1yLabs%2BvEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDE0hyN5ODH2CbdHCiircAykMlTHovu93HN9VYFkdtqnfP1Ge6kq5O%2F6gGH9FEN0%2FoI6H6GDTCDlRLgrVv0iB2HIKIPHnDMpOKEj6Xqz2R5zQbagxX6VUm3wYRO3XtqVd7AWkZo2ruNh5rV5UG22nCmMrnhOrNioYkhQx%2BlyNTERILpx3j5N9lBnldvKNTHUDGqdc4ifn%2FhuhmxE4Sha7Or3XTUGQ6KdFYav9VWcmWihlcCWqB%2FtHLcCo09glHuy4QMbqPtTMsO6P1dqWB74YzPyyDfzjOcD3zEE2%2FUo%2BCHQzfvGd9bYGwmB3hLKudnwvX7%2BSpGs%2FFjfHlZzbhhY%2Fj%2Bz%2FINDnj5jWSKOvMDAYlnfF70S77TEEDJTacW7rXwalretyae0fvZX%2BHWW%2BbM9q3vmiIpeJxl%2BS4UNykvCWaycqcliechLj6HVMKNhhue1E0JGtCNgSIwfsMz59XNytnyanVFjYagJPEpkAgZ%2BVNLQ8jvEmQPifMqMjoNemLjm7PGi0EKraCb9D8%2BQl2BDcoysDX4veLlRgIqaZ1mR%2Fvufc2sw9btxKsRwqTOvAK04DFjsjJGG8IW5dZ6nAvuPWCM%2FLq%2FW7HQ7%2FLxyyERiFiwszQyb2NksS1M9ldl7oy5gx1YGiOUOzGlgHXi4kMJb9ib0GOqUBa0bQVWO24VXf2kgN4e71n%2BG7f%2BvHj7rWbNtSm2XDyWGbpuk6JrJkuMsLfEAvEErvc57mmxPITnGO5OQB67cj%2BIVtoK4g7s%2FWxExyUmyxbNZN7f0kilX1%2Ftym2EuANECWeT3HyaJHqM%2FHY3YdRIvoNJTpg0cH9aDqwuh6oMFJwn%2BMBaEMF3vH0JCfYoiR2EiL%2Fv%2BZcZt9W0w3kqGYpDvXEuD1Xr4E&X-Amz-Signature=6c7c42620cb109beea4738fe9399ab2e022bfaf58e87eed0b05665380cf2594c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHE3PSUU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQCY7rWLyilgye7cOJqd3kahpbN1AFpOXBxtmGFTnvb4BgIgVeIe91oTr%2BZdRsMzICt6m049WFDbGhcURCoDG0X3H0gq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDNHc9B%2BefQpapWDGJircA1zpUNom4VZSxcT8oEAxbUiejzgha1r9Y3URfnugtkV6hRX5HCAd%2BtDbYFIpgO09GueMGjemF1MYP2VOh06jwjcS1H36YjGLkQ%2FRoG72JGjudf2h9X%2FjmHA3ctCY30MOEa%2FjdDAS3xxHZRIyvhj5tcHDaarNynkPPYbUlXiNC9ll6ATtm1gAwTsCbFFoEht862GKPt%2Fhkb4jIjdnVKaLzn%2FQ%2BIQ%2F3jdnI7nhOeKw6txKXCWKaUIDupc2RwCmd5Z1asSlW%2BF73TKmWbOfzLP0ilzuIX%2B6x13%2FQC6wDgBnEXlkJNqzFWmgDo7dv5FxhzY8XhNm8aiMcfhzXW3pEp5FlTIi0Kpolqdss%2F48B812yH8S2WHG%2FFLdkouGfr4DeoBpe6fej1yMihyoIHhjTxzVNh6vjID7lWu%2FgOa%2FuBCX%2BOkzL%2BCKX9K8V4XwxOViEktGLvniZU4CnhTZ9EmsQPtR2NJ7mTXFLAgAYyMPnME7mOLTvslFkwqMx966kLgE4nwk%2FJhtWOIBO9xWqn80BBxMZK9GYeRgneAeFGKtJQggUz7%2F06GxfC6Jqwk%2BNAo66JccAxoDUlCFu%2F5NKX5H6oNkctml5tY96k7NqzLI9Ygq1HX68AG8UXbGP7eWzxpqMM%2F8ib0GOqUBkQWxpp2CIoZty7h3NP4vqxVw51KFbSg8MG6SMWCGpihbIxKubG1FqAqiTE7wqsCQoCSD2P3zMGAB025rgKO88MEgvO%2Fp85c7eD%2Bq2M0nv9Bf5H1RylrSzz2gm5e2QkDhOKEi9yhE7hU7I33lyYnL0BGYTOpzf4WZrMExuawgwGSUHG4snF7ZwN0ksnVkAG%2Ft%2FK850yWFitX6DzW4MuTAARCuzUa0&X-Amz-Signature=e6e8a0c57bcbdb26c82b0391a4520ef487c706b0feee2eb1996269d0aaefa86d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7SKKYN6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGNyx4OfrFPw7Uffc9HiokgF4KFQ30%2FP1sITgAYqJEiiAiEAyYxQWy8%2BdF5T59UrrrJV%2BmdjoakFxaMkwrlJrxDW4pEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDKJipgmz59PT%2BMAOECrcAxVxlp4nT32V4vtyZj0FA99%2FeVyk35rox0wiOaFvzuP6j7Yg7rywZKebf3lJfTsJbIXHXetckoXGE76r6MWtWz9uuN6WUMiA9iTT5nTQ66DZBY25H%2Blc4owB9C6T7CHjq3%2BpXLaSo%2BadPxGFyXwdnrk0KrNnFeOGPF2Zf%2F8dyS30SgXBDaP9cSjTTrv%2Biv0vX%2BqtuPtlL0y54374vreRNjeVQStqqTsRC49UIDIJEnRynAng81ZkhqZVQ%2Bm06qoVCC9br4iqYh6g4C8sw0jk%2FGBEe3BgcZAv0godo811U%2F0mw011y2b661Y2384fQ6Ts0c1UQ2VNrH7978hbYJSWH3iQikbXh1GUO2Ak9SygEfqYfNND6s41pJV0v2yvaOw2DGuLvr3mdZxKb7zeOzXteTKm9UXcScR6xkekS1LITisIhaqsvxM8NF5I6LYs%2FCOQ4KLrnBhX7%2ByjsJY55kE5tDVlfLLQ1DcikZIRUtod%2FV9iJA2Q9QGrwtkjep6%2FPW57nZ0SqaadJjQln7MCvk1UdCSvkvMxMjKFkTJ4Y9lgv6isyUml0KqsNwkcbqTzScILvG%2BptIFyTF4hOl1ZHBY7WP%2Fis4Omwsa2qASSjs2El7DDLprIt%2BaC%2FsYIb9DsMP%2F8ib0GOqUBk3a56Zd6bxoqwBOwq%2Fm0FJFSqJacjHRfJF04StwskzEFyZecIt7vfL5Lc%2F4Ct%2B3yhLo48FPPU4NmYCDF7pj1UgAEz6wnSoSGlMByG7g7OiWfc%2FLsld%2BjWp0z%2BK1MWYl9xmzrTiY4ruZLpzGy9EvRrKFiH8xU8hzTS6uXx6592oUJGV1zElQlzQfygtrYxx5LHBUKmDcyLpHPSvyFp99YLwC%2BTF3x&X-Amz-Signature=fbd1fe885fd3490f08e4429eadde5612e8f8d7d9ce84208d89e9f5eae21439d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7SKKYN6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGNyx4OfrFPw7Uffc9HiokgF4KFQ30%2FP1sITgAYqJEiiAiEAyYxQWy8%2BdF5T59UrrrJV%2BmdjoakFxaMkwrlJrxDW4pEq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDKJipgmz59PT%2BMAOECrcAxVxlp4nT32V4vtyZj0FA99%2FeVyk35rox0wiOaFvzuP6j7Yg7rywZKebf3lJfTsJbIXHXetckoXGE76r6MWtWz9uuN6WUMiA9iTT5nTQ66DZBY25H%2Blc4owB9C6T7CHjq3%2BpXLaSo%2BadPxGFyXwdnrk0KrNnFeOGPF2Zf%2F8dyS30SgXBDaP9cSjTTrv%2Biv0vX%2BqtuPtlL0y54374vreRNjeVQStqqTsRC49UIDIJEnRynAng81ZkhqZVQ%2Bm06qoVCC9br4iqYh6g4C8sw0jk%2FGBEe3BgcZAv0godo811U%2F0mw011y2b661Y2384fQ6Ts0c1UQ2VNrH7978hbYJSWH3iQikbXh1GUO2Ak9SygEfqYfNND6s41pJV0v2yvaOw2DGuLvr3mdZxKb7zeOzXteTKm9UXcScR6xkekS1LITisIhaqsvxM8NF5I6LYs%2FCOQ4KLrnBhX7%2ByjsJY55kE5tDVlfLLQ1DcikZIRUtod%2FV9iJA2Q9QGrwtkjep6%2FPW57nZ0SqaadJjQln7MCvk1UdCSvkvMxMjKFkTJ4Y9lgv6isyUml0KqsNwkcbqTzScILvG%2BptIFyTF4hOl1ZHBY7WP%2Fis4Omwsa2qASSjs2El7DDLprIt%2BaC%2FsYIb9DsMP%2F8ib0GOqUBk3a56Zd6bxoqwBOwq%2Fm0FJFSqJacjHRfJF04StwskzEFyZecIt7vfL5Lc%2F4Ct%2B3yhLo48FPPU4NmYCDF7pj1UgAEz6wnSoSGlMByG7g7OiWfc%2FLsld%2BjWp0z%2BK1MWYl9xmzrTiY4ruZLpzGy9EvRrKFiH8xU8hzTS6uXx6592oUJGV1zElQlzQfygtrYxx5LHBUKmDcyLpHPSvyFp99YLwC%2BTF3x&X-Amz-Signature=52eb73dba6d28e95f6c8fbd2d561906008693061ec5cd42d5e7311646af77c7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
