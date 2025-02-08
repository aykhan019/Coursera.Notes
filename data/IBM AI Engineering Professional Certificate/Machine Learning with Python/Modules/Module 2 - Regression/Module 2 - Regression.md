

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=d5e2d8ae5b1e88fc83266504408ab2f10f9d549e1e086bbaa448da2895be3332&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=474fc1fb8c260ef5209d886af7c6e1307b2b9028c8c14549fbb035cf81d0be19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=0616f19483f4a524abbd2e5c7eba6dc23b6783b2366e37ab23b75c3ef693a2bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=bbce58cade066c19c5541ccbe63f7782ce972cc7245445efa1edb636b82bc13b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=6961a384a60b9997b7244c1a92a6be4018242501e30d8f7f60107e34e62d08e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=b0b5ba44014acf4989c45bb06510e1c03298a682c665df20879c829c048f8657&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=34da325528be70a101ee7122c80f12851c4741db83b1ee18dd353b04c0aafd6b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663CEVWM5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDmL04JzqWu2AYsTQ%2F5oWlvfIuf8Hi%2BwlQKtlwWTGYYQgIhAL%2Baye%2BGOb6aw%2F4I5t7Sf%2BS3%2BFkeF8mAH8c7uBDDYFyqKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmv5zO9DHGrVGZUQYq3APEI639gtQ6FjTqSlxLSibLuf5W3khhfLJz3WCOeL%2FTVKovuGXbSYP4%2Fdg00OPNjoGmD3GFqLZiqa5tkTIx4w319ITlmCiIWcYmEIZE8sYM4YtnYm7Y%2BJjak2FTL8QihacMA%2BmF5dPhKMscBpRR4wTFKBoVXEkSGZJNJ1MfVI%2F2OWKgh%2BcZcCREheM5T9hOq8ufaEbKSunFm7jkhAXKOaH5yAoTSQWSlQBslauAGX9qOskLXbG7yCd%2BaIEdYST9BJq%2Biyh3w6Ji1mPJPyc641se8hZFOS5KxdzEUlxli7633819ZfTV0cO7%2FL%2BbK5XbC2pbZa9fx8UiGABZucasWD63F7u1yDUy81o2I%2BL0%2FMyVOOe0PFW0JJERKQSh4Qy44X5Qx8NDYAYMO%2Fn81REt3V2yhTV47tRiYxDST%2BgJ6gjKvP3F04w9aD7ULVPLe8PEWIdA3qUAPRexkF6jwjmngl9u0W0%2Bgnnl4yxzkqk5J0Bv74qMyzMb053YVbLcV4njCpdoSF77pqGxG49dp7hKKEAFfJEu1YTYPfdCrKvGaavA%2B%2FviwGS%2Bat7WswVAiIC5myoGIPGGBWe%2FWpMqwJDOhKEk7YHQqlZtloVjO8D5NryITnWbNANu1XySMasRPDDG75u9BjqkAYtg77YtM5FAOtArKmGpIPBvKLzCvQwo5aE6UzRofzfYfugtaP%2BDL3tPOuBXf%2FP%2BXXsocDaDCgMvhTXxYMcuHaxsobTz%2FQCDjEQmhcE%2BAuhgGJhdKdLR3vFQpzaDwDVkDlggb%2FoTBVylm6NOu28hif5RGda2r8oyRQE3oH3lQXwudFIF8gqkKFxZ7zg4ywUPfBrFthhLndIFffReiplEOWvbV8HF&X-Amz-Signature=5136156f66290b52fa1b6748061380e1f1a00f242f3207411f259918ee93580e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GNDYIXG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIDxmj70MnSpar2r8ZWT7owLr4kl0%2BpI9EG67myyZsXfLAiBwC0hVthxh2txq2yl8pO%2FaSfx3IzFToVEM6XrnLPGWEyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM32pNCTZS7OI%2BhbYLKtwDrnLQFuYU8sebUbuQg1%2BRIA0Vhm08APB7kBUGCYoGI90J2agXvSX8g%2FSBpF6Vld8rpjBKdg%2Fk96xGjnpZ%2FFfnUfiHvBfc56LrmGIPdhc%2FKD14GrkwaM9cZG9ejzzvySKxhmWEhRlKAk39CPqYeVzVaWhnCK5IKCwgB87EmKq4TNLiNDb7ct7PS7a8WqpUag5kUy7uk%2BkwtT3ttul82uitGVHMbq1FlK84UqGRdPQAGfpgeq5EqRa9GSXXeGQUYNXgxKLEKovZ%2BNWoQNWr0mz%2B%2Bc%2FkBvzqHl3dHoydUa8uY5qhljb4kfP%2BN7ACOY6dLeCxC%2F8I63rMpMXrr9GYzD1qWr%2F7datUT4X3N01WgeGi%2BQpmEwTzrqA8tQMBgjqEGKL0%2FRa1evwjDhWy%2FBq06Bivn6gG3WV0yiE3dRWGS2H75a2cAXXqn6JEYF3Ii6RnVlWVHZgrEbWd5CfGUJrps7sSHa3Y%2BUQUqjMuzhzWzTT5Xq93i62bdJKy%2F%2FZEyJ%2BpJG8DHeZPXOE%2FlshaC7Mb0DjFCxt5D4fzPCyeaVkaH03oxdmyUVBCjVXJ%2FH1NB2mxfckqfyrd1tI13nz8Jh0MhJ1ER3Jo83FfGqozdUZ2d%2BeBARDTH6jYonejQPat7oIw2O%2BbvQY6pgFwznjuuAg%2FIyq7U1YKW2Tgstj%2FIXC2bZ6%2BvrxieZ727NJv6ytboH1hEgLiwty8Lt%2Brw5cnKO9%2F4AaJFLt%2FfonYAizZwYkZ6j%2B5U%2FY3%2FvZabN7AOczfvhPorOt2COiXVeb8SLvgDXnfrYvm255EHzooFuQeh4Xjm%2B6sPhKaPuxMu7SAJBX7vbHMnIGHux9IP2Gy1V0nI0Y62bcXmKSK4nizj0%2FVgcei&X-Amz-Signature=2a03d538ecab74e2238ba886be2fa440a9aa0a4f6ec05232718b4ba2d593392a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q65P44F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICm7d7zInC656cErb2RXWwckSDfE4sVZifinPpH%2FiOqhAiB0br0JsKXZneB99ep9rAt%2FD3m1cYuevleix9aB2oLWyyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvM8wwXP8ymeOBr3CKtwDxjQy5WlnUh%2BNG2kh7j8lRimLhwDiWsxOfSKr9VyZ%2FF2HwOKD8NgUyXytvXjIwoE2TgqSmCG8z7Hj8%2FutFJj8dX6ysTi0%2FFFKDwXi7AOezl3KtnvLHvy%2F3A0TIn23rgfYRThU76Ms7N%2FTb1YigRACytWxdDnnvrebsZgLrxm%2Bclfqs%2F59V%2FovV9wB0a9nwzKVdXqS7sbsJKrEXtEKgMfV%2BmT7SeOoL5UzO1fQyrDWM%2BzHcZUfrKL0H8MgqBLTe%2BbDltCgsDgMWGQsHi%2BQw1YHmnJ6qJUvQ2tfZY5kb6bLlkpGiBqB0QPU9u2%2Boo14vfbPZ4V88%2FWkdTyoGaSJUyi26oF3SJ8tIw4UHW8I9nM348ccLb0w2zdzj7FiTbXH1ZqxDSnsX%2FNR3BckF2zK5ZvZI8ZlSY50Hn9qpUPFJ5XTDmZsDAJpekLU2ioRXBCKpy0X3qCZ1S9J25vr3s3unq6PQEmcv93sIpNGlkaYFX682ZoaEH%2FZ1FbpMUn%2B5nDwhtL4JK7HERS9ocd3F%2FUK1yp0XcQvSgdLYZd%2FHqhyIv8ylVcAwp34xhr2CUwADZGOVExEu4gfS9AWRk183pkS6O9iUDTJVHZEqLwj1gK%2BDB%2BbmGOCB%2Fcn3Gm2BHVw6ZgwoO%2BbvQY6pgEnTOjF5lnkXaiagQpkuksSKs5GsPHaXKpHdmLaKyUu7GloB8iUHfcwj5X2kcEzmOqHKPj8lTKMx1KkGIJlu0yJF%2BOxFp5EgihwojaTxfjGRg96lZTroNZ8Ye7PSLdbW%2ByLQSKdCMV0R81E9MFcp06iB%2FWD5Wqa5kZR2eM%2FQwaLfkTkKfYz3%2BFzIPLf%2BtUoLxvpOg5eLxX0nW%2BbSBQ%2FUn2ySqFwzsDM&X-Amz-Signature=99543a0671fcdf5bf94c5a0c6d6c80de81ee21e3e5e9d33e830753d065189a8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UITJPXRZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDP3D95pB5PMgjff7nvDRNzT0%2FanJ4TAsazb9yydFFjEwIgMJozH74twJaRbxlLy2dfc5Cg8AP5GoN0TUGA3Pw8mREqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATy6WhjzagJIa9F4SrcA3q7OsuxZydGITv%2Bvj0upWu3It9l3L5OoR8n876YS6kfD8Y53WOZN2tMiBWL%2FbdTCRklsBUNjVvgdvPzZyqXkx9%2BkqLETL9Yi2x8%2Bpzp7%2FvgQuI9aJ8olWmqiVAtvY2c25V%2FTnrKahsBnUnqBC%2FRttIbu89Pz3dFzkXfNFow1syg6yEFgC5S%2BxaOdINify1HqSK1GBomjF6jOlv5UIaRF59yXEanILv7R%2BvvIoLp7XZZJyQcuwtEwN%2BK8FOO7fGpOCTc7Cu0xpJG6NwS%2FFUIx4aafTR%2Bye5QT0ZDAPAenK25KNF%2BTmcgyrmtexPBffdI3jTTL4Ero32M0C4PxQZFx4oaT%2F6yXRDulDdr4J3wFkXuydj26VcfG2TEUt1jN%2FmYtYd1EqgHA1HD7%2Bv2fjU%2F3vSuQgPfScQ8mzeOUqO3CJU5%2FToKXHzu5cu4kRGJO9zvJH0nJphcW9MiJZKTFlnr5623JqXZDsh7COkVhIpUzH1wC9Cv1bMqvtsBKzJS5d0Lddfl2UhHGI00C2bxCs4Ns5KYfoovMEg1y%2FSk9y45ERMWqNb9CvfkoOV0fsmZuJLlfjpfHGgKnSsDpmQ1KixNMHPOYYyW3rycgUVuxB5BrNtYM9n0iAAeeVUnJdLbMO%2Fvm70GOqUBHzItMzIqT6%2Bl3wsrNXZvsGJ6TuNUN8Xo%2BCZf3nhOb0nsgxMwqAXOJ6i%2FtbCOseJ%2Be5Cbv1Rio37cT3C0h1%2Bt4LC3mrjWtPNHOgz5uMa77MmOICvBTKEBwr2sfDzRbAmU714UmJlNXLQOghzbEspjB5sYP5CVSItl8fLq1oj94bdho2%2FL2KVLpusyrK3s0%2FtvrvTXr4NV8TBBDMbV6rBvigTcrFA3&X-Amz-Signature=bc2f995194f9adeada5b23aadb07dbede3efad0175d3c3a0a555d18187a7c690&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UITJPXRZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDP3D95pB5PMgjff7nvDRNzT0%2FanJ4TAsazb9yydFFjEwIgMJozH74twJaRbxlLy2dfc5Cg8AP5GoN0TUGA3Pw8mREqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATy6WhjzagJIa9F4SrcA3q7OsuxZydGITv%2Bvj0upWu3It9l3L5OoR8n876YS6kfD8Y53WOZN2tMiBWL%2FbdTCRklsBUNjVvgdvPzZyqXkx9%2BkqLETL9Yi2x8%2Bpzp7%2FvgQuI9aJ8olWmqiVAtvY2c25V%2FTnrKahsBnUnqBC%2FRttIbu89Pz3dFzkXfNFow1syg6yEFgC5S%2BxaOdINify1HqSK1GBomjF6jOlv5UIaRF59yXEanILv7R%2BvvIoLp7XZZJyQcuwtEwN%2BK8FOO7fGpOCTc7Cu0xpJG6NwS%2FFUIx4aafTR%2Bye5QT0ZDAPAenK25KNF%2BTmcgyrmtexPBffdI3jTTL4Ero32M0C4PxQZFx4oaT%2F6yXRDulDdr4J3wFkXuydj26VcfG2TEUt1jN%2FmYtYd1EqgHA1HD7%2Bv2fjU%2F3vSuQgPfScQ8mzeOUqO3CJU5%2FToKXHzu5cu4kRGJO9zvJH0nJphcW9MiJZKTFlnr5623JqXZDsh7COkVhIpUzH1wC9Cv1bMqvtsBKzJS5d0Lddfl2UhHGI00C2bxCs4Ns5KYfoovMEg1y%2FSk9y45ERMWqNb9CvfkoOV0fsmZuJLlfjpfHGgKnSsDpmQ1KixNMHPOYYyW3rycgUVuxB5BrNtYM9n0iAAeeVUnJdLbMO%2Fvm70GOqUBHzItMzIqT6%2Bl3wsrNXZvsGJ6TuNUN8Xo%2BCZf3nhOb0nsgxMwqAXOJ6i%2FtbCOseJ%2Be5Cbv1Rio37cT3C0h1%2Bt4LC3mrjWtPNHOgz5uMa77MmOICvBTKEBwr2sfDzRbAmU714UmJlNXLQOghzbEspjB5sYP5CVSItl8fLq1oj94bdho2%2FL2KVLpusyrK3s0%2FtvrvTXr4NV8TBBDMbV6rBvigTcrFA3&X-Amz-Signature=013b0e1c6855ca7f5e287d1dcacdd76afd2cc75c19de5a2bbfbd3f420d3e0fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
