

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=565adc2e38bcec5da2f505e976924fb2678d44310fa46718dca033fb742fac30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=196d9dce901c30b7867ab65d82bb7c22df0d08abe59b9a9f15a275b79bf45535&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=04a3b2c46b6f2ff4e15fea289d91bdc0694f9f6bf037b418687d8b1dde141f6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=a45e66cd655c0804cb8e4efb05a8c35b4fa6065778aca2540478198b15cb7282&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=0794e42e5b041a3d7826d6e5b3ef87580d21e713a6151e07d8e58255c07131e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=b546a5c0b69565ae9bd2c5cea63a36f70e2df1edfbcc4b4ac43ea0fd41409a28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=4bc52b78edd3512dfa585954bba9e74efad60ff639fba9e98ab11691df272ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPKXG5U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBJfIRGFyJNlpCJW7nK%2FZxIvBJC7c70A1BBemEP7A%2Bm2AiEAo6oRreKwTqeLr8GMk1EGZptZ4K6xsww6B%2FlWbzF7VScq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM2XnSzQ%2F%2F6hZ6JeWCrcAztwGDrmpHcR5h8MZGtws81cP6uCl0LrbPzjTdP3n7Shsn62NWKA34dlzmUmK8H9WwSACVQ0c5Mu%2BafeGxMfmXRpkF%2BTTowBmFhOJUB8gZ%2F5ER3hsOeLuxP%2BwyM6D20KxbKbRM9n7Yl3I3IqgWdkdRQxbZQcXL02Bsr45b9Fd4yQGPAb2GVZfKPeFsTlEZzcBIL2LFOEQbdDzkvDo4O2ByfEkxp30Ak1UveKiFrrXmNtYxHuf4QzCJnb39uKbQaY8BCaO0j0OtaMfLsr52UjFYXv1%2BhMPPugPQxDwfxNMCQ1O0JCFKBLfBg0iMUqiSlclaFnf12hYgakx5Kd9VJTVuPA4Yc%2F%2FXCyk9dcKIf%2BAfVa9Er0NvQY5bJ2JAn7PPP9LR9VSf9rMo1ZuGsmOj700Cr9gA42QONcxdsKqkmlJC%2BQ4ACtH%2FNKy%2BxdDbpBTwgS5wwna4XJReEqnRF%2F3FhpD6CJ5XQrmoGGrKzmsnjgdZXTQ0639IxOaHp60N%2FHt4%2BPmxWnKYeJl1u561mcpZlwIgmSsJvxdr4wGkbFuFTY9jVptdpwiRrszp3YaQSePa4oelQNEkqf4vTpxpOvgTNvrfQxrNKj3bLdRmi085Rd8UtkDnC4ljqPfAWILBFKMKjKg70GOqUB%2BN4z%2BvJnLMSxfGiVrxhoGz40MqNMH9cKMih0z09elbvrBXeaHngoyYQ5r4gyLejuw0NOX1s4z9WTtbqyzWU7%2B9q5zNOHkgwvgeUNw6IjoTJsK4ptl1%2FTeICwTjoIuX%2Fd1Ub%2FHA%2FVzMZWBngkQ8kKJ%2FNEcL19FgEN%2F%2BuT6a1UIEMsXHmN3VqhVcCFR5CrTfrfcXJTSNYIGFmS8IFoRaDRHLFm2RRi&X-Amz-Signature=1719d30305cc54ad5edd904faab8c0979ca9917a42e7286c9a298c2b1d979968&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHPWUKJO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIEz23veiZM1Zn6B%2F9q4ABbBvUon7P1Vg%2FDFI9Ag%2BcAoVAiEA6S52wXMbCgWfv4OPbVkeTKcOVF1Tt7B86AqX89T9q60q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDBxQtrzU9r3Fpeib0SrcA1ZjSxxdtRoRS6irOqREkGNhcl%2BLEUXUsi19HsXct8mayVVUg6Tqwuf5b5oiU%2FuAa1G9ls6%2FEEUAfcasYRq4grM57ErJnAsvW7HN%2FAgwZyQEc02TeFCJhuijaugmhmNcQTh0%2By8PMvQje1SdTV0Lil173VWvnKc2qpBOiBTpfZpI9Vo4kMQVl9bCIjqaYyon45ANO1zemUWpNIj0VGqwtblov1X3ujlCmELOCnrJoUdWSqMuGlkeRC3asAtafPhRQSKKEVNXcUb13Cw%2B6IfwH0mp2DBqqc%2FUe1JpphZDuGTKho5yTEMAaTh2o7ViOtuaNlouy13SsUODwAvr5hbh0qKnt5hFd5jdCJalpBpFBWA3qh%2FVRRg060NqDNY64lwWxg6qFsUGOINjaH4G8FXHlsRihTvsfkqYfiBib7toVMoCfpfv%2Bnm9Pav1AHk9s5rUjOFbrV453p6kQC2IfoY8WSxx8gepaQlUvdDK%2BIt1Tmwa%2BFGHY62SD%2B2uYQ501xru3i8t1TFjqVjv%2BFEW79Zd25nZSIxQPHKIOk0A%2Fch9Qo3rwiaWVPjOWxzkGxR%2B9AYcWclBuzMSa0eMDFwW8J9ZgjUKvJfd%2BfHDp6OxCe9qLYiW7%2B0Qwi6BkUwev3WYMKbKg70GOqUBy9MfEnkswrXDymVscWq53fnNTvcWPojXoADtypb1M37dNAmAGXbD7bTUIO082kQVxH%2BWKGM0iuu0wyEDKOE4BcRwYz03k7N%2B72UgRjpkOLP2KozFNq4WfytO9VhYDok1StARJKb4HA9Jw8htUHRN3PW84Ty1hVMT8AfLrl7FoxO88idlfTOQb%2Bufa4y59DlIwlS5183ErhANPRxzMeL%2FLi1q9BjU&X-Amz-Signature=1f9d0ea265e827ba318188ed4751f4342d82afcae915341c410cf70157a6ef5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V2FHHSD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQDTWFWFXtDBbMPR2XDqtMBNZuzQ4yz3ChqBhbTIAsxLjwIhAIR%2BD17MKed5yQp%2FAZGJyV02Nuqn%2Fu%2FYfjYVnrAN0k2RKv8DCBkQABoMNjM3NDIzMTgzODA1IgzCEdV%2BEMQKk7VTsyAq3AOTckCdtdMvgwpxF8vWHuvic9RS7eUG9F77KYEm%2Bsr7ENLwmb6Pu1YBfmOX%2FTncBbNpmDmeabD%2BP0H6VmPGIaSPUqBaK3iLV1O8%2BCp1liLZJ4bvLon5%2FSb21tOtQ1IHFTc1EhDYqjetJ%2Bf8dwuUX38Y7RURefVYJjgIWPCS9orKhGjvifaOq4kNVntCc%2F7kdFTihuL88aZ1reBccwBwyOhGE%2FtSvdJc16dDI48Rx%2F%2B9lPcgrBlTbYfHE5zCzsyCj6EZ%2F0rFoRLSWyaFj8h6zANR7zA2j7a%2FUHWp7lHes42dpefAyKxnVvflX55qbG8eJYbkGEdx7YsryqPfVHhwIvHTYZ4yTkj6wVK9hS7TVWGiAbKxReVo7Z4ZldXAPqdV08D%2Bdy3UTWAoSAH%2By4YEuhsJDodTYPpkoLo%2BU9Il2lPrQ02FugpRUMURMg6h84tcG6Exha%2BQeXFmSSbDSiIMbEViFJNv8XKrzvqTq%2BfSYX6ZWDp87LPgZBw6%2F632UmqP9zyKpLnIyxAyxNe0SN3nxWccXdSF7SZ0C5Y4kdQza6u%2BtwjsyiWvojqspCyDZKMprOXcvUeggmy9xcWmI13IoR4d3UzUkXfhDLZY%2BpOqSB1Z08SV89BqE2iJpdjmwDChyoO9BjqkAZPUGKBb3BNUZMDnoQz8hiPrcVJJssB8DYGrnyAbLYSgS1hBANLrhDskJXgve0gUQrD3P8RRJ6EU8dE%2BJKVVkX7YC7kF69SXljvdNjT2MLVYXXx3sOnasYica%2FPmYj0bFQbIC9L0L3NSrS%2FwZmu5tIMf3%2F96%2Bwp0JfX8UKeQuJiPmlN8Mt25GAWQ%2BDkfkruZEI2WXpnCsm8ckp%2FHjVb7gmkvPiX4&X-Amz-Signature=ec729e292412524eb609ccd021371e68e6e178a6f6dea7d5d3ac449d8882a682&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNBOARAA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIHbqFuZpH15K3u38gD1LMvMjbeTVo5zztXR2BXk2xxCTAiEAkL1cuCK2OjZEPTmo7UXj5wfdgVwSu6x7K7onlkR7qJ8q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDOaLAZoB3WDnb%2B4PmCrcAzrebDOvKbEXVA5SN3vQJe7K4amdwm%2BmYfbxmoNCpFKJkzTZH%2BmjAADUaUIVmZU03Q6hzeZMBTmL0UcTA%2FXHpTPFAFk7mWULMxfRMHby%2F4178QBQJeWlfaTsEBxK%2BCo2QXAyUNl68UUffmtJTkP4AhU9q8NYPozPaVY5YJZ1KA0ozUnHUY%2FJBCySFJXZsJM8VM1srIybIBjPtJJTt2UvekbYdECx2HS4EylDS5tlnYP%2BwTyO5FL2D4MK0jDMOjLYhh5oqHJRtvr1LY%2F%2FcpO5jgK6zgz3TpB2XgcuwmVAmwlKPHr9J89tsaQF%2Fw2uCcGtm4Bl2P0RqzMgSCUJaOwp5UoPHs%2Bm7gLLXWNvmdqfb1G0KLsOAYkg9mysxJfDzyeZ2UgJ%2FitFEyGAnrzyqMVScDjoUnl2Io8dSVOPGU9x3sRiRg%2FU9cZHc9TlIY1kZGU9fGaWX2DHX2S4CFlVdcQ6BOns%2FRMBTW7CZLGgPPfajiUpb92FwWTALzrba9Dk13xjI3nYTsHkpATFGVThKPhnoGqTVqwvmyg0dRFSXygATXL246lpgkikoaC5WUyYvIWIedmtRHYt%2B2riGVcXxUwK1Bp25xxNW8Iw2XrbA7oyBCVWLPib%2F5%2FFTOcaX77%2FMOHKg70GOqUByat3VslCXM72fl1Kj38qVlF9N8N76DLK3Jke9lI2d2xmzGPCyzvx27qn%2BnzrJcboMh%2B8lsKEUu0eKkEUMBuHuUszpQtn7gTvgaLmo9Th%2BYKTtO%2F5lFecdOUF9v%2BFh7n%2BQDN%2Ba88KrbsFYiWVk8R4qb0etTmvRtIYtCLA81JbBNIB%2FLAO0nzLMJ904yFHIKorVUl5FipxpdZEVPARfYiyP1kJBzhP&X-Amz-Signature=6c22b601c71f686445dd1f1eb4bbe010bbc62d081f38cc8350ef63aa8ba83709&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNBOARAA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIHbqFuZpH15K3u38gD1LMvMjbeTVo5zztXR2BXk2xxCTAiEAkL1cuCK2OjZEPTmo7UXj5wfdgVwSu6x7K7onlkR7qJ8q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDOaLAZoB3WDnb%2B4PmCrcAzrebDOvKbEXVA5SN3vQJe7K4amdwm%2BmYfbxmoNCpFKJkzTZH%2BmjAADUaUIVmZU03Q6hzeZMBTmL0UcTA%2FXHpTPFAFk7mWULMxfRMHby%2F4178QBQJeWlfaTsEBxK%2BCo2QXAyUNl68UUffmtJTkP4AhU9q8NYPozPaVY5YJZ1KA0ozUnHUY%2FJBCySFJXZsJM8VM1srIybIBjPtJJTt2UvekbYdECx2HS4EylDS5tlnYP%2BwTyO5FL2D4MK0jDMOjLYhh5oqHJRtvr1LY%2F%2FcpO5jgK6zgz3TpB2XgcuwmVAmwlKPHr9J89tsaQF%2Fw2uCcGtm4Bl2P0RqzMgSCUJaOwp5UoPHs%2Bm7gLLXWNvmdqfb1G0KLsOAYkg9mysxJfDzyeZ2UgJ%2FitFEyGAnrzyqMVScDjoUnl2Io8dSVOPGU9x3sRiRg%2FU9cZHc9TlIY1kZGU9fGaWX2DHX2S4CFlVdcQ6BOns%2FRMBTW7CZLGgPPfajiUpb92FwWTALzrba9Dk13xjI3nYTsHkpATFGVThKPhnoGqTVqwvmyg0dRFSXygATXL246lpgkikoaC5WUyYvIWIedmtRHYt%2B2riGVcXxUwK1Bp25xxNW8Iw2XrbA7oyBCVWLPib%2F5%2FFTOcaX77%2FMOHKg70GOqUByat3VslCXM72fl1Kj38qVlF9N8N76DLK3Jke9lI2d2xmzGPCyzvx27qn%2BnzrJcboMh%2B8lsKEUu0eKkEUMBuHuUszpQtn7gTvgaLmo9Th%2BYKTtO%2F5lFecdOUF9v%2BFh7n%2BQDN%2Ba88KrbsFYiWVk8R4qb0etTmvRtIYtCLA81JbBNIB%2FLAO0nzLMJ904yFHIKorVUl5FipxpdZEVPARfYiyP1kJBzhP&X-Amz-Signature=0ea5d2cf4d5d16825ca8de6bd843ee89a1de73c84dbfcd1f0254f88f603eeb4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
