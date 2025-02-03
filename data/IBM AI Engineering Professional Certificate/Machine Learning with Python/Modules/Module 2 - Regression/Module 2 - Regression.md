

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=3acd5c7e82fb38d60f02c0685d766a16663596552d288674b6ff8688004fe7e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=4e928229ee04020da8f22825dda2c43d02823dba9cc7b2d04f755d5dadb3442b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=87ee50bbcd0612d261fd33b357bacb4fda926870b47e7977cb5341b24b1692a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=6b8156a15f326a0954f50c72bbc0b3ae2684709323b6b983bfe48e93f5ec99b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=da5b3f0b489074063f5cdced71033f91a824ef074774782d00fad0a52eaff543&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=9ff785f6d4e3970a7e98e33d18228813dee057d52b4cea6937af819f8917ce00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=4ae856bf19b49d6e3dc53d9cfd23bcf2d77cf1770303540a42768bd871fdf709&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW2BGJJ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU3NZLKU9FKU%2B193FDzXSQ9rVIUw2DfZhWyY09XmUdpgIgaSgjIXBsMJGDRmC4KZo%2Ff5vqcCVURYnWfMapiCqsuNEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOgkHFhvXZuG5z81ircA4Y%2FXbDEfxZETTZI361k6isVnvnKRYBBtpaxgHn6nl%2BYUXK7wHwmyL1vDhpp0RIv7s2D6%2BGZlN7h%2B8VXYNVCKAMxmXeC2DzCUxXiZRtpcKaJYGZ06aqsT13mBB99hdTH0dWdEEzowohGYb0FYJjbhhptgRgEzP2cui6RflCQ7%2FVYFYbuRfz8i45vxszQOnK%2BPb36rCZ1lxuzWIVj01M6twQJ4w%2FqvzbcN08TIqY173XkzMQejfgpWsEvuszA9JxrOuolkKtWSvvv6AzpjibXAXxrH5z%2Be53xWdDwqAD87uUUCpAUNuowUHQaLSlbtxr6sSMfwd441a3x9dj%2BbPjtmY9GvGzSv8LVzJu%2Bf1eFhAnkjgnV4h0AlF7gN7%2FiR4NquKL7JRHzntMkpJZhzZ2kgPST4P%2FbeP%2BAZf%2Fmyc6T3kOeuL7hJC7HNjrKAoWxdOTpcyyvbgKaOldoCrzvgte9UlopgipmI28P67228lNER%2Bg6wLI9olbT%2Fjx5i%2F%2F0JHcHRst%2F%2B3OCQNCROLjU5Z08DElGqCOI6QqoYJ7CylUMpCNfHAtM8flm4JhAp6xtbvB2dvYJaOBpVzHkua%2F1Odf%2BTrCeYFnyeXX%2BvCzvhaeXQp0H230Txnhsa5c98eGmMP6%2FgL0GOqUBtg4jFTGhn6T7hoD4FNUyzSpfWNVRmWiPZjg%2F%2BdXRGMvpr7oWjtrk3IW%2FuNtBvVXnNTkmid316MAsOLI7h3lfdft6CtBCCG70G35X%2BksD3MMzY7Yz5IpNBIlvTCfwFeb339%2FKUxtZ4aoh6VPvv5xsmGl%2BXnSdtP9Ry0ykTKv6hKl%2BpxEuifSOKjOH4IsbXq3ShxVNSFf4fIov8fVt2MKqixgBycHS&X-Amz-Signature=bb466d81d19b5cd53aad290a88dabf5bdfc030fc41954acf3f16bc7e5d815e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOLVIMWT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICVI%2Bi%2BG4zB9QRLkUnhIKV4DB2X%2FeK1djMPw%2FTFgDkDfAiEAzxil%2BfUAhT5yaOngaqxS%2FBqFt%2BHMVxIGEtItp0mN6MUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BBERNYHJy2eSFdmCrcA6rggg3yNEGhcfEB%2BnS7ecpPjnuk7FKb6D%2FcoeNb%2FVR3%2FDHY8BEbtoEex1r4vmVkhMAbU%2BhY%2FE7h6P6h%2BxNNLS3yR26i%2F7BtxwTkD3XvZioSs00FeS8l%2Fx6PffctXHCdStC6%2FyDfdmOQRx5%2Bjzig67x4XLjVZRvbx6IIyLBsCaNkrHt8ZGXsGqWAQRVSdzk9aHf6mB%2BJd9OdEW09dvC5R%2By84lG%2F6LOnePYZVMM%2FgnaVz0zIpi2NzyhvGSQACSGsv7t2iHZaozadw7PK50GC4Zj%2FT4lsKMUZ4j%2BMFe4ce8BVcm2WUvm31u1JLG%2FSSpFJUNZ5y%2B20FS1%2F0LeV1PvaZJxE0FiTNFHweF3IcEb4sx9Lkar5MxiHGzQCE6uf8tPPAhEo%2FLZe%2BI%2Fs4xcm%2BTkJKwWVvCP6wR7JXWfOy8iTZ6uBMatNRWtdPtQ%2Fs6OOsy9VnDCFLtgvaWKrlMwj44k9d6W1MQ3TX5mC7Tt9xj2pYQkibzCeqIa%2FlNUoUSo3wzok50GCV652zOfWMDv6shTQPcGl4xRRSllyZzGZ31yGDrzK%2FMR3KELW2U9EJH%2BNVpc%2FSTjdy9DLB%2B%2BHxJ2XO2oBwZplLispRqaCxqk6VyM0njIT9aYph2onCZ7gStC3MIi%2FgL0GOqUBXVvyWpygTAPfS0A9n4vypRP76Efm0sjLJiAFbGZYXIxmXHO0B2IKg%2FcbkKVrLwVGcp2PItl%2BfvLE7M1TOPUX3xR%2BLgW1%2Bl7VJJ0f9JvVGv1sbqORc%2FDQn05L7PEtF5B5aU1029ZwDw6Sj%2BQTsusNOpXaml64hrVJDfUXoW%2BDjNdQZM6oGWeVlcqPrYBbPlMjdIgvsnrduvZh1qpgucVBxkb31vmP&X-Amz-Signature=63e0d9bc7f4aab11ae1d57c5a6b8ea4d41517dba8bf32d5493b4fa146f41574e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HXQDF7B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjsJWrNPTX29sBkmM5RIYlI63ap6l6eJJD7xJHfkbX3AiEA23CRpl4MpgNQl91pwqU60YaGNZWxKMKSM36JydICf6kqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBQ7VV7ZALDQcoEKSCrcA%2B8%2B5caTU8PiW892md3Aq15PVl6CVxdrQ7u2ZcW9msXtoDewqhWdmGU5fJWX%2FhR2rtTLBC9Lv52fTK4GImjGYHanO0s0yEPVzvypkN752NL1hx161B1bohP2e%2BfblCf7TF7UIySDUw2HiT2s7EOcsY32gCALCNH3QkbESwg%2Fr54FiOpkanihm%2FOrWvtOsJWcjwapQfH0h0hdVcxk%2FWhbsJhMvyB0awZBWCAiPD0Ox5uQs4di8IkrhpdttLdAOUOZy79%2BnTHjs95EaxCeO0KS0wAMK%2BTKTCR9yrHSukKcbRJUs82JeC%2BHOG3H1vfVHWAojUcekfnk7xDN%2BTIHHUkWSbhQ5IDSc9DfGRNNR1Wdzw76PAac6cpIPi%2B8GzUL%2FEPHqXkG0EqsjiajyafPrIYwcES1TW2%2FUuYo7ZJSiw1fQyljw4O6M6fT94uaASC5%2FHh6unZQRgtat%2B8xDlcJ7DNW5lTa4hX93EwzoJzWn%2BBYlNjkTLxDokO6UcA5a3lr%2BjPYcqsei7%2Btih5E81YBtueg8WRGlMWG2%2FnBD3OvzjjtF1UeZuxRC%2BcnfLbGqb2uV6wtTByJ2eUDTVoiTx0fo6obY5Tf2%2FayQ7bMUlvekwj7rrvfyvaIUcvsBF1LrWEpMN%2FAgL0GOqUBpJVYWT4ZYA5MBxK5iKevX9PKizr4SphBa3e%2Bc1%2BEVW5yOQBOx2MrKGr2eRdToGbkzZHAgyCYxWV66HrUiWSwg5kSu5X4qWUab6%2FKiF1286Amp7ogE%2BuyrCr4DSx3f9UcD94E7QtnoNS1%2Bi%2Bnkt%2FrtCGgboZi1%2F2ELO0ra10bkE%2Bj%2BfEmuj4NkOur0Qncrl%2B8oFeBmiuNBJXGbog3K6OLmBgYMPt7&X-Amz-Signature=7929cb37b5331ad8733f1a83749d9f2a7d109794a8fd895176ce1344408e2eab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ESUNQMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDzY5htcHD0Lr02FdCVuK0cxJRDEG4APECPo8%2F1ICF6%2BAiEA2pCN4PgnZhIUgimNjHA3w2LpqymU7zyvHJ9%2FfZgXz2EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFCDO6m8yPaNLy9XircA6aHcR18ARJGWUPdSdW5nAmCk0G0CGPMgyzmQih%2B7WoT2Snpq5l5Go5o0kLPDe3fUsPQKhL6%2Bw6mfhgVlDjTImcysuoIS4OUD8AO%2BBhSBtZ%2BtOhWLCukXWo2Ev7CvdyhNWL6KVW9p81ADc%2BbzPKIUjd3SpYDP4kc4%2FNy65CSanE9iOKD3TtvMHbjZy8UYiI3Tr7EAFWsDO3Yo4P%2BE0C%2BywroDxucoVSMNWjbOITPAU6COYt4QVuGFb3lYWi6UU%2FYzpqnAjIi%2FZeuwSzS8NQ1HOZ7Xw0O2wu7e%2B%2FoCCMlgBTvNLZoCUtPUKR1ivl0pmrT%2BG30ofdHHdlvnfrl%2FR0qFRODoUjE6Kag4t8vZrw1gW3QS3FakvgNi6Xg72BIFZARQBPjppaHKc1HC1WlKZo9y0uvqOj6BiXm571KVPyIF3nTLSPWNTEKP8%2F3QgqjCyoAHBYHtyZpcWlaK%2FFORQHHVJifokPag9Z7cFHQlkVaevDguZomGByBtPcWavaw7dad5ADPECPMSF4vAQptesIb09IeLtvwvBrlyU5wccB4aKDY4SFzoVB3wNZzGtQ5q0SiSf5jsduzGNL57kB2d%2FhhsNnEH%2BYnrXwuxBZuAogHhFDWLEZB2Wx2ZRAh%2BSdNMMu%2FgL0GOqUBqBGOP9qnlIorjCtScXycv1aNRVb6R9CaQghLiQC9ooQQFIaaIcJxvEFF6Yte9cb6RdLa9uVaBWNMJGCovV2NQDXr0z%2FLlnuRQYi22zRgSRmnh%2Bc5mTg9macmvEgf4bgrvIC13b2sbIbCCB2kqDbsoSGgjiMCmnZh8GotLQlIggY%2BV5ZzkRiG0e0CcSoabcRWOoYeVoBZJ64%2BmcxRRU1vx2Tdpzpe&X-Amz-Signature=4c58c83bf662c5ac4e00454c20d9ca3172940d2f51a237a466d7ed2a750a2252&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ESUNQMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDzY5htcHD0Lr02FdCVuK0cxJRDEG4APECPo8%2F1ICF6%2BAiEA2pCN4PgnZhIUgimNjHA3w2LpqymU7zyvHJ9%2FfZgXz2EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFCDO6m8yPaNLy9XircA6aHcR18ARJGWUPdSdW5nAmCk0G0CGPMgyzmQih%2B7WoT2Snpq5l5Go5o0kLPDe3fUsPQKhL6%2Bw6mfhgVlDjTImcysuoIS4OUD8AO%2BBhSBtZ%2BtOhWLCukXWo2Ev7CvdyhNWL6KVW9p81ADc%2BbzPKIUjd3SpYDP4kc4%2FNy65CSanE9iOKD3TtvMHbjZy8UYiI3Tr7EAFWsDO3Yo4P%2BE0C%2BywroDxucoVSMNWjbOITPAU6COYt4QVuGFb3lYWi6UU%2FYzpqnAjIi%2FZeuwSzS8NQ1HOZ7Xw0O2wu7e%2B%2FoCCMlgBTvNLZoCUtPUKR1ivl0pmrT%2BG30ofdHHdlvnfrl%2FR0qFRODoUjE6Kag4t8vZrw1gW3QS3FakvgNi6Xg72BIFZARQBPjppaHKc1HC1WlKZo9y0uvqOj6BiXm571KVPyIF3nTLSPWNTEKP8%2F3QgqjCyoAHBYHtyZpcWlaK%2FFORQHHVJifokPag9Z7cFHQlkVaevDguZomGByBtPcWavaw7dad5ADPECPMSF4vAQptesIb09IeLtvwvBrlyU5wccB4aKDY4SFzoVB3wNZzGtQ5q0SiSf5jsduzGNL57kB2d%2FhhsNnEH%2BYnrXwuxBZuAogHhFDWLEZB2Wx2ZRAh%2BSdNMMu%2FgL0GOqUBqBGOP9qnlIorjCtScXycv1aNRVb6R9CaQghLiQC9ooQQFIaaIcJxvEFF6Yte9cb6RdLa9uVaBWNMJGCovV2NQDXr0z%2FLlnuRQYi22zRgSRmnh%2Bc5mTg9macmvEgf4bgrvIC13b2sbIbCCB2kqDbsoSGgjiMCmnZh8GotLQlIggY%2BV5ZzkRiG0e0CcSoabcRWOoYeVoBZJ64%2BmcxRRU1vx2Tdpzpe&X-Amz-Signature=539cc0b1978e5b73b6bc4963d523346db121cf9e382ab2f913fb005f5fabe9a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
