

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=719d9b5feb2c29618c5050c53932631f46a0ad549a8ce7aadbe69aa267044dd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=942047fe02e24db58cb5d199808451455cb4833b1de5ed1888701ecbfc8ae092&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=1e1540ae251997049600accfbe2e2e07819d431a300320f693085bfbf47d75a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=a36d8fcdaaca370e2e9c13ae80b87547c264ad3600aac6933f40fce0a50df626&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=6ee0afb0b23b26ccd65c1fdfa3ce1ffa631cfff6e22aa2a23c0403469829036e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=9ccf668cf827181dbeecb3f831ee3ebb51d8e45a66d7ea5989d458472cc5eb68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=063a9f070ca9d816e6d3baf717f2321c0bd817bbcd653bd8be8f50e4799368b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=9ca865c52b2c3a84962293a4f0fa189eb1845aa7a1e088e7c7fb4b683ae35b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W37WQF4M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBWigl62Qet%2BWDQpdbJtOEBkiAphbELXIw0FmxDfVu8DAiEA3Esn5phXj9vtyZaJdpNYuhQkDwiwNohzlDx5bBHhJCgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVWIWs2jlUaqurTSCrcAzILyPS0MFS%2Fpz8SxxfZaRbwEVkoWfc%2FsImyTPdk4jfPWGHh1aX1qxwB4al7MBJJk%2F3xObYM5jHFs6eoatLWErEp7wHyOGiz4XzOtRfyldMOK9y%2Fo8D6ND7w8LqOazLCO334UmPu5EKFOoHnDGSPU02zsQzBpAVj46frnKBsDQMnoHQt7SGRDLhb%2BwoaPww8P%2Fo41cYmibNushi8lMfN3gZHifrZQLTpJGr4F5cLwXnVh8fdTKqCy0iPWu7KOANWE%2FU%2FM83LlIIRhnIfW9Ohh9qzKQshBRDcUv81SYq0X6O6GTzDHUC3Gl0VuVIL5AepAVzi%2F%2BdVeDgHtngfauJCZsuPniiPJX1l55SM1OYU9YoqGxHZ7dgcmaau9HMmmNNKAl%2FYu%2Fq%2FO7kaK4dv%2BBC6tD4ytCTn2xtxpVYIky1Xo%2Bm%2FjhZGLFLbkz2RBanZktQjtu3zhVD7J0thBR0V9Rv6F0AnrP9jJY%2FILOX3qpYrihrY2A0K%2FTPQT2ugtdwGloa1RXfzUcqkUDLAN77pRBaYtlz74NpFbR%2FUK%2BY%2BPyKkWqwXrzXlO597EGRLiH9Dnec5xYWMyfaAaEAbpu7Ta2rqsKXn08D9nZ8bzQyTDTKnRmp2u3Xw6HKK%2Fif0uigIMKek97wGOqUB6pVpCdhRPuOXxFzAZJpBOzi4bmaBK0sAPw9S%2FVZMk5YgDlVcs%2FpNsCZgel0Obi6jDBjAUtEB76zQ4gdJbpYvvfaiIMGnwDvQ8TjWTG0fNRIVx2xIBkG9tQ3%2BsDtb2RXo2bBlUz%2BK5gvF62a%2BTSnO8DEUW%2BZbp19%2BAFyzNaqWwxIQngRZE2rW94F1cNjdH6FW8rXFH7%2B8P9Snexx1EUMCN57Z%2BE6I&X-Amz-Signature=71533d8f5727afdd488d138406c3947d8042af8cd85e70e8dcc8707a2b683490&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JOWYHTL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ8ae1rzXqnZhKfIRX23pX3OOZHwFOMdSwtpPCsvHbhwIhAIPP8L0jbEoaZQaMrl%2BAAkn2e8vraFtZXxn1s36rEcq7KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJaj%2FLNIE5GdP2CRMq3ANYky0TAdbkc4nnE0NbDNndjNltOaqF0il2pFYmLCucy6OZN5Wfrjr0bJpdhOYpIy%2FxR90%2FTff81jkzYYBuibIw0ZzKz4G8gcESG9lHLZinxpn5aBQBlYGVgD%2FPDow1f3RMacx0gu6v2s%2BjoiKr7bAgxCDafFXjI7ESUrX2PfzB3pmCnMQdjLv9i0%2Bc72HjQI7t%2BgEAINp6fb2rONA0OA%2BDZsxtzEu1oFFp6jS00UCuGy4GxCzg%2Fh10BjeB3MgU4CcjhOJYJyosKCyKKcdfszUD04qYQSIrcZGD0cqktIrfu0fKPfvsgy7aGiHRfRKJ2O%2FV1xAf1pDfTnvloEg9CZT%2FHVNgng26Exp9XnlmHleEFXOHjzpK90sNtv%2BAz07ddIIa%2FdJaUADDEhgZGXVtnyHQImkJrKP%2BibXQFcTN2x0er9WwQxzqStWESZhloXUV8DuzoFhc2eLT2336Wmpw6XAVx08ZbL7ar2Dg%2BUquCb4lyhb8gxauk3cslWfZItzxJ%2Ba7tbZcJrQdRWA7p%2BJ2hxSU0qJbaIW2SIhcv5E%2FJ8v76pQ4cZFk1fL8XpdAoc%2BV5mUb4fR1dQQ4pea4Bet7rTX288k29r9ssKUszmVHdSKiRIm6b3iOK1%2F%2BEIBVBjDIpPe8BjqkAcgY9vEq38AuQzAd5IL8ubDUWSTyB5i7i8rOqQCZ1tBxTa0ySGL6gy3nKNFRR7TUQuXIdmxmW8jeakB7fdlUXT0y0%2Fp2e5ywRkvVXOGkgMZ5RAgtHGJK3GtDoye8Vg%2F0%2FKpHra9oYYqFgCmO5CYuFYwKAbHAbcNYUz9YZVnRhUvus8Pqf2DE8HbwSLNPeffGxneyz3oNHsAO%2B%2FYX3T14df2ssrNY&X-Amz-Signature=2be0a08d54d6b0e2183c8e75572176900a4b00863a5335c3d7ca59b32669990c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHS5STSX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG5pigvNmxcpznkJDkWIXb903B4Z0O0SDUgvsL7oMbcCAiBNbqIe8TvS3thfU98tJ%2FH%2FEKq9WpvExjp1eGxvpPfhTCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwQmbkECZ6au0HTQWKtwDnLkNRoBFdeAYyjzP4X%2Bzzlof1SK9sGEUzdY%2BH0UyhXHhyxlf%2FHEj%2BKGOzDlBrHUG1F0PO%2B4JAtgyh75HoPkke1FIi94FvUl9EvkmmPH46HQZFwgYfE2ZiDh3xBUfIfy0lLO4FW4E4YVrBMuIsPeOQTbSk876cSNJr7TT5KlqRokgJzmgddKS4W2sPvS9tvOhZDcWE5TmltY6OgIW%2BWK%2FFzYOVYCPiTyxV%2Fxe0gbj4PRhrsWAri773nqXk4q5bbRGsuSh%2BP3gv8iC6%2FIrLHt4bTVHCArdjFwuJ4Ra7KselTCQ43ayAm8%2Bvl89tGXA%2FAZHSvOebVKH13VJm5hmEHV%2FIjMGZ6NDhx3OuY46clgo%2BN%2FezzqsgSshQu1%2FvHYQvgyMFfI2C10xPChAOpVpsaoy1YAtkWFIJr0mixZsAVgLrSKhCESvzSSYfQmX0fEfgSYdygyf%2Bq4sRnjcQiSmwOMUi3ImGfz%2BtYiCzsYLXBhO8cNUvvKG9UHLjlkhiebJWx9tTvBHx5zXuRf1%2Fxa%2BBJL9jxT0yioHzAdPu%2FEeMHLVkmVFq2KCtv66vfyN%2Fjh%2FC2xKfykbLqoiW8xtUJv%2BMEUVbKRQwYRXF8B0gJG5fJCZjUVjHI3532oZoU2ThbowqaT3vAY6pgEYQ0bi7g69Xxecn9Z3b0Oe5lF82XoLOc9XzafQ3BHLdRbUBejtPwzwtoa4pVe77zIzm9%2FxUWTnh%2FQyqtTPFwhoXYMVNrNVlDGR7Bp5zVjXmbNQ2EtPPZdVyJGWEAzmTvWCmnw5vlbHdgmORd13GOp0LFNZsO2vEuQyLQFcefSTpcO0%2B%2FGt9Fkkw2Lz8B5Tah9BoBchYyTLOlMIhycdAKceFM8DTnLR&X-Amz-Signature=fde14ac508d86e6aa1b31bc177bac71b577d996db26900f161e9708972b84bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHS5STSX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG5pigvNmxcpznkJDkWIXb903B4Z0O0SDUgvsL7oMbcCAiBNbqIe8TvS3thfU98tJ%2FH%2FEKq9WpvExjp1eGxvpPfhTCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwQmbkECZ6au0HTQWKtwDnLkNRoBFdeAYyjzP4X%2Bzzlof1SK9sGEUzdY%2BH0UyhXHhyxlf%2FHEj%2BKGOzDlBrHUG1F0PO%2B4JAtgyh75HoPkke1FIi94FvUl9EvkmmPH46HQZFwgYfE2ZiDh3xBUfIfy0lLO4FW4E4YVrBMuIsPeOQTbSk876cSNJr7TT5KlqRokgJzmgddKS4W2sPvS9tvOhZDcWE5TmltY6OgIW%2BWK%2FFzYOVYCPiTyxV%2Fxe0gbj4PRhrsWAri773nqXk4q5bbRGsuSh%2BP3gv8iC6%2FIrLHt4bTVHCArdjFwuJ4Ra7KselTCQ43ayAm8%2Bvl89tGXA%2FAZHSvOebVKH13VJm5hmEHV%2FIjMGZ6NDhx3OuY46clgo%2BN%2FezzqsgSshQu1%2FvHYQvgyMFfI2C10xPChAOpVpsaoy1YAtkWFIJr0mixZsAVgLrSKhCESvzSSYfQmX0fEfgSYdygyf%2Bq4sRnjcQiSmwOMUi3ImGfz%2BtYiCzsYLXBhO8cNUvvKG9UHLjlkhiebJWx9tTvBHx5zXuRf1%2Fxa%2BBJL9jxT0yioHzAdPu%2FEeMHLVkmVFq2KCtv66vfyN%2Fjh%2FC2xKfykbLqoiW8xtUJv%2BMEUVbKRQwYRXF8B0gJG5fJCZjUVjHI3532oZoU2ThbowqaT3vAY6pgEYQ0bi7g69Xxecn9Z3b0Oe5lF82XoLOc9XzafQ3BHLdRbUBejtPwzwtoa4pVe77zIzm9%2FxUWTnh%2FQyqtTPFwhoXYMVNrNVlDGR7Bp5zVjXmbNQ2EtPPZdVyJGWEAzmTvWCmnw5vlbHdgmORd13GOp0LFNZsO2vEuQyLQFcefSTpcO0%2B%2FGt9Fkkw2Lz8B5Tah9BoBchYyTLOlMIhycdAKceFM8DTnLR&X-Amz-Signature=be69ba5def7626482f56aef87e0d9cebf6b45c7d985972659cdc00d7e06d006d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
