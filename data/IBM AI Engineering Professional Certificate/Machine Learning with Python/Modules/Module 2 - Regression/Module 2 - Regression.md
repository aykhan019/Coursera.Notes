

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=d27af5a87d0a9cec74d678c78f83c89868bf17985b14619f4255564c0472908d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=37196003f69d59de232e0747c932476d025171cc8eaa5838fe6fc7fc60be4097&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=d77f3bddf09c89dd4d42ae6e38292243f3b13cb47fe061c33b78507796111d3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=5077439065a02964afe44469852605ecb95926fc46cd37dcda8a6e0dc2dc524b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=01fb028dc7baac4efe66366f560e2fc7841067bfa46115a1246a0f761832b396&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=08cf195dbf92490aaaf4f194239630dcb59e46b09c6cfa2585748f15b4162675&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=2c3362d14e46a481739b7bf3942dae4c251bbbfcad9ff6f44198b53dc1c1cdfa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CMROQIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIEUGjum5kyKNwAty6hubzEUqn%2Fr4vLYGH9%2BDqOfOsUpvAiEAieebR85vyV6mxOYVDzMT7Fdp1pZJOProlgc5Su7l1Dcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPbJOSafiM1vgYTpMircA0KTFun9DijfE2Hs0cDENn%2BQu9yzuNBryUuhSAvjXncTS%2FUvUxDw%2BVKwQRBe9D9wIPS%2Fo5uEtvio53KNKvTu%2BsllxwMZ2GOqkmXx%2Fw8QNClngSvgHbzdVZHRXSfl4GiIkDjBjB4rCjtjkq2pfWqpnyjjtnLFk9V8YSmXh%2BA1xvgU73WHE4hOils1X0CYLMXEOyZl6GVb3tHrCx2SiQo1yqOxgoGIl%2BZt7mMP0aL7Xf55hkETnCxU5fh6mMu51GEhTQCW9mD%2BImODfB79ioH0kbZG1Lo8Z5IIDi2mdPLVUn8YJbzZYnCrORDKwnYKcjISATLmBYVgi1W2fi5IcQtzwOLop0%2BrK81zZs2GOGxxctPgYGYTk6r8TV%2BTOCva%2FiOj09%2BIr4ouTmtY52qXwD8ynTJSTuvp1ATOnwmhuuGxWl3bcwMc3c%2FkxBnJB%2BE8u1790lXEYWz%2BWm6DhROTw%2BpIrF5PgwQ9Jl%2FwtYbdN3%2By51yNIr8Ohuq%2FSy6RfPxtKYoWt2mqjTaaEsbkm5Pptc3JOVQWcxSyMe2lWjOTQpq3XFUeoOYw8H3NUurtBDfZEjgAHofY5Pc0AKtUUbxJUR0o7rRIYpssXw23k5LyzaU0abDM4qCkep9HJvIVfGcBMJqalb0GOqUBW1JdldDpiNxhsg%2Fwh4vdpB4RzcYqb2l0eiwLsDFMLKzxJvBKVL%2BycSPKg8Dtd6D5jegnGm6XTzIbqegwwQ%2F0WGNVebgjRwvrdLDSQw23odM5owiFB8ExEWb%2Fipbg38wryVxYAiWEFH5uZ1ZaZzjF6B1Szch4G8a61AWpvnUGeWBIvoAyPvGpzUr2wOuV2sZ85Wmv1TFlvJENZu8aNKMgR208Mrup&X-Amz-Signature=0471c4d54b4ed2116535cb5a1ff98cda722fa46779e2d6aa346bbffc20b4daed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNLZ5XHF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHX8bxS8SrRbaJy3lrzwW%2FGY9fe%2FZ0Aewd%2B0Tu6kb5pxAiAppkd5eaJ39ecgsPe5VLpsJoeddIWT2pEywuyrxstdzyr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMYno6vURWhzwtB4wlKtwD7gs85EfpJdl%2BaEqDI7KIYcm95SoVsT6ZJ0AU1F0CVeB7a5qEffRu1tVX6yXdNQnoRBkaxIu3Kue5O1DS8sBWBI3xAbJIqr5R4BR%2FX9QJPMQj2%2FrB18%2Fdew6SzWodH2QGWJP1bH%2BOXCUNmX0w1WhKjOJI6YAHS%2FDsFiwQg0JMki6uzMDGRXN7iMkwKkJ9WQtacRklSLTmjJ5eF59BKb3c4Xq6QZqbkvnx3Y%2BFrYsRWNEmGX99yPkBbyaNoHZvqw9TdByXuARskBrJnLrsJfvMrXHOovtoIV%2Fm5Lwdk7ixliO5DHAI0x2AB25vJ%2Bgs4zEakqH%2B%2B79wxOmHu0Bw%2Fx5TMXljABXX3odMXcW8UhM1aDZqs3I8tl5TTch15Sia9NAO5PwVSmsX0UqZ6zH20%2FuLa%2FbQZoXYIjO7Lxcx%2FM4Xct3sVjDTG1cDPA9R1g46GE%2BflPzT4BlJT3iXzyCBA7P1F2u5d4l0sT8JDQ%2BtCzwSWxVgjecnatwUL%2BcFobpsJDiUPzDtXzrWGOcJ3cZ4SkG5GLl1GFM070pwtpksnuWRGkg2uKPt53yJIojhJjxSC8RGc7u2DYYhXzG7N3Pkt7Ou5IX3YeSItiM6UAjZGBrNrFfXg%2F%2Fs6D0VKtpnTwMwkJqVvQY6pgEubqFqgEALFX%2Byy%2B7jQC%2B2HO%2FbCROJshqKD%2BGZPoYUgFGSwVLVhIcbnEn7DqWrmk7TqVcUzppWDMIFxrDKLFEHzTZZv%2BWu%2Ff22i41lYzhiRbdAgvN%2FKAB8d9Ob6t2%2BIz1a93g2MRjlBn3C0J6N7oBLq1QGxADbnjTYm2766BMlr0G96tjPQwjpNPnVNzS3HpsiNaRIaXCY20SchYxKDBBReOjcCpd6&X-Amz-Signature=753a71c0cd5fb4c3d24418777410786cf361401b580ea9a8595769788027038d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEDIXTAK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCubGlXFcGHmpfrIf97wp88%2FUZv3QIOkI1FnyL7FoKuugIgS3iqdqADHSLXSmmDcAH%2Bkqrn6WnlBXjV8yMTjMO53dIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDIimdfOXDQSnvj6RMCrcA1GBNj1MiLXi2lLjcia9WssFbuAviIG1l0PX409PbLdTdK0h9swSeALRYdc2gI%2Bt5Gbd3n2RjFYS8gle1PTyFgp6KORL4WcW3L0T09KR1p%2FPzTe4i82Hu5Bi%2FVo3y1buqJOuY%2FFwyyWjg3Prz9smefFhhL55crlUTBu2ZmQT1IvLRfiriJeeCd5%2Fl2NYeADDy9ITeW4hLc3VGaBH4La0EudplZv2ZWj7GRBDifdjlHAV26n5lvkjdwlQvJLzY0wTbAykMHYDVGNxOe3kVZy5LO8YeLljPZ%2FucnL63LgIMasKayI%2Fq43%2B6qP6iD3Gbj81b1s5hdzGHi9GtT99lnz1gw1dw%2B%2BkXdJbZJVBKmFus8UFkz27JBlPaeH2QeFuImwr1dZL7k2mPj8uuLIwNkAx8uY9%2BqV24%2Fo11HijZPd3ONnwcRUFpul6br4H6%2Bo4aWxKk%2F55TeYbx9R8WlMv8wqD%2FzFowWynmy1Q9vPivzwzKVrKCzy2dxJ4P7a9DdkaiU%2BjRvyW6w9NjZ1R40k17mfz7TYvUv6%2BFihicmz0HhFawJeH%2BgiL6QILFC%2BYpxTiLTD6cCHaHEl1mQGzC%2FZ0vw3oKzk8x1Cq6vp2nwB8eyYCrt%2BhgrWG3k241AXDf5c%2BMOuZlb0GOqUB8kGw4Vz9kBBXo2mxwx2t%2FtIgywy%2FqWhWakAekk5RJo7ApDtebccjuLkdrfQrzLSnX7v%2FqC6us0ZOtDP%2FNfQSv6zHZB9cqkNcwFXi7FffFKg8XjK7VoVHvXt3dv1SQscSs0ZhmCoJhzBC%2Bwpmc0ajgoqynUH0v0CiuKByhZeGxXCduE2uf%2Ba%2Fc1%2Be58F192BETDz1z3kv%2FjNIyVTJ1NTh2tiVhluO&X-Amz-Signature=d8c39d108a75f13a531efe67379ba19d4b5c4b7bdee6fd52777e81d7b1543e34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXDE6FAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCecLqk4DNxNxtFPnRqZ72TdKtpZCfbkYbZnMj57iHAzgIhAK9pfOEEjpCQrtX0z9KPJTUD4Kmg3UzcilZTEiFUJQLWKv8DCGkQABoMNjM3NDIzMTgzODA1IgyXEQXKhkuPYadz%2Fu8q3AOSML0%2BiNpoLYdkG%2BA7v870KY1URzYL%2BP%2FVZTNwpo2wYSCpbJowGIHeiR2jCzSjmO2tD727F%2Fs3t%2FjMRhyc5gw5evCP7ecDcgJgHsST9otydD5jl%2Bm0I1wvQ1%2BFBdGacgekWoMmxbRNIiurESmXX4D2kCgN57za%2BZeLc0MjE2HGo4Tq2FFsn96%2FSCpitBJYvWPV4y9fJrm%2Bmfknmoj9e%2BHBuGN%2BUZFh8bHpGx3EnqgtrORetWrJV6%2FHNVxENU8niNWYsMLs0jJygsQkJzVEaRzXgDweD29TXlSdaTD%2F5FeUf8aUaz3X43Czk3fCeiS%2FC88%2Fyb9A3MHdGTaaPWM3OG%2B7uUFXbXEOD6RdA%2F9t0zYNjUeCdHsLI5mQQAsOSisUlGJGa25qiNScLpYJnnRWlt4ljo0SkFSHNcK7V8iiX%2FFdhanccoKqU2dXTF7UJP6tkQQVZHr4SJTn1QhH3vFrM5VUxW0WrRvBa5QTYl4PDazH%2FK23YPkSm9wv%2FOuncmxY8Og8zVeFF7IOBBvfuJARZAZDwsculZRf9YpxRqfPR8ukkFoiK41m8ktoaB62FgmOIra%2BCPhcwX8cDB52QhFOGitnEefl0jSqT7Um4cUA6nLNFrZcf84UKwpB%2BZiOyTCampW9BjqkAX6uPQrx7LgUwMtRhEjCXmWganO4ZfaNcO2qMBmIkTTxJwEtwRsBZjst5B3qMO0rXXqqnixLUW31qWGag39Sg7pGn8OsGVVz3Cd9qdv8XfmTIORg2Jz1mm2KnPEytDSRx4%2BKYlz1d74M9eb%2Fg6lEzYSvoawFo7ppSYqjYqHVlCP7B5Pyw1jiinmbBXkq5wlrUGamaV5kKdieWljWX8gGIYFjk0Oj&X-Amz-Signature=5b60e022363f261502ac7e351e3880e43ec0b24716d3b8cc47197957681a3c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXDE6FAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCecLqk4DNxNxtFPnRqZ72TdKtpZCfbkYbZnMj57iHAzgIhAK9pfOEEjpCQrtX0z9KPJTUD4Kmg3UzcilZTEiFUJQLWKv8DCGkQABoMNjM3NDIzMTgzODA1IgyXEQXKhkuPYadz%2Fu8q3AOSML0%2BiNpoLYdkG%2BA7v870KY1URzYL%2BP%2FVZTNwpo2wYSCpbJowGIHeiR2jCzSjmO2tD727F%2Fs3t%2FjMRhyc5gw5evCP7ecDcgJgHsST9otydD5jl%2Bm0I1wvQ1%2BFBdGacgekWoMmxbRNIiurESmXX4D2kCgN57za%2BZeLc0MjE2HGo4Tq2FFsn96%2FSCpitBJYvWPV4y9fJrm%2Bmfknmoj9e%2BHBuGN%2BUZFh8bHpGx3EnqgtrORetWrJV6%2FHNVxENU8niNWYsMLs0jJygsQkJzVEaRzXgDweD29TXlSdaTD%2F5FeUf8aUaz3X43Czk3fCeiS%2FC88%2Fyb9A3MHdGTaaPWM3OG%2B7uUFXbXEOD6RdA%2F9t0zYNjUeCdHsLI5mQQAsOSisUlGJGa25qiNScLpYJnnRWlt4ljo0SkFSHNcK7V8iiX%2FFdhanccoKqU2dXTF7UJP6tkQQVZHr4SJTn1QhH3vFrM5VUxW0WrRvBa5QTYl4PDazH%2FK23YPkSm9wv%2FOuncmxY8Og8zVeFF7IOBBvfuJARZAZDwsculZRf9YpxRqfPR8ukkFoiK41m8ktoaB62FgmOIra%2BCPhcwX8cDB52QhFOGitnEefl0jSqT7Um4cUA6nLNFrZcf84UKwpB%2BZiOyTCampW9BjqkAX6uPQrx7LgUwMtRhEjCXmWganO4ZfaNcO2qMBmIkTTxJwEtwRsBZjst5B3qMO0rXXqqnixLUW31qWGag39Sg7pGn8OsGVVz3Cd9qdv8XfmTIORg2Jz1mm2KnPEytDSRx4%2BKYlz1d74M9eb%2Fg6lEzYSvoawFo7ppSYqjYqHVlCP7B5Pyw1jiinmbBXkq5wlrUGamaV5kKdieWljWX8gGIYFjk0Oj&X-Amz-Signature=9b5c2403cee734a89f7987c3139d375315b2e85cec9b21d001fe00414720964d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
