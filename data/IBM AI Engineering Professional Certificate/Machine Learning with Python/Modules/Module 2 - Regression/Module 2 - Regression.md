

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=6bc6b6b37bc880af1151e2811cac944cbe9ab8033f3770318f422625955b8c74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=9cc4cbe82f00beb5c275b7561b5f35ba113057ba0af1c797893451fc09895900&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=ec09b6045e521403ff53566ff3ea30dbc7e9992ff1aea6ac076ea0ca962c74b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=13934f6ede6b4bc9f556d351cc9a6ac556f46b031d77e77c845e22a54e41e21b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=40a60adff717a5de618d15bf153b17c1a6e80414e56220237017037aba80b8ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=e5359257c7186ec8132f4b2b4d48407174ee78b16696b3fb9c88a0ea0d75a1c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=e3d394a0a6ff0b91bbda5cfda9b8f3c5a0164dbf6bbc2122ae28320eba2dd881&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPY5N2O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwnmBQQzgyIfzT0OB%2BnbKKhCDozAtSodMikIkCQoFFAiEA9PwO8sURr5aQ6rHgJqQArgYhgL%2BVsTMJeNJpopOJkvwqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlzQ3Y%2F4K5M85vCWircA1Sv3Fjg4%2BU6t4R%2FBIvJZJcwxGFE5EJ%2Bg9JmwWLapBSKFWaZ%2Fb5tZpf4wqpIZFRtuhwA6wJ5jQo%2F5Qd90xrHTgEb0OmzOoT69%2ByC%2Bd1y2kaMmaWhtlWs3HcwUQqTco466s5ujsLXjG8ddENBgXUK9s5u4JVeJpuLUUwYg7pTtImqfcFVSsPRzfuBxYxtcaSIYlOPzVo3BtRxMLxDgYlH%2FtwtbMKqO2HJlLAmDRTvErqgSsxatwQwoK9LlxYoZCm%2FvqfX7BTVmSXrTRmIwsllrPrg%2FllkXu8Wl48pMkDIzBVa5LoLANi2luxY8ryvRCwv7bH8s%2FnFc4oiTna1D3EIhivrRVSgzE5hGGjjgs%2B3r1jM5arwXgC9Kq1kBNdaLmAIwoHTM3tPvrT1Z%2FUPi5sOjdUkxG4130jOfl30B%2Fm3%2FshMxgy%2FsXPkyaAlpNg%2F%2BuzCNlwrItLzhnnwCNsQnivfyC95AZms2Rfh%2Fwp%2FmSQLAeGw%2F0fl7YujFmSMdA3O99w8T50uUe4K0TMFoN71EGfuLNMBIGoernBQfHB0i8GWMQTiT8W420ca9lrDYjaLDnfP%2FPw1qIK2MBebOMhyGyQHe07kUtn8tYPcKq3Trb0w7SILvEzAw2nsb%2F1rLLWrMKzo%2BLwGOqUBYXxzt1P8BlppzrVQNSQNjvfqKBBnO%2FV2F%2B3rs0flc7Ho0eL44sRYH%2Bry8A6blec7JjWMic%2FGVAH4m0tcQErh%2FsyYLZh5Q4p4YfYSDnef0r3NJ2jg8%2FKU4ToWLTkN9lV2AKVa343sS%2BDjI%2F%2FPmfZNFx5glhpLsYS46VyUn8yusRzyOqsPKUtqp6mMHUCs78IlPe3DnGHGh308GRGoebfK3WLvVn90&X-Amz-Signature=8e1820c1b9c613c5f504aa40920a2d673a5cc1f29f5ec3416f567c00bda9dd59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYD5C2WM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkXccC5UjBdbOYtagqm3wAp38bm3AYFnzR5csvaOEHYgIgSU2OQnaPq6YrlFPBMTBK35zv9R1bafEp2bvP1PlPRLMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9HykgiNNYT%2BknUOCrcA16HhgejO6Uv6xblZnXF2S1rsQpfiilp4UlDadoeGwjG3ppAxscmVoqP%2FFfyN4Spo9kfOOkHZM9BiJLmgTd2zGUKedB%2BIC2t4i3IuAzQdua7XUVMu0fJkKNu35lvlL0m1BYTb0yGvL2SU1JhXHD8IAoCoJoVcLH75u9JvfVHQw9T9XmT%2FMjqCIGW5ZGRzYB2ASUV5qkJsFG30f%2BTLp8r164R7RCb2v1Fa6ZzLRbx8kV2wfPID5UVIbkIWQanO2vdMItRFyxwXbnf94QcOE2mg62lNlOBw4W1jAzr3mvvtjyfMrNNdhUZJnkkXZgGu8klGwNs%2BX0f9x4WI5aip07xzxECa%2FsvwcvDWvkKMBRpSKlFerThqyggluN5UjhaCEBbzfqbfNT3GsIn%2B2SWJu7bhFG%2BgkdYtFLkcGPa6GGaUeLC9O%2Bm%2BYjjXUZI9mp62NdqbxUprrd96TAJKx8PbaylavhuysYebDAuxecNrx4vQf6PQIxJ7S5dWQyLtgrxWoASueD0WAcHAGCY2vjNEK2ecspmAwhwD2XWMCUZMA02E%2FwzaaWSmStamY3IK7Zz2j8jj9BcDTOJit8C%2FBlpQXaeC7UWEgVjkfbxgHXBckogU9KX1a7dgU4LfpnTk2kjMJzC%2BLwGOqUB4fxrJzI5%2BdFZWxIArl0KR0GMDBj3cGNQxamjhh%2BhqOGNWaGsrc3%2FEcxDB8hP49nkWYOc3jFs0ly2fNbHTdUOXlbS1kVnZzFYesEU4TNv0ZXHvLDcw8Uzol9kkXUM6oxtMbvBVYWEXQUt5hJf0Y%2F5VU2V4wjC2IZOiVuyLqpCE6YCR5Lrig4z9lDXdQUnUU0eJK8k50UwB%2BZx3r%2Ftc6zl5jIJNHMB&X-Amz-Signature=13e452489f5772daaf21969d766e62127e6b7a626c681f80afa00138d7942da9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FJODER3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHtTFVf6wSnG6XL380GWa6kFFt0M9phP3NzKohZIXwxjAiEAnonr1JpIPbaZYFYcuUG5KOTdr%2F8d%2FsJXQhBpqx8qmLkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEWdbPwfLK8UMFnxzyrcAx9aEY0zon8QTCmll4kChC%2BzBCy4eGc6%2FvRMDfNye1vGmFZK4K%2BVfJHq7E%2FpA0EYuQ8tDpDynAy%2FHeUC11EiBAhzHEhlvjYGPW08wXmymhnOD1SeIhdq0qEuRQucOmYPVtLASk5zPt0quAGQrjDk0F7mM%2BlGfiX60XPvLF5eog1xCPUEe00Jl%2FHPhb0kGG6IXuRK%2FFwA1ViHU98TseoP2po1YF%2F65NnNL9xNTy2Vca4cgVlZFeT9agbJOF7RJTM1%2Fbg4EiDlkz0lkET9Jaj0n%2BoxkCkXt5hC%2B57OKWIwRMMQH%2FEwEBwaCqX%2BfdHkOvTwiyclC5Bvty9OIYBSSDDRggsUsvojo9dppaGE5SCONGZbQlwvGyw0XJjbnCdI19y73i2Ivp4lM4vaEy%2FW0dDlyu78RzJsekZRxwpO%2BiBVeVNYN3iuLXTIQE9KcmS%2B9XFmm80DIUxSeegKJZBdicpAgGdfdcKXFqTFj%2BF1zDtd%2B%2BjOQhLwPEGL2GZ9OgUjzGjbM2URpTiMaUfKs5v3ib%2B3r5EmhR5uzfjotEoM2dRZxsYmed9LWwuG3Vk7Cvn59GRPsLn2fhMw%2Fy%2BzJatxJ2wXdUzNgESXbjoKvAhb7DyuRswyECchiEw61ukuvVCsMJzG%2BLwGOqUBLOnnpoHdE9JPCOdHfahHlxR%2FTPobffZi4nSkvuK9ZfLfgQIPdXbOmwN7S5wbgP2O53qedv5ni6xNRYSJC%2F8r%2FGfadRiwydbfwvOUpunIeOmpuXB45t5lWDNbMqNH3ZljMxnj1ipGvdQqe3D3zjMwdjew4ydtuWo1bVxyEgyu%2Bt6brXsnQ21oE2VLZYX8q7doDNd8Hz3YCD0EOl75QZaBmNPxKP5X&X-Amz-Signature=eba8f267dada4d7898188ed6a4425b6d4b987587483a890bba0a489f47a5b6d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SNZMF43%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFnXLfbdKEXZVa5GILvCZjuMl%2FOgRjJqlxY7rOmWx2VQIgB0jOjjPlqJ%2Bw09EyWTwUTgNEL3LZQMPHyPU4CHNk5LQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsT8HH0GRBpaRqamCrcA5qJlAQQ4PysEvfBoGiF9jer5BKm%2Fe9F9ut65N28pUPmmF3rzBjW4T20uVDqVyMGw3Ve49VJrM%2FcW03TTwQufCs%2Fdv6kLA1XHm6JKe3CC4r0cc5PbR3Ru1RQjbUeTNOq9Rohlg9152id%2FXqAGLFdiKWDd4j938%2Bs%2BoPHETgIrKQ3mJ5yh38AAsJmDOPRSYzWKGNutjlqRKonlj808PWybV0Fg76BgC7XKxyd2HyeZtBwUr6T8OzNP5ppd6B99DW4KfBgAZCtOlkn4klXornt0FgFqWCmAXI63tHVwOzGPVpNWC1nFZ73Dwx%2FafwexpiDbicZyeOC%2F4zm%2BR3K696BX22RQjqnM7LG93IyjD1karyZkzSIHyT%2B4SwznEIs24quxAC1sA8FzhgSvpRQO5kO181dWdmjRGy8n4GqL1XT6dEzHdLwMYvLKstNKgYf7Ms0QO0RdsK58dX3%2F%2F7VRoGHRPHWxDsnIeaZncJH3DYwxvKfWdqa%2BX1zzLIgjVEucIopccl95Z8ICzPOlWlqIXt0i2IXS%2FK7t5HEfwEau2xLRyfeXyTlWV6UM3VxDS%2Fha7GCkAvT%2B5LuYd6FYRBiSTpfaRIChiHtr7w09wLt8AxPvKb1bklSz3Cc5kZeV8WDMKvJ%2BLwGOqUBc3Wv0OaRFotmBT4wTltbS%2Fzt936UinIQpWWvzpfd%2Fw93wkGXj1iUoFEDzhpl0373lFuMJP7DPJZkmMOlWKsU6f489gzuvmrd4xQwpnZQeqU23RYkd%2BHa4zAY2Ll99xBFsiHLO9uE59tUyJov3Yd1%2BZ1C6GAYAsR%2F8mo8PINDm%2FANhIQlfNyje5%2FtUhkCd1JrkIDpBzkOfzO3ICkcBGVv9DDl%2FHLv&X-Amz-Signature=ba608fdc90173123db60fecc95857873760847daa075db02d4dfec748b65ec5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SNZMF43%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFnXLfbdKEXZVa5GILvCZjuMl%2FOgRjJqlxY7rOmWx2VQIgB0jOjjPlqJ%2Bw09EyWTwUTgNEL3LZQMPHyPU4CHNk5LQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsT8HH0GRBpaRqamCrcA5qJlAQQ4PysEvfBoGiF9jer5BKm%2Fe9F9ut65N28pUPmmF3rzBjW4T20uVDqVyMGw3Ve49VJrM%2FcW03TTwQufCs%2Fdv6kLA1XHm6JKe3CC4r0cc5PbR3Ru1RQjbUeTNOq9Rohlg9152id%2FXqAGLFdiKWDd4j938%2Bs%2BoPHETgIrKQ3mJ5yh38AAsJmDOPRSYzWKGNutjlqRKonlj808PWybV0Fg76BgC7XKxyd2HyeZtBwUr6T8OzNP5ppd6B99DW4KfBgAZCtOlkn4klXornt0FgFqWCmAXI63tHVwOzGPVpNWC1nFZ73Dwx%2FafwexpiDbicZyeOC%2F4zm%2BR3K696BX22RQjqnM7LG93IyjD1karyZkzSIHyT%2B4SwznEIs24quxAC1sA8FzhgSvpRQO5kO181dWdmjRGy8n4GqL1XT6dEzHdLwMYvLKstNKgYf7Ms0QO0RdsK58dX3%2F%2F7VRoGHRPHWxDsnIeaZncJH3DYwxvKfWdqa%2BX1zzLIgjVEucIopccl95Z8ICzPOlWlqIXt0i2IXS%2FK7t5HEfwEau2xLRyfeXyTlWV6UM3VxDS%2Fha7GCkAvT%2B5LuYd6FYRBiSTpfaRIChiHtr7w09wLt8AxPvKb1bklSz3Cc5kZeV8WDMKvJ%2BLwGOqUBc3Wv0OaRFotmBT4wTltbS%2Fzt936UinIQpWWvzpfd%2Fw93wkGXj1iUoFEDzhpl0373lFuMJP7DPJZkmMOlWKsU6f489gzuvmrd4xQwpnZQeqU23RYkd%2BHa4zAY2Ll99xBFsiHLO9uE59tUyJov3Yd1%2BZ1C6GAYAsR%2F8mo8PINDm%2FANhIQlfNyje5%2FtUhkCd1JrkIDpBzkOfzO3ICkcBGVv9DDl%2FHLv&X-Amz-Signature=ee60ab7d3c99d34c3e947ad817d41eff38b7b0c9a41522fce903b5b782208913&X-Amz-SignedHeaders=host&x-id=GetObject)
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
