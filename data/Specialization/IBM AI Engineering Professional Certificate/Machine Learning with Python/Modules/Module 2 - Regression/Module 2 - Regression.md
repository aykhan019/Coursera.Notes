

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=838c4a52c0cc98f110362691b04d85791ae11ca0c48157322c47b7d8a4668630&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=016ef7fc65cf9d4ac3a4cf50067f557dc24a39b933330378a2b8bd920a2f4fdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=4ae417b7ca559955fbea1f17e9604f871a60afc465170140131057b849b5ad72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=2fb1951c3772fc0c859fed29d2b0f0cba6cda5378b774e226418dfd4141b3919&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=39fc984bb11481e043100793c4d919eed09cb9e1fb75652e855975c4f0dd52eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=c20f6194dca16b4f3f9c185963260c620a6bf7aff4e9e85d1a5f1b372ce87696&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=3029d06b180c3fc5335e05398d18075b2a180399227759139071e79b5d7113b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVJSUSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2SHTf8k72UZnZ%2BDtn9gex6m6nN2YMAaXftA0ncMGNeAiEAyjbqeEDU7C14FyHx97f0bfR%2F5%2BPMjwa4udMLJA5oF58qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn%2FlZeik5gKx%2F0igircA1hzeHTnLN0UmH0SST%2Fd%2FoxEt7szQedtnMrHBnod3ToBq3FS1ndtmi%2B%2Fl5bYze5ExeazL9o0X6EwLvHIudsGLzIOjRbOaewdUeFqtd5Fv%2Fg2RBhAxAFnLdVg2c%2Bq7W%2Bfxz237Ln8md6xMf9DKG4y20FG1qt5ClWt6UARESGhTdcyZqJ1VqLu8%2BXPpleVQRVNJw05c828hTFxMSK7o24f1jzLAK6MLh1vjTSvNvMawbwGB1zt4gwD7%2BYO1zwwoqa%2BRbJv07HTWV%2FIZL8VUSFZBPxpGjrRBoi2Cw%2B9nCkKzOsknsA9wuhWaiUyNCg%2F2WFEoA1UH9TOjj7YegFfNA1HOQICXYcyam1Vq0aYA6anqJX3tlmctYpv3Kq7BAiHSLdoPc%2FVb%2FBnSJEfN%2BN0LUN75P1q28mb5HJPwO1D%2BHvaGUWZe9yF2np55WpAoXc8CExGApsxdzzVDIpFVeY9ncXYPvdy6NALqsa5Itt1Rpxwfpe32rcZbX5UER9%2F4nkBdjNgAZPY8yxY7QcLdAbEPehURgI4n7dbLpVAfr4nnRWbaz3HAxKucPUSNYwnAND4pNPn%2FREZl%2BFFXYD84U20iQHGSYiudIuV0XDVpgcX9R1kPi8tjzlyfAQF7xNRzoPOMM%2FL6LwGOqUByn3LvxcN7JuznUICKG41ofNBkmzsrQ0rTF%2B%2FHcBz%2Fepk7uxWrirNp5KWUJlKRWJPKwZEPaCXeZk5eMnSHYInDApQq3DlgXsCv9nk5DKAU%2FR52GLxNrqXc3NyLe5lYSQg3HPIhwucryo2LJPF%2Fnh0rlMiUXHVFusn0g6VZDKCpQgMH4yEXSa%2FuAO4ocEbsPnowGjvM9AjkEuVNnkNjY4Hfgg0q8bY&X-Amz-Signature=aa32b77595fb186be4f0958004b18f6673a58ec8c5cc6ec474f5d05f9ddbf53b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFOTFOLO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1ai%2F7UTJhfOysqwatu0m5M9gGM72h3TdXiT6g0iHjXQIgAu66IAqWLA7cZGj%2BGDLewko%2FDJ4mNafwsXpuOUj2f0gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAEtwNS3CC9glsqQSrcA3a1knPhvjJOOFESKM20ypBS13IJ30u4m0zGg8heZPoX9lWHhmnckWMno3XsQiHQrrrUlJIAJBOMwRb5DxXBBWYNXzKhb%2F2X3aRxz7nktYPlNrKZDjNLc9ZB5eGd8GG1dXO9ndtp6F4Hn3xHTeRsv7OwbGp7vFCKUKnWgmE9N5nLpGmOMwOarbR%2FWuacvgkEXRSEH2bLQMvQNVDRTaCH8JO2FeGgviM7Rkid0WzyQ%2FaUzDPv7GYE4GnlHrAGge65atYBNpRmH4%2B7eMjOaIr4LggSMaGVu%2BGenUARqk6yIpP5tBKBr7LM5TINLDbR0X8ICkAGQOGtO1TJywSC1p73kPrN4qOHMz6263uFUU6Iyx74yAx1TFPvQRw8Lkd%2F%2BSd6dCbk1DjwJuVDx1kZiZX6iuEGMjxjuDbALxV89qtKNLuhIYhqyFHzCF2Mql4JdtZaBq4rNmk%2FIhY%2BB9HG8bJXwS1K3Q5ohgHvS8NfpTtTjWKMvU5EshWCzls%2BLpXC3SzpmlbXaphXgR%2BJiuoXiYi6yEyPoyxkcWOhBim1Hm0wvo3jU%2BOn3zFmPuHJGnXv3T6NzMRxp8paLeVCNKYHya%2BuHtGWXTBBjaNkbyvH6xLW3cURQzpxt6gtT%2BD7ftNOMJHL6LwGOqUBjqDkmJ2q50dMhOVbbhfKpGpGp8r4KFYuLdOuVR03mJsBwKLWF9NoWVvC%2FD91nfduGnrt%2F36bQdbINu3NSFkE7uLqII6%2BepwR41FybwXMzXqRjKwJ%2FRh5z2McWdIDjndAuveVz%2BVtDKwYP0941LNb7f4OyPiy3oi%2FWQDrnpYzejVM2aNWQjuVnJoSASdGyGDE6SGbflZ3iBeXsPIRsL1lrkhWPYv0&X-Amz-Signature=35d31c649f81ad25bba65aceea6d25ae060fce3971f8bf9072a4353bd01c4a14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRRSHHA6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHrLl6t%2FvontWFJEfgT8qy4CNkg%2Fn5YYiBSLtvHQbQ%2FgIhAIhY9IJCJCS5BYEnxzUyyX0IyVH1LofVlgyFF8my9AdkKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsY%2Fq76nKIOlStLdIq3AOlKqxY6OdR8uI8pBUX6A2U9tXnc%2F9U273DxeefiMfrbNJzQ%2FDaCg7mzjyytiZtbheHAeD9dhcHbJfvhFAsvX0m8WxqBbikSA2e5yvR3m6QnaSXoiq4DY6oxfsS7SuqrqSm8tGaVN%2FGnjZsemcUZj%2BQ7bDInTbVFGVt0qxcgUqpMK4a4mIl6HsYxW7XP130%2BNq16iS8U3H6Vfj0hHlXMLoHDLB1bVlZlHWGBa5OvKeKJFbT%2BMbRG2IXgJxGRRxEpbAl3IdjDy%2FZOCNTm94IvEVd3J%2F2RaXlM%2Bmhx4KiaYQVCN4ggAGIIFE3hoxMFomDTKawtiEWNkuLCINb1HcNnMCU1XKtmOfMm7AVAWKerTetifYa6JY6%2FYC2UfNN5ZkWbwpVr41BH08NQ1%2FfB9HCJiheWDYQ8tP6BcT70utqXuKGhTMN5z4YF4ID%2F82Il5tH62Y9JLoRbT1AyaZwgfGX%2Fwh06Ih%2BZ%2BkKgmdaHckdNBw6mdXBCOc20P%2BFa12KFoOsYhe4dbDAgao5o0uPcMyJK006MkGRkfvUIqTV2UQbk0XqLVap%2BO0o1vNJAfJRz%2FmZiw7PSb5NEUI3L1dLbmDoW7BzIMT2pQlG0MImwYCFiucr9tgs3bcVbDwfeirBSDC7y%2Bi8BjqkAUIIOsgLadT8S3Yw2dVVwusbWtp%2BkgAxpuB735PItVaJY1uJ1McWuvc5gqH%2FJp8%2BEY7HzsgAIkraZhD3z0xdh5ohHn%2Fij8Nb%2FxkRFGup7ptl0wEhgREjzhlx1LxLz8Mp1kxxI3MVu0rX09YOO73iIP0wU28%2BcpWFa9x2FYi2BTU5Q6ab3kowTMhpaFehwaYiWzJhcBBd9JNIiiS0M1UIIBS6esez&X-Amz-Signature=d14165e8708cfeb08916c66aef8c9dbc2c866a23c963e3f3ee06597ec8395020&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIWKF26M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAP7xU%2BuMZu3%2FJmXTSADabTDcQfymX7d8SbClvFaL0s9AiEAl67eyPcjq%2B2dorRHmfT4OwbqrEahrBLvpwwO%2FqqSQzYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3xYaLlKrXHHDg%2FpCrcA9c8LgNex3XnYyqeS3MChRjD55LRELzajK81zyCeTFtNDDF0xD62uoEwEgU6jMcmUU%2BmqbEJNDAZcBSD6r9wZXowTWdJTpnGjpzjO5tQcJtKTX145dE9VusYoJj4jZ3%2BwpKEV1glZQTvBn2cqwsKEKqO1zQkSQuf7L4AILwC9RPuRMbXtv6mgymvxigZMcppwdtZ4nfBst5MShGFM%2FcABcDMfWtA6nKOvlD%2For%2FDQj9rjuwhFgcK6D2fpgVyO5ZfTpC7rhOgwe6bT66gvWwGvzk51pbr0OdX9p59kBqXNm854j45Cz6dAG3TJI%2F034lSdzDacQoV09SqcCo2omPAFWuqRT6%2Bo%2F%2FiQ1q2eMQ5nx5Br4LLKxuOlJRanQWOK3cNaDnc4nQvH6QeE3AJeEUJda6zMZTi1mT1%2B59KqQhUQZ%2BBgOQ4m2mxplasA9WX%2BEXO2IapH6oQ4IIOauzD9%2FEIRF2X8BllOeE2EmvhQ7jLD5ny%2BDd05hG8sGoQ35soNbwwnkXlmT%2BdwXiB8shZQ241GfGz8Q6yZucPVUqY%2Fxs6jOlA62UUKHCE%2BOldf%2F5AoM09X8PYOpBUyaEq4UYsduQVjKgMU%2FELjbrQW2dKfYaN2p9GagTto9Ay6UBTbYHLMN%2FL6LwGOqUBWgKBb7t8ZCLMiIeTqGAFHOS0MBxF44lynZqsi87yyXbYRdxg1aZYShrmfPVjPrUuDKzMoxAADKScpSb2F9OarpD1i1O14Bl%2FP6TxQ0GHbq9cQRDBr8tVuqqD7%2BfGftF1gp6OADPL9uwX0ymuWIfAsvaoGyM%2BFJx6ZGpvE9IHCavQW%2BHrcLJY5JLYzqv1FNHFS%2F1E0bpMNi0lTwsWA4st72wUJMey&X-Amz-Signature=f894642d8dec9f57f9ab81ef18e0042c3c04e3371d04e3beaa320a1890a1153f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIWKF26M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAP7xU%2BuMZu3%2FJmXTSADabTDcQfymX7d8SbClvFaL0s9AiEAl67eyPcjq%2B2dorRHmfT4OwbqrEahrBLvpwwO%2FqqSQzYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3xYaLlKrXHHDg%2FpCrcA9c8LgNex3XnYyqeS3MChRjD55LRELzajK81zyCeTFtNDDF0xD62uoEwEgU6jMcmUU%2BmqbEJNDAZcBSD6r9wZXowTWdJTpnGjpzjO5tQcJtKTX145dE9VusYoJj4jZ3%2BwpKEV1glZQTvBn2cqwsKEKqO1zQkSQuf7L4AILwC9RPuRMbXtv6mgymvxigZMcppwdtZ4nfBst5MShGFM%2FcABcDMfWtA6nKOvlD%2For%2FDQj9rjuwhFgcK6D2fpgVyO5ZfTpC7rhOgwe6bT66gvWwGvzk51pbr0OdX9p59kBqXNm854j45Cz6dAG3TJI%2F034lSdzDacQoV09SqcCo2omPAFWuqRT6%2Bo%2F%2FiQ1q2eMQ5nx5Br4LLKxuOlJRanQWOK3cNaDnc4nQvH6QeE3AJeEUJda6zMZTi1mT1%2B59KqQhUQZ%2BBgOQ4m2mxplasA9WX%2BEXO2IapH6oQ4IIOauzD9%2FEIRF2X8BllOeE2EmvhQ7jLD5ny%2BDd05hG8sGoQ35soNbwwnkXlmT%2BdwXiB8shZQ241GfGz8Q6yZucPVUqY%2Fxs6jOlA62UUKHCE%2BOldf%2F5AoM09X8PYOpBUyaEq4UYsduQVjKgMU%2FELjbrQW2dKfYaN2p9GagTto9Ay6UBTbYHLMN%2FL6LwGOqUBWgKBb7t8ZCLMiIeTqGAFHOS0MBxF44lynZqsi87yyXbYRdxg1aZYShrmfPVjPrUuDKzMoxAADKScpSb2F9OarpD1i1O14Bl%2FP6TxQ0GHbq9cQRDBr8tVuqqD7%2BfGftF1gp6OADPL9uwX0ymuWIfAsvaoGyM%2BFJx6ZGpvE9IHCavQW%2BHrcLJY5JLYzqv1FNHFS%2F1E0bpMNi0lTwsWA4st72wUJMey&X-Amz-Signature=b530a90b0a4596edac0229245bb2f3659f9803913679f38d9835465b521631d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
