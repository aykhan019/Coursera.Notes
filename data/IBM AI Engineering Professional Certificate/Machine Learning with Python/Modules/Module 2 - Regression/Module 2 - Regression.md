

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=6836b871282aa4c78f22ad223ab64a72afd8e8b218702b7bc936ddc516d63df0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=4201ed44366546eae67f466edbeca5198baf4d5f5b6adc0abf5d8b082f87d598&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=4468372a0202952079e9fc54d284e8d086884b48b22fdfc09d7504ccdc52929e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=d82b9112dd72f3eea5b174927e1fff3855ae9f039d8291b47fe22153ee4e43c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=311dc1d9bf3a857ff2492ad2ca5bc5f504764ac1140a61cabae2f2acd95dc0a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=32027994f2e767c1bdf94a70f59074f116d7865906d7649c62c678aa34a4f0ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=479fb5468b813742735b5d2d004e6a902f04d3ffa1455acf5c514d1574e60d4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGP7QWQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDtWWf1kv9WNqkpFs36jFcnYStuR4WRSaBC7gpmCx%2BgfAiBj%2BYV8X86v1Ii563%2FqD0MLkAp8YwVeWeF4qrhxaUDI8Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMs1mZOuCS1RMGGGBNKtwD%2B9cz1LMVuN%2BwG%2F1%2BSLw0e%2BZlpuMFBH%2B7czUSrbfdBsGLfl9pW9JiO5YHEGXEm3fuvdOmoFm8NBB8gJK93VJXDVlodAIXVrUowEhotBTwCtEHep4RtvRvtgBjoK0KqiHOAWR6AtFveA%2BqsefdOPzqeo5eBrzMS5Md63L0Sgyu4ansgXk0A6LeToD3rJHZjRX1Rx0YFE2G%2Bi1YDiGnMfJ%2FnHV4Blz77mFtltt2TjNY1lohOQzMoOWLmckUV%2F4rk2vVDubVoEgaz8ZHZKtZTMGkNn9mBm%2FQsp%2B%2BH4F07N8PI7tWTJlwim4HKsynASQt4kz0gGJAbqRG6IGN3twk7mqdGc92kGvbOIi1aLarpUknyl5abLGKKckGkJEDuAuecFm0jBBuY%2BNO76vk2BMxhDvQFbs0Xfn%2BskA7PVeXTxWfb3CG0tiSXykX1LGLd%2BwWWFSRFuC6UPMoTgdZqaIsKQbTaib4ZOaXxH5KEaYmK2lob5Bi5KbYBSJAq2JXbgl%2By0tE1MlflwpWCLcl5gQu3KCpa9xz8NaMRE9Oybi88hBHKjZa7DUClnAOvDG4ZcKGInHFog6Yq%2BWhL%2Bt2HkahUYuzzKSmzWt8KGOoAJWtAxemcSk7qiYtCZ%2FmdPUrHB8w3vmWvQY6pgHNh98yLJ6S0nIpKB7gbE3%2FX6po%2FrRtmxb9wHwwHfl12dz2T8wg6yp4opVt1o031u366xvh40szasJaZGxhzVcU0lJCpJtuaELVZvtlelDWPfCkyr6OSdqcqmDweJNjyTCPh93oQaxQUGBswiTJs8jWBV30jZYUEWYfRnlcD%2FY1G2Sgvpwqbg0TH352vbw2rlvUS%2BWIpbCnBKZPgQMSi%2FOx6lfYFZ9E&X-Amz-Signature=fe1a1aa2410adb2bd5eca84c45d9da6cef221b8e421a2b4ff0b782fb5817c625&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WM4ZBF5J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCLzqhmgfkP12jnsfApd1vEvAxIwEGNUNloSqXkC0hMYgIgClIxY1OALEcP%2BUojfKhepfXbNfYpKygJQA4U%2FULUo3sq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDH7DFCKhKcOt0ae2eCrcAxDu22rc4htStOHjIGQ3YjMx8%2B2TIDmessCN2JgynYDDbr6qZ%2FYpeOFxxpyJWFE%2Fx6amd4MzKv9KW9FS07FetdCM0XUM1KHdcazUJRFhjnOmlZTDaSaBRltW4%2FtlDMx6dIOlXOfzWXXmApEdSM%2Bg5V9Wfi8nNnN9pPqHU7WvxZQbu3AJX7XycbsgODa%2FUwQlMIkCoJPM1JJPcXozWete4k71j945uxM0eIB9xsduH4B8S7lUg6wjmjrdv4ZG9qO7osyIOqWicg%2Bf3fweT3YCtBqiEmy1Zt%2B%2BL9h4pyMwK92p2FCB0lsis%2FG7i%2FpJBVG4Wz1WAQjhx62OWQjO8ast3crofT9gnQ39bS%2BtT0%2BvkXDgt1XRsSd1fWCJ63IQJV0WzHR8svDXfuC3BPtdBbDBJcJV1WlJWqbwrlVWfdAanYS9HZNeUdwIcgk%2F856iS5hFlw7ukdvkcNqPZYiPYtUEnu8KyAFFIQin9QTs0%2F3XYwBgmpNXWfAU0Y5NxyckqI%2FvlJIbN749chjAOHZRC6pv%2BmCb2EeNiEz8HA63rcSadEC6aJ3bRlhDTyi21wqPtgBH8%2FGRJkpLbqPvz%2BcLb7AOKTxtZ1qgh0iHSGZvF2quhIExY9XUA%2FeAys2RIxj%2FMNX5lr0GOqUBdNqznYNMAu2uo06JBzAoYXXbqyoSw%2Fj5n754TwbxCQi2W%2FMMmmYMmYxVUyr71w%2FlXB3YJqTcizzo916BxgDoBDekWJjzZMuGcnbxq13M8EIsUH%2BuZMM2X2kwuC8czSXEUkEmGAzkcojAq6CnzpyMUi9LK58Tgpx%2FJ6j9SB%2FP2v4MSIkSvdnsWUyNrTWwnUH8olEzimMhm2bdUVHyN9oylDWN8Y8G&X-Amz-Signature=e5ca408e7b93a5d8d72cb776c172cdc1f726d293b64705fae668b0e0c91fa1fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTLU2II4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQD5WnZsjtID6mI7JgV7DrGfCUaEbMkau47ifGYd60ATawIhAKbQ78Q4P3lKXEbYapOloAqz%2Fri8lv6%2FAGzbN6VrK50hKv8DCHEQABoMNjM3NDIzMTgzODA1IgyMqrYoWZu4oH61dhQq3AMnjGbEeRk%2Bknt3SPhhdsD2QI6eGcxClpjA%2B8tLUU9wQN1%2BbBYpy3zjYIPiJO%2B63VnEC5DDLoDXatXVWwnVjbRj08WDZb0eWHoP%2FQN48HPdxLohimPuu27hrfbU0GQy6GWj2FD5Xygmfe9UY6S57Nyswi1vYB20KstpOJln6jNN8Z9wY8JcbztlBCvgFOxFl3mKyZXP0FqvSUnhImmg5Kzi3uD%2F9Q7UMpdCGgAaswOoOzK3yP7SAelFiAsMoCsNrbLX5hAxoX08ww3WHsa%2B6UdIB4rFrVzVwkERkBB6d6I1trcPwmCqk6g%2FQgMhtITvoeruhmR4nHxk5fW8BbhKLzg%2FCD0LCl2Bs2zjbnZvdAx%2B24V6NK%2F9PpiaEacEacPTZ4kL8s9cii3%2BoKUs9IiPhqPryhyCpNSUWqOJpwj%2FdRU%2FgRjf4rTl1I9PKaHi%2FWoU4oLEkXrw14DP37zk0CxFmSR1%2B4e2E%2Fug27TGBzJHBknkDZn3%2BNwHT0m8pzwzxwDbkDDPu5Vm%2B5XG4weLe1CWGG4Kz2kawyKk4DiAr%2B4Zjfxw8%2FkT11YCWlwMgxU7B0gIo%2FAgwz8hvJNnUkNUg39beZP7gsRqApFNHXS4llnhqya3IGmjBWkDDZi2Y%2ByEZTDr%2BZa9BjqkAUUMVxNfORFFnUjl1nc9%2FanbtAt1cflsm2rnT0zhlxyRu8bsX2v1iowWFhtmlvVhVo7upwsK%2FcILiKg2saY2YcewRxtXg5EPqUalKdrTz%2B7GFtYR7%2FYNlJ7dtJRtV9XiEpygQQ93YVmuQc7yJxoRNyk1g336Az0y5xrwzyUwLSGjNthp5CqMykvBKlKzQ0IGgVCi7PS1RyR5LHeebMgZBiKvGZJU&X-Amz-Signature=e2be23871dcece055c70a9db520d7d5d94347ed59cbd18f6067d301208b81f30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=2788532317aa589274684ffbb83e1e126a077b4cfea7ce9ad2d2f3eb99027cff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=8462b1630475cf8889cf29168ce5119101965bb973ccde443b00bf74f46aac0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
