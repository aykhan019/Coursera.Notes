

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=b2c2e268568e1d71a431970abc2bb7abd54ff4d125a1c7fa7a6231a62e855c23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=c7f3b1088e53b41c1b0a4aed9cbf45902b1b36342973a753a6a0633592591c4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=18f4ab60776f5a08e02c0442ad0febedad2428a47d45790b425a716602aa1fe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=fed01af1c929550d857b71dce10e9b62598c1e85d349e8d6a9ad40af5617f09f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=c84c63aa4fdf59d146b9ba35a8382a7e0139f2b34debc567de939b369c790a0b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=e44708998cab5c5da18e587258e27724e8a7e54e73d17920280bc1fdf8736051&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=d6a3e4dae2321131f132ed7d62ac0d8f864dcf1546a1673a0d106ff1cef3bd2d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHIRPVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVf7c9jMOlHSwbguow%2FXvZNFp79hail2iZxcUFUJbkEAIgdTJi7b0UhLx6NhvCsIDl%2B8s5Pbkj%2FQpGr%2FyxsXFHE%2F8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEp6wiUNg1r7hXq8SrcA7yyiIfJYTAY8EsaArHu1RNVNTfEk2UDjgDQnLwvAUu%2B8GIux8E5arlTCNI42Ox5qKaTDdD06DDCUuK5V1PnRYkIKpT3YAbeFrx2zoVkRIh1lrvdlcFlf5pujt0A7B1OvHU5tLT7%2BO2VrDZvRDw4OBeNvgNhZnvksyT94EPT6Qi85b4EVe3P7kuj4f%2BphR5H3X%2FXGT4M5aWUVh8NgdnASqbvjqjvMKxShBtfmdOC0J%2Bw%2BlSWCjKWB0ori7Mx2nbIGd%2FqaglZyVAWQh%2BcY5KMYfuTUdwlsdJMTMD4I6z%2FL8BCmzASliPgkWFFgWbu3Jv9FM5Xdl4cQAJ4hstcVMDGPQzdIexaZhwZ9pQgKVZoM2BpnJnvfWqMnrqXgBdyrx9s5deCsUr9taFxpqKPKtviDydwaV7UTF5%2BgwNZQx76yfT83bp2dP1lUciZGOuiXksbzeHzOMnrvD4NoclAP6Nl1Bm9SO7YcXU5n1g5IIZWqXcHY4UHyupkITcbMXL%2FiOl1moz8HY8zq2HkG0X9TAVcK1NdEoT1gorZByeihWBe5Cctg5IEk0ov0XbfWvg4WNDW8XOQfCKDqVJr6DRUaVvugW%2B8knJsGNk3MwW2Kdn8EJBF6QgnfCo3kPUWyyfxMJnQ8LwGOqUBijlHGcyDmh6EOKY%2FV3gu45bdG83twz4txRrmsTEiwHGa3d7OsOi3zjUjV9wKlP9MjAF31cDnorQTQT5NVPkx6EoonziZVhlhL0lx99ZJtJvXU6MAGLVnDyJ8NOtxIIlBw84nZMI%2FjCNmfpBxQDzcmdwU6jEZUZJUUz1gBywxDLIC8rLDoonK%2BzthBdZsx76CX2xHmbK8AjscH0qnBV9JXa6aN%2BFO&X-Amz-Signature=4c6bbe1499d3857453798b8077ac06328e2a69602a327037d8c57a4e1a684a9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIES5J2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnl72%2Bo8or0vL151MMaIp0pjsgJHzi%2BfbVnb9EYJHCoAiEA5OE24p5iAkJy03Kc98MEXjcHjDEBE2L%2F8mKi5Gu85L0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLfTQ3igDXwWQj8LCSrcA8Y2GGCwvQNuIVcoQ8lSoftGMzesztTVQvKjkOwGj1eiRd4u0XEtisLWAfcKa7GlzmcvPS%2BOjOk%2FsxVxq8IOCr55KB8E5XAbv0kaPWy1omLPDUvM%2B1OFgaZ6xxrXE3Bh8pR2WbEaEbr56RhSUW%2FbEnVMOVretgav4Wo7A04fwF90au4pxWzrBXdERCkxr5PtM1h%2FieHmswYkb5tzcslaCAFCv7u47nhTluDZm6aJazZj9U9JgPTFITeNozDHwT4oD5ls%2B5iVHSd3Cp3gEjQqKjhMtu9HLf0qDCVjVIUCu8b1LFJL3n4mK6%2FKY4aKgy0eI%2BBzKHAEH0yVO%2FBZC111AwURFpvipGK9kOCzK7whE0mBeb4Fb%2FoAhSNWOaTyPpvFwW0GMEEk%2FhKe76TnhUUlpzn79UUilgzV9qNVlP8vHcmUKA3%2FHYRjd08b43UXK2ZLkNsQTamwClkmIW1iCVKZ6GWV%2FVAydhMF9UpnmQuwUAp%2F809%2BUrll%2BFUUVdbpi1LCVBQ26%2BtvWqOZmnnnoRzqXBrOcoN%2FyqZdyR5zQTR3jMBX6skSUGOI9GPcTsoyqUOd4TT%2B6EnKDY5i0411KJ0f0zu3k%2F%2FIdzjEFzxeUoJfV6W3eHh82XradobX0K6YMK3Q8LwGOqUB%2BLokaxGCoLS2sCaYjyctod7Ggj7v5O0ckJAkf1l53xkUPrxCABg0olthYJTE2jFS0BlagbhPrMVdB8rmxnvjcacOKbevDhz6C7eTY4nX9H00Mw7ihmgGpNu8lnQdRGLltB6%2FbQhUvD%2F%2BHODiQi59ttmRbISHHNJv4C6G07NzpMkyvT3Xrl1CX5TA87DC%2B7oqydSlyI2sDTR9KzXd0CgeJ2%2BrO0Ue&X-Amz-Signature=b1eb2c8e4059427f74bc2ead27a03b02955f2347bbe40f238d78a03525ebfd7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYPS4Z3O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbGIuIeE48%2BhwReMr4Kj9qVehZLNol7%2Bfy2AJqoFkyOAiBNpBTi5eTgwoRSmG0h10j%2B0QFpr7bWDrFDhJEfxn7cwSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNLacFFrh%2BuEcRq7UKtwDtK2n8gXb2crNKB%2BazAI%2B2hJ2qeREpygHFcaUF5R%2FTaawvBxAws5d1T%2BbUqwlp%2BN%2F0WhwWFzaNrVjE6L4ZdvSXfUdHUyypnFtaB2iALoh31EwXZb4rgytjCHiqHKE%2Bny0uFgD%2FOum2%2BXLvQBmamXI1kxjz7x73Q3RQoL3YmSAIOvj3G8J6KN%2FEDv1h54gtbJXeK6CczGRxxwWIeyPhM6QdDREb5aX%2F%2Bt3wp7XtU7EMjVWRoWuAkOu9PUhxNS4Nuo1HbuLtWhXYy6f5O%2BwTc%2Boz4NT7DGxK14qST2hwYz1IwQFrWxpLVH7pgBaHLvIC9rSiD2vW43a3IxNgswddWy62waXVCZ5lfLLTEFJualLGxF5q%2FXNRW2ftVaIzMd%2BUZBKXmiH%2Bs3LDQCTVXoEL26p0s%2F25lvJWTsOxyPIHiCl5BRycJTmeE9yflJ9L3MJfNNETdbAvcwoNuQlnzjLJlb%2BG6EhEXS9P326I%2BhmuYQnNyJJ2KLHetzbSQOazh%2BUmJ2gU4Q%2Bch3IUj01dyM2YFV%2B89d5WmDgrIyiwRusGm%2FiXAee8vOzFjsjB1ybXlLJmuZsDL4BM0zel0oQq5KDbxOPo4Z01HAChpdTKm%2FJRkJ68XXpx3LB2qgF%2Fog9XbEwn9DwvAY6pgHNSrogxB1cydO1XPPKt%2Fr5ezgHWPubarSDlDvHOwYFyBfo9NGRRwC7AtKp6tEuo1J2hkSOmHJTNTwm7XNwtnA2UjdVr%2Bdc7qGh%2B1gSMnTmcJuhu7x2cMlY2lkqiP4gYuyyjma2TnjGedsWf%2Fxxvm274YgWH0NKYx7mAmB3I%2FCjsB1Z%2BW8wBa1bkqjxss27ozYV3dxL7iifwwIl5Ll7%2FAnkkb0aPx3G&X-Amz-Signature=e35613270873d757088e47161dffad24e6f9526ac5c461939a2a23ce826bfc52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RARWA3Q6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZHmPA1QdG3FegsJWfqoPFA5l4Pvv5YliB2D2GSVW%2F%2BAiAxUEpjJcPSSr5ZpHDgs0CpxCwpq2a0PpKVFcEtAei3aiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeF8MmAKHirtU1QO1KtwD8RNE5fyZqzr6gbcTExro3GNQ7%2FvW4u64iyAKYFgrAGUjQN0YAqJu%2Fap3L4dD8JueynM5YTy0uqQD3Ac2niWJ4lVllDT2Ur1nFny5pzMfkCCZ0ApXi7IIMIige9%2Fh5pNAnSDe%2B%2F7jEPhVVqZ8ofBpDGSiTRiP4vIcdpC0j2cLX3%2B27rSv8rj4EWsvyI47fi0PsA1qs%2BQ3rVbJ%2Bfje63El%2FZOv5AHfy7neFyHSDwEEbVi98bohfmsBB49%2FZT2w%2FiFEFZUgv2clKHMxqPyuzCQcDwXlhroKyoMGuejkVxqlwA4D3%2Bq%2F79yOvkFhfTBYVNZG7WvmtKkgQIm%2BArHC7e2RYFDHYyME9IvXzJOb307tINZBWJvtwc15Fi4%2F8RJersKM33j63pOZxoBtiEeEasCj%2FfGvqjirsN2PuTaTEPSBLJI4EHWjVt9GPdc0OfGsO8aRhpUbe3eU0WOx%2B13hm3l9c4uiBq0QHx6RM9I49BprWxrI6%2FJet64dYmwdLCCzqqRZTJzGdXEGI6FE3cKFHo1T8C9IuG1JMOlDxPy8k5lIIkLLMkGcRNMsjIMjJhq7KwBPFO6sGx4Q%2FMxP9Cr1Urym1gra4SPTCciHNFbHDgMsO1qzPxKiBeHzNMPtTTcwudDwvAY6pgGKeBzi8cUNzUDnUV87zyVFuflmq2DhTB8YdfSirD7s7uM%2BZVPskkoRZ5GvunZ8X4Q0t4EoaTzhmc8TiAhE5qzv1x1nLKEOHrOXhFRHzoOZcGTPke1d4jkYGS9bHEDMkgepIr0pbGvnczSlRwRPgUVdpXi119y7ngp%2BQGfp%2BNMdEyggIqFT7C46A00k2X5aQAAOFbVUT0c37vPI%2FjUgjhfomCGDiw7A&X-Amz-Signature=4dcc8a641eef0173acbd95bf20fcb2177857e9a3546e64254248671776cb8830&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RARWA3Q6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZHmPA1QdG3FegsJWfqoPFA5l4Pvv5YliB2D2GSVW%2F%2BAiAxUEpjJcPSSr5ZpHDgs0CpxCwpq2a0PpKVFcEtAei3aiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeF8MmAKHirtU1QO1KtwD8RNE5fyZqzr6gbcTExro3GNQ7%2FvW4u64iyAKYFgrAGUjQN0YAqJu%2Fap3L4dD8JueynM5YTy0uqQD3Ac2niWJ4lVllDT2Ur1nFny5pzMfkCCZ0ApXi7IIMIige9%2Fh5pNAnSDe%2B%2F7jEPhVVqZ8ofBpDGSiTRiP4vIcdpC0j2cLX3%2B27rSv8rj4EWsvyI47fi0PsA1qs%2BQ3rVbJ%2Bfje63El%2FZOv5AHfy7neFyHSDwEEbVi98bohfmsBB49%2FZT2w%2FiFEFZUgv2clKHMxqPyuzCQcDwXlhroKyoMGuejkVxqlwA4D3%2Bq%2F79yOvkFhfTBYVNZG7WvmtKkgQIm%2BArHC7e2RYFDHYyME9IvXzJOb307tINZBWJvtwc15Fi4%2F8RJersKM33j63pOZxoBtiEeEasCj%2FfGvqjirsN2PuTaTEPSBLJI4EHWjVt9GPdc0OfGsO8aRhpUbe3eU0WOx%2B13hm3l9c4uiBq0QHx6RM9I49BprWxrI6%2FJet64dYmwdLCCzqqRZTJzGdXEGI6FE3cKFHo1T8C9IuG1JMOlDxPy8k5lIIkLLMkGcRNMsjIMjJhq7KwBPFO6sGx4Q%2FMxP9Cr1Urym1gra4SPTCciHNFbHDgMsO1qzPxKiBeHzNMPtTTcwudDwvAY6pgGKeBzi8cUNzUDnUV87zyVFuflmq2DhTB8YdfSirD7s7uM%2BZVPskkoRZ5GvunZ8X4Q0t4EoaTzhmc8TiAhE5qzv1x1nLKEOHrOXhFRHzoOZcGTPke1d4jkYGS9bHEDMkgepIr0pbGvnczSlRwRPgUVdpXi119y7ngp%2BQGfp%2BNMdEyggIqFT7C46A00k2X5aQAAOFbVUT0c37vPI%2FjUgjhfomCGDiw7A&X-Amz-Signature=d3d7272e1f6c45f4cecc77b2b42a5754a967ccc9785991a058ba629238a44709&X-Amz-SignedHeaders=host&x-id=GetObject)
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
