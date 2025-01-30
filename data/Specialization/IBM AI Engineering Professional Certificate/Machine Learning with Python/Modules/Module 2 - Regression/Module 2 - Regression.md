

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=b2fcfe85600b1e63181d8d598e4dfdaad499d6a3540c1f278e0199f3c6b69a27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=51be29f75a29df8e591e4c81f429412ecde130b2b2100d815ae622b83f35c57f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=73355e0b77455895d531e12aecb64c48c38a7f20e640578e0e5d233af9ffd90a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=bec5efd6c0c49594a498373524e3bb7c3afe820fd29870bca26455668bcc90d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=dc14c29a715236b930386c4dc796d93f2395ab69cbe44812bce4a7ff7596a73c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=4b11248254cc7a7c5cbcad27f38ab70faad7631dd458ed9a3857811075f14460&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=252e487730a57109d77ea19f9a8f4c75c147e2dd1838d1d6d51ec201505587bd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PI4PCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCh5KF3CNqEPLRs1O9oSRiND4lX0ZDvas%2FMVkZiIedkOQIfa1yoe3LZSiBdif0oLv2SIn5vV9beUIXD4JjbmtfPsCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsbXxv1qc%2BgCF9FHXKtwDBa3yTDxjqByZppE%2BRNTr4gUcpHvu1WwOdruTo4CHQwT0s%2BWzhsn6WdWN8RTzl5vt9KSpcI2vMRCv8GZIrWomNV1Amar9VxXOnK%2Fl88FPZESReeZ0wY0h4nuce8xHm5j%2FGQ4PZDh%2Fn41s6FmcL6EwxJ6A1rNUsu84%2FTObrThhVWfFdtE70YfgecbSCiS%2FaPsns5LZCW4RQTx%2BuInH9WZ0jmiTBeqwfG2YhNZebtLompblgGl8drImSWLwyq5a2a2adykwcyG5fW0k8oj76qN7YTXr5zBG6vxi%2FkvDdBY%2F3jPninEENwRCMoWmYpMeLXoihLZAMAAXQqnqRhMAJhuUSkK%2BAqi7%2FLxcu2hSZ56ADGhbx%2F99iju0XQbheZYTo0BqooJ%2F%2BpohxUk0I2XY2XLmwOKkfxhqFqpeGHMrmkQ2slCWXs0u59grtAwIXwbzMPeNAWQuQ5WAKaDwg8Jm8zotOE090Tq4QoP3S5xhRGrUegdcTE3FXCVJow19ibwD9leDrDEu1Aoobdzjd1UL4FO1jd%2Ba94LmjcfET0zPNsloTNcItJr8jdHkblg05N6Pk%2BOL7hnmw7wg4Hk99wBt5hfxDyxD%2BWcU7y4F6vOGeoWp7naUyPZUQm9TtAz3wKEwj4fsvAY6pgHKpSbE1FTSsoJ1yMUWZTfWCVUvWQM91DJSqVqwbb3knHr3%2BPtqFzOU6JTuaFoQPHiN0bYcN9KznvOcu%2BBeRefUZFNMy3S4A3JU6PrY9PQqhnIVOq7ZlumR6JbYhkKwESJYncqTJt1AqrLGvT7zIR%2FmE9dSicKTiUlGYpL0SDCZv%2FnfscZAyFyCV5GDVwNRZ6WOyV7%2BjsJXHVGduwS9hnIX6smSGG%2Bp&X-Amz-Signature=bab3d3f1c13cf7e0ada3219ee57598aa3f2b45878086b29562074f4739bab6e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQVOWY2Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhRb2aUM80ZOdgJf5jH2KIhLFNfdheLFBZ8lz9AOGMpAiAxQHZUMIXn40uHzUiZys3ZZznlVZe7ivvyX6traqzKoiqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCCCJKIFMhiqZmYtCKtwDZ6GgxbpIgUCFxiRlqjAGXn%2BEzpVCs2gda8QaUDnALe9gDuo2gIJrZXYgMZS3Ahg%2BOgFm6HvUg1lq6U27XiGUsS0fktEB7qfrjcq1BYeF6qiNd7%2FOhZjL061SbbSdzTQ%2FlAsxdp%2FnpgnjDPUT99haTJbdH%2BO1FIJZbu8aepE6pY7H5VIWLWtStuzDouTvzo%2FfqZiH48OoVkrLDBdds6kDwFfLSBjdwTGTEQmbyXTMwpWKaX0h2CSkitLo95UCPEbaN0g16Gxk9Uba%2FIADOPatNL9U0WkL%2FHtaxl%2F0hVFa1laQrG%2BtfhpeNnAq8Enqc89jmv6AIghj%2BqfunkCOvQTrV%2FsxGCJHz3vcqxDHdG9kemhm9tu476%2F5Gtv6MS%2F40FtKosj7ccltgqph6ePKp5bCRdjVkbI7JUEq9RuGVCu66Pn9Ub1WrzjeAS0SBClijjQcsvacgy3VLKeGNHlJqgoHg1x7iJcb9tYaqe51K4t62Gar5b7sYl7vtQeNujbW3sdL8fXecZ%2FoK8BjdY3XDL1MeHSv63NUbd%2FfLtudNk3hYilYZpWLOdlGGwJ8ZKA%2FPS8nM8pI8PEsNnunfKQ750mdeOkz31TpXcMc5EiPBvTjIo%2BeXpUH%2Fif5Q5huhw0wmYfsvAY6pgHOQYKy6tiiWgeSVZEA3kPAWgX2VoIMACD7A8EnEP2rEP2XGOyiP5vtDig3lK%2BWOG1AUPgu2tkFE2zzI9zmIY38GfmIk4jW9QcTeD9TO7JejjM6xD2VaD2SWd6Y0463%2BM11NHTvA79Xd0oSM6bQgybWlmKLN0AniIlKx7fPmHPAnFDEEVRzMLu6vKotMmMW7oepWQnsK3ok5tBW4%2B57TCQwmoBnqJ%2Bm&X-Amz-Signature=5b16a5bce2450020c0f41c83e92afd394cfbd8f3656f84e63a2c522405ffff81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UAWMGZZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjwExI%2BLLIaXA8ZK0lV8RifMER%2B%2FsaLDaxAZnWkkcdAiBZkQf4cuopcqKsSAGoqDhHirFHb%2BKqsvMJweqExcahSSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMst8JjyXv8GWpZAcHKtwDu65ZbD99pGhbJVSpgePYzEdjLoz1oQv3avOLK82VA2eiue%2FS9KgA3vOavOSKAzBe%2Fq9jKEf6doZrVpZZKHPez%2BVh%2BY1JgHEfDJ%2B1H4Sv7%2B%2FB7EKrdBD42oc8pPRqvbz%2FaFRqP3Rn05ttFHWaYi5BWJdnFVV6zXWRA9RbJb6A2BSvoWjbnmilAkXAWJpGQJEkKigGT%2F%2F96KvtsQCgj1W%2BRbnqAQo7KrH0ArVeiADvZDBruWSdIA0%2FDwBwCIkyhn%2Fo%2F79ICorhnymCvDw7XRDy8J1pc56n2Pei6IKkOlzKdZP7R4U01O1XPHr6llsksII9ZcLQ9GfUykxJ4y0%2F8in9aL6uax34XQjZUffYH8ELQeg8Vvb%2BkGywttIf1tBxlarNQCrioahIQta36eqNIeBGQ1IQfGjKFci2PT9rK07tFTKR%2FjLTfhjbT1ky9jH7Zpt%2FNPfqf%2FvYTnjloEVOcT500Ig4Rg1bvq8vnGJ2NNspPYT0nXPQSr9laCg16%2F9hVPgFJURC3DvrNJyqqLiexKPgZvwX%2BBHEjVdJFSSbw7pUMwdqe8UTnLNEHgM0wGh%2FHSdHzmTE7YzEkbnk8i2zMhtHRvTjOdtORaksR5EZq%2B%2Bi0qaQHH7M4NNhXfOItIkw9obsvAY6pgF%2BJFHwaYOZ91VQ15f%2BTg5KsBrzUSbpfT8EKR1Q8iYwB%2B10Fu5Z%2B88Q5gJEYIDYJu%2BpezwTFAxBZSTfUJMjOzL%2F8P6jVpnvk7DnLc4BuWjYni%2Fn2FUanIrWs1O36Os2%2B7Bm%2BEYCr%2B%2BaipzTjVXBU8zXnGYL4Txduzb94TW1s2uK7P84C%2FOu671eHITuJdjPuEfSYwJccKk8UfOCVO0PmLdaeOzM4Hfg&X-Amz-Signature=42f3b1e1921450b72e0dbbf962e8cfafee3882e7ac1cb89da993f4a2690c285b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHOC3VB7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAw0PIcBIKzl%2BP3URlO2U8jGSCKo3W2E6%2FJTYIjw573wAiEA3ikJByZf%2FezI6hPwoy5WnT75RQMQgdBp1GLDqDhCV00qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEt4UuKo5vpF7yB7fSrcAwf91%2BBEMATySCd5TzlYR0M7cJ4vduGl1%2FfukCaSAMOSuXbqvrrDI8IhOro%2FAtCBPWfUGSFuHyAGWkaWAMUkNOrVK172MdRggMiBs0EnZLNUGJKI6Y2tug%2FqECxpZcORmr9Mvfb8ogkqd5%2BBKkPP10y3a5edJ8wWCBdJ6CXNLTpELw8Qa9ZYnbesnZZnFABdWF6wO5Cw%2FHzK%2FNEr0%2B0zRdLJ78R9d6kfNOZO1evwVkLA1TQOttZh74MP%2FnYkjCmQFX5LuWzPAOAjO31IMmh3Cx%2BO%2BvloJeXADNQonqiNvZSXCNVZOkLTGBKAGc%2FOZXkPd5K53IWFMUDb2uJZ%2FujcYRzY2Wmk2iK6uRB%2BfUdhL5HbJuXTfQfyyP6I%2BYSsHz2gTyXcupReALIBhAwkKjAvX3dBBtEdFwVXQ8LFHivT7lRT29NPuJv%2F14X4%2FoxJnMrJ5UlSV9nxThKDqZN2T7BWzY0l6eBROidCn0GuZNM6qFWAw9yIX3iGAaJ0KJaeKnRPlbNtC9aF7yXZ4oIRpMzT0ZYFsSyb%2FMincU%2F7WdJEIPWdZu5Yl4kKvvHh3lDO2Dva8GIzFHkQ8X6NXORzfPxfJLMF3fEQYr25CDp4CjJxt%2FpAhbrFBEnMj%2B0f%2BYe9MJuH7LwGOqUBKVte%2BgawKAS51FXVGI2Ny8KXCTRusaCrydJAw596vWdYs7fvo3LJeB6SUgtB6AhU5jUfyl60vJmzQyYXx1h90HjEfQkyhsV0Km4mbYfvcoxBJZ7vew2WeUZ0XrWdDYqQafCirDgJLoB%2F1iSAwUeJ%2BPCF96wWUYkV3n6BGpJz4KilGwKa%2FPT8iHdnM3eDEunqrqeWp4Bpb3VWm0ENtIjfqPtqtFMU&X-Amz-Signature=650b203efcfe0b76c1d4d26e18c1235f128ac3acce606c7fd0ea5160c0b0e59a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHOC3VB7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAw0PIcBIKzl%2BP3URlO2U8jGSCKo3W2E6%2FJTYIjw573wAiEA3ikJByZf%2FezI6hPwoy5WnT75RQMQgdBp1GLDqDhCV00qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEt4UuKo5vpF7yB7fSrcAwf91%2BBEMATySCd5TzlYR0M7cJ4vduGl1%2FfukCaSAMOSuXbqvrrDI8IhOro%2FAtCBPWfUGSFuHyAGWkaWAMUkNOrVK172MdRggMiBs0EnZLNUGJKI6Y2tug%2FqECxpZcORmr9Mvfb8ogkqd5%2BBKkPP10y3a5edJ8wWCBdJ6CXNLTpELw8Qa9ZYnbesnZZnFABdWF6wO5Cw%2FHzK%2FNEr0%2B0zRdLJ78R9d6kfNOZO1evwVkLA1TQOttZh74MP%2FnYkjCmQFX5LuWzPAOAjO31IMmh3Cx%2BO%2BvloJeXADNQonqiNvZSXCNVZOkLTGBKAGc%2FOZXkPd5K53IWFMUDb2uJZ%2FujcYRzY2Wmk2iK6uRB%2BfUdhL5HbJuXTfQfyyP6I%2BYSsHz2gTyXcupReALIBhAwkKjAvX3dBBtEdFwVXQ8LFHivT7lRT29NPuJv%2F14X4%2FoxJnMrJ5UlSV9nxThKDqZN2T7BWzY0l6eBROidCn0GuZNM6qFWAw9yIX3iGAaJ0KJaeKnRPlbNtC9aF7yXZ4oIRpMzT0ZYFsSyb%2FMincU%2F7WdJEIPWdZu5Yl4kKvvHh3lDO2Dva8GIzFHkQ8X6NXORzfPxfJLMF3fEQYr25CDp4CjJxt%2FpAhbrFBEnMj%2B0f%2BYe9MJuH7LwGOqUBKVte%2BgawKAS51FXVGI2Ny8KXCTRusaCrydJAw596vWdYs7fvo3LJeB6SUgtB6AhU5jUfyl60vJmzQyYXx1h90HjEfQkyhsV0Km4mbYfvcoxBJZ7vew2WeUZ0XrWdDYqQafCirDgJLoB%2F1iSAwUeJ%2BPCF96wWUYkV3n6BGpJz4KilGwKa%2FPT8iHdnM3eDEunqrqeWp4Bpb3VWm0ENtIjfqPtqtFMU&X-Amz-Signature=8f64036432fd81e67f65eccf0f1b74a44db6ba376e1ac08cf9037074adacc878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
