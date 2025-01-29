

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=61fc2dbddca7eafdcb9d0219500e04a8823821f7962ace476f56649e485c403a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=2b0398342b2cb0bb715b5bbf205c375ec1a14ca9f6d23eb0bdce59e6d3b53d77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=badfc5b47be285a6471c964892540a86e41f014c6247b1707882a3beb12a5b9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=c0adc47bf096ef630393cf5d20be37e37006eaf8ba220be27af013164feed2be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=db938404058fd9323bb4c0a1cd8cecf498df3a08b74ec8762d5e5e318f8a8d2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=c11e1902191000774bfcbff3db0ca7e42ddbcc9175c24969a4d6974739ef06d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=eeb9e44f7710f61fe4d96142683dee35202cc94451ea77171149d13cadd5cda7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654RVNBS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpXUZYMnH%2FmyiP3oiiYG895OK6FkqZmTN5HhyP2WjfKAiB7MpzYMkOMKwkipl3bgGEDRV9IRsXSvEE%2Fl%2FlOc%2Fx7ayqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8xIPDoz88xX5Fw87KtwDwmBWB4s1vauTZ0X09%2Fq8kuQQurjJmUQmcxXb55ackheHZgtrxWmfHavhKsVDN8fqR86%2BwMsNQIWKos5Siypm1NcrM5SD2pjGcPjQ%2Fn%2B05dfjpFk1QMZV9mF0eAjcIoO4KrAXfEPju3nbyajRMCh2sJZFVscTmtF7nNJV7fnaoN4%2BkDTj3sIWv6r6PUpvWSUCIruOw3icb3o4U7ta5SwERmJ0O07AHfo8fIFmVt9KRLifqUlciog7W9UFv21x1gtR1StgRXZvji8e%2BVAYzVLfVoNfU1S7rh53E2MlE%2BNGBleOemBM6xMfBlIWcN37HzZWQ2xDb16C8zYbW6XZtiX4cELravwXNFuRF6T3V6dh%2BDn7zr4DwcQ74BQo3%2BOjHlwv3Vr8qIPWbuXZpsKRhY3YXFkWBXz5Bs0aiYLlKFo%2BW9kd3rd7JFQnD0%2B6C08aX55raGoDniHWWBqP6j7tf3%2FroW2D8D075TWX9o%2B58Jrd57z%2B8K6aKOjeZiZeW93%2BWkw2J4Qu3g54VBJQBJtoon7ANLthTn8lTuMFVsvHioxZjhDIKAOgNr0eNZ0UcJx6R6WjR5YDtmpKME0UZeiUVUKzg7LDSas9Q%2BygmvPWA9ejNhXWPgdT9mVU8erTHgQw0uPnvAY6pgG4FmIKPd%2BNr5QDOHB%2FR4LvFXAHc4tyv4VzgSelmQRRRspVSnc4%2B%2FDQyTZUk5%2Fygg97AuxHILoYtAOPmLyb%2FQhnPoA24YMFNKvAXJIS6DSuSftU5W8%2FFkEk%2Fle2QwNGwg9JlTMRFd9L1pwZe2xYGIbGpYqDq%2FU9wUoi66%2BRRFnWpZRKIg8A%2FkUNYKUFN0RjXECFQctSywF5LvEv4a0RPiHunETP1mLe&X-Amz-Signature=550a37128026d19dc9d9e3bd8330a67d67d702d0ebf8cb41e2342396847b9987&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BTJQQFO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2k6quylzZwykNlx5Z1kWN3keMeh4R4I9u%2F4c1miw5QQIhAJ3G6ShjeUieC5LgZ0Ud74aM0oEQXePkdUyNHkgCuApWKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFmgBJD5z%2F5XFdw4Uq3ANCI6n1i2HeVnlEQdBxPfcPCmft7sozychQcyADWXwOm%2FSyyi6wPXa9vhvtr9CTxUvGWvAaARkACRhf8%2BT0tXkZPl62jrskpJVK0NhEm6BjoZAnln1k4%2BWAqqWr2mLc64RwIbI5dLh8fFs1LQJFz3tHYcMrd54IMPLRgA5LLRAloXtDaIZL94%2BNKnwLm08FMc9pGIMMn0GRiDoszYL%2BELIwZTe6eRD7CyuTQVyAFBc7wWu94XPdD1TomTEvcESs5nxyr0YhC4LCnTxJq9JeXG%2FZ1K6M1HY3SVcumKO46j96DecQXb1OFpD7Oz2MQ%2BxTK8YmwPRt272YK%2BUNi%2Bb%2Fvd%2B4PKeAmULGRnrFpvZ7R7E632A82X81Z4K4sgSj4jmv8rJct6jQ7fxOBnuKDFcLF8NV1MWo468piCBnqi1C%2FRPtM8jw%2FmXIAO221R8wogAuowtAS4qUUWYyJduLIHfzzOxs%2BWnYIZLNL5wOcIPX8Wj0Ct4L%2B%2FTqy25bU3RZvPxfqLkwH4kkNAcISQIbEZgA50842ob5CT6Kxn3hYmALwzSaXavB85XbaWkIsPjgenSzI5gmncDroWT%2BlRD85bCSDX0MXqMSYzzrx8IlVVWjKv6ft2ckyYCDz6ERC0yyGDCi4%2Be8BjqkAaO%2BzU1Quz9bjwPSLAeE%2FH2BhNJbvQ4cvj0O3Dkbba37d93zGLVIKpNwpUL1FdP58RW1CK9AiC9TlrpZxDsflBKl9dY7GXnMwmninFwRL%2BwwRWl3vie7MBHlVcJmfOAeH815nJg2Vp6ebVdvEsJnCEjXFeSPP5g%2BB6Ljqjeel41hsbHIRXDM6DT2KMQk0UcWWoBE%2BuXR6UPcQqazZiB5ofePECrl&X-Amz-Signature=e2e86ba0e4f324da5912e70021112c5bab8636fb386f619440d4a43c211d099c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WT5SKHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqFVE9OZZe8QCHBA7xxudigFaFZAdZO8hh4%2BOB76DoOAiEA%2F7qVIzNglkdO00Xa1da1hRyh%2BmPSCjK73NLZnsn%2B8msqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDd%2Fqn0ZHX1DGavyuircA%2BsWiw562T90lrJYNjxdlF0brThbzjSTm6Q4ZJJ73xU0O2BGg8kMB8vEpGyxX8lSjOFCGPkpu5TfKCC%2BQ4AYDhH254wPSLMTzSdl5Q%2BKYnPFET8SchccueIALNCATHSIbsSHaUH5ewWuic%2FGGWstAJu10vWIN9GF2FDTC92f0Swd13xX8EEoYWJkLoZJmakRCN8t10u1%2BCKl%2BlOYWcqEiBehdRgAp7qFdzf8VMbudwdGeAsUCXM1GNwivVl9%2Fia6CufiKydMuWe4onU7JeZFSKWTmht%2FsAZv88r9wb0BPax7GOut7G2aJCrYhSj7QZm5Bv%2BupAuJA%2FAYJtO30jiYIafn1SPltrd11vrsrde3boCXWNKF874liJMp7nE7s6iH3NAC5xq2k7O6zShDDi7z0%2B6DXzbLmWkvwGnENW2kfCv4bk3SLIIk9SWCEXPbU%2BMAP3uRGCtF9yF9dW0sIXw6oey0SZQq82Rt0sckDmywQIQz6qzr0Xmms7OfBtDHMRJKl3NOgWrEmgFVjYdawLEoAF0LwJvvzkz8pr4mWbRJofoIAHIaszdDkwt82IgKRy7WweKddB%2BMH3xiza525yiXjUsMF8enNIeRElfMvPPOY%2Fo543WOtVM13rjKR0UYMKrj57wGOqUBEyRJzUPNFLQbUYrrmSDQ%2FpDchOAR5re8hXl3RDKqkJDIFMWoj9auGRpghLvo3GLDeMCRcfDp9uq5Q3uLwv4HS4Rv%2ByVB7A0%2B6jbHTRKXpVu6GvCXOdZigw%2FZZDBcTlgKQ7veR1Z3k5%2Ft%2FJQTJGzVy1fh%2FomCTVYlRcqlRP%2BK6XYQG58Cali4pk81ZNfH2WSSRFzFHKzUliqkIl5CfsS5hfmQLRxB&X-Amz-Signature=8a72bc17a39ed34e84ba4ab8c56839808c29d2dbc944de7f822b136e72736b33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYEBSYQK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3lRGPYtA%2B00l3oRBLdkp5fP9sTA5m6QpymF8KtsEzIAiEAlgW4PGlsvXxH%2BGUG8Z%2FhDx5iz4sOpIu3b2vfOGC%2FEu0qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPR6TzeVtzRg3SORdyrcAwM043VKFHjkMAhX%2FhWDvnM6a9hk3RzQMrsZgjjDnwO7W6rstj5rr%2FbqaFtdCHosjYuUgA4%2FqSx9%2BCLM3STOI2E5xAQdykzB02kGYWmGn5iMAHH6EUxeQa%2BywXbFnzUOM5cclaj%2Fzf6QINrgKz%2BUTTVL6eHTiDzKOZkoVc4lZV%2BxD4Eom6LTD2AASDmIsob21TI0sUharzqlKz1kGXXd%2FZw2KHtqCEKSJcbPYF2jsxQNg9KtbB9qw2sqKSAzACNkLImHPMkwEB6aPTES2HKjvQny0wpVdknPEVOTHIUrNdFB2ORnxf5OmjeXhkagb%2FvIIsTfW%2BrdZeL0%2F3cAgo5rVm6igZKOhk3S%2FNCBpTaFUAIx11ee%2B38MSmapZr4E%2BirgTW7BAg1Azx6nvL%2BGKlvJYTBvqvUml8GO2CkjQWi60fcGzFQ5PW7RS1avifZwGdZ7Jv%2FZJj3Jbf3f5FjjvVo2DzSz6HLUcOtlcpcjBCvaPA63b15rROu9iPRRplwRBgd1QzqAz6Jxo%2BkhMXxRLDBe7D4jol9DYSdMV3POMZzDcWqn4pCcyRseas8AAlhAQYUyPiq1IHLX36RRhjs4MaFSeB2D5%2BZR4YoeQ9ZMjNTUFBkeuD8tMKGAb8U4nBwlMOfk57wGOqUB7PLzFpzfgZZWVgJqoK52m4NauQGG6a1ZB3PB6OxUGG6vuCggxb8QnEGtYwQF324cst9clMCkLiebi5bpP3gHTU05jl835N8Z4%2FlRSq8UdvHXBWjlJn6zNQ%2FVHI3srZpTZXprvynOkCIvSCjIFZ99WhgtCvY2k6EThVfaee3uczLp8jQMnzPGuL9fJ6YdLgfK5ng1S7s3Rc2vNx%2BNISIsGTudd%2Brt&X-Amz-Signature=3e34b3ab00222c55472caa56bdc91e32d7ea7613009f5b0ccba168c49107e1c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYEBSYQK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3lRGPYtA%2B00l3oRBLdkp5fP9sTA5m6QpymF8KtsEzIAiEAlgW4PGlsvXxH%2BGUG8Z%2FhDx5iz4sOpIu3b2vfOGC%2FEu0qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPR6TzeVtzRg3SORdyrcAwM043VKFHjkMAhX%2FhWDvnM6a9hk3RzQMrsZgjjDnwO7W6rstj5rr%2FbqaFtdCHosjYuUgA4%2FqSx9%2BCLM3STOI2E5xAQdykzB02kGYWmGn5iMAHH6EUxeQa%2BywXbFnzUOM5cclaj%2Fzf6QINrgKz%2BUTTVL6eHTiDzKOZkoVc4lZV%2BxD4Eom6LTD2AASDmIsob21TI0sUharzqlKz1kGXXd%2FZw2KHtqCEKSJcbPYF2jsxQNg9KtbB9qw2sqKSAzACNkLImHPMkwEB6aPTES2HKjvQny0wpVdknPEVOTHIUrNdFB2ORnxf5OmjeXhkagb%2FvIIsTfW%2BrdZeL0%2F3cAgo5rVm6igZKOhk3S%2FNCBpTaFUAIx11ee%2B38MSmapZr4E%2BirgTW7BAg1Azx6nvL%2BGKlvJYTBvqvUml8GO2CkjQWi60fcGzFQ5PW7RS1avifZwGdZ7Jv%2FZJj3Jbf3f5FjjvVo2DzSz6HLUcOtlcpcjBCvaPA63b15rROu9iPRRplwRBgd1QzqAz6Jxo%2BkhMXxRLDBe7D4jol9DYSdMV3POMZzDcWqn4pCcyRseas8AAlhAQYUyPiq1IHLX36RRhjs4MaFSeB2D5%2BZR4YoeQ9ZMjNTUFBkeuD8tMKGAb8U4nBwlMOfk57wGOqUB7PLzFpzfgZZWVgJqoK52m4NauQGG6a1ZB3PB6OxUGG6vuCggxb8QnEGtYwQF324cst9clMCkLiebi5bpP3gHTU05jl835N8Z4%2FlRSq8UdvHXBWjlJn6zNQ%2FVHI3srZpTZXprvynOkCIvSCjIFZ99WhgtCvY2k6EThVfaee3uczLp8jQMnzPGuL9fJ6YdLgfK5ng1S7s3Rc2vNx%2BNISIsGTudd%2Brt&X-Amz-Signature=1e3fdd789f32d615098da89b524448fe50b92a38d5b1c714254aeec862122988&X-Amz-SignedHeaders=host&x-id=GetObject)
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
