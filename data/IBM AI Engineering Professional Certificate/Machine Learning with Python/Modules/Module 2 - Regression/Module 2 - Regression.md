

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=e4c3befb44838546c4c3e0f6561f9d73bd97f240d21edf4298ad4d4cf13bcfc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=9af32536facd5e8385d9a69c1375c7fa2ca62a01c5f5b83cb6d0b953175c4e25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=26bcc5070076e7cb5086a60ca8d734e50b3ec9debf11b41d9d0088a8df8889fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=a0c09672ba9cb0153b1f9167da2e66380cf8e62721eeeafed4096eec203c7169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=7ed9577133116325d10296cee5b1830f5e218fa0dfc39d1e3caae4e91b4136be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=b02a91ff87f4bc0d67aeec6b7495e6367938dbbd1218b7824fa7d47db1ed92e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=a57f03726cdf4c1e9f77387d9ef0ea1f6a03c5646e8c0f5f32c56049a517d3af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CCZE5UX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIAMrDDXIGs7qoz4%2F15%2FAmelJsIYruht2sAe%2FzBUrI1r0AiBuUL4%2BqrCALajQxRjHe73Fkp0ob9mtqzbUiZ6UT6ldrCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMHowzMIjazd%2BOXL4eKtwDxqLze4Y9eZh4mOHt8xDn%2BxgkSE6pLje3FXjqVsO6fXf9%2FgG3ycLPb4w1DA%2BzbVgg6DbdsDDIl6Qd9Hq%2F39bDtJMgKXSnSvxzFNLXZCVlC%2BoatRVpDknvO%2FVELSZAT25DMJbcfpzvc1MQhcU%2FykTUg24robeUDSazkjaTFVrioNZgENiXcMHhKu4kkgNssZmHbviVmjgiaOmPxB1poSXwRUUexxcyl%2BBlsigM2LKsPU8CRckaeaAP0jMLFaOX3mU6xkub2k30%2B20XA%2FAkFDIvbYDzM1xutKbAlt693G8pMy3QFgSyy5VIKBiV9LGw2nE63u9f4iLEmvaenkhYqe0iffaBWtNuLNpXu3eW2FgFhiVFRjPRYKUDg2XL6g09oVJS6TaWIX0ZEwhFMbTd1NNynOBaYAS38Br3jjyLbsGAl5K5B6SoorWyd3Ws15LJb35vGFQwPNeP1Hfvq47rS1bwQ43V9hs8ETjphFn1RrNDRt57LEPYm1quIxhG18tPE4mhifWpBSvVs8NZJK3AJeuyxAo5Jsf1%2Bm3lb7HimmiJA1K%2FbqUvO9%2Bq6AWlSZazN3EJPgOnY1teTZ7m8e3aboOw4wu%2BkIJrMRphm3piYddHcj%2FZlU69ALvHzk0Jpf8wu4WGvQY6pgG7f8%2FTRIj7icPTwJObuoTzsg%2Bx%2FPOgYfkWbYe7QJxvk%2BmGF7xMIWVVnlUNkuzSDc07IhtxMq6hAmtNNyP%2Bcva%2FScO36VSkHAELbOFUNsizmJcvsjc0y7iwLqfIfGseiBaTrlgUFywFlgMduYFqEmsn%2FzmynN7DrjKganPVAft8ot1qCr8esjoMGtDStA3XXvxs9aDYpbh0VjMX2r9rR1eCSm7O%2BIRt&X-Amz-Signature=b45d996f0328733e4786c617f369edb318d5df5b2a2c3ca249877d3c892b4534&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDVOOK2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDAVKtztBeAgTojfRPYRL3mxDN1bhPlo6HZSy7pJ%2BsqUAIhAJY88y1tVkxVw1HE%2FlGSKiEInLSVMa%2BLWB9sJPa6Yo%2FOKv8DCCQQABoMNjM3NDIzMTgzODA1IgwmsT2%2BsaddfEYEqA0q3APgfWGPYLpf2Bll7kY8UR%2BGcnZNGLj46%2Btp66OcDO2ib73Q9gsZ11nkzTp5H8z5PGZai%2BXOw2mEFkJOI5Cpqzpu3WuobeGwTRru5nX1cDbTetDznD%2B2d9K6K%2BsqXjF4FS%2BWI8WBJhiLGv9oO%2BAZfk3hCFbpQbN9yZzfNhAHIvZKeZH7M3zj%2Bwgzhx94lnPpjISMnTgc1ehSiPcCyhleAvLCpODfQU3gauBQseDm%2BPlMIPATre6X5dyT1yWOuew44IoP6GkeSyDVDW8uH9UPOE6bbarxCSou8Elm6PAaG3CPeKm8woFEjYwCe98d0MsmYXjZ%2FED7ovYrGKpegyztjN1MCc%2FqRUMZUF2KyPmMVf4tfTKfjpdXBpEzH%2BO4QNm20UBIPRYCwUUhplisv2J73EOXacIR49LUPhNrZSImabxrTR2HLKnipNEsJKiQrjPIFui9f%2FPzE5PJDPrhH1wwq6GViw78Ik8x2EYcaU%2FP8xLlYTVzo24gNPfhrQvx%2BE1Ti0HqWiULa0j3rCO32U6hHuiqPCxSemLdAZRhg4h45JBilX9G1eg%2FEivuRWFKBvz0ysk7ZUrwSvZMl6W%2BdQyl%2FVmtRpWb0n8Fg4uCvXLLfzX%2BpZSqHUV1mMrUgn7mjTCvhYa9BjqkAROpeRLMVjP8zhvVJwJldPXFs4dKh%2BpuiNuNMUSmTa0DjFlGiNrSTuI84bDdI%2BQQnzLzOLX6E690ML7SNBqjN%2B9Wi9K4CxhhhV2hdDJnO%2BYEO5PpRU7XWA49eBRU11T3kJOug5E%2BNR2KLi6g%2Bdv9ynjCMAYVkywbiDvY6ThK%2FRPnNGUMC3npcI64KcikcMB0DCESxNwYrWGhCFW36HZShZlnQxQV&X-Amz-Signature=48c0e6a66c63fa096566b3e52292d37dfcfc8cd5db4f5574b3432b46f5acb517&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FEYD2UO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIDBLLtJTL1iXdtABrrzj%2FNSXaU3%2BG0WoooZFWpbLCdxQAiB7uOimJqcNdxfDP5MU%2FcpkViV0vxPBb6APVeyOWJ3pYyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIML8cK5RmpEt1ROuIrKtwD64sEqxxulgbd4icTjJLJqpYTYj12JWhNRm9BdFxL9oCgT2VM3XxmZbv%2BmmdEWsvmbrcnketMOj718s%2FEJQ6T93P%2FYoNFj5S2azO1EAkziyRHpWfUPtkFGBRJMpd6%2By6fZVU6swMqurokuaRVqjNSfl21hbm1LStYrAZiP6%2BajV5g7QiaImPco9%2BAYEpR3jcnv4GLwVyo36sM2sAiT0umKqcnBPhq40YGmwdQwwgL4NWawwBj%2FGe6xCBv%2BbHxcN4lBw7q8ABR5yHjZv0Vtr73bgojshIMNJs%2FUZ9jdo5jOjHWO8lh%2FwzWKcda%2BJfQ1MUARpx1WBMw8d6O8BUEwfiVNoxiD8Vv7Ogt%2FiUwUd0qRzRQ3HsCDzQsuMMCAdt3iy7Y9ulesgfyu2OeC7dS%2Fd31Xv6yYLwtmmBmgj7v%2Fz0McpA5XBt3AJ6YWacW%2FwUCtgxi8t3rfMhpwu3RAdiR7NgLSAYxviTmtPfH9Y%2B6H3GRpC1VPeEpaxEh5%2Fwgl6EKkW%2F3g3fgDhaH2aPwS%2BiOBU1MWhEgb8Y40cVrk1A6gDUXrSJ66eT%2BFcxqdvjzD1MeqI%2BvB5Moa%2B7jW4rUj4rWQZqn2JVf4BUunMhFuqZaIUi7IteyH91tcPa6qYTpas4wu4WGvQY6pgE%2FXRc5byyzfTVLC6NxXGQl%2B5hFnW9CkLx8DftS3C1hnxBDOBUiKB2LfN3iWAvsnX2rPOHiqnqztrPoca9psRS4ytR%2Fok4y7wbvqh4CrCxG6JJjeo4%2B96uIOqIR3%2FjjegZCi3C08MXTyyHC1hQU0AbFSGI6KcWs8SqoQskzq9Aalgjfom5SLftm0J8xujDru21km6zy5JyeDbD6udAmnCfWoXQPshIQ&X-Amz-Signature=cf23175f8fd307f94e8bbc413fec6cb1488dbfd27c408e35fc6d4c5d572d63d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFUWT744%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIAWLbxKr4NbGQAopFfHArmYRxLTzFzvBkOyITAT1IV73AiEAv5SYMq5jiAMcAy%2BIcVofdv3xNHNGSmMEV%2BS76pU9zWEq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLxSQgf2xoQxsAMk%2FCrcA9%2B6llVGVWBO77XVKGGrfGkYylx%2Bjr5%2Bv%2BTup445wbyPa1jTJCyPU7FFjlpBQk%2FsZGpBAR5lSn3i9ygRjGHCyG3yvr9X7sWrgaL4JHV0TZbv7RvXhwmZSI%2F6F3GrnH2Z22ciN%2BOgAnSmNIQuENmhSW7uS5I3eHzUG1u8smoz0fjsom%2BPvVFfTZjfiy7rVHB32PiJEpm%2FGzYEO7oA%2FrONVn1HD4wjLRx7tPlVynWqH6jq7ON6I5E0BMgemkwXALalkcjOc%2F%2BT6haK3DsJ4wZdpUo78UUSXJ%2FB02v%2BEb5kNscBsKOl8%2FaAXnuzTKwu8gSU4qI%2B3YAfdTJ4awUAebHgZ315ET%2BUYXnjr9lQJJwCqqyG5F3bZJFoPIe4BcDlts1n%2F7w8zq1yUEfMaE3j4NQI%2F5DmgeVPnbJWvqEnSj0wBRRmFEEztJXjMO7VOC7sJOfq4Sn1CsLAXw42TftHlqm4w4EUOHFLbo5FOF39slK2l4afCEzWzsf4tY0LjWyjUUD9Gl7toDRSxGWgmnN%2F%2FQYWoF46l08OfZcbCKpEDdsEmuZjPT97G2VRRQMwDJCr463ffxuA9W%2BtkmkDc%2BfKc19yax0UOvhJ8kWJSavGHhI8k5wxh30JCm5wIStz1zIMMJaFhr0GOqUBV606BMohcfNqgFV29CbDTRnleL9O5mX1O%2B6naHi2vBD32QRWDxUglfSEsTiEPcr9w06sXROKa0hRZ8w8WTWpdP2gaNYzTdSg8uiRZtz9xLExksmv%2B1XzBj%2FhtEUzZ%2Bpo1xkAPeKh4U%2F%2FNTB3COQV8AWpuJMDKuCMn%2BCNhf%2Bhuzt%2FKbblcLdLkJQetUitHg4ez9UgoOp0OAZ4fNeDxBhHWrUrVrOJ&X-Amz-Signature=64df602f5c04610cd5d5215a536f15c8c2f289c9e84653b62af8da48153a0569&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFUWT744%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIAWLbxKr4NbGQAopFfHArmYRxLTzFzvBkOyITAT1IV73AiEAv5SYMq5jiAMcAy%2BIcVofdv3xNHNGSmMEV%2BS76pU9zWEq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLxSQgf2xoQxsAMk%2FCrcA9%2B6llVGVWBO77XVKGGrfGkYylx%2Bjr5%2Bv%2BTup445wbyPa1jTJCyPU7FFjlpBQk%2FsZGpBAR5lSn3i9ygRjGHCyG3yvr9X7sWrgaL4JHV0TZbv7RvXhwmZSI%2F6F3GrnH2Z22ciN%2BOgAnSmNIQuENmhSW7uS5I3eHzUG1u8smoz0fjsom%2BPvVFfTZjfiy7rVHB32PiJEpm%2FGzYEO7oA%2FrONVn1HD4wjLRx7tPlVynWqH6jq7ON6I5E0BMgemkwXALalkcjOc%2F%2BT6haK3DsJ4wZdpUo78UUSXJ%2FB02v%2BEb5kNscBsKOl8%2FaAXnuzTKwu8gSU4qI%2B3YAfdTJ4awUAebHgZ315ET%2BUYXnjr9lQJJwCqqyG5F3bZJFoPIe4BcDlts1n%2F7w8zq1yUEfMaE3j4NQI%2F5DmgeVPnbJWvqEnSj0wBRRmFEEztJXjMO7VOC7sJOfq4Sn1CsLAXw42TftHlqm4w4EUOHFLbo5FOF39slK2l4afCEzWzsf4tY0LjWyjUUD9Gl7toDRSxGWgmnN%2F%2FQYWoF46l08OfZcbCKpEDdsEmuZjPT97G2VRRQMwDJCr463ffxuA9W%2BtkmkDc%2BfKc19yax0UOvhJ8kWJSavGHhI8k5wxh30JCm5wIStz1zIMMJaFhr0GOqUBV606BMohcfNqgFV29CbDTRnleL9O5mX1O%2B6naHi2vBD32QRWDxUglfSEsTiEPcr9w06sXROKa0hRZ8w8WTWpdP2gaNYzTdSg8uiRZtz9xLExksmv%2B1XzBj%2FhtEUzZ%2Bpo1xkAPeKh4U%2F%2FNTB3COQV8AWpuJMDKuCMn%2BCNhf%2Bhuzt%2FKbblcLdLkJQetUitHg4ez9UgoOp0OAZ4fNeDxBhHWrUrVrOJ&X-Amz-Signature=c04a0d97e42b39a16e76aaa972858710416ad8e416b1f649910b422ba6928b7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
