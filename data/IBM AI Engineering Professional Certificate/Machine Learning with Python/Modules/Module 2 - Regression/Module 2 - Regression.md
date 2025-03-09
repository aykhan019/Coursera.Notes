

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=44f62257cc349d7494b2a8dbac2e529ee5bf19b46eac2ea081fa30d88f7026b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=9abf34002db23e21489ede4588ac947e3a0bb655e1d162d92ab713f54ee78fb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=f5e788b6678ad08337ae34ec0f2f3510533978683b70428a45fe99d4aece0b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=f15e01ef4210f329f0c52889db8ccc9de18fe5339dcb6872eb5a8af31cb9ce33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=38dec5176106024d6030d89f90fb29293ebf74dff275753bef10523609c1aedc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=6e6773229e35afca0d14058f35930eaea005b5dfa0d8a919461aa808d22d9e4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=4cead568afdbc38a7be3f8e9238410f6cf9b6e33ab9a7aec5e8215d38060d8e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVX2HNLW%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFSVuB8YEs3WvGhVGgqyWUuZ1ZpSGgcypnOiQLvySB3lAiEA0mlI9AC0tDxhE60xU0nJqxvbEjMVaJACxSFAZKUoHt0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK6seT6BQJp0wVHf1CrcA3uPmbU%2FLBdu8gtAFfIlF7i9xzc9bGyy0awo13hdR1CjvcDroVd65hb0u4eJoqFjBWwv1PlWQxNBWIcCL8V1hzZLuxvakexp8lOg0N%2BEavRQBQtvyCuxCT1kJjfOjDfgAN8EGaS9B3muT%2FqIvPTgPsC%2BIXYPZhbVd3b3C72LY7CwERaOChGBMzkqBBBF6n8rPwzrrilOl09WpTjKt5OjMl5YMkZyYLh35NS6rZNk%2Fqx8zyBON%2FgpNkbFPg%2FcpWFWYpn%2B1%2Fr%2BTbHDC42Qo2KCDg1juNosbVEuFnU%2F1%2Ft6W38EGyJ1x9vc2z7m55mYKZ5f7MTbgX2WKcjTCO3wCRYuHQ060%2BhcU2uLJtfCdeMHKffPeIFN90cYX%2BRq%2FhBH1A7NiGfPv7tx%2FgLqDkhgZquWPvgPh9h03VlZMz2PY1c8BWp1QOhqGTsRfrLPrB5UVTQOky%2B0Uk65sSWLG5qLiW9mUW0eVufTwefdi3nCSXwk1RVJ3b2xa0vYUvFzxVafS6G7%2BhWV4TAq%2B%2F%2F%2Bq8oUyD41ZbV05JsqPGdjwQraKNLDW7T4K73eWhchgKbDCiTPWneJCfdshQoWBK6mWFUaKnhqcViQ1Q0OAR6ZA%2Fk1SdJi49NPHbKmP01ANA4EvzZPMLmps74GOqUBIOLC4vRYWC8Lte9DuNct4rbAAWGbO4TcqSoEJ1DIQP%2BTLwkKQ%2BLRV9HZKSYfk%2FyCmfbphZEtHSdCjmB1B594KGsvUhpRHaiOs1dA7O3lQ6XsZV1L7a%2BVO1sd4SbP%2BN%2BfEZzGQmIsuJSTN7uBxb9TZxSf%2FC%2BCpaLFtmeFuOGzFhrp%2FgnChjHPzTDqlpVU952lP70KGfaN11HWBjlSMIDv9B715V34&X-Amz-Signature=0f101186dcea99d4ccb352c93b09167c974fee6c29bfae77d046f95b5b5d8230&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EBUE25V%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCjWqUu7iF3QwhGPcI2rQVE40zCHP0c6gUkOSLIjzR%2BgAIgFsc1%2FGg18IDLkUX5Q%2F%2By0AdWqVyfm0lZlp2vwvp4dRAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDGDYIUq6jZ6Ukb46ayrcA3Ck08Hf%2BQBXkFkng%2B0LXz26U0SaTFy4XwSmMGCW%2FUx6zpP7iPLL38DRYKCjX7gjscY3LxkJd5MEVKcfQqnq4Ng%2BGyUoS%2FqojOgnZ12zhUm4C8vYJd9DIxUHPPGLcYM8XVYbu7Ljs970Huqg%2FBr%2FuyY8BKHf6F2UmOWWxErq%2F%2FCkJWoAbmkPkS9AzIGlxUZOwDaUotkvcvl1ZBpU0bqInpfXWKWD17sLwvqQegjFD5MImMZgH4azFSX%2B5TQj5YD%2BZ2n4nxF5ZcCIrBWfI7DBZfYaj%2BE8W%2FDe9xd5PRUfDwgYHg%2Brwe%2FBu7BLHcvyO9apiiqgo0QNZeQVfV5Slu0v9iXFQ4sU8FJHban6bU5r1j48mTFx7N1mm369AVn9lEUAJXu8pTC0Mvt1aFjO6daR%2B5uIIemDCdaX9ypp8UecwBG%2FNbVR6UK8WD03BeV7l9wcxE9u0KTECEdZxQ4xbHzm1olACmSvgJhyuifRrBkWNgF0xMrBCGQuzh2kI3ZPhbXrvuclnl%2Fjf0j9Y8A4HKiByQ7baBikuaOXLrPVEw4fcHHmdG8oUw%2FJ2YkE5r0qDNRVYj7z73Cne9vXXEG96RBqCakJIkJR%2BZ5z7s0Lx33V8yZ0n8Mx9JEhnlzImeF8MPips74GOqUBOdXdnlEFSdPqj6DR5sEdvIzE3%2Bw4u9zbRDpemJ7V%2BACLph7IFlm6em0xuGp8cAglmrxlvTVMPQRXBPJ43g%2BMWKRjkfzYGjOuy%2BJ%2F8pTFt9vJvevzsVIlquZKPgQX7LCR2VQ4mAfi1a%2Bkr7jfMODi0IBXv7Jgm6KuT5%2BoR7KD5SnC3gKlKJHf9g9sN8bZC0y%2FIm9d8sMfRBwoQtkMoHRgIj9ccO0f&X-Amz-Signature=c0760bd3dba60b2bcb286db8e89a3eab187b663df3bc07a7421cde6e24a49472&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3XW7BTQ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHt6n8bd7DhrPdD14YdwzD9XUmpVaFGUq1Rs%2BX39O9qfAiEAkTcZXjucebu6JFjazWjXWkpiWHPUmYAfbEd0ZmZs%2B9wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLphmggBZaGISZI70yrcA%2BRxSIhvyPhza19%2FhQlH2Tlu4M6w3YySc46%2Bg0CQ3uJ0xxYKlCaDUYsdhCH%2BwjRJYKu29u12h2NGl4l5OZLXdx2%2FizXjxw6Q7btDRUnxaq6smbN6bnNIulYo%2FaKMyJwIIh30zdlJHojdDbfjEs7CL5qVQiUEfllZ2DU6dFmD4igcrzd0eWxJdafF2OzjgAf%2FbjoAkqbdM85IGac3mlloUV%2FOyywdqTVspJlscEvEBDhSgPUhu6nRoF%2FqfhoQ2DYOYB%2BoopvcIlWzx%2B2I7PsLSdxo%2Bn4noxd52VIw%2BIAN3kVW8dZA6CcN83iHcUiAgWkuLbetWBZp9HxcaIcEi1JcQVhcwzQCXMdV%2FlmGFtgbuJEfsVfa2WDl3XPUQTF5jSCEMqDiwse%2BMLA9MVonw4HortDG7x5DCrWv9B5aN2RBOtfJTKlcuaXJrpXCFcgKhOauS9XMcZL7G6pkYb9V5bQBzoWL6lyRlJr%2B%2BjUhDiSsb1FkykYgQsavAkgCHJ6rYaWn9G13fhaQGO9%2FmIWG0rgy8vTC21iC6o2r6oOcqJBT7mTYi6CrO82ez2obXByXE%2B2RZovW35HOP7f%2BytjlP61YEo8I1sbIfwlw3bTl0CJfSRnaIPqZxW1fiZVeHOEkMNaps74GOqUBHtKRtzWGvwpa%2BFaw1XKKxtbELmqwfnMVwDmi2JEgBeP73knK8p2qgRW29AwG2Cltx%2FiAhz%2Bu2tcWvU1DPi34kViNkv68IKQbIVl04KOhUbP2oNP3apj%2FNO5JqvSBJNtJ4%2BLaY9Pc9spFkxUSo3bkdrbIWmfFoziO0uMbqNGwj6%2FKMEQYl68xUC9COWlVgjKV5mftT9kWGeGlMB0xPFFTOs3Mlinr&X-Amz-Signature=91693367037b9c03c9d8fba42ade4421a924fcecd6e9dc11ac81cd140ae0ee15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBOGSJPV%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD12ijO9dd4wA9%2BlpXVy%2BLL793mhrw2UwHV3qMfUu%2FLywIgDgMrc8fh%2FJ%2FfrILaSN1uwBRRtfotytxcKV3WjdCwNxQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLt1Zwo4%2B5xHr2omWyrcA3JYyp6ZNMozz5fhWy%2BwIyE94nhwroUzpvob2kcZEiOShjeprwTWbe2j7hy%2F%2BjpyFX5ruqPRvPj3YEzrs%2FUVPqPpDmwr6TIf7HY9mllx6J4ON%2F9kG9cZKRwhir9%2FeITKu46CJT88QmfH9%2FMn8j8JHh4lnWedamu1HWRZmdL0c%2FGEhYHPzBzS7t4XmiqBDw77NYy9u%2BxOHUuD5vjz3olartzROWRY1eUWp5JdN7pxEFwbve6XWPHAl1mNlDl0D24pG2pmCrwP7IahHQL7G9XciiPoyN4EUHHKE%2FzUw0%2BBm7JMt6%2B%2F4uVBrBhhwU813PbzfEBM1nzXb47aRQcd7tsxmvVbb2fGOWjjmU1g6accFJPrnhqfPJCr6aKQYB8JbnRXuQIVuE9Kr%2B2ZNHx07TTPkXp0GjKPJ96te8kMYP0AUYlKhxM9LLs8wDCbN%2BNcjxkMbnZ2j%2BTjAh7aOgvJIvnleT2fpS1CGClYed%2Fx7R3mbfOa422Tw0gNZHAHcJLAK1a%2Fi0o4ET3RVdPafciyU0GzZkEMfB2OQIkwdL86JBVxZP857f9NJb%2BB011QpL7xe0OAXsv%2BVvorBmzo%2F80TVgkRlBZtNFakm04Fx5M%2FMJ8Q8KZc%2FP5xZN4VbpFqhj2xMMaps74GOqUB%2FAKTSE5ddthk29x6alPz0%2FoMUD%2FEWAk%2BLBmoYDepfhJ9cDOjr9tnHZnAOD5NHK7bCEXEUq3IPqbBIkLJrEmNz%2F6mtYD89Ml8%2FQ29C%2FM6gW2UBg%2FfVfPmqY5NJh4rnyCV%2BEI%2F%2Bc%2BsRmsvAp5lSADA%2ByXYmeG6k0aeuzqJWHHjjlKojiH7SpviR26CG1r8Abz8dNFPnq2RhSYyXf3mFwncaU23Ou2Q&X-Amz-Signature=1933154a4d8ee4edc6bb0fd91f95a509b8d844e9b82452929e12ea7328e0c476&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBOGSJPV%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD12ijO9dd4wA9%2BlpXVy%2BLL793mhrw2UwHV3qMfUu%2FLywIgDgMrc8fh%2FJ%2FfrILaSN1uwBRRtfotytxcKV3WjdCwNxQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLt1Zwo4%2B5xHr2omWyrcA3JYyp6ZNMozz5fhWy%2BwIyE94nhwroUzpvob2kcZEiOShjeprwTWbe2j7hy%2F%2BjpyFX5ruqPRvPj3YEzrs%2FUVPqPpDmwr6TIf7HY9mllx6J4ON%2F9kG9cZKRwhir9%2FeITKu46CJT88QmfH9%2FMn8j8JHh4lnWedamu1HWRZmdL0c%2FGEhYHPzBzS7t4XmiqBDw77NYy9u%2BxOHUuD5vjz3olartzROWRY1eUWp5JdN7pxEFwbve6XWPHAl1mNlDl0D24pG2pmCrwP7IahHQL7G9XciiPoyN4EUHHKE%2FzUw0%2BBm7JMt6%2B%2F4uVBrBhhwU813PbzfEBM1nzXb47aRQcd7tsxmvVbb2fGOWjjmU1g6accFJPrnhqfPJCr6aKQYB8JbnRXuQIVuE9Kr%2B2ZNHx07TTPkXp0GjKPJ96te8kMYP0AUYlKhxM9LLs8wDCbN%2BNcjxkMbnZ2j%2BTjAh7aOgvJIvnleT2fpS1CGClYed%2Fx7R3mbfOa422Tw0gNZHAHcJLAK1a%2Fi0o4ET3RVdPafciyU0GzZkEMfB2OQIkwdL86JBVxZP857f9NJb%2BB011QpL7xe0OAXsv%2BVvorBmzo%2F80TVgkRlBZtNFakm04Fx5M%2FMJ8Q8KZc%2FP5xZN4VbpFqhj2xMMaps74GOqUB%2FAKTSE5ddthk29x6alPz0%2FoMUD%2FEWAk%2BLBmoYDepfhJ9cDOjr9tnHZnAOD5NHK7bCEXEUq3IPqbBIkLJrEmNz%2F6mtYD89Ml8%2FQ29C%2FM6gW2UBg%2FfVfPmqY5NJh4rnyCV%2BEI%2F%2Bc%2BsRmsvAp5lSADA%2ByXYmeG6k0aeuzqJWHHjjlKojiH7SpviR26CG1r8Abz8dNFPnq2RhSYyXf3mFwncaU23Ou2Q&X-Amz-Signature=6153a708f67e02dcd61b1a8aa58cadd858068e4ed92469534b946fb4c6ac85e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
