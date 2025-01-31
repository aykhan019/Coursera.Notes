

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=32873e0b99b639b2448af803f26785d3d10cd8acc636b83e58d3fb2407aad4bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=02f3f6b15a6d0aba239b2b086ffccaec83c25e934afdd06a538622712289ddfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=fe72916bfebade9e0c5934046da0081ba9cf452ddc04014b4ef5f095d5810c61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=5bb30a98b24d2dbb4db20ac2dfb03a6048883af64e792b4597c01ceed68c374a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=0e3645a6d9459ae6bf6673be36731f2bcb9b1a0c56b46207774e028ccfae2e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=94da88a95be9a43fa2cb3aa77fcc19f4de7a26e0f3acbe6cc36bf3a5dca256ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=4b67e6ba78a204e9867c980c4da8d1fedb55f6a37e5a6d0c17008d193cd74872&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEFLOZWM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bk%2F1f3SuZ77VQWeRVApmxjtoYR76fwYiJwYKVA5cgLQIgL7whPvT2HscXGHBVEIxS7bx3svLbxRdtequujSZoULMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCgRCzuX5cWaYq43SrcA8S6FhKvqfgfk13OWrYSKSqDAwuG7aA8pgFfI9B6Ehsr0fZ6Tczs9LEZp18JxJrE8gQ6cHBON6qgxHhXPGFXAt0fZoYSIHItoh9lnxxmWGifptCaIibmrPb3yf0pGbQFwStK9XW0JKl03GR%2FaCMozsWPwPwF2XdarqFqQiHb%2BBVXlqHyJyhgwAcK%2FaYw5sFZM0C6SeOxngKUFxSmBTZ7orpF7nGrlSmqHrRn3KID9DPb%2FRHJFGiAvvnl6VzHJxXBkyFKscIxZ3%2FxFpOnW9YtULc6o8XY73vHyre2kRvx9iaYv85PjkSnTFrYr8Y1zk3do7c92Wg7vAj%2Bc278xgmhu54MYBU7FOIgbREtWKr5N3cSEEwr%2FKKHmG%2BzFC291kI0j2uaSbYG%2BdS5vQiMdaKcOeZjcp%2B%2FqF3LPNTkkNNu%2F2zm3W%2BUamXux5HPpDK2VbJUiOp%2BQudFZpWCm1WLJda67RJLSW1diTrRshqapUte0x7%2FkdAUPxSHPFswP2H%2FG6QCU24R0l0wz%2BtGZ%2FJkNa8QDlC8bgxGpQL2aaTUZVkbQItJtuIw6vTxMCcTZubnuFvz858dnF0i8TzlTZHCuH23Dx%2FbBH2smgUZEXtK8PMhRy4wUlMHf6mP4w7qC6n%2FMMa38rwGOqUBQg1CILOl17yV6R471ECZk1nVtYnD2rKMSku%2B4Mzbvdqq44bvb3dlaEpyKCieYWmH17LqtueKlQsIZOrG82kFc7SsldS%2F8Mo1JXldcPVIX%2BHWjiXYlR8S46gcnNLHuZb76V7hEKSSxTRRODf3ZgD0GYYSsKL665YdX7l9WDCoKrgYXVpc7NaK12AO6UUmzHnvI62Ww6f%2F6WPwwCz6CLyY%2Fozm4Rk7&X-Amz-Signature=f610dd312070a4715d4bd6ddc0155708ce530b4c420b67192e4f08c12ebc7a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662734ATG2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLSBhFI225zM3Luyo%2BpV2lHhkrBXcVVJgsozL%2BJPFkpgIhANh0ikU7%2B1gKwEAnI35KDQwwfQKVjLROBSTSgm9upIiUKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweLmsOqLUJSAM0S74q3ANRK%2FLaia1Cfg5FBWGqoZd19o7u5FAF3VAFixNIfQmLslzbZtxkfSQ79iJ1CJUuqbFMA8XTgdjwazHWk%2FfZlo2cxNf72%2FLp90bt26ytgfvK4X6Th0z2xw2zyj8rarCyI6PAGbAE7Z3f3ns6ms3yCpkY4fhHGY3lsB30Rw60tsSttZkN7kpUmzW1Bcjf99O6TR5zONw9%2BfggrqOcaQJnlg8gMPcUuVEjhGSvSwq5L2hhkUC3X4RfY2wVBIRkNcg%2FCCKtXai%2Fbfd7QnfOR43fU2jntn%2BBY9FdU6YKCtf81SwGKEmwaohUO6VW6C84ZFAaYFo1eVmk3IrEWgM9AjJDCI4RU8m1btInOWKrDnZI8lctbOAaEvuMVSoByFpiPo%2FbIExFgpT7VUkL8bBYRTq4cax4SBm44fzK1E%2FHnlR6DMTpMnDx%2FEhlcz%2FTtvUOEmB9b2tShdrIFgnHSD9xdl8xOtOI6VlA%2BZbJAWSMuyQH2zaR0thWRR9liZqGcT09vaIhxudEspgmrM5Wd7wpclTWE91gl%2BEjGp9RPVBkFubWF8zNmkDcVRGq7U3YqQQyYkzN9qxby5D1kmfWa%2FFUW%2FsIunwV3sSQl9RXiAOj7Y2SbXtfNoUNZdWQpEGsJFAuKzDFt%2FK8BjqkAfFHaF26Xqp0DHuDHoR2Ohu0%2FQK4F5vXi9oC2zkqShh1Xp6aiJnv1qqWJ5i5iJQUOcFUWC52je4NS4Zqv8xsruNfq8ChgNqsIh9fI39HgM8IgQbOumVE8AX3wxQpZqJMgTD1I5ebkE6pqRTUoBrfLvl4fSEZ1zIrJa0xsbIhUWAbtJrge5ooswKM7%2BrhKblppr4VdDJ8%2FanfHwFSX69jnOt2%2BbcV&X-Amz-Signature=25d842dd0db3aa885fdf77b5c4c54505069cf07b247f7c2f835e6c27f2431340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QENRCP7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDB%2BsqkvBd9QcfXF%2FSjE1yZrT0GqXcctKz4t1jv4mUZigIhAImOVTOU8ykACSUERktwgh%2FctC2Py%2FCbdPCe7w%2FNGGYxKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzvt%2Fi8T6iyNzO3zy0q3ANy4K9vu2KaA0kM8JelU%2FvdJtz1Yt5uV%2FxBSvFMeadfmFdjir%2F0smOwhQvsZaXoLiHlftiSQB8ziziFW6hUNF6RfhRGWws%2FI1PGyDtlsLnMKVbAc3NbZe2Y7d1pdkueTF9eJKmf9ZD3e14pG6KKcuiN3u94tJA7JAxjnD8J5E%2BdvbqmHt225qGhZ0r4%2B2FV13%2FfrkF4A%2BCNO%2BvUNdt3FHlZ0tmM5Yxe1EnMKjcVDGs8XjfLOcEQUk9pW22TaowPMB3isP3YQEpOar5dFCyRTTrm17j%2BF3rBct2m3PwgORq9XQVjPI1zYR2XQRPdKxIwpDY5vBwKsfnjJOmF%2Fud6eM3vQ3HQkjNusw7nVedwgJHjGm3CCkao7vYlUzAdCC1XRZpTtXw8R3mDt2YqweOBvShmMgf1yw2cnb2C24sVDmxsxa9cE6RZVIl8z1b%2F00zA%2BXPlMXvJUJ27iEM2r%2BnTb5n5V%2B%2FH4tqMchBC7oExd0jAUxX9EQw7svLn8dv9CeBgjhyOvwnSMHUKHORo6RSWhfH0HdsBqWx30htIL3Izp1g%2FtV4WLjknO3uAUwLYuNFHpYAPEdY59Q88FluSeVEOiPkfqIzUzuq5chhtt6s5rvR1arLZm%2Fjnx%2BG%2B8GU34TCwtvK8BjqkAQZqfq%2Bd4QK1YWQK8jjE%2Frd5P2HzcRZAf0g8yvTQhincHJD18i47GCM8dtRE72N6AkBD2VoONu1oCbJwFL%2FVG1ylKHMQHias74yWAqbyBA0AZKQXWxjVvmccFJmXxa0HX0j7KtoVYxyhHg8VMvEMu7ssxwdbp2sCNakhpbE%2BDtFhx%2B6qRMTk54HXEyNg7WrxMY9DppiJ%2Bm2fFx4XEe7QJCcYFJ0P&X-Amz-Signature=e3b7b878fddb0b4b70b3429304220be3d1c67f422d215da241f269dab8d1a2c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BPCWR66%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFBgMAXY7jCqF1G0wXnjR2i8nt8rM78rnZ28J4Z4gJ8wIhAIrKb2E9tQh2YzJOgsoUqgFExYClpNcR8wKjaBrxyYjdKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztaNb1vCDRsHSlVrwq3APfN1VDcKUXIwy78FGZ3yvx7843IpvjegoOldCKr306C3bpQ8t2F3cjyEqu%2FPbFA4ucjiiprGgth62t7DxCgf6%2Bo7v2QygU50FLMXjXZFyQ21PkzwGtROu9X5mNLnVBAwWnQvIrLkdV2u2FVGccBqTgDr4gE2QYXsbr6cfHY8I5lzL%2B3%2Fb5wiqDLMqF1e9JU1DnVgeBrd%2FYe50W2%2FvtpmPjazkHpR1k72zLxlThI8G7YeT9Z8%2BN6s1vtd1DXnq11wc0ZCN4ULP3W7cYkjM1hPotIy0%2Fk9rXZy5SatAXSnGVCC8GhXmxy3WSmVUHE0CveqrgegOQzVvdSWz2S9oyACwXD34Dq6Fx79J%2Fd06HaidcMoQItHIwF76gjkezH5em3MO7BTj6S0bG%2FUujW1Hn7dHZoUzQv3MkXTh1yl4qNJxV8fObaIRd8xOLM1I73uFnEjD74xJ9mqSC0QfdYCKqoaQVp7QiKTUblD6KDvEakCVZ%2Fw2hgXO3bSqMKBBJU15Xj5pg6sExl%2Bt4zZUjebBQfwjcd2wxZpFELuaKHSqf9JlJgt5yZjZZT4TYYv8EmZmAQF7G92c%2FexmR0cCK3r6wUdg8NC8Y3VFxdiY%2Fl737MBDOWww4e9DI4O4DXSSo%2FTDlt%2FK8BjqkAVUxzfS%2FZ9gPNiWzR0LJRjgM89c31rFpgCMlC6skatLG6nvXIqKp58dRCqUR7aZOWjGAwoqYIFkm4Q85miRIm2DCaGnzdjU3KkVB5jblsGmEcax2089BDmfJlcsfmqEG3Y8DbmojqlvFTY1IGZaYQsd5P8yH3aXwQnRJiqIYbMeCL%2Fy0ckMlVigKFP9VpRjJj7LUD8MovS70TX7EmAP%2BF%2BmRp4mW&X-Amz-Signature=c3ff8ea61bd119de1129464c666c02c0cf3c93e34759b98ad839ec6b557cee0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BPCWR66%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFBgMAXY7jCqF1G0wXnjR2i8nt8rM78rnZ28J4Z4gJ8wIhAIrKb2E9tQh2YzJOgsoUqgFExYClpNcR8wKjaBrxyYjdKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztaNb1vCDRsHSlVrwq3APfN1VDcKUXIwy78FGZ3yvx7843IpvjegoOldCKr306C3bpQ8t2F3cjyEqu%2FPbFA4ucjiiprGgth62t7DxCgf6%2Bo7v2QygU50FLMXjXZFyQ21PkzwGtROu9X5mNLnVBAwWnQvIrLkdV2u2FVGccBqTgDr4gE2QYXsbr6cfHY8I5lzL%2B3%2Fb5wiqDLMqF1e9JU1DnVgeBrd%2FYe50W2%2FvtpmPjazkHpR1k72zLxlThI8G7YeT9Z8%2BN6s1vtd1DXnq11wc0ZCN4ULP3W7cYkjM1hPotIy0%2Fk9rXZy5SatAXSnGVCC8GhXmxy3WSmVUHE0CveqrgegOQzVvdSWz2S9oyACwXD34Dq6Fx79J%2Fd06HaidcMoQItHIwF76gjkezH5em3MO7BTj6S0bG%2FUujW1Hn7dHZoUzQv3MkXTh1yl4qNJxV8fObaIRd8xOLM1I73uFnEjD74xJ9mqSC0QfdYCKqoaQVp7QiKTUblD6KDvEakCVZ%2Fw2hgXO3bSqMKBBJU15Xj5pg6sExl%2Bt4zZUjebBQfwjcd2wxZpFELuaKHSqf9JlJgt5yZjZZT4TYYv8EmZmAQF7G92c%2FexmR0cCK3r6wUdg8NC8Y3VFxdiY%2Fl737MBDOWww4e9DI4O4DXSSo%2FTDlt%2FK8BjqkAVUxzfS%2FZ9gPNiWzR0LJRjgM89c31rFpgCMlC6skatLG6nvXIqKp58dRCqUR7aZOWjGAwoqYIFkm4Q85miRIm2DCaGnzdjU3KkVB5jblsGmEcax2089BDmfJlcsfmqEG3Y8DbmojqlvFTY1IGZaYQsd5P8yH3aXwQnRJiqIYbMeCL%2Fy0ckMlVigKFP9VpRjJj7LUD8MovS70TX7EmAP%2BF%2BmRp4mW&X-Amz-Signature=09a4b2f37f5e98bc36e0a94f89f630884431cbd993199bec2e0a79591117edc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
