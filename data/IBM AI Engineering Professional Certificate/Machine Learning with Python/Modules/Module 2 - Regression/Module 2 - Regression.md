

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=b9dea0011693cd3b48930e5d6673d441e5bf12e92afdbedb98f28bc6a7ab90de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=e4b988e246b05fe1afda47027a06e8278bef943b93a8907a89f6fb788b8aeafd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=7b3ee162e9bf841a4f3baaf02ce181fa49060b9a4440ee4568c1d8f531b10edd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=c3784896e53f928351aeb62b54e5bd204a96ff4af9185ff9bee12f5d842f00d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=d3c3df86841c13eb609b49644dbabf294356fe173e15079fe85df886d976fd4b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=4bb91f6cb61249b50cd749498bd2b9d87e86d6603f5bf474225816490660a4ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=df9e954b39633a677c4ee6d4f6bc9a71478875b6ef225d40d5af1810c2b0cdaa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWUOWT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVBNyqVkK0dtlYEdKq9nDFN4JZ41fS2%2B1SOCQspbL9YQIhAKADQsxMyWjUJHKq775gYUp9XCNZsyzvnLxF28W7tKeqKv8DCEcQABoMNjM3NDIzMTgzODA1IgyzRGumIdzNBtB4tGwq3AOQlCe3ENY1I7PH9BDF%2BGdm5y9CkdLr9pA4SyF0WkD3tG51bjxO4jPF7kYlxeGXvEuf9tcQwPa9s9q2pVxdCjROkciJ6nzpvLPJ%2B2ICzEQFNSgdhvNjnC%2Bh1iZnU4NwLn13ad55G8WK5df%2FGnha8QOEBXtA99oreZD0FpqvIoXb%2FMw7sa6ppsbCoHlCvzAeEKWf5DTtowwZm5N8e1qDXZiTdctb%2BiQdYUepYqxHmPiMxcHFI8IRMUFo44TXaLNbhiqpASihOUGaocxzGXYXoYMcLGJx0vTNQ9H%2BqUFndOqyXUg6cw%2BGa6DjxBLqwztGTWgxrCxtgRo9D9V4djKZJzUlAxEUjbOA3ks6T45KUh7CIMDi6NsQnRJdzPyGhbSE0SEBbdzYo3uePn9byZMO7ZX%2FQu9MWgGMwNpYAPbwecppcmVC0yjHFyqfhoIfDuWCST0%2F8urxBB7TRjmNSK0wQaumGVTn1Mt8W2dTNjkIyccSgR1tYnWsxhE4FNy96itByICbHFWSFhwD%2FkynMLaiIUjtVD40oq9kd%2BGdvqzCSJaCHwBhKVpo0GKR4STaPv7Rh%2FqY7CDPfq68pEB%2B6LAuQftCmkZPR8wWyeXWfs1gb33L3ldyz%2FQsn6XeFkVRuzD74429BjqkASExF7ptRgLDPiEpN77Ma6x68df5VJI4yfwPV2uJ%2FUzHLhmuwZ4Wh6%2FDEd8SOf34%2BaL0MHBs156SbEF8gbOF2WbOUi8ogC22XvqpKiaVsCaOI9lBCGHtMXds28zsLfadyE82Wboi36MJCK%2F2aBkPsmEno2jTzuKiLKwF0MWg0U8U3ABFRX3vkLxieHWAPmGd3NbVJNSojWpiBmKSjYP0LtSuB1Ld&X-Amz-Signature=14a0854a66e005f0114af4a79321059ee17225c54de801063376dd55d564f0de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3KBGTMV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQDtDe8U2HYGrKdikdgCswfnho96zFtmLvdaRTb2IfbZPgIgRE8C%2B1hvX7Ja2sL7sIqgQnA3zCHJXf8XFNymVhK%2F4Y0q%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDIwuZ4d4HPnBUGuHAyrcAz%2BORet3ljzhYbFfEs6AUtiicKWWgKGISl5oZkFPxcahKyfSJPB3Sn9XDIytD53kq8ZgEz9%2Fg5skliQ3cCay7Ter1%2BiGhn5IY165i6j8Y0YIW3aNeiGV9OuPWgDJk1HgLj3oiqlUxSQG5r8K%2F7DF3p1rq8NaXanF92xxMu7Q6xlx%2FD9JWASD%2B8bO6tW6S1XOGgZ5rsnUlnynDYyscoR5ZVMnIWbfcMHnYZlSzd5mT7N7TPcFwwJDwC5CCjjX8USP5SpitCi%2B3co4nHKDsM92lwtyFCGUoEfI%2FEgp%2B%2ByCZ%2BDyj%2BBrOe0BsM5c8xkEiqdyr2Toju0%2BjXC8oVRzldApSXGWvzncqbDHf%2F4aAqC0m%2Fn9Q93BAk208fsWy0csWHaqlZiGZJVMX1MnvTPwK%2FvBvjQSMJwS38CgADQhFHp3b64sU56eQHRBSfy9877nZXf6w69JDFHBR3N7XTp88D2wJHZy0olk1LSUF8Yq2H0Bwk3h627qejeUZybQsoIWuWcrQ7BBk6MWjFNUmRv5v3FKSUELvNSZuN687OMnFaCU0iQev%2FuCh6mCMlu6hslcenH6BkbAeq%2BBhqIywjTYlkTNEe912LLYztRq87kZoXRlyDzBvlhl3H6bDhgr05k1MMKAjr0GOqUBI0IwkVxdCgs53j37U75%2Fq7C%2BR9Q7jlT7%2B9v3iuC6KKuq1I9qcrVIWDfGYCLRuVx0a632eXikRR0EaPXk9TDGRJdjSR0a3Oz8d3FgmD6kv1F5VokeTB8HlzLidViQGpOQPrV2JPysUeoX%2Bn9LC59r%2F9mLjfRLq%2BoYp4xcofUn2EKKQeDYQxo%2BfJkZyc0qCU0%2FAD4Dro6rd3nubYm4H82U6e1FlMPT&X-Amz-Signature=c22e20630be6a26a7bf5a2e676ab6faaa5c29dd163e644da74e1d2e00a8f57c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BMH2ISV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIF7w5NO2jB5QfLm7jsVvS%2BQ7HucovQKdFipvhR0AmS%2FfAiAxCmMH%2BJxnTZ1K%2B5ZiS%2BLRtghOiF63c5%2F0Vlr6mviSwyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMxPloEB%2FUhrpDPTSGKtwDIXVNDekvvE5%2Bo1wnirDHLr9BWYwQX81Zn6TFf3AYm8tjD808UFmboOl57b1euhBzJEOVfVyOJfovWAJtbSwsz4OWoceI8mRIKH11dcT7HZsVAbxLjSIKrKEUTfF7gSWqvnN4Pwa0ZLq2A%2FZBSEk2Av0uRVAI5MSELYm63nRAmUfy5M%2Fc7GdD5saCzaseB9majtReExEukI3wtXKx5ekzkKkXDOmqHrC4mahr%2Fc%2FH2Mem3GzZq%2BGtxV8BI1JAH16ZwCtpYzR1uaXMjgyuoVcqvAkRIzJj62En956UaNC%2FPt%2B8sHRfaZdk7PZsO6Q%2FOBE1gG4awOB38hXsDh%2BYfpLVZDfbWYJ1gr1JYUi1ROBxVOMnPRs8tROxw%2BK5u9qO8mZP7%2B6cgXFQxVqYWosunh9VSi7MuYmBYtRIoWnAg4l6LyUc%2Fb4IKGVqYKroPBE3FR2WcHKfhThX8yCjGlgYo5YMk9tkBKBhZHEAu0qoWDby7xNpwUZn8Pdylf6BjurAP4llDit0HUBCVYcdYCOAz%2FLBSkiDAxdORDxD6p94EBOv1%2BpWqDQaYANXwX8lDbdhneTOYIdrBeG%2FxHc0fgzyuqTQvX%2B39rbGiL%2Foi%2FYtZyXB0PfEKbK3Z%2BoFJno1fggwt4COvQY6pgGNufQdBuRjuVICTzb9NjKu3TQz15KGdfdzWRy66p4or8WVT0H2w8er8iGS%2FgDKZADta%2F15WQ2e2Tu2s0pKLQg4sORn2PzxWuvi59cA0HfM9WT9SKshuS8BiPTNfqqj4IVriz2RBC%2FzQ%2FI%2FqwP%2Fhn5jWBgc5CUFqZs91FfNQLPhtPNmCdZRSPhskkBrS5Sf1Xf9sVSy0v%2BlwXW7PDtpCoPmR%2BUp9hmc&X-Amz-Signature=7351620dc0d580694f5fed6b7e1b78483a0bd14f19d3dfe7d5cb7c4b27ff9675&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QEVE4U2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCSZrBvLyVrzAevsdgRap34WsWA7FJ%2BWB1nvuw8oX%2BB7gIgUv%2ByEkYX636ur2ccxDLrtpp81e9RzQ1nkRZYDZz7rrcq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGawj9myiuDMKuly2SrcAxup%2Fn2pKRMinxGMLxlzp1v2ErYlEJfpvU%2B1NT2G662kP20p%2BHBlLAbxyQOIFbzGGWj2VeicTOMBNDqbtpvBh0VNwXWL6vuP4JBVX7zhSWGKw%2BsY6Dcn5drTKENT1RmfT5vxJPB1lAb3EWRDMb2T58pJnx5j9nsMoxBINawzGyn5tZP0yD70Dv63%2B1oT5oHq302IZarayacySxanybxfp5g0IVaWXGB8rI2L%2B5lP%2BIsM0POsGOdprMg%2Ftv9ifOyOkePtdHa49CBK9Tx2Laz4%2F0hH1QjRH%2FetdDCRxKyOGgHK9lfAJ5L5jpx%2BCebjgP%2BiB%2BmLpLxzMAi6nAh%2BFYc0nN%2F44sxhYXS4iAtGF%2BiVYF67aaorKfXpvJ2t%2FbzD4GloMQRHxqEu7XXETwocScNub%2FNk4PPwfZ5Wz%2FC7v8uemCR6Ryp5RxoU06R9vYBUXUz1M1SdfLCsNPzoYcO6ATrL8%2BnlXnUZaqTDaNwmZGwbG18Vn0oLYoqSkCinRatVdsYCu%2Ft%2BfLUrWrqzzVb8h8YI6OXyu2vrJGetB75YSSDNXHXSOP2ZnJ8v0bLQ3Qfju46ovNibw%2BdPFklni5tpQ44FnRzIUnL%2Fg5nGNAN61d%2B7keTq8oGFHnplEyV36biaMM%2Fjjb0GOqUBSLdr%2BjyDidlvdSEvDcVt2NY8NGYA61FCL%2BsXatcW0%2Fmko24H0accOiOhNMuLWQZrfLDp9ACG9J9M0Rxg3UriHHSCmcZaJoXvntDxSGQcyJ3Uip8AtTGFQfRplRgIRRZ4xeWVavypuZWDk51PVp7PqqFeiqbi9fe2JCeqHEGWozH5HWcdSw8UCPmi67pLDBMpuiDhl1NKBz7VyPQaFwWoz1nHztU7&X-Amz-Signature=12d2d172a51e18010b87ccd4e1f6d3b4196ca5169d3170042a933e67369dd9ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QEVE4U2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCSZrBvLyVrzAevsdgRap34WsWA7FJ%2BWB1nvuw8oX%2BB7gIgUv%2ByEkYX636ur2ccxDLrtpp81e9RzQ1nkRZYDZz7rrcq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGawj9myiuDMKuly2SrcAxup%2Fn2pKRMinxGMLxlzp1v2ErYlEJfpvU%2B1NT2G662kP20p%2BHBlLAbxyQOIFbzGGWj2VeicTOMBNDqbtpvBh0VNwXWL6vuP4JBVX7zhSWGKw%2BsY6Dcn5drTKENT1RmfT5vxJPB1lAb3EWRDMb2T58pJnx5j9nsMoxBINawzGyn5tZP0yD70Dv63%2B1oT5oHq302IZarayacySxanybxfp5g0IVaWXGB8rI2L%2B5lP%2BIsM0POsGOdprMg%2Ftv9ifOyOkePtdHa49CBK9Tx2Laz4%2F0hH1QjRH%2FetdDCRxKyOGgHK9lfAJ5L5jpx%2BCebjgP%2BiB%2BmLpLxzMAi6nAh%2BFYc0nN%2F44sxhYXS4iAtGF%2BiVYF67aaorKfXpvJ2t%2FbzD4GloMQRHxqEu7XXETwocScNub%2FNk4PPwfZ5Wz%2FC7v8uemCR6Ryp5RxoU06R9vYBUXUz1M1SdfLCsNPzoYcO6ATrL8%2BnlXnUZaqTDaNwmZGwbG18Vn0oLYoqSkCinRatVdsYCu%2Ft%2BfLUrWrqzzVb8h8YI6OXyu2vrJGetB75YSSDNXHXSOP2ZnJ8v0bLQ3Qfju46ovNibw%2BdPFklni5tpQ44FnRzIUnL%2Fg5nGNAN61d%2B7keTq8oGFHnplEyV36biaMM%2Fjjb0GOqUBSLdr%2BjyDidlvdSEvDcVt2NY8NGYA61FCL%2BsXatcW0%2Fmko24H0accOiOhNMuLWQZrfLDp9ACG9J9M0Rxg3UriHHSCmcZaJoXvntDxSGQcyJ3Uip8AtTGFQfRplRgIRRZ4xeWVavypuZWDk51PVp7PqqFeiqbi9fe2JCeqHEGWozH5HWcdSw8UCPmi67pLDBMpuiDhl1NKBz7VyPQaFwWoz1nHztU7&X-Amz-Signature=1212012cae50b8846088b3cddf874954f29ad05e319dcb18909931780c5beb41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
