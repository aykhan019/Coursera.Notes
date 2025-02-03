

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=bebbd9dc6984320233c6d4f60a2525b796d775d9e5e359798028c70f4cdd5fe4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=d403842003ccda717f85c5566ac16a7a4a1b1965dfd69a97246799fc10b719c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=ae4d2520f1c5cc82fe319c284bb6758775a6f5bdec59696995e1aafb4c15c251&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=0b7c517029a5e4d498695c36cca071815db402c5bf90821b232fd9942abba697&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=bda6996c3a0d2fbfa79a401a8d5e4cd4a67529da5342a7909b262d933634ae66&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=dc06521ecabe036603bad540eb8d85bac02419385ef4e4e69769bb949088d3d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=5ce8162a044605663fd61dd51b3795d587b1753e2dd0a9c00d3d7b8e917342b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VVBOWCU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FzDelIpjTXnSan6qW5irof6VSKg6lNGvfavUCAy%2FcwIhAIIdZmg7Yo3N49d%2Fyl5PmfQa7o00Il%2FKYZ4R1hC0FLWCKv8DCBYQABoMNjM3NDIzMTgzODA1Igwrdwt%2Bjw7HHRtMSIIq3AMKgw4wq4%2F8aCjoB74ekFpu%2FgYWkUbG3dItBLcU2AO0E1U2tIuC%2F3zC5G6HT3znslnzjZ2MOrFlEycBqTTMOJjWu7hYI8jtzNxKl%2FGPXM74SDuKN240khrrfdFDU1aTpBoUgBwuig41Foz8t7bNOBX3WvPl8XvkZ3VEiN2Tdfr8usJqNWGqBXSJTycCdkKsEpCYbFi6yVhc6AKobV7OLU1KLkDy85xsxdvpa0%2FBMvBQ946Q9HjHkBqu6fM%2FJosWyWWrodzlSmJq0o96%2BbL46F9tMlT1rxW9FJqMNpTRrWqjKNX43Mp61Rn7McXE4l5wOeSrwRNaomCGB7gCdZKAEq9c0KG9mUveE8l%2BSo0xfVHuPBUWKUfw2xqf9LAvkC2iLF78b7BIhXL4ZfSz31o%2B468OAkgksiFioRuLEvHOmelg88W73AkV17nU%2FodtN8Ra1nDUI8NipyCLFJYSkx08umc4EgDDho6kd29llR8LTrNxnzpNuyqSXnZJAvPVIFUL4UUhWDMbR1dQtEMh7aS3k9iRshNQOOg1K050eFMyMF2rGgZmOK7KtpgN8Q1qhk848PuA2XlKAsbfOEDaa6d8mldaN6xvzVmY%2FEOu6xCvl3MjGfklhPeuEDfHvzljETDt8IK9BjqkARUFo8OdOwec%2F8CHMf4Sgno4wIjX2giWKSu6NwLN6msA4Wo%2FVjjBtWZwMX0M9Ty2b1EiZK3EtE3IxmaHC17VxB235Xt3rFtwIE9baKTDImwyTov6Cdr8A%2FHkWzKp%2FVuaDAf3ji3DdASwqjibbJHQjzEQc%2F5xFDyJ86%2FG63EWGD0WpAfCBOY5TAJksSOmJq5o3Soad%2FVCjqSz61A5n80KlTIBi8cY&X-Amz-Signature=8c1cbea0691acfeecf764b27503c9e0ef9e939ee649f56810bb6e942378a9464&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMC4CNT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F%2F5iRv38sv%2B8vAvrnvzczyTQ8IFmiSm84D2PXYuWj1wIgT%2BDLW2ZNyu2znxBvf7PrYcs2Dv5Jr86gPomvK%2FogQsYq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDAnAPpy1809%2BLqG5cSrcA9fLBFHJa3tXYptjyhVs5xZ4hj25ZLzNubPqpcLTX%2FHahuAK5n4jZL5DszTPpskjDRRFRdL6TiHV88M9RV8Gfc65fqzbwa5fMMafGlzT0FN9Y3AqHJX397cJjCvXdTqkFgI1C1kPvMf6Td1VERw2pGmmgZVGEd9EjRxjy1ezjJpiCRb9vsg%2BCjL4pqM17Gst%2Bx4uiD0sbhiNufBcgTxX44TRPMmlU1VlcOJpJwLTHdL7RXhBelNboPKfGICS%2Bh970Y90t5kveFx1nN9CIQZHdqHp4by9gn%2FTCNUU1YX3hEhPeyKo3jMjvhLcAedHX3ZIERzEqq%2BjJ6PYNn1Ovli%2Fx6ugRm0lHa3vzTe7RDy%2FMCenxcOU6FMCtOLtB71d5zk78ubos6dT7EC%2FBhwLJiHbai0eic4y77%2BSBH7vjvv6Al79ikKIi4i1KlL%2FQrMKIqo%2BA8XebRtKN%2Fi8Xg5BUuLTqg9yUtTY55eqva68Vec8c8TDvjFP5vos9ZipTadguQxZ97UXl7JqlJu%2Bu8Ktxdyd9N2TJDuXfpbjhRt2gzSxGyOOLrPhH7faS%2F%2Bi1DNELLovMMu994%2BfezsT0SbAf7UfaxSabBKPoS6GS1JvrznhZQoknZhlSH56F%2BQe4f4eMJjygr0GOqUBq2umtdC%2BT3VvuQdWV3z3nrCoa74544iiIdVEb5YQOTtyEslLgif6sX57qcmdwKzNI8Tz28JFa8xatSK50c9U%2Fqi7D8EaPvbmWhymmuEaYiWgG2kONEeZyejlyi%2BlhUthC1DpJH6vfCJNvtaDvSVImTi7oVOPQ%2FpozbiO57SQTep7wjxadyr%2BKvvEQoOKO5cAwy9ze0fw6dJypH9EeGyjVdTAZfbq&X-Amz-Signature=6818a3c12faeca68c0864e368f400f872633ba85141b92c3625f754433feb7d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPII2H7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiuqJC1muRmiX0WXVRs14wAF3Tfuu5fUqRJ6SEh4exAAIhAIDAYD9DsTGsWAPIyt8zIhmu%2BZicElAcwGWgWOYORxvDKv8DCBYQABoMNjM3NDIzMTgzODA1IgwUOK2h9HLX5QxAVX8q3APLogHo%2B9XMal745ddJRSygE2rIsuvgTpYNXp7ApdPywDT7itrWbHvimqQ8Itjwpq8zBQSk9cmarYrBtODq9wncgvF9TCyGVuzX0nqn5sOki6phOpqQSjcpn4auGX7WsqnUJbEcyZNLhvFRnJvjVmmezt8nkw5o0CSzrR1MOt%2Foz%2B2F7ibgf%2BfJTCiI%2F1kdQ1k%2F4yZ2ISVJaTknrlPj72v7CElmy51UqUPUY18j3mf3THCQRADhfHBKLqaFMgYBj6wOQqX5gQWa5piPYOw7qkqXBMQVg5if4aczoBbM5O1GKJmTRyUIwrSU8OlFw0mH4a7Q%2Fq9GKdmgijrm22j2u8vOsaBAxHXQSm%2FwBdTSsnErHVnfyphev1fOUvW2xNekdR8MAKYHm1h8SvgE07X6ZyMH7BqW%2F2AISKYBUeERqowxGFBl3M0naxmACv6d2qb8bsfKznWV1JDdtzAZhPUyWLDvVOZaVX81T80N%2BRLNEqGq9NjQXEWO1YfCTiHDJLD970TsUYhlX9atL7qI8o1Wy3dqfUFnCtBGbdotNJm7OQ9CfbzGwKflzcKlypDdPjJn2DGN1LELmztqUmfor5gzumk5hLuesPBJMhJEUrMBNe%2FVGUZIFFgPnIWgKTunjzCS8YK9BjqkAf7HyN30jF%2FmJbXl7N42NqFlSxhZvY0bqPXVrDQOBYAOvhLB8Fb%2FQzydQPf6D4PokaPZCkQmk5axRssF8%2BN6%2B3mz4SyeI9mOVGszgmj1IOWZBKZjGoEIjoU9KLSNqLa7wauXKV%2FEZ7b196jf5yv2catuJQLD4cvGX4nHJkiPYZHP32GuvAx2hl%2FO6qTuDw1A8jPCBiH%2BVqWjuyE%2BXm38l063CjBv&X-Amz-Signature=455979c433c22650d770e25a98dbcaaf06c1dd52d366aaaf26863f4a4156ca6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MHN76IZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv2psdxhJ1IXSmJagMx8boTl%2BwXw69Qex3ueRlkfYPmwIge%2FvDz3AfMEhcNoOyBrIwbcDcX6iHQDqCX4jD7KyGnp8q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDJEvYlrmxT9KiBylpircA7vn8F7FKvFYYv6oEK52W9h2TC9iDXM5vkaDoCxpfXsMNSHmyRA4MVNGyhPjms9FPLTGleEkSxpFEqaT3zaHs4lczz1EE%2FdiZjVABboTjAEosyyn9WwRYn5J2OXVppX1UV16W1e1c3wkFZMWeoBbbggEfD7WFhHp3MsKONtK%2FfQm8iacu4PklvVrLScFGTvjQJFpUaxEqTNueHm%2Bjg2mMeYt3tLWoaW75VQC4U8RZfpOJpUfV2%2F6P4XmGxIsGRX0T8ydpSMdlC6KOrMjP2gskNYYVudFZMODXTcR8qkq7NaxnP37%2Bl%2B0DROmf8qCKCTlIaaSAYpqFVqBuE1Y5i1zWnizSs6OjvLlbC1jaiJFJAqVfnT0aC56lUttN0MiS3cNOQb2rLxRD0DeuV39XGvFdou0iwM2TG97LefuMFrGIk7tRnJUZ%2FxIlPq2axmxBa9YyLgzfkx7q4yJJY85JoKlV4GRUCAds4pz8MDhRjBjIpFUIUuxdW5GjprzPahJuthemVzXJbHuImiwddSpWAgGiivCFKYD665Wxbn5cg%2BRSgD3PKSjZ3mKVGWYr8Wh82GaKdzaXt4%2FQOuRlY6RHfhIlH13%2BeK3HaX%2FGopd6y60SvLzi2T%2FIRZSIh9sITz6MIzygr0GOqUBdPgmdD1mhHTIWlrXcm%2BRDVjheS25duZzjrXc6jIZ2OMisUcjVMRJdzJaCQBXOjr2NpbMaj3MfAo3YrudIqveeXLJky7j1kmPbGLKY0ls1p4XfEUOaHSAuEoerRLjeoCB%2F%2BHzjfcX%2FWzkG%2BEQuFLCNeM%2Fr6VIqVof9%2BOusmuYoRMuJN5u1yBMbBpB11027%2FkEpWxHLdlmVOS9PP99mCGT%2FtPxQlbo&X-Amz-Signature=f13b10d6d02e6f7fa8a33a616ff4d40594845711daa8023939a980027dfe49c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MHN76IZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv2psdxhJ1IXSmJagMx8boTl%2BwXw69Qex3ueRlkfYPmwIge%2FvDz3AfMEhcNoOyBrIwbcDcX6iHQDqCX4jD7KyGnp8q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDJEvYlrmxT9KiBylpircA7vn8F7FKvFYYv6oEK52W9h2TC9iDXM5vkaDoCxpfXsMNSHmyRA4MVNGyhPjms9FPLTGleEkSxpFEqaT3zaHs4lczz1EE%2FdiZjVABboTjAEosyyn9WwRYn5J2OXVppX1UV16W1e1c3wkFZMWeoBbbggEfD7WFhHp3MsKONtK%2FfQm8iacu4PklvVrLScFGTvjQJFpUaxEqTNueHm%2Bjg2mMeYt3tLWoaW75VQC4U8RZfpOJpUfV2%2F6P4XmGxIsGRX0T8ydpSMdlC6KOrMjP2gskNYYVudFZMODXTcR8qkq7NaxnP37%2Bl%2B0DROmf8qCKCTlIaaSAYpqFVqBuE1Y5i1zWnizSs6OjvLlbC1jaiJFJAqVfnT0aC56lUttN0MiS3cNOQb2rLxRD0DeuV39XGvFdou0iwM2TG97LefuMFrGIk7tRnJUZ%2FxIlPq2axmxBa9YyLgzfkx7q4yJJY85JoKlV4GRUCAds4pz8MDhRjBjIpFUIUuxdW5GjprzPahJuthemVzXJbHuImiwddSpWAgGiivCFKYD665Wxbn5cg%2BRSgD3PKSjZ3mKVGWYr8Wh82GaKdzaXt4%2FQOuRlY6RHfhIlH13%2BeK3HaX%2FGopd6y60SvLzi2T%2FIRZSIh9sITz6MIzygr0GOqUBdPgmdD1mhHTIWlrXcm%2BRDVjheS25duZzjrXc6jIZ2OMisUcjVMRJdzJaCQBXOjr2NpbMaj3MfAo3YrudIqveeXLJky7j1kmPbGLKY0ls1p4XfEUOaHSAuEoerRLjeoCB%2F%2BHzjfcX%2FWzkG%2BEQuFLCNeM%2Fr6VIqVof9%2BOusmuYoRMuJN5u1yBMbBpB11027%2FkEpWxHLdlmVOS9PP99mCGT%2FtPxQlbo&X-Amz-Signature=187730a07b7c8776d3f0b4716a21b4a5004c3fff756ad6a0a12eea6a481292ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
