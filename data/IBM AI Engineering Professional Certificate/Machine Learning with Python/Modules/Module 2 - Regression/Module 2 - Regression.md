

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=c1e753791f7a810329757579a902945231fe0d6c9bf7620c8f450a2868c75781&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=a6c039e51da492b7bb27c2048e9d7e376e747d685b581df6d729a139a2ade4b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=2b2e79d7206f33eac26f388ad812b13255b2eff369bfb9f25c3b69948fd17a6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=a5de9a7d608c4903a2c8988517119c0a018a3ab4361717d790187b486db779cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=3c58a3505381d46689acc26ac4efb2e8137e5e28f4df9f5368e961b6be32a7b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=179b61a489e948c3e669d21eeb443dec7f0d8d5fdc06ebfa30eb41f10d56f9fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=ec4afa46534f947b73ec88d518b25fe8e32b88de92a5c6f5a9f8c1e8c300fe46&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUEUUCC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi6qjk0icCTx9R1KuScJCE7Cz8MrrRR5Dpe8df7zsTwQIhAPB2r4VznJNjQxwf7%2F%2Fqm4Y0WVznFmbrqlS2yhIx7CC9KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhiHtltWnrRC%2BK98Aq3AMlxhbrqL4DsEbQ%2B90MAFBsHYrcPF1wKC5zWcxPuRFjtS0x%2BtxZEFPAFmas%2BnbNM8UgdT1LSoFOvkLnCfQEJgniNjSOk30x6C5z01FKjY3WX52h7X5szeT3HWEwt81b7W69p1HSWDKoqWTQmh%2FxxB8TNv9W1IdMhN0fbTX6H51BytONQwhWnlGNN5PkbiZ%2BNgXIkJv7dKQyKxotAnmDxeShqlTRhdSAJiEGNs3hmM07RqYZD297E4wWvPWcN98z%2BOW7svfjyJCxMqVRyn46kv4DnPbX7Z1zagHGDG0XALbJu7%2Bvk8mXYK6jfTiFuoLSfhzKq%2BBt6YcH%2BpYCqkMCY%2FdcJ0t9X4BVGYCLxMVxMRO7LIU%2FSTMdwFAbHehelpNIHmrOqeXQvsb8oZ5wgiX7vC6PJUokHAkpZnz9DKczz1kCA1idxyIGhKfKkHOXqefYgwhPqypRRd5bYla8M4%2FUPe%2BbtqAAER%2B1QqqEwN1eqzw5LlvYuhK6%2B228zmJMfjlBSoDbXmMtutCBRsM2it4W2JnOmcGCqotqQz8uu8Ch4rjlONgl3sB6AaXnh4OAGG4VAohFktcgryjelTjKO2Rru1%2FH%2BADctZp0qaEt3zpVazMfNThpqctXXq1fShLvKjDvrPO8BjqkARyDt7XLoskc63pCY3%2BbbbWuVjnwozx%2B8TPCha%2FQsghV7lNcfChFRXIdNhd%2F%2FUKDdkkr8MmkvwposashGqULwnfa4o%2BChgt6Kfgn0nCXGwvOpnDCZMr8qUAUX97VWhj1c5%2FcJRjpf49aXvXLCvV8bcvnkLBHLOr0K0cvuhtGBhlX%2FxFlaLSgdk2QzRcfteSo391W47F2SmztNXfHTGNTKUjkcBLk&X-Amz-Signature=04b935a24c2166cab98a6da6189df4960fe7c71d997039b8d002d7ad6c11183b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ILTP3OO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgMBOyrUDA%2BGAXH%2BmaitABzQ4sW%2BJ79HnbulojgpohUwIhAKWeLLNy2tRvBpozzQNp3z5Yly4r0S%2BKEcgDrms8nuIAKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FQrRCSPNwMudaDK0q3AOB6HjkFPZSu1HdkFjYiSmiZLwhRpqu2J2HHetG%2BcPgZDMEVVzgssVhsxEld7oACA1r7Id67a2ozX7R2EKMogHxbi3cxLYPh%2FELstKPlqhay809f7LZk7D5fsY4ygVh3eQKNfKNdyOgDcoJua0P1c06EZ%2FCw4cdOuNcUC1IgvyZNFzAXS1Wsjb8WJ%2B8eIYQ%2Bt5lYodgsliKuPZR%2BlLQD%2BcaYAxZ5YBwFKPLDgP7IAc2Sbki2Ih0WXnRcY2lQmAm6r3wKcYHyU6S95zuDeGOnVO8w9DEEFqwWcIRCWlqyS7h21OzjCy3%2FzMbq2iXpKGU21aR9%2FpStwZe9fZ6Ghog9rWhYq8HFKsuxGrVndYeGNmVJY1zWADvFgpChKxUxHt1fwYCLnUgRyyBHFiSBrxAPfHx%2BORfsiRD31mDKGgvPLg3xCM095x2us1qnW1dttAZ4xnJVLjv7jl3iB%2F0bZQfDp2Uwm91r01kAewcVDn%2F34%2FxvSngAKFtk2s9J6ldO2QW44w196MxA8bWcpZIBj7jzH8xLIdRYaYFbNESbfzm4jDkIt5f17lkbWnN4K5brpuudSWs0lum%2F42x7J7PraZHiODIhajjgNDMbU5V1UHkZ4YYYc%2BaWDgzlSq84zmOKTDprPO8BjqkAQ6kANyjbKjby70YOmvlefN6F5MMOtmU8NLkEbWEiAZJhg%2Fkl4XJCZbJL0sT8n94Rb8xv6PFj244LIo6Zpkx2DyOdtwi9eiyblHNHH0zbNL%2BsYOAB8gio%2F0pGt1IBOKVaQvBZa9vvu%2BVHKBWRaflRoA3dZPESC62L8H6M6uek%2FnHHdMA9Ri1N7NbTbAcsIIJq1hvkbYjmAk8dGWDLxx3A%2FVqnbAz&X-Amz-Signature=a0ba42a9c6594f1ac0c51b99e3624347a48e4d69d79e9023e49b3e7dbd214080&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHPZ6RDP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFscWJsHYqYHVG88GAiokcXRvGWPHoZj2gdoNau%2BEwwAiEAohshZklUPTxNlD9olgV2NIJ7f1aAcb7F%2FHkXZIhWp%2BEqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpmeI2i04pQFXAmdSrcA6MSjY7N7x302%2B37G6lDWyXFw9UHdiWMW9i7rmMu5LEUvrzUvjRD8vh761uWje%2BidsaXgK4of2uCtWJcudOTp%2B1%2FYmEdLxbyuUnC0z%2B1r6XyDnqADjd%2BZEhPxjpcAE16WGeYM20Mnu0ooja7JafK2dUBUcZCTSFBdb9q3Yx9TFZu29Fif6Ynn6p3b4UWPSQm0uXZhyOidfb23syvBJD%2Bu%2F8mobzxeLTolGCPnhMfIE%2FkImvrRy22tIEm%2BZvU6WUFNALmNiTgtLzpZ2qZBotkfRAqJEv%2FUxJlxQNE%2BbYXnYNe9J5jEhkvNPgjAiYZRluUNcD%2F33xXRGtKmliU7RhpDPGmepFioQO7P4x9HjGXlsLtRVxPd9aTnGh12bCWSsc%2B4EiJW9Rhqkf4cbRO6AM0qlgCIqKUP3340Fhj58YBxDU%2FaolxaaiLaFjB6yoMhgAa46Ysr%2B4hy6mtRd35Z%2B65tCespZbwr1bDQOrkJt1Jb780ex7Ljch6iKZoUGI6Rb5PzPl7AR9TLa%2BRl0eo9dWf3gAkViWIkPMM%2BtfZBnFJ3jFIbaCcdBC%2BHF%2Fz4B5VGibzc9Zm5TKcCueIE1dh9wU3LkPwJTVk1d%2BKKpBS712Xjev454hSobi%2FSCbdFj44MOSt87wGOqUBpHXMmcfn5PqVFi4feUdOunYj3oyUejsWbZtN6LUvRNTFjWXs7V3tLsjUnnfsdQ3w%2FnCAIVnrrIGvGj6h%2F0ah5hjPfm8RwiP9vtqFWXSAEMrXxhbk63%2BGzlxT%2ByX%2FeQAJd1fMd4lWBzLUwvxiIfgiDSrdudNQM59uhTjXtyw%2FvMYf0BhaphBOtGGsq%2BtGnQDUUh3iyj8R%2F6RN%2B%2FrSwspFvEU1IXwb&X-Amz-Signature=1dbddab5c3afe43aaf052a6a67a02af8307304db23892def7cf6b93665f335d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DAOZCGE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3p84J0QooHT%2Fn9JqZwo%2B3v5XoQ4zoVciN6%2FpFvTKN4AiAOQcH%2BzrSR%2F5fyj9h40WGNXmVD7nHNVgTuG%2BXEUTILbCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT87FYx2zHfnC%2BWROKtwDL6%2FiZPtGDxhIhlYhli9GLa3ZKBB2%2FsRRqpdo3H2%2Bj4dy%2B%2FhqqzbgR%2BTsdZNGYfwEC8WcGHnKWrmHsuFnauLMVWdxGdyLL2%2FlMqrnvjSyLzx77bj3yyuFzj06Biu5gSv3YYUjR2pJ0GT4gZnM4G6wMoNKeBC%2F%2FIHSp7Vl3cbSorxgZJE%2BnvudJqRu5F6Rkabc4auPF6FglZBkp08H%2Bedhk4H2aMk%2Fl6LJuGqOGpVul1NxxGjGc9wDzYrQbqkKeKJQV%2Bxi6TC5RCbq%2BGeSrBuTceCWETZ64c02DTPAfRvm4JmPc571%2Bgb%2BV7ZoD%2FuRWaqjvJwq47wx7AF0NBa4Fe6W80%2FjqCRvvew9%2BqqyRNmLIB9l%2FQ3VoftuAR6uS%2BqTLBJT96a2I0FmM21%2BFAeWAKYLBWdx%2Fq8%2BB9ChLkG9ncUkMH6MO5vQMQqC8HMyw6xAIzkJTb9DFEOOHwTYm6QY30ZT8vnOHCDrh8RF%2BpJmSpt1u6TuDYqGjhql%2Fb4Y8rT4Xu%2F3taUhjfGdbtQBTD1O3SrzxgZzWDlD3gyXw1c0NhsM2Hfc5CRojcMs9Y0FurLKOARHdFomrSCUcFgEj0uSOJEru2oQfwRlDUjwk%2BVOZDAiV9NtXDVlaaG2va2VkKYwp6zzvAY6pgEPWXU2XdkGNlEnl4bQli2GPq3jkdjqB%2FurqerJFLDMqGGU4SAqYNSv68Eytl3ZG13oVyBcEBsxUs%2BBKjsLH8s8WIjbq06ZWPu6MS1D62egfu2wjpHBHzEI1T6XeUXwQz1zLPxa2JlbCOAWwtt05sGq4U99vU%2FLaxDRVrkDS7lDVl9wHaV3IeM%2F4zP3ANL5fYKVPnvrj%2B7paGgpSXJoou1pEFO597oc&X-Amz-Signature=66cc00a4a2ffb2886a4db569be3d0668ae98a3fc4550ea781ca73bfd98cb4c90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DAOZCGE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3p84J0QooHT%2Fn9JqZwo%2B3v5XoQ4zoVciN6%2FpFvTKN4AiAOQcH%2BzrSR%2F5fyj9h40WGNXmVD7nHNVgTuG%2BXEUTILbCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT87FYx2zHfnC%2BWROKtwDL6%2FiZPtGDxhIhlYhli9GLa3ZKBB2%2FsRRqpdo3H2%2Bj4dy%2B%2FhqqzbgR%2BTsdZNGYfwEC8WcGHnKWrmHsuFnauLMVWdxGdyLL2%2FlMqrnvjSyLzx77bj3yyuFzj06Biu5gSv3YYUjR2pJ0GT4gZnM4G6wMoNKeBC%2F%2FIHSp7Vl3cbSorxgZJE%2BnvudJqRu5F6Rkabc4auPF6FglZBkp08H%2Bedhk4H2aMk%2Fl6LJuGqOGpVul1NxxGjGc9wDzYrQbqkKeKJQV%2Bxi6TC5RCbq%2BGeSrBuTceCWETZ64c02DTPAfRvm4JmPc571%2Bgb%2BV7ZoD%2FuRWaqjvJwq47wx7AF0NBa4Fe6W80%2FjqCRvvew9%2BqqyRNmLIB9l%2FQ3VoftuAR6uS%2BqTLBJT96a2I0FmM21%2BFAeWAKYLBWdx%2Fq8%2BB9ChLkG9ncUkMH6MO5vQMQqC8HMyw6xAIzkJTb9DFEOOHwTYm6QY30ZT8vnOHCDrh8RF%2BpJmSpt1u6TuDYqGjhql%2Fb4Y8rT4Xu%2F3taUhjfGdbtQBTD1O3SrzxgZzWDlD3gyXw1c0NhsM2Hfc5CRojcMs9Y0FurLKOARHdFomrSCUcFgEj0uSOJEru2oQfwRlDUjwk%2BVOZDAiV9NtXDVlaaG2va2VkKYwp6zzvAY6pgEPWXU2XdkGNlEnl4bQli2GPq3jkdjqB%2FurqerJFLDMqGGU4SAqYNSv68Eytl3ZG13oVyBcEBsxUs%2BBKjsLH8s8WIjbq06ZWPu6MS1D62egfu2wjpHBHzEI1T6XeUXwQz1zLPxa2JlbCOAWwtt05sGq4U99vU%2FLaxDRVrkDS7lDVl9wHaV3IeM%2F4zP3ANL5fYKVPnvrj%2B7paGgpSXJoou1pEFO597oc&X-Amz-Signature=a4c98c9d909c2af1a7f0de720dfeefac01a8470500849a36fac1f41164d1d3ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
