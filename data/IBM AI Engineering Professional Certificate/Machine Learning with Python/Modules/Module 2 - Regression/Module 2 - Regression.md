

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=5f7c28c05b0c7628669e6065dafea2f1333b3d0c3ca620f474e1b88158e7f6b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=06d19922a2500a38245751b695518501815945bea9ca41d95ac5a3300993684d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=3dc33f58181128d0d51c55ebdf3cccd2cd888d0369b03d28a147148e0da244be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=c5fc85a922ed9c02f9e6ebdb545c58e517bbb35bda8197c602d070ff8e7ce495&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=b3daee9ca391f3fc2781cd384c572060e81ce9e2d686802b513b9a8806d6d7df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=af4130d08e343bda8f8df855f26cb946000e3296bbdb52b558b213ec9f35fccb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=54a9ab42e2126c7310e4f7931b517e4c2345be70fe9f42a4b4c8a7ac10c639b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBURPMXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9%2BgUrWGmiDLEOH%2Fk6TDMEnzrkF4tkk0MZUNIRld%2FN%2FAiBbOl%2FOG118cWRSwT4do3GJNVnrHj%2FzG1SmQYSfaiBX7Sr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMrw%2BpHF2a0h7MQfUbKtwD%2F18gUKzhLmrV4%2BqDYRt7vs7aUSjux5BRxrjCEFnKjE2YXcofNHRZMi1SEYVEz2giS4SQU6tqoYfLhqoNv4ImFwcdlraibBtfX1GM7BLDHbXjafg%2F428STpI%2Fr9pVDdVGva%2FfpTwH%2FK8Gtxxb1%2FbGeMcR7154%2FgfnL7f5wGLmDilBpiZfQbOZxphua7Qe2BMmEghvL5jE41WMVaMnzY8Ja3aDFC1a9vBhCu4gz2WS68DyDuVVbOl8XCVye9yNAdUAeT7OJOQzzQ13GwnAKzBhyD3jDLwHrXtE0r%2BJWhkB9cqRHfrUAaYJ7FxvnhjCwVGEmjygl5SANSRib1PIukbUwIZOiTF8QIaFFYt4wOSLZUU3vBJcv6ASfiy5SIVtFb7gm9A5E22nRnYyUqwBo9rGxxvE711fWPhylMhmCRXpoXBUP%2BggrtM0YfZI8N9iooFnkWbU308ki3OhjeO2raMLpYCVTd5nt4xV3cVJdUbs4RHf5AFT4nVH0I9B6qQ2rTSzuoVCyx2GQizWJFRqyDbzEDNMQoFFa6LECBWhNtdPUogsP4RgDdtJ7jv0KcjpDMzLXcJVX1dSENRjLtrstyhqGCGJmYnAaK%2FQ%2B2zfbueu7TvqSwdIcLIWwnUSVbsw7dKCvQY6pgHl6%2FcGb4O7Il2zdZ3FNakrjatamjEYBwF%2BqWvLfDmqyWLRzwf6%2BdHnod96isbZSnm5QYFQILPG5udY1WqBczvZkmz70ijuPWCMg7BFNILwEWONGJV3lyfXxpQ9CL1Zmu6MZ2RmRoM6mBQT4bSAV%2BHMDizyzSR%2Fs4qWlAY1VppJpRRyVPzMotPZFeUohMz7WKLZpWw7fyf7mRyrjP%2FTFG8V%2F1faoZkN&X-Amz-Signature=3fe0aafdfe9f7524b306703b7345f2b4c3946893b102ae4ee336c53a24c11b11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEKJMDYT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfSF%2BzCpQUOnH22HvNL1gm3BCTeArw%2FgOVhJcOQyPJDwIgfVjxUO%2F03ylcAaAf78xqnjccfyrxSP%2BBt4r9ONJl2Qoq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDBgFo9lb3MnrGWXrNyrcA5nYn%2B89XpOXr48YU%2Bg%2BCoQZpgDYzwtd1Ck5jxGzQk6wV0YHoGh0VgXiTrUxHCeSN13Y%2FKf3I6BOg99OrH9PD2OlRiNbzY7xL7ZyjFIgHYHnk53prGY%2BoBSfyHe%2Bj2J7ubPJuYCu8u1Sc%2BMJ5pzKtYNKBLYdQ6K5ecAiPRbk0IZjqQWfnJLZ8VOcModpNlY1KZf5tSwZ06q94BEQ5Gnzsfnono466o8VRhwP1ZM6DCXLEa4qizRukkTYvsnmsAjAGvE6ztC6bc%2FeZdCzLMC1Vmaz9SR2RUkiVF5Sj4w%2BSaEHnbt%2Bw5aUlUbtlyNuldZQ9P6fYzsaDBGeMhaJjtuXuqP2phZt%2BZxtnX4OE5mZJEUA5nKYc6x0rMunprV7t8PaLCDYxZgg1PnlTSu3f9q6aMoowMBtSfkHTvywWzrovBOadWj%2BIdWt5h9hIo%2F8Tb63O%2FqOZj1Co0979CeLMYzVqYZrUoKjJiTq0HQvtpXd7uuqsUfXjOzcuOgAMeiNrvSSFWjCv6vM%2FjrpY0tFk5Rz3Ap8Alie32fqNVexRiML4gghj4U26VQ3xtzjg8L66cJXBsBP%2BM2q1pmbnVd%2B1u8c1Zu3tDYpIQiSDDXm%2BGP7M9y091D6xfSJicbYjdakMO%2FSgr0GOqUBI5ABQTMhpaxreFK%2BmpW%2BlNemv7yZIk7ChkhvBTqU1uvESrhT1Nl7Cxji34D1dWXem6IFijgLI5c52XMDipdI9wRUxj7A01dQqrSnCiH7YVCjd7qSI6iZM%2FmKf4okblyDMsjYJilpi8jTSzJolYyyPfqkzMLGRBTdXf5NMK35REcPNxaKooxjq6bHbfBzxzTlx13UrJhNT7jpkVhQPbjTaNYq0Az2&X-Amz-Signature=df79ec3ab7c3c032f1faeb639e726cfa26f04fa8711d38899017d3eeeb33c2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3CQPUC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCULb50x9MCfCpG92X9DBb194s6rBzv%2FFw%2F5bSZwpsmBAIhAIFxAMjVXjJiAi7V2afCYeteHntAxqTACrw4IuqcMu9zKv8DCBQQABoMNjM3NDIzMTgzODA1IgxbzgTzhYEjyfTtQhEq3APR%2Fueu6L9pFgcFdL8dunVhD8%2FbNj9z%2FU10V4AQxPwRCRRTVVoPC%2BNEFGNRZmr5cpSyEciWHrZrf8JYN03QmWYHWMcXJZL%2BE3p2mWxoo7aymkIK6PqcaRkjHqsf35SiXRBVb2f22lO0wxPSdD9cY1QBlDkmkmJgOpjweqh6xkGXcoOZHubV81j%2BWnFCpXu04BytzmWzXjTrqJJfEcJCD6jhdtl5%2BX%2Bk5GistXL1Ra3oIbbRFgTC6IGBCuC5UG3DQGsnktvKF9%2F5%2FAFaauK5UY2hulIuSdKDQt7RIMZHsG%2Bh3HrDcehvYENGKnfOSU9f5PzsAHYXGUj%2F1gsF8va73zB8p2jwooH0bWp%2Fx9xKyTrba7%2F5eWrO4cjEzUeIzlHvRTOcix5sf8M7Hk0EqRKawqiigXXyw6Cm2JhOf%2FesqCK90PVmY7rrHyCuW048PBLFrBaPtmpQYKMUNLv%2BSq4ENZkIN9LO6knOAbgAfbLzGWM6n%2FAkKyzHHv21WLYpQ8gzLo%2BoMqA0Aky736mhwBPt8MYLU%2FhCwkHUEGf7b6m0s7L3PUCbxOOG3fGa2EBJZrDcQVRT4bZpdy9YCgVAJfEhD1CRSOvHYBWq%2B2trTv2ENCV7LU4gSRNILAPnk5TqITDh0oK9BjqkAZJiYf9E0Pb5Xxln8m%2B22ZpH37vrUEBb2bKHRJLoo2c9Ocz2Cc2Dd9t2DxxqIo6%2FOOH1F8hGjuHQ5HdLrE9JSDFp5SnsqAqclHcI7QO4cOnPyiAwczMo5CpXQ%2BvX0xSb7LGHi7gK7sO3zFKqsEK3%2Fu6DrZ8LiHpZGair5kjFT%2BSoO8NFD%2BxpbdVodR6BrG%2B98J0HcyRVyF9iydVnKCSgtre5RW43&X-Amz-Signature=af757055acc2b85e786cd92cba87199388279d7dc1e38f6b6e119d2df0f6559f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAL7ZCSY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3LsX72E3s4j6A0GwGmNUxGDQcCB9dZ%2FfPKL6hMqrsYAiBAaXjCeYhRPNe8BUbiKoIY7wQAhQ2%2Bu9HrROqG%2Fb5VFyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMSDA62QO%2FhAtK8urDKtwD8d08AsYRFjFKGKV0iD8wj4ziT2t2YCi2fSCmWDaegCFTdGkWAca9MXBzmSUqMVccGhq%2Bi8JfFaddVmtLvyOvQKIMc%2FUKfIwIPKmKt25x7kBhko4Q1rgmqcMdya7dO3PH0buKbi%2BRFKBANxLInPN78Dr42%2FlVTNjfjjw7Ob91QCnTXxorCH8BjOum8krtHEcMP574QuRlFeK4Yi5sPFRaAfmlYngUf%2Bhm5ajjFemt9%2B%2Bv4Tf%2BpTbeD7nHBbd4Bow6i4yIn4mA2OJ0QHNE7jaU2TAQ4XGd2J%2Fyyc327HXYyRC0sCBLi04oKDj%2Fx9XqeJKRXHG8O8%2FilU1Bc6cvUL%2F9vzIKWQ0%2FSvlCN7w%2FB3Pl0H7f%2BaOxgLUTheEm5Rf4DtuhKtiNuPVqGqnMBfdabVjYfzvmJGzR9rDG%2FxF13KxVwDaCEmrMH5hRGdr6edlbRjS6CiP1ntcbcxW%2FQAWGdOG0ijCJ4RUNBocfMkhXQSNP%2BXWzn4AonvChDmY5Tl8cUsHpmfjHI%2B%2FI6Ag%2BUE%2FMg95HtNH3XUxQVszU6lMEkCfgk3cU5YzBR%2Fk85KnR1QeS5zdiO3StPasa6FQLPTXiCSqdG58cHlVfIlYgM9VQbr9Jh%2FhnWfiB%2BrTMWytoA4sw4tKCvQY6pgEIQet5shpqbMxAPPrVbf6INRdflsXEx8p09%2FoR%2BIzGYzRB5CF0G4Z72otTkgtyTUqroBR5ac9ombAycyOY3SN7TWq4gFvlL5zS3TSTHQ8wELW677qsiqil3khprxK7sl1M4FvN8ZU5mqMVJVwaoZw%2FSXXfQTtdxr9MWAAO2SL5bRBE5sy%2F8uKDQKsME4LUm%2FuVt4Zbx9%2FoICDEYeo7fX7YV2y8XQY1&X-Amz-Signature=7991b0e638c8b0594c4c36d79020fd57a6982ba3cba772807d47e4ba105f5f9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAL7ZCSY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3LsX72E3s4j6A0GwGmNUxGDQcCB9dZ%2FfPKL6hMqrsYAiBAaXjCeYhRPNe8BUbiKoIY7wQAhQ2%2Bu9HrROqG%2Fb5VFyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMSDA62QO%2FhAtK8urDKtwD8d08AsYRFjFKGKV0iD8wj4ziT2t2YCi2fSCmWDaegCFTdGkWAca9MXBzmSUqMVccGhq%2Bi8JfFaddVmtLvyOvQKIMc%2FUKfIwIPKmKt25x7kBhko4Q1rgmqcMdya7dO3PH0buKbi%2BRFKBANxLInPN78Dr42%2FlVTNjfjjw7Ob91QCnTXxorCH8BjOum8krtHEcMP574QuRlFeK4Yi5sPFRaAfmlYngUf%2Bhm5ajjFemt9%2B%2Bv4Tf%2BpTbeD7nHBbd4Bow6i4yIn4mA2OJ0QHNE7jaU2TAQ4XGd2J%2Fyyc327HXYyRC0sCBLi04oKDj%2Fx9XqeJKRXHG8O8%2FilU1Bc6cvUL%2F9vzIKWQ0%2FSvlCN7w%2FB3Pl0H7f%2BaOxgLUTheEm5Rf4DtuhKtiNuPVqGqnMBfdabVjYfzvmJGzR9rDG%2FxF13KxVwDaCEmrMH5hRGdr6edlbRjS6CiP1ntcbcxW%2FQAWGdOG0ijCJ4RUNBocfMkhXQSNP%2BXWzn4AonvChDmY5Tl8cUsHpmfjHI%2B%2FI6Ag%2BUE%2FMg95HtNH3XUxQVszU6lMEkCfgk3cU5YzBR%2Fk85KnR1QeS5zdiO3StPasa6FQLPTXiCSqdG58cHlVfIlYgM9VQbr9Jh%2FhnWfiB%2BrTMWytoA4sw4tKCvQY6pgEIQet5shpqbMxAPPrVbf6INRdflsXEx8p09%2FoR%2BIzGYzRB5CF0G4Z72otTkgtyTUqroBR5ac9ombAycyOY3SN7TWq4gFvlL5zS3TSTHQ8wELW677qsiqil3khprxK7sl1M4FvN8ZU5mqMVJVwaoZw%2FSXXfQTtdxr9MWAAO2SL5bRBE5sy%2F8uKDQKsME4LUm%2FuVt4Zbx9%2FoICDEYeo7fX7YV2y8XQY1&X-Amz-Signature=7685278b4a4332c6d1668521d44c74664fe621a440298cb5bfe43ed1dde4a500&X-Amz-SignedHeaders=host&x-id=GetObject)
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
