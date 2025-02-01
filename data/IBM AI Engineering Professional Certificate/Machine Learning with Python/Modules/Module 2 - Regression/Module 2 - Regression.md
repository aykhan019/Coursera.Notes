

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=92bf18a52ffcb944aa733744acd43b8255774eabe5062d61444699d3ac5ff23f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=fe79d71e0f5e7d76307c4073ac6793df059289005b134a455a66f3947ce7a82a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=fecad8ea7f3e48abe2940cba8885adc4299715856b7a7a9d19b761eb1013e01b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=49c010bf32f529aea4a5437d61a7197ef99b6ae4e61debb022438e05e4a27d63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=d6d3ef834c0722b3c3a191a1d41b20157ddf57e84030d678f55d66b416a3a870&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=e69a1abd8edb65f3ed42bd7148bce932e96a14bf5ef096c0d1d9387d11164fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=6db3f1e151ed1661efa55c44b531e4c9f30c743a17b51f207940e66fa6305173&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YABEHVAD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1wjIlFQvFACr29W7Uw86Q9NOaz1562SvpF%2BSdNnnn3AiEAh9XiZUuV4oiKBuVBHzh0%2BRjvBgN63b6iffJeM2MU5XIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNN2d27Stgup2BSdXSrcA6t7HuYUdFeeBkm4DFoxxHGAjXe3pPVLrZtVwBE%2F74SKua%2FQXIsAo8wOHUpnga35AJ8iCckn6b37ntwWBCQ1b8VDX8CZHLxPGEhd3VkC%2FrMKXEV%2FIEboBN0FPBcoJ7zsPlRawA1P67C2SIs5GlTg%2FkD8%2Bo6sHNRLbLYZBOPkuFi45i6ffU00qeGLquZ2GnA37I3rvfZ%2F9VmpTtPdeYtxPk5ZQ7qiHt4mD3ImQkRtrbpfzwKZ4nkqjYY8V%2FV81p6oKRxMC5cZ3d%2BycNklgL7dXT1ZJanYcDuW3d3k%2FWA19FzKofmUo5kYTbjnJSLs%2BWp2IZmXeRE0a%2Be0u%2FJhOxMrWiz9o%2BxTU%2BSBo1ClsXe03rlAMjAGlI5qNrwAZFGMvtDfIFGG3AqmeIRT%2BfTjj9wLvWS5fIHzpDVEegzGiJvTsOq6AqpTX4ug%2BrjCiW7Z5Uu8m9qqVJlCEFSIVh7PwdjJRSmvfjEpJsMKbiW9k%2B1iRhpyay210MxrxOWK44KLhO1Fo7dGQyyX%2FJQoQQx8Qzdfgia82XE7vsnQcDX6w8%2F3cTjgRzcTTM1B8olaeHpzHww5%2FBN8iBOt4nw1RVdyPRSwQRqHNEVB%2FoWYNmrnrx2wAe2fPyQYVA8IImkXtqKFMKmk97wGOqUBC%2BsFZD5YG9wQEP5KP22OI6qbzjSYjb%2B%2FWyZ4hAhXV8FtQawOBhFcM1w4gZUaM7ImjX5M7vflgdcwIcQtqhDkjy4sD5Ygz1dA3bpjkxxLHIOwS5Aim%2FT3I38CSvkNQfUTv8XGXaDyMs5l7o8V55m8OUiu4PywIVxD29fNrqK88UN9dbnEZ28MD1ZV9nWqZVdd8e8laBsIkB8ido6A9M7Ei5zKCnCr&X-Amz-Signature=816ecceae28a2f9fb608c8d95632a09e81220b77805451fb7372d6490a6c82fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D52VSSG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0Fl3L9UOSFiqRdpoJRgooX2NEi2glZ0hpXQy2qx%2BfjAiEA9OB7jXzfiGOyNJcMh6K4%2FEPKt%2ByWGpK7DXDkccuezC0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpNZdS%2BOSVFMJOpHircA7ySup8jL3uQSZ8stuY4L1rK0Xp4FO58f%2FFJr2V0I5LVfuGK3yc73t7YMkxRPkksge2XPtpEa5Opk%2BwoUyRLzGM2T9hVi0t66n%2F16BofD3sHc0ZJzZACWRBgfF17FrxTfqY6TREY7qLsjKoFdheFc6uiKeWnIx2I6WcLZks3BvOWjnP%2BoW8UwGCquxFwiIyhNfzGZvA9hb5hfUU0gFwbmFz7i73zDjM%2BNsSJrpZs8xsuEKyyYGtYetJqNikg6H%2FMR2AOHzUtzSJSCqgrB6DnrX7pkDHcQv1ya5GGySCWOwY1pC07EcSViFA7lJiNcoYlNriO98ua0TG5AGcV2SUWHivYvNdgN4Ow%2FqP4W41LSgewZoNJntcZuQ8vCa3ddYeu1DIB8P7ixtQvXSV9zVaEV4aRpgMX1RSnJ0cBqNSdHRYKRDbDc%2BbrjP1HhncxpjMngWkWCUmq2R0wB3vJRnkQXMYfmcPS8MDW3AxojjUAm5BtO8mTLyulPoUtw%2BrfUlHPMLvyTfa8gMN98TEeSG%2F9s2ECOiOMZDjd7NPl%2FU56Mjz0uvf92g3tfOHb6DtGHuWXmq9hhI0HmEEUUZHr01qbXMlxwPS91E1zWMyiHeGbqP7mx%2Bd5Esat3yVxMw82MIil97wGOqUBEtavjt%2FtQSr2iJ8uyBjpxYlm9UaOHOSdFcgIJkSZKC9FK1uDZgyc2eBqaH33VxFO1OHenS3q8LtuQMaoqivFU03rFPgb1oqd%2FM1MJKIlEWB99783cTNXxRIkdHElTQAxx8tL4eikpiZvx6d5Ob%2Fe0J13%2FKUalbLkd5ryVn5A5L8L0A6F3C3kxhFuZbrDteBGLJvkoUc%2BuMJF%2FCdIK8hdwvj1lEX%2F&X-Amz-Signature=b2d2055dd0a94ac3a04559b895d414d22ab86a66c533c1f31654915b7526e552&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LYUVG3R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGk9Plh2snoangDk5nT9Sf9%2FsFoLtkpbIW3oYYjyvvaAAiEA9WPQLcjp9Q67kYvdzVEf1%2FyIkZgxkz8UopNdPVkRjj4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErsRuuVV5EDiYrjkSrcA5WEtDnQGUKJSD49tjlApv8FyTEWSLM%2FQ%2FoyYsJdLex0tu6wlIsdfHBPnF7knz%2FSBR2XD%2FCAMYsqNWMKHtNnXhhhwQLm5V6VpfYM1U9M3%2BzfLwnv9YEYW9xXOx1qjcn529pe1ByQRwmM7jKuhOW32ZRBgPF4x3uez5ecqf79E6nqBYnA%2FulASb9j1uwuuqKh06FtHC9kXmLLx2txMU7Qf6aJikLLxHAwshG%2Fv0K4zn2lBjsIGITSnDNAQ6Xt274cCTVXw2rjp9L1qrW0Zy1II8P7njLxJikExAOWEaZL6zRpCvzx7l6tGm%2Bd9rocDd1rVG8uhi4Pmv52L0XbtSoajTLarniAN5zt%2BYJZB9PlYIVNyCuCHpkRdVoewaBg%2BHmG8kRjMa6FhEq%2BxS9t0bNRj6ZTv5RIkUWfyr9sJdpEpdE6LGUmNtwwOFRMor9oJ5%2FRA0LAKzf7p3hmY9C7yDoRBYb9YDibpG0JHlXbNBXX2zIhl6up18JAl1zi1%2FUgTcf1O4c%2F9RDbdAKP4OXhTv6tbhiLECPrpqhvwPZxU0NyWwqrhDpulI%2Bu1qLCAh41he%2F57N7plKW5emBdXydQYFWGTFaLGqW%2FCS6gwW3Fo5ldBMm88CThB3ca3O3jTo1VMMmk97wGOqUBCnQVSLdwlMzk4TqhQDwlbyx9ClTfLAaPhsFIPtHiYZz4XtfZjJmcKK6myA8IVumU4VieJR%2BAl27wA63XoYDSWYRPI2m2nn79AmKvoSBcTxUKelgYZIR7y9v1fu2P5qPuf4QbQuYmXP4aHC6HW0d2fZ%2FKyRBrttJ8h8vLVhzVnjhkTvV1b3ENUSoJ696sUU6TUYNmQpnXE7OjHXKxtFV0vyeZ1%2BUt&X-Amz-Signature=14530325c065093bc151678871ff294218e07395cc7350a94e0179c2ffbf37d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3KMYQG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGjZTE1Jf3gxZ%2FqLDbjMUKjO18hG%2BHI8T6YWEtzO2FUAiEAlC8JJKrQNtlzEIIGocS%2BJKwAEEFaAZ9j3haiUaewPI4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYaZWo2sNZ4f9a%2FlCrcA1%2BJ3ZQqt1moZ2wTit3knJai2roTyGXoTru%2FvrKopM71oFq5PQSmbTcYKi0WHibFHDvbiKrK3g85r2OFXfCUbkxLbiZyk2ph0uj2%2BJpZTBQzj6DCyAXWX7sYXftMj02X4sm872Nn6Hr9UCNUzHy2aTAcDumCiOBk1XRRFWHy%2B29RC%2FtzRU1zTXftnBigootDRE6UBalZXlS5ct7AVLv4WbWKNb2aHKm3no82OkXmJxOAaC0g%2Fiic%2BHOaRCTUVlC2%2BZ5yI3YsRm3BUmDc4B6%2FBRgJdg4BJLvTj%2FUUwbvcw2ifGFWzOyJFwMSC1v1BzaVJr4lsWdBqtKB24BAmTfkfZmwzkz04c2iOW8gbocH3pGTh8TCFeTIgKHK45rtqhA0cFjnvv5I9Igo%2BaFJZf%2BZ2YHdhP6MQYiqWFAYC5MNuCAQsMuZFRAwCXkm11ElLazMB6%2BUAje3P1voZ4TV5NLv3Fet8VDRyFNJxA6CLpFu05DV28WIK6LvKhS8Bdt4sORXael0%2FD%2BjE6vo%2FOewFELfc2OoiX%2Fzls%2F%2FOJl2GXcV%2BIf6Cg2FiM%2BQEmY9S31tdpSeKcpkqrtdQBarbE1VBEWDfmQTMSaTCvlc%2Bzj1eo0fiwlDD6ffaqNquaTgtvIKFMKik97wGOqUBEynDTIBW%2FcsIIVhXmryRpE3r1OQ4jj4FSmgRB5pZdtuhGDojfF7%2F63dpYuJVYQYk85Kr3fUiVbAVatOJhgYbnM1RPBmQmCkt9pKo7m1O%2FEhF%2F1TnK6VwFOtKVcAn8gZs7mBx13JAF2b9tuqViratWezQ30zXR%2BfkrF%2F7TPJ3pejp7M4wZpjaotwYQwzKnrLbJyBBFbw%2BHAAxkuMvBZsDMVyGh2CX&X-Amz-Signature=1b6453ec3f96853f653c2f097099b18a230a995734a2f76183aa6ad13e1e5dcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3KMYQG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGjZTE1Jf3gxZ%2FqLDbjMUKjO18hG%2BHI8T6YWEtzO2FUAiEAlC8JJKrQNtlzEIIGocS%2BJKwAEEFaAZ9j3haiUaewPI4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYaZWo2sNZ4f9a%2FlCrcA1%2BJ3ZQqt1moZ2wTit3knJai2roTyGXoTru%2FvrKopM71oFq5PQSmbTcYKi0WHibFHDvbiKrK3g85r2OFXfCUbkxLbiZyk2ph0uj2%2BJpZTBQzj6DCyAXWX7sYXftMj02X4sm872Nn6Hr9UCNUzHy2aTAcDumCiOBk1XRRFWHy%2B29RC%2FtzRU1zTXftnBigootDRE6UBalZXlS5ct7AVLv4WbWKNb2aHKm3no82OkXmJxOAaC0g%2Fiic%2BHOaRCTUVlC2%2BZ5yI3YsRm3BUmDc4B6%2FBRgJdg4BJLvTj%2FUUwbvcw2ifGFWzOyJFwMSC1v1BzaVJr4lsWdBqtKB24BAmTfkfZmwzkz04c2iOW8gbocH3pGTh8TCFeTIgKHK45rtqhA0cFjnvv5I9Igo%2BaFJZf%2BZ2YHdhP6MQYiqWFAYC5MNuCAQsMuZFRAwCXkm11ElLazMB6%2BUAje3P1voZ4TV5NLv3Fet8VDRyFNJxA6CLpFu05DV28WIK6LvKhS8Bdt4sORXael0%2FD%2BjE6vo%2FOewFELfc2OoiX%2Fzls%2F%2FOJl2GXcV%2BIf6Cg2FiM%2BQEmY9S31tdpSeKcpkqrtdQBarbE1VBEWDfmQTMSaTCvlc%2Bzj1eo0fiwlDD6ffaqNquaTgtvIKFMKik97wGOqUBEynDTIBW%2FcsIIVhXmryRpE3r1OQ4jj4FSmgRB5pZdtuhGDojfF7%2F63dpYuJVYQYk85Kr3fUiVbAVatOJhgYbnM1RPBmQmCkt9pKo7m1O%2FEhF%2F1TnK6VwFOtKVcAn8gZs7mBx13JAF2b9tuqViratWezQ30zXR%2BfkrF%2F7TPJ3pejp7M4wZpjaotwYQwzKnrLbJyBBFbw%2BHAAxkuMvBZsDMVyGh2CX&X-Amz-Signature=8cc44f13c7bf446bffe4aa40b7de127d5863ab0fa80787018fbfce4728676d11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
