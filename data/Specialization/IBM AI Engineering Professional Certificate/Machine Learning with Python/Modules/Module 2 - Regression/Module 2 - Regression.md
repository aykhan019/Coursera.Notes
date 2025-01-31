

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=86669399cc588a6f51b1ca9b71a871dffd11d61e87a49ae98ae7f2131d4c6f8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=909bb0423dc5cf797480eb77fc16569d0f60315eedbb48de7480d738a8da2daa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=c1200c16227762c3ba795e77f30faa1c9322a5292024e720c5d18b997ccc68a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=3762d682c334b69f6d0f19e5476eb42a43f981ada6b538196d253e9f8c68aef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=0cc6a178c29e3983c5916200a03e946ae68fcc3c751c7975c268242a5bd4d268&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=90844875e09eeac236075987b820b1308d4bd481baa0ddf4a88437fa79ebe237&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=3cf135bf569e246a9d61cc07362cb84b21d13a30f5931417836e7f655bdc6af5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466666DBY63%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuVUJvid7SA%2F7donxcnuNc5FItcXSkJDhWudjgo3PnaAiBpKr4s7XOMzMVEohR%2FIgNwZegtXYLGFh2w593n0YOFCiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6Q%2BTvYH3Z133g0UHKtwDBHVY5xvuQTodSlN%2FK9pJWDpeP3G1VuXHHZ3bCXbtDyufZ%2BoaGrvn7ppiQrHZIQWTwRQSCUI%2B7Apjd0zvxR33suTVMiukaVxuhxRA9ll%2FlDfAYXedT%2BfaRiM%2FaJxkJgQ45lQpXH%2FstJ2yRlqDblB0B8fQQAp%2BiXzkz6UOryjOkwup%2BSK11a%2BjOoggyoiGzPWSfDZM0hozvnSCh2hZU1ArKIixinncuVmh%2FlYvymBX77QIG6lw1IlSL2ARwJ%2BeiMjDXlr54qOSkH0%2F%2FdHmwStF9VeiSRSxR1t59mRlhr4tTisDdz0i2gHYfYqPxZP5PQS6fkfxIqD%2BxGOHK4lpq9hOf6zQksU3div9pnj%2FpUB6qTgnBaHOW0NXsWn4svXH5IQ0HcsHXlBn73tz131GpCq431eLOV0vh5jstjnYdQa0rZNYvG68O9uY9N071t5aiPPrv%2Bb0HuG46NMMy31QfK%2F9ba7Os3pIqIGlQi%2Bm4OgchCXdk2UoLGw%2B2B5U5oAsH%2FxgHcEtsr83oILD8YDtcrbplMrG387q7nES1nsqluq6Pl%2BjNF2i9C4IsLasvw3qdiB2XHKjz8LOCqe1FZtZk1NyHvEZNz2GwH6Ja0HqcWo9FyQievC5bgfAkV1yd4UwmdDwvAY6pgGm7FKmwYMGtaxUPM8QAGsBkrpmWY5qzPVkjf8e%2FnBCPOooYhd90bnh8RLtcveA%2BieMJhronM4e3jL09jBjeAI%2FarTYOcjmd1Yyo8aekuoNoowbXH9sYGqc7DWfWwqcoL%2BQv4zwv9paRG6eYcm10SXcK8W3TuaJIfvck3ecMUjYWan6LPUxeUQizF0vhjJgJo70auZZLau0BPhNZgNTS1l31We7Q0b%2F&X-Amz-Signature=fc730435633d3300e449962d8269d87daac15551aff3bfe9e9ea5c4d1e015fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHN2RNU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGTyBTYdtlZYYNSrlaYZqP5ZgRiNiB2AGfdm3gVVcNmTAiEAy%2F%2B6OJmIZjwM2oSkTH%2Fi6Uy92t8dNcWvZga7xfMn5osqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGkF0dFfdr5T6mKAvircA8cwJSB7xWskOnXGtTuvzcnwoGiCQXME%2BTbRDQUKEHOY2fRSgNI%2BS9S0waKpTXbytrkMJrzhatHb14I%2BtupKkSiHcQjyBPscGIbtihJP3UfLc6EpDbV7f0mnhtdLyaULGCUX3ZDoDF11N8uoxZNOmc%2FZwT9FzztvEoRK2iuJ8wkFohmlwLUvhGhMpLW8iZO2QDFRKz8SCrdkihfcBqmwb7wp0aEmdQhHXC1Ku69w%2B1Pjv4qLC8l3kwS1RF4bU6339FVzpteL0Adcw%2FiHISDP8LknYkJ1x6vOL7KRDy2kgJSPHTezyAmHG8RZ1eIr%2FwcfEKGLAqug05kFY2WwnsbKfwKUiQcNfsNbkwpq%2FlO9%2BcEkB5FidUP5av5qqqDpktHhhMaEugxeVOf80HCZ4fYzpoZj4FRnjeYCOcNUlkRwPZtxdxachLNEy06BQjohuEXgdWP2LSOPx3eTQEIzHUM5NsyfkcTKTKKVhji2pwpwVk8zSB6ARDRvCHb3STe7P44Ih%2FoDZdufnVB9x6QmimhJleKPLvWdmq%2BRxx8drFKFonVxJrpXsTRYongZu9URSQbuKa5FGbYxzXYG5Nenp5sc6CqBRqJPJzXfSf7ThVZisTzEUpb7w5qK2FyamXGQMI%2FQ8LwGOqUBlImoi%2BeAfe4%2F1zwje8wu%2BFzva%2B%2FbD%2FmoMDdv13qXv2uo1H%2BAie3QYduILLD8rLVjQWTRvNVJD8eMNqHt8P%2Bz5HbSNdGfH6iNaT5QFRsuP9trMYu1clOt1A9yit6BKehuoeUwPzolNz18Eehxxn0f1%2BOk4chKKVkrsixM8cXCx5qxFcbY%2FB33yay1mWgABb2swoyuokg6C1oGf6y%2FsLwbAh1SuID0&X-Amz-Signature=451b8c42533bb999cd88490e31612a82ad2c58d5020332ef62524efd8c2d1281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7MEF3M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnEtv2cse1x04L342LuUDNulRz3Z%2BD%2Fz608qD8vORxRAiBe4taqltW5oMtOVfvc499KN43cSaw2DerEAFUwqCBOnyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1POJQ1h%2FaeKNKWIiKtwD7%2FI4kCN3XvTtRUJE36YPcu8UCs83QEY8F%2FJJHIovci0DTCXC0EbgXT3108wQZOW9vD%2FF9%2BjPFOkZWJwgNdH9jsmf9z%2F9caZsF6EqkVP6IjTPC9Ov9MW1Xdqg0K4CSWd1TOPtetSIyXQroYL%2BKWSRd857VsaPENfue%2BW2jdGih0VaM6M6%2BdnnH2LeMjrHE%2FNoU9r8FYmHe2HD%2FQrtVE2%2BEArMdqiV7IN%2BNw4UBp3g57u3Y9TNpvIHPjr3ee7t1A9RAVPthjjJU71KtTeuWrSsgKJuuqaD5FCL%2FGkZgNewu%2FVSE0aWjZALGFXgwY5BaXbevknL9ZVxKtSc54CvPGYXgCMSImEurQRTWbKx3zHFtkAvicDXlB%2FYvRvHNgvi3GOTh3rOohBoMQg8uq1C%2FvaXeuQoFW8XfGhKpD3YsJz4zCZIdg9smfOBp0moGd5x%2B3PpAxcplKTIwLzq6h9pmRcG6P7fZFBGqkO%2B6dR55T9vDsnIiiHcKs8lFdAnFr%2BGQThJ4Nt1%2FgApwOJFBMD0ZoYNEb85ti%2FpGHM8C0VP5xp1M6NF2A8T%2Fc%2Bs6pc%2FXc0hUOHnnXueQWr7pfL%2BqRveeJZ%2BSNm7m6OMcBS0zpC6wIEWEYUddap6M%2FT6HmuG95IwhdDwvAY6pgEEPsmSx4uFFdA8jbo3moUpISUEzeIg88QGEqc3d6NF3LqeKl1F%2BpDj40uM49ATlMKVjuYjssL%2F41VVHWyAF2CVkmgnikEkd0JXlMsX8T55h%2FMwLNFqU8tPgozuzMqdYCtmkEHMSXbE%2FSiYl5uet6bM0bjpfsmnAo2Lux3n6cA2j5llJg%2BmLJWdCu0Ol5PRJYv2fu6cXWz%2F1gaGp9RTYLbRPTXwcZ2P&X-Amz-Signature=3f465a26bdeeb3ecd90a123e68ef8add79956c0dc877172de117e92dc96dbf35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WVI6IBT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6Bd4o6IkZFlG4vK8bz2iH1iQqkXNxcZi9CUdv2CYzjAIgeB6JEBmEWxwrEg3%2BE%2BGM5NHdddwT3DoA8c49NEk9%2FegqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLgsYnk6j0vEzZM3BCrcA07PuTkJCHTppNRVktleR14gacX83lQEeSx359ednYQ6e%2BEkGxh3k%2FKVf0rPTGK%2BiJp8itxpAdIgRm%2BMStfJoxX%2B3oWahU3liOb5sk8%2BJz%2BxtOXX1ZBBB45crPn64wvLYWnp3ojRiyD%2BKPIquTKaq94%2FXCwr4uS2Mnyvw1Gijl4JmT%2FLI0n5c6h3smi1QtB6jKTh0YZ2g%2BFfiIVb3934KFl4zSw8FjgxojHZIfSNKeKgSupGkPBDqQoABMkgvUQeRAIg6Pzuq94I0zG33q0VMmpQgCP3ArUNPxexVGzIrVOzhXwi67Ii%2FVMMMA8LO%2FLjBxQa2SIV2eOBMfICnufXwPxgfVLfR4PqHeb84uhBDveKyIk5imQjEbnbqsuxGfLnDs3mDGjKqNuKXbtK7hulgLrw0zUTm5%2BDOZ0AbHp42%2FxTwu0EuTkDZf770bnkcfiEjvW0uaLnmfroslufWpk52Dy%2BsKhCtUoX98g7t1N0XUccRv%2BEi5kwQ9R683KsUDTnIhVxSH771CyUi%2FMs%2BF6J9WYog5d8USRnI%2BVoxLxEgZn645KQ2EiTew0Qc4NHtTVjK1XlDEMl0ToPI18cZYyb0a55a91Pg%2FZ0Cg3jNxmnGpmvB8UX1LbzkOVOBDlCMIjQ8LwGOqUBtiye460%2FGas1lK73jBnsDEVkG6H0vG8%2BF5CrT7EZcEssMkFpfXvlrgdZyIPwgTLEW5OXpYOwxPVF%2BE5K7a7wNRQ6m4f2O90Q8RXuPKBs3RPT5BpBwWsiLNFKq1dC199Av%2FW3VgLlx%2BIugWJI8nb4w9XlemV4U0tZVc8OfHxV%2FbzQevMK84ode9nfV04w33JvH60krfobjZ1gtUbwHYASyxDvGO%2FY&X-Amz-Signature=97724d3975348a5624bc68b0edcd7ed22b2986e73ec40163a14836f151e5574c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WVI6IBT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6Bd4o6IkZFlG4vK8bz2iH1iQqkXNxcZi9CUdv2CYzjAIgeB6JEBmEWxwrEg3%2BE%2BGM5NHdddwT3DoA8c49NEk9%2FegqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLgsYnk6j0vEzZM3BCrcA07PuTkJCHTppNRVktleR14gacX83lQEeSx359ednYQ6e%2BEkGxh3k%2FKVf0rPTGK%2BiJp8itxpAdIgRm%2BMStfJoxX%2B3oWahU3liOb5sk8%2BJz%2BxtOXX1ZBBB45crPn64wvLYWnp3ojRiyD%2BKPIquTKaq94%2FXCwr4uS2Mnyvw1Gijl4JmT%2FLI0n5c6h3smi1QtB6jKTh0YZ2g%2BFfiIVb3934KFl4zSw8FjgxojHZIfSNKeKgSupGkPBDqQoABMkgvUQeRAIg6Pzuq94I0zG33q0VMmpQgCP3ArUNPxexVGzIrVOzhXwi67Ii%2FVMMMA8LO%2FLjBxQa2SIV2eOBMfICnufXwPxgfVLfR4PqHeb84uhBDveKyIk5imQjEbnbqsuxGfLnDs3mDGjKqNuKXbtK7hulgLrw0zUTm5%2BDOZ0AbHp42%2FxTwu0EuTkDZf770bnkcfiEjvW0uaLnmfroslufWpk52Dy%2BsKhCtUoX98g7t1N0XUccRv%2BEi5kwQ9R683KsUDTnIhVxSH771CyUi%2FMs%2BF6J9WYog5d8USRnI%2BVoxLxEgZn645KQ2EiTew0Qc4NHtTVjK1XlDEMl0ToPI18cZYyb0a55a91Pg%2FZ0Cg3jNxmnGpmvB8UX1LbzkOVOBDlCMIjQ8LwGOqUBtiye460%2FGas1lK73jBnsDEVkG6H0vG8%2BF5CrT7EZcEssMkFpfXvlrgdZyIPwgTLEW5OXpYOwxPVF%2BE5K7a7wNRQ6m4f2O90Q8RXuPKBs3RPT5BpBwWsiLNFKq1dC199Av%2FW3VgLlx%2BIugWJI8nb4w9XlemV4U0tZVc8OfHxV%2FbzQevMK84ode9nfV04w33JvH60krfobjZ1gtUbwHYASyxDvGO%2FY&X-Amz-Signature=b6185709edc4c74c8eb0ce1c02f2470e8159810817d375439faf7f4fea540568&X-Amz-SignedHeaders=host&x-id=GetObject)
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
