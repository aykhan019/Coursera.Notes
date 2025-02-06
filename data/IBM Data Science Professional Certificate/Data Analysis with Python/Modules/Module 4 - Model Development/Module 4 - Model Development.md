

# Module 4: Model Development
## Introduction to Model Development
This module delves into the process of model development, focusing on predictive modeling using datasets. It covers various regression techniques, model evaluation methods, and the importance of accurate data in making predictions.
### Key Concepts
#### **1. Simple and Multiple Linear Regression**:
- Use linear regression to predict outcomes based on one or more independent variables.
#### **2. Model Evaluation Using Visualization**:
- Visually assess the performance of models.
#### **3. Polynomial Regression and Pipelines**:
- Employ polynomial regression to capture non-linear relationships and implement pipelines for streamlined model building.
#### **4. R-squared and Mean Squared Error (MSE)**:
- Evaluate model performance using metrics such as R-squared and MSE to determine prediction accuracy.
#### **5. Prediction and Decision Making**:
- Utilize models to make informed predictions and decisions based on the data.
### Importance of Data
A model, or estimator, is essentially a mathematical equation that predicts a value based on one or more other values. It relates one or more independent variables (features) to dependent variables (outcomes). The accuracy of the model often improves with the relevance and quantity of data. Including multiple independent variables can lead to more precise predictions.
For instance, consider a scenario where predicting an outcome is based on several features. If the model's independent variables do not include a crucial feature, predictions may be inaccurate. Therefore, gathering more relevant data and exploring different types of models is cru1cial for robust model development.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=3e041b3f17441df5d96ea985daece51cb49e00b1d6e99e4c29a158735a260cf7&X-Amz-SignedHeaders=host&x-id=GetObject)
___

## **1. Simple and Multiple Linear Regression**
### Linear Regression
Linear regression predicts a target value using one or more independent variables.
### 1.1 Simple Linear Regression (SLR)
SLR examines the relationship between two variables:
- Predictor (independent variable $ x $)
- Target (dependent variable $ y $)
The relationship is defined as:
$ y = b_0 + b_1 x $
- $ b_0 $: Intercept
- $ b_1  $: Slope
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=1004d8a894795af5e29128c0be9845f0043ad82a25a42edf433c8ebbdc3d779f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Step
If highway miles per gallon is 20, a linear model might predict the car price as $22,000, assuming a linear relationship.
#### Training the Model
Data points are stored in data frames or NumPy arrays. The predictor values ($ x $) and target values    ($ y $) are stored separately. The model is trained using these data points to determine the parameters $ b_0 $ and .
#### Handling Uncertainty
Factors like car make and age influence car prices. Uncertainty in the model is addressed by adding a small random value (noise) to the line. The noise is usually a small positive or negative value.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor (x) and target (y) variables
x = ...
y = ...

# Fit the model
lm.fit(x, y)

# Make predictions
predicted_values = lm.predict(x)

# Model parameters
intercept = lm.intercept_
slope = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=e57246c11a3cc6102e8e596183a160263fd29db7a6975b2115b34925b6c3c27a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=ebaec01c387083a08eef781595ac0583b4ffb12e51818f25ea339198b84558d9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Visualization and Training
With two predictor variables ($ x_1 $ and ), data points are mapped on a 2D plane, and () values are mapped vertically.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor variables (z) and target (y)
z = ...
y = ...

# Fit the model
lm.fit(z, y)

# Make predictions
predicted_values = lm.predict(z)

# Model parameters
intercept = lm.intercept_
coefficients = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=6125f2fef2b3689cbfb12d495b0f4d10c1fc012ac1ce770c55596e7975e0251c&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=b48cde5180e5afd56a8c4a2bf1eeb04e4c09bd02cabc860dcedf3a297719c0b0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 2. Model Evaluation Using Visualization
### 1. Regression Plots
Regression plots estimate the relationship between two variables, showing the strength and direction of the correlation.
- **Horizontal Axis**: Independent variable.
- **Vertical Axis**: Dependent variable.
- **Points**: Represent different target points.
- **Fitted Line**: Represents predicted values.
#### Creating a Regression Plot
1. **Import Seaborn**:
```python
import seaborn as sns
```
2. **Use **`**regplot**`** Function**:
	- **Parameters**:
		- `x`: Independent variable column.
		- `y`: Dependent variable column.
		- `data`: Name of the DataFrame.
