

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=cb0b065b89ce4adcf8bbc99d3a41a77b5e367bd8c570e83c7a66ae3075221073&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=1f57fd6971d2d4ded79ea93938d6d3c86b62d1676d7c38d31652b62f0e7f7190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=bc9ec7697694945fa91bf1f63c957a906fbfffc4162cc2b07f683b35b62f9e27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=ff538ce4d984e2cee8234dfc3d214a367bfa6ab689d43fa13a0708088beebeac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=a1ccd4a0dd64d34c041766710a9104ba0484249da1546c69f587f9bf71825e9e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=845621bc48c1b09fb300bfb9c2b6582569b8fc29cb4ef142e59242c99223b1f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=ed199969884d000396d38521e03810edef888e2ac28939743f1944bc3527f63f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REJOG3WW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIB6Sw4gNsgYVGHb7XtAWjQ5gmy0C6BqUGvpOuAyInxHkAiB2sgKil6KiYkUwwPRxMXIM7FIM9kxASDAf1yyTpVJtkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCV2u%2BHXeurWDZdjnKtwDYTu3yMyf1c1W%2BVCSMvRoOw4savJz9KZwq66kCEreqmDrGZKeMuS16HHG75B4P2oqS03Wq72XYjkDgxP8qpqWKz2wBOErwrd4yG0C%2FGTvijdwpav3QcqmFEn2MwY5Ve3FSgUX3gAGHVoON3Zi%2FIyyvVvEN%2Fi49yrk4Nt42JN6%2BRlcARcpN90GYH3pcEbkuYqCs7iLpdaPQsH06l1GiL1gKsYjNPn8qfJNXTePr3vKlDekyA7%2BAOm0FJA6nazPxjXjMEdGaFLnd%2BuBF%2F%2FUxAgxiMVCpFrAXh%2FxyKvhGsxU5CryicTA0AlJKDmqec0qVPrVyZrjWLVEU5NY1xhgcGNggGPs3Azz9ypo8IeqpUe7ybtMhdGPzAfSGek07n%2FSRS24Qbw%2BtsFh7XtsFeJEGa3w2NPTclXzGwc4MDGiVc%2Frae%2BZ2rTlFzUDC5f2NyI4Pd24pCRiVF8wrS9bn9qFl3vj2s3MF5IJXO3H9DaBhJM6jdCaI7Miwqsq6kt0LVjl2hLuuUufLQYKWXSvzINO90OB0V6a2%2F7zg4rEidCa89fI%2BkO4gjQuUpfUaDx0FoGkbviLkWrdbzZoSaXU57w8zr244fQNJs4cVRWdkmyMKgVN5Ry0BFz4%2Fhr90OTvt5cw3LKbvQY6pgHWgdAt0bMJEVjLLy2xsJscZEO1daQ8Zxba1shsNjez%2Fex38hW%2BZfF9BsiTZXzR9ufS04gSKkdg0yT58B%2Bkk%2FUzpyBzPiN8svxwJbppVBUkwr4NixgWqQyPXCnnjAv0KNkKOpO98MkuFt2re4N9TTiXSDZ8D8W3ZKqpLhw3HGDkzvVC5T6%2FZQ6FnxXzR41iLpPW5tllYbLrYJkqW1rQPVXhI%2FHV%2Bvjt&X-Amz-Signature=af8d4ee97135dfffdf8ffbcde66248bdc6d30e485a81ed0bbe704db419b0df2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5B6PRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHqXWJThgNOjx3eykc1FmFkIMB4vbb4EJzRez8ZCxX%2BcAiEAlUDjuSy6EAryW0kDVOrmrDVTwdkFnl%2FNoKBpooKdX9MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIXHNye0QSjj%2FYNSfSrcA0QsqhUVsV2B84LDmLDlFp07aBFGBhOw108x%2Bp8a5t%2FGHO3Ub0sM4CrtvlMmWffVTHyXoju2Hf0izhKboFQNWqdl7iwfhljb9wOydvHM4L%2Bn5CIru%2BonJ8oIjQ2cQToRa5A10PIlHS8aT7LtfrBdQck0bOBqxbo4LNtW0o5KS2lySiCrHFRkNI8iSUPEa6lpf0yrrttaEhEABF%2BoHsF1uKdqCVZmJzu0lPAI7hbTIasoxRCOWcqJ%2BrZSmR77IcVFB1TfhaE0ObAiE4%2BKlyLaHan0vrnNETOO5a19A739%2BCc8XurEjX1t4XBcwCFqO6JjUsDQ%2BUWrTYDS29JkTFDzo6ttIpOqq5T9powTm6fS002MGLPRTKoxS7UlQOEbtfCxCXGVSo9aR3BoWFreif%2BAoQaftAXiYtromwLWpPgBvag7N6bL94pxeSqakWkDKEE4CmvqXS9wMWOOzsO80ameWGf3%2BO0V0ID7RuELcZGL1OZM%2Fz29vaNPIanRow0DX94Wm%2Bv84M79lCY1w5QZfTZOQem8Li8zl9kRlPbSAPN51uEHNWAauyGrn0EJF88YLEYAaKpWgg%2BZlMZVOHvkQv4WW2p3j6M7xKSUBxbfuqQvE3xdi7QaDZozhNGlfZpnMNCym70GOqUB%2Fn7HQ5fkHeALYmpKp7nI0aJBdhz2gREvXptrZEYEgDsDv%2FTr5DZVnzY2MMc9Lrxo3EPzF7kUZJmFuh3%2F6rMFbsVplQEv7vY7HVM8i%2BHCtkuy9L1jrkKY0XC1oOHgNlgESkfNjqWkX2wVtOzNwFCXIlLqyIM9jKHt7eKXUomIeT8nDVyVDAZ4OYAdflTkRKDbwmiRPaJAOUn1IrIiHJb9hH318ed8&X-Amz-Signature=c0e2e1d31024e0c5fa0b828e4a7ae22804ca252ed1772624fec7360de8654dce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Q6UH3RE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDFyeeZ1ZWTzIOI6Py%2FsiPwNXS3Z7gEdg41yGrRuu%2BqewIhAPDB7sBVf1kiWdDT1Hpac3l064s7QZwlURlEpxPNrR6ZKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3zUl4tGMgbcwEDoMq3ANFjkYLsl%2FXDc3UfKpS8X81vP6Nngxqz7jq43ugB3bVAhfI9KNz2epUOG%2BhgQmNasN5btAC9u%2FXraBQstN%2B4hiOisDfP6ahAItnBcImpdoR3OLn45qzBhnNyRyNlzsswCaSNUzludTQ8h%2BKEM%2FhK1uPBB2gJcm6sCsWjwaQKX8XL08dEnqWBrk3O0nDFEoMT8pKztUpc1kCUBQZ8cCgqgju71iEy013sCMdjN%2BYyc6ukUweRO8aQ6UE1yc1DGjVP6xkfswrRDq%2FQX22G1VHd11RRKx7c5ZzHtP1kAuoz%2B7zz9Qyig6CxiW%2FMqnqc9nR7z9tec2fYE79bf%2FIzfzdSG4aCtbYzJO0ZQdGf888M5vitXL0kPW%2B7gOmbCoaV6jjlh7nUwK03ZM0OBwrnK1O9gS8RYV2m7ki%2B1EGnncF5ri8GZp%2Bk%2BhhlRjQWW33z9mqLUgOIRYbeigQ013IisbU66wH5H4QU4kPQ5GnmP%2BYriJ59slDgLVGVJhhAu%2B%2FJLn7RU2%2BEd7s9W4bvaqWQ90idJYGkgeKF2gcupy0Hbrvg71v6NgrLb2rOoNC4KAh0lu2FEhdSPtZBmaTOi%2Ftz%2FSGtdZ4O4gQtFWdVGeX9KGajKWu3aIafqlBPI8RA9sWqDCJs5u9BjqkAe5LeBulrh23OutTYyWlJXGRrM%2FVmFCXDueRPpEnLIp%2F5AJE%2FjH%2BN2p%2B%2FGtXK3JIAY%2B0%2BxYghOYOWuUa9PywqmtZdNS8GtdUycMFrfUzJg%2FLTPRvfuHA0TwA%2FOdQkJCSPXAUMgL9qKBv2ud5IKl17T2IecXOUpwkcd7U5PrPN9vHcFKCdlY1s%2Fkb4B9SCLcak9clWvobSqgwXYZPiIAGGL5LBneO&X-Amz-Signature=935391b4f0803ecff28b589861376f23cf38dac8c5d289f718a3852569047080&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466444VDCQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQD38aK2WIRPEGUtuC1d5stDy5wgGiG8pcX8w6Z0L09SUwIgQDPKDclhWOVvpPjRkOKVGHPfsaQ9DsdGDkdC5rHWkyYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgoLh1iU6qWfdTaiyrcAwV3jItMrnQQUFp1XY%2BvLyNpUQW2j0r8bZ%2BENpGBuKUM29F%2Fhr1ArYf5HdTUVYIle9bPEYm%2B9KR3eXV%2F4qjANlW%2BCTf3%2B0dXNsngDnNlchwUdmcCYKpnlXRo8IeqhIY2mw1gm%2FzrBDASKyl5KVLVXkNW43jMEGeV8EZ%2F4rx%2Fl5tqCaWP5Rn4B5%2FetbEcysa%2BR9r8BHkLYQUhzx4nvYMalM5J032eUJc1ceISTt9mcrNZF5R6lKOGH13tr34xSLwbqFobUSXaVjXgxaNNK7J3lIHnCsIcUs8iOqoxOKnjHe0i85G9POD304wjG%2Bd0sjsbMVtIHfedQSWAOwKmoNgbfSepnXmWFasiw1NWRSPW9CKZiJGFrN4clvIGf1HHUC9%2FfEcyml75k6SzIosUWQquGtPeEbKeO99GfdS45H1WSIN9p3HeEGot%2FKvhmm1KMyphm%2BkYpSdw4e4cQMcVBZewwxSxinypfAb%2FkgyHgtXmySt9HkGMVPfOXMxhruSfwdkHEgpJUNQEmfhS2a9xan08C2qPdX6NKCmBczbqQR2Z2W1%2B9%2FZZGTbAI5bJXKk2rlf%2Fy9%2BRA6MfpZA1xBRJ%2FWE31OGDO4MM%2ByQilT8AvFfKzJYxnQGNeanHWWHMrF4xML2ym70GOqUB31%2FchE9T6Y0w1V7%2BKUxYFbEPgbM5NbhayCW66ss8a4%2BZXcT8%2FGJWq4c2haQnUjsQafl5yr0RN374xaJOUM8HYHQ4fAoZ8yUNvn10bKxNsZkKPthwchNTr2cw0nbaAkKMrjUF1vdPgATXI%2BZ3h1LHKWMKl8PTyzoEaVki0didabqtnavGBgiDP5k7hml7%2F1zcqbFbfmkUeBb8nq6K0EmMS4f5zqyf&X-Amz-Signature=cba622930091307bd448d794e1a002dc13a20f950f7d597eabeee518d51b5562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466444VDCQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQD38aK2WIRPEGUtuC1d5stDy5wgGiG8pcX8w6Z0L09SUwIgQDPKDclhWOVvpPjRkOKVGHPfsaQ9DsdGDkdC5rHWkyYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgoLh1iU6qWfdTaiyrcAwV3jItMrnQQUFp1XY%2BvLyNpUQW2j0r8bZ%2BENpGBuKUM29F%2Fhr1ArYf5HdTUVYIle9bPEYm%2B9KR3eXV%2F4qjANlW%2BCTf3%2B0dXNsngDnNlchwUdmcCYKpnlXRo8IeqhIY2mw1gm%2FzrBDASKyl5KVLVXkNW43jMEGeV8EZ%2F4rx%2Fl5tqCaWP5Rn4B5%2FetbEcysa%2BR9r8BHkLYQUhzx4nvYMalM5J032eUJc1ceISTt9mcrNZF5R6lKOGH13tr34xSLwbqFobUSXaVjXgxaNNK7J3lIHnCsIcUs8iOqoxOKnjHe0i85G9POD304wjG%2Bd0sjsbMVtIHfedQSWAOwKmoNgbfSepnXmWFasiw1NWRSPW9CKZiJGFrN4clvIGf1HHUC9%2FfEcyml75k6SzIosUWQquGtPeEbKeO99GfdS45H1WSIN9p3HeEGot%2FKvhmm1KMyphm%2BkYpSdw4e4cQMcVBZewwxSxinypfAb%2FkgyHgtXmySt9HkGMVPfOXMxhruSfwdkHEgpJUNQEmfhS2a9xan08C2qPdX6NKCmBczbqQR2Z2W1%2B9%2FZZGTbAI5bJXKk2rlf%2Fy9%2BRA6MfpZA1xBRJ%2FWE31OGDO4MM%2ByQilT8AvFfKzJYxnQGNeanHWWHMrF4xML2ym70GOqUB31%2FchE9T6Y0w1V7%2BKUxYFbEPgbM5NbhayCW66ss8a4%2BZXcT8%2FGJWq4c2haQnUjsQafl5yr0RN374xaJOUM8HYHQ4fAoZ8yUNvn10bKxNsZkKPthwchNTr2cw0nbaAkKMrjUF1vdPgATXI%2BZ3h1LHKWMKl8PTyzoEaVki0didabqtnavGBgiDP5k7hml7%2F1zcqbFbfmkUeBb8nq6K0EmMS4f5zqyf&X-Amz-Signature=05b20d094524a484edb37161e23e6d9aeba953f2cedab9950b0bf7664494fcb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
