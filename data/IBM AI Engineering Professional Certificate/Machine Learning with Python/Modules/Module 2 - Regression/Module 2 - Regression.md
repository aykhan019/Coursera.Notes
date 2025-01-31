

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=73c67743dc6471e67c228e16b1d30b1423bc8b534c2587b08eb5d14359c82078&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=bc1c98dc4f26f1dbdf3b3d33e2f8bece2a094b30b427480244e7b16b29cbfdef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=1011a74c20e639d6fcc759b6aa8aac40e3f0ff63431dc2f0e342593e53003def&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=2c75aa83a0dc7840c01384f49ac6e348b9c2be9194a7fcf1ea5218754cec60a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=cfc8944e09180d64dc118e1e4cffb3d4e58a16b4e11d0d96dccd26ebe9c3fedf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=6dd7720373ff44def6b15a05c6d349762088c81d8ebbee8e2f554d24cb61230e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=b7f98262745b8d0ced779c0296a5db8e5296f33946e7f1579b9daf5b8d831c1d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2DLGKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO9aFhDxkJe5GBTNspqZdmrBToIF5vqQm0y9JGJIPkAiA4fiSPvVHgxB1OL8X7RAgL5lm0VdDxS0ZHb1rPAeXrOCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSCCTF9nLbzjHbrH4KtwDJFr1PoT6xexI1exMjCpPKwBFB6XfEptI%2BAD%2FXrii73Um3Lr2bmElTfgUuktCvfvBB09q4%2BwXYx0izfVZ3FUt0dzk9UgXww2BvQk%2BfK7SHCbcJ%2BY5K%2BnArvt9XrloQSi5ZRgtnZHW5ZtfxNGhVq%2F%2Bx0ECRDYS2dJ20BTD7S8COBPRyc8CKRd1Cz39DbRfDI5hBTx75AtZpqCsonSaq2W3rzE64YFa68hI30bzWOvhmj0A2%2ByZGOFWM1802eA9Lnt7ent%2B5RJwXks%2FpO%2Bo5YxvxYiyL3H03w3rvJDiJTeQRj5cN2iF4KZHyl%2BV%2BzEPg1k0tyggT9nIbd3pRals4aewyeMDm7dH4z%2B%2FrVnb7sOYXHAwlJdo5zj14Sp09C4VRPOxBaI9wwLZpuaE8vMzYxxs2eymVbSAFfuNMbNc6zWCnQ8cXyhYVSU8Og2MJ00o1N0uTGPlM1HL3evGzDYReVMYdtyvaTw4m9VgN1OTEJqkVQv6mrOmskoyjHZtTGEcZkBmpr8S2i2J1mqq4g8CnT7mKure66O1Hsntilcous5dlJ2IDmslGwyZzlSkrmZnEZl4b5BZefolUistjS%2FWLrrd%2BIlTa0qkS3FfdsdswKKtL%2FdEOnwzsnovwmKt4Icwh9v0vAY6pgGYFIjG9zQW%2FcDv%2F0VzW56kBGanYJ1siwOifISQZHF%2B8o6QS7YXQsNRTps578vOhiErh%2BMpU147pOwYrn5S1sWWld4eAmCx%2BqxKRgHQkbbINPITGO%2FMB3gXHTiBiJDNy5OdKDpsaARXKuHKqaRLiVANblKot5AxgM5e030xKN0%2F2gYwZPh%2BIUPhg0dp%2F6Dz%2FdagTZ3TO%2F6Pz1kYKlziwY1hOd2m%2FSj0&X-Amz-Signature=29ed7395a601097e9d2d852d94c9e84d45039e1f8eeb717a8f87d4577f0ac1dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHVZCAHF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIhuLgr7V3JTdjGyc2pgdqGgLu7oxMeatPil7%2Fm%2BI8hAiAmIaJZ6DzJVkiNfTi2vgcxs9lHoDXD65XNsgu4XkeLeyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd9sFWlqQy9YtVnwSKtwDV2tj9IZ3XDrntwQ5CfxZfafRmouG0zqOB9i15W9jPH%2F%2FRD9%2FLJ5M9W2%2BKCFawtIzKpt7%2FUenGMgt95j5WOcF2pxH74%2BbiGemZBoXFxTTEG4gzKULb3HeHS0rRPjyTmBTLWhLj86Ifpu2dVX49ZC%2BF7cTGPmB%2B4B4ljEP3P4XvVoO7yg%2BPVJ7LK0qzlgFpuagtikp7F2%2FPjZ0fCmrc3DTbXsNY7DZlkpsl8lp0o8XdQq514iM4eF6B1J3g3n%2FGCSUoItOP3GesSoTJEpyvdaeCDy%2F04LeDtITOP93HK5PCjK94YTuQIAWENDp%2BMdWhFCZRZFZgs4Eikn4CCe0dyB%2FCKyLTBgaQe6Tth8tISdGjVQliUw4ymqsa9vJHU9lRp7m6GZKWd4lkwKGsBlts0RB7lGmPidLzelgsV%2FR9CSt5gPv8bsXKkmM25x7Oy9Bgphm5Vfd6cOuBlZi%2FaaxqCADrpI%2BZImulVAnIHM80DRCJPXxB2I3PP8Q9jZ7clR60FnIRBzIU0yQxtv%2BGQO%2B%2BNuUYgb99CboOXkoGJxjXcCRCNbSkwGLOpgOXkmp3chHz6DctAJJ4ev2TQXlqoWzFmIyWO6IZtKPcCdzLSnh36poI7cE5lzdMjVqRRrLvxQwgNv0vAY6pgH3t8ji22sCHUOOCqh4NhZsRWjCkIGEy2s7SPRTQ7sgib3HMngoUPGCD7KCZSJQ%2Fbqwnq2uQqHdXOqrFGob%2BLuIGVYLbTECEsaIAHBAncWFELf3HcXNZkYQy0NSZx5pmgUa94FgOOpigSO9GQDGwCoY7DdvHsZ2R4%2B7JnUfQuw3mP8iTdLG52Q8ClGGIj0eQ07yB75ENkU5UuhopCW8AKHZp0%2FapH9F&X-Amz-Signature=016c8a549425eae8b4d0cd2c7f42e3696b2af2c4df3b0fa54de2fa32b1099322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLETCNGH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWFO7PqhxZ6HTA0UKOCayZyqBmlILIWGrATHiu%2BRXsGgIgG5WlrGXpPqi0FFlmq8hKRUxQyW%2BlLdIg1BWWOQe%2BRMMqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLyAOc%2FMW4AwtLVWbSrcA4OtFR%2BwRCJz%2BlxroQjCIh%2BrwyjnHQrAQ7A8yhNU5RrFKBZ6vJ6VDAyY97ZRdze%2Bmz9cd1hQ6i3FyK0HQrIkwBO6hdkDJhR8tp8wu8h%2BqsJOt0shcFM%2Fq2qQfp%2FK9LVBaqUzutpsAbGpmL1do0QrQvgJvU7lmTAc5P8PBlBJsPGXcjK1qwNSBVvnMmCjmIwndvnrx3E0wg1JiO%2BAtOXAMiBBWVh3ICTRp4Sm06FSaIPnV%2FOkJXxcwcUSUtxTLEJllZwq8B9BuHCgBtOTRNIjJu0OzQAfZfY0zX5%2BPVNzSyvQUkmj%2FeVF44s3NXKTvqWdN2LLODmiUUHPtuXdBwRmWBFLEe9gF8Qt4IJkydAKkw7siitzu%2BtbGXQvFkpMgYHetJaTZUYgK3W%2B3W7y6JU1iNA8CHS68bfDLX5G9qCJb4z3wJIzdH7TY5ofM1ngXG2NRu9dHUY318bMo2JsimHEbw%2BbP9NzxZqO24ccoUOSfuocp7JDA9OVfF6PD9WtEDVlImVVaxMEmUZSD1tf213nKhmf1bX%2FhdOFQt0LAVdt5mTuZDGxgXDXiT3N8HkOU8PH2kVEe2W3kTgOQUTI%2BZZ25jHaiR28qeu3nIp66hNcG8oH%2F1I6bWDLNwfPkjYdMP%2Fa9LwGOqUBmUaCbXLOz2EJ6iaezwgV%2FPNzFRH9g9q%2Fscap8T5Pt5WzYTqdKbG2ZMN8jghWnzx%2BbbMrmiTtszpk%2BQnU1OKyHGEiFylOmTt6NG%2BhiTLC5UjMlrQx7gEl8IQcR%2FOK2TmYtZ8pMi%2B1zl4rm3X3tjR4ZV5F13qbGk5XBm5PVB538UHE0DfOyxmZNKuf90i6Y9gMrkwm5ZU%2Fg0fkJIiJWu9Ovq1PiD6T&X-Amz-Signature=159516b0b5b2a2b82d7da55120b0bc605726e5a6abe660c0093cf97274b854a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQYDF5MR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPpKAlU3q9k9w2oD%2FiUK9xtxoRiH1nxv52REmmv08EqwIgYrsvOqhn9jshHHMAAZv7k0aG8njsIV2OV7VYSB47DPsqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdrkIk%2FfCVD0lxeGSrcA2y19TlF6AMeH78ToT6iwrNYgvw%2F%2BhbPO6o3RsNHNxce2nuPpq6yHY9ePJkyfsey8h0j3bbYPzy0j9y5j93NyNbFazyDJLIjOCnRm7RVR4KV0Q1OT9sm9%2Ff4cA6rAqtwrE6mNevXinN522Wl1iSAvB4D%2FI0HkdwndmYtdLGxGh9QGESlJtxOIkSTBbN0D%2FYGStVvNak%2BDxP8Ghlv1JCJ1oX7XyVbRlMaOPZIeSEh5%2B1b19Oc2pNNV9ESi0r%2BXtvo0D51BRhvbqh80Gi4g9XOYB63OQsgKvh5o5umKhx5Ko2o89DwpeQdFVdXzpNprrjcbvtLEtMc9%2BOPy2%2FDlxGheepPBnYU3LEUzWSpWT%2Ba61rcKiZ7L9kI4H%2BKZSmOHAKSiCnGC4iH9wrRGQLUJ3EVGl%2FoLZJBJ%2Btl8mmsjrAa5fLTV%2FwtA%2FecG1G0JdqE9oKS69lr0%2BCpTeePGJYvdUC7LoHk4sIH5eiray57Pis%2FZN9HCF6O8nZZ1i1cdk%2FDl1S6GtpEXJ%2FYI1VdBs853bFMTvPtb752jjBtP5rnW7%2BvuNKOzIQQyI1ubg6PDhtOjXaaw1esKLGnU%2FbJSFDfe1VJv8qTWgywZMQ38%2BsqewKf5WFxpMxJ66fZzP%2Fc0c4jMKbb9LwGOqUB2Uj9EXRaI51orG5PkBlBEbpSCZRRxihj8UTI3BUxgGFP%2Bp5yWo54gkHfW5YnMBkRcAfj0ESkrgJ0Bv22sC%2FGLy71Y6RFuesCYvdpJelQmyUCCFi1IN6gv0xYQQuavqT0oWF2wikWbULjYvF5x%2BuzgpoJPkHLMxa8Zg7CurhvmsvewJDNEVbvfXS4JJppHcKYKIm4hYmQzmhSsi5u2hDE%2F5CxHijq&X-Amz-Signature=f7b2afe11deb98e622adee0cb295f7be81a03e4875929d30a76b7a141446c550&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQYDF5MR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPpKAlU3q9k9w2oD%2FiUK9xtxoRiH1nxv52REmmv08EqwIgYrsvOqhn9jshHHMAAZv7k0aG8njsIV2OV7VYSB47DPsqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdrkIk%2FfCVD0lxeGSrcA2y19TlF6AMeH78ToT6iwrNYgvw%2F%2BhbPO6o3RsNHNxce2nuPpq6yHY9ePJkyfsey8h0j3bbYPzy0j9y5j93NyNbFazyDJLIjOCnRm7RVR4KV0Q1OT9sm9%2Ff4cA6rAqtwrE6mNevXinN522Wl1iSAvB4D%2FI0HkdwndmYtdLGxGh9QGESlJtxOIkSTBbN0D%2FYGStVvNak%2BDxP8Ghlv1JCJ1oX7XyVbRlMaOPZIeSEh5%2B1b19Oc2pNNV9ESi0r%2BXtvo0D51BRhvbqh80Gi4g9XOYB63OQsgKvh5o5umKhx5Ko2o89DwpeQdFVdXzpNprrjcbvtLEtMc9%2BOPy2%2FDlxGheepPBnYU3LEUzWSpWT%2Ba61rcKiZ7L9kI4H%2BKZSmOHAKSiCnGC4iH9wrRGQLUJ3EVGl%2FoLZJBJ%2Btl8mmsjrAa5fLTV%2FwtA%2FecG1G0JdqE9oKS69lr0%2BCpTeePGJYvdUC7LoHk4sIH5eiray57Pis%2FZN9HCF6O8nZZ1i1cdk%2FDl1S6GtpEXJ%2FYI1VdBs853bFMTvPtb752jjBtP5rnW7%2BvuNKOzIQQyI1ubg6PDhtOjXaaw1esKLGnU%2FbJSFDfe1VJv8qTWgywZMQ38%2BsqewKf5WFxpMxJ66fZzP%2Fc0c4jMKbb9LwGOqUB2Uj9EXRaI51orG5PkBlBEbpSCZRRxihj8UTI3BUxgGFP%2Bp5yWo54gkHfW5YnMBkRcAfj0ESkrgJ0Bv22sC%2FGLy71Y6RFuesCYvdpJelQmyUCCFi1IN6gv0xYQQuavqT0oWF2wikWbULjYvF5x%2BuzgpoJPkHLMxa8Zg7CurhvmsvewJDNEVbvfXS4JJppHcKYKIm4hYmQzmhSsi5u2hDE%2F5CxHijq&X-Amz-Signature=5513b4872a9730e949bbf9bdfa5d5781e16b42240b20edf995ee27b785acc9cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
