

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=dd87048225443c6e5ea91b911856f1a783c9ef22a32f33b31582d3633421acbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=64b73b9991a8d722be5c2bed09d90a8e73fbc49b948c95ac170d46d05c940562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=f3cfe308103b88c7191a78796367bd535789ec0541453124eac4246a08b00d61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=db8e1ac9bb44a1cb106ed82600e2d5cf5e50d7b73d10e4ac59eab747a1697ce8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=c93ff407bf0f1e30cd384659f1c6dacfbc02936b1b0244f6785a9633a65c281d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=38a8c751e940707d254a6d972f91582b4d6955206c8188ace9e1da5d579fc29f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=217b68cbfbf6028a22bdf4cc279aa9e9533300ad40d25c86aa33cd74cc42511c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6EPRNZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICuRlLg75DOoV19SsIaNS%2B%2FytnyJKhtqQkury99Jva7tAiBngOk30gL3UcoLmSDrBSpwZJM7rr7NOQIp6adQ7%2FnPcSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPCA65YPbFLdVVDaKtwDXAKiWOXbuorX9jtPrQppVrUIMZnDErIee3g8%2FnbRpylxHVdju1lxF3bSY9lZkN%2Brll%2Fr9Q1EjkSYz1tmiuHRnnyZHtOQCX%2BQb1oE3e1oSm5BZ2VD%2BjflxCAqx628Z9dw6xb%2FH1T9xs3n99C0%2FZSI2ZADa%2Ff7v7SGZQjEO7ZCJCKtxL%2BGkURenao0B9dolEJ%2BmYmIuwJyNNqEy9ouI20nkqn68MMZXvjkV55Ugf3kzKRIYwyoojHiAi2JjHUIX8oiDhKY9WJV6E%2BOuax%2BH6A1rDHgRJI2ALcrhdD2gAklYkTEdJtwIYOb%2Bk77Os7Jnk3u2DNK45%2B2jFj2LVGYRYjnbKTrJr4Pm7LqpOZfuiWPab4GF%2FU%2F%2F%2FHg0H5mwU3SbEFQAJmI5MTHchpZNd7TPkzcmfNjVIF4dlMG%2BgeDvGMLitx9JP5Q%2Bno4QVvPhkVwp%2Bt%2BbiihSRAx0VUilnVPPQKQqJlDbnYjJcmXGvJRG%2BESZkRWE6KBWx7Qbrfc9EaZaknE93aAPGG3XUlSo9vTe4Ro1Xr%2Ff6u2p0yWZf3ncXaNj4iiL4TDF6KelNnCciynjoyqDEiEVnxN%2BU%2F3lll0nXH9FvTFYBZkxsCqdRUAFJKQLeNC7THAJjMLlL2zPD8wq9SbvQY6pgFBHrg9uBK9Ski3b1u%2BfAZJxtgZojCJ8FSBT%2Fkp67xoPVn%2FDMisa5UiceoSvqMV9smSHEMPxs8b7CuFYnHAKIze7LX%2FaDMt88Lb6S9eqfYR8u3CJt27KkXNBJNKHypFnuS5KnxG%2Bz5EhIS0sKMLFEmeAOjKe2kKqoKGhdCSgJQk4xZXOZZx4FhdXEQi6HzQqg2Y%2FaH%2FhJz3LgavOXEIGsPFIEoBREkF&X-Amz-Signature=58cabc9e46c1a350bcc4cf8f5159313ed4615519f35d4195b9223a63c80df315&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USIV5FQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDWMPvGGFE54lJktrM1xr7uA87uRljKkSZY0VHahAF6EgIgDR4oYAp1G1jCMjhx2i9kM25ZOLabnv2OZQKOircB9JoqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKE22oiqBtJAickTySrcA2DjaDF1saHSQQQE08inM%2BWUtoN3eFs01nzwzrJmsfu593EKT2lKELGEB4xR4l54REuC3Va1trghZEcPgrBNQADXE9XrhyAXC1BhYrj5rsHcyWnxWw4uxE147RVe2%2FapZV5BFn43Ca2Eqy6mSS6q3oUoHt4RCDCZYAJD8fniCvsczWA60IASng48JkxwbbkEk35vBSf9Yt8XmOjoqaL2bhSIflvI6c7J%2FQkdOsTK2AzA6dHU58m4qp1jVZRpEkkJpkC5%2FIgUFNXToQ4lPJDr0uWAcqUqaKx%2BJl401JXoGZKxElSkQYmGmEV4dyTlZcc0n0HWRaAgUBAs8c%2FjQjaC9Z2l7IZG%2BDRb8JH1cjpWyf%2B3ZHBVgS21H9uNTsl6cK2pGA0BxJP%2FfBoteCFOGqTk41UOGx8pfWcOsanaDVMqYfDUbAf4fm2fUWH3nMaWupsZ0WxgDq6nD7cwFRYZERYYHQeDd7zE1aTdxc1d%2BzPDjW5TpVTIqI277kmbuTegdTCnIhPFHrpy%2BInZEa5ShL1QDfiZCRbYCZI5%2BEmR%2FhpMByO5BEVnstibLNvPNxMeDQQvKNqGW1lc8cvb%2BeI893d%2Fy3I8XmsTJrf%2BDodclvK2E%2BXW45M%2F3Jz16EInUggdMMDUm70GOqUB9Xqb2bEREgp35opXJ7zoAJVbJqgGkV3XY%2BYxtaQTfGIlT4qTUDfK%2BKRzqhomsqhmCF2REYPz%2B%2BQ2o0UPCF7d6cktgdSGuClVoBjfy0j28ACBK5rjyA4mKsDbqJaR1nx7EPx7kU1y6hHHxY9qhGob%2F5s5y3hmWBNJBRlbcV%2F9OOTkXe8qGMDqIhwY6INPe%2FWHjo44QRJZoOWFilCHpjvceTpoFiVd&X-Amz-Signature=63e7322a459671efc9987f8cb3a1071257502fc20993456e418ccf98d1b2ecf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHWHQGN2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQCLiYS4IAgHyei1Z7xqGPRkuVjftu7gPrfqXSGgzulPUgIhAPk%2F4ThIKGHBh%2F3kno3CTztdKUd2ONApV1Vwna3eCfIxKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igww7B7B6fwKUjzXM6oq3ANKsgV4yvY%2Bxd4c0xZZOwGd6JsJ3pssBqjnjQTRPCTzocDwtJ3RYRGKLnOIwlYUkR3ABZKrW%2BN3a%2BVvcYgPW8a4oXsU%2FvhPS5pXukQ9SGzt%2BZL%2F1vRWQ0wE0uzo81D34BpdbHAk%2FaoyKI2M5sViwYvhvvsZZR26yRCSgwaxsNO3Zs3V0cTmCiM35xUpQUrh2ZDcUknbUAwUfz8fNYs2q8j%2B9QKnixVUFdW%2BWKvM1kUOtHdDe8XUxC%2BxNpOTSZsyz9TilR4nTzZGepPOr%2BTVkYyu4qIExgENfhu6Cf6WHw8Ewx8TG7kUyvJ%2F%2BD%2B1FRAwolfGkBtEv7cZk7pZf6WI3rDEIran5eX6GgutgcRl2n2fC6ObxG7vgB%2BEa5zDrIL9kGhUYTwMPsdKSe4zb3n7vunWfwlnJvaAOJZAvzWxq%2F%2FEe%2Fn%2BwJz6RIov%2FdGjHXmyz3N7%2BAblJXW3MNb3rD%2FFrFVFZE%2BAYcF28%2B247pfH4xHAAPAPJykXoRgZvkRXr%2FrDTs0zJyHqTzFrJGo%2Brqv2KlR6imzaY0JC7vPPGxY0Kkn3VS3pLq0uSf47sZWVH49XLYAa8xKYdVhRCWeaNmco0S15%2BAw2YbjQq8WVboOxxbv9FkkgyUa2lK2rF4F0fTDJ1Ju9BjqkATY3z3DdnMfnfwasB%2F8u5YUlKJGd1k%2Fm%2FAKglOWncRdYRUDKDuHSyU5kveCwAP57QzwkxrxWGjmZtCWGg77KWGiwqnCTz5G7qnYSwEAEym23hv02xIpx1C3iZs3JHu75hfjSKaSt4ZYT9MNu7fbKO65fYkXccQRgiUdfC0sDAu6%2BKarbN%2BPqOvRu5x4v6OxFMW3FIFeCivVlewV0iW6pdj7LlRW3&X-Amz-Signature=fb7d7681ea0c70b53fc1aab5bcd0d2d4a1dc983f9fcba625952511bace4aef85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSEWBCSS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCID6qgeNEUET%2FpE4YhebE00fWDGdAWIoz5KfEs%2F5%2Fxjj7AiEAs1gG0J3luRfaHNqbGucBqVMHfecQLJveGZCEOyLs5QAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDId2F2N1lVS48BdmyrcA8altqm6SfjvAKjKAc53dCH4FXKItepK%2FbS8smm%2F3EuCU6YW2pLDsnUNDbv1vUzB12s0VgXVCsyNSxFrP7qJ38T1vraG5hFK2YfF5%2BEnlx2bw07VVlVV0dW%2Bzqb9EAmMoznXuBAqEP%2Bm%2Bfz4VVZNcmM8ikcytzUWjy3KKJTy0FWRhFb3F8fPSUlnnUyLRjf7z5su276GwKU3q5RPEdHudOlg7NjRR035sMrW5Oc6VwTL2XALz0%2FVg1g1UDoBrJyS3doMSkYmFiZ7LVjjR05j7qEdJvlzHIhny825l7flilFCd4796f5j3dRCmMlMi1u4VjwTKb616jXO6q3JnF3UwbEGgnwMGfrNRv32nFhthATsXoeiTDCCas%2FTB52%2Fi1MEZb5jcFx2PbHm%2FyV15XcRDOEgAWLw587JYigm%2FaA%2BmNwdBWt%2F55rwmLfHvaioT9iuEcmI7r3kd4845rxN%2BqbqwAwPE8F1ugjLwQ1pPST7qJ2OnWKIJoJoey%2FVJB3%2F%2FIE2jLt1ZzMmxZHfXnN4W9uPiISgjoYu4w8Xx5SqYiKY3S43VCV%2B5WUnXMx%2BmzkJL%2BxvVKhuReecZQJ%2BC%2ByQtGDp75ZdQwV6RElmQoIrv8oThXrZLJwo86TRP9LdP5IsMLXUm70GOqUB1VZ9ozw6jW9OdWRabUiXdcfghBnuRHJvFdn3Pco1T%2BWmmSv0loLdP1apoAv7HTDN%2Ftue10lnFAV4VXNYo6LA66ZZUqNgTIUvUohqmPWhqdP3AJUAgWHjVjYFEMbpfFV8C5aw%2BN7NcXNkBQBOL0s2XFrwxf3%2Bj3SBloR%2BXgc5s7RSEqfHiyTp9cIC6t25sDG%2F7A2zwGV5AY8z1LHans9hvX0nhBIk&X-Amz-Signature=f40d2a25c79921ea098284be552b4604bf498c1c99778f7b9a263bfc6e6bbc4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSEWBCSS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCID6qgeNEUET%2FpE4YhebE00fWDGdAWIoz5KfEs%2F5%2Fxjj7AiEAs1gG0J3luRfaHNqbGucBqVMHfecQLJveGZCEOyLs5QAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDId2F2N1lVS48BdmyrcA8altqm6SfjvAKjKAc53dCH4FXKItepK%2FbS8smm%2F3EuCU6YW2pLDsnUNDbv1vUzB12s0VgXVCsyNSxFrP7qJ38T1vraG5hFK2YfF5%2BEnlx2bw07VVlVV0dW%2Bzqb9EAmMoznXuBAqEP%2Bm%2Bfz4VVZNcmM8ikcytzUWjy3KKJTy0FWRhFb3F8fPSUlnnUyLRjf7z5su276GwKU3q5RPEdHudOlg7NjRR035sMrW5Oc6VwTL2XALz0%2FVg1g1UDoBrJyS3doMSkYmFiZ7LVjjR05j7qEdJvlzHIhny825l7flilFCd4796f5j3dRCmMlMi1u4VjwTKb616jXO6q3JnF3UwbEGgnwMGfrNRv32nFhthATsXoeiTDCCas%2FTB52%2Fi1MEZb5jcFx2PbHm%2FyV15XcRDOEgAWLw587JYigm%2FaA%2BmNwdBWt%2F55rwmLfHvaioT9iuEcmI7r3kd4845rxN%2BqbqwAwPE8F1ugjLwQ1pPST7qJ2OnWKIJoJoey%2FVJB3%2F%2FIE2jLt1ZzMmxZHfXnN4W9uPiISgjoYu4w8Xx5SqYiKY3S43VCV%2B5WUnXMx%2BmzkJL%2BxvVKhuReecZQJ%2BC%2ByQtGDp75ZdQwV6RElmQoIrv8oThXrZLJwo86TRP9LdP5IsMLXUm70GOqUB1VZ9ozw6jW9OdWRabUiXdcfghBnuRHJvFdn3Pco1T%2BWmmSv0loLdP1apoAv7HTDN%2Ftue10lnFAV4VXNYo6LA66ZZUqNgTIUvUohqmPWhqdP3AJUAgWHjVjYFEMbpfFV8C5aw%2BN7NcXNkBQBOL0s2XFrwxf3%2Bj3SBloR%2BXgc5s7RSEqfHiyTp9cIC6t25sDG%2F7A2zwGV5AY8z1LHans9hvX0nhBIk&X-Amz-Signature=0471a526aedd89e3f99f8e1eaa7fc2ce342095d09f7fd3641554c9380c90360c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