```python
sns.regplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=e9e714bcfa9a5947020b49a120fa7f22cc2d9bf7fde1d2f639d4060b4249bc42&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. Residual Plots
Residual plots represent the error between actual and predicted values.
- **Process**:
	- Subtract predicted value from actual target value.
	- Plot the error on the vertical axis, dependent variable on the horizontal axis.
- **Insights**:
	- Zero mean distributed evenly around the x-axis indicates a linear model.
	- Curvature in residuals suggests a nonlinear model.
#### Creating a Residual Plot
3. **Import Seaborn**:
```python
import seaborn as sns
```
4. **Use **`**residplot**`** Function**:
	- **Parameters**:
		- Series of dependent variable (feature).
		- Series of target variable.
```python
sns.residplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=76c5f9ab86bb8b0cda1e60d798c1fc9d1a48251b4f368d78fe38f9ef10c92a14&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=d8007350016971c1451ef35c684c5b1b61aefcf82ef679dbf8d51591324eb3f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Distribution Plots
Distribution plots visualize predicted versus actual values.
- **Use**: Helpful for models with multiple independent variables.
#### Process
- Count and plot the predicted points approximately equal to a target value.
- Repeat for various target values.
#### Creating a Distribution Plot
5. **Import Pandas** and **Seaborn**:
```python
import pandas as pd
import seaborn as sns
```
6. **Use Seaborn's Distribution Plot**:
	- **Parameters**:
		- `hist`: Set to `False` for a distribution.
		- `color`: Set to desired color.
		- `label`: Include label for legend.
```python
sns.kdeplot(predicted_values, color='blue', label='Predicted')
sns.kdeplot(actual_values, color='red', label='Actual')
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=591f24100c8f4628ee64fcf763d7caaac9c0a7f10228c973a337ff2233c016ec&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=9000dfcc203e7bbbaaea7817551db69b4a427ea25d064a46b3fb51ed8ac6a05f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Types of Polynomial Models
- **Quadratic (2nd Order)**: Includes squared terms.
- **Cubic (3rd Order)**: Includes cubed terms.
- **Higher-Order**: Used for complex relationships.
#### Example Model
- **3rd Order Polynomial**:
$$ −1.557x^3+204.8x^2+8965x+1.37×105 $$
#### Implementation in Python
- **Using NumPy**:
```python
import numpy as np
coefficients = np.polyfit(x, y, 3)
```
- **For Multidimensional**:
Use `scikit-learn` for more complex models.
#### Polynomial Features with Scikit-learn
7. **Import the Library**:
```python
from sklearn.preprocessing import PolynomialFeatures
```
8. **Create Polynomial Features**:
```python
from sklearn.linear_model import LinearRegression

# Create a PolynomialFeatures object with the desired degree
poly = PolynomialFeatures(degree=3)

# Fit and transform your data
X_poly = poly.fit_transform(X)

# Create LinearRegression model
model = LinearRegression()

# Fit the model with the polynomial features
model.fit(X_poly, y)
```
In this code:
- `degree=3` specifies the degree of the polynomial features.
- `fit_transform(X)` generates the polynomial features for your dataset `X`.
### Normalization
#### Why Normalize?
- **Purpose**: Standardize data for better model performance.
#### How to Normalize
- **Using StandardScaler**:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
```
### Pipelines
#### What are Pipelines?
- **Purpose**: Efficiently automate data preprocessing and model training.
- **Benefit**: Simplifies complex workflows by chaining multiple steps into a single process.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646B6HTT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHpo9sB0MWJAptuMZAIyraiBIaqwxyPuXUxtfnMjPmU6AiBvHbjA52P306EZsclMAPfYDS4s1nFJishZnInR3syLFCr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMLmgPlenKO2I6XG8zKtwDTuT13gl6wmwV1lAn6GMj1wrs1IVfqX3SFebsNZpj%2BMR2Qv7CtBxlQSFuIrh19Elo87Y%2B7BPgZ4BuBDikNXbtGlKoE2CYJj127P0szH2uwiDLsJshUEsRmIV77iSuipuHQnd2zjly%2BVP4UpXuwAFnq2B0eAepevNOE7xLn7Xb3xUFmlrTu2WkSYll10PbEEdOlWTj7G5VvcgdwA0dwEcG3w7%2Bhbx7k2Pb6XS1Qdql2QBA9GOXoVG%2Fu58MR%2Fb5HjOyL5kNeq15iFO3SQqyYkZXa%2Bfuz4KgBL3A2I8OHzfEFFjj%2FJeHW2xWnV9QbuzZEJ1EyhGYaPs2%2B0XLmDA6PdAOozJYziV3b3Z0Xh0180M%2BV3Y0m2FTFua5mPxK5J6HId4PCc3SKfAxdD93C1nlT%2FA0YgR34flLD2ZcDX5skJ%2FPhRmolDg37jrOj4dhfGxufjoPfFQvletuebfIZfB%2F%2Bhb0VZymTV597nioZSRW%2FF4x%2BmYKkNHrXvNPAAhIOqCn0p4mBtrcYCrTP%2F%2BzJrxLVjcgcVFMp18eOiwWQRXW0s3BBr1Se7znoxflJIgqN6O6oATPdcGzsWzO6OXNLbEqHl%2FL1UYt8iOiQfifryODCDf9jhovBGSQoCxpYjCGUuIwv7iUvQY6pgEaqvv%2BB1WfhmceqLeGayg3%2FbyVasWsDbz5Omos922beR1CWK%2BozKUhSiAlwBGklC3D3eB7QbbYwpSG%2Buv0Dg%2F%2FP%2B9EyALDRI2wRLwpKNvPcc1U2EMywP1nx7qWXeewjHIoi3mRqGr29M8Jj8YhOxrwrTi4v2isbh7oRrp8GyaDAbY1m8dVerbRTP6uhAGhouxXcao9J1Ja7VT1mLuFDVbwFq8UKa3I&X-Amz-Signature=ba033873345a777e3dd2cad0562cd6e0e005afca13dc5756406f072fd6d5694d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Benefits
- **Efficiency**: Simplifies code by chaining steps.
- **Maintainability**: Makes workflow clearer.
#### Creating a Pipeline
9. **Import Pipeline**:
```python
from sklearn.pipeline import Pipeline
```
10. **Define Steps**:
```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=3)),
    ('model', LinearRegression())
])
```
11. **Train and Predict**:
```python
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
```
#### Key Points
- **Sequential Processing**: Automates the flow from preprocessing to prediction.
- **Versatile**: Easily adjust steps and parameters.
Use polynomial regression and pipelines to enhance model accuracy and streamline your machine learning workflow.

