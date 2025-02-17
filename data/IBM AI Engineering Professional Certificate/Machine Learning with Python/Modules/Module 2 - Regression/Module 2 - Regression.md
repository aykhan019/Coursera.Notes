

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=24c2c4ce8bbb88d600ccf0f2bb4c5e49423806de51bb0b8ce1e5cd006c9f8a4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=d39aaae613de343790bc1195238353fd3f284a96db8076f520437823f5b9820c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=d27afac529da3bb0705b095905f7ad4102b90739f5843ff720749f73fe0d7f43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=e867a1a85e5e17778ef20335e4e44616e4bb7dbc65db5f175606dc90a66c7a97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=fb5bf685071bffc260acb61007064f0ffe33cffa708acde67c884bf9f20647d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=9793d20ee1b22e798423c69dc6a7d858f9d02430410874fd523543fc1b9f3c3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=48fa497090387f979e4c24d172cdcd1f760681de43003383195aafb2bd8008b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXHAWAVC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCID418C1WHwQiuP%2FqYcIoWxt%2Bj%2Fn5xvNPc2VDPHG8mYTIAiBu3aGNBiF0Xuhz32a3EHkZqF6yafmiECQpR6Iv2lKq0yr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIM8sIiAz4jd0WRYIkOKtwDnBnkI4R8ZS7EYD%2BIzrFbSZDLA8REnB77PqOVHyVVJwDmVk8kM%2BgwQ6Tsodrfw%2FMA%2FxobbWFmdvxX%2FePGD28%2BA1DmvRHHITJppSrG%2BgjI7sXH6Eej7lCAAKrr4mstnYBzDbYHZfjA3VUvlXL4E7nWpQXSg9Rc6dNLnVpM7h%2Fs23YCaJltN3Qs3e0m3rEvanJH6qcqBB9KDjHrpUYkUzrZmGWVmyWSFCcypbAD%2Be42PAinSn5oUHUrit1bhDsOO%2F7cVeMkk6tDrpxHo3eVIWL2DmbgJ4aQtHxZuJ99yaXgTs%2FtnZYKL6YrZrNbj2FXwD7%2FYsY6MOzBp8w9JafaaLDmzbUaQxeZ2rXq6L%2FfJAzV47gVIenrZpNZ6gS%2B8Ug762v8IYNOd4fdhFAFYBQaGiRfFK1Nd7LsgMQHEIDuweF7KMbzwmDeG4ggX5wm03YOyb%2FClNxkl9s3w2E4gpxDI9ZfOgrrfNYTV0%2F71tBlInDOQ6LbSkpY9avRKnwroWeMgjPOoLB4khAeUii93sAW00POPTdIFb%2FmsnAuUKZ8A27AxwLr3SS4D0ABSQY0QtPG98nq0m3B88kxTuvFyMK9ufTmOkklsIlM4euYA9oyV9E2qWSqLQAAQBQXD5NWO6Qw6OTEvQY6pgG2aTgMTNplcUqN92lMgkCT5BDwq%2Fp6UtC1ju2F1vaeAJuamKR83qzOY9dnf0XcnJLcnS5y84SzgrfnF7%2ByDvDyiqqnBdxf1eMqD155AEyYEdQD03VsZQkDNu690vYhfnX9s5yiRRpKGrIaJevKLucWaWLmkh2CY0Rshgucaz%2Ffpnj1E8MRpwu7hvQgLZ5ORDBYuNdfJo1uP0WhoFYK4LzcHLHQMPoL&X-Amz-Signature=98a62ce6972a80293f4ba91e2e9ff89d4610e35fd227962e110326a811b1c026&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM7MNSV7%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQC1FSTrhmgTsJjl5FirJk5bzUkA9XYS1fGyaWogbQu74QIgThcwNXiKnF62tKzie5yiuYnVFLRAPyoECfQBwLKCrysq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDMT4daJGy2%2BAXRD%2FLCrcA51e9LRz64fzLu8epULJDABoHOrurUOQgtYmDqL6e%2B5dP4zkaheiBfRTSJEvSIBGYbFbXg3vNrCKgQw17aq3ZGIl4IeNlRlYm1AzmoXSRtOSh9OBE9GfggxCVMPy84zPJW8FB4bLL24Qk1Torik8kkYBOZiXhmcCgzMUoKt1eSEsLuodrgG46OBlnOQxu9IaZ5qU3hCcrzM6qJOwYZR2u2FxdHqPJOnkeDbWk0B2FATsUxAs1XzhttPsso31C43%2BjAV1oT7lfRPPTBU9taFqDK3IBhU9mH4ytuJnx3no0bMnsBGTfVrfxoqzZhbNwu9K%2BTTBSyixW%2BB%2FE8jAcq%2B2suk32Hbhr3c%2FSN8LJ2mzzEsOWixhwpM8tMGlbEA6gewbSszWGleqkU%2BsG%2Fa7TDJsuFBU%2Fsl1xKYa8zxRpFT9UN6yPAFYBJklajObFXShhujPTrf7yO2VCVI9TKwe%2F5d3N%2F%2FFKXWErIxROa5rQfwH9KWYocDqswLLiLe7ORQHKgfdM7miJuwMWlknsgjM4tU1oaXoVQcWkHxFiC2C1hf18HOeoLTP1JMT6Nf1cpvNVz1D5RBVuoolqKGCYmzdp31WqINIEFrVSIITsNs%2B5e8DgGBwCivfoIk7uAC35h27MOjkxL0GOqUBssk2gsrdPZMrMGc0IlEkGZJjOjIDvW1dUh2VMlMHYLi%2FHNLWWp7rBzxZaBcDfSfXRpixRxWlhysydHXXLYpXUseUtsLZv5DnWBLyEtqyDgU%2BmjhsvDzp6rKmtYZpqnfEsyifg%2F03Mw4jyHUSS6g4tbS2MtQ8BgMwvfpjPqDXc94DkHKLPdl4QekWdbmO%2BAhC3gqvcZc7xirOLKZ4A7YsnDFfGtoU&X-Amz-Signature=d911c6ba71b80f46aa552d2edc3fc6bb97c44626f9f2dd82ba1f94c0d791f8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6STVDE5%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIDUMRzUcvBpqW1Cs69CEpymNkjrxyp1c%2FosiZNuTiT0wAiAXvPZyTLsprZgVp9cNcxXDOcs5LH8DLLxTI%2BD692X6jir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMP6WFP8CreP%2FuJj2jKtwDztF0pxLJ%2BVUjhwM9s8DlUtUhNGj%2FQNaZn3k4akk7vvWqmAB%2B49r7Rj952x%2F4h7eJC6B2j3bk%2BWcqZ0%2F3oBCzhZ6NjoA4A7%2BHfwzuuWq9YROUTVNihUFcUU%2F2gJQEvlZUUR7XxHKiZ7AngiL1LIe9LZ%2BWkdx%2Fk4OMKlIyu1Q7pMJ2soCOwkXz%2FBWWWHfojJg8LVNdN9uFteOvz6rC0lluoj1O5f%2FG%2BeYVvwpXWfVlFGPCUvzEwCqx8sDcXNVIBwIRd8A1ICr79LPa3LLvtlLePKjLYrNaLsMEm7YzQ7onXM8JcUSv63Aknr%2FuKPfWgiXFmYQ6zKodV3v7p4W%2FHFWBwY%2FNuz6UM9lxewV0qem5O%2B1RsqPmxASyjwiMFzDdKZki2iaUgBHKoU3WA1Z4cjcYbnUTups4x%2Fp6IeQRAmquYRsTtv0NnjyjDkaajORVcz%2FNPXij1WPnRuNw2ncBppKzNyaxhkgCqsTq9U0N%2BDefTw7PT1ytI8NbJqY2niyEsNaogNMvfreptpJk3DhD2t%2Bxn%2BG3Vrq7dmSplY4tUjYLvS5R%2BWPhw8Ys%2FDQBkIxxTLJ77Y4wvUHq9SAiUu2%2FncltV2lqb5Bzx4aXC0rOuTBWbBAZY11dfOERQlB8kB8w6OTEvQY6pgGoYovoSYu2NWxoioGq2vVArt5kWNqmWXucrgXn98%2BRzKN%2B8HDsL75%2FkCt5QCx83pZJW99IXqjBzjbJ7QWtMR873U175YKxNK937YeAxX7q0%2BvAJz8D%2B2wJiJeqmbj75Ird2EMRdcjDzV4dSPTk%2FLmmz7NOFml3Ghg61y0nMJ03l9WOM0NTb13jM8QfgSzHAXM3Cxu0TVY%2B2MEs8yStM%2B%2F0uVmKD7Qo&X-Amz-Signature=d09667159fa3361443ce8605109cf783c43c527b0f2dd9c76fcad734444c5934&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IQWNRLG%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCICMEGLcofQtx0mTiWjjG2SfRmskc5ywF1VMkc7HJJudrAiEArppDPeg%2BI%2FoICmAvkNAAf%2FdFrG%2BcSZ0ZvUxfMUL7WLoq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDGZx%2FWhM09HZElTWIyrcA76NfuMkLlbIJkuIvjHJy5KyHniBeacZDTuemUBwZ6dK1XU6DWE%2FRIy2V3gFxEGuiwaSe%2Bg463uTEnVazyjDp1V66Msnv3%2FIQuoQDE3fuH89AnsyW3ArU4TcolpGTvIGAWIUyvhYnyMRAIQgf5lHh2m9gaVgqUIIoHtu9i9QEAhAhf%2FRMHvukX%2FQPCE0fv%2Fsjv47Ag%2FldL63Aq7H8C1r6SNTlrdp33%2Bp7evpg%2BBVqIsqZTwJcGhhdF88DwE7LmZVxdi3vq5q5qQLU780w77jZPy119Gdj8w8A08Y9qgBSzaXHc61TIHGIRBnGM8lko3mO2E3LTpCsYujOW4YqaHlBbu1ARq5CfS%2BPYRADzLvNepwupcvXEm%2FOPQibpb1g%2F9SRzkPJtqivPe1s91ZN9BGsE5CVyn53NMWvQSvtYxPfm5i4BOdurE8O86sLabKY1l5TclqvdN7ShahvrnihMyyhr%2FcAn0N6o0YekE6nJRt1IVNqQjp4sCDYTQ6WK%2BX%2B%2BFTAv5Q4qfmlP%2F99eRIicVID3Ugz1RpJYbad64qjztC4GiH3OA9FKlVDUlx3eyKgKJVhOTxvXpb8h92KEimPNbIl3RtF4mAcmDQygoefRfNxovNcQoLrQwZWBQsWJLUMPPkxL0GOqUB0CFpDe1N%2FP4VS%2FObwPR5mtk0vA%2FVmW10SkL0wlKLerOtRPQ9xcQZgFgXxmhke3CEJJEdlGLX%2FsM%2FBiUKBYRWVBDKrQvHAmeLuyeUapUqX3amsbWdi8SMRqymSXDPqtbu66Xe%2BPb4TE56dqa8x8e%2BFJh%2Fyqi5I%2BmwFEefObdQoGuTmQJVUsv%2BbyrhUS%2FcqZDhBMlNPzLiJ0CaFZBc%2FfHT1jmGYT%2FY&X-Amz-Signature=3b149cbde9ff1b9a099f57693967a35a67b9fbd3dba942c8f79043b9efe305d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IQWNRLG%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCICMEGLcofQtx0mTiWjjG2SfRmskc5ywF1VMkc7HJJudrAiEArppDPeg%2BI%2FoICmAvkNAAf%2FdFrG%2BcSZ0ZvUxfMUL7WLoq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDGZx%2FWhM09HZElTWIyrcA76NfuMkLlbIJkuIvjHJy5KyHniBeacZDTuemUBwZ6dK1XU6DWE%2FRIy2V3gFxEGuiwaSe%2Bg463uTEnVazyjDp1V66Msnv3%2FIQuoQDE3fuH89AnsyW3ArU4TcolpGTvIGAWIUyvhYnyMRAIQgf5lHh2m9gaVgqUIIoHtu9i9QEAhAhf%2FRMHvukX%2FQPCE0fv%2Fsjv47Ag%2FldL63Aq7H8C1r6SNTlrdp33%2Bp7evpg%2BBVqIsqZTwJcGhhdF88DwE7LmZVxdi3vq5q5qQLU780w77jZPy119Gdj8w8A08Y9qgBSzaXHc61TIHGIRBnGM8lko3mO2E3LTpCsYujOW4YqaHlBbu1ARq5CfS%2BPYRADzLvNepwupcvXEm%2FOPQibpb1g%2F9SRzkPJtqivPe1s91ZN9BGsE5CVyn53NMWvQSvtYxPfm5i4BOdurE8O86sLabKY1l5TclqvdN7ShahvrnihMyyhr%2FcAn0N6o0YekE6nJRt1IVNqQjp4sCDYTQ6WK%2BX%2B%2BFTAv5Q4qfmlP%2F99eRIicVID3Ugz1RpJYbad64qjztC4GiH3OA9FKlVDUlx3eyKgKJVhOTxvXpb8h92KEimPNbIl3RtF4mAcmDQygoefRfNxovNcQoLrQwZWBQsWJLUMPPkxL0GOqUB0CFpDe1N%2FP4VS%2FObwPR5mtk0vA%2FVmW10SkL0wlKLerOtRPQ9xcQZgFgXxmhke3CEJJEdlGLX%2FsM%2FBiUKBYRWVBDKrQvHAmeLuyeUapUqX3amsbWdi8SMRqymSXDPqtbu66Xe%2BPb4TE56dqa8x8e%2BFJh%2Fyqi5I%2BmwFEefObdQoGuTmQJVUsv%2BbyrhUS%2FcqZDhBMlNPzLiJ0CaFZBc%2FfHT1jmGYT%2FY&X-Amz-Signature=b10f171f63a3db0a0f1a361af5e52a30e568805275036a4ddcd19461ea9f31bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
