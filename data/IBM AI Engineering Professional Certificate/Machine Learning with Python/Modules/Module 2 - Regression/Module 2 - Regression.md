

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=072d0565a7a05b2e9be6a9dd346d0bce5c0393ae733d181359fcb2901e96ba25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=233ee4190f842c716297736e49688a9f25d5ae18f3cba5bc023f0f6afca5753f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=dab483b646175236e295f016b0d7c011f16c27dad69c8c3cbcc40ae5fd4bacc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=5d9e0e5324542187a7d7c0ef2921e9da62bf45bae5e0fb5864b7a384861f4f8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=be188df9b4b0f240f3cb0e04e4f3efaf0221777948e105d512ef9afdf248a7e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=9179e63682c81c639903dfb27a258e899463bd3a80d8cabba78d8f68b5646532&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=7b094e51b7d5b87473790909f8d33201991e34a4f2165262a4ea5caf34e2df1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIXBFR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExLl0awrsnY0DdU60UxER48aQV4wtc5XlNRaSTsZPaXAiA1e8K2Qlsu4O4EczW1Kf9g24jR1KHAZjd9991k6y3ebyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuEHYr734u5gooBQMKtwDz%2FbyVUtZD5IrZRYsQqeDm5R2hmnmOOKR8IZbPpCPPIBuUhkTz3YSgkzOGro%2FA69gA02ieIb5oDWKLzqPD45RyRcq7PEqmDJ%2FGytgttNqmSDpQwHHYOb2XzBzqjKcx9kRc92MRkz0GL1cqvJtfzd9z4wyTb78xXiEOP3qN4ecDAGzBffXxMf4ywMg3G4MziOS%2FRGSiWXtuvku5v%2FRYVqOJhQ4LOwuz%2FQ9dXshTDFr3kvutqsjzq5LaUZl%2BtE99gSCEIqhMx5Wb9P42FpbeY%2BEtyU7CDLAjAtbX3CU2aobcAzoRbKXvcTX%2FLwEKDts6KaH6QxmnXvu3prNCWxh2pu9EEEWSPWza%2FpVnJIKxy1CeSD09PWakUB3EPpb%2BmnJMmD2pTeyQpuqQ8toRPq5S1E8CIBm6nf5%2FWNEhCVaF8EqNfKm76LwgiJ4Hs4n%2BTYT5ORn1uKA5%2BdZ8%2FN0PeVO14NH41wwQPfM%2F6QkK7CMW5uIsIcVzyJvJI%2FbhLs2EMu0AlDDZuh%2B87p6qg%2Bijxuxv7UUHNAzzbzZvYil%2BSj%2FhyTC2TG4sOoNw582RD15kx9pi83oIXPPlVJUrOeZE7tnka4yH74P92iCWFjP%2BrmWsGybozvdA%2BQMEQTiyb7f6PYw3Lv9vAY6pgFpxk5uEum7TzTCgy6thxGcFgkC8jOFbYYfz%2F7VYl1Z4RWaw3lyZLgbgpu%2FQUjMu1bcBZK%2F8PAfn%2B%2FhWTzeRQ7pL%2BlVAGUrzXC2JreE%2BFZv96BaxFy33K50wpuUSxaVpRIqqOF5pqmJ5ZNQb1c3yob%2BgJrLj3cvHPnpnOCtrUqKP9aIfE2TFUUwUa68I2luCErbJtEgW%2FdLyZ5H%2BXlNAKJ%2Fb8kSkZav&X-Amz-Signature=90d042c50ca1eb975f3eb383b3bbcbd232ebd0758dc5d64c7ca1181146d58bc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXCZGHVR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDdojirJtqxEGkdMcUXNTXjb3EJMP%2FEtv1QZEKA%2BLAhgIgR9h%2FMYD2Bl5xpi5vc%2FEjGSItn8zg85J8xZhNRsd8dQgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKPUEDKVJMTTv6MeyrcA16BS4Am3RQBqNQr%2Fbeus0oLsm9sZrcTXBaVeF2YpVovKcNvR4HhDs01xoGmTvxTw7qbUho%2BGK3iJIHAjJyvkMRkIsVTbqodoQA40i%2B8UOVoXFzEPTlZNrdAL01q62wttsjQ7KxmFMb5ySNiafxrgJwB7k9dpP86X0YkzC%2BYodhPebC7Jflohpgi5HQqXk09EsZhtP%2B6e%2BZhgqVD0Ooe8h4h5V8%2BrqIdSHHN6HUO2vmFapybuY%2BEfILZ0%2BHwWiw%2BLugzfeQJo8lDUiL8Tjt66%2B4mympiLRIQnW7gFgSK4WPz8ykUL%2FuohpXuD2jJFWHPZbtKsQGrdYZAgNSI%2F%2FA6ruJgblcIQpOzblJsAc%2Bu2q1Gu7i%2BVXJESWcQ8kI5B%2FOA0dExE%2B4K3dID3uHst5ErE4yj3hCRO4vJSkpFW8G6ORtpfHgXeqGxJggYQH9kQtW0uklv3lmMRw3Xg2a%2BnIDY%2BivDowZMK5PbO186gHEni3x9QXOxC5uIryqV%2FkPgzhHxr2aKvKVOUX0EC4pmIetQSws57RTtx0o5EsfGnl0V4uF2HZHKfQkOWzJ%2FWQvOsruBSZc%2FhZDo16TXF0Fc0Au10v6mb8PtAk2YF2XmFQYT1dqcG73iZ45GD3rWtWQTMMS2%2FbwGOqUBpRLiQec0sMpV9fHE8AFY6mWmXc7Es3cCwCUgQ01CZ3sV2MHSvKRQvfqiPWzV9W4600hsxjI5ugLn0ybgYaNArjXC%2BXEt3PSJ1Nj6mc%2FIrjBvKv4kfb0j7alTZ6VXs9ee4Q0eaN5RgwPFBWlkJL%2B7K%2BrKajBsYWRf9yO%2BCZfhjmy3cz47koe2%2Bwzax%2FhHfI40YyPLNALjmiXdjpy0%2BZHdZkAvznmx&X-Amz-Signature=57559c8a4718837c0cd589b944e8e597e9b0013dc388c0390a5f34ddd4c1bd28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QOGUVAF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFc3q2sbtSt6%2BCEK8SwK5%2BCBaBhzne9QYrjwDGNk3Rl5AiEAy7YdG02HRMUTZPzPob4ycqhMvSmbkycikwvsVYI9MDMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBQB5kvOvVoTmh42dyrcA6ZZKJcdRhfJOAHLLidqHOtVLrg8BSU16PztTCyNVc%2FVDS%2FhLH%2FpChvc4U86JlnqF08YSmo%2BFOeUYM8iT3qP8mxdR0Gxii03W2mGYEqRPb44BQn7qFL5AGk9w0sgrA5Jk%2BI7dBzgMrD0vLz3IELPEPfn4Z2FC62GSdeVCYVp%2BdalLRqW2QsmGTKjUpIp4nI%2Bj34o0Kc794SeBCOGXZpMAPbaXLIPC99T8Ms2%2BA7f5S80wVkakmBMztGAVct4749fjUsdtJqqiMCQiWLWHpxiXgV%2BfWIsHfBzUeIuvTbUzgPoLE3izaRtUDCVOE5jju0WmUOk72a5Jvs%2FUk8eNAgEgrBRfbSjBRCFpYhGo9qIlhf%2FXJ%2FL6tqvUoqq2YixJjURm9V259j2fMAvLrH%2BgccHd5ztYz1cVkv5YXJXqjrh%2BrAzpPdsP8xCxaY9DmKXLrZ8Fnj5KxRd6E%2FUNgqEbYjv2%2Bf%2FtjjSY7JbqZ66YrUxKK2ll3KliMv%2F6x33D1qsnYWpMIEGq%2Bk6d4f%2F7e4YZ%2BFxdKbIqlbPODdzqxc0zF1msP30ECvJQel6QWE9BaU8FT74HSxvQ8i%2B57gWxR4%2Bzhzv3KBrOwAZTEvp33FvXr%2FC5poyNnE%2BF%2B2h8VXDPqoZMLu5%2FbwGOqUBSyHJgB3ddn1Tzx9xKx9k7FYMvSPAoa4iHpOUF2YzhTqcRC%2FIikcJQX4fIR%2BzL5sDgHDij8Q72dLuF09XXNkKDhdYMnaFQqqWyMG%2F5uGM0AsELFCRtymo0sbYa4Mt%2FjT7VEIjk4qNwK83LgnBlzleYCWMdfMSzb8z2KjOKXtb%2FBpOmjObnBZ9DYQ7r09Cl8jmigMRtU8n4kTXMm12B8uV4EZfV2Bw&X-Amz-Signature=426f4fe45c0d2bb368a53ea8143068a3d652b43f225e0f2b530306e9c5e498ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H22LICS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeyA25%2FYrrn27UtfpNLNTQq0N02QxQlEIihn4o8w%2BITQIgY6LHUNFR4IwMwkOtdSBRsdnedkaHLZR%2FnpS2rYg7CagqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5trRFPn%2BPD99Da5CrcA%2F%2Fd4DE%2BbBRrle7qyrpHTLpbQLxVBushAM2IVzTXu8iR4hnVjKwFuNxxOwPipn%2FBr%2FL3jbAUFfn2Ke%2FVlDtT22z1M3DabPCIiFIrEdiCBQY6YF%2F5bDuXNl%2FLikzcCot22nJmcOu5qHLM%2F1QIaZVCLhrcI4u6MrM99udWCz7GgVWWhbSiHIkCYOoqTscXorBGKxc8Qf%2Bp9DznyxEMKCwt%2BnTpEezT3ZWwPd9%2Bimi6F3zbgvCpA98T1JldU2N5R%2B5282ppsCwNQCMOpBdqBINJJZPvri6oyx483g5CQ8nPLj7zaRNtE7cBidtWWZ5IObQOMylB1rQVVM2Kp1Wh4gICHhc2JCTXnuApQRchkq5fZ3VQHzXMh%2FcX%2BXBu3Wybfok%2BkB2D%2BuYtMrjZbZ2Of7SjJr6yHcEMLHxm3ZAXCnJ7l9FdY%2BebZZqPOQPDWW70%2BqpvCT3lyY5lcDc%2FafPo3g6NgokEkyL%2B7UKSQv5W9sXHcZ3xYy6RbKPYcDtbsEWqMfW7hzJ2muXMbprHrDL2FpdztFMm35LMNzPK7Qy%2FLeSPYENWp8EXQqXO%2Bs4CQS3hPqMFFj1iACwBdsi7bHkp8TrpaLXCeS79SEwexIOCYg5SOCuoabCw5126CfT3RBmyMOO4%2FbwGOqUBbFqP%2FwF3QMZ6aBqpNlMcdbTRKWZw6t4k3ek2%2BAwOAkrzu8eV1tfHmoMvFnbCMw28xN2BP%2Bk75pclPeAxQD0pcWHqdwh3pfxmK9xjQQhqHiApDrj5E732ZqLiFQzxmBl4LyinAvSFs0wSwrO6ln%2B5Yt8R6p8sHBM%2B0QrS3s7VDRd%2B2VQiBCTCFs3nINHBf5Acpekxzl%2BEwJBJLadxImqBoK%2FhBp0N&X-Amz-Signature=4994f554b1cb97568e77d9fcc3892641d66707df7516c447c6e4c0fabf871d6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H22LICS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeyA25%2FYrrn27UtfpNLNTQq0N02QxQlEIihn4o8w%2BITQIgY6LHUNFR4IwMwkOtdSBRsdnedkaHLZR%2FnpS2rYg7CagqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5trRFPn%2BPD99Da5CrcA%2F%2Fd4DE%2BbBRrle7qyrpHTLpbQLxVBushAM2IVzTXu8iR4hnVjKwFuNxxOwPipn%2FBr%2FL3jbAUFfn2Ke%2FVlDtT22z1M3DabPCIiFIrEdiCBQY6YF%2F5bDuXNl%2FLikzcCot22nJmcOu5qHLM%2F1QIaZVCLhrcI4u6MrM99udWCz7GgVWWhbSiHIkCYOoqTscXorBGKxc8Qf%2Bp9DznyxEMKCwt%2BnTpEezT3ZWwPd9%2Bimi6F3zbgvCpA98T1JldU2N5R%2B5282ppsCwNQCMOpBdqBINJJZPvri6oyx483g5CQ8nPLj7zaRNtE7cBidtWWZ5IObQOMylB1rQVVM2Kp1Wh4gICHhc2JCTXnuApQRchkq5fZ3VQHzXMh%2FcX%2BXBu3Wybfok%2BkB2D%2BuYtMrjZbZ2Of7SjJr6yHcEMLHxm3ZAXCnJ7l9FdY%2BebZZqPOQPDWW70%2BqpvCT3lyY5lcDc%2FafPo3g6NgokEkyL%2B7UKSQv5W9sXHcZ3xYy6RbKPYcDtbsEWqMfW7hzJ2muXMbprHrDL2FpdztFMm35LMNzPK7Qy%2FLeSPYENWp8EXQqXO%2Bs4CQS3hPqMFFj1iACwBdsi7bHkp8TrpaLXCeS79SEwexIOCYg5SOCuoabCw5126CfT3RBmyMOO4%2FbwGOqUBbFqP%2FwF3QMZ6aBqpNlMcdbTRKWZw6t4k3ek2%2BAwOAkrzu8eV1tfHmoMvFnbCMw28xN2BP%2Bk75pclPeAxQD0pcWHqdwh3pfxmK9xjQQhqHiApDrj5E732ZqLiFQzxmBl4LyinAvSFs0wSwrO6ln%2B5Yt8R6p8sHBM%2B0QrS3s7VDRd%2B2VQiBCTCFs3nINHBf5Acpekxzl%2BEwJBJLadxImqBoK%2FhBp0N&X-Amz-Signature=d2d07bde8dbd6848fa2fbfae198d75ea72d9572d409b2ce99f84b159594efce8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