### Note:
#### Simple Linear Regression (SLR)
- **Definition**: Models the relationship between two variables by fitting a linear equation.
- **Equation**: $ y = b_0 + b_1x $
- **Use Case**: One independent variable predicts a dependent variable.
#### Multiple Linear Regression (MLR)
- **Definition**: Extends SLR to include multiple independent variables.
- **Equation**: $ y=b_0+b_1x_1+b_2x_2+…+b_nx_n $
- **Use Case**: Accounts for multiple factors affecting the outcome.
#### Polynomial Regression
- **Definition**: A form of regression where the relationship is modeled as an nth degree polynomial.
- **Equation**: $ y = b_0 + b_1x + b_2x^2 + \ldots + b_nx^n $
- **Use Case**: Captures non-linear relationships by transforming features.
#### Key Differences
- **SLR**: Linear relationship with one predictor.
- **MLR**: Linear relationships with multiple predictors.
- **Polynomial Regression**: Non-linear relationships using polynomial terms.
#### Example Code
```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Simple Linear Regression
X_slr = np.array([[20], [30], [40]])
y_slr = np.array([15000, 13000, 12000])

model_slr = LinearRegression()
model_slr.fit(X_slr, y_slr)
predicted_slr = model_slr.predict([[30]])
print("SLR Predicted Price:", predicted_slr[0])

# Multiple Linear Regression
X_mlr = np.array([[20, 5], [30, 4], [40, 6]])
y_mlr = np.array([15000, 13000, 12000])

model_mlr = LinearRegression()
model_mlr.fit(X_mlr, y_mlr)
predicted_mlr = model_mlr.predict([[30, 5]])
print("MLR Predicted Price:", predicted_mlr[0])

# Polynomial Regression
X_poly = np.array([[20], [30], [40]])
y_poly = np.array([15000, 13000, 12000])

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

model_poly = LinearRegression()
model_poly.fit(X_poly_transformed, y_poly)
predicted_poly = model_poly.predict(poly.transform([[30]]))
print("Polynomial Predicted Price:", predicted_poly[0])
```
___
## 4. Model Evaluation Metrics
### Mean Squared Error (MSE)
- **Definition**: Measures the average squared difference between actual and predicted values. It indicates how close predictions are to the actual values.
- **Formula**: $  \text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2 $
- **Python**: Use `mean_squared_error` from `sklearn.metrics`.
#### Example
**Scenario**: Predicting house prices based on size.
- **Actual Prices**: [200, 250, 300]
- **Predicted Prices**: [210, 240, 310]
**Calculation**:
$ \text{MSE} = \frac{1}{3} ((200-210)^2 + (250-240)^2 + (300-310)^2) = \frac{1}{3} (100 + 100 + 100) = 100
 $
