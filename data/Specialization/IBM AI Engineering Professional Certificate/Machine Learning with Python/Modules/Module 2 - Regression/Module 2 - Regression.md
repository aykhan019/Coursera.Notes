

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=a810450b558ec918ac5b68e289d455475b36e0b36303b470f77363397420afac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=883e1cccb03d9818976008f85f484f9c9cee9a25a3c1b54808c9c256c9d8a184&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=99a2e09358bf4df8c5e40d4940a5dcb425b7adba0fbdb3e9de9930959650e1c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=d2d7fb519499a82e348af2ae403e9b4896a6a47ac651380626deaaa880a7d87e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=c8022f679975ab0726474dca301f589d1704431a7b4b59cb70d9e57567c5799f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=9421ae9410fc6fabb9f403c5a468d9aae14169a521e7716079af5209fbce99e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=a079a449c13b4315df49c1f8bd82fb1288f6356cec158bc2dff67239c0abae85&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWYXRWV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm7ZpT75f78iPJ5la%2Bw5md6cKRr%2Bu9nS0RdEMQUw6WwgIhANkviJePJoearS10QZHWxXADT640g7aPMLXRcGW%2BpAxiKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTsvWxfwm2KIt42ykq3ANT2bR7PwkVsjny6dWmtika0lOfZtzcwQHjKfj48yNJAjljY8f2z9DpSLN1FaqEKmR0x1Ux7l7tXc8GHMrUuvfJx6krFfPOx06dNvyHLgQ76xkE6UFuNWwFMFHxGlEzVtGRyKDAW7yUQ7PztZD%2BciARuHNZBX%2FrZv4sOC%2BOP00z3Oy8l3xzcwyde2SCCTT%2B1HUu6%2BE%2FtUDsRhOSP5%2BNPbtJp4kIVvnjbCasZZqRxiBEZtl%2B6gK6yn9TH5%2FHjaflyHvthWDD79r%2FaALxaGRXGavBXRGwarB%2BHu4waGYvD%2BP%2B7H8XCtDRZcheq28FnsMgGDfSVLrwT8kFwakwzwpoAXghVpbBQQUeFgkvjD0EdK6qrGJFYWbnz%2Bub6zQ5Jj%2BgVoU4YYZd6WCG7dmyN1j0%2ByZD5gqnD7HEvnqhXU14gx01TAcqI5gkPBgOt9Op5Nsd%2FZTrZYkSmc3%2F%2F4PYcIYQOFfaL3AWlXkVOGLvySFuW4mrLrFsNxsmI2%2BjvROknj9ymx%2FQXxunDr7t6u4TVWGHHvXfuQNp5O0RvqFvdZHHOKhHEYtYFsRm%2FQYiZrncJf0PHjDzO4mw6Z3JrGsGuON992qdr157TEtbSN4FKc5fIBwN8ywNXnwZM40cJOo3VTDGl%2B68BjqkAdCNyB7rVKhG9rv9vMCrZC9zanC8rw7uMmkK6PZSyELDG4ugHAcrWiqQWxu1jcvji1Mqao4RMwyVCMnI5zwmOUIT%2B1Yt6G%2BCy6OPuVQ3weOYKZVK4gto0elYQVtwWbnE598XX05B2bH0YCdg2SWeOm8DbArwquOgjyKqTElvNYwl%2B0byBTUH74yKgzdXVD1k3ObMS8S1iCukktN7Z7U3Z9d1n905&X-Amz-Signature=b55e1ad73bdb103df759f51d3d30d44b6930e3ce2813a1390485c42bba002cfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7CT2OPC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhi3SGP4IGkehRpyUQFVahgs6W6RcXg64oMXJQR1Mf7AiAH1ht9PC3p7r5ZzkpOMJohmHgKVMLxlHxiYmFZ533QaSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGZE7DQCAK0WwNWKuKtwDkZOcAefdVV8wf8sDV%2BRSj%2Fv0E3XSTLWMz4bA9FJLKJecMwVBW2fpmg4hpmiFppJFkDJ%2F0ftDg7qxKPHFZ5INB9ga6Zv9CeouizBOF0O2bEmrbB9YGIPEDEMXNyyivAMilS5O5IZuDOPBDfMMw53oa4QQTX1cqMgjuCOQObP7m1UvatZBVj34M8jyLnFdR1OUfxBsNm1esPoc%2FGkn2gQFJMOngjUKsTA%2BEDoCAlaimad28H5%2BQ9Jwc4VxpKuPk42OiefWc1QzEdSBtM6iYKYMKSxkpxIwDmJi%2FqMuY2TTDqn2lr46Nv12gVdL0ngD1U4cqzN642FJJN2Qe1atknytgqeBUfuTWoT2a%2FmesfWYszEW%2Fnl9QA3t1E%2BtW%2BHuXjSLFzDQh448mumsBy%2Bd34K3%2FxieEwxUrI4PRkEUpmH35Mx7bPaG8NBmDz1L%2Bz1wH6xSpW%2BXlqe4xxoJldEG2YwF6mc53EJ1o05spz1aBDeIrvEeGrQ7uxcBAAJjY7KcDEOIkmVGN%2BwD8agEav8GKHMh1m%2FsOP6kKw3gmZ8EfkUfgWlHtp2pJ9EfFarIM%2BISQrJU0N%2FkZ6aEad404wUxTZUGql9pDKIl%2B1LXumollHEnsIOTU1CfZ%2B4II8qL65Mw1ZfuvAY6pgH8uTtGbPfXUV%2B62wYP2SAdEJKeOf7z%2F7hrnfwAlyhxlsdbaOfmHSATWFaOcoGOpuigyzudSIb5wdgmOFGA%2FKKVdfhjVVhbzOExqqYY923g2hiLS3VDgCOOsjC1Lwfq2xbIb7jgOhgrncuiU%2FYntri61UvGaE3IlNML1hie7atgz9Ga1SQb7l%2Fd6RYCSX8VocjtqkOnK135k1Hj8uj4cBe7A8W6Y5yY&X-Amz-Signature=8e5309dc030f64224e875b45d30ab9e3fa5db75462e4d7673833b3720b94266b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBRYAYV7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE9FkP%2BVWX67ahecktmI8bHaqtg%2BhDafVe02fkrGMwTPAiEA7h3DdSWzEo0Lg0Nsn3%2BZ6SWYi3H7eTKj2h6CZF%2B%2FAcYqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BsU57iVFN9N%2F%2B0fyrcA1odzFP%2FAPXP5VXyf63vzKnmRLXk%2FJ4dc7jHSeH7o2RsSOrREyUkq9xmu0XzsiVcXNg2bCuus9siJ5eJGQQPqP2RXbFKDRRyRTRvWRIVd7u7cVa%2F8Uw%2BEFCF0YioNY8nvjk8lFRXDiKHFomjiTLzB65llYt4jE%2B2BfrxapDeSXmNyKfR%2B8dWglOaaAKHBwICn7OG9wfC%2FCDaj2zbFXQeV5cFVkAlIVIGY68I%2FHBeIewb6z2zoSR1tzrM817JIcns3XRm9t2fvAaAXJSrEuXlrQUgEBdVO05edBgEq0pVtwELTbKJG%2BgM5H5Y0j7hTDHmP3Sr9a%2F3VDHpGQpJS1Vdcgyd1gHgUKKHtQ6mEWgCL%2BKvPesQ6q3oy5oDbr9XX7OQALAUvEOfgY03JkKy1OoPfE0kMIhq9r%2B7RaaDLIwWapaQ1Oc%2FStmvhMM6GOs6a12YslMIp5cEQSWZGruhKiSBh5nn55LYFra583uarBMDyurGGyy1lgI94Uk8kjvZDRMZ5f2g3Dy422IIAj1imz5rkJVmYN%2BapibkRCBmkRfbu%2Bv%2B0iYF3alRlWQxx8bSwYtMjauvmOXK1R1WNH328MU%2BOGIt84LYXPlA7ZPCbhIjYcbQPmGFSWKp5M6nqjJcMMmX7rwGOqUBZoOzxnfW0ElEEAc5DGFIkawoon8oISpYJtN78BviYB3WMVBGOzjzAlJBw3Bd5rlu%2B03RXwoPpURUYZz4%2BQC0CgcJK28Vc6msKt9GCLNAE7MXCEa1hwwr1WV9sKiWZEkV2TwaQ5rYo2en9VBBkoBytQlobmnItmmixUacdcHHj8cR2oSS64nnc3EmlKVRlSY%2FRJYVIuS979%2BKuxTY%2BMV4hApH986u&X-Amz-Signature=e1c14686df7e2de981b4ef2374c503675620153501827db78f1969d816475922&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPEAEUWC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrTagVCCgdtkc9b4t7sPl1fiUy6B3Ei%2BCsb7b7tPDHeAiBFgJG9LWMrjzo5TxaBEtk0Gu5sqRS8bUlPtii95uHbDSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQmCgP8n7z4wTVgeqKtwDYdeqvwVb4uiQyXUwxm1Vivinfmp8BDUkF0r%2FWgYo2bmEyVlkS1KS7Oizq1RhqP6w%2B0Uh1rRW0UOm3W3e%2FpgWNlGmbc6%2BPNQTpLgIVbo3oUj%2BwApGucTxxL24R3jIirMhCQx64RN6D61crDq6yZwZvSIg6cfRBHxHRzWZc5%2FJmcumxaRJ8%2BveS%2FEuGa%2B9JCB2gqguIz8MuSQRRIFcncMbPGTnFJ%2BwsQgpPu0EYI5ZhPb4L4IOi2Dlbdzd1YVdBteQaH8kOsHI4Z8u4XwFoPz%2Bd767DXKXbTe3Jvw000xK1HB42BkCcq5EqUGVIkxoeXf5OYhuLUfHIqO095j6leNw4nW5CqyXKMI6A9Wjyyq6FL9tdPBSH5KU3Z3x1YkLhsOZrbjR0YkOhtivHxgJJry1l2QtOKaqGp3guxzEB%2BDoMMp6csbfIb%2FaHDTAv8tMN7KkGDW2o%2B%2BEL9QQ%2B6Rsz4vD3xOeKJ78juSODw0JERjk5YoDGbO37NsW35XHdPU9yMYpH4khPW79G6Sr3BuBc0L3h5otH7ocReJUznL2oVQw9DSkojVU9kb%2Fv8Jpcs4pGsVJKDNuZYMZIDTpGahnBEUY9aJns0SIshc5lwgMZbCY91KVKGkhuwBPfiCk7wswjZfuvAY6pgFap59mBkusgNklSIKNinCg58CUAA%2B9XYPrFcimXJUuV3akdmvAd9sw20Lh%2FC5TxWXxIjktKFtxNPs4WAcEy918kMauEMWjD9Jc3%2BgnXXlCokR4a%2FsVq%2Fo3hO7koya4oVsi%2B2L%2F7Jy0bj2%2FLMSUzwps5ioBAOCKWSTEIx%2FyY5eeNj4tcGclPtd%2FEbL5oma%2B9xksDnHtovxVOrs40RqJZse7urcw71vi&X-Amz-Signature=904a5b2626deddd1a60a2cfdabc840714ec9a58946ee9cdb62b9727ee3517584&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPEAEUWC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrTagVCCgdtkc9b4t7sPl1fiUy6B3Ei%2BCsb7b7tPDHeAiBFgJG9LWMrjzo5TxaBEtk0Gu5sqRS8bUlPtii95uHbDSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQmCgP8n7z4wTVgeqKtwDYdeqvwVb4uiQyXUwxm1Vivinfmp8BDUkF0r%2FWgYo2bmEyVlkS1KS7Oizq1RhqP6w%2B0Uh1rRW0UOm3W3e%2FpgWNlGmbc6%2BPNQTpLgIVbo3oUj%2BwApGucTxxL24R3jIirMhCQx64RN6D61crDq6yZwZvSIg6cfRBHxHRzWZc5%2FJmcumxaRJ8%2BveS%2FEuGa%2B9JCB2gqguIz8MuSQRRIFcncMbPGTnFJ%2BwsQgpPu0EYI5ZhPb4L4IOi2Dlbdzd1YVdBteQaH8kOsHI4Z8u4XwFoPz%2Bd767DXKXbTe3Jvw000xK1HB42BkCcq5EqUGVIkxoeXf5OYhuLUfHIqO095j6leNw4nW5CqyXKMI6A9Wjyyq6FL9tdPBSH5KU3Z3x1YkLhsOZrbjR0YkOhtivHxgJJry1l2QtOKaqGp3guxzEB%2BDoMMp6csbfIb%2FaHDTAv8tMN7KkGDW2o%2B%2BEL9QQ%2B6Rsz4vD3xOeKJ78juSODw0JERjk5YoDGbO37NsW35XHdPU9yMYpH4khPW79G6Sr3BuBc0L3h5otH7ocReJUznL2oVQw9DSkojVU9kb%2Fv8Jpcs4pGsVJKDNuZYMZIDTpGahnBEUY9aJns0SIshc5lwgMZbCY91KVKGkhuwBPfiCk7wswjZfuvAY6pgFap59mBkusgNklSIKNinCg58CUAA%2B9XYPrFcimXJUuV3akdmvAd9sw20Lh%2FC5TxWXxIjktKFtxNPs4WAcEy918kMauEMWjD9Jc3%2BgnXXlCokR4a%2FsVq%2Fo3hO7koya4oVsi%2B2L%2F7Jy0bj2%2FLMSUzwps5ioBAOCKWSTEIx%2FyY5eeNj4tcGclPtd%2FEbL5oma%2B9xksDnHtovxVOrs40RqJZse7urcw71vi&X-Amz-Signature=e4e0842b07309c1167cac0f8a6982a2399cc984d6aa3dc534e43382587a028f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
