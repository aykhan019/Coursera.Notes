

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=5dc8420cd30888a86a107036c3fa57c5da7f59fea02f4ac16373cb2132a870b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=e0ce91f4a246208bfd687ce75e5769aaf4ed2b14a9885c45482ce11f2f2ba092&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=cbec4bf5ed4e2cb0699f9f69ae3370b9480f04973a594d3717896be171db29f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=a8961e1386e1b349410fe987e60975f79180d213ebced3bfd702ef7bb0d7693c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=3ebb3baec04ea10a4ebf5e2dd58385f60df365a29341b0d0a707f0f677383c84&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=8a309992aee36b6491ebbb67ece8348b3d453d68ecaeda276ca6d8f48144e6b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=5f1eaa1bf87fbc1f417fefc0dac13ce683fe99a80dfc4adab80fe368a12c5c08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7RCDBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhDP7%2FaIhswpMxgpR7BUTwcyKyrSjrx6JUaU9FcdmoowIgJxFXYNcfE2vGdLvoz%2FSQAAPbiWTqqrrdalBIeP9JxcIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKmPJvUTJAhCJRUVVCrcA5O6UVN7Hl3iYtODiilPBDSpW723HJEEHvWR4w4dBb5xU8Mw7eoDzlr3KjSERGAvtY%2BsGSQ4UakjZ00ctqGML8oC7xHLjzDWa7hpg4%2BohXqc5nAwiTveFYV9f%2BJXnn4xDASDb2e5quFdXdlbXesX3DSwHvvCUM%2F2qVP0nouzUocR%2BMIC5UvaipriQEo18tlcEIBLq22K3H7%2FN5aogbvJAfVsiPbqaNkCgNCIQUF1FvCqWB2guGZ4xogbyuBranM33%2BNQ2UL83WzDzBZMIb4lJSJ45S58zM6ZQw%2BfqE0dPIykI5G5uOhpawJqSAAWlv0ZogUFyGeWHPbMl8XAUIgu0uZ8L%2BsXme%2Bz%2BQPEaM021yHz%2Bk4pL%2BPlYWaOR%2FpynYk0rqT2dj7qX9QlfxtjsIUp1fzM2qZmK0kNNzdpwoZDQhNDO2n8mNMwYspcQGGQH0x%2FJvWLsiuf1wCaJgkvZaGr8xITDf92s8I4fWyjScVeCPdMNCTw9QvVqT%2BZAUVggFiI2TLt73a4G%2BKNcl3VnRC5R13YZIHm%2FTaP9e%2BKqRLCU3PQtSw0ssdi7VKdH%2BucAqknewO4CG5JTyFRuAifmtchv2n5ERMQXKh%2FtMRUhQf8Sx0Yomc7GZzUi8WO4eAbMMXr7LwGOqUBno%2FBSMYl9w2XMB%2Bq7kza228stuEWEcoifvVDqYbygEeKsHBpYke2e9I0fklu4%2BzphECClSfBRxNi8HteCIgBSbU%2BDDsaYf1d7andZjj7leXvU7KUWdEhB%2FTRcZhYCZHfSdne6eXsTpdMOViz94yk5nm4gZSOEAx2xwmGkYjVYSHUC9IB4zPI72FA9ff2wZeIk2g%2B9TjfOKrGOScwQIwwccNXc%2FIL&X-Amz-Signature=94f1e693f6da9f84423ff42cd4a97af5146d580fc569cc1d79e66182f894a9a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY57BGZ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3RjZsQiUfyo%2F2tGWhaQkUp%2FZW741ZG6tzrGWWtdl9XgIgMgrP6YFbpPZqEQIpzxBS3Sl60DlMwrSQbMolqWiWC%2BwqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaouPnScGZRlzkj5yrcA%2FRWZkL0JokqtZ4ot12C5S%2BZRXLFLvhCN46LENhr1kdmTUc3knJKG57wtX%2Fz%2FoFQt1ugQ7BWsAztjR93wyMuaTjzfOLSIz3AvGjh2wOXv2lVOEzwKQiPP2HEmKzn4y2dRYEFIm2BwDecWJ6YTp5iCTzv3R3uddOZ08gGOahVBysjpnu%2BOiqJWnkGwLj%2BJxDsNdIOwq7i4wUreLnEO00hEsr3pjW0Qo6mgaDEULdQBNfCy%2BWZaygMeuT6xcrdZ3xHE2GxBt0C1AeqfSv2lBgWrfEKtve4v0e1wfyxRGp0yIFx0Mb9tK6jicZvn3GUQkTURDy2mtk%2FkYss6wNVBj1EhAth977bhItrYxCKBlySatipJHWvXiLkuQKLLWX4%2FZ5w0ey3nIIHbs8eF0AuH%2BDVJzU28Q3Yx%2FGGxqt49DfNBOtw9NNR7Vi76qpaK5ZABskgFrt054EH58OIqRK1K%2FDpnavLJfowtucgq36ZM1s1w74AiMuvQCdUojsDO7HhTjhUMXNPOLc7OFHAF7%2BI2M51ioMHkFN6Ber8PreCfWm16z6hvcZdWKsSD0CG%2FEWD80v74Vgz2kH%2BMlYKzNjbOrnxHLR4TrsKcyVR1sailiZuJ4To%2F3ZQ3LmXTsvBhC8BMIHs7LwGOqUBzizrOLSOEmKi7%2BhrHJ2163sTHWDIBvnJn4Rwq%2FmsH8btqeGVGf9kv0ML5FU0zfjTHD9EMV6gVSxrxXa4ZKmHFi7MOJOwLVWUp60HCCAtMP4lW60oh77nLh4OD9%2F8wu%2FugaW7MQLjUZRbkoVCsDyvCT30EHuM150Rb9BcfkyEL6rv0UIRfpCq7YEYFcNEEI72Jgspk4FBT90lrg4nQDimWWvZTyk0&X-Amz-Signature=9c63ce7e7007888500e3a218fb7ded6f7001c3fdfdb6b50c1650fd1497a26769&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663USDBSFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDApfwLGA20Re4Wid2FWxth3YwPbi%2FPvLFmL3e3YC%2F98wIgTY2oiVW3JgrJQmv5Muv3Vs9wsyBH%2BzpQ%2BAynrnCtGYoqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7yfPwUYzUrW7AtvircA4SDBwJDnbEJwixTsfyY0nFbAq1091WjmF1g4H69UPbBjo4N5s7mkPvXh4HXZHShqS2Xk4oowIZ7ImiwqL3WCsSVpe4wo3m8Dt9n3lhsM7sCsmgknp%2BeOq7EOwF0qBa1e0JneidRd8oKyIuWVpm%2BhDASD%2Fo6ap%2BazniSBehCbPHEQFErMWxDruyxui34u3lN8E2%2BBsWDFDLDjnnUiKX0UJKxY%2BwrDWtikgbsqAtWTY5RCUEzMVvrKOYNUOY6uVsmoRmNhdA9e9Ljm%2Bz4OQmh6%2FOSw4bhgr8YWOVKDoNP%2FGutW1jaeKUa3Sfvwn%2FEwKKm3aHE0yq2Yg46wRCB%2BYTdQjim6mivH0PUlrrSELloc1XHvme12cYvJBJKqao8uKBgGvODAq3GVed30yGJkaRjk5bdJkLe%2BSfwEARuLcPEun3MysKlXNXyWLxewOnTWs6YZlw5HEwEM%2FbT%2FMfe4dQgf%2Btm6GIHu%2FVy%2BlcA%2Bqhe%2FsbqlwtRhSxthlKXEUuwIErRHcj8cFB9VLE3FAOMhNwyA8cwPPgVTgwlU1N8W1RfGO7p46JdEa9hUKrm7z10grWxrbm9z%2BkWP%2FdOtiGMLMnwUhmWb4cOtnmVuTgUwAE1ilLJRr%2BxEGtqefHjBuCaMIHs7LwGOqUBzyx8NcuMV0uNb1Hb%2BNpJbDQwdS1W2RrP0nmxnTvb6Pl8v6jK1X6CmKBJuqJ%2B8kFYzh6cWzcgUiyQTGPwI6xUwtdqp3esAICuTx17OHrF3%2BuSsBWM7xWKA%2F%2Bm4HYSNYoSUgjbWZaR5Kq1uWea%2ByftSuV8M4E1NZXDErV8iwJmAmupHoobx6yvoUF1KrpO%2BSdnLGh5CZHyVVpw8AwN4rdwQAWNGm1O&X-Amz-Signature=857f8b21aadbf5033a5931d69984275bf9d2dfbfd19b11672aed0b6b3722d927&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV56GYPC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFSPijNnUtcTP4TO635sSkxnALe%2BWX8V10f6Gc8PFQuQIhAM8PWTIijV9SmItDTkk%2F2TT3iRrQlSDGoWXmDe9%2BC3p%2FKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJIG4ITY%2FN7EVz9zsq3AP%2FXFBpRYpihhRkdEXj0niEsw0oew2cEI5PcrqtSVKBFdOUylDYWMJgARTT2i4XUEfYx48wVb5B5wzRj1CuDWTphsvL6cJWkGPKqe0hqTzQfoc8pG%2FPruvw%2F%2FbYF%2Buo8csbXLFYs6QJ2arSMrGKVkzvy8p5Cqrdl%2FZ9MHuEen16RKyKcaEnCbjRG9h1UedcGLC874WzSjMzSJk59RpZQzWJ2jJEaTVU7p5gmVCw%2BQIUNNxLVfCp2aY%2F7pmev05SL7GzwtAyj16QSHFL0oy8Sry8uljum2sVwvbQonIvdt%2F48MBYBeLOTQH2mm6nTpCuCZy6jxwH7EHAObxAwcTJ1UdGMNlGNJTHGGKZbBUbNAUj8nyjIfS3pRw4fMgjCVZCvTlTSjbVqmhKVG%2Bj07un5fiBfAHebt4JfcRbBbLkbNhaEC8IRHl7AdtYMr%2BXHaRbz9XiG8n301pWUV2Y4%2F1elRYjIWfaTxQxIs%2Bmc8SdDvxu6ih3NXjE8SNMv1eknas397u3YHI8rG0MHBayvcb6Ep5LMwG%2FcVx2Rxt3P02vjiZXkXtUyczOKPSU4uueOWirAMugftPXaKhp%2FTC%2BOvJTnADQjbotCJQxd1lA%2BzRx0Sa3OqCZpmkuHf4FNaJDWTC66%2By8BjqkAdLUmHG41qPs8dII%2BrdmH1fsUpvoBLdLFOZfbYVY1tXQ%2FTh6DKA2bu9e%2Fdy%2BsxLpzL6WwaVBwoNc4g58x4QECCuikU0imy4XQ0JrpAidDS3YAHhpjTFK%2BsERQYyJ%2FY%2FAfFFg2saejjPm4kVXfvzDrukcGlqKsNapb%2BfGw6PE0Y9dZ1myXMXBMP00TquDyDcRVx7XmJN0yOm2A4UspviKAcBRBod8&X-Amz-Signature=72b22d110e70ca8a54d01ddf6ba9f394f491e059fe7a90cb59c5d47dd21c5bac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV56GYPC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFSPijNnUtcTP4TO635sSkxnALe%2BWX8V10f6Gc8PFQuQIhAM8PWTIijV9SmItDTkk%2F2TT3iRrQlSDGoWXmDe9%2BC3p%2FKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJIG4ITY%2FN7EVz9zsq3AP%2FXFBpRYpihhRkdEXj0niEsw0oew2cEI5PcrqtSVKBFdOUylDYWMJgARTT2i4XUEfYx48wVb5B5wzRj1CuDWTphsvL6cJWkGPKqe0hqTzQfoc8pG%2FPruvw%2F%2FbYF%2Buo8csbXLFYs6QJ2arSMrGKVkzvy8p5Cqrdl%2FZ9MHuEen16RKyKcaEnCbjRG9h1UedcGLC874WzSjMzSJk59RpZQzWJ2jJEaTVU7p5gmVCw%2BQIUNNxLVfCp2aY%2F7pmev05SL7GzwtAyj16QSHFL0oy8Sry8uljum2sVwvbQonIvdt%2F48MBYBeLOTQH2mm6nTpCuCZy6jxwH7EHAObxAwcTJ1UdGMNlGNJTHGGKZbBUbNAUj8nyjIfS3pRw4fMgjCVZCvTlTSjbVqmhKVG%2Bj07un5fiBfAHebt4JfcRbBbLkbNhaEC8IRHl7AdtYMr%2BXHaRbz9XiG8n301pWUV2Y4%2F1elRYjIWfaTxQxIs%2Bmc8SdDvxu6ih3NXjE8SNMv1eknas397u3YHI8rG0MHBayvcb6Ep5LMwG%2FcVx2Rxt3P02vjiZXkXtUyczOKPSU4uueOWirAMugftPXaKhp%2FTC%2BOvJTnADQjbotCJQxd1lA%2BzRx0Sa3OqCZpmkuHf4FNaJDWTC66%2By8BjqkAdLUmHG41qPs8dII%2BrdmH1fsUpvoBLdLFOZfbYVY1tXQ%2FTh6DKA2bu9e%2Fdy%2BsxLpzL6WwaVBwoNc4g58x4QECCuikU0imy4XQ0JrpAidDS3YAHhpjTFK%2BsERQYyJ%2FY%2FAfFFg2saejjPm4kVXfvzDrukcGlqKsNapb%2BfGw6PE0Y9dZ1myXMXBMP00TquDyDcRVx7XmJN0yOm2A4UspviKAcBRBod8&X-Amz-Signature=463b76408832386d47397be345ab250222c59b1e5d1efcd1150b23d365c113d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
