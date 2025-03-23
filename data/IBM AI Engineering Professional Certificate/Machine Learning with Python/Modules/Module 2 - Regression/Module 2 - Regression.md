

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=64bc936faa36c8dff480d0802bfe32267332a8c1ab1aef1b2481ac5637c8f5ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=978e986892da6901a06eae91cebd360af5d2d15838a08b2f0d12173ff9494bd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=264f7d1f881992f1ce96956891cca7822e18eb78a721124ebe121026b7499f80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=d1cf1b1e2facef2d0784e2c078ed92c1408640165bda7fbb82b868073cd834eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=9e6b2acbcdb0740c58f75dfda69f830b9aacb11ac1c1c89de6c43d7c42e64431&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=629255075396a3307b16c15b7aade7420e9d8417b1cf8b811a32705abddce399&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=18798b4aaecf98b4f966bb57ef725548106d2c2c3c7fe2af8b7cf22d2349c440&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VROBQVES%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCHCvo4V%2BE9hPxtve6uX2wo0t%2Bp1DRAhgcSPFEV%2B%2BrlowIhALXX948CT%2B3OU9z2YEbfjEPLfBfCpm1fW8oqZ6L86U59KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOt4HqADsJaiKaKr4q3APNv164VfniGVl9zwVjWikW%2B6GUTncnERzQEh9fUGcPYw6ofG5yD0L9rDAzhfFLwe4dsI3JOyKUkzXxfogSGSppQK%2BC0ZAzoWsVbTAPtYeO%2F%2B%2Bc8oReqe0alrBiWrVq38FyBVt0h4Ql%2F7%2FZZDWj3eSV54i8oUSVUp91SKlX0JplfIYWo63a4BYJcZSKlwjejyusyZ3g9FPpNo9eOmOAbT7FybP54H5IWWUdpsS%2BpeRl7ZhqIbCF6ypqawp%2BBTMijvlwEhOv2E0Of8sfiLIKvaJdYGwFWSX42%2Bxrtskr1TcQOIW5xMa%2F1hgVHmfTxkD65nT4CKEALm0LF32E1n842snh9i43zyzGJ6d%2BnwWE8VNUrAhPOp%2FquaIHMu7q%2Favm3EmHLb3yywtiGgdax%2Fa1aau%2FSnsSCuU4W3Uo6hRoG0LTvppW4nXxE739ZHH%2BcrvZHkzkuOuyOnQy7RLJ142vNmnNM6aT400yLXqmf7QqaOjR9hGgwv167OxwmHVPXp08%2FvUGZDGZly%2FHwgYoUuP0rjtU70N%2Fasf8qI2eSlwBu1Wh%2F3sLpfcNHvVOENA%2Bn4quXdyCDJ3r7W8tgaCH0CL9%2FC5064BGSGUGDUyuFJ3AC063rQqa0m8USZWGiwtDtTCGm%2F2%2BBjqkATY0pCQVJj0rbboB3LrD%2F6yVhqEW5LtioMxDry7hVoAjhPTDJ9FazM6HNz7DzdiEwvi5vWY%2Br6p9Py%2FLUN77P7tjIa1VgutSpSGUGXk70I1BbEhd7%2BMSTiYDkcjcs99JToo3blERaQFlMhMjr6iKuJTr167lDa2PfAQXec9ul9U2uTcVEC2nzGy%2BvvvctBbvA5S%2Fj7oCmSPtoTHA99gPGPyChpVN&X-Amz-Signature=8f86330e46768b75568c5858727e0fd2d25ccedf05d4558d85502152fb6c8788&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5NCMFR2%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHxXl49DqfIyfjJpqT7XXxQJYIySy7Ss3Y8xoI0mtFg9AiEAjqTDfnY18Tbph9I1KgaMt7F6q39VbwxOsL8%2Fl7IMopIqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLd1iYzLW%2FYQEd%2F5YSrcA9DAaZ1EwYfDAsYOFWWbpN7dYngfi4Hr%2Fe7R519tsq0KwGZ7jdfK4ORrZq0XFYJfVFKLIxNZEjbRUJB5%2F6Fkr9YKqQBGKofJBNsV0EMQwmTg90REXPSgWIvjVhpUBAKCe81bHtIDKLnUMZPt%2Bh7LdOHzK2KzYqjEc3OCwKUPKb%2F8OVvk4nIkY1kZnK3xshgyzJjdAkAdO5yEZV4wD3kV0HXtWlQlT2GaA%2BsPmGlXbg4I2xYdBbG8EQSGjDppfkhzG5cX1MukmMPPSA1T8rADOG1tFWlFTBYukWQ185ZqdLTMzh%2BCpw%2FshBtP5FlGB38NRUj7k54zH8hPQ1QbV5yvvP3IigzQjuCv%2Bmrf%2Fk1Hj6YnmaOJlEhfmIftHBSj8Zo6g0ybbN1V%2FTBfDE9gJ964%2BBpP1q9lUgwKMJyUDQXMOGSR%2Bj5M3kGUgXfSS1aSRoqO58QX340WUNkruKYeqWjwDgo%2BXkh%2Fw%2B%2F4HCC6pbkKXPAhjBbyGim1XE61O2Qh0R4akJq9HCnHE0k%2BA4gB188masfGbsfrXVkq7bODzh9ImtCk42NFV54GGWboY2I2aU%2F7bkJZfda1b8CBCkAZGGPQ9IESb1xf%2FqokohZKaZpggBD%2BLUOEaDxFjkXCXN6MMPC0%2FL4GOqUBOhl%2Fmunk0OIFVB4r%2FRHe2WXFodYoMHmAHDDI%2BjiArTOCG6VAAmPHKf6kjQfvRkBEoDdID%2BUK7t2rZAzFrZ8AhU4xWwARwnai%2BEPoZPalpsRzQ3mHONFLwiT6RF6KoTYNtNgz%2BaXdqTWdWAy6hHD58lnE9mY31j4z9ySbrdqTQu85UpTKj%2Bynxol8qC7vyNeG2ivcs6X7RMYYlqDuF%2BjKRFIh924q&X-Amz-Signature=179a77eb8bf3af9327f71eedb3e6f8597f77746570f355fae71b3d5a2a064031&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4QOCZFQ%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIHOSM%2BwyjfdQ3WTT4PXxc3epX28EyDHK3SpIPJzY3MseAiAe9JtZ0tFdyYS1NmM3X%2FV3h%2BqPRANkNbx8EWZfe26dyiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWkZwT7md%2BxXh6EUDKtwDobQI82fgETSAKh0FRY1eIwC%2Fxiwa9uk7p7ADC7PozHgCC156S%2FqFh%2ByC7qE7dpqxEJogfsqLqd3DusHRL84shTc81DcRLhY8kTtHNlAL1qy9PuvuZD3vKZo%2Bp1WkwAdLOnjYUwj5pLZkVU9Ah1db6pbLD5DkW95JBiBW7NyMNcohfDKO1U%2FYF%2F5JpC3j%2B3MlOAY6lBD34Ww6StiB5hn8iy%2F59t5OxMdp5Tey8LRajmJUxCDFLrScBshKHoisrDaOl1e93XbW2DpKftF%2FLDxuDLt%2BV5%2Fw88tkg7%2BreiLUUEiLWWGnSJ09iohLFmy2KIcDNCVMmcqb14n12ARW%2BhbWpxXRClHB474R1B59MFnqXpA88x%2BOOU2nWQji9EJQxg5KCwEvAbKmip9CLzVG8A%2FnAZECAKsDjlew74gFOZhv%2FPKuYQFZBt1PukqOhlRmbCwihVwCNOEpQyYuuHaNnhhIbivxzlgrmUZ24UZmRc6zpRE9rL3pnwEOBB7%2BJIl6nllgjNqdRWb33Kmr3xFao2MVQxKwR7C4ofG88Ma3Q3VKMJf0s%2FsMwmQj8kMDGuLUEJIEGSIdWlllYKTcRN09ddlZEgj1s4zyoTJ0oVflWovk%2F0EaEiob61KCeFqxS3gwo7X8vgY6pgGDCf%2FFKejNuL%2FvcdKyPhpXi9majrp2qHdml0OzPonyTU21%2BaXGiF91%2F2weaUB9oDkJiZZXw%2BlM436PCaHWxRu%2BgyYglhZZR4LoIEJa8CYgFuc%2FiHhCKRHIlB2JHUPTssRwhdSU9MFZToLhD4mUuUnPgfXT1lQ2qbJeE7496%2FQLaTtFi3ZTENnV25g86DV6BERL8KBVPOa3fBlQyRbo79eEuEfozcil&X-Amz-Signature=f3ce3b513581fd1ed7636c9dfd18cec2463d1e2b197756be1e85c320787543f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3XE5WG%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDoYmAgxnjrq7v8oSx3eN8AZN%2BH8fCbD85KeOdIlc7v0AiEAyZnYjk%2BwylAqgTncDBC2b5bulGuorBTDR%2Bw%2F6yBqNLoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEq0F3kMjGiB4kIzSrcA3zbRmbhcrejO%2F%2FftRpDrmyd87kWFetdGfAmUvT8cPImFA4O1DfXu9%2BYaPsTzDSjnI4m6sctrmfVClqc19Pv0CZ9CKvDfmFuTSHVXFXWmM%2BRJyqpr5xavhL23Yw6AtSMq4eE6rF%2Bf9VgoW9Y5qPSt8Z%2FfZkGl1NDr8WfZ2u%2FM6ZnmOjLjFfFyHLS3S15KLeTbm753Uy71127AGsurvXe75gsxRbBfrNDEI6WL1Zq4TL2c4A3zJuRjJZh9Hap%2BPOc8tcusb%2FvV159UrHO7mdG1KOABhACJgX0CbSMJGfyR4Z8MngNv%2Fer5SAlvM77N2LzaAH9lJYR1DBWX4PV4OOLy%2BHM2r0bFfsFr0fzmhI0%2ByggABqNofEzLyeY6bTF6ibADi5C9x3%2FGN5vRzOYAAO1GsNEElx2TqWvUcF5sdNMWrE%2F0a7j3KHzsco9b4aJwIFDVmQagCaUrf8zr1C%2BW4%2FpJnf8ykNdsmTJJfd%2BYOHPWnaAbO1YoGW%2F%2BINLDwJT3beJtTjr%2Fn2eFIt9iUoi%2BDFtlOaHizUdUPC0M8C2TDH6CfiXi5m4k%2FaNxWxAEGzPEJsqXDmw8o04Z9e6ezb3Wou%2B70qXxEX6bWKLChHlggz1ieu3tdrZDk%2FP%2BVWvZWp7MPy0%2FL4GOqUBcSf4aROjEfA0tunwIAZ%2BRh0HHKfpg%2FAeGQ9knglOVI4ICWpOCQycoM04%2Bs%2FrwbuJz1ZahYa2MZ%2Fttp9arvhQV6GTaY%2BlxCPanUb3iSOuZslqMitd7SoLsaajqC9QpgVAqtZwcVAfD5rrXQzeTjN4%2Bb4ejWqcunnxWuQtfKjkPyiIJMgqWtKPc6sYUqmR5rlQENsbMwekugz%2FP%2Bs4GHH%2Fs2bc4q3z&X-Amz-Signature=8898ef0f43472734fa0c60ccfab20569e8293bfe6cabbcbe77f5c2b1062a611b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3XE5WG%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDoYmAgxnjrq7v8oSx3eN8AZN%2BH8fCbD85KeOdIlc7v0AiEAyZnYjk%2BwylAqgTncDBC2b5bulGuorBTDR%2Bw%2F6yBqNLoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEq0F3kMjGiB4kIzSrcA3zbRmbhcrejO%2F%2FftRpDrmyd87kWFetdGfAmUvT8cPImFA4O1DfXu9%2BYaPsTzDSjnI4m6sctrmfVClqc19Pv0CZ9CKvDfmFuTSHVXFXWmM%2BRJyqpr5xavhL23Yw6AtSMq4eE6rF%2Bf9VgoW9Y5qPSt8Z%2FfZkGl1NDr8WfZ2u%2FM6ZnmOjLjFfFyHLS3S15KLeTbm753Uy71127AGsurvXe75gsxRbBfrNDEI6WL1Zq4TL2c4A3zJuRjJZh9Hap%2BPOc8tcusb%2FvV159UrHO7mdG1KOABhACJgX0CbSMJGfyR4Z8MngNv%2Fer5SAlvM77N2LzaAH9lJYR1DBWX4PV4OOLy%2BHM2r0bFfsFr0fzmhI0%2ByggABqNofEzLyeY6bTF6ibADi5C9x3%2FGN5vRzOYAAO1GsNEElx2TqWvUcF5sdNMWrE%2F0a7j3KHzsco9b4aJwIFDVmQagCaUrf8zr1C%2BW4%2FpJnf8ykNdsmTJJfd%2BYOHPWnaAbO1YoGW%2F%2BINLDwJT3beJtTjr%2Fn2eFIt9iUoi%2BDFtlOaHizUdUPC0M8C2TDH6CfiXi5m4k%2FaNxWxAEGzPEJsqXDmw8o04Z9e6ezb3Wou%2B70qXxEX6bWKLChHlggz1ieu3tdrZDk%2FP%2BVWvZWp7MPy0%2FL4GOqUBcSf4aROjEfA0tunwIAZ%2BRh0HHKfpg%2FAeGQ9knglOVI4ICWpOCQycoM04%2Bs%2FrwbuJz1ZahYa2MZ%2Fttp9arvhQV6GTaY%2BlxCPanUb3iSOuZslqMitd7SoLsaajqC9QpgVAqtZwcVAfD5rrXQzeTjN4%2Bb4ejWqcunnxWuQtfKjkPyiIJMgqWtKPc6sYUqmR5rlQENsbMwekugz%2FP%2Bs4GHH%2Fs2bc4q3z&X-Amz-Signature=d86918219c4bb4a9db37fc7a28a5299f88806d6cea84eb5b170f6f0bc71e841e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
