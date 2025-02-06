

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=3ff7a46f379e0b9f08c29c2d91d8b5b514b1736f9235834d3263b0ab9e069397&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=c6fa0f6123a9c2538dd36235251f33d524d44377f5902879366da0ccba354f27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=05b06eb9cd676850d29194ad410d3f6329fd1372bbfdc0250b75922910a141a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=f5f92b85939c81c65fc9d4a9dc93aabaf5a93e5217f792b1bc6825ec720c7b37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=17b7df90151ea1d65cc44b6dda1efa0869072ec5749e51d65aacf68903d5c4b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=da195b56382b244f11bcb4db2e5d2d7777e7a3b2874cefc7d6fb91b891ab110e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=f7134ecebfdc043e1570dedd38ae74ec235a792b5388893bb1074e8d0edfffb1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTUPXAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC0t8WTwdnEG1rMVeRwOi%2FGc1Nt3zHfbut4Of1yvWfTFAIhAMjVCMaVqQEXw9YU7AXP%2FcL1qX%2FRhYrgMrXnqykNk4LtKv8DCGgQABoMNjM3NDIzMTgzODA1Igz2VJogvPldEMtEYRcq3ANDg3Gvug%2BIF1lP1ZLQ0GX8sXNnJHRw%2BOvNlDOOZtm3LTEWvbpI%2BQrAiC1rDzn3OckB33zZp7ewI6sJCD6rBkN4ilIzGPNIqmWWep%2ByOq8iWRGHtlRq7deW42UtLpb8fRS%2BWAeJWGKBxdclyDVismEthdEGCtBtAlpnJHjEvEG8XVKIg24f%2FfOVzBIruf7Ag%2Bx8UywzxCxrtOdTLVlwWi9XBOKBNfjv3RWmejbYKn7%2BVyBzk59NWdGfy0Wb7QydxBrWKW3hdXGMXPlLSaustNydYBesX50lZFKKhTNerIeHws3DxNIM11rI6WcQlZGKr6qCH3o4AcBgY8iLifcamtJkddgQxGsxueCJ8ezeip5dlCmvq6pWj6Pf16RPofvt8QqRhNT1bXNnIbvBkxVnG09Yuvffv7%2BJ7IE17rqhh8qKp%2F36sTj9U3K3RWNh827rbYMVGIoxu43CZfMrOknYf%2BwH0ocvpNNqnL0kfzD14c55C8t%2Fm0GmIp%2FmaUOFDt4zY0CvsTDnHRf8ApFlWxz3OngvaX%2Bm68j%2BqSZXd0PzdkkKWUvX0Kia17VE2SxGAFWhCeU5I5k90O9VOoa7TL2a14cId%2Fc8mSMPxDnxB2V5ZXizqTtKIpAEVfTom%2F92YTDo%2FZS9BjqkAYwve81JLZ0gAZnwcpxSWXEZHkHwUSgWKTUkaxrGGd6JnVdU7yHZdBmJkanZ5%2FpcCk1dNBc7kX4D1lp%2BDVibPw6XnaahjkysmQYZXtYDxWWzZPR%2F9qrmOfcO0uf9uxg6nz6NhNjZpLJ6PPr8XEVuEinq6MSK%2FHE8b2CrvqDslDkF9RIJrzqM2WRC8%2F%2B4pbMUH14JJlLsICEEchdkLocFPQBrNc03&X-Amz-Signature=0e27456b1056ca3568cfc4857fc4da1b841970710ed1aa1fe9f1fb068daac179&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNW5BQRJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCvWgzQ%2FwWDKz6ZwYtuBnDr%2BWfOyQ27rFNDVsw91Xx78QIhAICoip86Wks4P1a0TO3OFXgfTUP5urJ2cUkr7uu8AJ%2FcKv8DCGgQABoMNjM3NDIzMTgzODA1Igwv%2B%2Fz4tjaSZDuG%2F1cq3AOjn%2Br9IltUpJlUSDFSN7wvlmCXVLYwJsPVIi7wx14QPojlqdqtuYOkY4S1gG3n2DPdneekudk4vPSBRMYDdIwDeKYq5Z1EA%2B7qtWzop3Ma6cfMMmp07n2d8VtRp3KxPtaOJViZ872ALqqx0FuOR6GmWENWovnjXiIiBlje%2BHGOVwZxXLIHty5hr%2BmHryv2RG%2B4sdHwdaEBeoFn5ZzIMX2tGA7xZ1sMn46MabG%2FPXpOSa3wwkE5uVjofl6eMk%2FfOIYfHzC4ZG0EXK8nW523UFEX4x6dY323YyDYlp4%2BHGSBMnsOrH%2FTZS9jiv0Ch99kGm7gohZKCNa22%2BSAE0dRWQRh3cs0D6axbcXcfYK77BrC6hzsq%2B5ciPfIIiDKsLjSDMsICvBQvHAu5qI6WGXKs9sqOnbO%2FniSWqu7LEvF1E2FIDvAS2kn5wWKyWXV%2BujU8zaQcDQmqz4OzHQ0clZVTU0%2BpLSaoczoJacaVzT1b1nwpPFwZMnvoo5QH0BkUS5z3GCPTZT1ye9922TxvFk5TDGZxxJF8oYys6nsXE1iCer6100aURFA7J3WCldSWSMqlxsnhUj%2BW0waAGdm55mwp2lX%2FszOSqzKqoLOFheBbQYOVMA4m12UAIfF%2BDavHzCk%2FZS9BjqkAU7%2FXkjhAKMaNWVXp2tnt6ag5d7sfDbFwWO59m1pMAlYZtYvi2RQGtJYc855M2N8cQEgNUXBteduJUcLvkmz%2B2GYxtkGKcpy2vxrY1%2BOT5GNZOEDWEu7omsqvZ3q4ggHQPXADTmIZ0ClNG3gwodz%2FmYskYDD4Ll%2BOK4GN9McMOyRihOaJ0g1KpQPXRvMN1BIikgo9DEh79LRK51QRI5b0SZFNbNO&X-Amz-Signature=7d858afef6be6d8b1432fc51131b0774a9a508fbb280354bf3c8c981679f1cd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z7IBSN2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCICOmfBDbPwWwvYiic7H562BShUBHsyb9d81M9MgiOMInAiEAqYfjIKh1Hpvjx4SZBa09pqQYcSlLY51rQwpLHUpAfdkq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDGee0v51PyngUuOsoCrcA%2B04MuZLGlOnXuPrsptdZDKpKGnhQdj7JlgTZC6ZmkjdJA4htNuUlsZAHnQd7vGE0qOEzlFuFMMJgnNF4Rcn8jEg3TUstjB4ccNzExg6IQDaClexL7UUVbEhu6trdYTfquFsD2IefI9ocJwq3DrxLpzkLk7QtBMLmp3RohKhAJoQnsmrmeCJAkKu53Tk7441JdJYb6MoWz%2FAR4eWxVgzcHCZqdJ72RxihEcKBvAPjPh9IDstJGysO4oT1yjd81%2B%2FDgjhQijhgSv2oeIvzVWPnxSXfP8MgGuJBSoNY90fOj84BuY8yre45YgkUh%2BGFhYpXwX6DEXPBYgPLgSoMoxUkCRBO0NjmfawjZeGTMR8vJazJrkmBNoob1bnHOkZFcTnxc8fIAlGrXZuwZbr245MMpNXBQ5JLaK81Ssc5KoTEwTs5UsAVkZXKcFQwzJweLhUrrKuxcpzhhWxAzGiOy8BNkFISRJjwwJEkW%2FOD6uHuLOeySYVbmDUbkpWBIWrfKyOhXrGRhxgRMqnDxx2W%2F3CSrO1oxyW5zp%2FvWYJwy63biBV3ZAjI3hvN4my1qAvAl1ffaA1yQlDqEPBMfzCjBm4odPaJ66sDCPzKkcEFzBVs%2BoMIotVfPGFqL1DsZiOMMP9lL0GOqUBF2UciMC3Ke8AZjSc2q7g7aAtzlTw52b0qFVfw%2FbX4DXoYqecZChoje7auEzX7lLG%2Ff4DBffqZtiK8JthylcaLePJk3%2BZvb0BjATIA8C53i3lQjNzlsGMrbR6RQBCSRLQGXx6O9QtulbIyew65br3D7JX8sXRmGemvHuKTRk18ektWtjf6yOTT1xuCwHriSGaOnq68i6LTGaKMNvdXInhZ3N0BeGW&X-Amz-Signature=30e96aee9ce3c2ccc2d378e9b5bcc5921d720ee635beffd676814512df119e51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOWXECOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDLB3KGR8CgNLfK7Sluh55hlipv7mUU7hEFQ4fgMt6nvgIhAJUFn%2FNvvyYnkXfEjuSPRyrBu2k1hYz1WNG34%2BAgrn11Kv8DCGgQABoMNjM3NDIzMTgzODA1IgyclBQXAH0PJXGSdYgq3AOMOEk9bH1oE7NH5mwDMzB6HuTJOA9%2FkQ70N04r63Yz%2FyxTyEIfSMO10kEXVvT%2BJw%2FGSUpN1DbryxU36m76VjcYEyXHZRn47HAzWZv9yQNX45aqBs3EH733%2Fxonx8MarL3YVZEkfYUXzxusGDv%2FN9JUKCSeBHf9JDTkYWPK094IJJBTLoQB71q%2FV8RsTzqIiKy5H5eI7FoCWpYEit6JD4fJkGc9LyC%2BJP39EnljE69tJgxDf%2FPtKsSg%2B8O5t7rehTWmNA68mYfgylPWiL%2BSpUNXtRTnr3NU6pvLl0BP85YG59luxHK8Hf10RvNKc6YizfYbjwTKRw%2BypZA6UrEkOVz2hM2d7%2F7WnX735sz8FJLu3Jg0l3%2FNviMTPCXiLLjbbGlgZICRwWV8bJdVH9C0KyyzJLOsEe3YLGwra%2BouKTVz66AlCRZFydD0f5YP6DViM0QTt96KMR3szbW7yIZtQD2HRno1Cxd6l4IZ%2F755NAIjSOLM5ehk0VkWjb7kcYRgkguFFOMXMaCKca5vHMtO6H82KbEnBEl8k8JoswGYwULiqs4%2Flgybb1eut3CTa5%2BSa0wQCINmo4zpciJ15%2F6pPSIlGn%2B%2FYDvGVq8JjDdC%2BVMfgfYb5lfKPrA56SwYiTDy%2FZS9BjqkAQprMHF8%2Baey%2FLZJQVdkrQcctXx78HGTd5s%2FfpazP5CZmEFpxgYBhqQuS0d%2FA%2FKsjqhprMyNXzpIuqiIk1YGjes%2FYWh12%2Bb7kU8psdbmp17viski6fP7gSPHkgLgP%2FLZTpcKbI0AQ4JrPTsqh0NjH2lkSLmJep63G4f3QdXtfMX5AOmp21RHappwM3jbQ0q98xph5UQP3JupM0chjbJOyALNSz6g&X-Amz-Signature=1f0143b0093981c832d635357aa2683bd90607f7411267feb560ea1cf8faa7bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOWXECOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDLB3KGR8CgNLfK7Sluh55hlipv7mUU7hEFQ4fgMt6nvgIhAJUFn%2FNvvyYnkXfEjuSPRyrBu2k1hYz1WNG34%2BAgrn11Kv8DCGgQABoMNjM3NDIzMTgzODA1IgyclBQXAH0PJXGSdYgq3AOMOEk9bH1oE7NH5mwDMzB6HuTJOA9%2FkQ70N04r63Yz%2FyxTyEIfSMO10kEXVvT%2BJw%2FGSUpN1DbryxU36m76VjcYEyXHZRn47HAzWZv9yQNX45aqBs3EH733%2Fxonx8MarL3YVZEkfYUXzxusGDv%2FN9JUKCSeBHf9JDTkYWPK094IJJBTLoQB71q%2FV8RsTzqIiKy5H5eI7FoCWpYEit6JD4fJkGc9LyC%2BJP39EnljE69tJgxDf%2FPtKsSg%2B8O5t7rehTWmNA68mYfgylPWiL%2BSpUNXtRTnr3NU6pvLl0BP85YG59luxHK8Hf10RvNKc6YizfYbjwTKRw%2BypZA6UrEkOVz2hM2d7%2F7WnX735sz8FJLu3Jg0l3%2FNviMTPCXiLLjbbGlgZICRwWV8bJdVH9C0KyyzJLOsEe3YLGwra%2BouKTVz66AlCRZFydD0f5YP6DViM0QTt96KMR3szbW7yIZtQD2HRno1Cxd6l4IZ%2F755NAIjSOLM5ehk0VkWjb7kcYRgkguFFOMXMaCKca5vHMtO6H82KbEnBEl8k8JoswGYwULiqs4%2Flgybb1eut3CTa5%2BSa0wQCINmo4zpciJ15%2F6pPSIlGn%2B%2FYDvGVq8JjDdC%2BVMfgfYb5lfKPrA56SwYiTDy%2FZS9BjqkAQprMHF8%2Baey%2FLZJQVdkrQcctXx78HGTd5s%2FfpazP5CZmEFpxgYBhqQuS0d%2FA%2FKsjqhprMyNXzpIuqiIk1YGjes%2FYWh12%2Bb7kU8psdbmp17viski6fP7gSPHkgLgP%2FLZTpcKbI0AQ4JrPTsqh0NjH2lkSLmJep63G4f3QdXtfMX5AOmp21RHappwM3jbQ0q98xph5UQP3JupM0chjbJOyALNSz6g&X-Amz-Signature=063e5fabfb16e7aff2210c5ff91b9d063fbb8260c7ed586a429ac3e388cf9015&X-Amz-SignedHeaders=host&x-id=GetObject)
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
