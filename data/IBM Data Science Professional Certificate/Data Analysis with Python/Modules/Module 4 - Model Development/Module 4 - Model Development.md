

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=d0a5ac47036c45d8d58ec12f2cde63ad85bac45037c635737476529008ca8032&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=69061e9c6d8b5733b271862533c672cdd7b7a3eb00f786ec9ef30d7bde49ef48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=77ca95440f6d978ba39f343b4d64af56c38c6ea78b477d35c7cc02269b359f3b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=991deecae5d82c1b260f7694eb4def8a0e86b179ade220deacc77da9ef00c150&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=2249478a5882c686f473c9f64742169d5b89b1eaaffad9aea0689f1b56522937&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=bd1e56a01dcec2749ad674530af72a2bc30d3bd534d44243a25062ce9fbd18c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=d49e6f970f8642210b1e3e4e04187f5e5b0f03688634e21791a72600394784b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=6f5cc11517fb1c6ec5a1170ab34dee9021effcd972067f07e0ee4592822ef57c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=842fd051d3816c8044830b0b33614a25f5dd908c3f34bac1123cb52a0e436245&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=40f389724f9dd84ede47f74b857e46d475f98ec1a25d05dfe9cf37d01f86be50&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXYDR23%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDGsNQU%2F%2B40LWPCLS6KIMVLOV%2FKiSFDup7Oagq8kTKI1AiEAxn4s4Jt26QvpuYEMocpItxZ3k2iXtn1%2Fr2j2sWGvR3Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOehFSHieu%2BZzEl0FyrcA8LQkUTRAtSLqm8wAVsFEESc4Eq86KRO5QeMPDgiC261n0TtVpGyDX5DMrwb5IAJqc0opgjOtjn6xZMQD4crCXa8mrRgavnslCq%2BFsXbmT%2FgtWpVDooY3YVXorVZ9NEHVFcgxr8XwnorKXqzyLQ%2Fsve1g9Mwi4kWXZ9aAFWRozkVKwf3wtndz5sEuHPFjC0Rywm8Eh2lKuMgfwpus%2FxXZnrLbYgbcSiz02ghUplLQXQYyPT9mb2iduwGNRieTp7CnSQU14HSImf%2B6vCjwOvVBganBiQNA7BZEJfl7LMuwsTcZSn0ENi0Vg7lVul4dCRdUVdjM4oHLxYxZ1fSs5rZ%2F0TmR%2FXoNpSt8Nr%2BkXZ%2FdPCfYLQZlk4HnPPKhR6pF2AOXOUrXdG8ZbeiEqEgoI6egCf%2Bbcm10qLvMUPmmwxfQK55KVsLqeII%2BRKW74etngweBvoHcbot00Fzl1Xhnfhz%2FMMKaX04u5nL%2BepEaJUdPfiuhWWI2nTeuO%2FHHFEdjc%2F8lojVnRouTGZlqtHZl7Rgw0CWjfXTZzMAuCfbv2cKg2tSIyZfOlQ9cdSsLkxjnT1YX31Rh0fVrQh1nxgPogypmZIfAAOWoANQsvwEtIVuwRc4edu2%2F6G1Fx%2FGrPFOMP6%2Bhr0GOqUBgECsvQe0yPVPcoOcu3TP1R2wBD%2F0kdDwNiII1Zrbty4p9uRCNrngumqa8lpm%2FpUhWbZqWQy2Uld0PS8Z6aNSZJODJq20qqJb3qvYXUmXMHQKz0afTTkiBDvWnVs%2BM38zEWVuoZtmMUWNKYcruOiVgIaWH7hwyj2xlgNS%2B%2FKxnJF%2FopnVdXcY2d3v9SuF2RyblVbq6fH%2F%2FF817e7xU%2BPI7Pgk0QPh&X-Amz-Signature=424bf650b77835690efc0836a48738045e1a73d7215f26c7576e7d549f1bd4f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6Z3ABUW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCZnN2OLycXOW4Ewfi%2BuS3F2stEEDNVxlVTu1zQG9c7bQIhAJ8z2jUgG7bzhZVg0qkSZs0Qs5vSMzulQqRbWhF1wXMqKv8DCCYQABoMNjM3NDIzMTgzODA1Igxp45UjbtHw1Ywn8wQq3AM%2FmFHSe%2FIvF%2Brj7wnhf1MFNiL27%2F0m6S2k%2F2huE2ml%2FtkqANPtH61r5bTkaCJLQm8YQAFZf0tR2SBDPf0AxjUd88IaWWufcxE3Dk5FnNRebjz5EaW4EE8tW5S%2FkgjdeyXo1GrNGqgKiKkfjS8Y5VSYU%2BepTNACj0fArPhJ8aw65XMF3CPWQL5SyGu2NjBq0HXEB2NjDfLy%2FWK6kNcDJ00sF4l8qBQnx7w4e1HZBwc5oaaVHW6%2F4M3d1FHI4vrY0BGx9vqTdiqioGZed%2FpCV5nrUJBz1t3T1RMMg%2FfKn21WZ5WjScjTA5QwUKMznDTsw1pKdTLeiJiknpyg%2Bexvxe%2BF%2Bp8A1A8F%2FhEEZxfa8JMaMyxSWEdDO0Uaingk0maptbNMPrkaR4wgnxiz0VJA1X0qKmaGIuiWFjv09xzUOBxv79hzEQlgqqB7jr6V8BDFPlsERPIoN%2FOGjYpA4sAdDUs5ZVIVLuL9WvRM8nOppzPjJwMh9nqaLwSIYzvuFx5iQQWLneXjQSD1Zd%2FN%2FoUQ%2B0h6k5szjjZJpYJNRuqYWtp0QZnICbiKN%2BNLHiu%2BSuaXu9dxmpb8YWdr5WnIeQkWOD8o%2BwSLACGo9onUBXRq56xGtbi9OqtoslrRmX1PhDCKv4a9BjqkAbbXP6G1QI4Mht92LGKNAXwblqpQcHUUkm2Xv6y4kpeuKLEYi1fu%2BTCs4P4oQWrku2h0xXypKtbX%2FElDN2ezhHiQsdUDiv%2FK3LdIwESaYuH5iwszI7wm52vbR3BoFC%2FJoJlu42cdHUcTmzzxqOiZ7SvznlXcw7Me0ecemCooGPUsVBlW51se8sY004h3adyydcj9HpX02Ris%2BSUR6cu4GszGuym%2F&X-Amz-Signature=7523b1984ed03eb831119b8c757e6b769202ca92ed0b176436fd8ea97df6421c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6Z3ABUW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCZnN2OLycXOW4Ewfi%2BuS3F2stEEDNVxlVTu1zQG9c7bQIhAJ8z2jUgG7bzhZVg0qkSZs0Qs5vSMzulQqRbWhF1wXMqKv8DCCYQABoMNjM3NDIzMTgzODA1Igxp45UjbtHw1Ywn8wQq3AM%2FmFHSe%2FIvF%2Brj7wnhf1MFNiL27%2F0m6S2k%2F2huE2ml%2FtkqANPtH61r5bTkaCJLQm8YQAFZf0tR2SBDPf0AxjUd88IaWWufcxE3Dk5FnNRebjz5EaW4EE8tW5S%2FkgjdeyXo1GrNGqgKiKkfjS8Y5VSYU%2BepTNACj0fArPhJ8aw65XMF3CPWQL5SyGu2NjBq0HXEB2NjDfLy%2FWK6kNcDJ00sF4l8qBQnx7w4e1HZBwc5oaaVHW6%2F4M3d1FHI4vrY0BGx9vqTdiqioGZed%2FpCV5nrUJBz1t3T1RMMg%2FfKn21WZ5WjScjTA5QwUKMznDTsw1pKdTLeiJiknpyg%2Bexvxe%2BF%2Bp8A1A8F%2FhEEZxfa8JMaMyxSWEdDO0Uaingk0maptbNMPrkaR4wgnxiz0VJA1X0qKmaGIuiWFjv09xzUOBxv79hzEQlgqqB7jr6V8BDFPlsERPIoN%2FOGjYpA4sAdDUs5ZVIVLuL9WvRM8nOppzPjJwMh9nqaLwSIYzvuFx5iQQWLneXjQSD1Zd%2FN%2FoUQ%2B0h6k5szjjZJpYJNRuqYWtp0QZnICbiKN%2BNLHiu%2BSuaXu9dxmpb8YWdr5WnIeQkWOD8o%2BwSLACGo9onUBXRq56xGtbi9OqtoslrRmX1PhDCKv4a9BjqkAbbXP6G1QI4Mht92LGKNAXwblqpQcHUUkm2Xv6y4kpeuKLEYi1fu%2BTCs4P4oQWrku2h0xXypKtbX%2FElDN2ezhHiQsdUDiv%2FK3LdIwESaYuH5iwszI7wm52vbR3BoFC%2FJoJlu42cdHUcTmzzxqOiZ7SvznlXcw7Me0ecemCooGPUsVBlW51se8sY004h3adyydcj9HpX02Ris%2BSUR6cu4GszGuym%2F&X-Amz-Signature=aaa562c11c1575463864ed4cd6b7e72978f2feba7faa037cf19447991a47f9ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6Z3ABUW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCZnN2OLycXOW4Ewfi%2BuS3F2stEEDNVxlVTu1zQG9c7bQIhAJ8z2jUgG7bzhZVg0qkSZs0Qs5vSMzulQqRbWhF1wXMqKv8DCCYQABoMNjM3NDIzMTgzODA1Igxp45UjbtHw1Ywn8wQq3AM%2FmFHSe%2FIvF%2Brj7wnhf1MFNiL27%2F0m6S2k%2F2huE2ml%2FtkqANPtH61r5bTkaCJLQm8YQAFZf0tR2SBDPf0AxjUd88IaWWufcxE3Dk5FnNRebjz5EaW4EE8tW5S%2FkgjdeyXo1GrNGqgKiKkfjS8Y5VSYU%2BepTNACj0fArPhJ8aw65XMF3CPWQL5SyGu2NjBq0HXEB2NjDfLy%2FWK6kNcDJ00sF4l8qBQnx7w4e1HZBwc5oaaVHW6%2F4M3d1FHI4vrY0BGx9vqTdiqioGZed%2FpCV5nrUJBz1t3T1RMMg%2FfKn21WZ5WjScjTA5QwUKMznDTsw1pKdTLeiJiknpyg%2Bexvxe%2BF%2Bp8A1A8F%2FhEEZxfa8JMaMyxSWEdDO0Uaingk0maptbNMPrkaR4wgnxiz0VJA1X0qKmaGIuiWFjv09xzUOBxv79hzEQlgqqB7jr6V8BDFPlsERPIoN%2FOGjYpA4sAdDUs5ZVIVLuL9WvRM8nOppzPjJwMh9nqaLwSIYzvuFx5iQQWLneXjQSD1Zd%2FN%2FoUQ%2B0h6k5szjjZJpYJNRuqYWtp0QZnICbiKN%2BNLHiu%2BSuaXu9dxmpb8YWdr5WnIeQkWOD8o%2BwSLACGo9onUBXRq56xGtbi9OqtoslrRmX1PhDCKv4a9BjqkAbbXP6G1QI4Mht92LGKNAXwblqpQcHUUkm2Xv6y4kpeuKLEYi1fu%2BTCs4P4oQWrku2h0xXypKtbX%2FElDN2ezhHiQsdUDiv%2FK3LdIwESaYuH5iwszI7wm52vbR3BoFC%2FJoJlu42cdHUcTmzzxqOiZ7SvznlXcw7Me0ecemCooGPUsVBlW51se8sY004h3adyydcj9HpX02Ris%2BSUR6cu4GszGuym%2F&X-Amz-Signature=7caa914096f64dd19b0dc038aa186a8cb09da3db9f73e894746457fe590a0c55&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6Z3ABUW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCZnN2OLycXOW4Ewfi%2BuS3F2stEEDNVxlVTu1zQG9c7bQIhAJ8z2jUgG7bzhZVg0qkSZs0Qs5vSMzulQqRbWhF1wXMqKv8DCCYQABoMNjM3NDIzMTgzODA1Igxp45UjbtHw1Ywn8wQq3AM%2FmFHSe%2FIvF%2Brj7wnhf1MFNiL27%2F0m6S2k%2F2huE2ml%2FtkqANPtH61r5bTkaCJLQm8YQAFZf0tR2SBDPf0AxjUd88IaWWufcxE3Dk5FnNRebjz5EaW4EE8tW5S%2FkgjdeyXo1GrNGqgKiKkfjS8Y5VSYU%2BepTNACj0fArPhJ8aw65XMF3CPWQL5SyGu2NjBq0HXEB2NjDfLy%2FWK6kNcDJ00sF4l8qBQnx7w4e1HZBwc5oaaVHW6%2F4M3d1FHI4vrY0BGx9vqTdiqioGZed%2FpCV5nrUJBz1t3T1RMMg%2FfKn21WZ5WjScjTA5QwUKMznDTsw1pKdTLeiJiknpyg%2Bexvxe%2BF%2Bp8A1A8F%2FhEEZxfa8JMaMyxSWEdDO0Uaingk0maptbNMPrkaR4wgnxiz0VJA1X0qKmaGIuiWFjv09xzUOBxv79hzEQlgqqB7jr6V8BDFPlsERPIoN%2FOGjYpA4sAdDUs5ZVIVLuL9WvRM8nOppzPjJwMh9nqaLwSIYzvuFx5iQQWLneXjQSD1Zd%2FN%2FoUQ%2B0h6k5szjjZJpYJNRuqYWtp0QZnICbiKN%2BNLHiu%2BSuaXu9dxmpb8YWdr5WnIeQkWOD8o%2BwSLACGo9onUBXRq56xGtbi9OqtoslrRmX1PhDCKv4a9BjqkAbbXP6G1QI4Mht92LGKNAXwblqpQcHUUkm2Xv6y4kpeuKLEYi1fu%2BTCs4P4oQWrku2h0xXypKtbX%2FElDN2ezhHiQsdUDiv%2FK3LdIwESaYuH5iwszI7wm52vbR3BoFC%2FJoJlu42cdHUcTmzzxqOiZ7SvznlXcw7Me0ecemCooGPUsVBlW51se8sY004h3adyydcj9HpX02Ris%2BSUR6cu4GszGuym%2F&X-Amz-Signature=ae112998a115933cb5f701a5bdcc43389d9caf6600073eef590edf45e8345bda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOZWCPA2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDk%2FNjje4r%2B6mqGyb9OnWW1yDKEuyqwtifdWsBJjlwlcAIgJTvgM2UxGxOQKzXg5eWLkb82%2F0TxYUqSQzbGAEk%2BJLkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGIKK6F8CRMZvKKi%2FyrcA52xXUEKGklOIt6vLezp9q1OrGXY05FCDhzOtFL%2BVOokSlag2TsXw31A85Fs2pHk1X%2B5a7sDcDXopiuXr%2BohZRQhQ3wwbgu6ksemhQBL6uKnwk0byp9srGAf7p8Q0Tl%2BY%2FvFLFSgB1%2BwgiPAyj9oetzieGsI9Y5LgKyYH2G8Kv7e4E2p2npZ9xqSAa1Jtfg3%2F80FIjUEZko8peq9Vel3TldwvofGK3xuv2%2F9%2Fz%2BzzzKDRFrw%2FPl67hz%2FuMGw3EXTWDyk496g6OGcg%2BmMlzwy6PLxGnfG07SmJE3HT%2FTIt21IIFBKB%2FOOYBaLVBryiZBZ79wkdQXjWt2mnOknRQ%2B45N52J6IS1pkbX%2FWKuGFBBFJ2snv%2BgYsCVD3MOSMbyLRphM1Jax37oBbY0nsWldtZ0ejLgGJWFc5lYhVbhQBP6w1oJWIhyKKFgZ4Ir2cLqobSE8%2BLrAcCIHaA1d4vyljZj1RRUcQYfYHrfFiYTqg1CgJvWzHDyKi7SOubhmDTwKIjU081%2FZCcpuVebUN2XPJ25WTelR9B0EYpnT%2FW80BiNKxshLWzgZQ2EAUjStotaFZOZtdIs23zb2HzGjDCs3imr%2FSlP1ix7Kd3Bja1QYqrRWu8CP%2BIi9wOXoB2%2ForrMOS%2Bhr0GOqUBC%2B5OFGo1j9UFbaYwb0DBLhmtqEM0%2BZOUEfv9j5TsAGvtbgeM634sSiJzgFHaiB5aKAa8asEQL85u9aUysAuuhoNkotIOUWTDmRs5NCNQsmzMP%2BEOhxish2R%2Bo3rNpiucgjclwK3hh%2FgezjSvyIy9cLkx%2BRhXbskFRf%2FDoTMfgZI94v9DChTOdoarLpkRnPMcgBR9EDRTC8BtLUjU%2BYCEbOqsxv1n&X-Amz-Signature=282e9589d4aee699f7ef0ba0eb110c10f282d88cac5b4d0b7869f49ce3905885&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOZWCPA2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDk%2FNjje4r%2B6mqGyb9OnWW1yDKEuyqwtifdWsBJjlwlcAIgJTvgM2UxGxOQKzXg5eWLkb82%2F0TxYUqSQzbGAEk%2BJLkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGIKK6F8CRMZvKKi%2FyrcA52xXUEKGklOIt6vLezp9q1OrGXY05FCDhzOtFL%2BVOokSlag2TsXw31A85Fs2pHk1X%2B5a7sDcDXopiuXr%2BohZRQhQ3wwbgu6ksemhQBL6uKnwk0byp9srGAf7p8Q0Tl%2BY%2FvFLFSgB1%2BwgiPAyj9oetzieGsI9Y5LgKyYH2G8Kv7e4E2p2npZ9xqSAa1Jtfg3%2F80FIjUEZko8peq9Vel3TldwvofGK3xuv2%2F9%2Fz%2BzzzKDRFrw%2FPl67hz%2FuMGw3EXTWDyk496g6OGcg%2BmMlzwy6PLxGnfG07SmJE3HT%2FTIt21IIFBKB%2FOOYBaLVBryiZBZ79wkdQXjWt2mnOknRQ%2B45N52J6IS1pkbX%2FWKuGFBBFJ2snv%2BgYsCVD3MOSMbyLRphM1Jax37oBbY0nsWldtZ0ejLgGJWFc5lYhVbhQBP6w1oJWIhyKKFgZ4Ir2cLqobSE8%2BLrAcCIHaA1d4vyljZj1RRUcQYfYHrfFiYTqg1CgJvWzHDyKi7SOubhmDTwKIjU081%2FZCcpuVebUN2XPJ25WTelR9B0EYpnT%2FW80BiNKxshLWzgZQ2EAUjStotaFZOZtdIs23zb2HzGjDCs3imr%2FSlP1ix7Kd3Bja1QYqrRWu8CP%2BIi9wOXoB2%2ForrMOS%2Bhr0GOqUBC%2B5OFGo1j9UFbaYwb0DBLhmtqEM0%2BZOUEfv9j5TsAGvtbgeM634sSiJzgFHaiB5aKAa8asEQL85u9aUysAuuhoNkotIOUWTDmRs5NCNQsmzMP%2BEOhxish2R%2Bo3rNpiucgjclwK3hh%2FgezjSvyIy9cLkx%2BRhXbskFRf%2FDoTMfgZI94v9DChTOdoarLpkRnPMcgBR9EDRTC8BtLUjU%2BYCEbOqsxv1n&X-Amz-Signature=ceb293143ed4a121da6076b7f0245e687695b10041347355c16493360974a416&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOZWCPA2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDk%2FNjje4r%2B6mqGyb9OnWW1yDKEuyqwtifdWsBJjlwlcAIgJTvgM2UxGxOQKzXg5eWLkb82%2F0TxYUqSQzbGAEk%2BJLkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGIKK6F8CRMZvKKi%2FyrcA52xXUEKGklOIt6vLezp9q1OrGXY05FCDhzOtFL%2BVOokSlag2TsXw31A85Fs2pHk1X%2B5a7sDcDXopiuXr%2BohZRQhQ3wwbgu6ksemhQBL6uKnwk0byp9srGAf7p8Q0Tl%2BY%2FvFLFSgB1%2BwgiPAyj9oetzieGsI9Y5LgKyYH2G8Kv7e4E2p2npZ9xqSAa1Jtfg3%2F80FIjUEZko8peq9Vel3TldwvofGK3xuv2%2F9%2Fz%2BzzzKDRFrw%2FPl67hz%2FuMGw3EXTWDyk496g6OGcg%2BmMlzwy6PLxGnfG07SmJE3HT%2FTIt21IIFBKB%2FOOYBaLVBryiZBZ79wkdQXjWt2mnOknRQ%2B45N52J6IS1pkbX%2FWKuGFBBFJ2snv%2BgYsCVD3MOSMbyLRphM1Jax37oBbY0nsWldtZ0ejLgGJWFc5lYhVbhQBP6w1oJWIhyKKFgZ4Ir2cLqobSE8%2BLrAcCIHaA1d4vyljZj1RRUcQYfYHrfFiYTqg1CgJvWzHDyKi7SOubhmDTwKIjU081%2FZCcpuVebUN2XPJ25WTelR9B0EYpnT%2FW80BiNKxshLWzgZQ2EAUjStotaFZOZtdIs23zb2HzGjDCs3imr%2FSlP1ix7Kd3Bja1QYqrRWu8CP%2BIi9wOXoB2%2ForrMOS%2Bhr0GOqUBC%2B5OFGo1j9UFbaYwb0DBLhmtqEM0%2BZOUEfv9j5TsAGvtbgeM634sSiJzgFHaiB5aKAa8asEQL85u9aUysAuuhoNkotIOUWTDmRs5NCNQsmzMP%2BEOhxish2R%2Bo3rNpiucgjclwK3hh%2FgezjSvyIy9cLkx%2BRhXbskFRf%2FDoTMfgZI94v9DChTOdoarLpkRnPMcgBR9EDRTC8BtLUjU%2BYCEbOqsxv1n&X-Amz-Signature=8c0c3cfbf33b12d73b9d1dec0558a44074d5f44d38059b148ee60be0711353e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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

