

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=0b5c03dad913e617229bc2db39d78b2272ee738bf0787ef1c9ce71e090d35c44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=22cd0acd32984f1861c3b9c682c2338fb7d1511d2ba9164175da9c970a854b50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=009d8a85fd046b2228272f116dade7c5e29c99a5cabb9453dc01e2f0ddd815ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=8ec542bc58ad6e292741a99f430f208a4076c2c2d8b4faeb8f5e121a163b1628&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=32bf2e26383d0c9d8d15ad88a4fd038349e4e7f6fe6a75b555b9ac5a553b789b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=15fda64809e8558b8a7a0e1f1d2878114fceafe18e10b8470b5174825b39a1e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=29152fe1cc2afe0295a4b2e19f82034479e633d323b64f6776b0b6d2eadcbe1c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJBVEZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDKBPPz6f1VDqb%2FvPy%2B%2FAMIIEjcQquFMdaxLG%2Bv7u6RVAIgegLNp%2Fi5oXE9VL5gV2%2FNXuXyKAsyQ3N4oALfGZTaBQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMcwnVm2kKHFXhlXqyrcA9aFg%2FPQGmFdRy6VaA7HA%2BFvFP%2Bhxud1dA18BawLVL96nGofdviq2FS%2F7x4914SmKOzjbsJhgQdcUprT%2FqSvrj9%2B2bCD8lRn%2FgRMsoUOHMEb01GZrFDme4lDe9Ik4QgCDXzRAAYIRVgufyXC7gMkafnFfspO3mjUiHscTDBWEDICA9kJyRjBTLAfhnBIgCChic4LwQ5WiGDKV1pgTw9LpkkkjjjZytc6ZDCIKXp9KhDkFZN%2FHObT5LW9yG%2FKl8WDVwbbmownA6gtsit2FrImMZrcv3kfe50ZokxEQzs58rrkQmWH6bR5QiUeLMgJp%2BlOwj3DS28EgxbQKqFKRgE%2By%2BwKOBCwZSDEOsbN%2Fh6aEaFIsaQq48EExPyuXDJXXC02wRx2maLSSUSZQDyGUXyefQ8OZuLm%2BuX51XeGTHpcR3EnSPTwBMgBqqA5WR7GSVFACM33HsAw%2B7xPCN6dzW9fNyK5U%2FaENrqoRSV8T1hX6i6hVbqG060SWrNSznDoEBV%2FCzp1UtBLksr%2B9%2B9t1v0qo%2FhhsHLkde2xW1lRUOje1u%2B4Fy1HynJq0BZTCxIqBevDoAxsjve4KEFXrBmSMxwEa9B2ifCrXyX9iybe8h6C6iiYmbwTOkP8HJNSY9x6MPzqj70GOqUB58I9aWSnyxtKlSRW7Cmym08c0tdjENgfol%2FZAtLCMqBI8HxOv%2F8L%2BA72U7iUtgONSW52Pa5sre1zVJTWzot6EuxWhCmzvjpOAzjn4deAoEUExI6t0YyHTQkS9sxKby2WGvEtk2tDbrcysj00txU2Ui3oYTWPR%2BcKBklgjrOaVkIwiawR%2FytO%2BUJvJTLn8pyHoEw8ItrzoG%2F%2FAXZVHiaHxZRq5M7e&X-Amz-Signature=3fa255007e3108b9c4b82af7a99c138f8eba9496e7cea04d6e7c4af89861b707&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSZIQE4R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIC7AjJRA3eFB2O2LuJicYVg6hgmqI2yV5GdjBZhxLCxqAiBf4qNyY9svqbBMVhv5%2Bna8Z7XcTrt%2FP1K8skjTetv8Syr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMZpvR1fZLa5L1UZHFKtwD8BpRqPdWPdUbE1tF02m1HwCSdobNolsMiN1s%2FHTmhmLScBQjEWHq5hCSu6eaemHvmXMt0rWnX9iJ%2F4jp2VfSNTa%2BmhwRwJK%2BL1NXLqmPxm1S7e4%2FhCUxGWph%2F8FRqpOsABIdzTmgLjrQPP1Q%2Fvj88FfUWWZX2U4KB0mmU2gigQCb6a44b5uZ%2BG5Srb7ZyPY1uvytUZTZDAkCBQmAc9X5P9%2BDpeO6QcRqSXh4uLhB0A284T8tmULyXczCeo5jOWVcTivHe2gnLnyxTZ0yd8P7IalpeGm7PjE7W7a7w%2B9cVCvU7b3EV8lMfd8bf%2Bf6%2BC6S%2B8kisyZ475ZlDB5cjNM49%2BCSAdAC5FeKBHf5daG3StUJkcrvi7Rh6q7eJLFEdcNPIBpD31CO%2ByiupVVTApEgwrDgC%2FZP3vKY4hLzKvR0x2kEY5ubRyj9I0rTJ9Z68MlwWUCG5ZXC8BROPhD%2BZJDxlKOjw3Gz%2B2uHgDiI88Yl5LZ3%2BuV3C3gpctorginyrLY4O3qtutnOo36H9dV5qtaO%2BQv2QeZnTcgn8Za8SsJtabDfjfuCDVDwJ3eAjJkz9GE9r6uLrOAtMzu%2BEa8erBZDhnhGItF9nvwP%2BsRfEZ6OsGzj9M2ZHVu5T97uPK4wk%2BuPvQY6pgHkKSYiemO2aCJt5QYI4G%2B0O6EXGLTlRBycni%2FOj%2BHEKzBz5VvcNCZIKYJx3JRajxD9RriO3LqXwe2tgj%2FpCCkgUS9oqoz6VUookCZHC1eDfRo4gEOpq1SKKlMJ5xAD697kBBPDDoTc7%2BGSwwQj7vik3S%2F9dqvSyYpMSlCbOaBurSEoylHmH1KAXdQGSUY8Zrodwdy5evcHCfynAy0oH7ecf50LWttR&X-Amz-Signature=d29fb7e6a0d60554f08babefd3dec7e68fe97a98fa038c5c0d406d7743c29cd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DYOGXOR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCICriUZ79FrETFAKF45Gvcs%2BeuI4czmrshw4qKhEmI2RXAiEApRu8hdNKthIqcCutGBm3Q1bqRU1SLSk9rsdHKqLiAHsq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMJ7Hg4kwZEO%2FrvRnircA2Lx5Ik6j6u0FoRHb9PTf7IDrHhjTRf%2Bt1vJRlLLasHjQQ%2F1nTijN7FVgUG6cADDFdafhr8o8gYxy2jUt1BMycUHJDDv00kQnPw%2BKm1aPlwNYqREe8H%2BcJcocnSx1JN9tS5kGVcifX5AtPtfYBx%2Bi9brK3MSa8l%2BaRcZ4LC1g5XYDyEi2wyHtznZ4SAtN24IVgLgsMp6ktsF%2B7S9NWLt9FjbNprz3IqxZ1E0Qo8hFQg1%2F53OacdN7mhPgI0rbRzkiFa4HZpaQX2295XNGOTgLaUo0%2B%2FNeYiJbRn31zC2PnEY1gGPLDSKH%2BU3HpxYN%2BsmgsWVZlTgfpibBjknblnT3u2PWhI2qXY5%2BlEv47A9Gwy7N2Uvkin2j7Z8%2BnoCW283XbG3cAGuxTtFbAuT2LPKmAWu%2BhAKVytyTNBv%2B9W2RBTSHtTJWV6dphwAZFYnmMl%2BTrQXEY6g17YI%2Fo3cHvLzv4OWmjtEeAM4LPXo5ZpFGXRbdsYaidxvXatwmdyFarwsNxCGdNIboQr5kfdn3V%2B76LtjMHqN38NnUkpogZELqVrxvzUtiTk37I2PMW1A0%2F8xn5vrn%2B%2F0CPUZR3fydlZ5jxIXvbKZIg30YZyU2%2B4Y%2FtQz2c3kc1vt1DYef7o7MPrqj70GOqUBmE2cNeKbHdNClI5BMFzVQJEaBrUDvaXnNIGH4YkV05RhgxzZz0tKDtqWWea9yZBi36VJNaqKiKF%2BKdJBIMvSott3yZDALksCPlDf1Z7AYyP0TylqWpvwthyKRALkg5wDhw7aw9U1DdkuyR7tTmKgoyQEWfHSxOFoSHdP%2BSyHGG6yzo%2BLj0eSKzI1Mp%2FOZ7lvsYZdxpjaO3Pb4MCv9oYmPu%2B3FFfD&X-Amz-Signature=e4636053d29b93ebc1342c01c4f7c495e0a26bc7b43fcd79a9457cf4b8d14c39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV5IIWUB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDH89WLsT4UduiPTaUn2fRyihYof%2BJrB5etMLL2q6Y42wIhAM69kVuVMcTC%2FoarVkJaefbcA3rYXDwDDwwo5YNb2DfCKv8DCFEQABoMNjM3NDIzMTgzODA1Igxc6HTmqF2sn4FUYAcq3AO1w%2BczsdDAAfl8mc2wnGmee3LtLo94SVs7ZbvfT886eeUz7nT6Xa4wYTsFZRWBhAC%2F1qOklO76z0tz3TOtlE%2FHgO6QbdeBn0djxXIHcy6wOu9gLLYEdsCQLQz7%2Fw%2F4pf71ReuF%2BZv8BZchlaGbQT0WtR2dcCvO10pUvlDOrWCIodi%2BBPdEeNMBy7OzENJLOHes54voITWNs42hneDtdsN4weRfzboG8r4eNPpbgaEdu2ShPCiAzQisKK58%2FU%2BLBsnEeMfFMVQYB9fVg%2FUM2ew2dNlHTVP7RCR%2BzDWXUfzv3%2F0aYtu%2Fb7UethJHkjg5lZIkueY6HWBpqjW0kWO79Dqxtg7O87ndBdDb0X80QsKcYsavoNMB3XAYgqO6KUT6vgEeqANrQqaCgxvKi1s69aoHpkPtwfqoM9B33TFF0t0jHsdgzOyfGXbOmCeWmah5ZgyChFiWV43%2BxRo0pqbRT6buP%2FnUyhd9u4NMU%2B7r%2BrSZ6%2FZvWyvbsZEtWPN0NZtHHHE8bhj8fIGigGYagE6XuYEnasAZMGz2eoEm0d%2B79h69KJk%2BRr4Rg5lj6r2EpjGNTSZNqwwD2VhTTek5Wf%2F8K%2FQ2yxNYzxgMh6430g6IqjzzXoGp2%2BR4nhfgf0zaDTC464%2B9BjqkAajl8WoeP2lyYODbh6HdFRORgO3WIZSMUJP3eEFsVmiGQm0m720%2FV5AmfY%2FeJ8mjq5N3ggnXHjfU9z3PdMAXt%2BfgVgA4eVvHK7FnKAOmKy%2F2YM%2FWCGTEdoSCkC9yIHicVn1cjgG%2FKarIfrFxFenN4Zlqs%2B80ukZKWHP7Vrp%2FevpYuPF4uOVmdWHOBfAuBwtF1sWRtx9io1%2FYMrqUvNZDBjPBRtOc&X-Amz-Signature=d024f6edac3cde290cad03457bf6eb6806931c0fa5045412999e9d1be18d3a07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV5IIWUB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDH89WLsT4UduiPTaUn2fRyihYof%2BJrB5etMLL2q6Y42wIhAM69kVuVMcTC%2FoarVkJaefbcA3rYXDwDDwwo5YNb2DfCKv8DCFEQABoMNjM3NDIzMTgzODA1Igxc6HTmqF2sn4FUYAcq3AO1w%2BczsdDAAfl8mc2wnGmee3LtLo94SVs7ZbvfT886eeUz7nT6Xa4wYTsFZRWBhAC%2F1qOklO76z0tz3TOtlE%2FHgO6QbdeBn0djxXIHcy6wOu9gLLYEdsCQLQz7%2Fw%2F4pf71ReuF%2BZv8BZchlaGbQT0WtR2dcCvO10pUvlDOrWCIodi%2BBPdEeNMBy7OzENJLOHes54voITWNs42hneDtdsN4weRfzboG8r4eNPpbgaEdu2ShPCiAzQisKK58%2FU%2BLBsnEeMfFMVQYB9fVg%2FUM2ew2dNlHTVP7RCR%2BzDWXUfzv3%2F0aYtu%2Fb7UethJHkjg5lZIkueY6HWBpqjW0kWO79Dqxtg7O87ndBdDb0X80QsKcYsavoNMB3XAYgqO6KUT6vgEeqANrQqaCgxvKi1s69aoHpkPtwfqoM9B33TFF0t0jHsdgzOyfGXbOmCeWmah5ZgyChFiWV43%2BxRo0pqbRT6buP%2FnUyhd9u4NMU%2B7r%2BrSZ6%2FZvWyvbsZEtWPN0NZtHHHE8bhj8fIGigGYagE6XuYEnasAZMGz2eoEm0d%2B79h69KJk%2BRr4Rg5lj6r2EpjGNTSZNqwwD2VhTTek5Wf%2F8K%2FQ2yxNYzxgMh6430g6IqjzzXoGp2%2BR4nhfgf0zaDTC464%2B9BjqkAajl8WoeP2lyYODbh6HdFRORgO3WIZSMUJP3eEFsVmiGQm0m720%2FV5AmfY%2FeJ8mjq5N3ggnXHjfU9z3PdMAXt%2BfgVgA4eVvHK7FnKAOmKy%2F2YM%2FWCGTEdoSCkC9yIHicVn1cjgG%2FKarIfrFxFenN4Zlqs%2B80ukZKWHP7Vrp%2FevpYuPF4uOVmdWHOBfAuBwtF1sWRtx9io1%2FYMrqUvNZDBjPBRtOc&X-Amz-Signature=0efda382ed5b3d343f4c5d468c5496449778fc347826395a476e37ec1634232d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