**Python Code**:
```python
from sklearn.metrics import mean_squared_error

actual = [200, 250, 300]
predicted = [210, 240, 310]
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)  # Output: MSE: 100.0
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646B6HTT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHpo9sB0MWJAptuMZAIyraiBIaqwxyPuXUxtfnMjPmU6AiBvHbjA52P306EZsclMAPfYDS4s1nFJishZnInR3syLFCr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMLmgPlenKO2I6XG8zKtwDTuT13gl6wmwV1lAn6GMj1wrs1IVfqX3SFebsNZpj%2BMR2Qv7CtBxlQSFuIrh19Elo87Y%2B7BPgZ4BuBDikNXbtGlKoE2CYJj127P0szH2uwiDLsJshUEsRmIV77iSuipuHQnd2zjly%2BVP4UpXuwAFnq2B0eAepevNOE7xLn7Xb3xUFmlrTu2WkSYll10PbEEdOlWTj7G5VvcgdwA0dwEcG3w7%2Bhbx7k2Pb6XS1Qdql2QBA9GOXoVG%2Fu58MR%2Fb5HjOyL5kNeq15iFO3SQqyYkZXa%2Bfuz4KgBL3A2I8OHzfEFFjj%2FJeHW2xWnV9QbuzZEJ1EyhGYaPs2%2B0XLmDA6PdAOozJYziV3b3Z0Xh0180M%2BV3Y0m2FTFua5mPxK5J6HId4PCc3SKfAxdD93C1nlT%2FA0YgR34flLD2ZcDX5skJ%2FPhRmolDg37jrOj4dhfGxufjoPfFQvletuebfIZfB%2F%2Bhb0VZymTV597nioZSRW%2FF4x%2BmYKkNHrXvNPAAhIOqCn0p4mBtrcYCrTP%2F%2BzJrxLVjcgcVFMp18eOiwWQRXW0s3BBr1Se7znoxflJIgqN6O6oATPdcGzsWzO6OXNLbEqHl%2FL1UYt8iOiQfifryODCDf9jhovBGSQoCxpYjCGUuIwv7iUvQY6pgEaqvv%2BB1WfhmceqLeGayg3%2FbyVasWsDbz5Omos922beR1CWK%2BozKUhSiAlwBGklC3D3eB7QbbYwpSG%2Buv0Dg%2F%2FP%2B9EyALDRI2wRLwpKNvPcc1U2EMywP1nx7qWXeewjHIoi3mRqGr29M8Jj8YhOxrwrTi4v2isbh7oRrp8GyaDAbY1m8dVerbRTP6uhAGhouxXcao9J1Ja7VT1mLuFDVbwFq8UKa3I&X-Amz-Signature=b40f2e1f1199eeffdd0653c268d1d84d250a65c2a73b8fbcb6c18fafc059ebf4&X-Amz-SignedHeaders=host&x-id=GetObject)
### R-squared (Coefficient of Determination)
- **Definition**: Indicates how well the data fits the regression line. Values range from 0 to 1, with values closer to 1 indicating a better fit.
- **Formula**: $ R^2 = 1 - \frac{\text{MSE of regression}}{\text{MSE of mean}} $
- **Python**: Use `score` method in the linear regression object.
#### Example
**Scenario**: Predicting test scores based on study hours.
**Interpretation**:
- **Good Fit**: R² = 0.9 (90% of variance explained)
- **Poor Fit**: R² = 0.2 (20% of variance explained)
**Python Code**:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 3, 5])
model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print("R-squared:", r_squared)  # Output: R-squared: 0.9642857142857143
```
#### Example Interpretation
- **Good Fit**: Small MSE for regression, larger for mean → $ R^2 $ near 1.
- **Poor Fit**: Similar MSE for regression and mean → $ R^2 $ near 0.
- **Negative **$ R^2 $: Possible overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646B6HTT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHpo9sB0MWJAptuMZAIyraiBIaqwxyPuXUxtfnMjPmU6AiBvHbjA52P306EZsclMAPfYDS4s1nFJishZnInR3syLFCr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMLmgPlenKO2I6XG8zKtwDTuT13gl6wmwV1lAn6GMj1wrs1IVfqX3SFebsNZpj%2BMR2Qv7CtBxlQSFuIrh19Elo87Y%2B7BPgZ4BuBDikNXbtGlKoE2CYJj127P0szH2uwiDLsJshUEsRmIV77iSuipuHQnd2zjly%2BVP4UpXuwAFnq2B0eAepevNOE7xLn7Xb3xUFmlrTu2WkSYll10PbEEdOlWTj7G5VvcgdwA0dwEcG3w7%2Bhbx7k2Pb6XS1Qdql2QBA9GOXoVG%2Fu58MR%2Fb5HjOyL5kNeq15iFO3SQqyYkZXa%2Bfuz4KgBL3A2I8OHzfEFFjj%2FJeHW2xWnV9QbuzZEJ1EyhGYaPs2%2B0XLmDA6PdAOozJYziV3b3Z0Xh0180M%2BV3Y0m2FTFua5mPxK5J6HId4PCc3SKfAxdD93C1nlT%2FA0YgR34flLD2ZcDX5skJ%2FPhRmolDg37jrOj4dhfGxufjoPfFQvletuebfIZfB%2F%2Bhb0VZymTV597nioZSRW%2FF4x%2BmYKkNHrXvNPAAhIOqCn0p4mBtrcYCrTP%2F%2BzJrxLVjcgcVFMp18eOiwWQRXW0s3BBr1Se7znoxflJIgqN6O6oATPdcGzsWzO6OXNLbEqHl%2FL1UYt8iOiQfifryODCDf9jhovBGSQoCxpYjCGUuIwv7iUvQY6pgEaqvv%2BB1WfhmceqLeGayg3%2FbyVasWsDbz5Omos922beR1CWK%2BozKUhSiAlwBGklC3D3eB7QbbYwpSG%2Buv0Dg%2F%2FP%2B9EyALDRI2wRLwpKNvPcc1U2EMywP1nx7qWXeewjHIoi3mRqGr29M8Jj8YhOxrwrTi4v2isbh7oRrp8GyaDAbY1m8dVerbRTP6uhAGhouxXcao9J1Ja7VT1mLuFDVbwFq8UKa3I&X-Amz-Signature=2331f1117556bb49390e8731b4b186faacd7835e62be400287730ed68b95f78e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646B6HTT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHpo9sB0MWJAptuMZAIyraiBIaqwxyPuXUxtfnMjPmU6AiBvHbjA52P306EZsclMAPfYDS4s1nFJishZnInR3syLFCr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMLmgPlenKO2I6XG8zKtwDTuT13gl6wmwV1lAn6GMj1wrs1IVfqX3SFebsNZpj%2BMR2Qv7CtBxlQSFuIrh19Elo87Y%2B7BPgZ4BuBDikNXbtGlKoE2CYJj127P0szH2uwiDLsJshUEsRmIV77iSuipuHQnd2zjly%2BVP4UpXuwAFnq2B0eAepevNOE7xLn7Xb3xUFmlrTu2WkSYll10PbEEdOlWTj7G5VvcgdwA0dwEcG3w7%2Bhbx7k2Pb6XS1Qdql2QBA9GOXoVG%2Fu58MR%2Fb5HjOyL5kNeq15iFO3SQqyYkZXa%2Bfuz4KgBL3A2I8OHzfEFFjj%2FJeHW2xWnV9QbuzZEJ1EyhGYaPs2%2B0XLmDA6PdAOozJYziV3b3Z0Xh0180M%2BV3Y0m2FTFua5mPxK5J6HId4PCc3SKfAxdD93C1nlT%2FA0YgR34flLD2ZcDX5skJ%2FPhRmolDg37jrOj4dhfGxufjoPfFQvletuebfIZfB%2F%2Bhb0VZymTV597nioZSRW%2FF4x%2BmYKkNHrXvNPAAhIOqCn0p4mBtrcYCrTP%2F%2BzJrxLVjcgcVFMp18eOiwWQRXW0s3BBr1Se7znoxflJIgqN6O6oATPdcGzsWzO6OXNLbEqHl%2FL1UYt8iOiQfifryODCDf9jhovBGSQoCxpYjCGUuIwv7iUvQY6pgEaqvv%2BB1WfhmceqLeGayg3%2FbyVasWsDbz5Omos922beR1CWK%2BozKUhSiAlwBGklC3D3eB7QbbYwpSG%2Buv0Dg%2F%2FP%2B9EyALDRI2wRLwpKNvPcc1U2EMywP1nx7qWXeewjHIoi3mRqGr29M8Jj8YhOxrwrTi4v2isbh7oRrp8GyaDAbY1m8dVerbRTP6uhAGhouxXcao9J1Ja7VT1mLuFDVbwFq8UKa3I&X-Amz-Signature=a762ee4dca20698806a40d200e81aa054165df0f3574eb8c481d061bad7ffdd2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example: Predicting Car Price
- **Scenario**: Predict price for a car with 30 highway mpg.
- **Result**: Price = $13,771.30 (reasonable value).
#### Coefficient Interpretation
An increase of 1 mpg decreases price by $821.
#### Potential Issues
Unrealistic predictions may indicate:
- Incorrect assumptions
- Lack of data in certain ranges
### Generating Predictions
- Use NumPy's `arange` to create sequences for prediction.
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[20], [30], [40]])
y = np.array([15000, 13000, 12000])

