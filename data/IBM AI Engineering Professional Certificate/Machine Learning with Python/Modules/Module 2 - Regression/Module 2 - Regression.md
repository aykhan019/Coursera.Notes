

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=ac3492bde65f94f97a40230c32d319e7abd0da7993142712c21daef3413af1c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=f7dee93d89973c8a8e2c4693ac8e7b5f75a026d8c6cbdb3be8cac9209492c5d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=90ad87146c0215f1d60e0d681ad271c148fb484a20d43e55d300244af42aaf56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=70a7fdbcb6f3f687666e16e97ddfe86367be10eb19f4ca13935a119b605c1286&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=bfc80418c69793006f1f4f91cc5dd398a2588912ba03401de4ddb1704a29e720&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=0a7f9e9a92f1c57ac2aa90db5403488ca9bcbc83d744c3884e1cdd5175b28037&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=a6d496c33679cde713cb053b73572a4cddc6e97c64501df3d27a8309e7039786&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSITRCUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCYshLT82fA9x%2Fx1AY%2BAnr5zmtxxqDY1EN%2FdlzUSgtyMAIgLnVFlZP2nMdEORklMtCXWCdxkFVzT%2Bmi%2BOeF6%2FkUEDcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo4ZWXZaqLcT3oVmCrcA58oSF7qW3GUykAlo6C1crbmv5hxYcaA991%2FPxXz4odQBuxdsu20LYdEWl%2FZESc7iMdZUDqlDfeXUqVnjC%2Fk1aiP3wi2gylwDCyz%2FucDnBasg4ecpAbaVGVOU8IhP91Y7gFNsHgt8k0Grq7P2RH8RQJB03xjcrSMZf%2FVpyln3JQCo%2FssEZXDszRvmstybFbmMIHn%2BZTyEk%2FdKkAFDnAYkGM7t8H8GeFwWYUxRUmKSE8AjsHij8L1m69XKmPPTuTn%2B%2BSMrVwwWUhq07SHSY10MtU93RlHUIGySuO6c1DFHmuTgdbz4GPoVBqQlQ3NcCxpWaFb10S1lgd1%2FaloDfWzO1wqONPKr%2FZBRPRff2m0f7Zk0%2FtE87iW3cAAJFQSqqCZj0ejVeuoKwmgNyGs9I0BQjEDm1PfISKsUIEeeY5%2B%2B7ChpusWq8S%2F4qiY19mX28FNiGGZlSMY%2FAjihz2pDAy3hLFUQvw0g7flwe80tfm2%2BegmS8RlwBdztoQ4LRxumND%2BPHDheuSCAKPc9k148zjXmDKajVCDgKt5%2FSIwV2tf4UqrmTUoRmjSd7fTZctcPDENZhtmAwjBX6%2F5wZjEiInbS90CPto1ZiZEH99Lxbi5tzXQ7PC7x7Ta7STv7XIlMJ%2Bym70GOqUBi9dYLewDWSZzQdFI1G1Xw4H9JfKvj5crAFnXDjsOvbrp3UgUPtM%2FzJwtZjhP2npeoo0Qdg8zxfMGJqAalmtCvHKNbcvBr0ZtvbLoMUkw37J%2Fy3PIkmHW6Jz%2BEX4tiruH%2FAiiMqHqrLmC8kHrBK3WE3JGUq5LS6PySsEolnKl7qzOoCWfgKlm%2BRhli9o8MvsHs4zs0QLgAN%2F%2Fo0Lf5nAXDcRuJ96d&X-Amz-Signature=19a0c7b9204b69e3186132cd072f0a5ffffdb91f122294d3c31fc2f390e5aa58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNKNGATI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCICZlHsLXo0RZXyFtDPI1aD3y%2BVOx9FELBhMZazG4sHFzAiEAysRFhdRhD2aXTfime5%2BeH2JdpaU2LBIISuEe20fwqdsqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBMDSF9%2FvIp2zv%2FWwSrcA%2FuafkFyZegUxOCq5ou4SK9Af%2Bh0uM797lyDl8LNpvcAb6dk5g66ip%2FbQr47ujj%2FxR8lA0tx1zz%2B%2Bqc%2FP5CcS391DBbNFk2uzrirjNtimlDoICBCEvzZkRJrnyp3FZFWWEio7rqDsJ6WB7s%2FChRCg1jX401wCZSB7edEw7FTT4Rmsk%2Fo2R7JxOgTJmsRw5Vk%2BPAJplvAl9qjaW6aBRtnqGWBy1uyHCmVlx8hUzec2eSlZouaa0muPtgFsgHVLYSOR1y2GFfurnzQqCR3kIgxVbwr2n8H4EXkIVuFXLoqDacOb4Y5iM%2Fzu5JoBvm%2BDsKqKdias5HuxwT%2F639BOhLoJ2s8AX95Wr71PGw1U9UidFNV1M3f%2F2El1CaNC44Ta9rvQxZ08EPlMhTKrHr6sAj1pucGMVxNC58vyuParcLg%2FOhSOXwr4KhOXxUgOe7yOUIvYXvDbtzwQV21d9pBRDXn55yNsOntrHelKKnLZkJ2xAp7s%2BMO3WrnliSNqRYP2a17c8%2BelSTFunlWSFjsE30APV9Q4qyvNOcpt8GQmmUBJ9cVmvY6zm3y29Fppa4Gd0CNig13dimHYL4zrYsCZ%2B7kVxoshtO9sdb8%2ByIHi0BenLNIOo%2F4gdY9XdLKdsrZMJGym70GOqUBt%2BhzMsmj2q5ssmGxfEO7h269dte%2Fa6C2I75rNCkvPpGA8jZqH9YbvxIcc0Sk54gb%2BsgXvRSkchGK1GOttx6O7%2B2mhR5SXA1%2FZhc2zClZR%2FByCe%2BlvoyTDSA8x9zlnV56Iw5fbI%2BP34tbnzK6bcEpBmgia%2FrbChjzuDs%2BJS7dEyj1TBG5WwiNrKT%2BwYKNV4Tl%2F42YM8UpHQBfrGObH2cikjo2S2QR&X-Amz-Signature=26bcbc8cfac07d7517facf333905e9f0fd4cebeded94abd116dd360d07604e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3NGNAGW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCxw%2Fu3mQXj9kbZnm8V%2FqpvONBjDMcuNxWuhn%2FXZXylQgIhAP%2FPc7f2XgicUOLmE58UWUxTvJ2FzEe3jlT1M0lV9IdbKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BOev39Aok1QFdbLEq3AOW0p7vd4rcoBEASHPA%2BZq5B8Q45k1nTdE9zmA%2BZzp%2F%2BAKkMfxIj8Tr0NTmDJP7OoJt2IuaVO2QQXHUGjkXCsHH%2FK4I%2Bi1VCL4GC9n%2B3sr38mVCoG8n%2Bd6BYTavUgQ8PG9FOyUh95UMKXHiLZ3FBgvTzwOu%2FhQ8mbhjAt7vOdVc%2FCfMQkwaoGXu%2F3v4%2BBGqbeBadyb2%2FvD2YSPrUdG9cPEfFIvIsrCradKCiR7rRGInGaQWrFjbGZMx6IzkFTOGQVCP%2FGXd4DgkF1NrI%2FonAO1B5mgEv4RemgVdsDicdU9avjK324sw2QWL8Ygb6Nr5GcACvhDhxjYgKshQSBOu0g2ccEkROCSXm3KSAxxziKl2uWmpqc685jbp%2FBrtpeZRu76G54hIImD8iFfcmLK1%2Bplx2bLPbl0YUCcXoSyvennWYE5pT2nLUZEUue79iEZrLzDb%2BK2zM7HeVfRZtL4wY0gw433MLO05yz1EvmSVnVPkR4JD690QwmWiqvqBC9FqDzQM1ESzfSnGoIMo0lVWpjNs9KnujwlUcWJCUKzDi6u24HwXnOC%2FfcKX3vqSBkJmiKtld4c5PMkrTeQlRE%2FKk%2BvywzAx2tiEHNxNSd5crHAKYQkFt%2BxcM6Gq4%2B31BzCSspu9BjqkATgKIOT8opWqpN5obE0k2fYImjT61Xr7JnCcb7hHrn89XsZHBjuR9l5qnE6RW51bkesofr9r8Rxc8mVcZC%2B9kBeIA4ujW2vY9X6T%2Fkqu%2FwmF6SMyLHYq%2FBY%2Bvsihkm9J8LfJydtmZ%2FxsEmk4y3o8ssxQ3t452jE%2FbeloSj%2FVrCx1gWgE5BQ3kawbqurmK4pBgiMfVoR%2BhoFoTA1VAlJCyIB2NUT%2F&X-Amz-Signature=5c143786e03cd976a580f0f0614e586d37141c5b68834f54270c6754e0012bd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUILRC5H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAL%2BLhPPiFbfkNbw3AbfbOFTzKdTjQrBapx9FgisZhldAiBPel3Y9QYpIuIYce6DLvzAewZC4qVGVfo8HTtq4eRGwSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiGdqjQQyTaulqeCWKtwDk37zsqWnhHg4O4gd491%2Bi%2Fgmot1AgKhOkJE8imwsji5StxSNZhdWDBe%2BsShcc2pp0HjQ65DSUpuI%2FTL1gC9X%2BvYV9xZPMLkgtaB%2BYL%2BIQbIf4pEUfdSmKRz%2Ff1gTcY2h2dtS%2BCeV05fXcwpT8YBlYqrDzbm%2B3VDORar0w0MPmyqspo2ApF3jrlx8MZXDGRAG4hnOBMUzfpEHIe1RNtKvjxcOpwreMA2K7dPmBtcNa2jFu%2FZhO7245sl%2FYljj8oknEIHEKV3xZ6w7%2BJwXPjVMfnXkgVgBNEzQMRDRdn%2FxrPUXXwzVz64ArXFCDHe6PW17KBqoQtr99bXnZXN6lcsANp7BoEd8jUuDe%2FNCZdYPkn4h3mNOLLZULFbWkL%2BMsdEM%2FAx5pgs31v5LcxamryK40EaP8TLsyabjoQwTz%2FrN6bHBhUaXpLv9QXHaFuw%2FnS9uF5hF3FrQqbkDucb3o%2BwNUQYOyAUBzuYn2hDC9O7WLRMpPPjZLyEsBlLKVzpPu2ITnaTXCWZ6iE1%2FXjaAAHmzPVHXGBWfjqjXGawCRF7dycXVzkNJEPNZxNHMNASHRveseNZyHTV41s9J7M45v2sKW3vwr0Xmj5IwdTeGAivNoLLZFlqMZaOIEiYyxUYwjbObvQY6pgEWR9vZGEpHoW5bFvfgKrUi6aDoJmq9%2BNYaiqwiKQ4wXkkXH2Up1eKuh%2F7lCUDbAbODIv7MZhsXPVJ%2FEj1gG70%2BPzPmfonIw3J9FVICHRZf5ToTmijIUlYODFCrGXjTRPKsEv65JLbFqiYE1Fz0cah%2BCaYbBL1Detvi9wW1aDS1bKbkmMZSyueGdHyKJ%2BRLRFe426Gr6yx3jBGOwc%2F%2B%2FjlGb%2FrqEaOL&X-Amz-Signature=92ed18f93e2ded04140908baceba2f7883a7b725341bf85a5e0a640163cfb81f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUILRC5H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAL%2BLhPPiFbfkNbw3AbfbOFTzKdTjQrBapx9FgisZhldAiBPel3Y9QYpIuIYce6DLvzAewZC4qVGVfo8HTtq4eRGwSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiGdqjQQyTaulqeCWKtwDk37zsqWnhHg4O4gd491%2Bi%2Fgmot1AgKhOkJE8imwsji5StxSNZhdWDBe%2BsShcc2pp0HjQ65DSUpuI%2FTL1gC9X%2BvYV9xZPMLkgtaB%2BYL%2BIQbIf4pEUfdSmKRz%2Ff1gTcY2h2dtS%2BCeV05fXcwpT8YBlYqrDzbm%2B3VDORar0w0MPmyqspo2ApF3jrlx8MZXDGRAG4hnOBMUzfpEHIe1RNtKvjxcOpwreMA2K7dPmBtcNa2jFu%2FZhO7245sl%2FYljj8oknEIHEKV3xZ6w7%2BJwXPjVMfnXkgVgBNEzQMRDRdn%2FxrPUXXwzVz64ArXFCDHe6PW17KBqoQtr99bXnZXN6lcsANp7BoEd8jUuDe%2FNCZdYPkn4h3mNOLLZULFbWkL%2BMsdEM%2FAx5pgs31v5LcxamryK40EaP8TLsyabjoQwTz%2FrN6bHBhUaXpLv9QXHaFuw%2FnS9uF5hF3FrQqbkDucb3o%2BwNUQYOyAUBzuYn2hDC9O7WLRMpPPjZLyEsBlLKVzpPu2ITnaTXCWZ6iE1%2FXjaAAHmzPVHXGBWfjqjXGawCRF7dycXVzkNJEPNZxNHMNASHRveseNZyHTV41s9J7M45v2sKW3vwr0Xmj5IwdTeGAivNoLLZFlqMZaOIEiYyxUYwjbObvQY6pgEWR9vZGEpHoW5bFvfgKrUi6aDoJmq9%2BNYaiqwiKQ4wXkkXH2Up1eKuh%2F7lCUDbAbODIv7MZhsXPVJ%2FEj1gG70%2BPzPmfonIw3J9FVICHRZf5ToTmijIUlYODFCrGXjTRPKsEv65JLbFqiYE1Fz0cah%2BCaYbBL1Detvi9wW1aDS1bKbkmMZSyueGdHyKJ%2BRLRFe426Gr6yx3jBGOwc%2F%2B%2FjlGb%2FrqEaOL&X-Amz-Signature=a8d22289534282e338a0330510c95d1dad90719e0e19cf52680bde588da0bb78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
