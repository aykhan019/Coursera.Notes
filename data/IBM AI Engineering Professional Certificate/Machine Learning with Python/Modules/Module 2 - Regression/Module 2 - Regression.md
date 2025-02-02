

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=91a2f1dae8efa9cc1caf0d7b1dfbffa7ccf718a6bb662fca44f5b82f549c3734&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=635551ad51f96d04faf111a5342d989c97d1a6a58d89aa0b9a1fa6ff65e0d2a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=f8ac0e7cf1916abaadb3bc7a46fac0862cb7e5342a20e50007b13ceb7872ac66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=607fee6690127abe9b71bf5b83a471ab1cc8c9de4d3fa173fccdb059fb805b36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=b6332724650ddbe95a9ff851ddf718166deb7bd054b773d04c2483a0381b95d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=8ba4947f23cfd35da9413545bc9a62c5d90300c7ab7e68dbed0d52fdc28d13ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=ced1394bb1b8e4c4672ee32772e7b9677f4f1638e33e12083c11a07bec121bc8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=b4c6472d18caca27a581c8160400fe0333ac4caca04b94dcdeffa8f47f85221d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6UF2R2G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2mdGRgtDf2BzOd9Qf9NmKufQC2eaSc0D8uj0CdTXf%2BQIhAMpuA7qfVCl2tCHakdUTmT4W%2FhzdHpgpCOHB824AkAyHKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlRAl9v%2BsatD9AwU4q3APVq7Eif3j8SsyT6paP0vwWtaZMg%2BkCU%2BjOFCTK1KJrKxbHJTKobqqyoS7SmygG5SUC1D%2BMSJKyKqvxR%2F45Dun6A9cdCxzMCBcZzCAmLsHmhmLe66NIaHb65b9KW2hYt1SCRoyUd6osXmdF%2FrjaM%2B5zEU8LAl%2FQF7l%2FTSPwgD%2FUq1ZGPU7vyBPkSNM1LNtSUuDcr2n3vXx58DjqQc8LX6aK7OVlk8irk3T9rTZLa%2FTuSyASlEu5fln1qq4YWOOW6jSvGcnjAIyTWQfFjhzqDdJ1hALOJ20Xmx1zTaG3p1x5vBJQEngR%2FBSCYPaeKDiD6%2FtiK4M99akV2bQ49TR72h4ucgUTYBQOvmPav4LbsfndfajW1uCumS3ABUZjGW%2BdHYydCIOklf%2Fgw21TxDIu3B%2BdYjwMHt0xcXga8VbArWaJTu1LXlR7DwhqhqfV0fnoFEoBuXtIQCbVy6mSS9RwGfuzlbQ0VggUS6FiXbzqrYEa6RAD8yIYOg2uM3VQypfI7yGcY%2FE6O%2BkWHgamBGEmbZ2I8a59wwffcTwsQIXasn8rHIZg1Yg%2FGGSnnrNwVoSONzrOqxNJiOU3zIdqxzgb3Oe0E4UFmtKAq1EMIyaV2yxqWTtxtD7ZhS93H2xhDzDTvv28BjqkAR2M66Z3LeHaucRxA%2Bhw%2FZb0QB9%2FeSg1Z4TsLDKG%2FR3049c%2F9tnYkCf31gj0LgMivJJ0OQegRKUk3i40b2yvdfw7QmW4xsT7ji58eqwGYE%2B2hAfyjyZ3TFOlXM4nqcfF3HteTFAr1Wkq1W6qJan1jydFBpyLfcLBXK%2Bq4GvXXcu9xpSn%2BVuAkKltNsjg47HWqngqF5Gu6f4Y%2FJA5rYSUFpBiaWCB&X-Amz-Signature=46de73cfbb7571ee58c5b68f435983b1278d223e4d9f69ff4f2b9fccd7e71c22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OMVWLT7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDii5%2FjspWkcTGrjNWUg0odkXM3tWakGIaHQ9ERKGIt%2BAiEAxGCZbd8YRMKvU58s3mvuJpnPrnfL4SoW7i1vw%2FV853AqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtrolnapcxwaqE5OSrcAxjVG0hTdLE14bDqhpsNGFr0%2BxkfQXQQlY4ExjV%2BVPd8ZjtzAEj85gkhlNpHrp7E7cssg7V0hSx9YSwRJ4rVmzfEclpXCErhcuqobkuoYUwMpSPrz1xtsKCgCUb14fZZC1b0e%2BA%2FarShoL8aWjcpdm%2Ffjd0fpAB46Iz7Y79xSY1BEvW9RGDMdebUv8BEYPa16Gj1i5EIvm00hyGDBEW7AS1YunUB2q94%2BsAwIGKFzHqG9W4VkUqzKjQ3gJitLhaYulTlD5Igao42VRglnYAidMGF%2FQyxu6rxVOdUf5veVFNEHjyWQm9UnEu3P3aiE5eDUnzcnxbylXsJTFAlxlHecxVFf84yGUn84cCgA80HHkSmAcRRC37l9K6rciaDui69qdRPSMKTdlEl1aFzGWJAuTbLBe8ZYm16OW8oaKm38JmykLRpu1b8VJSFZZuttyrMHxfn82RPg7kBmmZssr68sYiiPAM0iSiGMq9KiUPUL8naXmdwQ8OY9DcMdaoLEACbmKBmTeg1NoCUON5CNMlUyvEXhRUEet6u%2FtJUoJ0AZAeir3gGrzr2CLR5qlr06KpYa%2Fc9NIXUR4nwY%2FK%2FHN2Jizg%2BR68fYGMC3iPF7eroR2ki3v8pOkXsOjQLY0u3MIe9%2FbwGOqUBXpY%2FeGotW%2BNvE5Yj6jWEN3uQxvKJCU32L5BiLGSZStIvrJYLrTHljAhWoGu5j%2BiGwSe8F3IGrvy4Cw1PiGi2B4U2truoAAj5rfo5oDzZ80XI6nDxvyGfW0elRDp%2BuksM2yQVdva0eMYqfk0AIFwRHRrD9nw2jSRucqrWNwrzGVwRh6jzpEsPZSovVPuKXUq1AGYkJ8U68KM9ACFWwMw3Zt4A73u1&X-Amz-Signature=2d4e1944302aacbc7d6ce59fd9b8fad6478a1a52acffa901d2f56492ed10f709&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F4MCI3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtAcy9jiQQchYPoBpZ4Kh%2BsEczBna0ZYwkraWx1KKQTwIhALqBilvKa8RoPZFvIkCvQJ7q8ppiHtd%2FRMMXZySCUqabKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTxPDxEhQHqsS6paQq3AOFMASYn%2BXEXXk0wZFFY0Z6r%2FTL6t%2FN3kEED0uXdJnamwKbPAPmN7nnE3g6PZUshm53GiPjrrwiozxbq5MFMWuKUtmdMwvYYacNK1RBEGi3IFNMSVyPYisRQI%2FI2LkJpgFQWpknuNkwVYe9KG4XkCJr0ewNnMIK7UYyUbejhT01ThiVMm2Livgwd05AMI%2F9yQs89QEUM1XjkYbJX9%2B75tzwF%2F8oDn6hj1dqWYki%2F4bs4Io9wl%2FTuWfeWI92rG6P5oVRr5gpHIsNyGjNUL4RPOQoGERgOGwDpsflAqH5bPZwUmzTODADaRFpCv3oSRZr11Afce%2B2z0Y%2BXiD8TMhjRyAa1DAet8giOu9u0wP%2F0sdABgballwd1Pdjl0Icrx1YxVLVwQnzzdk6WmS%2FDM2pLjnUqhNKdIA85tJ56Iuvn%2BG57SiyJCFsk5n%2F8DuOtJcMRuTQSeRrPMXYcPOuRhRCoyUvmhXuwwhQZPG53cg2GckWvjzixOBofhpHoooK%2BF0m88wwU1%2B%2BhmCMsdp6mOwrjN0ECmypqRhKaXD0KYV2hn%2BGMNXOdy39jaREjNBAlKCx8f5ZmLH15BHsP40DI%2B0%2FbuebBxwNJYAiaR8U3PjU5iHqpR%2BqV%2BocMYiVJJEqiDDIv%2F28BjqkAU3LQD0tYBnI5iA%2FDIEHNnGk33hYn7MXMyAOBifbUkQJJd8wy6Y0omo30xgGyGTTpeOXk3Jqx5ueb2Xv2UoeLrMKe47QurwSSyW7V%2FU1zQS%2FTk4V0DFv%2B8%2B4CzSTQRlMToexJT0jqJQ%2BsoywnLgwLsA%2BoMQTq8EbVLFuQ1RUe%2Brtf8M%2BKS7CJYXoExYbZmND0h2mMqK5dM4RzG2GDBDiSEJ1FX%2Fp&X-Amz-Signature=f627c67a84de77da313ebec4a3262a38a6e8ee8861f42839db1dba010beb8997&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F4MCI3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtAcy9jiQQchYPoBpZ4Kh%2BsEczBna0ZYwkraWx1KKQTwIhALqBilvKa8RoPZFvIkCvQJ7q8ppiHtd%2FRMMXZySCUqabKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTxPDxEhQHqsS6paQq3AOFMASYn%2BXEXXk0wZFFY0Z6r%2FTL6t%2FN3kEED0uXdJnamwKbPAPmN7nnE3g6PZUshm53GiPjrrwiozxbq5MFMWuKUtmdMwvYYacNK1RBEGi3IFNMSVyPYisRQI%2FI2LkJpgFQWpknuNkwVYe9KG4XkCJr0ewNnMIK7UYyUbejhT01ThiVMm2Livgwd05AMI%2F9yQs89QEUM1XjkYbJX9%2B75tzwF%2F8oDn6hj1dqWYki%2F4bs4Io9wl%2FTuWfeWI92rG6P5oVRr5gpHIsNyGjNUL4RPOQoGERgOGwDpsflAqH5bPZwUmzTODADaRFpCv3oSRZr11Afce%2B2z0Y%2BXiD8TMhjRyAa1DAet8giOu9u0wP%2F0sdABgballwd1Pdjl0Icrx1YxVLVwQnzzdk6WmS%2FDM2pLjnUqhNKdIA85tJ56Iuvn%2BG57SiyJCFsk5n%2F8DuOtJcMRuTQSeRrPMXYcPOuRhRCoyUvmhXuwwhQZPG53cg2GckWvjzixOBofhpHoooK%2BF0m88wwU1%2B%2BhmCMsdp6mOwrjN0ECmypqRhKaXD0KYV2hn%2BGMNXOdy39jaREjNBAlKCx8f5ZmLH15BHsP40DI%2B0%2FbuebBxwNJYAiaR8U3PjU5iHqpR%2BqV%2BocMYiVJJEqiDDIv%2F28BjqkAU3LQD0tYBnI5iA%2FDIEHNnGk33hYn7MXMyAOBifbUkQJJd8wy6Y0omo30xgGyGTTpeOXk3Jqx5ueb2Xv2UoeLrMKe47QurwSSyW7V%2FU1zQS%2FTk4V0DFv%2B8%2B4CzSTQRlMToexJT0jqJQ%2BsoywnLgwLsA%2BoMQTq8EbVLFuQ1RUe%2Brtf8M%2BKS7CJYXoExYbZmND0h2mMqK5dM4RzG2GDBDiSEJ1FX%2Fp&X-Amz-Signature=7ff05d2df673d9f525b0ccaf5c4ef00b19b22a1bae4333665ccb70d8d70bcf3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
