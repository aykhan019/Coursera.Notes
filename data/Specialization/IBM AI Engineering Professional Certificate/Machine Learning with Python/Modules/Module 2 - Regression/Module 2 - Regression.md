

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=0327fdfc5c0b75fcc05236ebe5a96c44745a9846c66bace5e88c6ab86b57cffd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=ca0728f015667f486ed8004e49a18e759849e82754b30a3284a9939eee1198f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=391ea49c939a23b41d0d4c25123f81639dc708b9a1f109284dc48db24e24573c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=cd99511d152bc2c4bafc98bd7caed775f882ef0856278aee6c063e8889a48a58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=583654a49b746a0aaa6917ff0081d32cd90fbd477cf40afe87c507ea2043ccbb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=c3474f1a2132e56ca77210ee64414ede2d7791fa96994c572aa4a67d72afd970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=00b80c7ba27313e89610882a00060a9c350c80a8780f46de98d8bdbf637b7fd6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFFTOPPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fpq%2BJnmynNOCQMpmPG9MpUKBvwftEyK3b6hvUKyVZMwIgIhMmLx10IpokUoLLZj7jcosB2i%2BpZZPEDlyI8wZz1iIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlUK25yu7dok7DRMSrcA5DpDrk6JfwxrZCjNUx35fbCXlFY%2F38ivxcFT9gIaWJku91tNIbShbfhFXgkw7oaljx8Gx7pC1saSqX4xk77BFJ6dKV3U8rkWBCKEKdNjAmwqMgBYtNyAozHyv8zwiHgdDDvARGI5wV6NeLXoMV2XvUfMf%2B2kuZ2lAF6fDz%2FfvOeB0lBJkVy9rcwGd1mjdHrSLvARh3Pq7%2F%2FhRO8I0qddDz5YprvK4pC4N2YxeU8UB7Hx%2BiK1HtrL9yuiY9IfnKbfN6wv%2Bio2AvqMrZsVYSAAUoFZi1I1FMeukZIIqn1wDBdUPK3s0BTDY7WBWtW3CmIy%2B4PYevWbbtXg41o5gXQ6blTMEgnTLXrY3%2B8H0nuEA0CD1JH6bxGaM%2FfjIxO5YRrXgjhVotDO66Hfw58OvAlTksT5Gm9gKeiuGl2CgLo40mAnvNvPfU4donUiMB1DgWmzQMVqfo8EtTqxoup9TWkeT5d%2Bhs1B9%2FnByIgaYk%2Fw4xFfjz8ugsf%2FlAScqXB2zU5Gq%2FpRqjvUYJ9PC4VREO6KqXSWmQ1266Pq5ur68vbCgP1Z8NFMylmcT8jA0b95tFAs73GYCylb0WtnVOEQckkyI9vELU6uruT1yLKQHr1EGIfy7Sw%2BJYUfSn5dGnTMIDY8rwGOqUBk8xqeJ7ii5mDUbKNF01NYQcIQQd72SsjoqDgXcMm1N0JKHk2BtKrWsOsK%2B79IFLZb5yot64h2Kd%2FapV19O%2BwA0szNVbDD1UmTrsUrJMVXATgmSnse3dkKtCC7PFAwkaU6Ajzx%2B%2F4BVbhJWbzZriZYB7xJUEylvJvhRZgK2PX6aSOOQ%2FtnxisU2Y%2BbWyug%2BRUnzEzT2f3Ln3MHbOAN26IF8PByoFd&X-Amz-Signature=ffbf619c091284527e10d4141e1ff503240e2d5c19fc53a325ba0dde1326789f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHA3V2EF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNsKzG7j2lEHyquxgYTVhPdzJUiGgGxaOWq7m1XkHdQQIhAOWNJYCymOowEhmTv7A%2BPqe7AkOGXpr%2B18Jz4crsurKgKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy19FMwJ1rerhX6%2B4Iq3AOB9cdC3wxCy0cUT92bK7UDgpMBPvQHpEVad9utRIrNWF56tCkYzEbXHuRxOT%2BZ1NXyH6%2B3e4tDFVQ6dk2U%2BVEls05GJV1Moc9OrY12Q5uFvYR1qFoeZagfIDe%2Fz98Ctk1EplBXNkEfUIGzIhthH6a1aqApMOYYof6QzCM58PDrA542OEq5LUMMYth6IVzpXRMZp788oRhxYooRNSGIHu3jP%2FWa1%2BrcrdXesprUIzMYj%2FESEwI2W5cVQOOf2KCLDo8VxtzMf8TYXGi8XL1WSZyDKLdxn1TENov2w8gk1ZShUz%2BuWB6FOQO0sIwDXkNv0MKyEgn%2FgnaaSi17yRqKDiKLtKGYJ0iLow3lRJa35ZRpyaPj0FySBnzlU0N09F2POUp8iM%2FlQeyAecGIVWJHPcViBJX%2BtG2Z4CZFEv8P%2BHcCvp7protp9p6dxk8WAdA69wHBCf7MQer3VbDlz7Qrovc8QUl38vhDdXdAlC%2BHQmjwNoLO%2Bo2oLRNDco2cIHE5lDr9dCjGXZq7r5n45ghfwUXpYEcXLNd3Ebh3oaZvrmG8FyBAuSeh2f0E%2F%2B0ZTBeAJt7Dh5kBMZZnVhz75wt8FNtxueQYM4vzV7t23lLSUmEeV8G7cfpDAV3vcMFI5jCR1%2FK8BjqkAWuPp6OSF1nubkX6w7N%2FMXhmIUOCVFJZa2bS9X0tyf5lHt7enH8LIwu1mcW5vX5z7MOXSz8chDtI%2FgvkeErDPPYIZ%2FsKK7G3wDOSBSp4N5mrZbMk%2BBtk1Pn%2BT1R4DZl3H7fo2fI8vZM0%2FoG5t3Ghcl2L3OEZWiWObumqdzZrYydxKWc6Wt4BpsaXxZWVLOnjMWfrJVNvuLCLAlUHBL25hkW01srT&X-Amz-Signature=ddcb60ef47b9515c31f2b545038b96756e3bdfa50318e860c734867641ddcd9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU2P5VT2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAt0v5wa%2Bk4sO0wGsJpJOGwPWLc82SkAX6palmCu%2Ft43AiEAnuBLqHqn%2FuLRqjoDLphHJn%2BV1ynTyA4OrtkQP7APXKoqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkS0B6zRdRG9aMsiCrcA8mHt2To75SWm2oMtmaXI%2FYzSQWJlq9WeHou4C2FCFQakYosa7FDe9uxTi5N9Y6tjw9IWvzTdudOa1jkI7xu%2By2wIBEKj7sT7fhJGVJmBWG4ASbg6Lt8rcA%2F5kqlyHssyxQy0H9ZruQLcdcD3AJGw50BCD4NcB2PqOiGGTN68A2%2BOpMeIm8ApxiN44ludbuI26AEsIyKqyKVtjw3sR1KCmSQZrSKD4qJoO0ts0%2B3ww0Yl9nECuCYyeR4rdupSVcpXOD5Zm630h2WF9m6RGvgMJlBAG6xA2JSILOdTZ60vK%2Bp293BEYqDQt0MC%2B1lOHD%2B6uDt33J2osstcPYsob4TgaxclUlEPIbcfsYkcSu%2BLNdPy%2FjDkO0RkReCv020jR2b7CClrAFvvwgU9nPs69Rc2dJlvyfDvYSh%2F9FydaqUWEzfXcUKYBIGsBWmUsT0%2FbURYBmDX%2BvLVJdEuFOIKNYw7dKbd%2FgVg7Fz3w14Fi4qR%2BDaf8kJ4IRwAGOao%2FFY5G0ZAP1l189tdMdAk1BHflg9JKnOvlrwzHrCV%2FLVRIww4ZNvP%2B3YuoHXFBid3kCc2o4mlRPMepfYbwwzApMUFgEPw8To7T11mbjPJoZSFcVhRV%2B7jBkA27W4TDPHzyfZMOXW8rwGOqUBGNeVQNSfe9sltgVCZo3AWqLin7UN6GzTKMphpnYF4APFqAEZHKTBSVbcfl%2BAg1iEHFI7ur%2BHq5XqnBw0OKzAVBTC302GbfsdhBZpkef%2BeMdeGflfzkrK%2FNF9WOdcbAkM3EqQmdWBWAiCQ2cfZtsEDpd2undDR14bBz9iyQaTcS9hJ8fL4aSH6jUFfaZ7Q4pN7nXmZwbI8v4kve8djsLAXewKHt6Y&X-Amz-Signature=881002b1ec487dc092812d3d558e71afcd3c15d5b6bc743709cb375870bb5bd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ACZI72Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAZB8AzztI5tUOpUE1ZOZN2G1RTVKyC2Eku5IW1AInEwIgb1YNMB%2BkWBYeAA7OimHI534DngfMgD4QwK0YFrtgnRIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6nGRGqanub%2BRdHXircA24WbyM7nnkmJ3kwCHL5hwXhHa78RNJ8ynrfMYSMPG%2BdeuVrpg74%2B7RnCSfUDw31qeRbrdtj2p48IIq%2FM%2FyGvewibsknoTvPwtmO2gBRrWBmBeF4HnVc4sfAXnsxR10zy5Xpbyk1JzGQnYVrDl%2F9wQdpK3TqfNMFrUeVcskmSe4Wht8kbRO2r5EHQnOBAgznLtgthj9y2qZ7VA4XR%2Fs6%2FVnjwGM9SzJj3Tk2XQ5TvzQCMLd7hVWXZXvO4H8KpzKnb1quVBW2QZwgPiyJEhTP%2FMt4eKB7s0Cd9JQILeXwDjOCYROkQvps5n%2FMmyxy1BoDGbpf5Pgb3RvAemO0KuGTpFD95i%2F4kk0V89VrG%2FS6wdOYrwsloqlKqz6r5sfVulFWqJvnJnJBB51H698tFcaD%2BgRRve3D3YFqS2iNpWF5N3ec1aQe44Q8Dpga4r%2BicgYl63TCta%2F%2BLQlBk0J797Qx1oHPgrF7LteKcN9p8cnPUxGySRzIDeR1LABseKjIHe7tqZZ%2FlCTMtfwXi%2FvD9iadZbSz4eLVPiaNDWWaKKKaV%2FglsgoTY68mLVZ%2FXnTTjtH6dvUqF%2Fm%2BtJKOMTzez43Z5jXvpj1B31fJaOyudwTZWM5gT8mbhzdLZKoKoh9wMIjX8rwGOqUB4WYKHRrd%2BdCDwRUbQKoLWWfDWDR9LhQYoL95qqyk%2B1ekgqw7r1ndkF8VzmHIEw8WR5t0ZRm5GiXrKBYfPIbXQ6N6jVTTQZz0iwiTttKjqiCCtolQKJCksY701zkl%2BJXXMz%2FbRSNC3ze4KMIvtQ0hLeYdw%2BpFn3YBeA0zdJeKati7DXWCzQLet8Jd%2Fj4UaJaPUWcMPzJ%2FA2bxx7RQpnZYer3dYkXG&X-Amz-Signature=43f8b9d2c6877884a9ce178d6dab0a13201bff2c3ce5ac57044774aa8faf58aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ACZI72Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAZB8AzztI5tUOpUE1ZOZN2G1RTVKyC2Eku5IW1AInEwIgb1YNMB%2BkWBYeAA7OimHI534DngfMgD4QwK0YFrtgnRIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6nGRGqanub%2BRdHXircA24WbyM7nnkmJ3kwCHL5hwXhHa78RNJ8ynrfMYSMPG%2BdeuVrpg74%2B7RnCSfUDw31qeRbrdtj2p48IIq%2FM%2FyGvewibsknoTvPwtmO2gBRrWBmBeF4HnVc4sfAXnsxR10zy5Xpbyk1JzGQnYVrDl%2F9wQdpK3TqfNMFrUeVcskmSe4Wht8kbRO2r5EHQnOBAgznLtgthj9y2qZ7VA4XR%2Fs6%2FVnjwGM9SzJj3Tk2XQ5TvzQCMLd7hVWXZXvO4H8KpzKnb1quVBW2QZwgPiyJEhTP%2FMt4eKB7s0Cd9JQILeXwDjOCYROkQvps5n%2FMmyxy1BoDGbpf5Pgb3RvAemO0KuGTpFD95i%2F4kk0V89VrG%2FS6wdOYrwsloqlKqz6r5sfVulFWqJvnJnJBB51H698tFcaD%2BgRRve3D3YFqS2iNpWF5N3ec1aQe44Q8Dpga4r%2BicgYl63TCta%2F%2BLQlBk0J797Qx1oHPgrF7LteKcN9p8cnPUxGySRzIDeR1LABseKjIHe7tqZZ%2FlCTMtfwXi%2FvD9iadZbSz4eLVPiaNDWWaKKKaV%2FglsgoTY68mLVZ%2FXnTTjtH6dvUqF%2Fm%2BtJKOMTzez43Z5jXvpj1B31fJaOyudwTZWM5gT8mbhzdLZKoKoh9wMIjX8rwGOqUB4WYKHRrd%2BdCDwRUbQKoLWWfDWDR9LhQYoL95qqyk%2B1ekgqw7r1ndkF8VzmHIEw8WR5t0ZRm5GiXrKBYfPIbXQ6N6jVTTQZz0iwiTttKjqiCCtolQKJCksY701zkl%2BJXXMz%2FbRSNC3ze4KMIvtQ0hLeYdw%2BpFn3YBeA0zdJeKati7DXWCzQLet8Jd%2Fj4UaJaPUWcMPzJ%2FA2bxx7RQpnZYer3dYkXG&X-Amz-Signature=33fac5ddb7375063e05a568452cafc9705275c52ec15341cfb5123f75392bebf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
