

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=a1b92e8cea93056765e8d8ec6c8bf81e884bfb6b9744ffd0e8a55ed1e4c432ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=b969f6aed92ea1c2a4c1fd9f95af2edf27d5bcd08bad2826bf15ced06e2c4644&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=ee7a5d4f6b0444d8a50ea3fb9a01cd199a51f8b2e97cd5f24be901e23a56edc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=05ab38ce713db0341485a799bae7b28679c98b5d4c790386d215170f79990e90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=4a0ac8d8af8fb136c0e7487a9ca8844d15b187774d766eb1a6ce2ca482d9eb13&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=a2962954ba788ae171d628943e90555bc9a32ab09c0012d5ecdc718740326a20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=9df591a860c9f248baa07fae04098d65135573808aaee41f0e8bb83e56b16e9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSTTCHJT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDagDCkOvezu1YtsdFwSed0NjM%2BDY9NO%2Bz4Yy%2BRBaO2ogIgL10QIAbYNfV4r9T2XNbS%2Fbu9lNzfdsl7g9u1odg2bG8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDEje1myI%2BU3qID6X9ircA7tvytzkfwFKmgjpOtRT71CN2nh0xdCU0Eo4GFgdEaTmOD6S3URGlunxXNgyzoTBI3Sk9CMTiR5rIELKA0eV%2FH57iEsEd9XPPKNhy5lE7%2FLdBHXgA6L4M9dx7QcR8ZjuybDBgTj3r6Fnevu7FT%2FIKOgFvgbFVbUrNYXr4FzcxRr630A7X6zECF8eelvi09JrkAwdmz26SCOjf9UePq%2FjNG2itp%2FzKWks1DXvCr4ZVdhQC6lSuww8LKGlK%2B4sy%2BKfa4E4U3Rrf9Jkjz6VKfvpquxwg9eFIzSIlpWVkopychH2mgd3ioRZHZhdDAYRsIq2NkrfIgLeU5rrAgjaejhls4KbC2cPZO6ecuNpFJh4%2Fyd5jrh5OEgxeFnKntRx%2B6goBc3lgIsOonRk7i7wk3x6Xn6IBmnQUl49Zn%2FRdy6%2FSZnizPRnZEivXBQZqxh98iQDizpl3wEGtz5%2B2Ya97s3HpK3cItBhDWoIkWObC%2FBZI%2F7etPoORHboqusL39eGvhHvN%2FgZPBJiii6jQvPBaAjhWyeRxwkvvW91iuiEFaSi4eebXrRBSOZIBZjdr%2FCbRKNofmNlHedrDB9Xw7NUoytd42NtD3HFSI4pyO38u9Ed0tH61qVjUT0UaxGNfIbGMIS1kb0GOqUBpnofRIFzbUwGThYXlEfZM4wqalkeNyMxbOSnkBc3pNwaFm%2FjqxXUg4lbUhrd7ZAHFgKJp%2Bg7djY%2BgzdNfGA%2BMxvjwIoNW6Te35XCxd9fq4eEu50G8awVg6Do7BV7Ti%2BcpEw66InygJmNQQuf5RcdPgjBGALTfXAqTpakV%2B%2FzSSr%2BwB224cnyUpWPOw2iTcX4s4Xo6gu4Z9ZFm9gPN6vLRilJxNMZ&X-Amz-Signature=6661fd3ef27e2b66d461d63c9c92dcc138792b3252dd91ae88890b3de4b7f906&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AUSANUM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCHFU5TeoBkFr711eBDBYwUNNtOuq1GcdC5%2FU4jesdzkAIgYsl0ntYgF7q1J%2FQGBcqCm2kJlfvNDZhmW3xyCCm5kDEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDGXGwZVNYYgZ6GUr0yrcA0mloCGHemiKzOwdxy7iq3qCcuQy%2FPDA2Unyy0M%2F1nwoO5EIb8Jn4210rD9qZ2bQl%2B37b4xakmLuycJdwmLdpH%2B%2Fz6YQExc7XscWDCbECq2W4kf6G3GoVnnmc7Lld%2FIvleBuS5GZaIRygVoHtyuFA9Gk1Koep5WqsHqbOH1sr04Ako8YIYRNdUo2AWiS8bUvx3k0t5LAJcG%2BzNCbvUvpjw9cI0fuw7DvYyi9ylly%2FcSvW8k4FxU2%2BhHGLST6rJF1l%2Bw97WnqEtL%2FFohQmuT3l%2FmBDXJpcAa%2B3%2Br%2B8FHk0gQr9rB45LiiDfqk3DT7gOJJCAjmuhvyMjRQYCg5hcl%2Fnqq2yBfh0O8ysMBttX3e1%2BJXjwIONd9CYeABajg2a6yaTTIDQVc%2Fu%2BKEhtZK3qtWceqp5RfIyhpsHKHgkgR46v91ebKAu2cpxl%2F14%2BS5p4y%2BLxb8TZl63rfIXUQjc20jHZTai%2F8Ccw94BNJHd8pboPO9xNY70Q1FXy7iI2hPqksvU%2FfYyACAdDNkLUWt7hFfNxgOposZzQP2nJ1uDLYQxfQ0%2BgP96y5QuC%2FUJYaKebqkL9KrDkpw30rPgCm0LwqZcaKm8eKvJEqmj8cy0EF2rS9aEVfBnP385KCkLXRiMNO0kb0GOqUBNpK%2FlnhAkQ5paETFH4OwbNZuCic2hSoWr2t82vR4NFn%2BoTJmGacIyCNkt%2BoyaTWXI%2FXMqmoFbGLYhbyibyxHLDnE%2Bn27lsYktU7o3wHkJCKUbHvXx27b%2BoFE0dXHIDUd1u0BAnW7PqCPP7JLSz%2FWmyCuFw6bpa2jCTNCiclIabqM9%2Ftr8YU%2FFZGgo8JT7v3YBzl%2FJThYWdQrYLzf1BF%2Bweb0kf20&X-Amz-Signature=12b82b127193afc2621f5d4888dd649dc84abf3bdc27bd635ee3e6628a2f8ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B26VKYY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIBLI1M0UWShIu4JzIvhJ8FVozpLtwwJ7DajelOYRIeKCAiAecoA9l6VwYpsz6hEWJAons5YzydiDovAS%2FFgblVfkiir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIM3Wkv%2FV%2Fxw1aIZyUAKtwDYLDiK5TYhwV7040ns2qkGgWe8agUlne7y9C86TL226AeAs3oHgs3pzRGqcaoI5uCfbxFNuKjTdR8xNsvKz56ooCQdxWu%2BKaDZ7iqLQYLT6u%2BE2oXmlSKOkHiyVTbeqBkzJmIZdmQEi5SUZ%2FLSo4tQRrzk1tJuQDzGPWPiYYyggmTw1xd06WkYh0hIDoUAqQed9OF%2Bo8E12MWarNmT4mLp%2FE4wipqxeL%2B2l8tHBxBGcDmLzX1yZ8R6D65UGYmtQHTeQn4sVn7YpdzWeSmBo5bKXdJOpzrzdd1v1shFkjDENBpSprMMQmJMRk7aM5kGG2ou0nb%2FntFLjKiUrVLjjoq53rX%2FhOlF%2BoipcRpmuaHMGw9jxYd7H57HwVZVEhgSOz3%2FeRzZP3yxvXLt4jZWjyEW2panzBvCrsaRvX0rCxQsOkyqh8lPZOp%2Bt4fYoEKvPYJcVRF6hu12hW5yPXEBn%2Fm6UJVYjN%2FO%2Fl0dAXOxC0bonuewGGMXneI0iXE%2FuPdOK8T4pQOP%2BjzsH4u5V%2FfiXY0gI6lzEstRLUnzn06rJatqqfZ6znmzG8FewIM6p6ipmharI8Wi7lyALuEKxvyjfHOB%2Bw%2FV%2BqDT9zDcSe9LOPFdKg79SHL5JnlhnDD8Ggw4bSRvQY6pgGMH9qMMHlLthIqjrwORH1T89FLolIK2DxwKsDq%2Bf7BS071eyZ3%2Bheow8f89ch0wig7xRAJDEky0Eu%2Fl7OKuYM9nI3MERrMJOTQiy16r0BTm5JAm9pRHwS%2FRBlOKMHdI4LOraUJrqBBb0n%2FO1oM4Azp5Dg2M36eVYVyKvp2jmHjt%2FXfLvs19ERtWa2uMZcjEb9pWmD4bvsOQacpeV9dmZTcOh2ReI4B&X-Amz-Signature=d3deb53fdab059f78eb53d8c63edd8655611655a8f05609303f5a1b52aa1f46a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGPJDY54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC8PTso5Iz0VQzKAynsD06lfpa%2B%2FlUOG5lKGRcXJa5WFAiAdRcWmOeI%2FPuBhpqH%2Bu7Q5XgFej%2FZkvOwQijHSbx38ISr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMEHKge%2B9Z7WnB6WglKtwDZTpVTDkGloab33hRLE6RjHtEnr7icqnYDWrkO2NnfuZgM%2BNbHn9xpp5NswWfHF8NYOBfxybD6r2z4Hcp2qzVEY6luBthZ8Xs1CMzWfeQL7zEM8loPfShGSvpl%2BS8EDGZHrI8xDWDNn8bEurZBvnR5ARJp%2BYa6DhzDjg3pyt3buPi6Ko2ziHxLdN1%2BLcXCijPXeRVwAF%2Bj5QFXy1cj9QPPhFvp4riIEn4lRu5NchERW7MtnMvC8L91QRCOAykpO0De1kzWjbjKpkHuusPsQktsLa02g%2FqFReOK%2Blgk3WDGgP%2BdV0XmSzZbh2rk61qbD5eRmE7mqnIwYKbLgbuE8gXhiYiqaSGkhKz3T%2F5HBS9P2t6UDQUdw07jTlGD29aNXpbZsWcNzMBAublxA6T3bQl%2FkstdyHJRnLaU7tR2IN3IJytYlJBd%2BLtC016eWsHoSChdeAmaciAS1ge7lUCgxDI%2B6uvrGAlu0aqWP%2FMcHJwhzH2%2F0x7kfsOt8TqXrYU43Pu85gfe0hP4mAxmrjsML%2FyWK%2FKx56EJCNRejwykH8cDXiNKWmSK2eBhqWfPNmyapjK6d%2BINmaMd2afOOqovvuLtFMK1P3Uw8IyQ0n6eewB4gHKmmQGbxAqIXhLIX4w%2BrSRvQY6pgHgsk1D3tB%2BVSzJY2KSqtlvWOAK1ehZukHOVLldXR2uc1GGBg6NjyYer%2BJ49jshU8jcUh4q%2FpeA%2FLUP27ApLqovx0VTREc1%2BUXpOiX9ue3Ujx17Sf1384SENa%2Fz0auzteK9cx%2F2Sfu%2B4We%2Fuoq%2FSPIajtrutDz6HhRo4fD7Bh%2FkxIbAjhSUV4l0c7ISNNHd%2F7HNFwimuFHXXgcR9mPS6F2eWlnl1cia&X-Amz-Signature=0ce8d21f200614284fe30d5b217519473ac50876dced4b1b3a3a794d50d7b832&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGPJDY54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIC8PTso5Iz0VQzKAynsD06lfpa%2B%2FlUOG5lKGRcXJa5WFAiAdRcWmOeI%2FPuBhpqH%2Bu7Q5XgFej%2FZkvOwQijHSbx38ISr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMEHKge%2B9Z7WnB6WglKtwDZTpVTDkGloab33hRLE6RjHtEnr7icqnYDWrkO2NnfuZgM%2BNbHn9xpp5NswWfHF8NYOBfxybD6r2z4Hcp2qzVEY6luBthZ8Xs1CMzWfeQL7zEM8loPfShGSvpl%2BS8EDGZHrI8xDWDNn8bEurZBvnR5ARJp%2BYa6DhzDjg3pyt3buPi6Ko2ziHxLdN1%2BLcXCijPXeRVwAF%2Bj5QFXy1cj9QPPhFvp4riIEn4lRu5NchERW7MtnMvC8L91QRCOAykpO0De1kzWjbjKpkHuusPsQktsLa02g%2FqFReOK%2Blgk3WDGgP%2BdV0XmSzZbh2rk61qbD5eRmE7mqnIwYKbLgbuE8gXhiYiqaSGkhKz3T%2F5HBS9P2t6UDQUdw07jTlGD29aNXpbZsWcNzMBAublxA6T3bQl%2FkstdyHJRnLaU7tR2IN3IJytYlJBd%2BLtC016eWsHoSChdeAmaciAS1ge7lUCgxDI%2B6uvrGAlu0aqWP%2FMcHJwhzH2%2F0x7kfsOt8TqXrYU43Pu85gfe0hP4mAxmrjsML%2FyWK%2FKx56EJCNRejwykH8cDXiNKWmSK2eBhqWfPNmyapjK6d%2BINmaMd2afOOqovvuLtFMK1P3Uw8IyQ0n6eewB4gHKmmQGbxAqIXhLIX4w%2BrSRvQY6pgHgsk1D3tB%2BVSzJY2KSqtlvWOAK1ehZukHOVLldXR2uc1GGBg6NjyYer%2BJ49jshU8jcUh4q%2FpeA%2FLUP27ApLqovx0VTREc1%2BUXpOiX9ue3Ujx17Sf1384SENa%2Fz0auzteK9cx%2F2Sfu%2B4We%2Fuoq%2FSPIajtrutDz6HhRo4fD7Bh%2FkxIbAjhSUV4l0c7ISNNHd%2F7HNFwimuFHXXgcR9mPS6F2eWlnl1cia&X-Amz-Signature=a42539484645e4b3471b9fd04cc93a52689b920a38c01ec338edb002c5ea3d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
