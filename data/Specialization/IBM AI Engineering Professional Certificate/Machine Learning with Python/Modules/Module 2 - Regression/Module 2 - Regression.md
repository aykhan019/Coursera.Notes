

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=6c114c47ce1e066964b5de0e2c097c4d5e2bec925c207e810f82daebdabc2938&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=b44431a9d7a0953c3abc715a35cea47cf8425f5d1e16c91806fcfd8701975f75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=498e6f2438c89f0298e4676ec9e702f0b2a8b6159f0dcfed2514fc75c93c37a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=294fbcbfce6e4de8498eac2291de0aae1ee37b834752267af87873194227a6ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=48a1ac56b99c95f2e191a16ef023b131d621f46915f9f0cef7b17e5009b12ebc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=2e0d485178c6ea383dd6e2c4ffe3506ca68e0313cb18df2b71398598845bcd75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=8a3f50a7692d0308b99cfd5ba08597f7b3f104ad4443885a7e892a798b6789fc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOEW6EDA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnVXvNaMoy60C48g3AD5sBvf4PZ5Lt1PiwhLIFjKrgQIhAOMmQVzC3CYw17iqjjrL%2F287a0CIbv5F27AObx0BDpv3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWE8DLGIPqmf3fUhcq3ANEJlXg%2FYbu%2Bo57Y9sfmGPUG8TOBkjRO%2Bfnj%2Fecpi2lspQ1qbFNNygh7CmdgrT33GHdP5BXinAlhre3c0guhGdvNaBZn%2FO2IKu1TtG5Vf0tC%2Fp%2F%2BgC0iA4kvRDQLQasZ4k4k%2FmzdfzdFrjriXOnoD%2FcWeF3I15SaA5Q6D%2FeIBIUMtWq1gB6KgqIGNQ33eipVIGUrgawNE422EyW1pwnh9ZdkAMCei%2BnZYbgJ1gdXntBYjLtjXLh1U6efbN%2Fvg8V7d%2FqBepACRdHkKVSbEnCOpQYDl1MD%2FfB2rSs%2F1CeTkbScqxEtTq%2BYke8r07pI7ziuiOXk7uFTYwmWwithXqqmEgHo1Ya8gnnJl00A2zxOdvr2DPdE41DHgPNhgkV3SluXHJMk%2FG2is%2Bp0alxbHAuj4e%2BrB30yAyn4Ux4v7g675Mu9PWRiSflKkJjOARm1sR6mixiKCVTMiPQJ9pe2HYATBuOSSFmAcW2Mr0AY4GeqeOPk8aYiEKGEK0ywhw8M0U57EGXknn%2F%2BEloc0a3ZXU%2BqzL0oDMY8LHw9uobjxt1rZhndyLs676twv8BWil7lUf1TCy62huwZMYN5Jmr2bv5KP78Y6IaZvnSMk%2BuDeLB5XJFv284LZ6EkJmiMh9LYjCSxe%2B8BjqkARFdqEwYQtHwGWC2KacQcNRfkIqlBOfdq5RWmxLGKqaAGHuqmUcw8oTWuEqYWCB4AgCJj6SYSKXG49pHRO%2FO3ud%2BtSEpR1Uadrm%2FFXGqtMKoHRX2Xsxe0q7exv%2FLHfO%2Byds0%2FKzcvRPxmY1qOtswcOnKPGvf4cbDBeU7KA4qTXEZNBmscSw4NNKEqXwUsQqCBXgnJHnVuBf6Z40zt1%2BZTPBrdvhI&X-Amz-Signature=9500daffe1f4572cadabed348da4e37c3f6b60f5e8d8fc8f4033cbc6b65a9c03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXS5SCZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3BrZu4A2PSH%2FfzaUhhTmuM%2FPhcI6TxZsjRKUOAesciAiEA7%2BKrgfwp2fuqGImgDLcWfKhai0h2J7qjHwqfiJ74K%2BwqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJq%2BvPahQfgwR9QnnyrcA%2FUucOpUSx7k3uU%2FzVoDFEOIUwuGMOSXmQmCek4ZR9Gzq8pktK%2Ffzhpak3SGbBIYugXQWHMtnBZJ6r2Inr1Tf%2FIHqcrrYoxwrF8rNrSNQl6AdH%2BcUOh1RP6ds%2BPeRsurT8S8RxJGLgx5ToMK25y6V0%2FXBGVtph9JrbGxAdEXT7hBrWwAMaFlSGnEc7V9mBPHWQFH%2FEtAo3nu5H%2FGzv0O7O3DEy%2BW4RRw4tkfZ7%2B0X9CdpvOXM9L01MMBkUOpS6KpzB3F%2BgUlswSDtic2OO5HLsQ75fBB5YGgxZiA7gDNoWjHp5e2hQ%2FUnlE%2BHRzgsY4TW2y1eJIEHN2HbcRM9IwPsOCOQamr0SkG5xtcEW6MH%2FRi52aY7V3aXP2ndT1vAg9PZeOiFnFPTnjGsJlk%2Fr6%2FTj%2BtpFaBo%2Fuma2gJh%2Bd5rahWCYEZ5Nr69ROfEP7nzP4%2FKRDC7dHB6ERrA8tTl3p4gjqQdfjAVYQpQ3v4DuzPAKxY8zd9dkTXQW89AlAliN4d%2FHSXy%2BmUL2pPAO4wJsrBqhQRzH4fdbaST%2Fi41JHAQKi2q176CTABcXdOMxgQqy9zhdVIr8KqQLoRNI2JqU%2BhWx0v%2Buo%2FIqlAQFKbC%2Bg%2Fq2XwTc%2F7wkpwNGtsXiCVMKfF77wGOqUBfJ5RxV8Mh1fGF6GSyAOcBQYtrVxosCG7XEEL1w8FnE6LI1m%2F7A6smmPDY%2BljCRdd%2F75vnEhcGs5RFDGW4g0mn8ZAkrsX8NFBWJUqkRA34oOlmqIi2JAMfhzQrD0coEPUv6Bg3HnIXA4ROzA3tImENmt8EB1wM8WQogrnS9bH%2B0mwbj%2F1Oy4%2BDKRapce7oXHz9%2FHkai1U%2B4jDpQBiKbunTyyfSwWp&X-Amz-Signature=4b996427978a429eac8dd35bafe73a6483869e1cdebb2b565c6e48b2efbd1d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJORWYKI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbsvZej%2B%2FMB4A5oxKljZP9mgTu5G431S8K9jTLySl4qAiEAqt0OGEkLQznBnPFgcaU9TG2whDqTP2tCov7xYdl%2Fz%2B0qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL10vtWuTbmsYfTh0CrcA9EiR6XyERESQQZ91V6iZBUm9OfZk0%2Bz6sSYlRgNHhtVtsswnPFC8X0G%2BUpSvn%2B9%2BcPYTUfW1bCWGMJhA9EC9ZbAZNmixSRLraUqVpGCxjeYJATuhtz%2BsNjpVAR2qBg9PcGn0wwczCAeTaGXRvpavh8nZflgGk%2FQuOSLeSyQm0JznXhIXAZ6mE1B%2B%2BkHYubU1RocD2JN%2FZAepVXJts%2BFJ2Y%2Br96Pw2me1r9rAFZvcVfYS5W8tDYTrOZEJOj5AB3cUmDd3eqftANBc%2BjbEgh1vzYQrdQD0jixZRghYfIXGoJ%2BE4flg%2BN%2FAaekjj0h4%2Fl2Mte9TyEnvBNz2AnAHydkoBCL%2BCP9FDkYWPJkCK9FySp5aIr4JKS1sonoX5c4ksi7syRFVPXtHQxeUz4fLshDSTe0XKQf5eg6nvsao3IuZWCoA9%2FKl48JGRNiX0eCQs5N2gJCCJwS8pdXSMurkFR2yAcOcz1MtpuTtbof9ukUyvf2Xms6kLVasXLoysSfS4S4TJaNvWt2ewd0ZgM1zgxRKdsSBS%2ButiteeMMXrka7%2BIH2PlsIrJwpM2Wur6xJk7A2RaAPRhcapE3ed4FbD8M%2FUP0Zj3%2FCJwPBI9vJO73rS%2FUBM%2FyAk6XZ1cZi6GEeMJ%2FF77wGOqUBY2a8PJ3hjHw7pukXCUnm%2FgCgl1h7BfAfkHhqUxayxNTuao9521JRN6ScXG%2F0ipQOFPV%2FCLv2mSxU0%2FRU6mZrMpbjFIQGeKR62LyELFyH8rM6GAsfGqLrEGfm7BdWeYCg5DFG6kncwdYAEuf3q%2F4NZ0ssx0bkmLrK0DrnkDVyV4kedmk2Uz%2BPcN8v%2FreCWykLE%2FtDT2wlaLYHMqzcT93xe9qBsySE&X-Amz-Signature=dc445fc21cc6bdb824f1c04482f644952c8740840b5c9dd44df4a37458a4ebba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7T52EK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF7FfT%2BkSdaF96fUi2KGyUXim6jjLrNHyxHJ5OFLWSznAiEA3TJfzQlp6PzwoIGv%2BBx6RPAvBlsaNjjFknaHSrZmKr0qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMot828qFW6bSaZdgSrcA%2FZkUEmryWYCsNqZRdo48dNCF3W6e0%2Bd2wWNz9W2b%2F5T3OB0ETLYr7esA6Yy6%2FyZRyxatcXPBPNe8lNwiu7%2FRHF9X%2F1JtWMHMGn9mtJ5QhyO83UYRDvXR8%2B%2FmFa21e1gFIVYrOr4i%2Fo8eYfm5ldj%2Ft179I1sSt90%2F%2BwyRj7PB%2FbuK%2Bzq0xaIM6n29gcjG4Evvz%2BepbvymrL0k7zTc6%2FuRONmJXeGSCN%2FeU%2FRCTIfNzv3KDO21WA8Wjx38PjeVnGph%2FZGCJySZWuEXsnS1j%2FIarYKRkMHik2Qci%2B%2FOBP4jeeVmUYZRIBRRtRFc5KtbezpSK6sPw2DY0V4%2F%2FIsRDZv%2BT9LJUVlaPrI%2BX8mS8g42X6%2Ff2OhDMwqpOF6g0qJNIWd3KRRK%2Fkg40Nd5ZcKc5OBV%2FOdnL1tPkdwqBDutt%2FwlAnwjsjueufvLCP6duvPz4dqFRJazCjhAijJu5vA6WLQtmYq6BeaR7qCj7ZkZFJjktW1bgZzVU5LjiLc6%2F5BzvqyxQZRubdWHnbU%2BVrhJMnHDSBU9xttKhPy5tk2m%2B3e9Ve3gv4aYSUcYcO3Fmc6Uu0JUSLN2quGNaCujRSssqBsukhEQV9ww3upRccfG%2B3ZU87Db4VbWuNR4s5n%2FuY9MNzF77wGOqUBsgDr7z27apEcJxJtGkJl6n6V8Hc2XMeJT8EXHkvRdq6mcBmIJKYOjJKPDXAXiVUwvTHWfLrHndkZGThNlF9UejdTzJjTob1r9otdfiI%2BVxRJtOnhxlW4rVAgw3tzm8vf3EqEZnRzoUxCtcZ2mrJC161n4c34UGDIYiar0mNWPrTtKVViPOuJb44xmP17ERCpRvdX75%2FQr5nO3WAoc8o6MWowXbDj&X-Amz-Signature=408919ffe28d49ba12c25e61d6ac3b0ec1151bc721602f15c60a47a68376e5c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7T52EK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF7FfT%2BkSdaF96fUi2KGyUXim6jjLrNHyxHJ5OFLWSznAiEA3TJfzQlp6PzwoIGv%2BBx6RPAvBlsaNjjFknaHSrZmKr0qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMot828qFW6bSaZdgSrcA%2FZkUEmryWYCsNqZRdo48dNCF3W6e0%2Bd2wWNz9W2b%2F5T3OB0ETLYr7esA6Yy6%2FyZRyxatcXPBPNe8lNwiu7%2FRHF9X%2F1JtWMHMGn9mtJ5QhyO83UYRDvXR8%2B%2FmFa21e1gFIVYrOr4i%2Fo8eYfm5ldj%2Ft179I1sSt90%2F%2BwyRj7PB%2FbuK%2Bzq0xaIM6n29gcjG4Evvz%2BepbvymrL0k7zTc6%2FuRONmJXeGSCN%2FeU%2FRCTIfNzv3KDO21WA8Wjx38PjeVnGph%2FZGCJySZWuEXsnS1j%2FIarYKRkMHik2Qci%2B%2FOBP4jeeVmUYZRIBRRtRFc5KtbezpSK6sPw2DY0V4%2F%2FIsRDZv%2BT9LJUVlaPrI%2BX8mS8g42X6%2Ff2OhDMwqpOF6g0qJNIWd3KRRK%2Fkg40Nd5ZcKc5OBV%2FOdnL1tPkdwqBDutt%2FwlAnwjsjueufvLCP6duvPz4dqFRJazCjhAijJu5vA6WLQtmYq6BeaR7qCj7ZkZFJjktW1bgZzVU5LjiLc6%2F5BzvqyxQZRubdWHnbU%2BVrhJMnHDSBU9xttKhPy5tk2m%2B3e9Ve3gv4aYSUcYcO3Fmc6Uu0JUSLN2quGNaCujRSssqBsukhEQV9ww3upRccfG%2B3ZU87Db4VbWuNR4s5n%2FuY9MNzF77wGOqUBsgDr7z27apEcJxJtGkJl6n6V8Hc2XMeJT8EXHkvRdq6mcBmIJKYOjJKPDXAXiVUwvTHWfLrHndkZGThNlF9UejdTzJjTob1r9otdfiI%2BVxRJtOnhxlW4rVAgw3tzm8vf3EqEZnRzoUxCtcZ2mrJC161n4c34UGDIYiar0mNWPrTtKVViPOuJb44xmP17ERCpRvdX75%2FQr5nO3WAoc8o6MWowXbDj&X-Amz-Signature=3917b557df8ce0b718bb301888f98134e875d63b7f9fe52e99865f699d8790ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
