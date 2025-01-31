

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=9dd179429b85734a265ee1668e32b03d335bdc29463374c2a1f9d035805dcf78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=fd70dc4c08131db5440f54b022302f464cc5d621007b9e153e49c821becea0ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=561eb21b8e24f87a2714c7132ccb5eff4fe6464a49b1da7a5daa43f4762ff995&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=5de4f0a254ac7036816a6f9f1c325ec251ace94adcfe5dcd257d50cea363c316&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=01b4d0d5ab4fbe75c424732f085c680c25200ec6a369e0f87180646dd1d4cfd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=a0eaf633549d24adb132de704ea754d4ada93e75b1add311f41746bba7a3c51c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=ed4461f73b2f560e84b4e4d8e916b029c99ce091384e8485cb0e8b02ac5ad676&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDTD4QAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiuL8FitY8X7yGK1Y34QOpGo1noVFkCam5iWv%2BgaiJUAiAH2QsB3D1bA5r2%2F8f1UURe%2BJPd5WC3AYYxOH54EVG7iSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnwiutxSPA7bYQXcKtwDmmUm0Afkybqs1yIf5VxCzJ2A5T%2BpzDVT7kqvwrScaNCH4ljRozz6rm0VgM5OAzrx55EZQcoiqukFU9FE23YGiLzijsDG%2BfStp4UISeazRaDPlwkn2uJJTTWVi2KPszIikHTJr%2BJMZenqeoYybol7sB1dH2EAPuyjUHd1NGMLE8NHz7a2QK2FgJCIRPXfB4RFPgpKwe6q8uJo1XOl5RvAw7JC1%2FdtGEjYOpBXlAnyTp1ZMvsk9AxblFHZ1tz6KBFtiMshwKBXdW4fXtNC9T%2Ba13HNTiEJZT4QReNwiaffqM5ms0mtHKnza%2BZzAVXsPfl%2F14v50e8v1sgZLMd9ouvH1j8G3lQQTgcjSXskRau9QU18UDlwTItqE%2BCql98sqmysqWzQPOMnHpoozzZaCFXYtMTZ76CSyb8fI%2F6ANpye7Q3hl2bSAHxGN8YTjhUByn7Ocfi%2F3taYEYhrJnCM4A00vxcutXXJxSTDUXFJXb9y1sw2akvAfbeC%2BhIu9yDA%2BG7sIZVoXF4FwtiD7izyfbfWXl0WAVF2t9liwgxgQG%2BtW2B9SqbTAMvOHaB5YSm9y%2BTYG2kJC2MF98nGcY5sMuJrNc5zJHNR29plx1NHN34g70jmOTYAuJz0Z47gyaowmpT1vAY6pgGGDnwzv%2B7swCAnTaV1hNox%2BCMh2CRRhSvmbgYXI%2FfYe0ZHErGgh45Oh5lr4if2Q3qxtAfU7p4rkWP4kV90f6cubHyLj7gc%2B8ati%2FPLs2vHAi%2BJrk6tL6RrbxFCy3RwXddzsLeZezAuZSzJxCVCSoH0v7LEJLXCTY3%2FUnGu5b4FZRmZz9ggt4DfMzEra5SiVtLHUNsx3GvLKPycaFq2IO8f2wRN0RXo&X-Amz-Signature=0055a5fef82b2fd9a59dfdc0fd1bf01157e52e2eee940e3923cf5c2224a92421&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UWZ6GZE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd7G1iuYb2Fe04xCPdgtzo2w9AzLjaHG8dkTyaJk0qRAIhANmXmms%2BYKTAKhpNzy7n4VQJSQzSuur7icbO7IQoulOxKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4i%2F8XDOA2zYUj7DUq3AO%2BxokbCPt78C1XjVdN2dprS%2FHahpQjKhMGL38AQfZua3k4MViPhdUFZT0EZr31hKueAIlkBH4dUlZD63XEysrQLjPvsG%2B4aE27cWjyCa4zBLD%2BWTxxAVJKN0j3waINPNA3X0jAbGznyhOWI28VgeNC0bDhwJOlGqisYZwtmxuYcGTo8Ld%2Fu4yPffqF3h0rigjSAF%2FTsvRRL6VVlYM9kbRtzn87gAr5OUygAGhS4yMAzffdEhaquJgimslIHN0yLlzU%2BIukAANF5w6VL1NWTPM9G5W0CgrpM7%2B%2FvLadPrn%2Bpqb2zcqDMx4%2BThDxIN8svphxf8L4PwS1ZDBYe%2BHV%2BN5Hoiq3ys8vjiys8pv34Mb2Z6PJkUtfpUMx%2BebGhxnlzDR1tz91zdWdGkaVNdtuYJlSGgfZEkqTxREUySaEW%2FnnezTdcuqlucEh%2FHEa03oxRcGrEAPH%2FwBca6v0TKy5PIjcsQ8mQCFYvq7bDmz7ZMXQXFkHMw4gNRggoWtLZmfwmpMfczN5mS5xFmA2ZXvsEFy53Zqq5SWKfOOUFJZXv%2FrlMSrO4Ip5F1Melza7BaVxOx%2BczIbH2vp8dC0igzHx%2B6IM7FWB7ryIF8LQFjUj5CxjcM0V1qVbAGkaojjYIjCVlPW8BjqkAdek21xcn8o5blevVoHLYaz48FT7D1dh8haN6Gg7AjMBLfLZGIF4YiAhV6rb3iR4kMFvVQ4tl7BsAkbeBctxrIeAH%2FqlhPhxPNWM%2F8OAFvqs0BuyR6SBY0p8tI5Ls0qjy7Rjx%2BU0VUcNf6cDquV87PgYXisSJwv8JpGmkWbvwPyWPgS4TpAXjvh7jQma995yCR5kQZxpfrRNevCbKjxwkxw7Z5S1&X-Amz-Signature=1845e076920de5b4d4d6df56882e60e819a842d2f9e3e72df34cebda29641310&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4X353TB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEA2NH%2F%2Bk3DwzgSmyu6OBFyYp8rj%2Fx9da%2FXAVYF6GW9uAiEAqKr38ys5rns%2BxjvfUpdKZcnqkaLg%2BGlO6jhpNg%2ByWIgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNO3lSvkluGsUVTOISrcA5fmK1UkPXgRoaKcrDRt7buUJbsSrCf%2FgZA4D%2FZyiGG1I5hCdOpcke1zZ9mX0vDeryy6Y848jE%2F7htGa7UCq2pFe0SQI%2Bj455KbuXTAjP8mfluDzLBNRCGXmY4O1fdvMbHFbEEVtdIBfxPVvMRUhCF166Zif%2Bbb9EzHLHrsdvJLrfmvpU4mws5U7dEWZjjrq2QJqSydLXcTAGHMHN9f5sxah983wqt%2FZYlRm9Z5lOe9Tojx5qdQWbhwMTEtC0dMKTbtr%2FsVMzlL41y%2FI3lX12BRI9SavjQF8XX3blIc%2FEM97TAJ5EqjUejWD3TfV%2FdRZqZJ18Ch09H7%2FBu3s2Rm6w52IzB4qZFhxTRVbcZnSQsb0Xo1Hn8LC3VFI2JDNKJFH%2FlEMOL1A4TAg1c8tmWkTEptHLQ47owQwmCohlk2A%2FuiXzXbnfRSSbpibW%2BcpB8iwsEBYstZmboM01CD1sfINt5dekfaHD3%2BAv%2BCcnsfS8a54gnjXOLQ%2FXfungmDe2xn5wj%2Bx2mqaWTbjDEsZWerqNcemq6Qh1Gm84mCLGDZ2teBrIDCRRqdDIa3UjW%2BRhuleIVhwLBG3J36dguUjPv1cJlHQqRvsXNrE3gJTZx1gfM0l6xAovPauJ5WY3gzVMNST9bwGOqUBCbrLJflLmUokGbzNCp1ajGWCX%2FFn1szSboRjdL5hOW9nL5uDc4CKOotB7XA8ALm4Kk8f14ajS%2F3eUmS5HrlnoYKPVyK%2BCUGS8%2Bo0tmJAxTXrUmuGsxKPoxgljSOqyowyrvENSTEYqT4CEpDuGjLqlgXf8Kn3a2X%2B22fqNQ%2F%2FxbpAWK3xj8vqzoiASL1jLeDJ7K6YJDWqNv8jNc56hcy1O6BLoJD9&X-Amz-Signature=810c3eb16932baa03c25a54d8f0a423be3df4c9eef595aa52280d3068ff2e45a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYUMRPEE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA001qT1WUjh2AZT5la92Z9wY35LCw6QTQxDJ0CcmvJgAiEAktg2d%2BU4C1%2FgJaNLqf5K2hrtMF6%2B8PsUG8gqso9CXSUqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7mi%2Bex6iKAhaA33SrcAxFSnUC4gzvYod2Mi1C0bu3II2Bof6DqJOCvuzLp8jxdMgsWXDk02ZL33pEpiYhYYiZtcPDu8RmnBZD6GGM1T3IiDdP6%2BhR4rW0B91k7a22xlIyWzOYbUkDctjpEDxBYehqOyEy3WMKR6hSq0Y1wpkQr%2FPEbinffkjDbbx%2BE%2B2LwFPYip7H1R3hRhJYyUX4JmjkqHx1DvhukrVlMflHWwIhyrR0xWF%2BT7ZxzEXMES9iJgSb9CscgOaJ7zQoWZvRPUeZKUDDCTtlbyEdXgtN2rJCkEkxHD9a7dg6IjlYfMDXYT5PgCYgBFytyxdTpcC9SQouAaOuK5q2zxJ5fbQaS%2F5wnjIzf747XdD%2FjHPKU%2Fr%2FnVGGzkpP3o63u9HlktGvRmm8wkCe7VtsHt1Z2NEOB7oYMwszHawhm9ppHX6z1VNvPk7qHBtkHhYQIJvxgiVD5acOcMHLtirlvroMSON%2Bv2Jr4yZbZyl9qfuji5nO6I2L%2Bi5C5zVP890jfbKEWqQRNiquaDv%2B0OmzE16ukC3JD0%2BY%2BwxCCHM1HtiR4or3Tdp5fsXr28bc77hrMNJEDtT5jFouoTdKq1QJxYGlyXt2x%2Bx0EZIHqIMLjm4smOLyZBFE7dPokvydEEHUfYGx0MNuT9bwGOqUBINsElMmUf1GVRZBqm4lWjdYO%2FN87BQidFMCLyBrpXm%2Fh7pa2Hy2%2FEXTXlZyTz3HhJMJOOn8GqRoFGWT5hDlGX2ZbcCV5nYP0HxDAsn%2BE02JXMo9nH085neOl9FiCrbBctdZcf0PwLaU1fGoJVhVj90CxJyNHDN2FiA3ivH3AAMsEO4%2Bg%2BmrHdOylDBVss0iho%2BRwNPPIq3JZXoBXdTOqIzHTlBlN&X-Amz-Signature=2d9a54077efe5e3b7737ddf00df1de9fadfd7d3424dff493a7c239a847f50fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYUMRPEE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA001qT1WUjh2AZT5la92Z9wY35LCw6QTQxDJ0CcmvJgAiEAktg2d%2BU4C1%2FgJaNLqf5K2hrtMF6%2B8PsUG8gqso9CXSUqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7mi%2Bex6iKAhaA33SrcAxFSnUC4gzvYod2Mi1C0bu3II2Bof6DqJOCvuzLp8jxdMgsWXDk02ZL33pEpiYhYYiZtcPDu8RmnBZD6GGM1T3IiDdP6%2BhR4rW0B91k7a22xlIyWzOYbUkDctjpEDxBYehqOyEy3WMKR6hSq0Y1wpkQr%2FPEbinffkjDbbx%2BE%2B2LwFPYip7H1R3hRhJYyUX4JmjkqHx1DvhukrVlMflHWwIhyrR0xWF%2BT7ZxzEXMES9iJgSb9CscgOaJ7zQoWZvRPUeZKUDDCTtlbyEdXgtN2rJCkEkxHD9a7dg6IjlYfMDXYT5PgCYgBFytyxdTpcC9SQouAaOuK5q2zxJ5fbQaS%2F5wnjIzf747XdD%2FjHPKU%2Fr%2FnVGGzkpP3o63u9HlktGvRmm8wkCe7VtsHt1Z2NEOB7oYMwszHawhm9ppHX6z1VNvPk7qHBtkHhYQIJvxgiVD5acOcMHLtirlvroMSON%2Bv2Jr4yZbZyl9qfuji5nO6I2L%2Bi5C5zVP890jfbKEWqQRNiquaDv%2B0OmzE16ukC3JD0%2BY%2BwxCCHM1HtiR4or3Tdp5fsXr28bc77hrMNJEDtT5jFouoTdKq1QJxYGlyXt2x%2Bx0EZIHqIMLjm4smOLyZBFE7dPokvydEEHUfYGx0MNuT9bwGOqUBINsElMmUf1GVRZBqm4lWjdYO%2FN87BQidFMCLyBrpXm%2Fh7pa2Hy2%2FEXTXlZyTz3HhJMJOOn8GqRoFGWT5hDlGX2ZbcCV5nYP0HxDAsn%2BE02JXMo9nH085neOl9FiCrbBctdZcf0PwLaU1fGoJVhVj90CxJyNHDN2FiA3ivH3AAMsEO4%2Bg%2BmrHdOylDBVss0iho%2BRwNPPIq3JZXoBXdTOqIzHTlBlN&X-Amz-Signature=79aeeef48be41b102b07ca1ac3af6b21142afc56b2bbe7d81a6a27bf2a0e4c8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
