

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=d0ad496a11720e760531373dbb8f768e105999f13526aa08755bc4f3bf225fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=d42111b71920c401f01062cbc0d5a94cebc508d137543fc42a4bda544b3251b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=20ba4330074a5670cf31a3644c3576e29e362f153a942df97b5be19c3357818a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=00db85577771ec6e2ba50d11dc2f7671204a53f83f1ed8a405b690c6cd7a94f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=a2e8fee45b977d53560eeed14b41cd88b65e27bcfd4065596759b26151604a79&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=da558d79a37910e717e9dd1b86bf967b70a3b1f130e45b0d2f9f6de734386f41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=14526a0b4e2465415ea21f9a18b7bacce60d89bcbd6e4ab2013f557b00fb71b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFILISIP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCPNxeHGcSPvQbscM7rKkqDs8yT1s5YppGPOqj7OJsgIhAIltUf9dI1Hs3ToNS7kBEIAuzZ%2F%2F0oYupCkZc4%2Fp3xYVKv8DCBEQABoMNjM3NDIzMTgzODA1IgwV3U0RMNdyl0nkKvwq3APBG3bNHs6r0zEIPeWS1ahQhbP%2B%2BnZizcpkAZOTCVwaM1J%2B1C4vu03%2BBOwqATFKmdGYh5WSBl62R226ihj7kFUmjCY7FaZavAT2fDfgNq1tFpL9lQrEIzgAvlAR4Hg92hA5uybY218ogpR0R3dRHgzYzPVaX1p5Ehb2P6Y1URs2wLYwWi7EyT34F1GAOfCzwyZVrDCw4PMbsCjwbZxWpfdp2Q7UZCvERFInh2Bfm2iQ6p9I%2BsmthpmskC%2BrbMxQF65B2hXU6rp%2FSuTTuWcTlXZDHraDmxQaf%2BSt2WaZ1oLKVHA8iMCP7ZLSrNhnP7m%2FxD%2BXU4mLBvcVP9rFfoLnX0PLP%2FrUBmg2joSTrw0gEEyHT9kCHr8hnCjj%2BpFP5knZ9GALA2R7GEBRJI2N7gh0wawywvftHQVbcyFfgdxwTfxXogaRfDraL8gZ%2BEvYT6Ou5EZ8dK%2F8zPyepkQ%2BPyPchCuAsVkCtsWxrzfaQfKp%2FNTCyxQCqM2oiwv19xOH%2BW4rwNRdZ9p3W3CZA6SLbPfcOjKPL%2BHUAjqfBkjHsYorX0mkMb6tZ69Y4Yzuehy7Equw%2FmPUZqoljQq792JGeDAa4gdfRM%2FwT3Zt4BufJmdK7niZBfbh8Lx1ZM5o%2FZdMazDH84G9BjqkAa11cPQeqB3mByXKjDv8higTvwNfw57pR8BFuOixkF01a%2F19%2F8OmD8c8FKf3kTwN%2B2GTvFmNbCo%2F8GKtLub9eyy0axNV4YRHv9BgtqLZDw3vRE2hzJ7jSREtmP5GVt8WlhgFfgCOuYqw5VaTtR0DXB6rYkIB7k9WRs8M3Fvdk2oRRMnyHFgWv6sovegGdQfgKtQbfhzFKs7iAFuC1mK3MubIrj5M&X-Amz-Signature=b7c7d7862eb9455c0cc82e43958e91a9bad5b8fb9cb4319d41cf5eda500bbb38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDKMKLCM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQmRwRP4lZQY5utDH%2F8rxNbCHCKqvVD3faoQ8ufuAYEAiAfa9E%2FII7diyWk%2B%2Faho%2BxHxaxVYY6z6BIVdWj%2FIjdiCir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMJoDq%2Bdgl0d46znoJKtwD9Yyb4aWZfs8M04DheV16FygnNtMTJzgv7fD%2BqT%2BXJdFNPPonYFIuwRLel9HxLQf%2B1HfO04FwZp4lUmLi%2BUTBCTl0At7eH%2BzyJ3WC08Pd%2FD7ydK8XTJ0TkVAo%2FHUxLSbgVF4s7Sq%2BCWaBVby63Uu3SiXH9mHULE56oeEo9nRPJ5558l1i1r6%2B1ouZ4NYLibnXfOKGMojHSN5HU3Or16z167n%2BEcRH2xPto7YuYiObYF62LgSxtKjEgLnOy2al2vYYcP%2B7LS4e2%2Blfw279qY3m7OLsRu6Dgk7PUBTosD7XFhioDlwIuVEaR44W8L2kxCs7A6QzfqSvV1wkTpIJrYfYo1KCf98lVxG8z0Y3YJTse2TI5firBrxxHuv3Zbffs1hxIneaScwba9ZWBewj6j5iSCjiz7qovGLxcsB%2FxUof3%2BDtQma%2FyFte4etEX5ScrtwQZjJTF9rz12cp60egMSrksvgqOvr02H1BbY6jBrgMRG%2BGdTDvqHhoai8%2FiJ2eIsU%2F%2BUVJWFMOi9uuLqApqnusLQWwDBfwzdhZH9DhQCRgrUWAM21sgywvBC478UPY4R6xzu9A%2Bnj1f30kRuszBKG%2FeGEzLxCunB6uohJMJKTN6VKN0O7f5hZTjKF%2Fhzww5%2FKBvQY6pgGMKlHraZwJYuOzHxbupI86wrcSvX3NEdiJZrm2xPs169LkHAiHE4B56URP%2ByzGrKSMpudcJWWPjwdGAEDnGlSACxzf%2FrQnqv6eHxutm0NzLygLmAQXyDRtR2HwnC4%2BpjypZ%2Bt6CTtQcpiO0ogvQU3%2F0CPWHgor0dM8GbDmhC%2BJsXRtVJtgZDZB03ngro4iOX7mLN9F7%2BPDUq66x%2FuJ5k%2BeNhmGINQj&X-Amz-Signature=584bfc076ce307d178fae8804b695c32d53082d72ad62842dbca5cba8692e8b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662NOMYM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzNncP3eBq0QyAnoUpHuEv77rCKKglX5xu97w%2FLm804AIgNcfYlIG50K0SZF2LO3BPW3TnANmEr0MQXz6gm9XuXx4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDK7jEBPOXTfZv0fQSrcA4c0Tr7A1JaHnPsFz7LtQoiEWy4pBBQiFj82ySzdzfZyyDNl8a%2FxV5fsKf5OyBjERn%2BDH5NxoWyXTQstp0zE9UkZC%2BRHJvwOqeUsBxsthHpa38Q23Pyt%2BmAfgOLUpi9wX6Zp8kYeCFyWWInFLMwoxmtOCdVMjxKyRxcuz4NxlbLOYNY5cblJhtRn2LlYRFP7fyezT2G%2BWLBUebpex%2FoHoiA%2BlVKz2RYAW5Uw%2FgLmkLeIgYR1MgjnkdJQhRNRqaBwcrfmK%2BUpvHp8K2kOYNU6%2FXEJKc7WlA75MoyeFwz6grewyxe4ztBqbfgwhfleAfveo9SuC4BGgpIXeQM9rfYjWN7R%2Be%2BAcx3AU8JiDChJ4MkiJvrRCZZ0MUV29iC0GJhhjK9h55c186yHNrjyME6gkY3EdWxp2wXYkd9DKV8UsdeICjfsjKvVqIfedocAR%2BudnBJkV3uskwXDdGJyujDipgufvQ8rTz6Fw40PfmMKkGLriFk6ceMuhnZriGNdCpcG7%2Fu69dgN8jBDmHNPEAiJb3%2Bt1R7onrbeikZ2xfCc8xz9eIXT6mHgUbqSSLKzqj8gsZPBTACpjkEEqPbly9dBLwOzCsuhuX%2FbuAdUCkLX%2Fox2L9f6TS9bFp99qERgMLnzgb0GOqUB0zj%2Fd90eJb2H7%2F93PQRHGRGCG4xR4mMPQAV0zB94HutFKqRVGjAUGVpMYpgclMgouLzQ4AbVd6t87iTV3wp%2FlGKIXvT8Z1dmuIySWCbd9rLiNCJZADOOQFYkuPtG87U99%2BuPuJxxjU%2B6jP4YE566q%2BQ3jufHck3ejtvjY87Nt3IsYPIfHc2fuYEFuSVSVebh%2Buwg0CQvgkEThI1Y32gpwvSAy9SB&X-Amz-Signature=6c45f809f581f452ea4e4cbb582173c282f439604e46dee06271d378161fd10c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4CPSBE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgU%2FY095jhM7n4FbK%2FwunbXceJeBfnPsiK%2BPWKXThLHAiEA2wPOpspoqxdv11CmbDRDxs05HlI%2BiAvJ3vpNC%2FY6QRUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBIkwGFKzJh8A1LLSyrcA5enIC%2B2XL2n1vtTPw9%2FSDgYIEMWFFr0GUnIUKyRmtBez52RzqcfIp%2BClXFefdvxExQbjb20XiMw2%2FZsxS7%2FAogjcCliaA0r%2BFRfcT8KlABZO3IKhT4B17NhJ4YGKTnUr65HdF54LoQVEGYH6PL%2BO59ll%2BDjXRCFwKl7vDJFeSvaK9MDhXMwtrmP5gZ4xn9jIYiL3iVbsMyDO6rfE59BUOE4AAluDDAvHaP5ruzS%2BCuKft%2BvNolqLf5cj1mxHJQ6Nc5w6kl1rUk1q2SdUBi66UBC%2FXPzEmhTlZ8SrsmLDgK8GcSQAefuGEdZzGWpBEby8ptmhIz6NmNLHDSRiVDhfbjLoGym0QDxjyMWusNNTI0kpTarZjQVwYb1H8FtixwSYZfybs4GJOurhsxeaQHPm4jvqe2DZJmtagAKavEaDgKlUlyMVL9qxPBovrLZlUKCXfzUJ55pVQD0qLb7dB%2BLiz427iXkwkN0ePGYide%2BRIYZ2mh2C%2FE9hgA2dEnO%2FuzlHUFK61xRH3nipf%2B8nIoD%2BL2kTxXHInk56IsJoG0rKtGApX%2Fg9jI93KUcYkmXB45MHzs4HAGYyBgSRtjxpFoMmVZIfcsjSHqMlBo4oiTHzNbRrfF9XkdWep%2BbC7N5MKPzgb0GOqUBd1SbtDmnDiLP4O1nCPYeOKLRfZBQC2ohRTxw0dwtOlegn3jmHlD0Q5z7QDRGnRl26tQAh3YHlp6sHGO16atdJmrRbBSRLOnKYXh67fAcRooZnso6aPGBiT5BVe%2FDA7kQfETQzRyQ3zOHcUET9vuCupPHRUMMmIuTWZISM8p1%2FU6RWDdF8GcljtXf2FKycBcOvxDNWbUjMocG%2B%2Bn1BLILpMBQUh5Z&X-Amz-Signature=c1808805ca1bda373a4c7da85c97bc7da948928bfb61eec4988c9e85bfa1dc00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO4CPSBE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgU%2FY095jhM7n4FbK%2FwunbXceJeBfnPsiK%2BPWKXThLHAiEA2wPOpspoqxdv11CmbDRDxs05HlI%2BiAvJ3vpNC%2FY6QRUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBIkwGFKzJh8A1LLSyrcA5enIC%2B2XL2n1vtTPw9%2FSDgYIEMWFFr0GUnIUKyRmtBez52RzqcfIp%2BClXFefdvxExQbjb20XiMw2%2FZsxS7%2FAogjcCliaA0r%2BFRfcT8KlABZO3IKhT4B17NhJ4YGKTnUr65HdF54LoQVEGYH6PL%2BO59ll%2BDjXRCFwKl7vDJFeSvaK9MDhXMwtrmP5gZ4xn9jIYiL3iVbsMyDO6rfE59BUOE4AAluDDAvHaP5ruzS%2BCuKft%2BvNolqLf5cj1mxHJQ6Nc5w6kl1rUk1q2SdUBi66UBC%2FXPzEmhTlZ8SrsmLDgK8GcSQAefuGEdZzGWpBEby8ptmhIz6NmNLHDSRiVDhfbjLoGym0QDxjyMWusNNTI0kpTarZjQVwYb1H8FtixwSYZfybs4GJOurhsxeaQHPm4jvqe2DZJmtagAKavEaDgKlUlyMVL9qxPBovrLZlUKCXfzUJ55pVQD0qLb7dB%2BLiz427iXkwkN0ePGYide%2BRIYZ2mh2C%2FE9hgA2dEnO%2FuzlHUFK61xRH3nipf%2B8nIoD%2BL2kTxXHInk56IsJoG0rKtGApX%2Fg9jI93KUcYkmXB45MHzs4HAGYyBgSRtjxpFoMmVZIfcsjSHqMlBo4oiTHzNbRrfF9XkdWep%2BbC7N5MKPzgb0GOqUBd1SbtDmnDiLP4O1nCPYeOKLRfZBQC2ohRTxw0dwtOlegn3jmHlD0Q5z7QDRGnRl26tQAh3YHlp6sHGO16atdJmrRbBSRLOnKYXh67fAcRooZnso6aPGBiT5BVe%2FDA7kQfETQzRyQ3zOHcUET9vuCupPHRUMMmIuTWZISM8p1%2FU6RWDdF8GcljtXf2FKycBcOvxDNWbUjMocG%2B%2Bn1BLILpMBQUh5Z&X-Amz-Signature=9489bd75461da8f4af19b4009b1de5dc912405e8b192ef541bc7d0050a1f6a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
