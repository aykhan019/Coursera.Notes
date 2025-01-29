

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=29a0101ee93c727e57076257b6f622a21419c51f3f439791bb7ea23861dc3e3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=9089e615043d57f8efc9a171a10fb1dfb56278504f16def5fe06c80e4897a1a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=981ed3287b702938b3fc9dc0bd79ce34b460e945111572013a657a584b89a715&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=f29c51e350795eb2487bd0399a619b4793590f97fdd085b34862494a3d34d5c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=51b83cf35fae514c303c31a82a9012142876fd94efbf5005f7466555f05fca2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=a960060c83c16fbd67ceecea07acc645ab04b04de0df5d7c83e7c9375f1ef8c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=0c5bba82d27fec17a5500a75678fccc753b54e41b135c8875f7c8ef588fd03dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LNMLNRH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjUS1gtWkYlu7W%2B8yJluN5RgacDF%2BsuYQ38vb5IBkwbAiA1Qk3%2Fwj8m1BdfkxCfdc3J46BrpwJuvacX4l4QBf33biqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQjsGgNQ0Ivv%2BdnZKtwDRaS%2B5SqrzSqpIua1aqIT1bVXeo5gS2CDBd1AYVjgvPkciB3qw1m1ujLsYuRQ7a9cD6%2FE2jiLDOmnXWvYKcUkyyUwaHZsBdeDokJztErqLPsC%2BsDt%2B1ywkTwLRIRZiSTdCUj%2FFojZpLHLZvOJqwb0HXBWjLLaq7zIcF2EeIj497%2FOKqCnBdV%2BqGW6f8uW6Pv1VnYIVyhgrbtrv1s5rpe5WmjQFijvTnLhxsqNAhCvoqGMcL%2BCvuOCh5uDe2qit6C6X38eBdAy9Aq8T1ECUxED7yyU5DQgVXHLyPBjC5thny23ykkOy3c2F7MiUR4vIEOSYQ7%2Beh60hmNK5lUWmVYxk8mEDiKmlDAdwnDI%2FgUnlAvdEYZaLwtDHqplJQtPbeNBGdI72n8Y%2BWYXL5We9ILQoyiym1VFaHlFfKLk5hLzSYE73xz7q3S1KyiAuIIjrRY8GiS11Kc7jc4R0KBp1HxyuPcyCTCSY%2BxxUCVXHkLmooTL9pnDxs%2BBneqGXE1gOsU58Mt6TSFy2RQRCng3Q4MhkW9LjwSt7V%2Bl1LB1QRuQoPhTlj8lEfHGUJQQpQOMrz6mb0C7fMvts6foYdn3nE0OpvnFpJhlFn1xbRMGGdjVWNlaRnoZhxMrYDao%2B9swjOjovAY6pgGxLKOueSSnvTzdaySCz4Sgw2V9JV%2Fg8vINA9e25tRCH%2F4%2Bcl9ecrNC0u3vuiRY1pu6We%2F5p5BTIMpaa8ZtmtKd7tNRdFXG9fNNVVVBU7ooC0NtKIPY7MOgwjVT9T9mp0Np0AVdegoKHceIatOtjrbHN3poIH85hTh0DPT%2FV1yz%2Bsfpw9KWWSbe2rg6ODWPABNKr3mqHFFL6ajyxKGsLPsC%2FHvJIXBp&X-Amz-Signature=645613a0e88a87753bd6cdcd6c7d6e7f984cfae819bd8a42d6c6389aef09df35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWBAMTRU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqFR4vijLge08QHdxBT6XBhBoo%2FlAIz0EEa3kHeMeL7wIgYUyYD2uhwCeFT5RahJwY359%2B5wn4MHp1%2BRCBE8pSxHwqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOTi%2FhPnpPcRDGP0yrcAxE7zqdQY%2Fcy%2F%2FP7TU1ad2THU0yla7fZtgbiePbkAlPkFzrIRXtWIZVmnFWScXJv2BBwyhni2m9MNt%2B5%2BnocP%2FLSzfNZmiCdKM5olUYK%2BSzCuzeKe9q5WjUMtwEpE902GiFvU3LiNg9pByatcdSe9dbWmqey%2F44uw8UoHiMzUIYeeXziVx4aUrIPIkcGLMsA5FtcHbKR6l%2FnrGODUI0tM0N3UuKs%2BneeCtIXx3hoiIzHusfshSSBJ2tsUBpiWw65BHSSZ%2Fkp%2Bsmqh2ZnO6UT23Dmf8rCPDHrxwJco6EYXYiGHwi1dItwMWjcXFbas2RLRuyAkrxlChzVboMXE74cl9uU6SxhggnxmoY9gkm32EU7wOgLhImH1wDCx26SX5gEYmYXsFM%2FQzWt31qic%2BpNu090EH151i%2BQVoMrpcflLK8A6klfIfHTHA2TbGq3Og5LZ3UDQkA7c2TILAhkeLv586fpD8kt3WhIJ42AsXf%2FBTY9U0uTiwmAA73ijAiIAxImzkQDotZphq2aYWHKvEmT80bR5nkIvuhVvQLpDfwZWv2gl1ovZ8tPE8hBK%2FAlAhf4gH60vzp99j6JL2NSF%2BHTLe2wTuVB5rUyIrLmIbzlhNt%2F09XBvId72uejjUj2MKXn6LwGOqUBhueVTQ0lCSzVaq0rYyNLcMnWYAaNmq7GA9NPOVtqMAWClM7Z6%2F8vxG5VuldRgYiN5WqYbUP8u%2BDVIPzn72kgQFRfHxbEmiM9ffZ2fIntOgBH7Y5aFMBevubS61L9rXcD8KWHS%2Fjz0F4%2BLl8dgWy1oftgHb3zEMiTfTWYfJqPtSOGbQAIDpHGZ8NhwH4Yu1tylPuWHPlz%2Bu0p8ao6vB8x8o53%2BCAy&X-Amz-Signature=4a0acdc71fbe59aadb838a0f93d9466fcda81da1f914d267f10cb9617781bdfd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCDUP4XA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFpSJf00aKNYjiAoDfqYn9345xmIl2RCsLO5tS2yX5QAiEA%2F9cYY2VaNhasu8QIpqVVKZOCo6dN%2FZbzllgLqu0GQIgqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLgEKcOAFOTO70mppircA0PRI7czemAJMZIU%2B6XJXrLiBqnrggzFCTqwqiD0fIwUJHWSVY%2FpBqdcPQbK9gkzFxMJrE%2BqqeaR6OJ%2Bf2s93sBX%2FoNFXUijzZFqbZUdSrKnuYjF1jkEMP6gyEOlpAWeNL1p3FrS7KW7MagiXlhB7jy68LyXpoRz5DoskWfHap8tgAzT%2Bon%2FdlNrpN%2BqTbgkigXetj6TpsWIG297j5IT2weOWCzExudsOcTOoyfPHfX6wSeHBueJ3HJgC6pmDpYAS8WScXag%2Bs1YD1J9ESSRK2Zc9mUCOgYerCphitGhE10ziExDb72WWuCeL8niANjJ3DETCxcqPjnzMZXRbIVfOLHC78M6AipPqAnznz9ErDgBEuXyEqE5TRg2wV4Z2kUMvzConteiTMYeOensjtumx9%2Fz5EofUeLIpL32hL3MiKMzAlP7zfGjmdSjZ3WWGlSFGzyvuwpMzD0sqpLx08WqMuNgc%2BXQpHJfUPqq6sxbear3L9fKNfDKspxyLMidG%2B7k6akeC5FKbM9ocMB%2FzHvqShLiVVe7b978t0GjRpCs5h5KwoTuxDAkdg9krGjmCX%2BrVJljTbDDbeOFavELpuQ2VNPIU3rFEs3nwUEHFOfGxiyBOT2ZgDJ1B%2B29LoZ6MNLn6LwGOqUB1Uk0bhCtZYrS1Rw5gvKSXFQREVM4XlhR%2B0NmkBINAKhxk5O7e8FWOTA9BSBVX6LwZpM9x9QvlDeHNpwE1Dk8aB6UUb02f4rUPZlJ4brRDantye1aNvk8xTkcH4ryYIjlxsMW1LgbSkNjIux2rG2AEhHl2ubVebkQOZKH7FPsjQnrcn8aN%2BQ4hltF%2FxvpPO40jBN328QD2F4rs8vh4DZG7KG8nxVU&X-Amz-Signature=e8fd37e3c6b1490601dd7cdb3b903b32dccb6e0ca7d9bf513d714cf7f4ac1141&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYX65DTP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICdVAcI2Qs6K6T2VBdmRl9CF00DjSbgAWuJ7y9WruojTAiEAgr50QJoAI8wk1LZ8l9t7nnSZZw%2BzAtsEqCHK4ZgR%2FZwqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBnJuEcvlsn52%2BDTyrcA8Gcjvs%2BY8YfMyylY51zOmACBRi9WZl95AdSlVCHvHJukw4xIMZ9RWPJx4jgfXqNZfGbN1QR0ogOvEJPYx6B9ZVkkejN%2FhWcUZzCfWlFKB2W6MAB%2FDjqt4IIlcShGnRdCI3Lioxil4ogo2JbLiyDH88mXpaM9xrFFa1cAWthV3lQKMSZAZWXTR5PMqdw3bpC8b2ENk2McBEOyZ07CeL2luMX7%2FMZFp7yRvvlMw%2FsGG%2FbybfQKkzTvtKGxpPbSsK800XK50B1TAWd1OKMsuOgn0p%2BB8Ilx3ImtuGqqANmZGPQ%2BpmR4vB82HaaBsU0VSrM6kpjlpYA8ngroVnVKFvVDWuc8UWlS9CU4a6X%2BZLjal%2BkUGk3Y%2Bg0NhtIJQzfFgynmabMCIsxRdkx%2FlZxHXoYJ9P9fi8%2FO9wqJX4O1GvnFxMsXGPqDBnwPFcsnzBEDsOtYBNk7eJLglIEqwY7OH%2BzgJHNhKk5zPIMo%2BuDcYnpDR41PVUQtJSSney5zCs1aFTB%2FmB%2FYFCsCl0M6B%2FA2sFephLReWzlFneoQhQnS948vqYxJr%2Bx%2BZ3C9Emxa8feXDWr6DdupKf%2F7mhEF7Qle09HFqxEmIY%2BrVrMhFf%2FxFGP2gQOowhcf1GtpI5jHytFMI3n6LwGOqUBTyqWE5zyFz%2BhfDIVRvArZcm62mWcNEvY%2FQXh2wuMeRD4HsYI5IA5zwNaRyYJtNKZEY3rIWblwMac2TbkjEJOK4OrHJpXqiTfJLH4re%2BSPXUhF%2FeMaUUz79cLCt6xhv5SDlTKWa24V4RUQAWsoFawiANl%2BD392hgy0VHapH0ti7mqXDPHyQMoz9TkkQuiOF54T0w5%2Fhip7p9b%2FNWxZsBUmQzF6ZLe&X-Amz-Signature=ac65985501a2a945a53ca0b28a1450e946cc9c95550285d3799430c2168d791d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYX65DTP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICdVAcI2Qs6K6T2VBdmRl9CF00DjSbgAWuJ7y9WruojTAiEAgr50QJoAI8wk1LZ8l9t7nnSZZw%2BzAtsEqCHK4ZgR%2FZwqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBnJuEcvlsn52%2BDTyrcA8Gcjvs%2BY8YfMyylY51zOmACBRi9WZl95AdSlVCHvHJukw4xIMZ9RWPJx4jgfXqNZfGbN1QR0ogOvEJPYx6B9ZVkkejN%2FhWcUZzCfWlFKB2W6MAB%2FDjqt4IIlcShGnRdCI3Lioxil4ogo2JbLiyDH88mXpaM9xrFFa1cAWthV3lQKMSZAZWXTR5PMqdw3bpC8b2ENk2McBEOyZ07CeL2luMX7%2FMZFp7yRvvlMw%2FsGG%2FbybfQKkzTvtKGxpPbSsK800XK50B1TAWd1OKMsuOgn0p%2BB8Ilx3ImtuGqqANmZGPQ%2BpmR4vB82HaaBsU0VSrM6kpjlpYA8ngroVnVKFvVDWuc8UWlS9CU4a6X%2BZLjal%2BkUGk3Y%2Bg0NhtIJQzfFgynmabMCIsxRdkx%2FlZxHXoYJ9P9fi8%2FO9wqJX4O1GvnFxMsXGPqDBnwPFcsnzBEDsOtYBNk7eJLglIEqwY7OH%2BzgJHNhKk5zPIMo%2BuDcYnpDR41PVUQtJSSney5zCs1aFTB%2FmB%2FYFCsCl0M6B%2FA2sFephLReWzlFneoQhQnS948vqYxJr%2Bx%2BZ3C9Emxa8feXDWr6DdupKf%2F7mhEF7Qle09HFqxEmIY%2BrVrMhFf%2FxFGP2gQOowhcf1GtpI5jHytFMI3n6LwGOqUBTyqWE5zyFz%2BhfDIVRvArZcm62mWcNEvY%2FQXh2wuMeRD4HsYI5IA5zwNaRyYJtNKZEY3rIWblwMac2TbkjEJOK4OrHJpXqiTfJLH4re%2BSPXUhF%2FeMaUUz79cLCt6xhv5SDlTKWa24V4RUQAWsoFawiANl%2BD392hgy0VHapH0ti7mqXDPHyQMoz9TkkQuiOF54T0w5%2Fhip7p9b%2FNWxZsBUmQzF6ZLe&X-Amz-Signature=e213007e440758b4eb9ef30c9e1e0dfc5fb5763994bffba242f95295728c4232&X-Amz-SignedHeaders=host&x-id=GetObject)
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
