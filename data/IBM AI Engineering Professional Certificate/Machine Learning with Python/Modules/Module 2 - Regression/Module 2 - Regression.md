

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=05c299320b8db48a12ac9b6b9561441efda4c826470491c7a69e1d193d5120c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=07de36c99e4aa7db0db527b14f6f5c9e3925b8d1fe77ab0a58c6e89280ee23f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=c36b26d112e707724d23e6a27b5dcf0f32855c5a8d342715cafc1fb4ec171cde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=2a18cfbb84c10fcb3523203a15fc2373776e9236ccf63afeb67b8f29c8ed3948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=8e3d042a654fab4d93ef5fbb467346c4fb0f9f297f28870f5dda5cbfed59ad22&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=3442ef31ea97716f2aab0c1eb0f4b1f9045c281fdce47b816be5945e09dd418b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=a88a220293b3bc41d1e73b1cfc2abf3c1933df1b48801d1eb51795057a58c34b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MQIK2AS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYb43NxDIHOd6KfqJA5psguptwoekEtskJNlclmkyZMAiA62uPOvBuSY9qAsrE3UdAdQceVDn7a5%2BaE5yjbA7h5ISqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9ILB8WB9jEt%2FqWX9KtwDJrOW3DqXwgwrcZHTQ68aL9L2bIUfmPpyHE5M8Mwht0GZVPNKTD%2FZtETqUcJffbLqhopTwad4YQLKfIkwews8D2ZVpmr8pFn%2BpPqLkPUnCV7hu1JR9sQRufVizXp%2FpSC0Qa9mOoAoroHHeDeKH4tQv8ptc0lcgnpz7L5b5E21w7wR6Qkv7Bu0VzCCy2cnanJRnaQ2iOHsUzRZHaLYZ9oa%2Fh%2FROAmaXmeV1we1G2TX9%2FxRa4Hw5izS98dq%2F7S6CVUmdni1yw9Q2%2FyzvbBF%2FEzq3dLx9aZwdRZlkT%2F5J0a%2FXMOmsOMC2XRXqWfKM4Wd4l5NzSM%2BVkJll8UW7flgVZSxbtlEbJUhP4Ho5abLTX932mjLg%2BpDWGmYrw67P7sNRMnUqXCP4m5Pz9mBd1qVRqaXGpBds0sRnpTlFVIZFnktyR1J5wuY81XFZD%2BUp02HJEqpkgKyqFoCQhr0G3RtDQKaXyxZyEMZ786sNOglhyDi6EoVIG8zMdRE7WFcgSMsV7r4CWfocUal2S4dBO8UM%2B%2F%2BkBEe6VoduIpCODxDehneAytQAPsBy7%2FUZyWdDDcw0xT4MUK8pi9IfmogBOW3BG9hw3JOv9en2eyz6LRZNwoGqqG8ls17KDwJJ1nuIb4wzZv8vAY6pgH4ysLOq4oQT5nfTdZLXsslUgrcrQiMklD1pRE6PnRbSpJ3ESy6AIZGvitbp4DsDeAwRWbY3pz03d2TqxkhY%2FPM6ZWio%2Bki5kNqV9Qf6A%2BQ%2FI5vgUmSK9f4vRTzR%2BSeUbgk8A%2B6RbG5%2FzF1MTEBOzsQ9b9q0MpvrEydzS%2FNy%2F5KnxlT9IdiixxlqNIjHP9p05AdLe1EEsLJ1I40aiLFRiO2LC7p4ZZr&X-Amz-Signature=3e390ac059dd0ee1aaee6d34257ffee1a6130702b6d6f55eb5f81e9e47f4cc97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGJFFZTL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHw2c5k%2BJhJ%2Fj6jnfMFe0hk%2FENasjy6s7WqZraaCOZs5AiEAq4SuaC8z6VDaKGjkueloz8R3E7%2BFMyJb01NugbRSncwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlfFrG9WbHh9%2FfweSrcAymNMTmcrM9mDENr0JkbrkP3pCyEvzGxkKeaJQ9zKEjZTcnnflog6HgJaq2FmD2TrfeBWN6iCRahYHaf5G6aJvvogzxaM%2FWpBvkBUQfBbcWw%2BzZGKEB%2BdHpvfR7OMoxoCvwSHXFdF11FsSLLIEqLkChB5gF01rL44f5T4%2BK%2BlSYIH%2Bl1JQ5aPEXoixQjX%2F7NS7U3E2drhJvI8jNJZ4xB9HgF7pj5OX8IU82401ifW6aWr5klah4yx5ZRUub3m9AiZ3ZEtPOFqa91dNYA44L5Pm%2FpJXi2gkPXDGxobmcCnsWxJj%2BsIa7%2FP2OgMkmyv2XFGvhAq67swPOU7Pppu1ZFxuNvMoBPsvCdOuGU6px3xqtpCWulkNfwmd8LSWya9HZsdqx2aNF3WyGKLKUdFXecxkd4z3MKd%2BZPzwD0g8QKT%2FLvfm%2FlPfoQejAxatxY7TMXG%2FyER4I6NCBTen9cyY32%2BhWjV%2BBdYEor2PNMDkw25sZpDXDl5mqLo7NyDW7bsmIVM%2BffV6H7yWZUxy8pqA6bIGaHAyhU8oc%2BBhx17q0z0OvnL6r917q%2Bdx6v39TMgTQM95mXDVQMIIBQU4XOs93Ur1BCjr4kfb1zMC52hSxVvMzYHyyRVOqO9SFarfVeMOub%2FLwGOqUBTLhroQp55kONI1nT9FcECvKRdQsTwnLCiRQAAa51%2B%2BtnzgbmZvsjQP%2FX6X5lD5LxYMeuYV4XmafZ%2FxJJmaPfLb6CT9HNdnx4PM5HW9nuv2G4mLyvzbgHoJbSBu4sYheO6jA3CqLuBnl5uZVRFyk%2BUHE8cEhnUoG7Hkgq6pG0BirSrR8l5EKOwGRtLDr52f7KQgRBBqdsSWyPz7gmpSwwRjjakdVz&X-Amz-Signature=7ba6bcf76d07ee24034bd323929f96a165ffd54071841f6587265d4a5c80527f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZERMZU3I%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC0wzJMFt5tAO%2Fg42eoU57M1Rk296gWxoeP%2Bo66PCZQIAiAPFhSwy1dN5WyyWxQqEewzAZblKgvutvyzc491ybJ4biqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5jw86j0U04q9nYVKtwDED55kqTqeLhTDYQLMhimzujekXFv%2BSuG%2FicRuC%2F6FSXjyJcVNq5p5VwybBbdJGZq7Dbido3kgIxwrgzPgCbrYeJR9kAFEsqQaYyiziPA3fxEQuXJfk95jVaDTCq6%2BQ5PHG8hhCrKq7ijTU6XI0oOEO%2FeUBP6fTSs%2F0roTJY77rXIMqyuEtAfqoOaK6Bzt%2Bld%2B%2BURafJ8rkYi%2Bxs05Iq1sGPMEMEA4IDdkCIvEolq4ZYP4tPR6Tbn%2BGSzWIGY56hPdoqPIUuCDI3j9SP15p7gSnvQBjGvYCFsao%2F1VCXC%2BcS2aGOZ5NXLdI%2FiTSN33WviUuOIkGMdV0ozj%2F3KpIhgDzyO3kHvqRIbyQ5xYA6RCxHORP3M51slEQS1eFKfmlyjvPyTPsM4B3CJQLSaIz5A0sQwUMUhRZ0b80p6KOOVqh9jjljCsBnHDsB8NxMZv7iQdGQ5aXVrRRFjvnt5q25lJ33OqJL9nSn%2BN8YqsM6sHGI%2FYoW96VE%2BgqAMjtny%2BzZTrtv2Iq5b2qH6Tcv4LVyq9BH%2FRr5jJZpCS6X9uLefrwNxAE4tuobJdd5Ka819REf4Cqflb7KCdfsPSiufe4ybvcp0LBxjZ7WTBpKj3we9fRBbbnMb%2FzQigo3eX5Iwzpv8vAY6pgFc%2FIUMZRmv5pGWBh64KqeHrLU0df%2FW9ifnwpJ9ZHEeq6pnH41rCRr7trPNCIvwPwjdBbcHop8SI2CSO20PM6HTn1aXw0RLDPiPwtKKVSXaCZkKwhy8vPWYPbr3pqprMgevTdpDfL%2FUgPD9sp3%2BdFfkcpXB9vs8%2BIVtkOv19%2BNfHRwXqqujuol7bQwilSbnGumvUiVkOmjFsjJlThSmxN%2FdTjjBeVVV&X-Amz-Signature=44c3c875fc80833977e134481f0da5c4f9586dfeaa559b34425800c4b58fa85b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5HMWG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMRCQ2JWfL3LCCx%2FZXLaKFDqOI7cHgHTapKUtFPFQNwwIhALu2HD219qnleb3iZjXg3%2BAXUdOvM3HAv%2BcFO65hEjbGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHFluY1hJFqR7LSfIq3ANSKgBuXzXNelRgyE2LukQLPb6B%2F2fAEamforuGIl54KkNXn4oA7cT3i%2FV7oVGib0mowuQ3aNd7f%2BMNGagqERbVqrTwdLRYkoWQ7sY9ynY6T1kL5W1mlygSK9Ou35keOfo95CnEffTnsn3UxpSLxoEd4bMltrID9WJxXtOJbGkWGF9iOp9nLCAxklWRaFbcWWqXoZHHsUEXt3jOV7A4BlDGs%2B%2FM6hKP9fDI6tRYJE4%2FxImRjLy%2FVSkxThMuoKO5rn7W6s6Ytx5%2BJSLXM3N6aLAp4qneMhletun1dMMdc0s00pcKOHUaudRnAslHwcDDj7r7434lVnZiaAsWb0Y%2FVhhdjco0XWooKGvMDlG4Iyw3pOqXHy7OTUC1rvAuSCKHYSG8ZqvLaW%2FP2GLZGdwNsc2AdJT3K0B8ticpc6cAaKt2xxZ92ycXgoEWwLOyYJIRyMJLZgFz3t24xM9BNQNhR4hJ1zmSISiu%2BgqcVIZyBBrqLHw1qdPkjngztkXEnCuXJrkuA%2BrSuZWKCxozaqvnLtObZucB46maAhm1Na9b%2FdPx7fB%2B6SuAik6aQZZG%2BxhU2QQJDre8mmG1rRz62imw6hr2JwwIv2PeROnKYcPcK08smZL9OcvcCYdgwNb0tzCmnPy8BjqkAZ3LEO2nwsJ3hHmi%2FiUxfakJRQC0VYzmwxA1MGtnJ1Bcu78l4frNvRg54JThKhwAOik2Jl1BZ81G0aXP54vFsC4W%2Bt02%2B5YwaxDHLUCBqblrRkJv2nRdZ0UuR9nXiAGi%2FxNFLhbN32gkTj%2FkL%2FCedVlsYOwNyG%2BZMVdIvIHHo737x%2BTf8U2acmsPovgkbMtV9xdEJk6mg%2Fjya0dUHuIGjZPy8Zzp&X-Amz-Signature=f91edca053229792b9d3c61918a5b8f5175605d7592743bd6da6d7fdf1032deb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5HMWG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMRCQ2JWfL3LCCx%2FZXLaKFDqOI7cHgHTapKUtFPFQNwwIhALu2HD219qnleb3iZjXg3%2BAXUdOvM3HAv%2BcFO65hEjbGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHFluY1hJFqR7LSfIq3ANSKgBuXzXNelRgyE2LukQLPb6B%2F2fAEamforuGIl54KkNXn4oA7cT3i%2FV7oVGib0mowuQ3aNd7f%2BMNGagqERbVqrTwdLRYkoWQ7sY9ynY6T1kL5W1mlygSK9Ou35keOfo95CnEffTnsn3UxpSLxoEd4bMltrID9WJxXtOJbGkWGF9iOp9nLCAxklWRaFbcWWqXoZHHsUEXt3jOV7A4BlDGs%2B%2FM6hKP9fDI6tRYJE4%2FxImRjLy%2FVSkxThMuoKO5rn7W6s6Ytx5%2BJSLXM3N6aLAp4qneMhletun1dMMdc0s00pcKOHUaudRnAslHwcDDj7r7434lVnZiaAsWb0Y%2FVhhdjco0XWooKGvMDlG4Iyw3pOqXHy7OTUC1rvAuSCKHYSG8ZqvLaW%2FP2GLZGdwNsc2AdJT3K0B8ticpc6cAaKt2xxZ92ycXgoEWwLOyYJIRyMJLZgFz3t24xM9BNQNhR4hJ1zmSISiu%2BgqcVIZyBBrqLHw1qdPkjngztkXEnCuXJrkuA%2BrSuZWKCxozaqvnLtObZucB46maAhm1Na9b%2FdPx7fB%2B6SuAik6aQZZG%2BxhU2QQJDre8mmG1rRz62imw6hr2JwwIv2PeROnKYcPcK08smZL9OcvcCYdgwNb0tzCmnPy8BjqkAZ3LEO2nwsJ3hHmi%2FiUxfakJRQC0VYzmwxA1MGtnJ1Bcu78l4frNvRg54JThKhwAOik2Jl1BZ81G0aXP54vFsC4W%2Bt02%2B5YwaxDHLUCBqblrRkJv2nRdZ0UuR9nXiAGi%2FxNFLhbN32gkTj%2FkL%2FCedVlsYOwNyG%2BZMVdIvIHHo737x%2BTf8U2acmsPovgkbMtV9xdEJk6mg%2Fjya0dUHuIGjZPy8Zzp&X-Amz-Signature=213c61c0cc1a8a7856b7c0125a0ca9451ef59034b60a3dbe2d0848452b071636&X-Amz-SignedHeaders=host&x-id=GetObject)
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
