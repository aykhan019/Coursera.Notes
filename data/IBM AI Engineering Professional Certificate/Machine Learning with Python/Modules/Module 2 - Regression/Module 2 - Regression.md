

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=b20dbf7e3c8da7756e350640b33731e78585a393e7d233b6b07c5c17c65737a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=353f8243b2d966f3db49a6ff0cd7af19efad04aa36fe585f97ce67cc797f4f75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=1303a4d11157fe4ba4943f19f54c556fa0bd6a4625c0737530bbb19d5c5b42ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=6d6b144c07da3a0f825f14976be2e0dab31a04df3ba8733c5d3b0e51d77ec0da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=321967750d32057c563890ffd276dd2893f6273c2c232bf1966a92b63cb5038b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=a0a272b855284103eb0f4cd7fe055b73fbacbc83abe1a5f56132d8c0d0d9eb94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=99dd3193a08f90e1cfa904a081850ed4d6ac29dc8fe34b5fc8327d95ca1cb107&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=abd5a85019ef70558a540456bb37f024f05334de8ce82fe9e1d6e44ac7061b80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLP34ROU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCoqZ5oJSTJCvqFvc6BTrDpsz0zqgUmOvquFwxU9%2FieoAIhAIccn%2B2Wajr8MYWixSw8IjukKnHPNdgFILVRtQ2KRiCRKv8DCEoQABoMNjM3NDIzMTgzODA1Igy8Ybl6%2BOluKzbarREq3AOVYIQxHgPtJPPJbFhzdA6DYWWlRrkXzwMjL84%2B7%2BZKnmu8dF40c3YS8%2B1nWtfenmGJXf9stu1BbRciKvAnv9tRRabzWCufubZJikT%2BS7vwo1gyqElXLqZfuw7zVBglcuTgWqsVMlUqBEQAXP8DMp74%2FeD6g4FwJTbmZNV19mvyY3xYRJUM4Xrm%2FkR%2B5MTpcY6lA3rI4wq8FIbHFxC2IrDj57SGyoMybI6ZFishyx9nZVvqLLnYH%2FMAAcFG7aFqlQr5IniHQqk%2BXxr4xc3aaeRSTlGFa%2BRxD3BOcktGMm615rKOfng6Xwn%2F6xvZvXax5i40%2FXzPX9Ti4LDXcUYTavaj%2Bwi7HCcs5sQqWrlZ0zBuSuOUY5TUXCvOw8PLUtNxOpYUsAoU3aTPdz8Iw5rQX7f3CFUR08qg86R4SxnbAXLEIMizQ00PIz9qFIj32hDC0LUK2Uc694LR4aFqYipc7aQot9kDKFZQp2tC5nIImMtl672JduxuTXyN3LJ2mo3b5wiukWDQC10MY1gmeBMaE1GEI5y9Js1iFSlbsU2PTaneeNIYuo%2FMOO9khqtKajqdBEe7Qyvo1yA4sKafRitocmxOl6sIj9vNtSG2sgS8ZFWnBlkNENS4mlcrARMbWzCXuo69BjqkAUv3aNi571CwBzh42eQFAyq108LhhsqYhMQbtdWe4aZjP8S9ZefRFZXH%2BmcAJQDzrPmDL5NzsCHSR8pdU4nQfOIYhnZNM6hjYRyvBODNNK9nGiigjnyEY%2BdWtwBtp1KBSBW%2BgRiNIQQTBK7IaAzJFwXe6hBQUmcHqIyZe3dhUCD8PuJAmSGQwKIgNn2I4iuT8w%2B%2BwhkW2%2BI5mCMZtU6jkrV6jJsC&X-Amz-Signature=a19b72fbe8a09bfaea0b9b3980a8738fe7d07fcdbd1985ce89d214cbe0ee118e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJAL733%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBb%2BoSa%2BgH%2FnwhsslhqaEMLZyGvGegm%2FXiRBsEKDX3%2B8AiEAj7tMvTuRXE5hke8hVhBcAsgSlAhnxeCR4U%2B3foOSGRcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDF5qRtfXC8bkbQ%2FnryrcA5csI5g2sBpO9Lmft6i5v0gEGlGw0Z7RGgLpHDaAvUlAgZCgytLn8r4JfeQ8ukUx4puyMO8D72rcgWz4bQ%2FARxzs17rmkHwW3Za1WUXBNdSHoMvESkyRCz2rizV%2Bn14k8drmxKS%2BbdgnU%2FWPuIuJBfQWpxOFegIBJpyju%2FiVcXDIl4xpuq0be6PO9W4%2F%2FA2qHk%2BTf38ZY%2FIocOwsPS%2Blii62BjyD8bWr4HmL0iIYgDeLUDtk2YX%2BwYV8UukiwW%2Bq1vBKFDlbAXJmwWMWoKpHQPENucp5g42%2FWydbK3R2QIru0uSxtrN92%2FWVptOmU4pvciWBU8knkBgfnbIyJ1pKNX3BIIRgaWzmAupG77UGv%2FTpxh1flj%2BFux15xUNCOdoYhqiqrrMe%2Bp5HHxsrv9ZPh3K5OfM2Ekfum34pcNL%2F8iZTSMjkp8lEX2y%2FYSJ%2FnxQkam1A8mSCucym9hsBWILmpvQmuNlAaEK%2B1dOUUV5nZH38MHzQQkNDV1IpKzyi7KmAFQjstrhdx%2BeuQnBcus9ZoFkzR1DXMuhmGxoR%2BoYxWbqmVChRwj0sni1q66F2lh6n%2BrN9Dg8ow3%2BfWsbdQIPoLi1C1AV%2Bdjrlu0bGNiurmDnc3690%2FneaDeppjgZiMMC6jr0GOqUBOe0n%2FK4Nz8fee7MC3qI%2Bt8dsiaef83oXZDVKQCIaJlULtjznxmPpWIloLY%2B%2BZ%2Fl9M16IJC2siHnAlgZxSoiXOsGEpp2n1DeImIbkh%2F1gCqJ%2BOg3TRQAtSQoPlDxa1Rb2GOdDqsMDlkfqUia%2B9mpFpM6wEjc8PRq0SGHKyUNFuHSVPqTYHR4ftAOA6CuJbvQNYQewbPLH4oYbqzn1LrOLNe0B4VFm&X-Amz-Signature=bd892efa67b76f934da007658798bdb64d6df8449ba02fb1bab55956e2c07b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPX36I6Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEaD8R5ShwLvBQufFeOXpzb49nPxmBu%2Fk5vebF7FwvR%2BAiBuf%2FyD4iJMPu0X9IPOgcg8qp6dxzKV9E36bbDOcQJSSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMEwdafnvJj2BEUJKMKtwDi44F24fgWQF985CUf1kbs2yZLcmVF9gGPbHPkSfyOhmfXDGCjFJv4%2FzFIa1VfIovQ1HBFTv5WKxWwVpq8hk6nVZQA2kHLM7Lgvc78QpIJq408bGwnf1opRoS0r%2BnINpLDI4kl0lQJN8oNa16UjGdeOsmCmkcu4DGF3JM8XF1JBoCSCc76WJmebXWQx3u1QdtUqmhXR7nA2STt9QMYdobPUZT9FXkj%2BnWx%2BY6PTnfFxUemFsUnibj7RX%2FKQbQdiTuAiyk9WslIEEuEqVb9ma%2FnjVLHXDKJiyKJDFnlbFElfYdm%2BSsBRGpFJPBdi09hkAyn%2Bc5apwdcEMOy0I3VbJSxPFIauRe%2FuuB15lBvJKukGdzt2awjHMLlfX4xTfav7ggkuCjFM4rd%2BIYs5LQYaim7FcMixXQF6kxFvYA0s%2Flw5rJxgW5t2YoyzmvdOIOLtb%2FAvG2W7zTBAQxKiQEu%2F6TGPhdV8oQbEXvzCZ%2BYzm4d%2F%2BGvItdYpH4pbUoztFrYSuF2u9lyaA027v73jcChz7Ozz3fH17HeZvrQL2FaSUAkyEHwInGdL3tpSFBYAutxwg6ztWPAmyErdj3qYs7a3bjjOHw9eVSoQUDALvkdsB5O3aR5eLyT%2FWgxGRAKy8wr7qOvQY6pgGsP%2Bow9791TYoh1xhq4GE%2FLj2WrMDux3Uqg%2BTxy8hlEz4F%2FoNYV5EaDNoGNmMi15q66OYnYzd8ciPtI17iQo1XcrCzettuixRhHyKx9KQnN2XNH72WaE9KxbPw8TxvTc5kbUj6bmZot47Qe9sM5H7KV9yAzi2u3XUJGn5GunMNIjkeBx%2BI0VLjaxXYbVqIuyzlVEc7LnaKjRsobEzkfNYmbyNYL6iV&X-Amz-Signature=f32e356ef4869817f03d7cb0f623f602e1370a6fd7e945630b3962786c39cfee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPX36I6Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEaD8R5ShwLvBQufFeOXpzb49nPxmBu%2Fk5vebF7FwvR%2BAiBuf%2FyD4iJMPu0X9IPOgcg8qp6dxzKV9E36bbDOcQJSSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMEwdafnvJj2BEUJKMKtwDi44F24fgWQF985CUf1kbs2yZLcmVF9gGPbHPkSfyOhmfXDGCjFJv4%2FzFIa1VfIovQ1HBFTv5WKxWwVpq8hk6nVZQA2kHLM7Lgvc78QpIJq408bGwnf1opRoS0r%2BnINpLDI4kl0lQJN8oNa16UjGdeOsmCmkcu4DGF3JM8XF1JBoCSCc76WJmebXWQx3u1QdtUqmhXR7nA2STt9QMYdobPUZT9FXkj%2BnWx%2BY6PTnfFxUemFsUnibj7RX%2FKQbQdiTuAiyk9WslIEEuEqVb9ma%2FnjVLHXDKJiyKJDFnlbFElfYdm%2BSsBRGpFJPBdi09hkAyn%2Bc5apwdcEMOy0I3VbJSxPFIauRe%2FuuB15lBvJKukGdzt2awjHMLlfX4xTfav7ggkuCjFM4rd%2BIYs5LQYaim7FcMixXQF6kxFvYA0s%2Flw5rJxgW5t2YoyzmvdOIOLtb%2FAvG2W7zTBAQxKiQEu%2F6TGPhdV8oQbEXvzCZ%2BYzm4d%2F%2BGvItdYpH4pbUoztFrYSuF2u9lyaA027v73jcChz7Ozz3fH17HeZvrQL2FaSUAkyEHwInGdL3tpSFBYAutxwg6ztWPAmyErdj3qYs7a3bjjOHw9eVSoQUDALvkdsB5O3aR5eLyT%2FWgxGRAKy8wr7qOvQY6pgGsP%2Bow9791TYoh1xhq4GE%2FLj2WrMDux3Uqg%2BTxy8hlEz4F%2FoNYV5EaDNoGNmMi15q66OYnYzd8ciPtI17iQo1XcrCzettuixRhHyKx9KQnN2XNH72WaE9KxbPw8TxvTc5kbUj6bmZot47Qe9sM5H7KV9yAzi2u3XUJGn5GunMNIjkeBx%2BI0VLjaxXYbVqIuyzlVEc7LnaKjRsobEzkfNYmbyNYL6iV&X-Amz-Signature=614cac8a915cb50ea83392da0dcf7120835d0246f7c4dc2991f3a80661dacdad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
