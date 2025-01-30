

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=a8c914a6f1a420bc602299d700a7f39372a42fb275ba7f3d507982cbdc842927&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=d07070bc87fc69a559fddf3196f88ce733d20f66ba0e321cb2ceace5e845e922&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=4359a10d178eac3067f9e99bb6e49fb3eac682626b23fdc5f2a7bfbc0d81bf87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=f73ab2556447a2cf5ad3af185225320f7e50d98f80295d27d08554e7716948a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=8be693ea96457f41dc011eaf149a9177c7e3115346a46653d515a5983cc1d7a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=0f083ddf1aa42eeec5cf8ef5f8f4fbdbfc542bcbe772fa9c90432ec137a07e23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=7be3b99dce40644267d6e116958867cbbb464ba7209b4ad79d279c55d1f5f6e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRTB6W3C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxRUzaCNbyzVkYtS5eecUHTotLppPhwgHA4kL238kY2AiEA58a9gKmrZ6iPLGKHWBg6fLc7hZJQaKZCb3h3ZCqvUpsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLU4s76lnYCZ2DSCSrcA41hA4BUf0iL4phcQtgsGtrSEaT4NjBfhD%2FpNFwKk7nRgJaiIOb28QHlBziSaFVSPNSKhsVj5GIqEmyV40SaJ8jmaUAHQhCSndYN6nu6paX0sCK%2BQSrLuqMGqGonsbnEdfAX44tgoguNGH2TF4GxgPOHS9VGgr89OYieC0qoMpRpzbg9SWOLfRiRAYGXcDhX78%2FRrJdDlOiL%2Fefcg2RwGOIRQdIEpv%2BZVh4ejU1cSwBH775ZE1pIBHrop6NiAx7%2B4e4SO3V9Uj0LfOtb4EpUvF0yBeZjTgmCI%2Bn1hKNESeT8gkd3kQg3EZVR9RU%2FMU%2By5SjaNMxlKly4BdOvVEpW0rPi6pI7Kkulv3Uh76i7F%2Frqzsu52AIET6Sx75iXZCrVGr7vn%2BXKbcZs6jcjsvZI5gsms2%2BE8ed005WFFUpDt6xJNIpOa0fyYDWOOdNz6YecbYKQbp993zKvdSNNMvzG7EhS%2Bd2PyiDt%2BtvMjx6cOCcCGhiWlHoUPx81d5v39YturxFMT53gVd6u%2FeVFGnl3VhKCLiBx7KJgeP5mx%2FuDM4BjAM2dU2S%2FU9o1flT9eamCSqo8N2qpNPzxCvHrobxlNTCe6yJCCUFqnrTQWzZTGJaEuZ6ao%2BfWXI1NtZWyMKuj7LwGOqUBv66f6VcFloRoDHeCk%2FaHOxIIjPbnhWVHRiBO4SyAWLZynZBbtYZAZa4WLbQcgzqt%2BWBTNEmFwD6c6l3GqX26p43pAoG7jONB9Xi6S8Fso6JWIYkS0K%2BcvWgzNCAU55BEAuz%2B%2FTocJIQoJd0ZzGc%2FyJYjWbkeDV8xt6TzKy30qleSVt336kfpLaEgl6acriAN10hFQPzFuGHZSM3upDgurC7Do1ui&X-Amz-Signature=e7499daa0a4940524f91124f052aa049a125f697d98a75a04ff99c2fa8a0a565&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWP5ARSG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCabQbBOinlMQ%2Fe%2FSIODX2S3DwRkUm%2FuV6oE0rbypU9xAIhAIbm6fcwTMlgtmorJSjEKUR2XGGwEi7QKzynvUD9zgUEKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2FciyGt%2FjZFy%2BSs4q3APsdA2Dyza7e9WC2Nl5eQX9xO9msSO6Zqf%2FBOoN5tpbNJWHTxfEuW9tvR%2FL2dkbUqB9llAv0o2aO9RGlJz%2FIkC5NIdM4P7jFM2kom4J1py2FwHhZeYuSS0ZLnQKJP4DXkWz62uNKohEzwSLP3SV2KmoNZb14S%2Bt8V76sfZ%2BHEzHEwh%2BelJUWGjt3k2H6aR0JC9OI1S65B67q5X0Os6ydO5WFzqGd0jx1tXuNmUyFJrECGjS5kqXEtQjN6qv6dhO8kC3UfahsIFIayXWkvP5P3k9MGrPt8BnQyhUa4KrevxHaTlNNQViX4rA84tY0kKjBeMc7BIYpmo1Hm7UgO5%2BSfZYj636GRM4FRmmu0P4OJlSzqObCmtX2rXs4hzq8%2Bks7rhzPSGz5I5xqj3Betfd2MbcXIqfeazO3e%2BOmXLKt2FxORsMB4fo2hDDGxQkjF%2FL%2FGnj62h7mwOPRKfgED3fw2a6Ype7PG9SKfPOd%2F38gjdw9sfpCnrUJC1gVc9BMKXNpD6JcTt6waIHlbrUVKvdJqwLNbSU%2BReHs2pl%2BMuN8cjDhM8Ka43gc5wBPqpf542MWqhiDxvpb7iwgPbhw1BEb7MdYs8st8Xbm0d7XgpEivDSSS5gdetsR28on5PMozDkouy8BjqkAYfgU%2FI%2FdIFLamP2eX8HB5lO%2FG8SMz0Z3MslIFSc0jjbFfbYrKmr6YHKPS2TEDwn6gSLY1GOkuqVPLs8CtNWwrNcnLppXqQXY0wHnFKO6QAtxhdKuz8h7iWC2XLpkLopwu%2BUOybn6g7%2FUcnonCkOJ4DjFPWTzl9s3Mna%2FI77vMmXJJ6TVy7YguK5MU4oRZwbkQtqf40VYVrQ70yMQOa12hvXICjl&X-Amz-Signature=55bb9906dc0f850321d74aaa238bb5121aa59f9b9ed1834c18d8baf5030c8451&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXLUG46U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ9B%2Fy09Wua%2F0ZyIU6Pwgwk7lwGkzt3NV2lD8nWbv1sAIhAJuk8jwk%2FvIUuQjCullE8XbJV2UjVcHhplL8SzRUCiykKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2PGroC%2FVWLaSEed0q3AOGZkrM%2BHIFI4XI44ukaiIxe5GG8hjmWwxOkFwbuEuu1kdjYqdCAOsvwpOHPcOnl0h2dxQj%2BSodrG8EIEJR9kv0q9kOYSCkNtVDJazBs0cVWiay148aNzb%2FT4HweFEmBL8X%2F9skP5W%2BSSsiNetmdN%2BHJOkGtifWv4p3cu086E3v45QTungNnQAxIMGvXB8TD7cG5yVYJtPtbccaaKjsDkMNnDFd2Iyt6f2vx%2Br%2FEYVqsG5DHx8T2KZdyPE5%2BCZzCwyIIIAd3FcPuxjma7TyIx07m6DAakwq%2BJGfi%2FR3yE2gs%2FuZhu8efRmNHSga8gg2eYv3qTFkH0yUSy3ZQfeETD9k9CKy5iQE92RcWzO1bEy%2B0l%2FUa2a3Ld%2Biy72ZJN3zzKyAK6pd8nKVvfHOpYknoqaypm9HmaC9GqjHETWlmqFlT%2B75wS4%2BE%2FIy7Cc6t0%2F%2BKsnXlJzlrUgBks4CeH06nnliNiBcCPyGiopsH%2BLB6%2FRFXcyGTTpKRuqq7%2BS5CXz0%2B8nixeCeqwWubLdHLXQBgGfYNrrRsg5u%2FlWUPzIIi0%2FAqxL1INWTjFaQHCX2cowhS2S45O7BFnVskDEonBrdjk16evgeBR5jtUgJjgE3CvXyGn96fnI64dWfgNDsFzC1ouy8BjqkASIgLcOsdTsQQB2o1d%2Bj5pR2ypLLPKy29zEkNUqhlyqelYI%2FlkTGeBXs88L9J0VK7kq5qnlWqH2kyE0PNxIu4ApLEykYa4w%2BOvzUAE9KwVstELGqBNrPzAct3vBS3jDcp1frM1tKCWFL8lyVYiHGjJX3j9BC%2Fo96uMpn8s2TJIyAz3ah35ufM55C1SWnqxQJJFel3hIcigIgpLke4l%2B9BERLyrZS&X-Amz-Signature=326f7c344b37050903ad8381994591737e76f51ae2b315766165d4ce00f4de8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKMRIR3D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPXQjHA%2FB6wl5FP3bGb5AmF%2B605WCmnxVJ3%2B%2BvhVbMgAIgD7N1sn4uYPxqbICe2wHKjkBkmmxHeZNGiOH%2BOSFQFa4qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlMYTnxl4gGrqjmNCrcAx2aCjF2AolWwpoaOtAQ5LMtqq0ohVTdfXxj5KUc2b897k54HuNSgJkb5Wt48J9%2BRVEpCPcIDZEWDI9XqJUeIXadbFzgn3qBSbUiaE9Wkbm6VazCQ0cutzC1H4TG91WV%2FPJQBqnuvFHwr9j5E3uwKh0wTK5kmQufQLC%2BkozoKeoro2OpqKftuoJPX8jkja0DF7vNbsTCxPWyqF3u98nnQJIxwrC7n7f8PlSQ%2F%2BSTeWmxgYXpkTLzmDNTDa3XQz6Z6WqbrTOf5N%2BTeYDLijQ2jCda5wRfVVn4OSO9I1iwoScF%2BTPW%2FLlnE30TfnbPZaK9TmnwVKx9dZwN%2FL2dACXf78HqVMS1xqFrZ%2FVpo9RuMas%2BvoXeRkgsCOwY7KzJ8F10W%2Bo8xQiX%2FiATNX4iOuPpdBFXAmbCijZ%2FYAvmFsplYAkvWTqqvEoHEaeY1iVYTPJu1fSYNbQxUBY7Io0%2BfVtyqNo3OhZidkNdL%2FetynBm49DWcSfUKfVx77bGTqUMY900QLBLx%2F14ap3Bi7RqeQ4L07L9TECr5YbA9x5uZ4vZhfVJXk1Hrau02y4%2BViASIDAlmjNxUCrVrBjgrekeJMsHXBDMNowS8GtoAKuloRcFmAmC%2Fik6J3aBWPNz3XzwMNOi7LwGOqUBPk0c8VGTgtuB3VtM0T1S92lmIo5b3ExOSbL6dLjkqcO8FqYiUKkZiyBHdfdgcPSVleKQgd6e88Pm5DWw1v9Tm7UrvJhZRhc%2Bf5vfbZtHcKAGLdEC5mNMwMZzYAC2ixBR3UA75WgOBl%2B%2FilmDpAV3sB7Gu6Hx%2BX7qtoFRMpOsONtKQOIXm4E8DJxyZ8X%2BlepIV6oT1QGbr4N2ybDdSW7t1mlt2ISv&X-Amz-Signature=9df47d7731df9abab4be8b44ad89da1fa5f1d17578e130a372eeef55bf84bbe4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKMRIR3D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPXQjHA%2FB6wl5FP3bGb5AmF%2B605WCmnxVJ3%2B%2BvhVbMgAIgD7N1sn4uYPxqbICe2wHKjkBkmmxHeZNGiOH%2BOSFQFa4qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlMYTnxl4gGrqjmNCrcAx2aCjF2AolWwpoaOtAQ5LMtqq0ohVTdfXxj5KUc2b897k54HuNSgJkb5Wt48J9%2BRVEpCPcIDZEWDI9XqJUeIXadbFzgn3qBSbUiaE9Wkbm6VazCQ0cutzC1H4TG91WV%2FPJQBqnuvFHwr9j5E3uwKh0wTK5kmQufQLC%2BkozoKeoro2OpqKftuoJPX8jkja0DF7vNbsTCxPWyqF3u98nnQJIxwrC7n7f8PlSQ%2F%2BSTeWmxgYXpkTLzmDNTDa3XQz6Z6WqbrTOf5N%2BTeYDLijQ2jCda5wRfVVn4OSO9I1iwoScF%2BTPW%2FLlnE30TfnbPZaK9TmnwVKx9dZwN%2FL2dACXf78HqVMS1xqFrZ%2FVpo9RuMas%2BvoXeRkgsCOwY7KzJ8F10W%2Bo8xQiX%2FiATNX4iOuPpdBFXAmbCijZ%2FYAvmFsplYAkvWTqqvEoHEaeY1iVYTPJu1fSYNbQxUBY7Io0%2BfVtyqNo3OhZidkNdL%2FetynBm49DWcSfUKfVx77bGTqUMY900QLBLx%2F14ap3Bi7RqeQ4L07L9TECr5YbA9x5uZ4vZhfVJXk1Hrau02y4%2BViASIDAlmjNxUCrVrBjgrekeJMsHXBDMNowS8GtoAKuloRcFmAmC%2Fik6J3aBWPNz3XzwMNOi7LwGOqUBPk0c8VGTgtuB3VtM0T1S92lmIo5b3ExOSbL6dLjkqcO8FqYiUKkZiyBHdfdgcPSVleKQgd6e88Pm5DWw1v9Tm7UrvJhZRhc%2Bf5vfbZtHcKAGLdEC5mNMwMZzYAC2ixBR3UA75WgOBl%2B%2FilmDpAV3sB7Gu6Hx%2BX7qtoFRMpOsONtKQOIXm4E8DJxyZ8X%2BlepIV6oT1QGbr4N2ybDdSW7t1mlt2ISv&X-Amz-Signature=62303d5c70ff409248da2f4829aeed31670ccd602295a18a892a1fb8b86065fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
