

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=3d85fa64f9bad95109883c2dc8dd44e03e81d8120c85bffccdcb9621771a29f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=a0b5527f24e174d17df42e20c1f4e27c62da99843f2640dfe552392e40f76b6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=3ff386aac1f7a3a8ade9fa99ec084643feeed7557b4156f56d7d31a377c24bcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=d0e138ed039b67e1b78f3f2720d2d13f7be46eb557539c2f5b68e9ddc03b0a04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=f2a457d03265b736252ceb78e45c74a3526af370aba81d9a38d595ca8cdbb30f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=f60558735e2f9cc06ab52ec3fe108422325d1536b077ebdbff21215f105e8612&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=8b1f051ca9935d68ed064cf35845b807e2d43bf451f0edeba060ba65ed0a5bd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBLE36R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDj5PI15h7LQ1YrzrIzihfEJyYR3MZwnJhK5VNt5eZX%2FAIhAO%2BeXJaVkcHWTkjVqs3WHdzm2PqOR0gYMQvjjaqpMC70Kv8DCEIQABoMNjM3NDIzMTgzODA1IgwJwb01po%2FY7sJR3Sgq3APTiWW5LJYqEB5S0pSU9ccpCcaOEtRLWPVDQux3h2IQA8pcohN3gsN7zxeJ3EU4fgteFqswpB2jEKU%2FnIfoIlQEbRE7yu0BeIFnl4d5SXPvvU%2FeSm82Mq7uPAyqcZ%2BBFTqYudSQGsqU%2B2vAULsr7lIoPwJ8pu5qjfEPQ8O%2FnRwtLhI0oU8hhuMCXH8s6sM0AhhnrOr9AaI%2Fl0Vakhp5rbMPX61FGee08Dp%2BKJcgxtz0sgONp6x6VWxQYIygG10tbzWRK9ku1yQg8KzGJWbvrnBPhZIBa5gvxVkl21totVxmlLKv25upWPxUVRKcSzdj7SZUAOdTdLWAjqPeuN7IXCqxOsUsZL7jeJOQAqNquRJ7sC%2B8qoG%2Fl%2FnRdo%2FsWzozzpHvOeKZirHGAibFBNhpIxfyQ7hPBjHG%2F8hcznHkHqYR%2BDu4Bu%2FAAVm6iHu6aKFC6Wdni%2BlHO1Mzc2z7yfzrUMuekNFx6YK9fafkVVDSlUr2fn1c7wtmg0cXmX%2F2csMT4m376WwfV7UrjIhB4Fm%2FwDjy1x791J9yGxUKOgj9wPROtUGHjdkqWBaNUJjkQowCjlAW2i6dxfIcs35axUZ%2B558wLYhMxESkRo0O21PhYnQIX3XX%2FLpQunbBG6JzZjCC0Iy9BjqkATPoi%2BKIqmDi%2BHnjBAwdUhkeBSMDM4xJS2AU2lUHPsZ5iaOb8LDCkWPxwINsk0pZm%2Frs3IJoVTnUNUP1clESJszxryB5mqaYR%2Fm1c2vGx%2Bwf%2BK1lsGsPnsgwa7dGd5HWNyLF9xoCfSZTyXXvEJnWv6Erq6JRDLyFCdwf5XKTNQSGAX1HWXzkUCWyNxGbZ18qv5xg86PDJDhHBzUHk0bNC4i%2FmTqL&X-Amz-Signature=bec570538dadbca8ce6f28a9168790769600efe6c94e1144f5d40bf61b7f7a8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTF5KTC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCqia3GYMLgK5oLpyDqInd%2BW1rrAqtaFVzoe%2Bt96kJ8JQIhANGh6%2BYY5Z03Eu4IaXysybIRfQR8kdU%2B0TSZ7nwgZsSIKv8DCEIQABoMNjM3NDIzMTgzODA1Igz7KXyVjRLNWT3A99Qq3AN9%2BrQJzOMqubATPsknSHADkonX3H0wN8UXJc3KClf8PXu4zn5VJJyPVrve5miIp3aZleZaiyfjgLv7lhNFHM3zbGAZGPoEnqnJsHH%2BT%2BILMxbqf44OhfbCrAdmqetXZ0xGI1ClgzSqeOhhBQmtbEuEXq4tYX%2BQuvPoXv%2BVdG0eYbI%2FQMZ3SHAfNNZ%2B%2FsS2A3QPpKKVQYnOtMXW9XTKmhWwxLOV79QIT81J%2FKSk2RwljecWLiu2BW3WkyIOrfJExg9dx7PrjqGpTbmWw43wkouYqRyIgOiwOkk8YeQVzLRVV%2F15Lsuq3BUSoG5AYn4vo4XmsGDoTWJyMrXTGhHE7b4mbcf1ajoo3m2NN8qxImJyK5KXInEXIN5gXvzUx0j5%2FAJ%2F53SdtXJYif2%2B712b%2F6%2FNCpE1J45BwNzZn%2F5wCIy9ZY30CzJlsnZaiitqNEV93OQhZXM2PKL%2FOcIDXOSs0Crrk%2Fw%2B0kJBq9xe78N4GpvBDsP9mE9IagT88CQVwDlJnUZhbJMInAt3Vw67iiu6k2M1Q4aWyYpAzmePh2Ja0qNzqPPh1h2ot741YuRfmFO5mwTsjCyCyQCk%2Fp0u83drS8xSSQm7c0LM%2BYGAZ43FY8fauq610wtQxJiIfefzAjC4z4y9BjqkAR9KslylnNwbcLnUd6%2FJP%2BbW7EbnPEzwEWVIE6CCgSFr7Z1GWwhGeCw2dnd3Rgyab2e2LQ9HwEbAYlvdbfyXukPAPX8%2BXPc2rXmTPCP51QYWwF5PL%2FvS3nCLawr3Vcpmv9eT0kFkfIUSkS3buzPxnDr8cgO%2BPoPPrL0y2wmPU2TLn28Jzpt918R%2FMT6vEb4QeByWwp4MOsgqLPlvSMer2FivImsH&X-Amz-Signature=aa0c034b596d07c1b9b84f422561945b4a71215806987d054c2523335e7277c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPGFHUB5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGxXgIQgNeWVJ9yXIr0ncVIKSym4L%2Bm8863fj4lMWEaAAiA3Znz7BVdcvEPqYl5XwnetiPHCardC%2BI5ZIRqmSGodair%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIM2bvgmczIX7bGaJXaKtwD%2BUIWfhXtQim96tohu%2B53E5lAlp4mLQQWzS%2B2tIpT3LqHzV%2F2p6%2BTdN61eh0Nr%2BenoduMwTO%2BjTG5L%2FpJWNH7q9vbE%2FdUm8zy8kcfYlSboiSwx22YmzQFZpeC2QAk53QhzUQFkt8o5zoMgP5A2p8qFVN5qK%2FlsVJ2Nu57wAt6Bi9H0gr4eVYB%2Bssj5gmsYxV74Btr4pUYAZ4YzwKTTeBB83VI3g8qIA9YC1U9XP7R13tQyDaBsn5oSZstGCjPTNDh0FZStAoYtJGJJ7rMXin7py8KamABFJgoVkfmW%2FoYltisJX7yaRjDi9%2FR3hhEkh01IF2e7%2BKntHp5y%2FeFwrU3vRZsB4jJPEWa5nAa0BO2px3Fs3%2B93X366bMkNQCTBlrY9SAx0hQQ%2BZ0S%2FXKSb%2BVyo1a3h86NNvcCpYD39OE8Pcgu4OK403uZqPgrzLgDVHRoVJjC9GUQiKv61PDBZIv09GHmhB5x7s2lrUyQLhsYK3lZKYalpEz9h2RWqbaKnGd1SRxtirN6VAHLZl%2F%2BfCW2HjaL4KHKy%2BdtL%2FWQI7jWgp%2B%2FMz4IZYNK83JN0Zj1lEDY42mN6iXO0rPubQLdvJDyKKwmD1ApYEuSnbhwhF88WjHJ1Nf32eZ%2BNxJbVkYwss%2BMvQY6pgHWI3zdzE1EHx5I9Y%2BSKjh8K%2BnDPfPRfAEcE6s0fgYAXPy%2F2gilcb%2FHoem36mMFmy12DcnEWF%2BwyPQNCdOpbk6Clnc%2FgzuMJMOKVi73Pnc4fkPxkBQ3jr%2FPZE3fZpBZAHxnYSWHpzQCDUaMApiOW%2FHudKe6gRIsJ2dNf82PMHbr8eB9Lmur8ZHmR1NFCBu5uTldJivwGTb08O%2B1IV2jQQqZOAiwDncr&X-Amz-Signature=11754508df43024e351ee08909425722892f977323f218e63a3b235bb9ef155c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WEZCY7M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIFJ9ZpeGDzv7ZHoZedQQL1E%2Br9aDxWWcPEOMyB1UIAvzAiBDq%2BAtM%2BjELBp9Mee5wFymoBBa6tM6TCRCtkAFLksztSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMjmyagJCiqmaW4JYkKtwDYKthUn6vKwBmqPAzcH6vLdBp19kNxnaU%2FBAI2zHG7BskuMW6%2F8JMZMrGvdjkLXLP%2BCDjBH9bQD0J671zGvKfCfVxDgbicel%2Bm6Gzsxnn35mKyqZjOn0Ph%2BD3Klz%2Be3WX%2BrJP88PPzMjehBpGGdP2aLDmsB5IWymwEzkV0UHQIk%2B%2Bq%2Bffe2gl3FsFFYLVoEL%2BwcUDdu0uTalflCLlIkeMOxOpCRDaHIKIyiU9T48yDCiDVnoZRigiBWZaIoCcKoovJoGbf9aC38pB630WHzh8il2nECOYgjMtBdm94zor8SHOa%2Bvp2SZQdigOWd8h6YOIjkjD7gHJJY9D%2FYXw6mI1jAHrNYeErLutwUH2WJEQ0c6F5GMAMRWI7Vc0VI7QveAFMJETzXryCpFFro7wnYFZ0T26PZ1UrU1yMHE%2FjOnPkpunDAlwNbP4MlsqyDaKhD7ljtX%2FdpuWxOkigrLQg2s48UIQqvGiubssKxOAMTvplVHMPms5yUrNnI%2BlH63ocNQRl%2FJKIls%2BtuJdLTJG7Z7qhBF8uVyfB3kMeZd26rj6itfSWC6ZpZNvC5nENANqIydxBMtPaOXNDnaegzWqUI8ZkFMkgMG%2FRp5l8y6ftE%2FvfBozcuRQ%2FbTlxhYjLL4wx8%2BMvQY6pgH9w7OSWWhTL4m02CbMuszZAzbw4GUiZN8safMO4ARR78D03fzbbwyzwUbzTKLe7BCMjMplVB%2BE0et%2F6pS%2FhMOXN%2FdswENbh2RjtqkRkPIS7%2BvLsCLAWk%2BDaqvg2V%2FH8Hn0wJ%2FNzhqGh9FH%2F1sKZysymxx92p%2BcHNaq%2FewN6LX0i02cFm5vc4npWMorN%2BNCsX9pts3bQ2UxS6OzAKleIGY%2BZtE5pXeK&X-Amz-Signature=22cc9fdb3089cd0bdf80202c748cc06653967a52eb64ddeb62ad350641393bed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WEZCY7M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIFJ9ZpeGDzv7ZHoZedQQL1E%2Br9aDxWWcPEOMyB1UIAvzAiBDq%2BAtM%2BjELBp9Mee5wFymoBBa6tM6TCRCtkAFLksztSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMjmyagJCiqmaW4JYkKtwDYKthUn6vKwBmqPAzcH6vLdBp19kNxnaU%2FBAI2zHG7BskuMW6%2F8JMZMrGvdjkLXLP%2BCDjBH9bQD0J671zGvKfCfVxDgbicel%2Bm6Gzsxnn35mKyqZjOn0Ph%2BD3Klz%2Be3WX%2BrJP88PPzMjehBpGGdP2aLDmsB5IWymwEzkV0UHQIk%2B%2Bq%2Bffe2gl3FsFFYLVoEL%2BwcUDdu0uTalflCLlIkeMOxOpCRDaHIKIyiU9T48yDCiDVnoZRigiBWZaIoCcKoovJoGbf9aC38pB630WHzh8il2nECOYgjMtBdm94zor8SHOa%2Bvp2SZQdigOWd8h6YOIjkjD7gHJJY9D%2FYXw6mI1jAHrNYeErLutwUH2WJEQ0c6F5GMAMRWI7Vc0VI7QveAFMJETzXryCpFFro7wnYFZ0T26PZ1UrU1yMHE%2FjOnPkpunDAlwNbP4MlsqyDaKhD7ljtX%2FdpuWxOkigrLQg2s48UIQqvGiubssKxOAMTvplVHMPms5yUrNnI%2BlH63ocNQRl%2FJKIls%2BtuJdLTJG7Z7qhBF8uVyfB3kMeZd26rj6itfSWC6ZpZNvC5nENANqIydxBMtPaOXNDnaegzWqUI8ZkFMkgMG%2FRp5l8y6ftE%2FvfBozcuRQ%2FbTlxhYjLL4wx8%2BMvQY6pgH9w7OSWWhTL4m02CbMuszZAzbw4GUiZN8safMO4ARR78D03fzbbwyzwUbzTKLe7BCMjMplVB%2BE0et%2F6pS%2FhMOXN%2FdswENbh2RjtqkRkPIS7%2BvLsCLAWk%2BDaqvg2V%2FH8Hn0wJ%2FNzhqGh9FH%2F1sKZysymxx92p%2BcHNaq%2FewN6LX0i02cFm5vc4npWMorN%2BNCsX9pts3bQ2UxS6OzAKleIGY%2BZtE5pXeK&X-Amz-Signature=c9b0b8a864535cb03e9f45faed503eaf0b4cafae2bb76679a26c215877417383&X-Amz-SignedHeaders=host&x-id=GetObject)
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
