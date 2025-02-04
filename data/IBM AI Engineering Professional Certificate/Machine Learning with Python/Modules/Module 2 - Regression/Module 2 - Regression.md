

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=171a952f2dd6a7449bc1ca95eff9c701a5f0e5e0bd6f8a32420cd20a45f56701&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=24f2bad48ba3c9f665050e005928664414cbadbe28ec49291b73c1c170f9417c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=da38687e222b03e031e20765ea4606d0b11f31d3dc3c779b8d3206d3b4211846&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=5b8fc3adab496f102d9c8b73b097c79637ec2b788dcd1ac01e05ab31866a3d99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=ba58546808038e60d3c28ff44b4e7426568b46757047e2a96c0b64db02ee9439&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=2a4fd40337cd34a558c0d87f0be53dca9ab7514d6f1765358f75dc106897f4d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=7bcf4c4f8a40a5ba141b3206bcea80d30b1658e4f9eb8390fe6c8a6422de0d59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWIQCE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEkSfKAH5SpEfb9uS1H8Qu4K6WI%2B2acjUbCKrUuqOxEFAiAVgW9NbidOpxfO2DoTmDnSdDC1E0ihXmrD4XdEBEV1QSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMb8A%2BwUakfpIQXGDeKtwDnp1fZOV9tZ9yBUhyYwPwA9XB4saQ83OhIOb2RRK%2FDe3IYzTkdD3%2Fo4xRpMn5rp7BUFffIU2IZxIJZ%2Bc1aAIbAsXG0oEKqehTE9au3e6%2FTmd3FGxQ6hBn%2Bx76DtqVnTVcYjJpw7rnhJKrPQPdEr6RTXzDYH6xX2QZQSlju045emwAXJ7c0vPDbc6mzVdD3jHL%2Bt%2BSY2zk8likhjgCdZFmkLL%2FxxoesYxEQfpNERoul%2BHIao0H7PXv%2Fg%2Fb%2BkNk5RzQxgHbbHTXMc1EVUVehaTJS6A8UdBmgDPc4hLbbWRHhEqxLHWtx3GMh3uy%2Fqb%2BU7YmtpfW2OBpliXj18s1dkC%2FyI0WQ1jYBuAq5tX2kaFjLaPLExQTmddNOMJhIDYlPFGshY6bFAHkJjkjvxr8o9kcP8uGl2c%2FGR0DfvGJDxJ0ZPhZtl4DlBqHHMBqfBo1MLTeX96cJACeLt81cBOyjgTQg%2F5T%2Bu7%2FunmPuIA7eZpeSrJHXWG%2FQiJVjraCiTl9OiEMa6Tt%2BSHzn9PPGcJW7XwHqq%2FlS%2B6lRpST47RS6N%2Bwb8KG%2F4lYor6z%2BcA5PwjHqMoyDftxVWA9z%2BISGwcvN%2BHwtIvuQQQgdcYzFmSiRG6%2Fp9AH6gl7K9HWeSD3QnUwnpSKvQY6pgFSjLODi78KaF%2BNgGwvsXKj2IxZLvlPVauA5ZwMJ6CbRZzp5slcqLjuAMhsOWP3lclu3gloCIFNbUNsnsbJBeoIjtXLGsouiJVzErqCxLManuEt%2Bspoi8nCZLTGLXDVgDKTZOTKpL4j9aMS79zETiNz2HShND7QI5M6p%2BZ2%2Bl5sp%2B6bx%2FZDCTmlNOvK%2Fmvm8EefAY8UN7bdkqhRD6ekgmM6IKQidoS5&X-Amz-Signature=eb43bfa165ea38fadf4e49f09e927ddd83bcc9b2450b0c7954bd21beb4e3fbcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WGANRYM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIB4TvjESt5lOO6howCVxxc7ptlsiChgCg6wZCAko67m%2BAiAwasN5r5V5mW0DL2Q1bBUHs%2BuQ7FXn6EMKRdRdlOh17Cr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMaU360fKRBwjzYzU%2BKtwDFA%2Bn07yPt8lVnAHR9qqwhw4Y%2BAf56pZ3hRsa95bctOy3LZ4Hbgd9D9%2FnOld2rUz%2FXeh9asiphHiwEAVAsO5xxnAMaGhf8tPz3Yr6XFhcVLhYaA5lfQNIleDud09Nz4tu5sIZMZ%2FDk937ltmpt0gBU8I3dHh%2BPCV9PqcLXgx14zzwpSTuFZ5xPLiv6u2Lan70hfTGMkpkqFs0GiI4KKNZuz2Yae6IUbRcn2%2Fw%2FMFlYny2XMzIQ5vhXha%2FseIyq%2FCiawbIE8BnQH7QRV7VStSauDYhe8Ka4BXghcnT4cCy8XgM%2FdVajXrAaHb%2BSDPqEyTiepjMF5lDyute47TEvhzgOkmcxhD1spPpHLfvafAzP%2BpALlcuBrpbFViWVAsFqoa9acM9F9CnL4906xTJcDti3jaUQ%2Fjj%2BlJP4Z8nZa4DpkzuT5FYJ9YDTAIzWTZWLUREtUIp6PYXZvCWncmpNXfDseMQEGDBJBr%2FTYJ7GZ9G0UajYE5R%2Bb%2B%2BTfX8xnCSmgmEXeiRg9iBnSfO43xIV6O8zcAYevKMF3PuKwfsozOCvZYeqYDXYaG6FDP1zLvXHKHQ1GfHgvfcu8icp2iuXF5%2FpxE7%2FFnDlu1gMeDG8Lh8O8nz%2BNSA1VmOXtzmKdQw75SKvQY6pgGhHGwK3waeSE%2BH6IF90BMGFSc9sAG0D%2F7%2BYjuQWB3swAUOIrD3u6H1j63ZaWz2mVul246XPaIXTOnyKzHbI%2Bngh6txlSMykgaIF%2BSs%2B8YMfB2cbmgA5HhSvvjYUyGHkS5kTEVuy7T5ajE8lJlaBmVgHZmAagj2oztuT9KzewrvACZfvqIzic4t78z1pvnB8T%2FxLLn%2F306bS3oOFgDqG6mTzt4o3%2FIG&X-Amz-Signature=2ed86ad137f231ea0154822bc548bc6949c209cdabd6693e81e382be1c55fd59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBBAU5UA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCu9F9TBf00TP3XFqUcOl0NuL8fnSnx1ZbfH9cNsn9JkQIhAN8gJfZ5AO0SRC49VE833VllEzJYUOixuF3wwRt%2FvEVDKv8DCDcQABoMNjM3NDIzMTgzODA1IgzM8zPVwTkhBh2pXSkq3AO5sWCt1C7viiFPfUsDhtD8yThiZitjGqh5z740o3%2B905jI%2FCx4qY0VtYTrEVYbV4EIKLSH0NUv1O36KWLeyrWOQ31g7OHFoqF4klow1u4TFA927US6Miq%2BVei9st2EvuWX1HSwVKdN%2FrI60%2Bhd1SjEbrmT4yPQexdOulU9qCVSjY9690EVKzdsURofQTfxJUuHUdu%2Ficx%2Bvowok8hSC8OZAi%2FISIaVJlYo8XUDiyBkVhHjr4a2caz3jGoc2eOU6JyEbTIfRDCFrqic%2FvUjKjO6i0L5xvRt0xY6iNhqCSryHhaunTCiU2CW25KKt%2BOpow2%2BK96T2vV58uXcLdjyNYRzZpB2evOXcME7qqwHWZsBjFlZSJ62QawR59UKYLyxuLMHAIKYJOfN%2BdZTQ%2Bcg30bnifLPWledHYif0%2FuTgB0Vj2enCBvcd6nV7nElHq8dLLpSeQhbN%2FiFIkIeakTY6lnmmonceYGmZ6aT4VYpFBY7pYrxj9OoDD3qqmtdg2POxc0LIjT574B4j6Ow4cCB5oUUWqfmcECC4dYhcT%2BkMd3QW6N3wlM%2F9fj4XuswCwr6X6z0XBbQBLXNnYz%2FnOCRE%2BAMuPCWOy5EOIGvwtxHtni%2BGUcj7S1OskCrdy%2B25DDflIq9BjqkASqjWktrVvPs1kr%2Ffog0R1mryDfklEQ%2BeFwCdH7FlGnGNgE1oA9LWTq6josbYznvdk%2FRVoq2Vvwg0YklpHyCMphKzWvMgfpkTdv4uyFZjQRSQVmKmDqZufKnXn8HG3mxXzAR30GO2geitcXxKLclb1r%2F88UD%2BHpGstuy87vKi5KxNK5fxcJnaZEMFSkonIfg7ux0eeUpamuPR764lNLwi079oLEE&X-Amz-Signature=98caed3cdd35cffc857c1083e1c6cc4cd9f447a07e78026233778bfc14f3f40f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHI25J6S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD%2Bb3aPeGwtgIxjnzn5aW8TozGWLeIRVPnwR3pqDqQlXQIgGkWV9kqyfjQNh%2BkGrTqE6xK1raCqen66%2BZQxsWR%2FaCYq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLIlPhwr2J%2FzOJhKjircAw%2F6VDgFR2NjW97kOv0vHnwegSRscYQ6apN42OsvqfyAsrcBCypi1C8fvPE2%2Bv2QZzVtyPfozB%2FkXW%2Bi0cwDSt7Xa9xFaYDBATb0ky%2BCvP351kuUhHMk3xwwcKuMHhz8xvLHHVaqBshfeWZe6IiKMt1kS1nmmmvHjuBeYEUQkgbdDXOYzf7wAcpppkGPk1H%2FPaRuwbnTs1Q%2B9PW7Is4K65HrM4A67lvdOxQQjfWJccH3UvSLlXTX%2FC88r3nNyEr1opAToykf4iYdA2D8nIcMRypFYpV0aac8kqFHysGMa4ZJCwF1ic64K%2BQDsQIdJ0NuDoBcPgj0edGUVUFQXC259U6Ng%2FnkK703v13QrdS%2F%2B6ciD9OPrp44MjlUO0ZZkjuzE%2FM7eoGcMH8w1CGEN1W%2FjJ3EANSj4XSij6wrvT%2F0bHuttXaUnBrew%2Bm%2BW7YvxODO7o7%2BjQxLEx8BlGA5bH8NyX4mYUuDJUevh2n8NtTTzWBiRvnuq25A%2BqkhFbSOSgOMsJyhDmuHqtugOoNLPDh5qGLX6CZv7y0quM%2BJqz5EbJomg1ucH6OCMk%2FXAi%2Fkrmh%2FDzlP7eCZB45Aw3yxukrtk%2BECvKIe0niqyEjsxPH4KOQPmL3ACGDqD1Taki4pMJ%2BUir0GOqUBqrAJfCNg3gkzADJImfNipOj70q9H94mka0OtfhcfCojApxevtnracOEpywpRiiEnL1QIAGpT36c9o7HiYtjIKM3qYIzKNRAKGYUbB%2Bdzk%2B6RwvWcCi4fvVzhid0Eo6BQoXgFNR5nq1UsX1VAY5K2GOBTFoNa%2FcIkbUypOyZo3mKGnZZdaWpSsiOEe471YmpuC%2FgaHox%2FRcEkeOGtcgS1FoZ5OoqX&X-Amz-Signature=75360fbaf1eb27a002cc565c283d97750f9309f079eb0eb9bd003edf5005ab1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHI25J6S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD%2Bb3aPeGwtgIxjnzn5aW8TozGWLeIRVPnwR3pqDqQlXQIgGkWV9kqyfjQNh%2BkGrTqE6xK1raCqen66%2BZQxsWR%2FaCYq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLIlPhwr2J%2FzOJhKjircAw%2F6VDgFR2NjW97kOv0vHnwegSRscYQ6apN42OsvqfyAsrcBCypi1C8fvPE2%2Bv2QZzVtyPfozB%2FkXW%2Bi0cwDSt7Xa9xFaYDBATb0ky%2BCvP351kuUhHMk3xwwcKuMHhz8xvLHHVaqBshfeWZe6IiKMt1kS1nmmmvHjuBeYEUQkgbdDXOYzf7wAcpppkGPk1H%2FPaRuwbnTs1Q%2B9PW7Is4K65HrM4A67lvdOxQQjfWJccH3UvSLlXTX%2FC88r3nNyEr1opAToykf4iYdA2D8nIcMRypFYpV0aac8kqFHysGMa4ZJCwF1ic64K%2BQDsQIdJ0NuDoBcPgj0edGUVUFQXC259U6Ng%2FnkK703v13QrdS%2F%2B6ciD9OPrp44MjlUO0ZZkjuzE%2FM7eoGcMH8w1CGEN1W%2FjJ3EANSj4XSij6wrvT%2F0bHuttXaUnBrew%2Bm%2BW7YvxODO7o7%2BjQxLEx8BlGA5bH8NyX4mYUuDJUevh2n8NtTTzWBiRvnuq25A%2BqkhFbSOSgOMsJyhDmuHqtugOoNLPDh5qGLX6CZv7y0quM%2BJqz5EbJomg1ucH6OCMk%2FXAi%2Fkrmh%2FDzlP7eCZB45Aw3yxukrtk%2BECvKIe0niqyEjsxPH4KOQPmL3ACGDqD1Taki4pMJ%2BUir0GOqUBqrAJfCNg3gkzADJImfNipOj70q9H94mka0OtfhcfCojApxevtnracOEpywpRiiEnL1QIAGpT36c9o7HiYtjIKM3qYIzKNRAKGYUbB%2Bdzk%2B6RwvWcCi4fvVzhid0Eo6BQoXgFNR5nq1UsX1VAY5K2GOBTFoNa%2FcIkbUypOyZo3mKGnZZdaWpSsiOEe471YmpuC%2FgaHox%2FRcEkeOGtcgS1FoZ5OoqX&X-Amz-Signature=68dde440b2d8c778185ebe87cde3df3b3d73fa5b13663b33f09eb835381f8870&X-Amz-SignedHeaders=host&x-id=GetObject)
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
