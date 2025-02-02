

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=a4d6648806ab959851ed28ed1357143f6e311ac69e250e576d5f81d4b44e3286&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=527b5b5a58db2464ec30801325ff593302a7f6f81938e2586a15b8e28df0c6cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=cd8ac41e90468cdc1908e330bab8dfd883d5f77eacb3350f87f197f742aee8d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=36c2bd5dcf569ddf89f3625a62842cd46f66f80bee532a597375940171a9046a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=25822eeb49796751777411c0efdc2a789ae9fd47da4ff843ac2aa0872f3387f3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=ccc7315c2f5cb83b3718d913df06640a9bb7b2fa92d1aa006899d1ed6c897b62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=4a68110d95e6a850f4445b50c30f43f997f903c1c95e15b0efba23ea6e5e1ea2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YXABMTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUFVCBB36TAcyf91C9qKR%2BcDWgyBlNCdPERmSOCLbELAiEA%2FzfkWMrhJT8v0V5TxqLHXkszH2LwUr5%2BMbkzv769aFIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRSAMqWUiuWEeg0WyrcA80nZAAEYdh1Ecpc4Osvnompb9GYj3tGbrD9e%2BgKucNZ%2FsgjTe7p0Y25SeRLe16ZzdL4wWStcvWiKLUi4%2FlGqrRjqoQZyPETHeqdBgjKwiyo6X7pqf4YOw6kj%2FUrDbtCcFQAxWrq1FPV2Dpi70%2F%2BLx685i6imRMz7hPUt5rqMN%2FnkPlhEoSyCMJ8if00pySsBW6GuLcM6cgnwmntX0hLI7ecp9KWVpMem9ooGNQV519d1UDOiNESPtVlUGWxhlGh5wUe9ZueV16nQaed3CxdOPX0tYc1IkrsifOkvYcRST8nX9Ruhng8fuEZOlbAP539A3xnM7cB2YJRtZBGimI6yQmzRQNW33CP7PA3Z%2BphilX3DzjWOJ9fP67DMDKbBZIlEWblbFXkJAaXcU2IvkZDsVBv8vnWZQkOBTwh%2BwEoVydBezXKvqSHeOxIIkuFZHm0GyvwdECxBG%2Bx%2BfORzgoeMhH1xUwUvn%2FG78Q%2Fb2BnwIP%2BEY8itGeq19%2F05foGJ7%2BJ%2BZIQpHZbFE1y%2BFvbctgA8arDvNQkyJyayKyFn3uos5kvcXaupQ4HJ88UeQWBo%2FD8buQ0HhBUzpCBpHEulvnqlr2%2BiIviYDPg6VohrtPAx83jrMT8aB7iDx7mhsJrMN%2B0%2FbwGOqUB0wv83fqkU4jDrnB9ZjerAgK8qmziE0EEc1S8Cw4QUfbvn6xO0%2FVhge2i7fgEADwuJ5dIQIgMh0Ewj43ZJ3o85N7%2FJ3NgQPyakLDJDjMh%2BispFXtmQ0%2Fyx%2Ff7Y9NGUh2%2BMqZyUs6jigctNQyrXiGOhFrupL7yjdacwqhbY3liakBMjr70vhFRWYijgSbBoNmaC1uMP2LL9AKO4KBNu7QFmuZN0vfN&X-Amz-Signature=0a1ab71ab2f3bbc8285cbd0753d60f4dacd7fc6c0132c17889f27cbdd0b5468e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCMYHWCC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2B3lYfeLg5vxt2mvG3m6%2FVkAAuIknMteT%2FJWEyY6J7TAiEAi5sDxkLkE5wYFD8fBtvWUj28lqOSLjZas2snUg3MyhUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBL%2FtTqTJgWC9cYlfircA%2FvOBEyFptPMOBVEq2X00SnIza%2BQ%2BiR2qFMhAu4DpU6i%2Foyqdyj8%2Fgh1f5FAH0GMYBF%2FYmoXTq0RTjUbkE4NHqySN1IRAXymSOZ3xC9ey3DY7SlpIdCcPR8EPBUcb4m%2BHp%2BHYuTYnZQf9UN%2BrEHEJsBnGOuJeXxj57sHc%2B%2FpqIrYlp039IEyA7EOqj2ChQBhyRnKit9SW4vGVuNpwnoMb5l%2F28c1Rynpfmj4kQrmN41K4EKEz%2FRyi1nh68wMKktNzkE1wRbsd9oO6RoM4OYdx9Ru85oAe9wuC95M5es7VOl33H8ZpJYgvj9lViXiAWPltwKevk1cy9psbJ%2BjofOzuHfa2z1f5GBtJrXTxbu4epKLQEkFYTbIE%2FOU4fg2tS1JhFM%2Bk07tn761D83ylLlbheXm2%2F6XPOwPnW%2FYZCFp%2FOrk0wN2dUKXhsFfYqhYjeieTLXbpNTWfWvfoxCYUUCgL2KQi1tjb3UTaZTFcATukIuRjTJ%2FoVOT%2B5R46s9J6LN87d5BUN%2FYEHycAzMIY%2FG7Wg2x02ragh9oSfHldzvQsfb0stYmf0tXqaWCVm9uxJ%2BnwcqFs3aeImQnOUrT3scZeEnjAYEsK61qpWP30AspbdzT1oo9cR2vHdrd66dxMK%2B%2B%2FbwGOqUBsttUGDuiQeaULOmgJqHW59Pd8zP0mY0%2FGls6LaHibROAMlA9MrvkGz3B7FGrAOH31wfTr1YMDOd4tmpZChUagpyem3MYZ0VFyJ%2BcsY8vpw%2Fwqpm%2FMHUunx7O6aVbH2j2APu6QN8wfwIY1bIowvbm%2BAZwJ0xK1KzZhc7d5BGg1%2FSiVFEREp8OoJB%2B08z248GRXDjb%2F6b0D6xFZJp5f8JYvCLxya7O&X-Amz-Signature=cea584f34f5070d42e8c313cf2757567e37236a43e550414e5f1db0d2b5df995&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=9349367a0cc3e232d05d02abd2f1cb5f87b07b43069ae28fd5aceeac6815a445&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMJHRCGQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFUv2mQVXbZYxj90b5r5Yvn6WDQXatbFY6rrrnEBfScAiEArIBHYW6RtR7IitLehgT%2BcjCXdBm3%2BbWH2KliPVRfHRkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCg5GGXpCKynU%2BhhKCrcAxEVHeo9cwWPRfBi4eM%2BiunMgw8%2FXs%2F%2F91rCsYroqBQ%2Ft2g4CMfYMPkCiizx1daXohesaPzVVQ40AqdvCMcqPV2wT0esae1OmsORrfdgfHtVOy4c4z6iuUp%2FwAXBBXOtXdSz3tqj9rJMF9Hl%2FX5WHdxIojD6oI6qO4i1wN29KavbLtlRCYr74e4eRCrYCOrsfIeHRR7kjcqxrnTv99gW5BeH0%2F4K6B1AEwfcb%2B9UGEAmnt21jwhYt0mo%2FJoKLaMLP9NXUAgCPxiSj77t6EW%2FO%2B9uyVgctY85nRobjSV23UDJdTw4jA8a%2Fr5yTMOzuHDn5Ed4jKZ1GMnh5fNTxMWP0q3wqZeVTj64yg0PtaHn5nFEYKV4oe3zOE4gf4FBA3Q3fRFlT5lAbsV3r8npodjTKH0uSsHcuOv2ra9UHiii7et5EmQzw%2BvZPrRlE2hyceN3wr5%2FLxi5YWMZpI3xZ8cGemBP%2BVoLxsBdGB5rn69SgS2KOboZhjON5oW3Qpf9eKtBhbx5PJBkIX8PfI6NOanSL344sIroTQHD1qDrXdiZNEdxICbv%2F6%2BGZwE1S1YoWUan9R%2BV3CAyxGK%2Fg6lupYGrgigsIOtskEINqkQauID7SGvn63WqT9MIAb%2FnIEXSMJu%2B%2FbwGOqUBi%2BTqvvKbyVOmAlwMEvG%2B8kPMmPQodKm9oVabzg%2BzRmLRuMWjsHdFZtdlsZlpXxO9LgzZtW5gKvjxEu68k34ZASQ%2FymqP2tFgStNnuTBUw9OSV5ZmObzBayhRBODnPqXt8bwkjhRYWsUjr6JPg2BL1pXPsTN9mkuJq7Ko86A3BgYEB0tyY%2BIwxJiC8wjVlfjH71U5Ive4rYOMkkp68QUDv9rbimgD&X-Amz-Signature=533cb6be5b68f3e477a96f0993ea4e33f227f8ab29b8685b2e6461c647ac2e7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMJHRCGQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFUv2mQVXbZYxj90b5r5Yvn6WDQXatbFY6rrrnEBfScAiEArIBHYW6RtR7IitLehgT%2BcjCXdBm3%2BbWH2KliPVRfHRkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCg5GGXpCKynU%2BhhKCrcAxEVHeo9cwWPRfBi4eM%2BiunMgw8%2FXs%2F%2F91rCsYroqBQ%2Ft2g4CMfYMPkCiizx1daXohesaPzVVQ40AqdvCMcqPV2wT0esae1OmsORrfdgfHtVOy4c4z6iuUp%2FwAXBBXOtXdSz3tqj9rJMF9Hl%2FX5WHdxIojD6oI6qO4i1wN29KavbLtlRCYr74e4eRCrYCOrsfIeHRR7kjcqxrnTv99gW5BeH0%2F4K6B1AEwfcb%2B9UGEAmnt21jwhYt0mo%2FJoKLaMLP9NXUAgCPxiSj77t6EW%2FO%2B9uyVgctY85nRobjSV23UDJdTw4jA8a%2Fr5yTMOzuHDn5Ed4jKZ1GMnh5fNTxMWP0q3wqZeVTj64yg0PtaHn5nFEYKV4oe3zOE4gf4FBA3Q3fRFlT5lAbsV3r8npodjTKH0uSsHcuOv2ra9UHiii7et5EmQzw%2BvZPrRlE2hyceN3wr5%2FLxi5YWMZpI3xZ8cGemBP%2BVoLxsBdGB5rn69SgS2KOboZhjON5oW3Qpf9eKtBhbx5PJBkIX8PfI6NOanSL344sIroTQHD1qDrXdiZNEdxICbv%2F6%2BGZwE1S1YoWUan9R%2BV3CAyxGK%2Fg6lupYGrgigsIOtskEINqkQauID7SGvn63WqT9MIAb%2FnIEXSMJu%2B%2FbwGOqUBi%2BTqvvKbyVOmAlwMEvG%2B8kPMmPQodKm9oVabzg%2BzRmLRuMWjsHdFZtdlsZlpXxO9LgzZtW5gKvjxEu68k34ZASQ%2FymqP2tFgStNnuTBUw9OSV5ZmObzBayhRBODnPqXt8bwkjhRYWsUjr6JPg2BL1pXPsTN9mkuJq7Ko86A3BgYEB0tyY%2BIwxJiC8wjVlfjH71U5Ive4rYOMkkp68QUDv9rbimgD&X-Amz-Signature=b57f27dd5b4e84a66f7f9b00ca09a1090e326d72290c00606a54c65b994fdb5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
