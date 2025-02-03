

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=ea55298bd9f7ee6d9016a3e0b4396529b95f01ef87eafa4f3fc2e141dd738874&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=f9b8c942325cc497b574c7d535d80f34b51f56f01a4a773f81ae24937c9e5619&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=57018aa50f8049b95347ddf8b03a9116906f5c654aea00503be4902a22ce74c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=e223804db2c0455eb9e08534080a6b1eba4eefb3b11d70ff353dc0a240824b48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=bc103bcf2936ed6c9feb949f68383f61109e164f92c9d8309f5736d6679c16c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=70cda85f2d94ebfca6912343b95d96e6ba22bd910dff972d39a5ac6d3ee69eef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=1c547ac951c46bdaf704b611df8e833d9507829c589573f5d3f373a6d3eebd6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIVVBGQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5G2mqFhFQMEL0iqVq%2FzMoJIHKnXQieBLkGaAPbzerlgIgDW60cz4R0jBzjORa3tSpt1cHdPIZtfwLM3sXj6wOcrIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOP91dArhBchVwpECrcAw7bMdqm2yQN8OCY6wQmqrF9ib%2FueAfHS0d1ue8%2F%2Fna0AG3lzGfvVeVNo1Fj88cuhsF7ktvk4JtYDSHRAFYyNz%2BnoLuCiSBtigv%2BJ1JaPkOwQ7Fa507eeV%2BdELrI4gWPSxIBqmUjN1mrsSyb2GmlAsteSAFuqVyOWTz%2BcK5SybFfEFryowUTEaKCIGMWDDasATVVQWV8LG1IUAiK3zx46pFCw0RL%2FgapbbCbDfFvchjnYmwuqyYreamZtFvMt4pEfvjAvlPAvL5YLN0M6vfB2cSYlt77UGBAQLtfixqf9pW8nFb%2BHCc6vQ39M1MRHXikrFhbScaL5XRAHu%2F37XYyWFAWbEdmWEZHwMSSTulxm%2FJA8JrGlqyR1VeeIVodjWB%2FPLQ2CrDUiReCBYFNBbx9%2FdvARcddfn4zMB4FahcrkIaZJnwwtZRB%2F%2BN5mHIL%2BmnoXf8YbIrotNsQiuYIGeEuS0IO3o%2F0GuSJQ9xmCT3K5FSF6ynUViYUySFeuBXZaLQ%2Fi2HXOYV3POu%2FzIXuOq1vapaoZGQz9ndrSmyk4etN98bi6Y3h71B1HAr1abnm5TtydGFyy4R3hqv%2FfbRSZNrCubSzdDy%2Fh5%2FZSeDKuPk%2B5lZH5a6UgYgM1zwI9jVKMK2%2FgL0GOqUBFE7vY3ag%2Br6tF%2Foyr0mDhnk7DY9tjr%2BwlZk7VwxkSEYFldcneXQ5lcgSV7UHMUu166QveenkqvGMWBnm8b%2FuKTxZp6Zg%2Fw6bkVsyr4augZbU93uUAzN%2BYwgH2tjDe9I4SylmUio3hGAklSHL9Ohd1Dy2H5JJk1q8LKzeGOrL%2FINPNIheYt1u0N9P8VQ7Rr21oqNIj%2FYZTwXlTpd82RaeKjyfWgRH&X-Amz-Signature=90af94f606843b7fc5f2217996aa37598c480ed15048b6755c4fccf6c8b3b117&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGAJVCRH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCONs%2F2rzWG0AYTGWxE33tIsGgSJCaSjheqGwiEyQIkNgIgRTf2RkWdvIRTZIRoAvMMof2Rp6fX31dXjww2%2F3gOA1EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDngr7WWE3XIt5SVCrcA3LGLOK61BYH0XtiTIZjhkW7t6qXM0yh2xoXI%2F4gNuVEm4QyJZ3MrW11TYHn6xLItNxFvMuDygHhoPaqhyq2jW7kMR%2FhL%2B1jJqSqe57WrrmQVefYv5zXCMtZKKG3SeDNB9d9%2BkMzIpandpwoiyJaZVwPVMIj57HfDtGBGiSpZI9nH67qi4hlIoSpRFvJHNyg5KdvEigZfzgkkvL9OCHE4kzUE6OYwJDhIXdBPmV9xtuNz%2Bx8MRZbYGhlvwPnppp%2B%2BCKBDaT7y9Uxb7xOoDVWdUMxhtST4RuODp0UxYLrYiMzEQ7xhlel65x9Ov0a3mz2jl7tFi2x%2BToc0qFS9KXbqmgaUhcw7Z6tsMTpLL8Zrg8neuWMcfVghxJqt6M8OfdJh5bRCoHmZonHXKwCpRox7FHRkc096ngUyuiHY5pDWc3Ddjg5hve2YUxJJ6wqWsND3KlC5P0wVOhd3mu1AC5YZ2sJEU3nwj6myekWbRmbFUykgN8WhfWvmXTWWDeZU1Mzhn2RCiNq2eV4jhFVF5ot8Kmdn9YU46FFcVOaBfLw8nVwqAR9r%2BWCbYT7u3Wb37ke8V63WZI3GBuKpv4MRxq%2FPhUk3DmlNGQ3y0jiL9i7nbdc1l2Akfu4loWAyycqML6%2FgL0GOqUBIuRkWO6%2FVD6avDPiYZ2HfJK0V8YiLweT3sh3%2Fg8Y2b3eOMbWOhJk7w7VwFXvAp%2FQjsg%2Fb1rrvHw5d%2FFTSRxUPU2MLWVHKXkmiiqMZex3lmT8wKys%2BhTR40QKI%2FuCgPPNAaC%2B1HNpdvnxZAi1RBXERUJ%2BeTUfWw7UlzoViU38Vcb4ExsVzGmhOYxPF1X%2Bs%2FNLk865uXQfMOe08rkmZORufeu9xRIz&X-Amz-Signature=b5567d3709d5a0443ca0152d1247a94957b2bda9a5965dd5154f457b6031ff25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2WDCOHZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4e3u7P%2B5TRdCzsgfzRBc5%2BW4J49IOqNEry9OBkfkpzAiAfiYCnC1uYhGOfyKKp%2FVHxabnlO0736XcPIt2dBzXkMSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWCcLhZjFpQVM06ZEKtwDdvQMTm2qKfD70AKGCHAOPCA3w57K%2Fc04%2Fi6lShgpuhHX4gKSYN6fHc7hNFCzjZQnmx4O89piE%2B56QwGOdYNlaJfD11DZsXvQJCKCMj1Uuoee0D6f%2FX0%2BBhj7JAyuUjE7RPNiFnJ06PcZe9d4fTabAb22FNwjQIn1DTmSQ3LMT7e2UOIf%2F6KroEml6x3urfevoIKkwN8faoZ2LgglzmOBrAi31ZwsBjDuUdMx8cwtOAqqY671u4f7g5aE4fnOT5paFReaFK%2FDzBZrQ9%2FCEg2EW3ogsfzq0lukZjPitCZMi%2B6%2BAYjSEj8j9AUm%2Bp%2FWVK%2FQ4FN2ApRk3wBPcRP9z%2BM1e%2BnGrBGj4VG4Jv5oScbaUlP%2FJzilTLVOdxC0l81Hcmnk08rPrS%2Fp%2Bxm%2FUjAYpAC0NVvhBf8yaic%2Fw7AP1WN21pXr7iw2RrXY1QSBvd%2BcEvhuDB3smkGWZ1em05D8iiXLmJ3gK7hiv5uiFVAg%2Ba9AoS8jFGyno%2FVOfKPnXtJApyAlElroZC0Aexr0LeHCX9kGT2zoFuu98yXG3f6L%2F%2FjrF69TDyL%2F7bAM9KefWw68edYACCrQdIAmM8fXXVzs4RWGAWxTMmqfAH%2BL4kD%2B0H95kNQXWoeb4z185O3qWrUw07%2BAvQY6pgEkk4NJuy0kc05crjfY0V%2FMP6g%2FlgTY5YOEc8kxaWb8NhuSSzEznzXIUUE0y%2BH%2FdcNfnPU%2BHnBzj8loah7HjIz0WtdbkbDM2%2FqUUgsMmSRHPsw2PfdOcnI0CPLOTCgZv%2BDN5LxdEb%2FjGlvMASpNbnglsAPGpdJcy%2FJhXd9Bq8Odd4sTmlOecFDPu4nnu0SjS107%2F87ZWbymR7%2FcsDrJ2eb2pdzrypnQ&X-Amz-Signature=ba85c2420b397e809cc4885a79ef55127a4a58866c017a10dece4b03aa5e34c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z62FNVE6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFpDbsThtXy0%2Fh03TDseuF6Rp6HZaCqz1OJ4xyKnVdHLAiEAtaMTsegfy9%2F06E44xktvkk6lhfzlH7NEQwwDxcwGeukqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKONLjL4o%2BB38vAA5SrcAys6E6gkHz1UvClh8UGAFLocS3cfBAVFH7Mftg6WFZXxfK7y%2FIUCQQXHbIBRoMKvjjISq35rytHdT%2FoX4%2Bb59n1b0DazCXq%2FpdYw%2FaKMlWWGe7dlEABciRx2I%2FySYjdTxqX1C2Y2QXTO0jWWRfhk2DBg%2FGvFS%2FXFRmMqNstL3pbjNkQF3CRYcP0En2bFjZ%2BMKH7yIJX9We1cigmtDg9WFIeSHnagNllsJpn%2FtQmhOTVS8lGwVz5Ic5LIpAi5%2BTzwU7mMq0SwrTkrrjprg4IjoaDLi6wMcb9TTpSzgSraqAovdvjXHs6xBxGvWKQdN1ngsMe5UxFXJBj7jg1NFzsNnH16GFzpDrQLIvXQ0DTtECQ2SNGEqnGazJirIyogwVmQOTkLX0fAW8brW%2FsaT3y4BhpgqCb3d5VhVlsIbd2q7xHGseRGxCloeZtXSJ%2Btspuhg6Oh2j25PNpdnj10BqGYFRgNzfy2mfuaUA%2Bga%2FOSDGnGp%2Bwo2EXPXdIj9o0JFbLu2VzUoYlZ84qbq8Kf5tcPUmowC0MR124WdOytBs%2BGrYjg247TUcAKRqQsbOOdUW5CFQ2dSs06NxsI0i%2Fui188i7Bx3hSokV0YLdbVxP3%2F8X6sjZLGHTyLw%2FPei2XFMLW%2FgL0GOqUBMo61DLbrgflfnGFrrnPYBD2MLRuBo2L4UUOchchCWWxRZ2CtKfsc0bFJ%2BRkuI7fQmJVSv5QX3vg66NtutqbGA6UUaCqow2VCseprnoSSt0WWi2PGu3iCoufcFLfNu23Sm8oxo9PkTm7qZTrVhrX92%2BZ003PIzecwWyLDftveKVfC9uEyVF3q60rn1PdwFG90QqAAdwuADR2mTUuBLO6bCjj33ENc&X-Amz-Signature=8563158929e8ba1189182c1ab36c74d70fcf74c4ae8ec91d9a67abd5f092323b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z62FNVE6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFpDbsThtXy0%2Fh03TDseuF6Rp6HZaCqz1OJ4xyKnVdHLAiEAtaMTsegfy9%2F06E44xktvkk6lhfzlH7NEQwwDxcwGeukqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKONLjL4o%2BB38vAA5SrcAys6E6gkHz1UvClh8UGAFLocS3cfBAVFH7Mftg6WFZXxfK7y%2FIUCQQXHbIBRoMKvjjISq35rytHdT%2FoX4%2Bb59n1b0DazCXq%2FpdYw%2FaKMlWWGe7dlEABciRx2I%2FySYjdTxqX1C2Y2QXTO0jWWRfhk2DBg%2FGvFS%2FXFRmMqNstL3pbjNkQF3CRYcP0En2bFjZ%2BMKH7yIJX9We1cigmtDg9WFIeSHnagNllsJpn%2FtQmhOTVS8lGwVz5Ic5LIpAi5%2BTzwU7mMq0SwrTkrrjprg4IjoaDLi6wMcb9TTpSzgSraqAovdvjXHs6xBxGvWKQdN1ngsMe5UxFXJBj7jg1NFzsNnH16GFzpDrQLIvXQ0DTtECQ2SNGEqnGazJirIyogwVmQOTkLX0fAW8brW%2FsaT3y4BhpgqCb3d5VhVlsIbd2q7xHGseRGxCloeZtXSJ%2Btspuhg6Oh2j25PNpdnj10BqGYFRgNzfy2mfuaUA%2Bga%2FOSDGnGp%2Bwo2EXPXdIj9o0JFbLu2VzUoYlZ84qbq8Kf5tcPUmowC0MR124WdOytBs%2BGrYjg247TUcAKRqQsbOOdUW5CFQ2dSs06NxsI0i%2Fui188i7Bx3hSokV0YLdbVxP3%2F8X6sjZLGHTyLw%2FPei2XFMLW%2FgL0GOqUBMo61DLbrgflfnGFrrnPYBD2MLRuBo2L4UUOchchCWWxRZ2CtKfsc0bFJ%2BRkuI7fQmJVSv5QX3vg66NtutqbGA6UUaCqow2VCseprnoSSt0WWi2PGu3iCoufcFLfNu23Sm8oxo9PkTm7qZTrVhrX92%2BZ003PIzecwWyLDftveKVfC9uEyVF3q60rn1PdwFG90QqAAdwuADR2mTUuBLO6bCjj33ENc&X-Amz-Signature=5d43ded20b4a40bada08c05a869420487659ddbd2856944eaac575c8d141b74c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