# Model training
model = LinearRegression()
model.fit(X, y)

# Generating a sequence for prediction
mpg_values = np.arange(1, 101, 1)  # From 1 to 100 with step 1
predicted_prices = model.predict(mpg_values.reshape(-1, 1))

# Example prediction for 30 mpg
predicted_price = model.predict([[30]])
print("Predicted Price:", predicted_price[0])
```
#### Explanation
- `**np.arange(1, 101, 1)**`: Creates an array from 1 to 100 with a step of 1.
- `**reshape(-1, 1)**`: Reshapes the array for prediction.
### Visualization Techniques
- **Regression Plot**: Shows data trend and potential non-linear behavior.
- **Residual Plot**: Curvature indicates non-linear relationships.
- **Distribution Plot**: Highlights prediction accuracy in certain ranges.
### Evaluating Models
#### Mean Squared Error (MSE)
- **Interpretation**: Average squared difference between actual and predicted values.
**Example MSEs:**
- 495 (good fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676B5GUVU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCKbX%2BUB6G7ELoG8sEEYVyy1PgsOpVp3adnfqOTyTUbSAIgIqNLtvwtQcsss9BZksJD3MeGAOASPFA6hoM2%2FVkn%2Fjoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAD0HoUuC8D4FJHI4ircA8UPcmQrqW6v2d6vWn%2BCAVBzSl%2BiDyW5cNIu%2F%2Bu7SNTp7znO37PVtgVIr2Mwqj6gZVBsXIWsVt2weOgNuZvJqeNXtVBWMc96c6A7o2MYG0ej%2BgQiJE2UWPWoRfl03QyFINvXG8HX%2B5dkzHIk6hrsVh734qvvyaNTiWimyCnDLKPzBzf2MTHDAZmCyDY%2FgA3VW5%2BFRLIGaVCB8iTC3YZpSxNkbOvhWYwcvTTPGE7Dz4EzUQ%2BgeAjf8zyBOioEFuDXqNHNFUmFY1nPej1O1obAqqcxm7PMR%2B51U6EMAbXXMtESgrGh4zp9lKuh0SrkS2%2Bn%2FtlAIkQ9qA7zgyvHNY800EyBvDguY9lp%2BT3ktEsRCWuAcT2gIzZ2Zkl90QlWPr%2BjnPY3hKIoipjYyn2ADp52eQOTzNxgBVXMFmYjujjKfH2Gxt7uyEsXCY%2BYLortsnX8VyW9mYAvdkyk4mqKPx9rwSoOl53AofnibR7ienYXGoSasz81K3GMfwXY7MzdNcoBdgzTalFi2NIjWqFgitDUGIR%2FtCvBSl9eFH9gpE%2BzBdD%2FmHcmSxDaJ%2BXdiTJgPegjGg7gxJkblLzGww3RwLOYvv%2FSZasT7RKQ1r8uagYjS272WOkouYOubkmf90lPMOW3lL0GOqUBG90pO0ZorfbX8zRAEr1FxGwcftaTEQ3R%2BXtQCjHrLjKq9Zhf2gkkNZrhA9GCeuN5XjRuKJ9AzYJa7Mz5OBAL1oB8VS2odsJ%2BxQH9GcStqIXo0kZmT7rFT8OCUnb09aFmay4vagZeF76gCnv1OenLhgZ43%2FPKmhqgCJXRfzmPd97Co943ThjLZtH1kNPUEju4qKG5Pm2lcnPRvHpkIPjKmeUdPdVL&X-Amz-Signature=f820283b816f3aa6a001517660de0a10c2ef1b201b6de0a66bf378fca6737ce2&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676B5GUVU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCKbX%2BUB6G7ELoG8sEEYVyy1PgsOpVp3adnfqOTyTUbSAIgIqNLtvwtQcsss9BZksJD3MeGAOASPFA6hoM2%2FVkn%2Fjoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAD0HoUuC8D4FJHI4ircA8UPcmQrqW6v2d6vWn%2BCAVBzSl%2BiDyW5cNIu%2F%2Bu7SNTp7znO37PVtgVIr2Mwqj6gZVBsXIWsVt2weOgNuZvJqeNXtVBWMc96c6A7o2MYG0ej%2BgQiJE2UWPWoRfl03QyFINvXG8HX%2B5dkzHIk6hrsVh734qvvyaNTiWimyCnDLKPzBzf2MTHDAZmCyDY%2FgA3VW5%2BFRLIGaVCB8iTC3YZpSxNkbOvhWYwcvTTPGE7Dz4EzUQ%2BgeAjf8zyBOioEFuDXqNHNFUmFY1nPej1O1obAqqcxm7PMR%2B51U6EMAbXXMtESgrGh4zp9lKuh0SrkS2%2Bn%2FtlAIkQ9qA7zgyvHNY800EyBvDguY9lp%2BT3ktEsRCWuAcT2gIzZ2Zkl90QlWPr%2BjnPY3hKIoipjYyn2ADp52eQOTzNxgBVXMFmYjujjKfH2Gxt7uyEsXCY%2BYLortsnX8VyW9mYAvdkyk4mqKPx9rwSoOl53AofnibR7ienYXGoSasz81K3GMfwXY7MzdNcoBdgzTalFi2NIjWqFgitDUGIR%2FtCvBSl9eFH9gpE%2BzBdD%2FmHcmSxDaJ%2BXdiTJgPegjGg7gxJkblLzGww3RwLOYvv%2FSZasT7RKQ1r8uagYjS272WOkouYOubkmf90lPMOW3lL0GOqUBG90pO0ZorfbX8zRAEr1FxGwcftaTEQ3R%2BXtQCjHrLjKq9Zhf2gkkNZrhA9GCeuN5XjRuKJ9AzYJa7Mz5OBAL1oB8VS2odsJ%2BxQH9GcStqIXo0kZmT7rFT8OCUnb09aFmay4vagZeF76gCnv1OenLhgZ43%2FPKmhqgCJXRfzmPd97Co943ThjLZtH1kNPUEju4qKG5Pm2lcnPRvHpkIPjKmeUdPdVL&X-Amz-Signature=83f9dc566062fbf521a0762d6c513b3a357249e076e9664c6ebae7fad4c74207&X-Amz-SignedHeaders=host&x-id=GetObject)

**Code Example:**
```python
from sklearn.metrics import mean_squared_error

