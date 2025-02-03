

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=6ba1d8395d5b940a891afdd3e857bafe575c93ab0dbce88f06321225b266d47d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=5d5b7f84b17da87d37deba17d65ac9c41955acf42998d477cacf8d795cfdecf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=b8523875122e04dd1032ff77be8dd7ca9834f2a14bc704f76ace137368f9c081&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=287f864b8438aa36ab1bf931ae0fcdd18030b57f23079df7c2e8915b763a5e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=d0e864a96e70dd076c388bdafbfc9cffd0a169240d3ed2fb709b799032a3caeb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=364a2b7f8dc68f9f436b9c7e02a7d24eac6c5be36cfc23f04779ad2dc54079e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=20cd2e4989af386ad2e8f5e125d906cc41fb3f934b286d879dfb0b267b7afff8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2VFASFN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET9I4q%2BQoyBFN%2Fchshd1tC1JwUrNbSgA2TrYKfrUvWrAiAHRJ%2BobqJddCBvLNrp8ye%2FMrq7KoHnYvPIxWY%2FmUWd6Sr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMAItu4EEdNOvwIYieKtwD5fSQ6DnBXv4ivXUJsruAi7aNMIc493BZvgChE7RAzGBgJZTSm6s080q022Xw%2F7PIFmIKy7TjXdaYor%2ByPD3aA3%2B8T0lqhOw4mpvSLdqKjN1H9kr8BsyGyfcEsBrlta%2BkgL6DjWS2XvCLW1LMLkBXyYdbc5pGFG%2FFCBqia005IE7eWqjaLlBDpVVoj8h6HN7svUtKxpIV1%2BmTpbkgRV1VE4kriG4ldqUB%2FAn%2FEuAaFH0RsLOPoKD5fLWS0RFHpZeYhz6SHgKqvRW9t4GGOdGAEZgAbnhi4T1NB2ln3mSa0xAYw8xvKUvLKtXVG4ZVHrgZrVJAC4TKR49QiRoR7RCU05W2cwLcaLOOKppeH%2BE2aE6Qzu7YZVuAUcRNQzkX1WA1RRJjP0B1Owkxn5x5Rmfgm6HwYfcMw2%2BSETbGFSXA7g4Xr%2F8cM%2F4BFFd13B6STJk8bxMHyLAY2BoNNhORwhfQfyTbP1cKpLoWOsK2KrSHmTkYbX7eUPH%2BKmX8AjBx1FxBeQcIuC9m2g2rSA6I1WqkjPBbam2eUuMCBXR8vgrkhX1EsD4owAbUp%2Fodqvfdp1tleCZ6ZOZYpMVQhE3K7GVY3waOGlOMN2SsVeYKO8ZFPGK27X%2BN%2FdtfF5UF1scw9o2DvQY6pgFzjLwACSCWAlM2BgsGWpIVwqD0L5CZK5w%2Bq4UD0Jb%2FYge%2B%2BH2nJBN3DxHZfULU4A0kILH4rxA1EjGo2rnd01qOW8QIqsntjeXsYX2KmNK9v1ZMSlHnEC1m%2BWOVBLjmX5b32xqxpr%2BiH6ds8CJQ7sv0dEAzmQV1%2FoVxS9dPLI%2BGuSdIfz9hZGxk9KsS64%2BrlOhE%2FN304yMZT8djXDkkhiGlgKgePOWo&X-Amz-Signature=6d7185b88d8b1d10ee2d437e7aaff5115431b01e0d2f87dec9afc54280bcfbac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQZPM53Z%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3NTkqNa1hyhgNLQGXqHt4MrzNOrN93B8WT6Ez8U2TgwIgAhHcR3ylSeSKtOb%2FLcX3RGTEm59FBjLCvGXJU%2BtfDk4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDOG0lqpistzaW%2FMBBSrcAzdOIIam7LvtNvUhnyahgnw23zp9q79T%2BcOArmeNjH87SAHjuEn5NiAAvKEGJb%2BcR4hv%2Fu2gc0OUaMQoMomBkAmpWRFo%2FjR3L0zVqYV80eevCarNAGSLYjBqyB0%2B79vFs3fFUHOHhliub5GoqAFDRNcmdxKqQCTd6CEuYCfMdCDostoSBgj0Ji9gl%2B2AlL2LmcEKk%2FwW%2Bx56irQvLyBbFVeqSKiKMEgp9hptelquNDxAMdSjpu%2BMRLtY1SXXoZJZP4kzIOsxpVVZPCtWGfrgi9L30QD%2BED4iBmgUCTtWxbAHtKVc%2FapW6Ed9Csose9iiOER9xDiCBJIjWnAM%2FFDrm4lxCPkkAC5O5ueFNfwJz%2B0PXsiDgW27efuVTYaKpbWVg9dZXhEs9cO%2Fd1PJlmZ2aiH7F9E1yIsD4Fb%2BmQeY4bJDSPAo%2B2maE4hubehmlfN%2Fwsz%2FTdvOmugU3HH0%2FPuBDtrThLz%2B18YLn3jRcW5hyfWT6fpnkimnvXJtAevsGUQQ06OlrljO6xonE%2BZRSsDBUqRpNeaS5Cp6nhLsMSWSEjy6o22IEuTu%2F1XeuD3iAIHrhdl1mRPQrWJE8ZZA12JUw%2BBW4Yk6JTrrYcAeTj5l8qGCKMAXS6GflvkceqTKMLiNg70GOqUBlF%2Fofivt%2FcRchdnbeatVCCKslfuQkGj0cV2%2FmYDPWMgwf4PFjDl5D3HsvPX7LMbTPu7xRvoYnLr7rDbMSsQ8kEvxgbD0B35L5qxJ8NXVbCh1w15r3uMJS0%2BZXbefN09vYA%2BuqeGe5z7RlGf5z%2Blvb8iQEkL4RHDv98%2BkM3m3Lr79IiChbYqxZS444I%2BfT1yx6oI7khwOyT8%2FngaRr1Zo7OpPNjAI&X-Amz-Signature=e729fa7b4a950ebd74ff32e9594a99be9a83333b7e9ff6a6eef77e881d840809&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZ2TSRE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLfSKFtv29ynfH9MvEfwe508W2X3iWvRpVlRVaAysbewIhALTQl9U%2B5JhpMplo7J6fkz3DRHvksHkkII021mYmV%2BX4Kv8DCBcQABoMNjM3NDIzMTgzODA1Igz%2BAjFlTgnZmdjcDJsq3AOIt5q%2FlYdLmU9M%2FH%2BCbCwZJUOKkSeoDV%2F%2F5CGao%2BtPlsEhBq%2FuxBBaB2mt8HQe1gS0hsdV4Kf4afSY1FHFIRScFH3aHV5mNpuirD5iQchVdN%2FBCktQ6aNpTgskZmblBVHpsev%2Bv2TnR8eKlHovpEcwSGbAmMuZwgVnBkiLMdrjdLyrGJIPqnGmCBY2SYZt9ZpiNR0F%2FWREq8y4wB5hK5hjs1GGf5qDYGZ0nD3twGO6Z%2BGx9ejXJoD3T%2FZHYIiorL2zZIRMJI7Efdq6dlSM9mGLdm15OFrqJJFsLyHzALhKMg6FdWWefArDg72sfjw0T70f%2B9v7a64PhtkmS%2BryLrpkg4l7CWtreqAPeLAY7bjAJSFbqqeRadWI3OipFBMaJr3887v%2F66DR%2BhviOAtLug8dLIUE1JrOqGodmvblDbvG8mG7JpJePP9zA9O%2B8faAR%2Fd4nbFbR8XrAiVeGYgcVXON38W6sfqw4pUWY8txL9zoQKLf%2FFalgOw5q%2BS0YHRy28fmLfG2y2YH8%2FP0awCSYVkPpITenPBaVeSftWA8VeKRJIvixRLQOoDH3epp6b%2FLHS%2FMv5YSV6S885B66yCx4%2BrYTS5P6oODh%2FdcEXHutrYbo1xNVtFSqmDJJo4cQTDkjYO9BjqkAcoEUStjQgsetDdc4PvpIcMPXCHQ2WipnacD%2BHeWdNmv0%2FszlQZ6sKwPanC7llH5jgmx5GrxTMSnJ712LKyjwHkBC1i%2FYRP8dUxb9dnyYCZBMzWGXF%2B7nkY%2BaxnApxAOmqtep%2BjYQJYfQJOz8LOxv%2BD0AAe6VfAIjG%2BJ3mNyiLHuoUwtYHRuH5Ij%2Buq3n0U2RAKdXYPuA7pi8k%2FwUL7W7OcB3Dfi&X-Amz-Signature=61e6bf0a8c09327fe4e6aa5eabb4da8e1bd6aaf1e99f61868c476d593c68b53c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6266RCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmMiiVcJGzCuFvEEosgAO5suQOBJLiBHkYilicrUIVmAiAJHWyzJaX7pPC663tN6iMw92rx0NOMeN%2BTFMVc7OutHSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMMD5WpdYqG3kSGfbKKtwDKJxyF2D%2FinI3eAR3QJAcGA5IXJoNO0bHAfNJB2eiBD6h0nQdhlwZXfo%2B5XbjhACi5OZGnBXjILvsEfmj7WqAVx4cTa9xLgCRB0ojrBPqGWgrBuLH0ogs2P7Bq%2FJEv9SdFB9ErRkgZpCXoIPzZTraipaVe3w1aB4mMdMDwlNbAwsv2FQixGORG74yXaRFKQJ079uFbqYIQ5XZc7Pu21rwu7ewt9u78J3L3tAC%2FS2vmeZbpM726ChxGxy2eUuh3MYytyY38vq8zHFcuNbU7qJSmb58shnJ8jS8pEZlPVZjLj7UBhFdTefUWYk2VTR45HMMMJY2F0LbF5EJqeDKi6pwH%2BqolOYfWEug9Z%2BBsRIDXxgExQxNqcoE4G%2Bq7SsoDVIQDhZ9CO3RcVzn5Vtw6nbQiW%2BCpWHwTjS%2BE2XoqZ9afcp8sXQrGTu6KtiareCwpoaPQUvfI5gFp6mzHuAf%2F1sku0goMdsCK8RxxE1O2uE7pzlBikmrwSX3zRyW9xOQUyWqvj4GLtdSfHM0%2FkVE3pjuNOQL57hiUnGeGKG1rluqLdvtDbqQGJXRWMcng%2FYRQAu2YV6J7zsHqX9%2BecMAgFST6iwsXrKDcE78ZqPr0WCb6lhminwY7tb8h8MzJJcw7I2DvQY6pgFj5V2uESJExZU8E8g5rTjHW2qt96Uk77xqj%2FTSEVlE5SJgtkoa1cZWk14%2BkM0u9jaPnjO9xVr%2FKC%2BP%2BHuqoUe%2BfMgzq5CJZCMoPNzL3guHkvjs8YvcPe%2F%2F5xfuTKxzuY7OWfVNQg4iy%2F%2FbA4gTTPL%2FWmDu8P%2FTwMSYk9zJpmw5s0JN%2BjKFxXSfKKY5npBZciUw4Xe4J9txzPg8ziGgzS5NXQTtRDU7&X-Amz-Signature=46ac11a086434a91768ada75e21901167e36280ad055ddbc3586d327a1800f01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6266RCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmMiiVcJGzCuFvEEosgAO5suQOBJLiBHkYilicrUIVmAiAJHWyzJaX7pPC663tN6iMw92rx0NOMeN%2BTFMVc7OutHSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMMD5WpdYqG3kSGfbKKtwDKJxyF2D%2FinI3eAR3QJAcGA5IXJoNO0bHAfNJB2eiBD6h0nQdhlwZXfo%2B5XbjhACi5OZGnBXjILvsEfmj7WqAVx4cTa9xLgCRB0ojrBPqGWgrBuLH0ogs2P7Bq%2FJEv9SdFB9ErRkgZpCXoIPzZTraipaVe3w1aB4mMdMDwlNbAwsv2FQixGORG74yXaRFKQJ079uFbqYIQ5XZc7Pu21rwu7ewt9u78J3L3tAC%2FS2vmeZbpM726ChxGxy2eUuh3MYytyY38vq8zHFcuNbU7qJSmb58shnJ8jS8pEZlPVZjLj7UBhFdTefUWYk2VTR45HMMMJY2F0LbF5EJqeDKi6pwH%2BqolOYfWEug9Z%2BBsRIDXxgExQxNqcoE4G%2Bq7SsoDVIQDhZ9CO3RcVzn5Vtw6nbQiW%2BCpWHwTjS%2BE2XoqZ9afcp8sXQrGTu6KtiareCwpoaPQUvfI5gFp6mzHuAf%2F1sku0goMdsCK8RxxE1O2uE7pzlBikmrwSX3zRyW9xOQUyWqvj4GLtdSfHM0%2FkVE3pjuNOQL57hiUnGeGKG1rluqLdvtDbqQGJXRWMcng%2FYRQAu2YV6J7zsHqX9%2BecMAgFST6iwsXrKDcE78ZqPr0WCb6lhminwY7tb8h8MzJJcw7I2DvQY6pgFj5V2uESJExZU8E8g5rTjHW2qt96Uk77xqj%2FTSEVlE5SJgtkoa1cZWk14%2BkM0u9jaPnjO9xVr%2FKC%2BP%2BHuqoUe%2BfMgzq5CJZCMoPNzL3guHkvjs8YvcPe%2F%2F5xfuTKxzuY7OWfVNQg4iy%2F%2FbA4gTTPL%2FWmDu8P%2FTwMSYk9zJpmw5s0JN%2BjKFxXSfKKY5npBZciUw4Xe4J9txzPg8ziGgzS5NXQTtRDU7&X-Amz-Signature=dd2c695f4a97b7b2ca5f78c2874cf19b84d562e4ff3afa0308b58bae7a54557c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
