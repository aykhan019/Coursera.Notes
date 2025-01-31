

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=7fc2b96368d5c29148b83449307ce98799ca42f086b1af4a57c14e161104cc1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=373a7a48a3af01f58fb90052298d6b42b4a128b7d0cde3b3b9f59e6179523147&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=7c198f77489598c23ad12fa55c110f67bf8c024e922457e691fc7b08fb0c1802&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=a0f6a78ad32cf650cb40abebf0880c6dee058ad6d664e76dfe62baaf2097a29e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=61f42efe74e4ca69f464e03c76f6e9aa45a1a203f7e65b562906c3ea76fb5d4e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=53f654fd09023155008620843cef880bf5ddbf28d797c06b555a1ff99f7f35d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=1ab513b3ca2082f576cddbc2823eb275ddcfd4059b0d31888b92020738c84de5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBBQZY7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6TirY0mdJ%2F1k1rAuRz1cHkWJSH3PlWpQgsd5SjyQc7QIgJJ91RMYYZJ8XZY3if%2B7dK5blqLQFSzxOMwcK3O2g2%2F8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tDfamgLrD%2BWv7LSrcAxgenphytfKJkNqTyTw1bR3VS1Ec%2B%2Bm2nl3yJoWh7PpcpVwfzj1OuULuQoors6tSnmI0HMNEhLTXl3McNHguOJplkiFa4kG0gQKOz31BiC8iUu6cQzcYvjUBwdDjl%2FiqY0J8qVXOBpKQvFtZBdC%2F%2BpZu%2BQ9YA8zDa%2BiH2lQ8ssks49%2BmVn4FS7jEKpoFynzx%2FAgBboWfVyFGv407r%2BvIb1u9tfuUz15Uobhch9AcGEm0h0mN2o62mhlI0mrUA3N9EnIRUVjRPnEPYBdlJdMU04djo9IYOwbY8puOk8lpvGR7LG2vQw5wc2WyQZYtHD4N%2Fov11JsyVF%2FCYQUj6IQQkqAGlC2DyKv9BwnZoWUAAmAPSYPf5aTaYJWBQSVbXKqOMRM1szRvH3crtTnbYp7ecLepIv38nTzs4ZiDXF5j9M2FHPk4TX3YhCjsEpW2cVmJiJQ%2FPlF2PVkKTsbM16V1drWVnPyfztIWkEknlfQ%2Fzs86oJeAdJoqyc6Nel7tXcJw%2FW8BZN%2Fr25Fqx9MMLhgCgdEk5F%2FpE56BRgo%2FFXO%2BLtlu1qWqwq1KEfnUByphAKovZleh6Ejn7pZLbHQMVy3aUSYRxSzbDd%2FHjrpkG%2FkCNFBnlbbEDHvMjTlZHFoeMLTI87wGOqUBtVxsNgH0qwP%2FwPz5RsACvh6aKl3BclgURHtCWxMCYZr2fD%2FPQ%2B%2BLilizPy0R4Vk%2FhOVLq%2BRO4Tl7m7%2BLhpJ62xhVKmoXzXi6OoZS5xYAkAcoFfE73lXNO1YD8iXTlOEat6NiXiE1VB0p%2BtZqBszj8j9tirIeQfMBRyr5pqnAwLOqDL%2FzR4AiX5JI9e%2BdBVKLFgu5h1PknDfUDHoiny7c9MVM1fdn&X-Amz-Signature=08067f187afe29a09b66163fd6c2ad6b624f92b7d9978dc5ba4d5abcf42da147&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VH4RICMC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXP%2BkEJujOVTEdnCutntAv1SyJqQzFGL1N8j7hP7IzHAiEAjbMGv7qYTX6qlwBGJJlnuphY8AQ0RI8wYGJUzTsv8A0qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFe%2FUrYpzcak0%2FqJgSrcA5ro9k4kpotugD%2FPGCgoPqTIK2NQ6k33N4XxXcba579ds0FBIjyhjwG4W4AiRw3P8oDHOpx78OSHn%2FnW%2Bi0ICX9kLoagiwanc48LwjlP%2FRqV1dAtq5exLGxF5a6Y2OIF%2FuzskMXimoyttTdtkA12qMow6qyP3Aea7Z9xt19F8LMFy8%2FANReTvO5%2F%2Bw4tYIwd9juseK%2BDseuJNEnbIDR4siUY7UaQpUo4Jwd66RvEfMVD7JicRym%2BfAEchQsQcyeioys1ZxsEeHSQ9P9kBUSUozaNPQIfdGo9hAstYsQAB0UPRQ%2F153E6NmYsuJnW4ORTmEd8Q98zgSbDEA2HokEXzJxxcNTi7rlQ5I9t6djkF2yEXx%2BIu0d6fsNZ55NRhQXX5ppwGvN4R5Qt4xfKkUOeORVP4jtlBvN9v1ZXa8BjHDE3aorphpLA9cNKxtJVOCVtDCSWOwyxI7yw8iiNQcU9m9iKRqB81m%2BM%2B2gp9uz1OXx04EQaZe%2BoTFpUP5H64uY9K0%2FyS23yq%2FozucrVTSG24qQmIbIPPlqzlRQ%2Fq%2BV58pCJqOJF1PBm5w9d29uXCWnx0Afo70ym5TjNunJVLPh87zQFyNMIOLoJ8erX9zynghS%2Bdz45AS33eElb2M6NMJDJ87wGOqUBpWcqq9pXw0tSJFXsKXJWpiyMaJoWvVitx9c19S4Bc1mRGsTOE53hxFl2OVk5bR%2BtZ1cJQJN%2BhiKKIWfgbUCNE2FmnimSNzEOkbXNfuEXYR3S6Lw6XJnObpFM6bjQ6tf8aiI9UyH2KTaSW0tK3%2BXtP9EJGoOlC5wk1vBbJJb8l9UN56NVztBvxhVrf4A88Mwqk8%2BWSm73%2F4E9HygIYE3CyDFgt%2BjJ&X-Amz-Signature=38c948f2df297f61f43defa2795f13bdd968a779b28b94d7a6d6a25c747f20b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7K3WELD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWNw%2FBRelTqMLXxtt6r4pJkG0atkJ5djO%2FKF1L4OUUBQIhAJMs2kA08k4yTDHNI2h3gtvng9Jh%2B3yzVynZuwosY%2B1GKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkKB2KWaeA%2FqttvN8q3APb%2FYol65oOdg90HPb6c7pENGwkIok7DigkpEp1w2RG8YGAts1mlOA6l381%2B9qnFi1QqHzkUNFtmfNOloiRWCf6H34XUpPv68%2BPi%2FhDrbbtHsnUxFrEaQGnNce42JOdgqOKExmcJ1yjZqpJVl7FbT6qUgCGIUFfUh0wJCaXQRr31bh5l5T5NoD7scwOdKxat0mmkznNkEcAjRhN417lGPkPGFD81JEvDbFxDFcom0o1UwjyoMnPzE6JteRL6TlDdlNak2IThUfW8yMCVyazOpSqF7InmQuiKo7WwEXZMZOi%2B6EbGFaQpxGCZQ8B0xs9%2F3cvy3STc5V9fg91YMQMiXlTHbSuGOG5b4Y%2B7i8ZjRpw8NHUBMElay2KOldH5VtNFQBTfN6yVJO%2FS0Ke0WY0rzbVt9GGQJPRpQa%2FhYH9pkzc3YXVGLslIL4ASxpqwG09Xb0QavGe8fsdyTe7Kw2f%2FFV%2BmQ9n1c%2B2uVw50fsSDaTX9aAPVJgFcTaq1aWimSttf3RwZTPNz4WH5IYQq9NM7z4rPrQ5BXYl364HU7uGVQv6NzyHWopNwUb%2FUQ87Q5jYKjxfb86gdQ3PGcKfdMTqgK7mo3ANpy1311PLRljEaDo75tbY8BZZoDafkxsVGTDqyPO8BjqkARZyg6l4KzLGTuvrUCnCNlsK4n8ad6EgdbUUiMlUWRY23kCWbExqtOxJMUo7PkuU8gUXthj%2BDYt6VwfO5X6YhdkXU%2BsHdx%2FoUboOvST0x1lLUAOarAfX%2BZxVlJ0WzTrcG%2BvKfVgiUVeLia9vyBahf5rKl76%2FReGfmBwagEG%2FPzfNsAl2q4wH5EP%2BIFTdWlB%2BTZM9iUHrZCCMJYuGkJXhOGY4ayiH&X-Amz-Signature=c3d87a69d266eebe9bc7bdd8fa45f7ec511ade3308a0d0c2af120e52a711d338&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IELFCGC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxjcjuWAaz%2BDqTuK9QN%2FEGG%2Fp6z%2Fk%2F6pOZkne28FZFvgIgQ5OrkuV16bfvU%2BIQn1gOuu1jxREV1o6b%2BtCyDPlvtU4qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKP0IfV80Q8VS9gk%2FircA8UhY0SrZ7I1%2BI8ipg%2F2o8LV7H6rbD1ejsWvr0vJP4XHdyuweEIBnAraXhL9hiK8JRSU3exduBf%2F%2FaQl7zaY5fxQ%2FWsvdPpSQ0mVMFdI5uf1t34ZvsOTSGbCnjUhcFQl8JfoM9mifebisBFl%2BNqcyf3HjWmlKYJhuXZiNzIfcfDRq80vCK%2FGmXEZJ77XiL4cHUc%2F8y7my7wRy7gl3otNxUUJIv07WSfxIZsnFgBqOPQTY6gof4jt%2B8%2Fxj8KWLbD4cpGayogSNEJZBWzucejQkXmajMbYZSQ8B6UKYiPtx3TZb215LZPmQJgZMaC45WC3bZei6peztqeSgzo1%2BywjiURBzOiT%2FdU8suhaNyKGaeZCOWPKWdqYEoto82p0ZKqFeoH9l8ZM8FAdOoo4FDFELYVdjau0S2vEIenFLeWmlA1k4pNtk9hw4gFeVsC1OzRkZlguIXw99%2FF1yZnAWE7d80e97S3H7QSmSi8KYRS7DN5YSiSHvRdKODmYd1jLbHiZFMlcQRhrYfGmrwQocNrwDwZwW4SF%2Bs4IU1TbGy0d2324GUBZQPe6RyjgEB08r1foKqzOkqShPSFXanTf8jlD0lVUNLg9WY914lEqlUgOBHM4Hjr1mfhUh92LD9trMKDJ87wGOqUBGFP7XRSDNq9VMFQUwJkI0ZdP1jBmOSiVy1vYYNWHlFZJtX%2FjeNA%2FDgVULo2Aw0iEVWX%2FIS%2F3AN6YsSi%2BGm3q1HV4Bs%2FX8byw70YJd9XGdu97BklmyJZMFC02177rnfkdbt5hSf7JG3sTOZbRsqeuAkyp%2FOBROlsRqK26hbtEYDEmSzFvTFG4mPeas4bB1FPQVKKfybveESPrrX3FFWNy3DlDltK%2B&X-Amz-Signature=e59d909b389a6580ac05637e7c0ed50cb8abaebf3f4c862c2f1ea27241a95209&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IELFCGC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxjcjuWAaz%2BDqTuK9QN%2FEGG%2Fp6z%2Fk%2F6pOZkne28FZFvgIgQ5OrkuV16bfvU%2BIQn1gOuu1jxREV1o6b%2BtCyDPlvtU4qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKP0IfV80Q8VS9gk%2FircA8UhY0SrZ7I1%2BI8ipg%2F2o8LV7H6rbD1ejsWvr0vJP4XHdyuweEIBnAraXhL9hiK8JRSU3exduBf%2F%2FaQl7zaY5fxQ%2FWsvdPpSQ0mVMFdI5uf1t34ZvsOTSGbCnjUhcFQl8JfoM9mifebisBFl%2BNqcyf3HjWmlKYJhuXZiNzIfcfDRq80vCK%2FGmXEZJ77XiL4cHUc%2F8y7my7wRy7gl3otNxUUJIv07WSfxIZsnFgBqOPQTY6gof4jt%2B8%2Fxj8KWLbD4cpGayogSNEJZBWzucejQkXmajMbYZSQ8B6UKYiPtx3TZb215LZPmQJgZMaC45WC3bZei6peztqeSgzo1%2BywjiURBzOiT%2FdU8suhaNyKGaeZCOWPKWdqYEoto82p0ZKqFeoH9l8ZM8FAdOoo4FDFELYVdjau0S2vEIenFLeWmlA1k4pNtk9hw4gFeVsC1OzRkZlguIXw99%2FF1yZnAWE7d80e97S3H7QSmSi8KYRS7DN5YSiSHvRdKODmYd1jLbHiZFMlcQRhrYfGmrwQocNrwDwZwW4SF%2Bs4IU1TbGy0d2324GUBZQPe6RyjgEB08r1foKqzOkqShPSFXanTf8jlD0lVUNLg9WY914lEqlUgOBHM4Hjr1mfhUh92LD9trMKDJ87wGOqUBGFP7XRSDNq9VMFQUwJkI0ZdP1jBmOSiVy1vYYNWHlFZJtX%2FjeNA%2FDgVULo2Aw0iEVWX%2FIS%2F3AN6YsSi%2BGm3q1HV4Bs%2FX8byw70YJd9XGdu97BklmyJZMFC02177rnfkdbt5hSf7JG3sTOZbRsqeuAkyp%2FOBROlsRqK26hbtEYDEmSzFvTFG4mPeas4bB1FPQVKKfybveESPrrX3FFWNy3DlDltK%2B&X-Amz-Signature=a8f8502c6bfa51e1615973efa850d68e109aa304f70c0cf6d8b581e1f6164cdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
