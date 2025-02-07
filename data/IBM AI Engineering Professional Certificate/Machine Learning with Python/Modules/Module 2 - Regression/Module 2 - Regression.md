

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=d2a087049738c2a65cbbb660ddd26e065a837504b6da098dc11199d762f86c54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=d112753cd9176523415cbc160f6d094449d8f4f41e7f45989c346d39b89c50a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=3c6c2d143e9c917eb422ef2238f2ab42c3a0f0fe6eb69902c69f219face0693f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=43a04a047a388f7147a1dbf7aad4828f1b4a0eb1fdabfc27d0247814cd87cb78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=876ea58b538e0eabe24dc486cabd9fede8796a6cde1c3523ecba1aac29194b73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=d42e1903fa1319977212346e7d533e05264ccdbaee22fc8b7dd8b5a8a078b74c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=c28dd949922b8920a4cb037d4c48a9414cc7d935eb5ecc7c33f8cea4f76a6bee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S7JQF64%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFclP2572O03EagyBUk%2FaNl4dll3GPDrgWvTRnr6bEk%2FAiEAlkNoC8xSGe4aTXewcDFcN0dprNAWCaElBxKjxWWGjAoq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDEDmIkB1li7ISSbQsircA3eZSjiXTXxoG78XMqG6gB6bi96LI39nHcc0vjsjK%2BE3nfp2qLcwLVzwBbMQnM%2FkDruqqq20wndVXw5bbmh4CzFN9UGpVJICogVdyIyQSIc3yKVBnAv7DxzwPvKkMtpXqTTMMaLbpNBrfSXyNpMb0TueDi4DtdU%2B%2F%2BMu2Gcf5mtHha44rK%2B9e%2Bj%2FBcEri8DcOAVwIfVsc5uaGJ%2BiwD4hkAgz2dNTpdpNOMIoe7BBsezqMHSdPPoKShGbtd0Pq8f%2BuVLv%2Fh%2Fw%2FHvWzMNyW7Zhxnz3Fu%2By0tyoDK8%2FzeHhQlbJfuc3jDHPPV6AWi47YDdTYbBIWZgh%2FwzOQPFJSXCwpyxmTLHWNUIK4HdwG77Jos4KCSsUeY5wW5iTdYiU3tpIly8yVv00%2BnBj7SQ1pXH%2Bg7FAwrzBoh9%2BAYCRWwgOGjkXNzhBZ4VQ6lCS0sal8pTyjjMALorCf8Wvj56kEfX7lz%2BSuf3EHF2L2W2Kd39aS17dCgk5ugH5DuqFpOO9VkK2tINubZUZJfecL0ZJNAYf27EBFHd2MAlwpoHmyryNdnavT01rKCYdUrBYOV0vJ8QZk6d%2Fbd2pGHayO03GwVlJZTd5SznVJaLYiTkSLlgR14ctTMsb73AzwtfLdGzXMNXEmL0GOqUBLYCVNfzSjEGwTpxPZqPGgj6iOflwAA1inudO6i04hxbyRjYOWWiau5fQtR8gRmrpMXdq01WV8VoybP162ydkVDWiWTjNcr0bGVTwMHiO28qtLSwrG08D4tZhCYKYwf%2BJ%2FaNTXGtOJ%2BSsYW8uCZaE0gbhsLgrVA57MQAWDZrjHi9PeriZtJTBC2wuJCqJGf7qy7xlN6bT5ijHKXol0SWmvRqBwZjF&X-Amz-Signature=7093c7832cf42098e273c30d3fe72fde6bf88208a6f41309e1225fe3b0b679b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT2BLXKO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCxNafgJIG4lkBzb5HcLzRbWUGaD%2FSVgMezPq8MJjHyoAIhAKdnSrtBkAKjFbQwZFg7u7iL%2BBHhDvbBUzWUR8kO%2BeFxKv8DCHgQABoMNjM3NDIzMTgzODA1IgwNV6mY6fO1iq%2B5ssMq3AMKZO1nT%2FzIGzGzttlc5HEP5fesI3v5mCEkk4iPAyekCe8gDmIf3NDV4G0IOKYqhe52Xl%2BrSg0IXfkIpw5RzsIzVkI7EtOVsrKTEzU5VpleYaZNvvAEYmL75rD%2FW4OzlglLyzG1A8XPuhWUwb%2BxBahqNF6SZkZiLZRnsQN96%2F%2BxuKOMKDerG5kRsP%2BbEU9Pzy4DH6jsC8Q1jLz7Mp%2FYRiZXDHVo6skpzK3zbPWANPb9TWpyMZH61yyeP%2F2lZsMXdx2bZCDrj5i2Kx%2BS%2BWMYoXOAZEjTGW0ffYUOJd%2BwjQFAw93jAK5x5AenKR63%2BQg2TJ50U5h2bVeKzzUFZD7H13iHo4Pl6YfEVwXIPWmL14gdHJao9qdILoQGyv7fp2aH1QT308Hph39B6Z4TXqv3Ak9ltAVIX8Zt%2BHkcKqQtUstbfEa34Se5Ko6ThQKFpQKaT%2FCSJjh2H5%2BHr9iqHqqRiYtTvKjHaMab5tvq2kV2MUTVR5w0C3prr5CU5%2B2Ubs%2Fh7Xv9Pl%2FeUTDxbkw3lNl0sVC30waps6wE84UwrTHqjcWRHyrmt2pWBKJN%2F2xA8s3OMxcGB4viBtigNDTYlLE6vhea4DFFK6Od%2BERa3iryiSfTxztgtE0TqKZIznzytTCTxJi9BjqkAR%2B7gTjQ%2FnZ3rOcNKxZlN6tL1hHgX5lL6Z%2F8fKKzqt21fILhvptkKBE3L91LRkjAVs7W6B40UsPlenFKt%2BMYE07CBaCHIwJ4dEYmIc0qLSjNrSmVY4R3tbUnA1j4fmrH%2FQkguJZYb8OZsrROd%2Bduk6%2Bldj9v6rWKncxct2gsOqbFReTtnxflamorqWKmtXYPnarefNBRKr2iijI%2BOVRZX3X9GykS&X-Amz-Signature=61b90a9a3c4713d5d20db3e7747195cdb6e136d766a9dbd1f7a64a9ba469d60e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6TUVA76%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCTwEQGCF5QQATPld2bDAHSj5vp6RsyUotwygBdwmYCgQIhALzcqeRGV%2BdJ6E08wzUruJjE7q%2F5NvRi9fszJv5t0ov4Kv8DCHgQABoMNjM3NDIzMTgzODA1Igxx963%2FGMija1ftL0Uq3APTDG%2FZAbBSnuBrBuBblRMk5YTycoem9PxB5q6aRaXHBJcrv5pUO7n0Hk67t18%2BtuPpsSHmT7xkxVn%2Fj0a7GfQlau7FkLP4qIqkHNC2%2BIH%2FCq5sNFb8eRGI5qD%2BJh3r%2BJfU9vIdfxXK8uBij%2FgnNGRNkcRkdkCT8bpqTJk0pvmA%2FtjRVGULLpPyxT%2FJ0spQptgHuVxHWobWtF17VEX5MTKM%2Bwz0%2FHHVqphJSmBMU8H0SDAZQ1aOqR3U%2B9aPviQIszKm8z9izA3f0MHYt8%2FlRM77WqI3RBaeMm6nGZTy%2FjXAs0I0AfTv78pr2BDard%2Bd7gIhUqH3rxO3qTbIQa2c6LNnYVkBhwU5EKzsjVNKEIBkeCYkZL6yQ7w2Xs75O1zc%2BOKzGIdJ3QHQsNdLByLDProaB2s%2By3UiISWu6SJdwZQBB2Qsi%2Bi6TbWWhrGnER79zLEPLsbcYqSYu7On%2FfMB97UndR2%2FdqGTVt3%2F1Mz2LKHj4LfHfGrzUq8h3CyR4rH8C%2FjvE64bvJplHTVI4IziaSdaYbwjgOxHMAiPgYFWwya2XfQEq0PZyd0rUHYpBGQYq4jGsagls4YWfOFDE5IlY1acXjSz%2FC12LzJ4Q6%2B%2FYru6Ba5cBW0LqWtbOEmfKjDjw5i9BjqkAYjonNva3HppV5tCF50PIXUnhwtTygSk%2FMIPo%2BtO5XVLrG6tsAfW2cO81BOsZhhfNuoQwfwrE4duyjqQALL%2FK3gIshjQ0Lvp1tqB6EZQ7DjNdwGE3EYkgc%2BxBgF3XkwAoflHY0AlRghsskP0ZjTzpb94zxA%2BHu4OxVpIkDbUmEfrPU4hqVvlDq6cwQOHUJ84W0lWOUWDMtKxIXweFu0vctUQ8IXf&X-Amz-Signature=8dd0c60ea0428599c8d0c6d5f33a87a57a86af164c7909529ac961612b8ab614&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KS2HCLE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCeu1bqRf2THccv0nYUTKDgXmM1y7UagsIlB7GklE2AQgIhAK2a2w9M336y4R0eWwryMtmz7kqJOsRS0OqFPYELtkAdKv8DCHgQABoMNjM3NDIzMTgzODA1IgzkLWcZVCZhOl31g7kq3APZC0d%2Bl8ILCVYkCQAfVmHiJbc56llVXNk8Yoh1Joko8DAW11yv4Cc65mBbE%2FYu4jhHGzMergfgTPK%2FaYj8%2F1%2FiP1SqLWbq2BbiaS0MOFcbYkyQKGAwrndtzp7rObK%2BJ%2F21U3IMdaX%2FyLbNiKo3NAtjfyC5viWISr%2FyrfvBaGECcskSYrVrEUAAzXb7ra4cJVpBMsTGEt4EPWqxFY6znIXJ7PnfCoBeY3nJEROQPm2noXDOnjEUCUjfncNKQuWQFyy14OZogn9NiVbz5%2FkrRb%2BogXGX%2ByRUmqFxOIDXpio62IMKQgVg7lzjFo21vm7uo9M6GO5FPJhBV2ypQGrXPnyIO5yOXP1Rp5bvHMtyYh5SOfII%2BGEtTDddsAtiXhmgCYLfRFqLUBTVniVDy%2BjhpL1uFnVq7z2WQbwqC4aVxnMY5wVlZwkmJeLX8oGoeZQ44wpHwxv9ejPSzcrlEmms6BZL80dlQHgCN9WxxZT740AmgP%2FdLlpp8D7%2BOzm1urJSpewo6LxA%2B5J7fKZMwZ21FL6TwaGRmt5VQme39myzIZGXGg3YDVAPVxwfvKSsCKsFFX5j8jmXi0odmV7QznOWr87NyHdDy%2FLug%2BhcbTgUbRO2E%2BcfWYe6UcgzSkiy3TDmw5i9BjqkAe%2BtOPUA04d76MeYyB8awvH%2FQFboMwSEQS4tGRueyD9YgVNclfb%2FVraskYG5b4JGLmD7Q7O2XABxhlI0NeEu6Pdm0Qhx9oai9j4WTLMdT8QLdfUMYTEyx5U8SO9BxyiG9nUvjJZwzCuTPP%2F1UDY%2BXal%2BJbHw2c%2BWhBUMZ7uKdCmrHOQCw3xlFird1X3QpE7NVB4GByVwkG8DECbfvqOSmA%2BfPKLN&X-Amz-Signature=32fd234ab9987abfef5dcdd5c5f17c774176814f519fd07c45b5dce233672841&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KS2HCLE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCeu1bqRf2THccv0nYUTKDgXmM1y7UagsIlB7GklE2AQgIhAK2a2w9M336y4R0eWwryMtmz7kqJOsRS0OqFPYELtkAdKv8DCHgQABoMNjM3NDIzMTgzODA1IgzkLWcZVCZhOl31g7kq3APZC0d%2Bl8ILCVYkCQAfVmHiJbc56llVXNk8Yoh1Joko8DAW11yv4Cc65mBbE%2FYu4jhHGzMergfgTPK%2FaYj8%2F1%2FiP1SqLWbq2BbiaS0MOFcbYkyQKGAwrndtzp7rObK%2BJ%2F21U3IMdaX%2FyLbNiKo3NAtjfyC5viWISr%2FyrfvBaGECcskSYrVrEUAAzXb7ra4cJVpBMsTGEt4EPWqxFY6znIXJ7PnfCoBeY3nJEROQPm2noXDOnjEUCUjfncNKQuWQFyy14OZogn9NiVbz5%2FkrRb%2BogXGX%2ByRUmqFxOIDXpio62IMKQgVg7lzjFo21vm7uo9M6GO5FPJhBV2ypQGrXPnyIO5yOXP1Rp5bvHMtyYh5SOfII%2BGEtTDddsAtiXhmgCYLfRFqLUBTVniVDy%2BjhpL1uFnVq7z2WQbwqC4aVxnMY5wVlZwkmJeLX8oGoeZQ44wpHwxv9ejPSzcrlEmms6BZL80dlQHgCN9WxxZT740AmgP%2FdLlpp8D7%2BOzm1urJSpewo6LxA%2B5J7fKZMwZ21FL6TwaGRmt5VQme39myzIZGXGg3YDVAPVxwfvKSsCKsFFX5j8jmXi0odmV7QznOWr87NyHdDy%2FLug%2BhcbTgUbRO2E%2BcfWYe6UcgzSkiy3TDmw5i9BjqkAe%2BtOPUA04d76MeYyB8awvH%2FQFboMwSEQS4tGRueyD9YgVNclfb%2FVraskYG5b4JGLmD7Q7O2XABxhlI0NeEu6Pdm0Qhx9oai9j4WTLMdT8QLdfUMYTEyx5U8SO9BxyiG9nUvjJZwzCuTPP%2F1UDY%2BXal%2BJbHw2c%2BWhBUMZ7uKdCmrHOQCw3xlFird1X3QpE7NVB4GByVwkG8DECbfvqOSmA%2BfPKLN&X-Amz-Signature=ae9529a82c67bb9fa8dce8718250c050ce78c4d4b91847a2fc9475e7e6ec97da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
