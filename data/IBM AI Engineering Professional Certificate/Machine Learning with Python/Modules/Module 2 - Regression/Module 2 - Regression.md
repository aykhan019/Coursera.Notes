

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=0d28368e4b5c792a7b61995a232e33e0e1e83b13bac8067afe6fd842c8f245c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=22a2780c130330792b14d11c8c55cd0f50406174fe78cae7fb2d50c0c1763da0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=3545e3934fc4e95e9f55acce347fdf1d315c567151ea3ba3d8cd705ae2801119&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=7d040d678b872ecd7532ebdbb7910ee6ea2101b40932fce3ef523cf220f3bf21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=60a1a7260562892743f3c554e3e691b9c6f9a984b796adf23c7f84d8b88425e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=56344fa224a96c48ee691eb8da001b8175457c7362a322bc34f982bc9e55a0b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=395a09f3526cc80ca99a58484350557801c05543dea2ec6d4d22795628d88db9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFPGIYGD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFefRxbMo3eUVmrEXpDUrp5%2FuHvuIaMk7pJRGUmtfbK0AiEAm4ilyWZ7GFKGBAEOVhBqTdbtOWf%2Bm7EZYAbbgiEybzoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BM7%2FFpelBz7ZKPDCrcAyhLxhIihfeyyLKyaLjBY2fnJQd61xd0b6RKsr8xCi3YMh6thPpHxf%2BXwp%2Fd0R8rrT%2BBWEVxgqNMPtMVEfwRTEruCRgNm8HomMsK4QVef5jiyO0ITI9ULsxSdZMdxFaCgyxgLIq2etq6ZWn9bOKp6giQOZvrITTReLH401RklJiqsWNoTxj%2BjikWKdxBacolp2chhgumhpKJ8IjGtXDm8Hb9EX4wyXquxSHZp4W0wS%2F36lnw0mQr97Ebj6YCFuR6aCK0QGChP5mLz6IGQfpuMbHZcz66mWrEmfmmx2L3ZJxpQHwyeU6yHTmhx2lq6qEUqSIGEr28zSCMMdtk%2FYZW1mTrmhVX92ig8z9kEHQ2DdgFI5gBAxXpV50a8l%2FZaRY5QA6JY5fk0BoMpD11MLhD%2Fi251UD3kp3wBI%2BP4WINH9sB7EbwCRPmI4GR9kdkdMV7Qqq0Rk0iULPvCcKqJj4BPWJzhhRBvJlFBY3WXCFhHfQn%2BCqepXE%2FPZ16V0tAffPxbgE4wz6BIvcFTpmIxFOufVpgIU7NVKrs06O62CRTps3Wfrs6d%2FJnKMmEwDIvehCR9e7lnrZPF2lq7ubHnCEJJgt7h7ivBvAU%2FH535jGKN5GBrOHi0%2Fn5NR%2BtUIjUMJr08rwGOqUBRFJyzML5PPscgmh0hRMuqdfrKMN1%2Fh%2B%2FVWxmNXXpoNwMpwK9%2BVV56Yx0En7%2BCQYWNRaceM764iYj5QYtz2ule04V%2FVTOtdQ2LLkgoTRzrhoY39TwYV1GTx6C3%2FJFK7N8p6RjltEv3ijNDW%2BcT38Zzo%2BXOILyM4ktPRZa2HJKedQGp%2BZqBc7twf9BYr6LvT0bxM7CiI%2B0HSmlZ7MIlZKk4YbsZjfu&X-Amz-Signature=882627a2fcdc2c0c3b616d2fa3f85e8208ed95ee7d707edce2804877238b3b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4YK2L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEiTEHmIxhvolT2%2Bhw0gjQ3HBob9hwCqSR8HcXJUgF9DAiBFBlxmmKRoWGucvwzO2m55AvlA5ShSFezLnDxhPNelfSqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeIhVLyxxt%2FyJR6B9KtwDhU2MxRWFLb9zulTuJSJQfXjYCQY9wZ2P62h%2FPb32nRRCY4ZNy%2FBQP5rgJVUtgluamL1G1TQ%2FgG%2B9yvUS0VJZFiby7zEg50HfxP23xCaNDBv8VunbWAvryARH%2F%2FnzT3dW7tr8iowuuiEYhZcMtuBrywQ0ge3Tz%2Bk6EYlx3qp2vjs5%2BANTWi6B0o4o3rqlthc0oajEa3ecVJyqaP60wiZdt%2BogZrKDviqKcVvwyRKH0rmuU6J%2Fk1oWWKijqXxwhOz6FE29zxAwxCGAc6a2dxynjW2tZBokUFkyQiE5o%2BkOTCaoZfAvu7dhRDrfSan4CgoJzQRwVIcFLUNZLAx%2BtRSUlM2cI5kgI1gyGyRM8vlYBqPVs0oRa9R9LQb3Jj8ac3jO9%2BR6v7Es4bRZjNPCvuZUbn2r0W6N9QrWbqJ%2FW6zKMNNlgnnyWVNT55Oq7JHpIj7CW0lFjeAS69hr%2FqvZUPykvxWb1E7%2FyjKUiAxuIFXqKn6EZt3Nmm8V%2BYqY4bFwVR%2F1ntfe1rutOcmssXd39kzQZlbGiXG6ssqzbMkoQnXxtLeYjL3ZxpP0w7RAXbj5qeGGxoEGfr0HzCkgbhN%2FyylIbFBClqGrKssrGhDNu1bctkFsBzidji4q9mIBe%2Bkw2fPyvAY6pgFdYjIYbS36ObStCDdBCIvn0B2IY%2F%2FI15ggcTy6ZD3w%2Bu27LCh50yitwEunwUd0UTnkm3Xcgf0b5TIUJCPsOrwsAAuew24J%2FBwh8E4ml3x1tk25p1%2FKSILEdLhJsZLy2DTt7HY7gldrpTFooFh5S0ku1boArdxbVt1Gw85T4iuJ4I0pzqaptUut5u9rhk0hynqP%2B2N2ezvhjGZDbYEZWglO8U8jVli9&X-Amz-Signature=310b61985de843afeffc833969f84c78b1a51d4779b3e5561beb9efe4209bbc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466226UXTLW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHDA0854zfgSmUR2weqDpL%2BFNK78NNV6JlZ4WjoBFj9TAiBiPVVbrCSCscLWFm3UE4OwLkRChRlOWYE4aXqMKAm%2FaCqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHg2OIySz9DfZ4i7LKtwD41xfCp1KqWUGSFEiM53IlNd83%2B8u3LaflEfSi3u0hCPP%2BjX0y8bcegcEPfFcF3gM2akKjSfUebbaSrfEpmZ6OkuDiw2jH%2FD79%2FPnF9ztNHpE29s9UDj5aM2U3JlCyk%2FfiD4OvS8FKVriTwKFI%2FspciycJp1VRNHpKgpVgJcwto2ySELZmBSqJu9BAMx2NFHGISXV6SP8ggyDrBuGzPkUAoOKEt2LTiYCOVPfTJQo%2FHTZtQsXVGDzscaCzWXW1WuiT%2BDCV5madAFmyRKmGwTmGXmOT2vvnr6BVVHKZ2GpSGrgcRVFI8ObaKDSWjC0KEJ34Zof10A6hFrDrRPzcbunArKqNeVBByeg%2F7tC%2F6iSYPeD3SFkzKShMNgNSU2%2BGQG%2FQmEWFXlGt%2BnYerAKI46hJekBqhtrTD%2BqSZf1smdRMdMvVMXiPnsabG1FK%2BUCPw6RkHoX7dbBSvtEFthz42tg6pnG4mBeCtsRY0YZJhN%2BjZOo9u%2F1eYlPxV3dU4nmN4WczuBfUQSprICjm%2BrChfUkZ0GYJsrZ02PV7yAR%2BwWGWcsJQBwwvVhTkKbum3JzKi3SgyabLV44Pcg5M8vmNbQS4YYneVFRkzny1HVMBxu09%2BS1WXv4no%2B4VilDFEEw0PPyvAY6pgHIqxd7aSOYU%2BDs697WAUN%2BS67bTK9ogmHe1CEWiZyFVQtWPFWe2ngaGWOIPzuaFnYnNMtFNjWlfWXnBGpZSmBSNCkx3hBzNHB%2FY9JPbiC%2FWu%2BlUkkbykjQf8B1bXtvKLzBz50B3U%2FU%2Fdvb7OFgqs8dD1HTrg91%2BMg%2FrVKr4KVJjaX%2Be67E6s%2FVPH2Mq2QmMLRZI8bvJIBSeQXsvmFGTEpoRU70S61Y&X-Amz-Signature=04bc26a669fda87963b2fa137ca6ec178674cf0054d89c71cdb3abf2a9489f75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSRAIDUZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFYTXjg0HyVJ2tKWSUzX2FnfMwVuiLiizxY08X2knJufAiEAltHm4koM4SX6PKj2CiP1vxw2ZcYCKXd3w9tUDPGqPRcqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz%2F76u6vt0ImPU8NCrcA%2BIP9X1yy%2BDuysKDHUYDdjHSMgDg%2B%2BGFlIVvgQG9LYx4GpVC1lnvef3uPS8yvM3aY3SL0siZ4LJgONVww%2FWnruTHN4DRtN3NIolFxW7HJ0X%2BszGYJAgwUpXaFMoPqKcrxVeiMx6lwPBdzioatBBlQWuA%2F891mhacxGukrEIDsev94JUJQ5%2FAago%2BUaFWYX%2FGUa9zi4GI2Yb7aWoLSn9NBVprZ3qtXG%2F7NnrtboXPpsoUYBhru%2FIknPTG2uQy7%2F9k6XqVzHqkseuX%2FiB1j6cp1MAdzk2frSi4WRnL%2FW1tR%2FxjGG3ff0HCeF9F%2FO7eR3K89ShC%2BWju8edXfX05IEvjt5j9Ccd%2FNjZoJhU4VMEaZKIM3l9YDI9H3M2eeaD7TgB0%2BZfck8VPi7kt8f9micih73LIOBfqpjW2i33tTLIvIpzgkqmEFwTKbrHU5LDR4NCIPwkuvTS2iz4%2BOCWAyH3cvq%2Ft2WoPrRsDY3quU1JMybHb9ifs2Ce1q%2BFXdKBaBpESilN1qrCoBkIjPb58iFT4QJDyqOanppjEur5h%2F7HuyLyGcuaIDte5DHlAP7icC4X%2BCO58qLYYo83yBKlK%2FKSvIDrt4UvCaowJ9gWdw1qkO4gwZYM%2FtOvF9zx9I29FMM7z8rwGOqUBLgOrOcehF3%2Bx0bt42q9dSrvd2jttCIvT3k2YuNI4YrgokU5q6WcOE58Ekbvo1NB6Fr7VQx%2FOEN%2F8lFlub5Ubo85h2w12Jvr7%2FXUVPkNgTvlLDf7Xb%2Bh7rKQk7vZTVdb8xJX0uFRxdWaB8oUNshtaXZtbjcx8b54qNPt3UNeOPVXGq2G7qRfkUWSGybX9uQG2N2ivbCJJ1MUhjiKfFiJRKd8W5EeY&X-Amz-Signature=61f64aee491b3289a27d6335353006b7c46355c68ae496d9bad2abac1ebdee75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSRAIDUZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFYTXjg0HyVJ2tKWSUzX2FnfMwVuiLiizxY08X2knJufAiEAltHm4koM4SX6PKj2CiP1vxw2ZcYCKXd3w9tUDPGqPRcqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz%2F76u6vt0ImPU8NCrcA%2BIP9X1yy%2BDuysKDHUYDdjHSMgDg%2B%2BGFlIVvgQG9LYx4GpVC1lnvef3uPS8yvM3aY3SL0siZ4LJgONVww%2FWnruTHN4DRtN3NIolFxW7HJ0X%2BszGYJAgwUpXaFMoPqKcrxVeiMx6lwPBdzioatBBlQWuA%2F891mhacxGukrEIDsev94JUJQ5%2FAago%2BUaFWYX%2FGUa9zi4GI2Yb7aWoLSn9NBVprZ3qtXG%2F7NnrtboXPpsoUYBhru%2FIknPTG2uQy7%2F9k6XqVzHqkseuX%2FiB1j6cp1MAdzk2frSi4WRnL%2FW1tR%2FxjGG3ff0HCeF9F%2FO7eR3K89ShC%2BWju8edXfX05IEvjt5j9Ccd%2FNjZoJhU4VMEaZKIM3l9YDI9H3M2eeaD7TgB0%2BZfck8VPi7kt8f9micih73LIOBfqpjW2i33tTLIvIpzgkqmEFwTKbrHU5LDR4NCIPwkuvTS2iz4%2BOCWAyH3cvq%2Ft2WoPrRsDY3quU1JMybHb9ifs2Ce1q%2BFXdKBaBpESilN1qrCoBkIjPb58iFT4QJDyqOanppjEur5h%2F7HuyLyGcuaIDte5DHlAP7icC4X%2BCO58qLYYo83yBKlK%2FKSvIDrt4UvCaowJ9gWdw1qkO4gwZYM%2FtOvF9zx9I29FMM7z8rwGOqUBLgOrOcehF3%2Bx0bt42q9dSrvd2jttCIvT3k2YuNI4YrgokU5q6WcOE58Ekbvo1NB6Fr7VQx%2FOEN%2F8lFlub5Ubo85h2w12Jvr7%2FXUVPkNgTvlLDf7Xb%2Bh7rKQk7vZTVdb8xJX0uFRxdWaB8oUNshtaXZtbjcx8b54qNPt3UNeOPVXGq2G7qRfkUWSGybX9uQG2N2ivbCJJ1MUhjiKfFiJRKd8W5EeY&X-Amz-Signature=d25edb2f5cd174a2d23f555a1b8ea29470560a6b49483f0146847994847ddc1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
