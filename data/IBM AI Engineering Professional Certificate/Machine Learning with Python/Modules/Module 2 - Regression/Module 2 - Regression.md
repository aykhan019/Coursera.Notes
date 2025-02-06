

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=383c8f75f94878d9506706eee09979475e189ad8c3b09ee50f688ce1c2138ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=ff154c7f409d3e7800dfaac78d556d3451c9bba225ac2f4bd6745e51d9605944&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=2155415d0daff4575636a764e2ae7387017be2b847cafc6b9da321b803594571&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=7cbab778944f3d12f7e77c215b0e93c05d431a80ee4f6d82e6f3c61cbb1953fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=2774ea358c9e17ed55fd5d52abaf25ac6cfb89b6f869f79d4198c5d1a767aae0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=153978958d5109be61012f6db9335dbdb716463723dd2a9be8fdf8efc3bc147b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=9b93c3d7d9a72c170a55a8cec76af861b2637e12797d699888fc0d66d8f56fc9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIWIH3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpshAPytRY%2BQPNvg7P86mfQPFxxM36cxCvj0DdBxPEsAiA%2BhWmBXSzmWfb9hFLjI0A8lMXv8dt3aSESHuU%2B%2BtBz7Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM0w4fALI1XeWNec7ZKtwD8lyEDc%2FN1NDlwKQ0JxRO5H%2BNk%2F5DlkWhqwnNUtpOM0jU4UcCzFm%2BN2Gmm0i0Ja7DKmeqer0qqGtfuaAI%2BdC90RNW4NP7su5TVvv6S0ZI%2BF3rStX%2Bow0dci%2BHtiVFdC%2Fa1h7jb2Ll9MUpgpeuSrb99wk0Ro1vyrHFx%2FEclDPmYE8kkx120kw9%2BC0jn8B2DdpOO9ZKMILjmexr%2Fnpni1Zk6WlUiGzv%2FfiVj4hEdio3aK9I6ZvhHVarNaCP1R8a8eDRr5rqVJVcxD5tIXdpX9wyswvBKZOLjgJHxwDAfJ8MTj3yqMhsvYJJFT4DrVj7I6pt3dCeX6wQybpk7BlG6ZYyG5t8sMmp0ilsprOqpU3%2FZ3gZLLUtWBP%2BVYtNpFlV2jVNUYUdvPqV5U0rfqlBTQcbXvpKwzssNBoR0w9RY4ilkDUoq0IoJ2yGXNq4SKAIaAfYkHSHvGpRc038Ylnd5%2FqXuicH4bx%2FttObaYUK0Tcg%2FuHiMHtfHqfd7pfWDBfY0LPglamNxO2Qu6D2cXw7LZXstISPcdnEk8%2BZzBkLPkAT41iYbAjSFRkXa63jl5mynSyS3cSqTuDNFO4JRglAobf3Hsmk93%2FWiJWdT%2BOYBEaaLyVpjVNoXn8A8MX1Fg4wu%2FuTvQY6pgEk744eWRSvmNUEaQSZKBX3uvYlVpwWqNuOQuRRco8JxI1fXnZQQZ3IjWbbFWQI2MK7DdZ%2FcNX5p8zdjrFTtRL3yXmb0fT6OoN63OVQwUnTk9WzaVCqRU16uEXvYpy2uL5ZZ%2Bzm4HB%2Bhhou%2FIHGsTbvv8Kvr4myXSOHzDBZE96RYNAoQSbxMXCVsXvH2sCQEUx1huXVhoOqcWwpr37jWPlAEfY%2Fpk2V&X-Amz-Signature=5d8767143d23764fa0c85455b0ceb50c2f8c1240ad2510e408f8aeb5565e82bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DQ5Y5UG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD08VHtzFG2PD1BpIQU%2Fb4YD8Nw8d4%2BMUIdbEzxb9csZAIhANk3MbVmQETolS2aUlaEXKsU56aewkzaYr5ukFv%2FWu%2BvKv8DCGMQABoMNjM3NDIzMTgzODA1IgwwbLmDiW2lNg3rqzIq3AO0wx3kgci838WbedpySgFJqixxo5pxF%2FgnQtytxW5NhCkrNnzy9%2FzCJSOr7vtDi7yYy5uFp56lusNRM0gfZ4LtUQ2U%2Bvk0MtvwkOz%2BRyurrr4EAuZ5bjzpNBVrjfI1sXMokwdy2YBcHDutrYAgkD9PRee9b%2FUlGjeF0W9f7MccxO9vUwlNvSTsCmGBO%2Fj49%2FWVehZcDwq01D5bfKs%2BNTbfRJBAmACEc6BV%2BPW64ZKGiq4FKPx3a2UF4iqTa4FSRQdsrLj8bNUYY1%2FXYLznQ9pbHDtd8Hdy504g%2FbPCTw470IRl6Kb6C79f4raif2XNYAZArxv5Gr9XjvCN6hoXtYPer72ZjcbylAxKF1l8pC%2Bb13v1rEVeTEw1UIdrueK6048r20MCuR%2B%2Fq3AEULM%2BgaBPgKGkpWudtCm5a8axHceWYWa%2FaxXp9nvHn4noMYstaG4niC2yw3uScPARHXeJCUjV%2FkdyM0ij3JwnidvetbVCTTG%2BmpjaLkJLWLjXI2G0QfzEeyLa38RM03rabGIu5AwVp0NU0AzFfGxmSV9JjepulL68sfp8y23EDcfnO3PDyIsAsx6mLZiVLjWPJRHDOCWS4sRfl3ht6koD8AsbS6xPF9S5qzHmaOZ3OG4l1jD9%2B5O9BjqkAaYVVUqfeRzWiRcx69I2WKV%2BuQl6po81Vez0lyyqALNJG3g0urtaqFIJNEQX43EBpUzOVHhvSQqIyQNqIPHQ%2BWw1M6cqCRl2XMDKUYcGaKBZLld8S3sCum70bmva6WevnWDuGXflXGMo7nd0A5KgZjpjmsx4Tg4MhVfxhvVxieTH5dD2SPELPH0P3M%2FDFrRaO5W4wDfxAT057WMY4kCaIbeDoxM3&X-Amz-Signature=f288871f21e8bfc1df7795ca95169a607fa8f26995fc1ef3dd5bb242619f3430&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSNZWXOO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAImbvu0zNNWC%2FFs3EMyxaTl5OtfcbEXmzowBXVOeug1AiEAjlrYJXwEf%2Fwpa0J8ZFmJWTxbXcFWYy%2F8iNTZS2RldYoq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKWQ6mAMOmcFj8kTyyrcAzBH29pZR2rVzsxjAAKtZ%2BWFUWWbfwEFxtVflYtI0booThs1yduFAsA8JgNpvDmlW%2Bu%2BytC%2BCjeaJ%2BaHzPjMnHaYYmWz7WP9Sl3BxIdEICrz1hjpuib2vzOHrD7CXtsSOgbX9dgcuURxFtHyzH4l9hstVeWEY3%2Flz9ShAd87l5fMgI4hFRb2rmN8ANOrim25a5XgFUsi03jsz%2BMp7CMDnBuNVsg04t%2BxE%2ByhlvNevZYcZyYgRyG5uAkDXjUCkfm9S8zgrGXgWUv5UV5%2Bdh%2FuvlRY1SOKw2X7TvLoZExvBI2xBt9072MaZ3B0E52bYdniWiEzDX4mxEBEdNdsyf32kQZhiiqdbIMlH1pfXZqqn6G4SBJsoXdwfwwEcfLWsUXIrsXq0XQFajxyIDqUBpUZXm9WwMgficyfylz3MYunPD2cI0YdJItxze6uJ9dV7CEddk2BQ7RJSgouaqgQCPh0gft7acYRgj3GWbnBiJ3vBHfwdNMrNKZEZwgUsJWreRufIw6T755RDlKdALyftSs2a3ot1On9P3%2BZzB04q7ajt%2FuiN0q28jRWEuvGxo4oG20cUAWVUx2D1c1rngODfdtFvC9AkIj8uLmQcVcI0KjFWsK8I1R6%2Bekbv2MmA%2BUEMJr7k70GOqUB5B6KqTL5i5IqZ3C5TcPD9KhjdVsaTJP528y4fREuvuiPP0X88JZ3%2FVJUZpv%2B%2B1bivvYAeZkXwqStrgJhOXhlquMErWAfzm54tAL%2By1HLEc7qz9vxGfZwyu68RQjKnokQK0KVLN5djIW7SX5bWNFmDn%2B8kIFJW1VAPWEKV8oXSMACrgFHJCylG8Cb1PNwyYXtJJBvy30cSkOaVzx6dX2NlyCmFwT4&X-Amz-Signature=784292e2e6fd69e287ddef44bce403e99d2c17fe7500d53e7c0a6444cd0c7eb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMAYOMBG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDoLjZXe7jFvoeG8IANIhZ9NDaDDR6ApWwElW3UdZfUIwIhANrP9Vmbgj4CpQphcaySioe3ADydz8rmHJRtkYlnMbLNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz45QU4TgahWiB7Gmgq3AOrh0IPY12icS2%2FOUEH1uyO8kG%2F4gyITgEGDPOJbAMP7ZAx%2Btf%2FWb%2B%2FzTZskDu111O5BP4lLePMP7feg1t6LTV52md0urX6Q4E94xUOMOwQLeO%2Bak50cN%2Fvcq%2F6MojKaLg9RnJBiD8gu0PkuR9VhfA%2F2TjB%2FZLsrnzgjqc0CXcOCXsteq5BgZNwqpvdtjAuqeOz0lK78e4ViXQ%2Bq1WRDAFDa5zek%2BvdwfF3pizCKK6eZfxkPpWDj%2BXs1tStWhdWmtAIc%2Fr93mquI5YfqmKJpXpd8jWv%2BsZM0EF1YNvfXNhkQouKUsXsicrktKteNDPTzGHhgPKNnyFgzqc0T7dX4WAZWuB0Vqsz2FzMIuni%2BcHOzOux4M%2BBOebaL2ip1WOji3UJHsuXEIFPfLDwu2fzroLn3apSlOJ4woxb3uRs%2BhHdkR6UMo9ePYOhSbr%2BCntknKobx4Y3KsEXa7DEwr8u7T1vDUqK7ZuVXUXoQ7Yr6GQ45n%2F9j8ncoOLDttl4SEeAV3zKboXOLc52LMgkek8riWWesw2%2FZUAebWJh6mqCh4gf4IgFaYLvBOnjGHU9FoPBZqXXN0oHzl7l3xpx%2BFbmI6%2FB%2FWJuwURdEgbsXE0zQE1lwjktR6DU00s5eJdhyTCj%2B5O9BjqkATBVvjiJkoBaLJ8Jbwgn9f8FYxgUeXwbInzNEv9B2t71%2FXaF3P73RWgUuvri5ZsSilmK%2FHTtDbdz%2BvNgzCjbgJFShak6poX678dmusDRhlMvViUVZfUI0ydA1xyyg1P4XMXMGys1Az5OeOX6jP1YOjFaWpDMWSeNHu5XQTSND%2BXFr4BS0A7pcNluYdJYz%2FVOjSdZ3ohphI%2FB2JtxXGfGqiR3OhA3&X-Amz-Signature=a00daf88a02a7833e91107e885a01edf066ab965d0a3ec5e8c001d63afe2a762&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMAYOMBG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDoLjZXe7jFvoeG8IANIhZ9NDaDDR6ApWwElW3UdZfUIwIhANrP9Vmbgj4CpQphcaySioe3ADydz8rmHJRtkYlnMbLNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz45QU4TgahWiB7Gmgq3AOrh0IPY12icS2%2FOUEH1uyO8kG%2F4gyITgEGDPOJbAMP7ZAx%2Btf%2FWb%2B%2FzTZskDu111O5BP4lLePMP7feg1t6LTV52md0urX6Q4E94xUOMOwQLeO%2Bak50cN%2Fvcq%2F6MojKaLg9RnJBiD8gu0PkuR9VhfA%2F2TjB%2FZLsrnzgjqc0CXcOCXsteq5BgZNwqpvdtjAuqeOz0lK78e4ViXQ%2Bq1WRDAFDa5zek%2BvdwfF3pizCKK6eZfxkPpWDj%2BXs1tStWhdWmtAIc%2Fr93mquI5YfqmKJpXpd8jWv%2BsZM0EF1YNvfXNhkQouKUsXsicrktKteNDPTzGHhgPKNnyFgzqc0T7dX4WAZWuB0Vqsz2FzMIuni%2BcHOzOux4M%2BBOebaL2ip1WOji3UJHsuXEIFPfLDwu2fzroLn3apSlOJ4woxb3uRs%2BhHdkR6UMo9ePYOhSbr%2BCntknKobx4Y3KsEXa7DEwr8u7T1vDUqK7ZuVXUXoQ7Yr6GQ45n%2F9j8ncoOLDttl4SEeAV3zKboXOLc52LMgkek8riWWesw2%2FZUAebWJh6mqCh4gf4IgFaYLvBOnjGHU9FoPBZqXXN0oHzl7l3xpx%2BFbmI6%2FB%2FWJuwURdEgbsXE0zQE1lwjktR6DU00s5eJdhyTCj%2B5O9BjqkATBVvjiJkoBaLJ8Jbwgn9f8FYxgUeXwbInzNEv9B2t71%2FXaF3P73RWgUuvri5ZsSilmK%2FHTtDbdz%2BvNgzCjbgJFShak6poX678dmusDRhlMvViUVZfUI0ydA1xyyg1P4XMXMGys1Az5OeOX6jP1YOjFaWpDMWSeNHu5XQTSND%2BXFr4BS0A7pcNluYdJYz%2FVOjSdZ3ohphI%2FB2JtxXGfGqiR3OhA3&X-Amz-Signature=027eeb384a762c343a6fcd48d48cd3bef3a89e510c1ff7c165c11e82b067f1a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
