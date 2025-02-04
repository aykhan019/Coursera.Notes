

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=91cc67010b333de0075f61dea916eb9e22fbd1a602d2b3427012c1b6c863292d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=b3b48033516e1173c0fa2ade736edcf399c1760ce8b8b03769528bcf8747e3d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=3b7763321a9370eaebc8a02db9dfb9877ad5082b32e5feeb54d77820d9c75643&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=02901ed62fa17a16ee173d3072d4a32b4c4e57df6af83a6b645eac4452d0284d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=ae1e077be697d77f7cb9132633caa9f3e0540dc72158aa58a39d444f1a5b437c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=19656c8a34c11d057bcc3bd9f817beb079725a78d0c9d5358ed0c2b4a31bde5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=9f1627b573605aa1c6da0742d1813b45c3f75879d6b49456fd84280a8b41b4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNMTKETU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIA1FRXaj5I08v5eL0lUEzn7jU9HWpT5Q3%2FoFkclFiCZsAiA%2F%2Bhj94mHxzc%2B1417HYkViuSpKzQqITdQ7iThUYZjSWCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMlXbubZ2oBfF1ucLTKtwDElH8tL%2FYkNx5fM0oBVEsWbeO%2FR0l642USgAafQwUjmA%2B3ZKv4UVEmSE9N2ZAt513bCmB5%2FAhKStnYSwVcy%2Fny4SUaJkV4qfJx8xS57IV75%2FBgWNumWuS2rd26cJPu4Rvg%2FT8dHwhoNIkVtUexZURzjak5fWy6Lhp1qy7nB3UC1k5o4soaKUr91cIbUzqr8nBpFfG6s84A81Ds00pypTiI7u1cGFgziwhyF7BMJQDKiYWcmETLAHf1h1tsXm7dXpgMoI2BhGZBSNC6Je530HhzaeurfNj0FJ%2BQgcuG9cPe0hFlM84jE%2FhmnhDpi1UN%2BxKHPk3XUMWjSYmEpcpDwTCBV8watrX3Ewr6bylGM5cCD2ZMtsTrkVhEtaUqsshFWizD3nz7V5DvkHE8hOy2MhkXLhhG7M8OqMTOabRHqvBL5tQooZ94456Ar3LhcnMcO0kM5GWTgCl5Vic8X%2FyVBmPtNIwkmnrnrFJKoyOCdrqZ6UBM3bDiGn8ZXXBB9Mxc6x8b9LHtNY55qFtGkku02f3JePr0O3X4dyUDmtbApnnHIW4DPU9zY4mmRpygyZ8AMnvmLEDsLuXLE552wJbpdYYgJ4M5NbNaTZaWe0dphAJmxoZa8rPABeP5QQ2dc0wsJ6IvQY6pgGXs6ggMTXSoOEqkDs0SQfGwsT0YfCvoD6Mt9UZYfIn%2FOfkcL%2Ff45DXuAIbllWZ0d6W21gS3ijzuSSiIneGwgiVcnLValmt7KtQ2BEi3uZkzhzEfgLJnFm8ZJOUfbUZUis9v4IGuDUH5262e8wOy3zAhGXrKth1b9zfd5AwtL%2BYIMbS1Ed3%2B53TxfZtgMx334S7syaX%2BEByIEljyDvpEc56N5ChtxeR&X-Amz-Signature=27a3895304509937a7a03f63bfdf20f1e5be8f74b78625ca3ae9ea48f84b28c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IBVI4PL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIDvWmF4kf7wZdU%2FYVmHlX10z81AnqkHcHPgikxTv3aGCAiA9ihez9R4rAfaYULX706xsg3wQPB7KyeFYBeVKjQtXoir%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMH1mSSU5BWITHXTIJKtwDxEr1EgjA5uo6CtCbikMqZXxK%2FYu6oo6dV%2BdTCIvMvBbMewmqqrcDWV0T089b6%2B5qSCcD8LA1TfDmp5oomOEtWSGmXy%2FqDDGB9LkEJkGouBHWXqol4%2FwKR2aBgLL66ypFxfgaIWFwqSZjs1R022txyOyIaollpZHQK9H024XStxtXOWV64LAuns8BdwhEGclFaDV%2BbXeQsYC1ms1ro30lCtyMwVlWVkEG%2B7vftVizPOsoj5BGdNTiV93NFRP7kqAqSQq8u%2Bfj4vq3J9yeTwcPTDTd39YYTyZ8%2BkVpVN7HWxQAkhKW473hxlbomnsvWH7rFXVqKNpXl1NMj7W9IK6f1LnizRpzbzDh1%2BuFeLXJLjlxyub%2BOq%2BMGFwqhHRbKwlVeUW3A3j0ci%2FZSEkC3AkksqdWuP1melzZDCVY3DBJhylVE8S9OPQWQF1iEjQM1O2CZkcSfo1CFNFUiigrEcrcjj4IOSk5o%2F2w2GeZVu0oYdqRA%2FOm0%2BhVigoy3OELSenjMaOrQOB0dvZHlKQYV58Mg0T7wtYtciZwx%2FS1k7qik2l1Ddb4cJkhwh4FDDmkupInuG2sHhFXlH6%2BBTZTOj3%2B%2FKRYc5EujaW1Jk0yPocx%2B%2Fd%2FmIRlpQfe0mFzaeEw752IvQY6pgEpCFJtwHXF0%2BXpiP6oxZ5MyqqKdHey%2FUBwuwOmvfjdhW3dw8rH2Q66HqoYzmndy4MRszAA4zctLvqmHPytGcAiUfdFxYpTWDJH8ZPzqu4qN5pg%2Fti%2Fu%2BAap8NB75ln42UZ7SpMW9N25OFZzp%2FFE8T%2FAfHQuRO1x8pJ5c6CCnCLNtH3g6zA1rEsfsPG60JlVyJ2KAaxBQy4NOSpwWo%2FoivUZI%2FHp518&X-Amz-Signature=c63d128920053d71e660b952cca2fff283c67ce043c277f307068aea69a9534f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBMKBSB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIELmk7IQIY7BuEHwdwk1b3RcOqN5gxlSPBBisDEcTPJ2AiEAmI0KTLXr%2B6iQnt474EYDwfXnWgb4foHkpMOWc%2F%2BJLj8q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNOB4mOkmBxtt%2BQulCrcA8X0xaXHpy6vUxKQTGq%2FWHl7mhgF2p%2FYy9tiKuYtG6VZitBJ%2FBMpPZuufMGwL7oC0StAAZSBJI9QCKC7Nr7GrZZ%2FU%2Fm%2B5lsnb%2BtAxFnK0RxyIdCfinVQeGz4JWYoCkmVdehuitphoASsMvkkRx0rYbiTjbfhxTEUmhWbP6tWOT8UeI8cm1m6PAktqBfUVxXSGiBcbCtfHjVvwPKVyp%2BzrVLkEb4JHEqalKOsss3QZH%2BeVRglu3gNiSg0y47V2buTAFuZuSu2hpfw4H3A5QbwowspsTbzRdrdcLMSDzo977wxmzrgZc8JPHiDnPza4sc%2BDFeOKmFd1lhrh1fwVGvuwMYAStAmISRPATmsLXel206wR3HiD5m3QSfBYQgocr4%2B34RZvOxyzeDczjxijOreS%2FfEor7DySLcpljRH9zqNQu2DVcj5X1kxI1%2BL2CMwSiChXFtGsuyZIVeOckhpVTLkV2N8XUcOkZOnNiF%2FhAWkNANx2%2FtakD2jkLU%2BGsMe%2Bb%2FA9Dfmboog22H3pYFOZnLoGu%2FMIwU0ne10Gq8vyQCxgKJ9Sxg%2FATvy533Tocm5zsRJfDci6%2FNfXZSxJggLkIaNDnN0QgDgqBlOlKRRGKYFp%2BdFB8cBf6NL2T4Gs4GMIueiL0GOqUB%2F5IdTwn6r%2FNXvOfYfFfP7RIckSxJwZD5F12w%2Fvp7tFSs4u8La4%2FGubj6LlH%2FCrz7bQvAkv4Y4fwdYrOqx6rSdzV1rZObDtwG0Dxqf76od5JOS816%2FYgPP5FtyoYD%2FVgvxunM8gPwknmAXwojq%2Br5QWnaXuJHKLanu2nZ6Nd9D3ly6FmsuhAPBCB7TsR2s47BqeEIoINc6HS6qxvkhaS4LhP39jBw&X-Amz-Signature=985b18341c5c1b2d159e7820ec1c23f7582e49f87a1f824a267eeee7f36403e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BF7BOBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIC6uZ%2Bg4RNUTbrpcGV0GFb6kiBZRSI6Xa3xk9KU%2FgMegAiEA1lOzgfJJvM6m8bceSu1jci1E1bkYmUvoNe4MeI%2Fv5zQq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDKHk%2B3NYAK7fi3isWCrcAyar6rx5KzoLZoImbzAzVHdsAFZ3P8RBRM2ODTp%2BXc1JPKpUVsuZEpBDvdER2XIMy6URkBWmB2%2FHc3SOpY7czoB4fkvpWqZUj1ZRwV8RxPeJ2paXjNhxSGpHIYjpa8JM7QADuxS%2BE2meTrTdgEeN2Y25y5g81t2KWP2hihYnC3j%2BxxUTQ2bjRFnyQpt%2FJroKlfb0FGVbjNZGNndBpXFiZ1ZEHxCwcEZTPvx6Dp9MB9vUZBubJ6TNP9jzR76VScQShoyrbNL2hqzj4BiEBa2nCvUssTG1sYYc6szrtZhW3ye7qaECq0v2bJbf8cBgQ%2BqntEdt7EH46xDhKi%2FtiE4T8CvypEl7W6Vjcdrfd2U1dBJ47uzx%2Ba16F72rWh2VkD3776qk2DFhvbSB1hd2RtB%2F%2FiXUX3iJ5OcdmOmf0i2mxExQC06LYWCStqGowPwu%2F66zDlq3dJnTBqfylpQgSAx333Ebd%2Ft5r4CP698Mx9BXGvUGY2WqxlK6oAzzFGVxQhbogpTJrQIH62WnTYkqPO5Q%2B948t7UkeSnfeCVzuZZiTLQcERq4jHb6KTITwwo6rQkW8HnaO%2B9axxD1a8Mabga19J7NtgFxLk73oeWfmGxYZcBWlhgSG41%2F2gfC9b7NMJieiL0GOqUBvEOVkHJq%2Bz2Zf19LcfByDeeebnuwU2d1Td7dIC%2BnfTpFdy9zY3oPPw0Iyem4MMlAIsgExLnrwkWfj91pm%2FQqcv3oBaod4BUCCyWgzHBwhYL%2FMibj9HthRnXSL87HUzGT5L%2BDGh%2B0LfKy4rgRlFnCg9guqXeqm0BLAC6Jc2bmRp7hwifQ5nNJmSLNg9vM3gt6sptT571aZ%2BU%2BNplX97Eq7csVP81f&X-Amz-Signature=bbfc922df26729aa1189f48cfcaa0a7d481b394d1867a1581e092a3eeb5a9993&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BF7BOBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIC6uZ%2Bg4RNUTbrpcGV0GFb6kiBZRSI6Xa3xk9KU%2FgMegAiEA1lOzgfJJvM6m8bceSu1jci1E1bkYmUvoNe4MeI%2Fv5zQq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDKHk%2B3NYAK7fi3isWCrcAyar6rx5KzoLZoImbzAzVHdsAFZ3P8RBRM2ODTp%2BXc1JPKpUVsuZEpBDvdER2XIMy6URkBWmB2%2FHc3SOpY7czoB4fkvpWqZUj1ZRwV8RxPeJ2paXjNhxSGpHIYjpa8JM7QADuxS%2BE2meTrTdgEeN2Y25y5g81t2KWP2hihYnC3j%2BxxUTQ2bjRFnyQpt%2FJroKlfb0FGVbjNZGNndBpXFiZ1ZEHxCwcEZTPvx6Dp9MB9vUZBubJ6TNP9jzR76VScQShoyrbNL2hqzj4BiEBa2nCvUssTG1sYYc6szrtZhW3ye7qaECq0v2bJbf8cBgQ%2BqntEdt7EH46xDhKi%2FtiE4T8CvypEl7W6Vjcdrfd2U1dBJ47uzx%2Ba16F72rWh2VkD3776qk2DFhvbSB1hd2RtB%2F%2FiXUX3iJ5OcdmOmf0i2mxExQC06LYWCStqGowPwu%2F66zDlq3dJnTBqfylpQgSAx333Ebd%2Ft5r4CP698Mx9BXGvUGY2WqxlK6oAzzFGVxQhbogpTJrQIH62WnTYkqPO5Q%2B948t7UkeSnfeCVzuZZiTLQcERq4jHb6KTITwwo6rQkW8HnaO%2B9axxD1a8Mabga19J7NtgFxLk73oeWfmGxYZcBWlhgSG41%2F2gfC9b7NMJieiL0GOqUBvEOVkHJq%2Bz2Zf19LcfByDeeebnuwU2d1Td7dIC%2BnfTpFdy9zY3oPPw0Iyem4MMlAIsgExLnrwkWfj91pm%2FQqcv3oBaod4BUCCyWgzHBwhYL%2FMibj9HthRnXSL87HUzGT5L%2BDGh%2B0LfKy4rgRlFnCg9guqXeqm0BLAC6Jc2bmRp7hwifQ5nNJmSLNg9vM3gt6sptT571aZ%2BU%2BNplX97Eq7csVP81f&X-Amz-Signature=2141940d712e786ad161bdc2c30c9c84f6278b883b777faed3bef30922199b21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
