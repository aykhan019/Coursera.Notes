

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=e3cc2dab0385cec653a0eab6235169b1c979102e5cdc046cb211f4636bf64fac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=f85eff9f997fd0dd394130f00bf954b612f1e937757eb17a17d1d94741ee1131&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=3f3e6fbb871497a363386141b74db4cd0ab4bdd412ae513ed002193848899306&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=e831b5a44efd347914d3b124c83f78efd8d3a0d5135fd087893edefd688702b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=3f9b58f6e13cc9b808118d0b2bce24a9d077855ece5bcc94f2ab4a7e78ff2242&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=2d83384c2321a76cc80702ccbed686818d749260aa7b5a3058c5759bdeeec1c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=9dca2f50dd5a596f775bf89edf6303ad6a92e8e37dbdc18752fb4352583767e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQJJJFS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtXzcFC1kiCAXXvPbNKNJ5JctwbKOxg4VlLsW4jXwdAAiEAkj30GAnzNj1qW59becUCL0K6RihZReGJYsfuMpRJFvYqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG6lsrvostnPKXLGyrcAzv5%2ByVj0V5ziTnfz9qdEl8rxgp%2BCaXm3EEwNtjCiuxrVTtOYK06jtIJfv3e4SjZ9illV2vmFkC2eBBjgFUvxwtoXbupnoDzPWY7kLVMpPmcHYEOnUH1Wc6GYdK5nv22DBY5mBwYo8%2FMTQZ8RJGnD5GA3MHI%2FSvQ5aeZe%2FH8ZnDLSJU1d7hwhDjuawLGFKUYHR1wrVoYCDQ8eX7b%2FeGy%2FJJG%2BlAqGYzfjveUNXbW47NDglUjjaOPHJj%2B%2BhDpgsEhD3qVsjmJuP6dDTEEBHDJvMutxc2%2FGb3tKS6loTdAuOotrQY48cLQ8huLc2y%2BrijCoUFarijpR0pHRSffkG3evxMtP3hP2iL5Vzur08nX59Q1Fy1woAdL19%2B2e07pPGEV0S%2FRhO%2BEW14gfm3dlj0QJ7okczS%2BK2qK3PCFS%2FbeJJRFvfaxjAwWPERLIGUZg8v%2BZZ1IExkQXfVPeOUPBc9tRFeJdpNk6k7a0AZDaWEFutd3swLpX8%2FbhG3o05aQ1xvK7S0nqEtM5iRkAF2zZdeudsm%2Ftd2PwTypRXwKRENaFz0acJC9hf2tPC9fYmQiLZlTyFqIcrnDiQxNzMs3S%2FUWq33rIt6oAwil1BlgPZUKXHvG6IrBwLO1bg9KoKgXMMXY6bwGOqUBZfAQjlxhYNS4QAufRRY39hD7oH4m5nheNBOm7hg5QaKHhmChIaXU4zaavkaCSvCuebI6e2i0N8lcQmgs65u6AWgtHRZzmXxEglXYMMCJB35XOak%2FpWeOID9b6l1aQ0YrLTp3q6iDwTKUUDpkYLAk%2BZYBhJD9uTn4doUQH6Wqq8SmGXFv48jf4pDmt%2FRtXeEfCpIf2XelpTF1kfvColUEDAluDvBY&X-Amz-Signature=08a1a32e0980273c3aeb77ffc3371dd7801a49383aee731e6536a75c50486823&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THDFS5HD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1HDcbNDDrxg6poY9t68chZkhsvSgCKAHQafpF3g0CZgIgenqaMUOZNL5F3g%2BrU76ENTjt0J711Hl79XPPFPeybecqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAWSBRKnzJefTObmBircA5JqWmLW%2BSLevNU8%2B2tD2FbETQXfilrMQVsSRBwJsRbKkfA0ysYHMSBC67CCZXE%2B9fQtPCkAU8F4eyB3JRyhNW%2FgEyHJyONHPZsm2N6jgblwKjXiNZYZGsUCAd0Q8TFMxo%2B740syoc8ai4fZtXMlGxRnCghcuYD2AerhaGC%2BT7YHG325JnzBc1MohtRyXUjEP5pj91EjW0IZqfZ31Suta1TgeBO3dnedf3dAvTG1pPZLKW6Lzb6qZ8xXyW3GylObdoopJ9hfFlZ2QHJKvXyAqapqzAG5Xkx8qis6641zOzqi9a9vq4C4Et%2BQ%2FX1%2Fdp%2Bhp8buclsQfxxVV799NoYmO72OtYOnsY576qN64U%2BB17caqo2maJQ%2BEZNkkn7C5BpK4qF7Gks4CgDRbZcyRkyreZfpGgE2cPcKW3ePfDSpz26zrphujUSz59ZFk9Pm4HKQ3wgtua0XXzr%2FBe4mdx0fsWqi%2FXB6HIPGZ5WNJCIjQCgTE0l2dZyxED%2B3npd%2Birqwn9uhYEyXgMKAHAoryIQX3dzkYHaRDh4M3RuT4gl%2FPt8eS9G8bzOY6B708nizrk2K%2BfnYESzWjPHQ%2FTyOwUnF751kRcc7JT9tKYYpwPyqfouWmG2vbqsGTr32RQg%2FMMzY6bwGOqUBL7cRMkZGY6fHJjq0DVVtUxkT9OWFMxLSwmOghypgMUfELzU41frzgo%2FvC3yDZAD5Trwt3YM%2FAI7Swdb0dQ7FcQTv4qOpvL9wXu7aWTdGlfVkwhnYM%2FLjA5pAMk7jZGRA7CmuiXtPrYZQd5uvi4OFa8QN3oT093gsYW7zaOrHfy%2BjSOGuG8Y1Kg3iDgI0L%2FcJWgYD52waytQS2jt5kUJTriY1J%2FAz&X-Amz-Signature=d7f8e96016a7e813857dd62e52c5053a7089d78e476115fb35cbea17a11db5bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4JDN6K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICbgBC%2FeSeWv2BWwziCzfG1diXDQijUkpkcGAoxC%2BVUzAiAOnhtRY5H%2BmwgphY%2BdASAR0nNQAIPzIupV5AKU2CWCDSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwCSTjO2vG5lUd5xPKtwDKpe6AbKYzuBBu8Y1uLRuP%2BaFM9kTuF3YaPJSFi1rl1fl5O6z1qvbdCuMuIBNjD2WHHpXhClwZiXwpQDrG0SNbryb8NPrFuSkWaegeC32w1zgYft8iQe2m5beCysrH%2FCsPWSMSj3GJ3IyEWhe76gwqukMUpDLbDGitNu7LMw6n8jyBnLIo06B2IZ2amo1uwBqiYecH0BSzvaNwKWdJ%2Bcm74clIrRpI8kNSn6YW9Ov%2F3e8cyHB4VZuact9nuak7rsBkASbQwtnDrGpW4De7PJ7hHNArOOov6Xcc%2Bwg9a3Deh67nE0r7FBK615C1v%2BJuWRfmQ7UGwpmqlePy2ASp25500NycG6Vjsm9jWJTczXaXTcvz6erWRAIoKmsVYYSL661F5EEIMtA0795rgXQ0uMKiAxFHsXxyPjI6tlv2O%2BYp2AYdke%2B9WazpEQ0NMnyHIg4CtliBjNDQ6tEEkMPsS%2BeSTcvlb3FyyeGS1vVVaHOC3D0800LaJVYHO7w0Tuoen02x2bu9KPhnEcb82fc1NXOqRXw2mi3rA22CvMGS5p3J%2F3vh%2Bb29vMqHBXeXMlL9pxdtYK8ixZOyWOVCiy5mj7PTzDI4b%2B4exYdmcekWQgNozkKZgKTDcNubUrBRsswstnpvAY6pgFlPHodjSpk3x8g%2B%2BWfGSt13sz04KWSAQYdz9xL%2FXPNN1AE8Nd0cKwCRNDulUtw2ffX%2B0oaixCOxNPLEzA8cVWv8liLPZ0Y%2FxKA1T4U2%2BZA4WNgz4%2F8G3qx%2FdkuS%2BZYsuHjJK52SB2HUnmbQviJFsqXkpm3ZxoBFaiVXlacgQo%2Bw6YTOt34slHe%2FbQskYb1o3TyIsOqm7%2FvQ9VxzbtKUxQCV59cPm6g&X-Amz-Signature=132f949d868a1130f82a6f6415bb6983464f96db3f7aa173202acdc930754f9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IXNAS27%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAH3IsccZLMUaWZSDFIg2EbEUtA016WezGwx1mWtCRiqAiEA0X7IicCDU5%2FgmDfv%2F6tB3kC47XJuQ7LjgWOlYks1Fv4qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzYdR2R7UzEZPbVjSrcA5VVio28Our7N0u8i3zvkCl%2BbfGNFNwnNgQjfZRH%2Fxk%2FBbJScn2FmxILSbETEIfXmUHe9GBMMwUToP%2BVrEwdz2UIP1mTwvF74%2Fo44A8fA0KnHGJ2UBnKhS44yAIvqslGZN0RWvLZYHL6kr0IkfA6ECeQCcBfMT95A5QoXnJYYeiRrHddBMijbiKDs2dRv%2BxX%2FnpccfZO1VmZjTp3Ff7Q9mn6b7D4H%2FBkivK5fvWrSdUHziLaz2S8i0TyRTASnlUDpiN70cp3vPRuRmyTi0ApbDVEAYqF5elXBL3y7LGR7dXsUUc0qz%2FZCQGxvXLhAsmrPJb%2FSTE8ARo5X%2B62mTDDqNQi10Eaj5wtwgAunhuCH3LCvm28hlPFZSNlvGzR2nGL3hjph6glbe%2FMb6A65ZQ3oe5ZkK%2BypFjH1ECXjdZspLfkN0doNH50qdM0BB%2BFbIJleJXGHEcJWjkfdTpnRatooaDIlqSCBYUKAQFdo4ayT2K%2F2Z1pyXBj%2FNly6CVylIpc74wEh1t06domj6zNtdjRoSos%2Be4uhyutO%2F7pnpxMErR3L77teJ2xhYPCePg5Dg4QwJE%2Bl5oAvv2KhfJKnhlvBke5bMax3ByBirQo1gz0jWATWlgovL%2FZ7ISblnPBMPnZ6bwGOqUBlCFjuWN7FwTCUPiHqzyGQiXJwN1gskBMXhv3VTo6Z2syqTEh1wacxmeVcMopvBQCnhOila%2Bt2hG6cyeO8MXGqI%2FYQkdSHRmyrdo2ekqO819%2FLUY0zI%2BwYp%2FsTDYLY6Wa9WPbVuvEr%2Bp85iaWhw3e%2B0sGH%2FlVnDCEesJ1xne5COSqE9hIPl1xJofoya3ASGkrx5ahAXNzJxbsAe5YIFqqwhqTAqa6&X-Amz-Signature=215714b60050b25d48b65a4088284e6b46811b1ffa776bc67dc55dac9623078b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IXNAS27%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAH3IsccZLMUaWZSDFIg2EbEUtA016WezGwx1mWtCRiqAiEA0X7IicCDU5%2FgmDfv%2F6tB3kC47XJuQ7LjgWOlYks1Fv4qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzYdR2R7UzEZPbVjSrcA5VVio28Our7N0u8i3zvkCl%2BbfGNFNwnNgQjfZRH%2Fxk%2FBbJScn2FmxILSbETEIfXmUHe9GBMMwUToP%2BVrEwdz2UIP1mTwvF74%2Fo44A8fA0KnHGJ2UBnKhS44yAIvqslGZN0RWvLZYHL6kr0IkfA6ECeQCcBfMT95A5QoXnJYYeiRrHddBMijbiKDs2dRv%2BxX%2FnpccfZO1VmZjTp3Ff7Q9mn6b7D4H%2FBkivK5fvWrSdUHziLaz2S8i0TyRTASnlUDpiN70cp3vPRuRmyTi0ApbDVEAYqF5elXBL3y7LGR7dXsUUc0qz%2FZCQGxvXLhAsmrPJb%2FSTE8ARo5X%2B62mTDDqNQi10Eaj5wtwgAunhuCH3LCvm28hlPFZSNlvGzR2nGL3hjph6glbe%2FMb6A65ZQ3oe5ZkK%2BypFjH1ECXjdZspLfkN0doNH50qdM0BB%2BFbIJleJXGHEcJWjkfdTpnRatooaDIlqSCBYUKAQFdo4ayT2K%2F2Z1pyXBj%2FNly6CVylIpc74wEh1t06domj6zNtdjRoSos%2Be4uhyutO%2F7pnpxMErR3L77teJ2xhYPCePg5Dg4QwJE%2Bl5oAvv2KhfJKnhlvBke5bMax3ByBirQo1gz0jWATWlgovL%2FZ7ISblnPBMPnZ6bwGOqUBlCFjuWN7FwTCUPiHqzyGQiXJwN1gskBMXhv3VTo6Z2syqTEh1wacxmeVcMopvBQCnhOila%2Bt2hG6cyeO8MXGqI%2FYQkdSHRmyrdo2ekqO819%2FLUY0zI%2BwYp%2FsTDYLY6Wa9WPbVuvEr%2Bp85iaWhw3e%2B0sGH%2FlVnDCEesJ1xne5COSqE9hIPl1xJofoya3ASGkrx5ahAXNzJxbsAe5YIFqqwhqTAqa6&X-Amz-Signature=7482a843bcc6e6fafecab898b469c08a8bfb149ad75103f1076f1df5d048db9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
