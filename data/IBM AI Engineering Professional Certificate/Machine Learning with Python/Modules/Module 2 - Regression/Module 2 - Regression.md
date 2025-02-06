

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=5f590c032a7e15afba18680211ead4ccae1bf8ee49975fb8450d310ecdf5ee22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=c9d7bc2e05ed794a477552f682970047fa87a5936fcf906ddc261cda2f240291&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=26be33b294290c97b802ddc14e545feec926e21725668317ceb00e5a01344f85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=91d9dbf21539ba0b78cfe332395c812b89d577212d1d39d421a0dc38cf2b04aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=960430eb6b5ff439b9ded7f37da4d09734ae85c3542ab4132fa5a11b7f018ffe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=18ecb098420125cdd00735f6fe7ae1941c8485629d3bc324d57ed67cc89ead27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=9f1ce2f68d902c877bf865a97ee8666defc8d1c81291864a243cd13ea2e091c5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5NUUSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD1OUCbr4bLVFqPKD%2BzLERrMCXub3wBBNQcdYNGjQwr2wIhALeEbwTjKlSUoJV1Jok3Wf8IE1Fjk3UBPAOr63mfGOFAKv8DCFoQABoMNjM3NDIzMTgzODA1IgyQeinI%2FpjKlS3q3fIq3AP9eHcHBZTX45Sp3BAYNRudRvcb7dlbY%2BVXrDRv0zQxUQ8IiTUaX9USPL7pLDov9dnTXceE3vOkaRzCM8lLD%2FmKdNwaVSVHfldf2Oz5Ds9kAp3%2B5ks%2F2qqK91vqN8c0CZ2fzCZ45uYeP6CLLSaeClK618Ui3MH8NeZUY1CUgC4WlGpJZvFvkHPiwMcyeari93FEA0E3FrNusjbhRbc%2FKRnWDEWr0EZ8MZrvcyhEspAuy2fYL1qgCOGGlXgFc1eHG4y2JDaTQu3CGDc5gA4BcnQcFTThLbWMAbFIjDjTQT%2B5WEzfMeFgcHw7zCCGybnJC5muYM5y72jIY%2BAZ1oyaYpoWwBZv26%2Fb%2FpvZBg0V79tKuEblzHNtRHqXlHpIjEqDqwDaQgyL7SnQaBG1YIxyMs2SFtFSO3419cMiAv0Pzm1tKscShLbaJETMpPpT9coKEIFMHgJM0MoXxHUHPyL3G%2BbdtmnZe3QyrDeafrHz8LGnRzog71sCgWt%2FnVcBGwDRTr4%2FJxL3yVr8DPGHwfcssvFkAHXNbHlqUmyxHDagHqXopuZcUGpOKMuRfxLul6oHl%2FaK8trbGsiQtRWmlxZmbi0yGYsER2ng%2F8Bmr49BYk3LBmJMhMiCdHjNRqFf%2FzDa7JG9BjqkAWvxAahUfgt8qNphr6Bl8xbyenkkSJAs%2BjDJqPfFoG4ABvMQVDM47NKc0i5dxRN5EN0W1Bhy0IuW7BF3AIZDkraX%2FkV4Sb5jI%2FQFjONcdpCrdeNaBFfW0K15MXbIUJB6anYnuZ0bdQ3DOwAZk6x559zitOdqXDiayfiYSUwIRAy3k1PgWKhBZA5iaEkvAHHV%2BOEUMxbjInaVYS0ZCjzQrjUpJXDQ&X-Amz-Signature=8532e0ba86dc1596b7b456212761a2421ebb49bd40adf9012a225cfca8ed65ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HZOCLHL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDDmwbCyYrT%2Bx%2F4AZ0Tz67cHhT3kQE2VnoLNcuZFMNcewIgRm4DVKdNzZfH%2FbsO32ToeTEsQdNrIXoakZXW9fFQ4bgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDK3RmztvgGfbBPzVOyrcA5hhOlXOm%2Bq93ZmM2WKPmr7XN6JvQBq12K%2F%2FQnEn47UOWP%2FUt0i2H%2BoLdlCyyWSe4L9jlGYx6Wv2t%2FwMdMUKdCO7YOrU4goxMrIyR3yTW1efOysTepZmZ8XpYD8B69vcaARHSeMzSNeKgrj1PDGqD6RjnLg0HbsEUtnE%2BAYgbSGjIqErFpZG7v4rS51O3C5fIu5vGVxXyYe%2FA3NQeMPwYpZQ%2FcE9TGhgkXyvWguTxEfpCBm9HW78nFvvd0lfmOGUvnZsff2OE9fw262O5Om%2FBlJRbXFu090sgGc6i3J%2B5gCAqhV7%2FVyCHE8W%2Fc9C%2FlMLUpEM1YZWr%2BplxhlFwbK1JNyfN%2FY0oi1HJkQ9ZmAGjA5gpCWQeazv7UvPpQmVbcGFq69ep2GgbaFX75ht6EzBHsAxerqePNNQ%2FB4clLZ%2Fmsq483OFAKXeCyuNFMpN3JJA3hHz70ys60tet%2FHTiqWXk5aWsmItt0UHOKb4v1ElqApqrihHqaZpAobH5rtISCVkJ7PoOx7b5n5xSLPhrpTyL4UYTPfojgOY8CUcdGDMf6KqakNMvjocHdvhTmfFq7%2Bmy%2FW9txMyV8t9iMzbzE7AEsg5zjMgg6Ywh0OmfrkLpSSeUsqkaQS%2Bm5UyPE%2F1MKPskb0GOqUB3cXL%2Bzb9M3xPSfSufruyE%2F2CeBVP4v8athPfNEUWNvrY2ZGkFWZYAs%2FlEwPy%2Bc%2Bx3ovughdnDuqFdK3UbtZ5zEiG1vFjWh%2BW6k7t2WyOwvCvWXyxKacXxCMlh1u6s0JQp6WndB8ahcQRPEXzpNwDyInLddyN3iq4l%2B72q0qvQ7WKjsJKUgVQbBPUkwZOaRulFiElw8eb7QJ3k8O9CSJlp0TvDx2q&X-Amz-Signature=ff892a0386c60897bda4407268bed4426cc467a975a53890266b8f8886662003&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL3FMOO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA4CPK%2F1NRGCNqDLBLVwxvklK3CbAagMjPhH9YwdkaSXAiBP249KL0wauiySvFQ2yFMmVDCq4YAUIzWJc5AlSSnPTSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM6sAeOrBdvCa7OFRgKtwD7GyhYkIYCoozCBSF%2FNnTgWF6MNuUn0dVqOSTdIGd6P%2B0Qg83tKuzuDOGlon35%2B5FC0rMBWUHeDJmMrI3PIhVPN8K9Yi2n4UA5LdFImTYlWLEw6VmcMXYI3prtHiqZaPiBVfIbwbzHVG3u5X7tLweLV7JVueyT1x74b3GNZf6t2QUMAq6gbI7bST9sEtDjzZoQnb8Q6GQ96sNGj8%2BqrJg1S3GOtS2xgot53SCbYh9D%2B9zRPoixifvaIVDccs2H%2F3nZic76b%2BFOnNWOZTuHVZhsBzrvAwau4zfHbuZajtrBAk91M2nDaycGKZqUftCjDDvi70NQ%2FZSRl%2FImtwgY2DjxKcHfapDmPGCWDAbvuACR9u1Ac9NyOGl57aiLTwTBjyj5p4V%2FEADdReMBw36ENyv2FlJks0z6FQC3ff%2BgsKoICVa0Xj3mrPHxHdO8Ac38qZnh26pt3r4pem1rYBmHxv14cI3%2FqgBvyrWc0kNWii%2B1GUpsjJwMb8rlgUCAO2%2BSsPJGH3l47FEvx6x0%2FA0Dz0jm0X%2F4KC3d7SZSoN3OxHzqCpfT5wTk05P%2F4HgrLqqhJEaBKHD4gpAOcK36SgZMuf88P8V7Dp5zgewrwc6zPXkhsOfPk%2BuHAwqi2JeE8wwzeyRvQY6pgHyXTKW4t8qaXCBX2vLrUAI4aHpYDcagtAo2ZO%2FKADLfS2PSj1BfgCyo%2FrSDSaiJEWy9Xfyf5TR%2F%2FFd4o2OwEYMMmTTz5viYyHx3bqSKc3hY3JC4OJ2XGuY19i6m4qwpapQbHWs01DHl%2FLvo5pjmwwxmDMEYIe5%2BUGfyvaLTFe7sBtIMpEU2PhXGCP1SrtvyehyCVZn6CiGZQUs6KcnuwGqLOre87RV&X-Amz-Signature=ac3d8586de9337e2e07365fbc8cb9b2234ce39cc59f7aca7dd655b89024b4b3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z36CASW5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDGGykFAyG8xEytrtKI9FtlVpJupWwyI0B0leitHB1tdgIhAOTrtfaO6UWweBsSDS4z7lswzu6LgHAOCbBj%2BUERkLqWKv8DCFoQABoMNjM3NDIzMTgzODA1IgwtnZliRJUdL63KkKcq3ANHRTcf6yy3UuOpPCKxVDtBg7UCldKYg2CxxygVh7ULIiS0kwyazQz%2BjsyDe9UjYk7WaIlR0h26uxiz0%2Ffxb9B23WZa4x8urlhv9kfRywiv2IyXH0X2HAVQhkB2cTSgPA%2Bhd17uVLNDglZOdKK3aySVuFgR6X3SE1dfUE92m5VXZv5ST5pAohiXiS4avBjyPv1TuCVCmUSXwdsIGd6BvVGTrbkg7Tp6Sl0PN%2BrAi45nTTc2P6cv9%2BFVLT8tsiK8vNdVHJhKUaW%2F00WyDmJ3FW79cvvONfveLrFDUASj5QAxuPn0kHiWlu7uRjQFL8FG24U%2FfyMgLjQutNU3K%2BcJimqQvV45AGss7yzurefCPpqSYGfMj%2FO%2BP%2F48w4MzLCaQV8gLNQa1k%2BZWPBBLDgfMF7pna2hIMa0WU88xROR73QmS%2Baw8%2Bw9Ob9skxP1LiDtq1tbH9uRKCqKYS4MBFWOdCDMB04fTUjyxlO3PsiSzQPwK8oahbpPkirSFc%2BLaqa0wfkSuztBb%2BM7UNJa79Z2UWl%2F4EerrqqHsrPWZOR35NVOGB9wk3Gh4GOBX5lraEm7dUvNvHVgmOCjwbKy38V5V2IfMClz5DN5EFHHA%2FouPXnPErL1G9PuK4IfsrVA2azCg7JG9BjqkAfm8PrxEAYAXaUB%2Bszv7K%2BfjIlI%2FYiblriUyDxvUYpQ7DsjpuSbrEEFP4d4iN7heccnCuUvxSUpqOFffP5H2dtJPYg3AH4TppXp0AzIPMVmgDR%2F8yb%2FYXYTuIAF7SaXFfPlLNNmf9idFfQUME6vhhsvhsvXpKFP1zwX59pcpPabXJGVKenzY3ofnwAM%2FSLM3LMXf6SzoRZoBayZlF7kRM3gi0qgs&X-Amz-Signature=b9ec356bc4d8e68a815c702a783a2417ce5aa398fdaf0d0cabe4e7d749cc3c3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z36CASW5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDGGykFAyG8xEytrtKI9FtlVpJupWwyI0B0leitHB1tdgIhAOTrtfaO6UWweBsSDS4z7lswzu6LgHAOCbBj%2BUERkLqWKv8DCFoQABoMNjM3NDIzMTgzODA1IgwtnZliRJUdL63KkKcq3ANHRTcf6yy3UuOpPCKxVDtBg7UCldKYg2CxxygVh7ULIiS0kwyazQz%2BjsyDe9UjYk7WaIlR0h26uxiz0%2Ffxb9B23WZa4x8urlhv9kfRywiv2IyXH0X2HAVQhkB2cTSgPA%2Bhd17uVLNDglZOdKK3aySVuFgR6X3SE1dfUE92m5VXZv5ST5pAohiXiS4avBjyPv1TuCVCmUSXwdsIGd6BvVGTrbkg7Tp6Sl0PN%2BrAi45nTTc2P6cv9%2BFVLT8tsiK8vNdVHJhKUaW%2F00WyDmJ3FW79cvvONfveLrFDUASj5QAxuPn0kHiWlu7uRjQFL8FG24U%2FfyMgLjQutNU3K%2BcJimqQvV45AGss7yzurefCPpqSYGfMj%2FO%2BP%2F48w4MzLCaQV8gLNQa1k%2BZWPBBLDgfMF7pna2hIMa0WU88xROR73QmS%2Baw8%2Bw9Ob9skxP1LiDtq1tbH9uRKCqKYS4MBFWOdCDMB04fTUjyxlO3PsiSzQPwK8oahbpPkirSFc%2BLaqa0wfkSuztBb%2BM7UNJa79Z2UWl%2F4EerrqqHsrPWZOR35NVOGB9wk3Gh4GOBX5lraEm7dUvNvHVgmOCjwbKy38V5V2IfMClz5DN5EFHHA%2FouPXnPErL1G9PuK4IfsrVA2azCg7JG9BjqkAfm8PrxEAYAXaUB%2Bszv7K%2BfjIlI%2FYiblriUyDxvUYpQ7DsjpuSbrEEFP4d4iN7heccnCuUvxSUpqOFffP5H2dtJPYg3AH4TppXp0AzIPMVmgDR%2F8yb%2FYXYTuIAF7SaXFfPlLNNmf9idFfQUME6vhhsvhsvXpKFP1zwX59pcpPabXJGVKenzY3ofnwAM%2FSLM3LMXf6SzoRZoBayZlF7kRM3gi0qgs&X-Amz-Signature=eafb790e1b7dcc1b23bc7c73b931fc313f825df99fcfc5f1881771714cbbe3c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
