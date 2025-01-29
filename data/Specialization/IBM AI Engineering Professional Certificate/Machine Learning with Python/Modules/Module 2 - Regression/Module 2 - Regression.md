

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=e90a29b47ffd4f14ec45b285b4287b1611b90cfbc79430f451dc27ac99ff09b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=1160a06fdc4a45124322096c91556568fdd20e225591c8bd837c3802cabcac08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=71b1506d4e1a8d6a002c2a67063f43926139d78645bd0f146105d57d36a7ca79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=89a96eed6f486d3fb3f1e50c8241798ac169b704a327fa3bd5367037f1f57d76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=858f0b0a1c3da60dd28a51cf39f38ee3cb410979dd97fadcfb892be163dae84b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=8d52146b3160ea2a8b6533869205753171fd63656b7cda407522c166bbc669e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=cde731ce6d8fb0ab9ee8d137b977cbbbb302d3bc5d26aeecc8199a749f21e8da&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TANGG3MM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDi5MlOl6%2FEHSIBr3gDfAlNpdtAVbNoHtoPD1ij%2BF5w4QIgEird27eBJmq2u3L3FvLaQ0k4oY3W49U9T8oNCdtUL8IqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt5%2Bl4h67QaZUowRyrcAzwrEbkleAmGa7Ji3xpoqIb9RP1eHR1nL1z6kaRcrfsNpA4ZIQwB6FKzki%2B1bEPrJuoliGScVb69EmOpeuwvS8S4cqnXk3J7MbZXR6hAqLo9HOpL6%2FOUo3IbpojFIDlpvtA7h%2BICIC7lz%2Bx%2FH2k5PfcHgts2PZA4tkId7DGMLwnI0NFntP1XnWlPWsACW4HW96t%2B2cNmCYr%2FO3RQOFdpoPjEBQV7oyCf3h20pRaq%2F2wHWMKeIWkJQ4ozs3DLXR0jaOqQJ8Pbz5fdh0aN9sOItNYMk8BOM%2BYJ%2Bl2bzxsEV6xCZgo7Zv%2BeaEgZ5ayRpyjVK839%2FFpHyy5QRHVEmPSiDCqo2yw7EgQWLLLdyX5Dw2iTkwCGFNYR6lWRmIIdO8%2FHj2cOIPDC%2BJeHv1j9zQy656jd8zsA0BC17cxVzf1SphTueRkJO9A%2BEicEtxMKKfLibpjOvsMjKrR2lbomaL%2B1dXqcte5y03xTtzsZMAR%2ByO6zoKsdpqZaKUW5CSLwfHbs32k%2BRuD%2Fz2G1FjterFnrNvgyMy0nXbIngyK0P7SlLL%2B7VXX2dHHzGJPyGRMwwvSNJ95xq%2FzWWa0hIEaf1pg0DDc7yzKbPULL2vEB0ry%2FNqcBZgrjorLLoeAZtoCMMJG75rwGOqUBoic7HoXo02MjKCcpmLzTxx3j%2F6Q4BJGK7Iz%2BvJ3P7zISKcER58PvFDj2qDcXsABB5KybnlHwj4WJb%2Bs%2F5vqe2XH1ueFsZWcgKaLI9dkxXw6%2FpGXLKJzX7BsD350y10Q6QqfsVn1gCO3awQSY6iQ7HM78lhHoQLR1A%2BzSUvNeQNqbc1zFYTvzN%2FUW49DdTJ%2FOHcnCr8lwBmucqvAoIQSXWTUqEsGB&X-Amz-Signature=7aad9d38a47048e7545e52c1ca8a5b6311180ca97d9cdcb6c568c595a6d24e4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K3KVUMZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAF7uUv5f%2BtbNqHEaYDDar2jS4gU7o6GUQjn6MHcdvwIAiA94X9mtKvxcMNR35%2BYBkRxmpywcVWoghgOF9hlAAxgSCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRI8JHV17%2FH7Cp0I8KtwDxhjgNbaH0fm%2FTd9GquXmIguxl2tcCCVvXKbBdUJIxSLOCCZjEZq2NIdC0LY623SlDGSN0yklhWLoo8pW8n65cuI8otAY2XVKcmuWZDpuN4uCG7RimDZ0x6glpA3IIWW8la02OgBJcKfxUwCL6z46ojnEA5hL0ywFJhI%2BmmE%2FTM93zx%2FQXVA8xBBMdbMN5Pz794F%2BW8xIWGwycJhUfAf77Au1E5zlLUqPFxVvEsYe%2FYhipE4hVDgA3HIqEJMRbC9245cVjU9WFZq9Am5HIQWvKAdMoJOMFkl3aSQIla4pKkigiKzaRhKNX7Tq3pgk461kcJ4VOoMvyCzHKIvgghQoPfTwfX5R2E%2FRTBXst7iUHKH9gciekJoabNuPjtU2WTkGUGbO3WAsqgtDA22c5rgfgz5aCcXn8rZNXTrj8%2BZoBP0YtI9pNzkeQGujryKAUu7glhC6aD1zzs7U2ABUU%2BVzxgV2LsJ%2Bc6l4%2BPUoEnWpv6OV6xgAJMRVtkOSkGF0Pr53ywrK%2BW8jLgsiuI5Myw1gcYPrVysrh0SfSbAHJbJ2yQu5dhNkVRNiK2%2B9iowSmgjpUGxNRta4D%2F%2FCHaCIUNn3j7%2FJiUV%2BewMF%2FQyvdJK0ifBMUNdJkeflxbKaasUw%2FLrmvAY6pgGaG04L1y4iNdvUMn2Io3ioCWU4wGsXU2Dm6ou0qm709KXBV8roIGZg847My03taf9KuaCEcusA2hUh%2BfjFu91mW67QG4JtCsMpOuDRablh9Ze%2F%2B0Fg62wbHqoXTmHx9Op7T%2FYiqOLuEsYOJ8TS96pnyqGgn9HZrKzBZfHPkTv6l%2BS%2FkcAMIqxQCWwz56OvX8ZqQSfnQwZgNqbvF%2BbaoyXM6KSM5QiJ&X-Amz-Signature=b80ca3635635f3bf1ffac5151bf9403115df4a2ef21563807766e6d92f30ce96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S527I37E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD7oT4ij2GDVjq8tDrFJbj6dQ4OxGTXeVqYcbwJiAlthQIhALH7Y5qwzCXtgPtsVzJVrMUWLCnaWQQFV5J0v8Hpg2R5KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BPD8lQu0lxUUN6zcq3AON68Dc6pSjAqTya%2B6cKIn%2BTeMW%2B99iXHUxYPp5Ui2nlSLSIU2ugDjdy6Vmdmz2hSx9upOUBBuBvw77%2BYbti%2FlTpTQTCTEFYSRmgRu%2FC6dm65Qvstuiz2hBW6PdA00bLhYygAvOS%2FOVxnV8cKgLs72OEySSI5iT68I24We6lILPDWUag9o6vnkQoSihYSWzE7g9ULH2lpAqnA9zrmlt5e7zoqPDClgB4AY8i%2FPbWMh3uev%2F%2BCoBfAky1IL07eZwcrFfqAXWXofctm02cjmR2CnWdjxXG2GOMG1vdyM4QI7ulBBAJXBAkyrMC%2FCLvkWCC8pK1nG%2B0VBlSX2wcgIsmIzz2awvLmL1CtL76sd%2BhGyezpLKApRVIJu6LrD%2BY8NgND7LZNCBnpnqYfWdGqaKvJtYyRajPsAQqypAQpREXvHVYFRKW%2FBgtuCQ%2F2emBWfVM6W5cokj96yQ88202d5%2FqQwUNtVGO0pDgfrAnqK99beqXKjghM7xvebO5euJSP1Bm6aHNaLSggjbYFiGDAsuUbvGfhLDcIJ1vThdL%2FTkkWHX%2BZ%2BBhS%2BOa1cKUEyMuNek2LIdQBMj8%2BKVn%2Ft06rDQV1IQWDngmQpQn4yynLEAtsma%2BWwZQLp1qD%2BI64TNZzCou%2Ba8BjqkASKXJ5UV4dCfNzre3KVvxcxJl1YzV2UA40oHvrFrKgb63DgXN3aIbTvHH6HpcrtEUCtpaKXYQP0Tt8n8d6JetGV%2BfR0oSrcbgYzlPu8IkR0Tm3PvOncbGy7qBFRoMNgGSdF80LOa4OsmYPpt0xybvFQFkzOrbU3K7eWxITB%2F9tjY%2FDveqYDHDEDorrYWOTQbuxZjbh0DgUNreeBOrH3jJRo4ZDbP&X-Amz-Signature=27626332bf192204873ad8a714d5d51fbdd16f0213b992ab3dc52782f14e8dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XEXG4VT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQC6YtqYKJAr4uCdZ9t1t%2BUrMU%2FaJIrOtzeLmI1yOMFlwQIhAMt43y4h9OcZn3sWCnLpHzk69jURDUhJCBr9j0OQTa1QKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwiStBMpNd4sXYUDEQq3AP%2FM962HeUs8KAg7M%2Bn7ShA8DKwBkBLoJS0pQAfhjZ2DkmK%2BvseFSOMRepBMGVhdSGvBUUFD7k4yPmOyaR6aQHY%2FBrWlkgfaNZr7IiCf2QLdUDtO2j2eMzW5TI%2Fuvks%2BdYLz%2FhW2yyk569fOG9bM5mrgtn%2FDjSEZX68lf4dq4o8%2B22ZQ8Oam7Uo3%2FMmlLTZZK3mycwmpyAUY40skE4uI2BLw7aB5jdbwYsriZ0CNud7qfJvcRrq8qqyjXRSPGBE5pUW0nOMXvCptVcg4891h0TNhjAQscHld7A4d4OGejStr2EIsJDByCF%2BYKZZlvjxpLXWRyoMH5%2BLn3eUgtMByU27RCGZH1nqkJPAet9r4M3GruyDCx7Z9VOlU%2F792beLSK2sIb%2FpgLXG2N%2FyHlIpCjUGC3oUGexTN%2BqZCaipaNJRNxpSTH92RuIgaTNoYhQvF3eALNU8fgKa3MfsYFL%2BxooEyZDDOqGu%2BjOlL3lNjLqipRb0puziwDhp0N7cn%2BQmMvp%2BLD6mpmU2ErdwFm7lZijAW4a4g6tLGFuzwc4f0yScP0r5yMWJ49W72F9%2FY9%2FxX23h7YXiZsKil4TIncieQ1zFc%2FycQl%2FK9d22CS370Ov0GHr3V6o533Vg4S2BgzCEu%2Ba8BjqkAR2n9IewHaF%2B6%2FFuy0jSyfoXZ5ok0u7FmOnH0qum4MVWlrQB1h70p0q%2BW8r1rd5i3Bb8SrghB8RH8uVF17kJOOk6AvI9AJ72OFoRBwyQxGsx5BG7xFAot9LDZJp6cPqbFQ1yHM6KYKx1ppp3ROuKf9YPfSM%2Fu%2BcogpUQuoqZfVVTjWbJGiy0uNODOe5hJb2KbHsTwrwZe5iHLMbqibEBG%2BRW2czc&X-Amz-Signature=c232577da616a7f3875a4b4fd1d7b1afbc920fd85b6dfcf74c21e78ccc67d8d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XEXG4VT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQC6YtqYKJAr4uCdZ9t1t%2BUrMU%2FaJIrOtzeLmI1yOMFlwQIhAMt43y4h9OcZn3sWCnLpHzk69jURDUhJCBr9j0OQTa1QKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwiStBMpNd4sXYUDEQq3AP%2FM962HeUs8KAg7M%2Bn7ShA8DKwBkBLoJS0pQAfhjZ2DkmK%2BvseFSOMRepBMGVhdSGvBUUFD7k4yPmOyaR6aQHY%2FBrWlkgfaNZr7IiCf2QLdUDtO2j2eMzW5TI%2Fuvks%2BdYLz%2FhW2yyk569fOG9bM5mrgtn%2FDjSEZX68lf4dq4o8%2B22ZQ8Oam7Uo3%2FMmlLTZZK3mycwmpyAUY40skE4uI2BLw7aB5jdbwYsriZ0CNud7qfJvcRrq8qqyjXRSPGBE5pUW0nOMXvCptVcg4891h0TNhjAQscHld7A4d4OGejStr2EIsJDByCF%2BYKZZlvjxpLXWRyoMH5%2BLn3eUgtMByU27RCGZH1nqkJPAet9r4M3GruyDCx7Z9VOlU%2F792beLSK2sIb%2FpgLXG2N%2FyHlIpCjUGC3oUGexTN%2BqZCaipaNJRNxpSTH92RuIgaTNoYhQvF3eALNU8fgKa3MfsYFL%2BxooEyZDDOqGu%2BjOlL3lNjLqipRb0puziwDhp0N7cn%2BQmMvp%2BLD6mpmU2ErdwFm7lZijAW4a4g6tLGFuzwc4f0yScP0r5yMWJ49W72F9%2FY9%2FxX23h7YXiZsKil4TIncieQ1zFc%2FycQl%2FK9d22CS370Ov0GHr3V6o533Vg4S2BgzCEu%2Ba8BjqkAR2n9IewHaF%2B6%2FFuy0jSyfoXZ5ok0u7FmOnH0qum4MVWlrQB1h70p0q%2BW8r1rd5i3Bb8SrghB8RH8uVF17kJOOk6AvI9AJ72OFoRBwyQxGsx5BG7xFAot9LDZJp6cPqbFQ1yHM6KYKx1ppp3ROuKf9YPfSM%2Fu%2BcogpUQuoqZfVVTjWbJGiy0uNODOe5hJb2KbHsTwrwZe5iHLMbqibEBG%2BRW2czc&X-Amz-Signature=1bf2cad8e421d9b1ed5aaac7477d42ee2ddac463b842026b1f62d037c529f321&X-Amz-SignedHeaders=host&x-id=GetObject)
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
