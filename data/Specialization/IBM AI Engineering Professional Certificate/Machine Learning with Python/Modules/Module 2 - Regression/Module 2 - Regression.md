

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=ad88c1ae7436de36f8506cd67e795c201eb3bdf7c986708b0b7bf8577fd50f32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=5893e38aea65ce3fe474d07f8f93bbf1ffde4fc4c9dc26bb8b65121a08ed4035&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=229c2a42ccfc1fcc1a02bb38acafbaa68450748ed6cf764c3ca46e9e060e9b3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=160d709a197fdeef945c4bddfc06ea2215802c6826daef9908c6bcc16852563a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=e5e64a8d4bb134885cfaf82bb6dd1e5f4fe9c182759b3983469b968c878baad6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=8fb164489278907462a9d4b902fef440bfe25b80c2e055c0da77ce998b9d268a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=4467236ffaf630447b2486a3b4a510f65fff53af54e8cc446d1d165a90420a05&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LSHV5B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCceqcVpK7tTuMcBPvcxEMz8zs%2FWxWvz%2BJ52B5ga6JUfwIhAIDq8B8dFOuOVs85tk4cAbKrnvxUCFTTc%2Bm6Kq704JaLKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTlcMgkbkRdN%2Ff6VIq3AP3G6%2Bhy2JGI9vz4JgXoWAbZbRmD6d98XFTMLx3B5A8%2FwgHv%2B1JKMB7UctGiMAM62HBj1TsPx%2F6LPFW%2BcY9IH%2BLNIih9OApXpEdFST1NWddZ4NSCa%2FrALDFuiW1gU18wAzNmEUeddf13RUf2y6Ao85Welt6uwD5OhPChxYCJ1SFQAHt57EG2eZ%2B%2BihAXPY93raIDd3qMaAtQZPlV480%2BbMP2CKGMdNo4C6v8HdUKQiY93RTXWJkBam02WBjxIbeugt9%2FUyzEPom8XxPKz%2FA1E2uURJogl3U5F8cgJK7eCZywLjbjVYfCHuKtY18k%2BbqYrUSVQ%2BwsTOwuK18bedR8%2BKLjW3Ew4lu8W31G%2FgMYRmlPelik%2Fc9iwhwix8MHOIxqh3kLQf0VU4XWJkrS2wgSMkFj6tFR7cvtUpvYeyLnYBJs4Y0AdxlFewrY59yy04ySTXiV6mTUOpcan8KKOcpoyM8RKmR%2BKbLMWPpbN9FI9uPJAiCCGZiw7A0eiOtc8F7JWTDzi2wXkBWYi4M431ZRIk%2FGM%2F%2F%2Bfeu2anHchjc0uMR4ydUQ476W2Tl7jAO5ocwiZH4%2BGpd8z%2BwO8rgH3KJSQs59zr1xjAi7IKk5yE0RfrfdH5svBkyGnp2eL%2BGRzDhg%2Bm8BjqkAeY2zKp9oKmhSh3eVTd4wHFvIe%2FR8%2FLoJ1VpsR%2B1fa%2BUzO%2BXQuPRHFLrcK5WEzVpDd3V3zSDNw4XEOCPYzT1SuBPDr%2FpsdmeLxLlVl454jJkcOblCcIIIKOsJqpkHoZEvCdrRFmrdowhG4cu6sAe4jYNxgMHn51FgP2MwX85EoqrhjhHG3t6Q9kuE5dKKr2AG6D2Ws%2BTmf2%2Fqe0XUDAtMOw46Xjn&X-Amz-Signature=fa05e2c4f43fa8963e110694c35dbda860c22f4bd5b187b1792801d42e41cfa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQV6XNL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFcq1YaLVR0uUJMt3Dn26cEOqzRNW7cq5FFsSd%2F1OPiQIgdrcb5bMDjFlN6qiaIN561wUMSm%2BKEjvgGWWUCqAOHOkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNAGyGnrsZpqdCt%2FPCrcAwn3x7q5tC5BdQS93XT89jKz%2FaHJSQja%2FkqjupxT%2FxO6kt%2FN9%2FM2mIN%2F4aJZH9qOgb7%2FO6aUVuNlRWwm0G9u6GhN7vtCGlfZaRkRFMJe9kVGjxZIQsQnaIU5frUGw3aMvSXHEdgnOuFIHRUz2ZUiEBFf%2FDrMwoQMUkMmLF5BCLBPwS5IPGZPTG%2BrqY%2BxO9TV9eCLJufklFXKKufbgI%2BRxEsyjOdVm5ri6wwOvtVd3YTiNXx%2BPGJJlwlJsObHM2%2FufvMLKtmE%2B6EfRIh0GnJ8TDz19Sw81c3t6yszPb3mfARzjpcFO48EnXygSDFDlpY%2F867VyptJ2sxb9A0P2dO3s%2FxUCsqxFym4BiXJLm%2FR%2BFryIE4EJXhNeMP%2Bakbp%2FwTY5j9NaOJfzvi9WoQyfXtx5XIB5XcrjFAdHmhbTH%2FCy4TaA2uncvIE10ZPr%2F0%2BWy7VdThKwzuRMZvg2qtklC5fWGREwwE4OHXk6PgnDbsvtiH8AR5aEWdd7JcT%2BgxVQki9PNuBQlVv890lNqdcEaWn0gqkAo2CPZGK%2BQfw5yfIA8P1Ber8n2SsTrrSxDPEes%2F5vm7SVaj%2BoPzqWPRgZ9AwD6zKCbJ4ePm2Jn72ols%2Bi%2BonB5ADgncuY9Gg3YW7MNWD6bwGOqUBG9vVJWzDOcFAXZg753NIliFUagr7muOrr0FKdmDJovL2ROkbLWObQtQAfLsnC2SxDkeG1CadUlhmWt5Hdo7%2FHcxV44EnaZLTBIMrTEEnYODFpspP2KqGrjQyf0HAt6JRBJmykbycO%2FoiJ9qhu967xIsY4T%2BApJrTtfrHB7c9bwYzEIghvoTwv%2FVEt5Mje%2BEQG14AHpGDOtF8Dqg5Eg%2Fk8mCvDJPJ&X-Amz-Signature=5b2e0ace4115b123ecd6863431dc03a11cdb684ed4f66ad284a8400f9c9dee06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEBKC53S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4arEddJVa5j5m8RG%2F%2B0WpKIL2PoKvgirLewM3vLJmuQIgdPqGwxpD9gsrQJElnnwuXapPZMlMPd59X65rXIyocPcqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq4cMQLB%2BrDKvY0KyrcA3J5T3XhN4JvkH0iT2iKdPi7CjmRG4sj2BscrbEj6v8HvZEwi8xhv5Q%2Bg1258fOsKeQzhowZSW0tdt1uKJxFsaKB3PLZlDoHhfx87OgluOvdfaAGBEunWHSKJBA13sH5WS0AZngZrlQP5GI1z9B0nUR%2F3EOxIEpAN80S8%2BLotXkeyl2KawSjBIV%2BXEFgoXJ5nsUjPzNJoBg5FvzJbOzQXS5fJk7i2yaX27dMYTlP5LFfKZuTAP6hka6qIajNAMlbE1WJlmoW8MxxOnZ%2F6F%2FNmS309hyC6fFwrCddaMKASbSoJ3YjDRTkbbmr7iGsoa1B90GKvyV5%2BbIEWG2u%2FDcEFUGtaa34Mq%2F1vzt0xe2ERQhJ04sGc1h99TCRP7D7OL9zQ%2BzUQKnnFm7kUuQRp5rIeg%2Fe2LGOn6VWiGHKIwsXAKaFZVjMz1b%2BlU4i4plE5SIyFNmonQzOXznX7l2qimc5MKibJeohazCKUeeaD%2FfMnNld5mVGafZMANR42%2BzlpOUt5Rva2v%2F7fiMXiHgUqsov71nyBHb4mkCZVyHgUZc1a90rJUYH4cz9aPdxYunCI6tLg53OAMPt6%2Fmdd0D5gPTo5UUFMZofgzzmHjxZog4sV0xy2o8NtcCrIVwygwg5MIGE6bwGOqUBbZXUmLpcJ7OQQErbc%2F4bBFQyOAHnIno5rL8n3jjmZFNuPV81YxETTL88EWq8A%2BXgpu2NXIbzvu7CZTOHzqfROos6ypkqw4dCTqP13xAa0%2BBwlZunmTSLmZU9IdHKo5H1NsgRQ6m6R7bYO1E3WAxNBbTVWSJoTydWpDqC4kB6g%2F6GXrnGyKQaDS%2FDw3ufD9VqVNXdbiMx%2BlX7dpLNGq%2FtiBex2R7B&X-Amz-Signature=43bad4d4e936a6992138739876e07159d83ec31236200284986858aa0d0096ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EPQPEGR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDu6T5BoFPi%2BRrj0EgPpsYOhnVE0QKL9KrEtPl4vLQQKAIhANRAyZs1fFwl3tnof5CzQ5LWiT80NX8bptIIPv0C3PjvKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuLrkMxvhGIVSYauAq3AMVaMHgGT1xKbuQcKDU3ZBGEqGsZTv2UMp0MdyjT4CWAYNAbsihp6tlU%2FZNYQ3TK2mHluLNItzUNH8wWgR13L6FXsIu3IFJ9qGO2voScCnYLZNHEbROoddV%2FsizFWJUmbsbZStH68HphoIVIWubuX3Huk35oQQPmhEtkMt27bXgp273nXWOz5ZUlXktWLVcIBhliIOW2U%2F658jKj8ClVzvRRz%2FbuDleDN0WGAyvOYAusVNSv5NVdBeg56KmRNklTOKqRBc7Xem7L%2BS06RHSJzhaO5Vt%2BOkW2TiUSDaGGVbR4piLNipuy2FvYv%2BIJGrvY4eqbumbSzfNpMxVyZFwhKKWbrBQjXUJTjrgiss6TuUx9X3aVWQKQ1ju41bXrebuYVIF43eh1I%2FKlRd2k7IcjO0a6My33fBuQIXwQ%2B4iG3hqYla3F7YwC50yKbZiHGQl%2B8Do6EHiJsKUn4D8zRbd0pikf%2BvOuKXBD9jRGyxsMNiOLvCA7hU7U00W3g%2FA%2FPJCUKPn5k8OSH1i0qb1imt%2Bo6wyqO84d2MpkYnNWBodyT0BYvAzAA3E7nRt3T5bMi2L%2FSxDvCQtY%2FJsrOV7%2Fx8maBgTy15NHOVF2Fmo52D3VNaNIzxx0W6xk3OO2H3xFzDwg%2Bm8BjqkAaAhFMVBR%2BlC%2F8B5sh29eQCCMXJz5HegPV18X%2FLdcyjQbGSfonnrCZNxGlmJKofmMK4myKS4ppj7UlRZwMkKum%2BoXl6A3EHyxtrTvOytgI7Qdz%2Fu7zBP8EmmdKrcx5tAV%2FF1MwqstbzuY9HEYF7z1OtWA%2FdstFhLuzGiE5A7Hal%2Bc%2BJa2iQ9RMFPpO%2Fbwhd4g0KDn5GM510dkguKWy2qNFAaNTMk&X-Amz-Signature=16c23bb050fc3a3930002879a069f8131bd3c2653a17f01b5a890d5fab346145&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EPQPEGR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDu6T5BoFPi%2BRrj0EgPpsYOhnVE0QKL9KrEtPl4vLQQKAIhANRAyZs1fFwl3tnof5CzQ5LWiT80NX8bptIIPv0C3PjvKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuLrkMxvhGIVSYauAq3AMVaMHgGT1xKbuQcKDU3ZBGEqGsZTv2UMp0MdyjT4CWAYNAbsihp6tlU%2FZNYQ3TK2mHluLNItzUNH8wWgR13L6FXsIu3IFJ9qGO2voScCnYLZNHEbROoddV%2FsizFWJUmbsbZStH68HphoIVIWubuX3Huk35oQQPmhEtkMt27bXgp273nXWOz5ZUlXktWLVcIBhliIOW2U%2F658jKj8ClVzvRRz%2FbuDleDN0WGAyvOYAusVNSv5NVdBeg56KmRNklTOKqRBc7Xem7L%2BS06RHSJzhaO5Vt%2BOkW2TiUSDaGGVbR4piLNipuy2FvYv%2BIJGrvY4eqbumbSzfNpMxVyZFwhKKWbrBQjXUJTjrgiss6TuUx9X3aVWQKQ1ju41bXrebuYVIF43eh1I%2FKlRd2k7IcjO0a6My33fBuQIXwQ%2B4iG3hqYla3F7YwC50yKbZiHGQl%2B8Do6EHiJsKUn4D8zRbd0pikf%2BvOuKXBD9jRGyxsMNiOLvCA7hU7U00W3g%2FA%2FPJCUKPn5k8OSH1i0qb1imt%2Bo6wyqO84d2MpkYnNWBodyT0BYvAzAA3E7nRt3T5bMi2L%2FSxDvCQtY%2FJsrOV7%2Fx8maBgTy15NHOVF2Fmo52D3VNaNIzxx0W6xk3OO2H3xFzDwg%2Bm8BjqkAaAhFMVBR%2BlC%2F8B5sh29eQCCMXJz5HegPV18X%2FLdcyjQbGSfonnrCZNxGlmJKofmMK4myKS4ppj7UlRZwMkKum%2BoXl6A3EHyxtrTvOytgI7Qdz%2Fu7zBP8EmmdKrcx5tAV%2FF1MwqstbzuY9HEYF7z1OtWA%2FdstFhLuzGiE5A7Hal%2Bc%2BJa2iQ9RMFPpO%2Fbwhd4g0KDn5GM510dkguKWy2qNFAaNTMk&X-Amz-Signature=6ef42eebf53345c5b76d0aa416befcda75a2626d0cfc7c1f20106540fc96431a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
