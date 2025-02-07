

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=114231f85ace04faa4a7bd2520255ba76b89748babc20eb793350457764aed4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=dfa884b53dcad0f400ee6a94471d14d322c0c714e5f1e8cd803e87967c63abd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=c7591a0a05318bd955567cc79a25e2887271303c08f55694688063b6284bcacd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=dcbd29f3efebd3bdc1e762153aacf4760c630fa129980a756f4f15e86a9f190f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=6d32d2dbac0a3041187d4bc167498de50ca776d9ecd6354ade3d5730392d8e5d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=93cb548c596a728992dd9609a889a581f347446c91fa7e5454618386562c152d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=6463a2467536828070b331515cc0710d2dd6049b4b71469749d3629fffd5d8cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFUJEAAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHq9SCvq6Lbtbklvz%2FAbD7aLBr4II167JVNiAvyCgd5DAiBdb7M0BUkaYOhN86qkaQ%2FobELOdgXuZd0nnpOddOiUHir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5vgLiEq4qiUbogH5KtwDQr%2FMT4cEDeG3oLL7usgfwoUNRCGiPJbO2%2Bf1Lx1BmsyERIQs9Ii8PKN2fL3z6a%2B0vuENdRFvLos1ZJtxQTt41aMz%2BRJx3eurSvs1tjOoaebCqTZ%2F5%2FcYH%2BgrW6TP4cgTK6E6hHiaDmchv3X%2BRgTq66ZoIMn%2Fc15sUdA%2BTqwu5OGUU5bSrXYA7Wdw8w6AjlfAVio06wWGKZrxd5gL4dhhq3DcMbIJ%2BgnlxkXdes%2BPaY%2FjrG8GIG%2F3GfUgvyaJt2ZRVMI8pDQoqSTTHbze3MTF1BOKvrcxqna31e5EMz%2FR1csVkZOumchUBfSHoPELy9RuxbPz1iZSpS19BTe8uA2S0tenkSLS4hm5G%2Fc%2F0jDQKxiQJjsrL88GyCz7xaBf37At1hmKkCh9K1bEuQuA4M5VyOp8lWGInnxhlyc%2Fb9m4I1fJo1gYrWrzgkxhX8Osz0%2BGG5hu8gzi0CoUk5iTfAMOKUscGGmM4sHgWngYFwuVvSr%2BEohCBfScXXPv5It%2BlnNsQJpwXPrsxFJuA572B3y0oL7FH9fbXwyvWnawxAapcAk3%2F0mvlfFDYlGXQb3WQFWZLEF8g4DHZGGkdUFZdE9aHQ%2FhnqWtqR1IdY8VaQ5xzBu0Nl7FF5lr3Fa%2BSGIwwvmWvQY6pgHXYmoc7t00GgP9zpNmJOa7ZF%2F5MeGqhnWxQBVStf8UvDlusJmjz9tIzgRDXeuiyVFbiXlwKbNx1tZ3VeUYO4B7iD2h6EONUWnQMlo2dSwXyKaCrMdBuW8YTpuulQC%2FkkW1RGFYeS4Nzibe4tH%2FtKhuyRQfTtrXoHuASa8okZSB%2FFVG3sMcQY4EjIwRAMUEWB7yBL4TB7qc%2BvN9DoO5FU8M8huZCXxF&X-Amz-Signature=d68da457f02151a77bee0283f28b571e11f3a1febbbc83c141aacf675ebc00ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636O7CTQ7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIBTWlheOtkc%2FJhuKT4mfWYdaxIIWGUHH8ty8zDcCn8V0AiEA87JHDB4tPHrB2Pvgwwo5guo3oRMPjMiBlmiy45lgnJYq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI2P%2BpXPxiqN77w4aircA7B0vQUS2BapW%2FGGDsmaB7wAdvOhoGGO1fR2NwWdaax8y7f3iS09%2FY2k%2BWvQfqoeowM8egh2H9ZKSBOaXF40A5JZLFrSN2RI81Gp%2Br0YISz6J2jJJKAPGGgT8FRjaW6AewHTB4qlQtd0iBTocaeltpbtKbfOga5GcyVWqDMjtb5Hq0JcdOoof6xb3AsqJo%2B9QWmUG4VCYRPkyZCGRr2sExyohSA4f2t718ysyCGTCtm1rv0xDuxrUP7yb%2BRDLNMri9p2E%2Bs61m4CH8H07xb%2F5lpFNUO%2Fm1YhCrb93w6n5G4fpw1rhf4K9KPOSo8DBk4kJ1slxeZo0c6Ox0XO9T82Lf3f52lvTvzZrRsvwC%2Fx1PnXIGhI3TWzO6NTcSiiI%2BtjbIQbwR%2FM645YYdaEiVpQQrHH6VHrmV%2BuYk3zh0gMLkkID4%2BpE0WHt3J7QEDEsPtXmXed1i3M1cwFtjCMRzt7CcBtoayMEF%2FP5RkiVFTCmZUymWrgrii1g%2FUT1Vrw9fcKOhbCuLWju%2F9r7VWAUtrIDxvgYTbnl26MRTsJJ0xq0YwLnHKK2GCGvY%2F%2FRa3k9SWodSkBFK09CvV4VtZWoYbjIsQMLWznVmEoKbmXpe4F%2FAANyFcemohsJ9Ub3CmfMIX6lr0GOqUBtkh%2F2Nat92Eh6lcNByAfuMEktk8iRv29aQ0r7a2PoPtfiUG%2FFaHNjZBgrl9vECcwXnEXVTu3DvIWG48UoYvKc4zYdrHc4uGw29KCfxeppXsBMZg0FhAf%2BJTtI1wXn3qfGwmad4da%2BZCrWq9rDlZCrWe1qK3fvetdHebII%2Fs%2F3Ic%2FivjvRm2WOk8JsaBaJkrn37J6PVGLAMTauiYE%2B5qanD9HRe7E&X-Amz-Signature=5c4444a483d02013d8f16cd84b58067b3a8c0a61c2a90bab88a3e4af431b7a88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY35W7J6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQC2TDflpaYGnFPfRiLyjVyjRykivEXjqwjK6RLhZRt5LAIgPicTPLxBSMNwHiaHcJQu8zoW1wWG5oNdokgbfKXSUDIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDA1XrGzlNP508fm0JCrcA%2BR1eyUDQsdlSpbSocX9qI%2BMlrP4s6RZVf1H9OTE2rh3cTxaKVsDh72GI%2FSi0vRWMRSPmw0DAvQZVJoC%2BUtZ%2FTghNr1S1QcCchlz%2BTlxqfcoSD5Hh6HH5HmMpMdFE7m9PrvVHBJVEv2k72rO2Q4Q5SRXcCqphay2%2FkI9nJdUqfyu6WA11ounYrfF%2BzWnoXzoYDN%2BOwkoxpqakM0yrqSR3Sd5TcX4PU%2F%2FF3EK8K04MzI%2FQBM3irEXvkrbn%2FVgailrRcd8BLhhoxejR176tHAuSjesDlH0OgoMEyqxmtHu%2BJG79o7mLm7i%2FCtzFdaQD6q5V9NOeqSyPSFfOjN6%2BEk4ZZvgCgvPYpZ1Z4pcQDJYkpH7KYV%2FF0cYN%2FszMDzbyqv4OcwPY4%2BQlooyFdV8TktPNqNZnjIXz9R5UlvbQYpqPxsuzmuMNlQq2VFb4VlAJT%2FNRPP0c2xRpu9dEPhwDj8SoW0wjB0mUb3%2FeGBcWy%2BZUujWAPMdchotwYUbpik%2FMVaasAU1xDAkWEoLQADIxCzJPZJZ4a80ta%2BdN5dxToFcQtvK2iPOF0U2T7997Kn8ZZ1ohDM6%2BSH9%2BwrdzC90nli0HP28iDctJ7WSC6d7q95KGN1PidL%2BAOed1hlmcjTwMNf5lr0GOqUBFyW5eWP2X1mPMGkOcLk3tlskxWvRxbDHAdEOnD5O2pn1Dm7XEAmM9w2hixAi7oIukHAVvF3piPnZp0wYGz6JbRpBBXgDhheR44PvBUby8btRg9%2BCMCgruUDQR896h4%2BxoZtIOIUXo4pI0M%2BsoehyGYQWajCXvqIMsA67hYIb%2BkfK3NATmqwzQd9NTQhgxfN6aXWRuTSYiqqQ5X2tNvlTqpNXpo5L&X-Amz-Signature=3c8ef9f12e6315a5a569ad803e75c9b6f9cc1bcd1e9a720e8a38781ebb718c77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4S2QBF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIBPRONN10wuPhHjJBev1SfWz9V9PzzONHmxyegzy60NJAiEAo%2BquE77CEJq%2BNhasBDICdL3X26aktmyjf7mObQCeVEoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDMhtc8G1MaEHufR4CrcA8NsxMUdxVwqDVZqDOFiMw2xuHuaUQkAMo0UR3ukqxk%2FD9jmxMo4gJJkHMu45tHKMi3xw0HOtUOv7RgBNGdDXqw6IycF8O5VDLLwq%2Fu6risbst%2FDeWIxkMEXU3e8nZD86lbSuOSpLYXlrRQEDO3XUw6IPJDP%2FItNfylCcyhnGqqeUDV0A%2Fw01Yhw1NuBkOcKj9bgt1exYl0Nisty55rvrDNI%2BDa3raUI%2FoOKIIjBWtDnnGLCSorkobi4D7w2rlAl5n%2BpM%2BhCXnDyokDG%2B4cYXjb9MlaQddygNYlIgsrE2fiETdi%2BC3HVOl3Si3a5CPWdKRQMJpr7VLlKdCnjtOSoL%2FzL31rtbbjt5vAlgf7QlRQZpdA0aoCp73xvvltjfliSHiuxacGdXLg%2B77HfUhOiw%2BeD8RdqIE5Y0hY8YE4BgIZnFu0Mx2Jjs3yY%2BItwMmmGwtFKPl3MACTVJJapHr9VTiIOURDoACaki2VKejAAeWeyikQluoh3jJOhJwFwQGK6bFEp4kDm4J7MVhaS3jBbOqwTHpFsuIbUw%2BaH6jd12fwL4NawGHSlzOXQxhxwDVMvGoR%2F4uQMLpDlnNA2mS1e2ECDXpQ%2BfgzxTtH8sx9Jg7oDPnfELDLG6nuvKBjmMP35lr0GOqUBYFpLBp5jTesuvhRH2UOwCckKgdsCStK%2F06xQxZu20X%2BGa0CxQWw3u5BvzzzRHRvqFrTw%2FOU3YxCUcuG4QfRGpRFIwc0nM1gmaJAxcR7vABVTnVJZ0kcOqkWfxAGCllaZ%2B39gmPHUZFuFno9l3guXOEOu3RzWZoh1v5Qkw%2BZmdiL1CWDv0F9w2UwCqbdNeoiWxLEcJLTIFnQ1TUFyzH3652vnqZ7k&X-Amz-Signature=a4bb18168f0643683b7e1f8b28508f23f40e30abd79ced580dcfd3e94994d34f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4S2QBF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIBPRONN10wuPhHjJBev1SfWz9V9PzzONHmxyegzy60NJAiEAo%2BquE77CEJq%2BNhasBDICdL3X26aktmyjf7mObQCeVEoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDMhtc8G1MaEHufR4CrcA8NsxMUdxVwqDVZqDOFiMw2xuHuaUQkAMo0UR3ukqxk%2FD9jmxMo4gJJkHMu45tHKMi3xw0HOtUOv7RgBNGdDXqw6IycF8O5VDLLwq%2Fu6risbst%2FDeWIxkMEXU3e8nZD86lbSuOSpLYXlrRQEDO3XUw6IPJDP%2FItNfylCcyhnGqqeUDV0A%2Fw01Yhw1NuBkOcKj9bgt1exYl0Nisty55rvrDNI%2BDa3raUI%2FoOKIIjBWtDnnGLCSorkobi4D7w2rlAl5n%2BpM%2BhCXnDyokDG%2B4cYXjb9MlaQddygNYlIgsrE2fiETdi%2BC3HVOl3Si3a5CPWdKRQMJpr7VLlKdCnjtOSoL%2FzL31rtbbjt5vAlgf7QlRQZpdA0aoCp73xvvltjfliSHiuxacGdXLg%2B77HfUhOiw%2BeD8RdqIE5Y0hY8YE4BgIZnFu0Mx2Jjs3yY%2BItwMmmGwtFKPl3MACTVJJapHr9VTiIOURDoACaki2VKejAAeWeyikQluoh3jJOhJwFwQGK6bFEp4kDm4J7MVhaS3jBbOqwTHpFsuIbUw%2BaH6jd12fwL4NawGHSlzOXQxhxwDVMvGoR%2F4uQMLpDlnNA2mS1e2ECDXpQ%2BfgzxTtH8sx9Jg7oDPnfELDLG6nuvKBjmMP35lr0GOqUBYFpLBp5jTesuvhRH2UOwCckKgdsCStK%2F06xQxZu20X%2BGa0CxQWw3u5BvzzzRHRvqFrTw%2FOU3YxCUcuG4QfRGpRFIwc0nM1gmaJAxcR7vABVTnVJZ0kcOqkWfxAGCllaZ%2B39gmPHUZFuFno9l3guXOEOu3RzWZoh1v5Qkw%2BZmdiL1CWDv0F9w2UwCqbdNeoiWxLEcJLTIFnQ1TUFyzH3652vnqZ7k&X-Amz-Signature=8b7ffd6bd95ac3416d13aea0550077898708dda38b0034cb9132f693f97aa595&X-Amz-SignedHeaders=host&x-id=GetObject)
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