# Actual and predicted values
actual = [15000, 13000, 12000]
predicted = model.predict(X)

# Calculate MSE
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)
```

#### R-squared (R²)
- **Definition**: Indicates how well data fits the regression line.
Example R² Values:
- 0.9986 (excellent fit)
- 0.61 (weak linear relation)
```python
# Calculate R-squared
r_squared = model.score(X, y)
print("R-squared:", r_squared) 
```
### Model Comparison
- **MLR vs. SLR**: More variables can lower MSE, but not always a better fit.
- **Polynomial Regression**: Generally has lower MSE compared to linear regression.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676B5GUVU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCKbX%2BUB6G7ELoG8sEEYVyy1PgsOpVp3adnfqOTyTUbSAIgIqNLtvwtQcsss9BZksJD3MeGAOASPFA6hoM2%2FVkn%2Fjoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAD0HoUuC8D4FJHI4ircA8UPcmQrqW6v2d6vWn%2BCAVBzSl%2BiDyW5cNIu%2F%2Bu7SNTp7znO37PVtgVIr2Mwqj6gZVBsXIWsVt2weOgNuZvJqeNXtVBWMc96c6A7o2MYG0ej%2BgQiJE2UWPWoRfl03QyFINvXG8HX%2B5dkzHIk6hrsVh734qvvyaNTiWimyCnDLKPzBzf2MTHDAZmCyDY%2FgA3VW5%2BFRLIGaVCB8iTC3YZpSxNkbOvhWYwcvTTPGE7Dz4EzUQ%2BgeAjf8zyBOioEFuDXqNHNFUmFY1nPej1O1obAqqcxm7PMR%2B51U6EMAbXXMtESgrGh4zp9lKuh0SrkS2%2Bn%2FtlAIkQ9qA7zgyvHNY800EyBvDguY9lp%2BT3ktEsRCWuAcT2gIzZ2Zkl90QlWPr%2BjnPY3hKIoipjYyn2ADp52eQOTzNxgBVXMFmYjujjKfH2Gxt7uyEsXCY%2BYLortsnX8VyW9mYAvdkyk4mqKPx9rwSoOl53AofnibR7ienYXGoSasz81K3GMfwXY7MzdNcoBdgzTalFi2NIjWqFgitDUGIR%2FtCvBSl9eFH9gpE%2BzBdD%2FmHcmSxDaJ%2BXdiTJgPegjGg7gxJkblLzGww3RwLOYvv%2FSZasT7RKQ1r8uagYjS272WOkouYOubkmf90lPMOW3lL0GOqUBG90pO0ZorfbX8zRAEr1FxGwcftaTEQ3R%2BXtQCjHrLjKq9Zhf2gkkNZrhA9GCeuN5XjRuKJ9AzYJa7Mz5OBAL1oB8VS2odsJ%2BxQH9GcStqIXo0kZmT7rFT8OCUnb09aFmay4vagZeF76gCnv1OenLhgZ43%2FPKmhqgCJXRfzmPd97Co943ThjLZtH1kNPUEju4qKG5Pm2lcnPRvHpkIPjKmeUdPdVL&X-Amz-Signature=9be4b6f63ac2bbcc71fe3ec1c60e0fab5d4af013836d99772d8651b4b936e7ea&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
- Evaluate models using both visualization and numerical metrics.
- Consider context and domain for interpreting R² and MSE values.
___

## Notes
### Regression Plot
When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using **regression plots**.
This plot will show a combination of scattered data points (a **scatterplot**), as well as the fitted **linear regression** line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).
### Residual Plot
A good way to visualize the variance of the data is to use a residual plot.
What is a **residual**?
The difference between the observed value (y) and the predicted value (ŷ) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
So what is a **residual plot**?
A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
What do we pay attention to when looking at a residual plot?
We look at the spread of the residuals:
- If the points in a residual plot are **randomly spread out around the x-axis**, then a **linear model is appropriate** for the data.
Why is that? Randomly spread out residuals mean that the variance is constant, and thus the linear model is a good fit for this data.
### **Simple Linear Regression**
One example of a Data Model that we will be using is **Simple Linear Regression**.
Simple Linear Regression is a method to help us understand the relationship between two variables:
- The predictor/independent variable (X)
- The response/dependent variable (that we want to predict) (Y)
The result of Linear Regression is a **linear function** that predicts the response (dependent) variable as a function of the predictor (independent) variable.
### **Multiple Linear Regression**
What if we want to predict car price using more than one variable?
If we want to use more variables in our model to predict car price, we can use **Multiple Linear Regression**. Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain the relationship between one continuous response (dependent) variable and **two or more** predictor (independent) variables. Most of the real-world regression models involve multiple predictors. We will illustrate the structure by using four predictor variables, but these results can generalize to any number.
### **Polynomial Regression**
**Polynomial regression** is a particular case of the general linear regression model or multiple linear regression models.
We get non-linear relationships by squaring or setting higher-order terms of the predictor variables.
### Measures for In-Sample Evaluation
When evaluating our models, not only do we want to visualize the results, but we also need a quantitative measure to determine how accurate the model is.
Two very important measures that are often used in statistics to assess the accuracy of a model are:
- **R² / R-squared (The Coefficient of Determination)**
- **Mean Squared Error (MSE)**
#### R-squared
R-squared, also known as the coefficient of determination, measures how closely the data aligns with the fitted regression line.
The R-squared value represents the percentage of variation in the response variable (y) that is explained by the linear model.
#### Mean Squared Error (MSE)
The Mean Squared Error (MSE) measures the average of the squares of the errors. In other words, it calculates the difference between the actual values (y) and the estimated values (ŷ).
___
## **Cheat Sheet: Model Development**
### Linear Regression
- **Process**: Create a Linear Regression model object
- **Description**: Create an instance of the `LinearRegression` model.
- **Code Example**:
```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
```
### Train Linear Regression Model
- **Process**: Train the Linear Regression model
- **Description**: Fit the model on the input and output data. If there’s only one input attribute, it’s simple linear regression. If there are multiple attributes, it’s multiple linear regression.
- **Code Example**:
```python
X = df[['attribute_1', 'attribute_2', ...]]
Y = df['target_attribute']

