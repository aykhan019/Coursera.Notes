

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=ea3348ed30860ffe1dfa0727c9ee48be5ac7fcd810b8ae5842f5c37d067aa1ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=49b27fb2a9838d741ce6995f4c6f6ff2c4ff009224da581916c58de10288140d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=144400c1f678435250963415caa331d0c30a5b49a9d724be3d199487d45d5d57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=7c522c8f474e955fc421b737e26370b18d7248f94ae7385fb37ce99ecebbde47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=8a02c3403dc9c294701387a71c517efe6d1404497ea24aca8cd703dea39dc5c1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=1383ddad554a23d66d41822aea8b6ad017513fcc480fc1f81637140d3c0bea8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=31cb59cfcd97f61676546f77014ef8e5ebc5824640dd406ca8d3b30facc98a70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAVL7ZIH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF9ItVFE3opbp9M2aICB2SbQLPzTCyuW1IPSUtI3J4vQAiA%2FZScUyMXANyA3o9hi38ApCcPlVIzfIRzylcCTXHdd%2BCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMxJCW8UAbgBXpOQ5QKtwD%2B%2FmGRi2Fs6gIAy8id16%2B%2FwIN%2FEZuxJXPAda337WWQod83ZQJfjCtOS%2BFu4er3vtD8tXZBfTPxqhCaY5tp4esxL%2FPVJDrwHisfx49pTWdDuY2JGb1LZQPBugjgETRcKjNN9Mo%2FxLCPw6ujZjfIx1cjDZkoVTe8QzKyqPiuud7wnalekGd9giZj1kwYSUtJKU%2FCSojjXhKr17Ada9CV2zQlTyE7TVNLglyLtHllwfzSH7ac%2FaY4fOdWqNeuldNt487vi%2FR0vL1d50RzDi0Iw3CuY%2Bvajns5rIz82PUKg4I67JjGQHQe2Lut0%2FkQx%2FcVZsdtA6t0P46C%2B9hnvQCawj1d%2FBZA7ROVT%2F9tHqCeUdZfPZLUf0%2Fi3O1msmkiCM1ALSVq%2FkBAqlRM5uGLPOMfBZGbDqKv4RP%2Fsb6lpladtVg2%2B2lGJDpI%2B2Ujyp8A3q4Uh4WAtIB1oxYhVvjeihFOECU63bD4SNYsXOk72cJRvCklV0B5Gc%2FEKiZEy%2FAvoqj7Io%2BJkuB5bhhHhrhYOleZ%2FdWfgE62L2d3VrhhUVLWgc1mHPKXtz3Yg1BlmqCeh0YONzRtErB4wuBeXjn4b6kDC5NZy8z4apEPnnmuSYDfQX%2F1ldzLQdrK7aWEAb1AZAw%2BOqPvQY6pgE%2Fiv0w2Wp2bs0wAGnPmBtW7wUVghKk1IqUvBHAbBD%2FKDyF0RyGRwLTXqMON8Dd7JhFqzLE8%2B%2B3D39X9GIHKOwSq8qywYJ6PbCOjTOvlbZPVstJU0M9F8zOyCsRdxrsMp4x%2Fy2ECfSNixK3tBO4v9ZXHvVtn%2FH4rONrySzDF8A3O%2FYpPd6OKJiACGLprQV6orMjuwDGfCzcK9SqKbsKaNfnewRykmOZ&X-Amz-Signature=d960c8be05438840c26b1ea7a5dd04c6a310131553634df3369293db8baf5c48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65J4JK2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDNPIINphNGwQmfKCZPQmWxp72ic6%2FiWFHft5OrrRj65AIgEZWExYyDhIEMeOJ5DRLt8h6UZJ4n3rfk4HATAlGuoyMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOwAsyIl%2Bz4Ay9gj4yrcA103T0T0KjTl%2FgWQtDOtBi%2BAA50efmBPMi4qaxUSAhXBuIDh1YZQpa6OHEqIcAdtclof01%2BYHfHjaEPdVHHj34VW%2BeTqiHY8hbNYR%2FUfB%2B3K5vsDJnp7xdxyY4U2KUzk4ApvuJDnV%2B04kqy%2FBEQau0MaUd6S67Aer%2FCmSxfVALufR61zIOR3XU4%2B74ZGlezwicFdI9q2kc4cHoe376qL49YqgGmfVO0pkfvwVtZDnPJ8DoHnVhw4EDpW4bNsds3htUJJ1FlMe8df68veoyZpqYlRLZrXqHm2Sbx2FFK3w28tnkBCPyhEB9GtHERHnHmKMdVrl2qpxKy7enxgLUv9970QHV4Gmk1Aki1xmw%2BTUj0HwsxjHozlH8bWtbCA6BdCfAYmdfBjf8e7I62NWG4b7kgvesCmh3RlAqAXamLW89fzNUxjb%2BjKNautq3BsRaupMMZnEv%2BdnwWPL30BmtpQ1J813w8obETRSUEN8FQ821jwWLYX3u2L2P5cd9TMP4qPt1%2BSDoRkJSExhtH84KDdiXZt1LAXDinCI5i8tWm7VGhfU%2FpxK%2B8jg4V6XmzU7HyYfeRngemHH2w1B64a1Bc%2FSi8BKLBGpyFXC4KVHzTlx0m69kVc1xDBjoYpw4mBMN3qj70GOqUB4vG5xHMjJaBfQF%2BiFvU%2FmSLZ17s0lknd1Db5Wy6UWPMMewNRf7vhbEycS6KaueLMqqKMuPFF4%2Faed4tGt5KJ%2FKqphqjqTNuF%2Bgjb6Co%2BSsXTiAfIR7026RHuNicE67EjzOOqcRYLEoy6prvm79onUyV6XMw6yZhv5tnTqOO2UcQcqN4E%2Fvi3hV2YbqQ9%2FuVaFy%2F5tgta%2Fbud8Yoh8xIcfzpFPCw7&X-Amz-Signature=b1f145f2cdb41271e39a4abfb5dda1127b424b1774ce41784031b146a346f77e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCFZJ7I5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAfEjKYFdYDypmUT4xMGWcR4m4NH5TLm9SuwIFuZ%2FCQPAiEA3KtetgQcRW9nzks5X%2BCC9Q6UfDxgfoCZJzE1rgS%2FSb8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDBb9Zmaq9l%2FGmLEvWSrcA1NxP0bGSeR9AKU4%2BxpZa%2F4nAo7DyEFPvMIkyMGikuBquVB2DvBaT3E1Bp0gsvwCsBmyPaKu4Uk2uT9YPZMLXcHl5kpNX9MsxAMwsN%2B2BViIiTKj7d5su1fQ6wrK1DJVOvR1n%2FpBU3hx%2F8RtDzzA45VA4AOT6ALK%2BLI8Ka6MrcvlTeLW64trGsRAEU4FNDaqo4OjlFyBHZyr6NBFxUuc3hy3DlgXt7QKQwBcqpaxLAMnVZ5qWtYIK3JzdnWnYXAheo6JXufNNOzNLngrAbbmPn5w5bPdmfKnxXmNrLAdrzgWKTmC9RgDU12K7HNICWUQV1eDtVDFbj3s3p2QxMmz%2FyrD%2BggmCh2s0YytfT7YvY0%2BI1HWhSe7Br4KEPfzpxT5dIwf3hQkXw4vMNFh2y1jXSyFW2DR2iQzG2w3flAfTYuZ4LvFmQrvdzdAYs62mzGzQa4PuYn7DTiR8hWfHU4rTMtXbKKu6%2F0P8sHD4%2BJiu%2BU9bJV3Jg6GH2vm%2Bs4L0KiFd4Yqx4pyGo%2B5G9OaWzs5cruAhnpAHZWxOcHqBAnyygTcLvF7BRuoN8vqnoTDz8f8TwK3Eo2T2Z6KJXbGwzvyG2%2FTfsmRqO%2BmUfmufDYVjEIv4q131Qe1%2B81RAPHRMNzqj70GOqUBGAdlczsRDXycyzSG5rZNf%2BNI2xjdzaurJsy7ETyl5et73ahu%2Fb9fdc3yJNIs%2B4YRiIoCFrGQnKj6GTIjoIyrdEZxg3lYHn6zMp7ykcu6JsNRyWyC%2FBq2D9uTAnUiGimtqcERtiY2rw0v%2FrpUIkIVMP%2FNpJaMD1C%2FDqZZC1MiamWyryslxHMIRWwcDG2PaUJ5Kv%2FGtutVSARUuk9%2BJk%2BmcKXM0s4y&X-Amz-Signature=cecc220c35016e66f37b21ee20657cbaaaf1a693400c3feeecdb7b1541067d94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5UR6VZO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGTJ%2FvFTOHsY7mnG3va0IGfFaKI02rsrRFUDL9Zv67%2B8AiEA1ThkzDrgCIiHFzW4b3JxLT0YfIx%2Byx7p6rcKD7iKK8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDC9RKUMf8YxGj3HP2SrcA7MMmajT%2FHEEOZc6BYxQdPv3%2FJCY1IZJyD9qKCiD6yCXHsqxond%2BXoRRfcBRXvHHk8AN80XXicHJGsbb7kj%2FV3bLaAsiQa2qDh1OwdRI47o9qHhB1vC6x16jN7vGtAP4hL5cPsYBZ8H%2FynL%2F0WFsq6MulGqUP8%2BFApjR7JZ6decifHM1nPh0vLZ0zpDd59WIREOwwM2MJUrVG0rAx%2BdUnzEOibsVsLW3IMcr%2FaGplJP6%2FdEBGfyam2xVuuL%2BZFyq8itzUQxTez3kE0z0bbjAyYPFwmQv4JAGCz1TBje3Mz4x35e6xADGFeTt%2FFcQbw94cVVcMnfrDCO58ncHlts9uVjYyXoiBvTglEZDSXDrXSARcVz2d9L4vDelzUGcCjtGxedYk%2F89q6x4gfZL%2BTAysrxDNo5kiRkLbz%2BywBfp3GTBI0n9v3gyoAzclUdEpTV%2BPK1NY4ptTcIvTZzDL9lTsnk9TqjVR%2BgyzQsqP%2B%2Bu23RcwSXM6tqW0tsY8Wsp8Qbs1sDRiJllN%2FuO1A4uX8SM8JF3mwEDiCHB3GYojEGKmgOElt9vq8tfqMs5MZY1duKI%2FT2NoGACOs23rm9nDUEQyISg%2BvUWH%2FarxHmw%2FH%2Fnqmp0bPtFYGpv%2BFdVtCrEMP3qj70GOqUBQHaOrCylnfpdEUtw8IDBts7zGf2cnAt6uyycgPVg5MaTENOejhyH%2BRBasNYgI2Wbqb1q7JybodePnajH0sLq3ZqtNzaIabozIEkd47JfA3OZQt1edPPJPk3fRw0bU2Gqf051i6xnRU2tdJz7IcG4ojRGT9nfTvlewINLUSmX6KTLeLFknX%2F7L1dGL6XWfHHuyBb7MVPTvM%2B1rbzgFcbo5jao0FaT&X-Amz-Signature=44e371915c9cfb11464e0892ea27ac324d37207c2648652484f05b7ad477351f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5UR6VZO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGTJ%2FvFTOHsY7mnG3va0IGfFaKI02rsrRFUDL9Zv67%2B8AiEA1ThkzDrgCIiHFzW4b3JxLT0YfIx%2Byx7p6rcKD7iKK8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDC9RKUMf8YxGj3HP2SrcA7MMmajT%2FHEEOZc6BYxQdPv3%2FJCY1IZJyD9qKCiD6yCXHsqxond%2BXoRRfcBRXvHHk8AN80XXicHJGsbb7kj%2FV3bLaAsiQa2qDh1OwdRI47o9qHhB1vC6x16jN7vGtAP4hL5cPsYBZ8H%2FynL%2F0WFsq6MulGqUP8%2BFApjR7JZ6decifHM1nPh0vLZ0zpDd59WIREOwwM2MJUrVG0rAx%2BdUnzEOibsVsLW3IMcr%2FaGplJP6%2FdEBGfyam2xVuuL%2BZFyq8itzUQxTez3kE0z0bbjAyYPFwmQv4JAGCz1TBje3Mz4x35e6xADGFeTt%2FFcQbw94cVVcMnfrDCO58ncHlts9uVjYyXoiBvTglEZDSXDrXSARcVz2d9L4vDelzUGcCjtGxedYk%2F89q6x4gfZL%2BTAysrxDNo5kiRkLbz%2BywBfp3GTBI0n9v3gyoAzclUdEpTV%2BPK1NY4ptTcIvTZzDL9lTsnk9TqjVR%2BgyzQsqP%2B%2Bu23RcwSXM6tqW0tsY8Wsp8Qbs1sDRiJllN%2FuO1A4uX8SM8JF3mwEDiCHB3GYojEGKmgOElt9vq8tfqMs5MZY1duKI%2FT2NoGACOs23rm9nDUEQyISg%2BvUWH%2FarxHmw%2FH%2Fnqmp0bPtFYGpv%2BFdVtCrEMP3qj70GOqUBQHaOrCylnfpdEUtw8IDBts7zGf2cnAt6uyycgPVg5MaTENOejhyH%2BRBasNYgI2Wbqb1q7JybodePnajH0sLq3ZqtNzaIabozIEkd47JfA3OZQt1edPPJPk3fRw0bU2Gqf051i6xnRU2tdJz7IcG4ojRGT9nfTvlewINLUSmX6KTLeLFknX%2F7L1dGL6XWfHHuyBb7MVPTvM%2B1rbzgFcbo5jao0FaT&X-Amz-Signature=006210fe3d92dd4e769eaa858201ac27302e7789370df1c64124385231bbfad0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
