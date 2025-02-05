

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=d38c2e0bf0ce3495eeb0578bcb0c5a566fef713f839b1a9e8d36d76f1d509b52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=724acb6c2a40177edeec549f09684b9a0b1d9da2d18cf0c489311b84207b7b42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=3391a701baca7080586670e437e4be22e6bcf3b1a1a144207ad28d34e82faf73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=3b1718679190179dffce1ff28a839e72200a2ebe741552d5589d6646b3e62013&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=99d4dc5d073da8a615ba5e1547c2c8758b375a9455b53df832363c2f93339b66&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=b941e3c5c7fa6d1a6337bed571e612b8e99e1b13c99517c2a58ecdf4ad348c74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=164ce3598052d646b78fff9ffe271f8cb766bb512ba47f9c1e9345e6b801b56f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=78ef04788b1629874dbe11ae7e50bff42013d4c3eee8a413030973d34481b64e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHR2FDBN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQC9ZDjGwBbX5uUCQZHgp%2Bei3LJd4Q8qoTiA4Pfcw7BcIQIhAPED3FXBgh%2B%2BkwXZBaUu0IsOCNpjWz2DALtmtdeInb9JKv8DCEkQABoMNjM3NDIzMTgzODA1Igz1IsvZ9LSm%2BHWz8p4q3APkjj6BG%2B7FDl8TCzfXwM38XHIfChpx8rdiAJaEcBqd%2F%2BFihSxbcbdalRSZpgH5v9cpk%2Bo%2B4%2BT0QokyfW70qUK%2FmensOtuEttSfHSiWsB26fiStv%2FvR8v840W%2BgIgSaEBpbZABdZMPjcDF%2B4hhF9EDxH1Wa%2BNhh0APfKcV%2Bj4lb4kDX0BpO5u6HeNZ6oWxTCWDkhvaW2q5AWGozSao5cITNVG6w7EckRfcrlqVXHIDdQUPhLG%2BSVNDKDIDCZNfHW1%2FSJoJZaWnWxLoFeo2rQf3B4OE%2FqUeIHSTxUc%2BTJ4JOs7cqocnoKo%2BUzbzRaH6kiK8gET6kXvk7%2BDa5bIqiLjmUywlQGfs718AR6UM03ZEREgxa1cB1N9TZlubNs710uAbClzqdOP4CakK5rxqgHRrewlxdypV6Rs1Q33fS1kSXXRVJ9r%2FL%2Bz1FjbHt%2B0auO4WpyffmNFxgwDHcP%2Fvby4O%2F3jsPI93F1LKuC9HdbDepH3PRzOnReZ4%2FgcEGz5FuIAf6WR9rWiYT2%2FFVSlmdGgJGrS4J2COrO2vkQI9mXaxGBS8qDcMZQru6i0VOOpcKrx%2FFyxwNLkS2s%2Ba9exYfXhtKJs74%2B9IEyxVC5Hr%2FeusDQWE%2FAoe3ReO%2BgiWAXzCenY69BjqkATwrgbf%2BcDFWW2E%2BMHTFj3i9X9fI6T9GEdO9SytweT2CmDiMBKfE%2BPCoqNqy5emDCnYy2d%2B8gnA7w3xwRmLBeIK36e%2BTbL7n3g54SpuC9nu6WZF5%2FNqECk%2BXFbtbH1GfpdcbKySur2lb3jPUmQxifEhq1vNVIFiU0sC59VnylURy6Msrtd%2BOOcOkB%2FivDdY8lPX1MWLKPYY59IlH9vTWYkxv1Ems&X-Amz-Signature=abe7341e0e009e4f9424a5fd31d86ed99658d8f2e00f82bef11d9d4a14b1670d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZADYVIKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQDeHb47v7wCuYlxTL1QlSpYzkKBLWF0QeBDbivhvyeEnwIgVHt8lXdV%2BMbMRkhKCVVwr6mP3gfGU%2F3irn%2FqLwE5QiYq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDIhCDO9NguHrL1WplircA9tjycWMpRVIPrb4KwOzvBlaXjSIipY%2FlDAznaXkQUIUETH7Q%2Fy1NYpZ245S8s1MOF%2BenCCBmU%2FqH8Vxwfs7bWaQVUeEUyoCFvvD8PpktbRkxyLzWILlfLBlg2v9j2D%2FK3dzryM4OYT%2FyVYcuYYKQt2TQ5I0sZs%2FBVxD7L6DQg8NrB2jasYTKKpxfCaSxhgaHa82QxTcOOeSE%2BVEm1%2B9fUibLzxQfPIawe622%2Fp1tqIf%2FZIiF4DQ7H2QbvPynPoPyjG813Nfp%2Bvx7SBmth053iCXle4fIk1HYl6B8Y1XUujaH43Fr4fA6%2F7sPTtpSFHgUCXt%2F9RtyikU8cP96p0LDsfd%2F6kE3GQ5LrDSHKS%2BtqbrrrTImXs9TA9brNa%2BVVENcrAK%2BO4Y0yEf7Kk6eMQhuuOhjkEK5Z%2BhLXBkPMIg5SyBBndCUd%2FtfILidhqo2JYHHJVM1rTgnuWETp9CUM8vaXxs4jl%2FVZcAqCA%2F7lIPRGphadEVDW%2BCyTal1SoBAX2yZC5WhYMYp6niEdSNqos6m3tptaaQJFuHE9bj5amkESb6R0Dbsa0G4fQkHo2obM86mOrCr7CewNHPl1Z01XHx7x8HOB%2FCjw2YPTKxBsL%2B8rr84MBMLbwjDoinaJZJMPOAjr0GOqUBNHl72XgRUjupcT9mrwJkYqNBnzb0iKAND%2FsDnqKJl4256lV5LlV%2BPQtcOT2yYf%2FS648yHorxLLkoq3Ueg57RzHI7hgP2Ops1U1xokp%2BXJW0sWYndNk2CPY%2Fdp0ANWWSvCNfGg7NOGaE6%2BB4dBeSRZEZoUzoTvXElBG%2FbJjjTgnCviDPv%2B19pmLvfNY77%2FlUCBNy9pxaMZK0fwEpcNj4YbvrrXcX%2F&X-Amz-Signature=108b6292fa9eabd8e9deeb4b5dabb6fc43a3f4a68d21a5abc1cadc0d925c9268&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JNICS6U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAYtIX4lkNbX6eDRAodtsRkcCGU6nlc0pvS6OrCMShEUAiB06Mfzi%2BBSsAcmrrlpsBtOpklEj4YfxiPq5Vrv0cgsUSr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMY915fD2K7ibtTp8qKtwDN1%2BC2Fi3X5o5ZdEgpD8UsqfJLlDbP9UTYC5XfOBwqGSAp6XFBAN%2FZl23nG3fJbVIdvCqAK9CZ225vkMZBLHj%2FyyO%2BRbKqsp2FZkHBCMDfBQy2QhETVEcCADumRhTFzAMOGmzcHzWJaHUYNmps1oBNDXWJxUOnAloYY7Wi9vgAvOiEWh0yTHriFZxF6amdCAPNXg3zw8G1Sol7EWy20NWbrk3i2P9WNbRZnZlmz0Fz61hR1N%2BIoPEkOHuv5M6SbW9s2M8xCgMo3M4p7bhljdyOSqUx5EL9v1iQVS9RESYUkRMLvVxVpLUbelUxX%2BMVGnu3IaenQzbRKoFX4BD%2F6zhAffOjaigTrm2%2BzWB33WfhaeCCAc240lmxLfV6hTBekNz8635SSzv3GQymreyWkWMJ3laMLVQcPuXMtszYxmk4UhSbrXw61BNiqrljlE9LqMgQBLYeUifA8qlgf2zGc1DEccSIUaT5aAilN5qrfzXr4qg50OpuNM2CoboOcaJhdP7dAECV%2FlrBGBuh%2FrvNVz1a0rEe46EcASUzDkH7XTn549Af9CP1ctqoAKGpOdLTtbnuA4jvTK4U%2BsW6W9tu5LBBqHn69AjrNnqPdCXmML1%2FO74hWMuDECoDHioRpMwzYCOvQY6pgFYVF5CkY2mTVVaY4c%2BeCTqmTan6vk27ZGrzYlQTrK9IpU0d0qVgFHGyT7FmMSU4B7qr30Kvrn%2Biba7xWBdW0PWAzJlNHFZGXYg%2B%2BpJHBU%2BRaUMEPVT0WW0tt3ImOgBmYH7qWnNRuip%2FBennBwqQg07MOQq1qV%2Fq9z3p6suEOuBxhYOcsDkoloweSQMSBx92rw1i5IILQhGuCTgHDhiZt0tyRaz%2BHSo&X-Amz-Signature=93a70283236bfd008fbd1f5fc126b7a76461dea86e627929346feb810666df43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JNICS6U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAYtIX4lkNbX6eDRAodtsRkcCGU6nlc0pvS6OrCMShEUAiB06Mfzi%2BBSsAcmrrlpsBtOpklEj4YfxiPq5Vrv0cgsUSr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMY915fD2K7ibtTp8qKtwDN1%2BC2Fi3X5o5ZdEgpD8UsqfJLlDbP9UTYC5XfOBwqGSAp6XFBAN%2FZl23nG3fJbVIdvCqAK9CZ225vkMZBLHj%2FyyO%2BRbKqsp2FZkHBCMDfBQy2QhETVEcCADumRhTFzAMOGmzcHzWJaHUYNmps1oBNDXWJxUOnAloYY7Wi9vgAvOiEWh0yTHriFZxF6amdCAPNXg3zw8G1Sol7EWy20NWbrk3i2P9WNbRZnZlmz0Fz61hR1N%2BIoPEkOHuv5M6SbW9s2M8xCgMo3M4p7bhljdyOSqUx5EL9v1iQVS9RESYUkRMLvVxVpLUbelUxX%2BMVGnu3IaenQzbRKoFX4BD%2F6zhAffOjaigTrm2%2BzWB33WfhaeCCAc240lmxLfV6hTBekNz8635SSzv3GQymreyWkWMJ3laMLVQcPuXMtszYxmk4UhSbrXw61BNiqrljlE9LqMgQBLYeUifA8qlgf2zGc1DEccSIUaT5aAilN5qrfzXr4qg50OpuNM2CoboOcaJhdP7dAECV%2FlrBGBuh%2FrvNVz1a0rEe46EcASUzDkH7XTn549Af9CP1ctqoAKGpOdLTtbnuA4jvTK4U%2BsW6W9tu5LBBqHn69AjrNnqPdCXmML1%2FO74hWMuDECoDHioRpMwzYCOvQY6pgFYVF5CkY2mTVVaY4c%2BeCTqmTan6vk27ZGrzYlQTrK9IpU0d0qVgFHGyT7FmMSU4B7qr30Kvrn%2Biba7xWBdW0PWAzJlNHFZGXYg%2B%2BpJHBU%2BRaUMEPVT0WW0tt3ImOgBmYH7qWnNRuip%2FBennBwqQg07MOQq1qV%2Fq9z3p6suEOuBxhYOcsDkoloweSQMSBx92rw1i5IILQhGuCTgHDhiZt0tyRaz%2BHSo&X-Amz-Signature=4af155a5e1dc453f3505a64515127475857a4e84b1a01fd8d6863a7fd63ca10b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