lr.fit(X, Y)
```
### Generate Output Predictions
- **Process**: Predict the output for given input attributes
- **Description**: Use the trained model to predict the output values based on the input attributes.
- **Code Example**:
```python
Y_hat = lr.predict(X)
```
### Identify the Coefficient and Intercept
- **Process**: Retrieve the model’s coefficient and intercept
- **Description**: Access the slope coefficient and intercept values of the linear regression model.
- **Code Example**:
```python
coeff = lr.coef_
intercept = lr.intercept_
```
### Residual Plot
- **Process**: Create a Residual Plot
- **Description**: Plot the residuals (the differences between observed and predicted values) to assess the goodness of fit.
- **Code Example**:
```python
import seaborn as sns

sns.residplot(x=df['attribute_1'], y=df['attribute_2'])
```
### Distribution Plot
- **Process**: Create a Distribution Plot
- **Description**: Plot the distribution of a given attribute’s data.
- **Code Example**:
```python
import seaborn as sns

sns.distplot(df['attribute_name'], hist=False)
```
### Polynomial Regression
- **Process**: Perform Polynomial Regression
- **Description**: Fit a polynomial model to the data using NumPy.
- **Code Example**:
```python
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
Y_hat = p(x)
```
### Multi-variate Polynomial Regression
- **Process**: Create Polynomial Features
- **Description**: Generate polynomial combinations of features up to a specified degree.
- **Code Example**:
```python
from sklearn.preprocessing import PolynomialFeatures

Z = df[['attribute_1', 'attribute_2', ...]]
pr = PolynomialFeatures(degree=n)
Z_pr = pr.fit_transform(Z)
```
### Pipeline
- **Process**: Create a Data Pipeline
- **Description**: Simplify the steps of processing data by creating a pipeline with a sequence of steps.
- **Code Example**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]
pipe = Pipeline(Input)
Z = Z.astype(float)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
```
### R² Value
- **Process**: Calculate R² Value
- **Description**: Measure how well the model’s predictions fit the data. This is the proportion of variance explained by the model.
- **Code Example**:
	- For Linear Regression:
```python
from sklearn.metrics import r2_score

R2_score = lr.score(X, Y)
```
	- For Polynomial Regression:
```python
from sklearn.metrics import r2_score
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
R2_score = r2_score(y, p(x))
```
### Mean Squared Error (MSE) Value
- **Process**: Calculate Mean Squared Error (MSE)
- **Description**: Measure the average of the squares of the errors, which are the differences between actual values and the estimated values.
- **Code Example**:
```python
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(Y, Y_hat)
```
___

