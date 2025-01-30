

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=0ee83f1c1f25e26a84ae88ae3b1d66b05bb7c18da8d64b08a52e37ef8da3388e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=a10654066f87c74ed8d72366d4e09ce1aee9e7933f88ebb8b5d1199c79690f45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=a0476a983b2ee66e42cbe00de48a4625ff7bbc96f616ce1fffcd16ecf7a1b8c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=907523f1a459058d682c4ca66eeb231fc03e2d8b4a4197a938aad7c8ca2e90e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=529eb88fc4fee4f92a699cb4b0a8e65a724b44227f592e29e843ea6f07cc4ab8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=ef59cf41a53d503d8eadf5ed0031452c0e1255854914722779818b048a9c4d63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=eaab99c7c0564fa53a89ce1f25b14e82660f1eaa0c7f512d1235fdabbc528b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662ZGTUA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLfnnDMmYwGlJgYShbwkNL%2BzyU8ZUDiL1VRRZnF%2BhEmAiEAjMMKXEoCsaQQbsG9mcj9MHJmicHoUxKy9ZfZYYWMLa0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeb5%2F2NZxmzHFE5uircA96rGYKnjv0Sy9mFy%2BwlSU9cBNgevzbU9a4zPNjTBeXRzHcGxWzPi%2BIottzhOz9rJVzjx0qi7chFMC%2BxRVPYnMcWMTUd1bFIMSDQemp5gG%2FL9Y23RDoLR4rUrg7i8gVQqREubtoMJqJaxxHT2%2FTaRF5pDjmEF%2Bp%2FRNC0COS%2Bf6EKJimzOCwaTECLsUmKzNWWEZmJ3i0gSe38AEOTbLX6g6cF9aKdGoYvyO04XSg73uJq6sKbHjuX0dwHJbLaqjrdNDm%2B%2B9nSR4m6JFRbxf6YVcfEFBivO1FC7bb9Y0x6i%2Btfgu7Exvu%2Fx3Fkdu1ewrPNOWRxHovv8ixsNeoiOOZYfUiIXSaxZLLZMpndFElN6bcuhgt5uGVUDz4ERVok6n5U1a4sJSOwUkx%2BVwO%2FvLnA7YhaJUZecnqMxYV%2FEOOqBXhenKhFtr%2FtSWNwv%2BTRW4qwPZDuhAc4ibGz1ldFlZnTs3rJ46CWvcm4ImZWk5NhIN7uniYk7ah3ocQW1pThBtdn6olvRtGRJSLElvke4qFYNl15ECxXM93GSwcdO190LjqNEw6p43cSReTmu%2BrmcJF%2BPC1po7CnoFCtY4h%2BjSoE83ahSRIBkjI6lXswPXhyLUTTozNgb%2BlYrwTy8KCvMLze7bwGOqUB88noHktlxC5jCTPhnskVWhVAa2p2vGaLDjFjss8qRrDGoLtKhtLvo%2FeeYLVCwzQWKhURkKdkgEN1rw3vgBaqHeRoliCBjioougkbI5SsnUmqvaKwJr4wRnxMh1tZT%2FVNtRefFMcTrWbWXnU0CUcPabGGpy1xDAjd15TmpDE6CTO%2BeD11u0Vcrq%2F%2BbXI1u9Yy09bafNJN2ehlYedGkSWOqs2s2rCJ&X-Amz-Signature=b5e8321c07583a409912d79b2a41d57f43dca04a85acf9d9c83f17eeb4b66512&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRH6ZJUT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxTBvGhlW8t47R11gkGmwxRMHxsPnaVKwSUTRqQdcePAiEA7mOAyFIt936LD1sxjCpEXwhYuVC2hZDctV1cIsPFtrwqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEgoXDV6Hrf8LdMHircA5W0ABrNkR80HPx5vPDFqpR0w8Rufdrw%2BquS945cvV6ug0F4J%2F9Y%2Bt7mQoXMr%2FJUZZYoUmPa%2FjUUHE8pRLsmIAmqqBWEP%2F6e%2ByME8gg7377nrBxBO%2FZ1xd09g5OjkPh38pcziaty%2BAHZfcee7obGfICyb%2BT4G4APsv4HC%2FTAmzKoQeyvxP%2FH%2BpPDiatpA%2B40zQY9qHebwVvfLAl6MjcAoaer878tmuCfeuiJqASWRGIpo1hpvBZaL0h9YrXcn7pIK1eqo%2FN%2FuBirWyWxwZYVWibPJ1cHqLW5yWW0blpWjVcBBR1%2F3kllTLj1gga5Vtjw1rqwYcB5WrIupQ%2Bm9i9uIFqf%2BWQeqhk1C9yQVUGsdoVnRTYLTff1lCPTn3XqtZklVtjdo34pp7BN5puV5P0bcRmaoIt83%2Fy4boOWyRL9oexaQBt%2FHFh4dCu5TNCnzFYM3euGyXdYCBSPue%2BgKGDt6yPOCBpUQTiNDWT08FOQL8bDIlsPTJo3agL%2BdDK3FG0fU5A72B2jjKQPW%2B%2BYsx85QuLIOMGiqgIm8sNI%2BgFS3KgoihCE7ixr7V0JGcjfispcrl9W0Ga%2BNDQEwl5BuGMuGtcI0R1zAktz%2F1eSK1qRg%2Fwhz87VkV2cSl2%2FzpmiMLLf7bwGOqUBuEXn3af%2FbaJVxeadgo%2B5OjoomRVP%2B3PePJCLqvDs0evHXyogeJui3CiQzXu7BivW%2F%2BAJkjh8y5wp4SGqFg2jQIlASTnW9sysvQr%2FDrjDv4EoWrimBrXefiE3klS2vVHGbc%2FrIzuc3W3IZEYhOAgM4sq8IqhdiLQXEHmIbVB9J6JFXvJg%2BlR9z6%2FzhURfRWtuK2PjLV1UEQwyupxN%2FnTnu6JTRQQM&X-Amz-Signature=b3c148b2407d5def8d1bd86ec3f3dd57736e47a36f91d0b4be1548fd1d76f3c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKH32W65%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxWs1cHNpLPxmlKe0028FIsSVuCFl15VkV%2FFUyjVcqFAiEAqZr%2F7J2Z8wPlicx3VpmLy9xKvmnShCPHkUxJC3GC2HYqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCe6I7Ejg2FXnTwZcyrcA3lvGRFb2C1EfC%2BeY8E6gBgsYMzU3%2FpiW1WxhhT2s4rU9QcLBzqrJYjaBHg0Mle6zTUPgZINqbx3T57GiTlI735DjOM5AoMhZyZoxROgbcU54rZrChYfP8b15brqQTLHYHgzuA48FO%2FZWB8d39bJXqBRqXsNSpzxv1KWX%2BaXuzxuFY60x%2Fnv89DR2JSZL1MnUqmBFwyeWwASeSdRr%2BzItK1vrIcGXe4x8lBXLubTZFjrkdZImJughulcXYugy2lJphirsI9AsjhJVmttkROtb%2FTUjZ2p0HbwBdQO%2FXY7GqCMC5x3f3qKFwa6bTwAaLYKag8nRYuiyhOdvzRTApZxUdhSco%2BSVaVQzJpvT8XoGFY%2FB4WkZWowRUVQJuXK5%2FkVXZNZjmW85fCF89unbgJ0QkHycCRd7EkeLGxAzrGMJLYzCPibvdR0uw3RoZO54j7UNpGB%2BDcuuJZZXRRBY38lQSgJLwYBMlhnR%2Fz4u%2FyWyOBM4rNpbqdfRqZ9ST7nf0PSyDOHvRtGJA1Yq9G4cFCZ3hw2mSMztvA%2BI%2BD2mMXKWZ7QOLqTp1zEeFuJ8xFjvdXCIyZerk%2FkfQmtdqgzEOLHrkoeC4Q3NUNWQnxE8cIJXeaXdzU084bZjFk0xVESMM7e7bwGOqUBvLPfwlyLg81YiIuU8aipWo1HITKKGw%2FsjVr8%2BraL9iP9JSf6sfU1SWLUNErHtjpu%2Fbbv6YgSV1UPiaP6jHhEywC10WG6hB2osDmZvJEC2BL0O7FhUJvamuXp%2B4qxCjmFmknb%2B0hzRZbvCxMMI%2FzRt%2FgSZCWcAVECrz9HD7TvKqAiSicK%2BRHTkziBekZhgR1c9fd1bqz0pZbDCIUotzDSu7UxVXNL&X-Amz-Signature=bc083d334597ffa061788d382c4c65fb4d1436fd02ae95c584353cde8b67edfd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTU3FIHM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICm5VQN63SQmA0H0vHNngJoSs9mRsVN2eU6StX7vX%2BmYAiAeW%2FFPihD7yCAD%2Fh2EFJWqKAkge2kl5bxlvF2myJ86biqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuvJ%2FrnDvtrbos%2FrKtwDcEc%2FuTp3c%2BIqLekgrCLHkZupjce3JhyHxgGu5WZwKul4FiRz6GdSIvyrAEc4lgaAkPlO7McfbLr2NBB%2B85SjrL7cuv3aD4zODxMcXPUxAk7c354T%2FCTiglv%2B5aa04Z6hi1CKDawc8o4b1CXNqZy4KjgobN9EhvLefdp7qXPp3PmcYL5brjbJrzUueuAQdsSYOMV7mGltyCtSQawjYBod1b5pXNJPzwcyDwcP3OG3FC2iiHtHfhYCzkduuQ6GYlTfSTcnm9BvCYqiLPB3DsvIVRqefpVaPfjs3u1PIcJIqfvZL%2BOshBd6XXObcXQxtzvI%2FWJlfJiE0mPugztW9KKfq6s8eq5Y0Ay0KJN1ieflIwlLeWkzRjV8GBzHhNCkDJXGfjKfY%2BvvJfsCGEp%2Bje14NQhBNXE8GFhvWmPR93CopIqDiCNhR5WzXwhIx%2BvD9hDJonW%2Fk%2BlmGHIxUumxEN2a2VNTUNQDIPOOu%2BDpVxgBimg3GMbOZ8g%2Bs3hdyBUZLWSejVQ3j6T5HV%2BJWFCpH9aPXNeDf6HE2yqE9lFpqPYZrUzRcgQLB4UVBi%2FHS5v66rlPsKf2qxC9AXQnK%2FzClu4mIGokKcgSb7Tr2IoaxZi8rOz0UcO8w8UM4bKzH9sw%2F97tvAY6pgH8Oy4AiRtbH6Lbbxb2jYG3OBnzJEIMOhijlTXi6lTyEPHHUki1CADVsja%2F5yo1hKAwo1Vs6HKRpP5u5kBbu%2Fwzrc06i9x08ilrN9ttjZI6e%2FEVWtMua2SgD2vMdXae8YYdtQbQOLbN6X0WJx7xsrVol3NkQWfUlQeLpr4xxOA16SSBHUf2MBp6Za9SaOWOGSLv9xxng%2FZaDLpFSYoakHos2Y%2FYRQZ8&X-Amz-Signature=a5371d138c4e12b1cf1f610ae9369b722f941d51427f4095f5745575842557c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTU3FIHM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICm5VQN63SQmA0H0vHNngJoSs9mRsVN2eU6StX7vX%2BmYAiAeW%2FFPihD7yCAD%2Fh2EFJWqKAkge2kl5bxlvF2myJ86biqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuvJ%2FrnDvtrbos%2FrKtwDcEc%2FuTp3c%2BIqLekgrCLHkZupjce3JhyHxgGu5WZwKul4FiRz6GdSIvyrAEc4lgaAkPlO7McfbLr2NBB%2B85SjrL7cuv3aD4zODxMcXPUxAk7c354T%2FCTiglv%2B5aa04Z6hi1CKDawc8o4b1CXNqZy4KjgobN9EhvLefdp7qXPp3PmcYL5brjbJrzUueuAQdsSYOMV7mGltyCtSQawjYBod1b5pXNJPzwcyDwcP3OG3FC2iiHtHfhYCzkduuQ6GYlTfSTcnm9BvCYqiLPB3DsvIVRqefpVaPfjs3u1PIcJIqfvZL%2BOshBd6XXObcXQxtzvI%2FWJlfJiE0mPugztW9KKfq6s8eq5Y0Ay0KJN1ieflIwlLeWkzRjV8GBzHhNCkDJXGfjKfY%2BvvJfsCGEp%2Bje14NQhBNXE8GFhvWmPR93CopIqDiCNhR5WzXwhIx%2BvD9hDJonW%2Fk%2BlmGHIxUumxEN2a2VNTUNQDIPOOu%2BDpVxgBimg3GMbOZ8g%2Bs3hdyBUZLWSejVQ3j6T5HV%2BJWFCpH9aPXNeDf6HE2yqE9lFpqPYZrUzRcgQLB4UVBi%2FHS5v66rlPsKf2qxC9AXQnK%2FzClu4mIGokKcgSb7Tr2IoaxZi8rOz0UcO8w8UM4bKzH9sw%2F97tvAY6pgH8Oy4AiRtbH6Lbbxb2jYG3OBnzJEIMOhijlTXi6lTyEPHHUki1CADVsja%2F5yo1hKAwo1Vs6HKRpP5u5kBbu%2Fwzrc06i9x08ilrN9ttjZI6e%2FEVWtMua2SgD2vMdXae8YYdtQbQOLbN6X0WJx7xsrVol3NkQWfUlQeLpr4xxOA16SSBHUf2MBp6Za9SaOWOGSLv9xxng%2FZaDLpFSYoakHos2Y%2FYRQZ8&X-Amz-Signature=a019625119028f20c9001f5c60f1b1901457a4768e0820ff86307d92aa5cd8b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
