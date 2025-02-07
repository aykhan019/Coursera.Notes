

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=bbf1944d8bcaa7d91e06236ddb0afe62a33849a868f48c2cb4fca5641cee047c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=3cc2ccf1ceb8adee79caea84f6b3d49857542850508f11cc5ec573ed19f33c63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=db93b92ba2e3f647d38b629537322f1928625ce284139dba6f1bb80a568cf0e6&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=f50ba988f8d76af0506eee67234f690db93d769bf81c3b934e788fbc7691681d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=c30f6386fe240298cc69eac9c8c294325be58e3eee111690dd15c3f8b406a910&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=39bcb2bd713eb06089e8c90658a4660d96f64dc79f5f704b93fa125798f6209b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=52604561597f88e06041a6bc6eed03a5b10ed507f0ca2041be13cb63c9dc277e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=266cd8b0fce131fb92cd507caac23872779f7ea67ef9f28c6cd16ccb4fe5e7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=3b54ac9b6e2f86736267f2477c9ce12d1c0f32378faf793cf65341ba40c17b8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=ac1133d791254ebcc8a9ac6b1ddb4fec0fdb153f4f03f313252b13cf4cd601b2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS53GOR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF1GZTTbSRa%2FOtF7n8fF0OKHlkCpyEUJ5fG4wooob1mRAiB6Ojpnw%2Bki7W11bwWwv0jkNJe%2By0MZigibJZeHttOcuSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMqnwTrjZgu1U5UCcuKtwDb3%2BgQAeIbvpuQ5D1MVXrhtPFZkCwyB2UXR31%2BHo9a6aNH9XLm1azsmAXCCccUJOGHmwNgE9v5L1a3Qu6Ksi4tVeDDhy5rZ9k1%2FPYxa9WxNtCFvt9w0iMtZdkLOg7rbQpcUSmqt7e7FwmOGKc1fCwUkarIiuNqR%2Be1IEKCXxDAzofF1Do%2FS6eGnMAu1nijJ9OejG9Dp%2BLPISZem1I521d%2BKKoDxb%2Bx5QOovaq1sV1TsmL99XybMv5YYqIzlvXA3Tch0ZmsVSUnNDJbzsygPFV%2FCuwmx%2FpLxegl%2FpPtkQbJRJAiI%2B5w9MhZ5xhboxOjzbjVPEdXIWxJXkE33ypRCZwl76ZeOBz5kZxLACZGvktRFhekjLNunoqUFjKZ0oCCTUaLM7VyaitXFh9f1XlJZ%2BSbJJzgA1pblXQ6fHOTUKomq82nECS2sO%2B9rKKbKPyS7yhwOwhmvTntRXgjzostQKPYduHavOgeF5bSGMfnAVQB29mp6dva8%2B1EryU6gOZLf5rR2PvxOEz877d0eFZVIHXOpkIfPOvTBz5talFKdVPeGXM6kzL4a6SkS7A%2FsiTnB7SgKykHcZxFnTldDw3Tzy4AE0mpzJTYw0tYbzP3sjp%2FREsKU2dfEuTNG%2Fok6ow0fuYvQY6pgHE8FEHUN30PNwirrWTh300UwFmHqzqpoZWAtPL3P6CZx%2FbtfPhSkLeYsfyOqAHar0KZTmPnUkFIb33G9ErH9WT4qYFhm7p12DIMmChkoSteLYCzQ3qF2FboSgDVLMRlxfxvn2zdRzUf7q7n0UiVtGA80IL24wE4ECYtBbRPap%2F35kCIckQa6EAm17Ic%2Bx9v6%2BstjFIBsgnp7q634O5iIj1P7kL5o4d&X-Amz-Signature=fd6a03bf86e549cf1b9eb892c0e9c3a37156f77f46fbde45e8a74935bf49d924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC357APT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC6P5lvtfD4UqaLGHnR8%2F%2FoKi3XvLNAVlQy2y3P7pbYsQIgZtbCT3ejpquW4LnS6oM2WCFxAmLwliBUS%2BPhtb2kVzgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDG8WlBx%2BKXwAez%2B6QyrcA5kkcOzav7Ei2mUHP3%2FT4Y%2F8IMWJZcleRVE2X%2BkjqvEbYUy2bsQ4Ymck2%2Bu6PXWiscCMq3sy3vQeuuqMGDvxWEQMIomA1kCXW2tv7MeqdSRUnod4nze35uIlfdFK2b0EVj5sZEN7anWAotjsaP6LubmifTHWj0K%2Fpn%2BgtKsYJvuFyoPVrI7XCtqT06mPowD8hvokQmpTI5iaZVerqUsWhmVekB1CXYJ497lM9K5jqRSYjRBasjHpmHaLBRszqFLDZkyjG6UzOcjBNWM9Swkof8u18%2Fmr7Rxo0Lr%2F5vs1ZP%2BASAPCXhM8Jzl54LH5%2BVQckqi0yo9T3%2BUSlmnmr5q0v24QFHfxsSaTueQsS2OHhl7DyzfK7Hxo1LV9bErh8YkewdKjUcomyfUVAZW%2FzX7FNo6uDShZy6IHKajeuhfzQdyHKRmNXyY2zcp6ew%2Fya23cpn5op%2BSD3SgrJBO%2BpMouw2swV9qfiNTiGMTsqgIV8thFEHxpilEJSfkQ2JM%2F0ly%2BVaqLZD91m79SSRRfXRCvAwqXYQH3SW7sgP22bHhTErj2QSQThOIYvoTyhAivHn5T9Elxxlkl9oMmwV5F0qZRhHIa5IVq5jRIdEgdt54szIwiOQTaO%2F%2BMtQYSHVnGMIT8mL0GOqUBX%2BZ0dUZrhSmKrpdm%2BoZeLsEdYJPcNA%2BgTqJaomQJXHW1JdAkAwT20%2BjRT%2FxBH54IIOf7VgO4hhxc9U5r85C9rqGxUxoD%2Bn7y1PsLEDaQeeCx5RcCWF92p60Ba1FDuE17dZApSX%2FnqSrF6KVl0pjAoyqaTn4O%2BGkOdKv9wLWoHm4qGa8wyrwAMC8lnzcGsaqROZ1Hdsgxz2DE2XeUELty2I4jb7gW&X-Amz-Signature=639f10a9ce80a274f2aa8e1ffbf74566ee3f1f2cd67be54841e163916bb4e426&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC357APT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC6P5lvtfD4UqaLGHnR8%2F%2FoKi3XvLNAVlQy2y3P7pbYsQIgZtbCT3ejpquW4LnS6oM2WCFxAmLwliBUS%2BPhtb2kVzgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDG8WlBx%2BKXwAez%2B6QyrcA5kkcOzav7Ei2mUHP3%2FT4Y%2F8IMWJZcleRVE2X%2BkjqvEbYUy2bsQ4Ymck2%2Bu6PXWiscCMq3sy3vQeuuqMGDvxWEQMIomA1kCXW2tv7MeqdSRUnod4nze35uIlfdFK2b0EVj5sZEN7anWAotjsaP6LubmifTHWj0K%2Fpn%2BgtKsYJvuFyoPVrI7XCtqT06mPowD8hvokQmpTI5iaZVerqUsWhmVekB1CXYJ497lM9K5jqRSYjRBasjHpmHaLBRszqFLDZkyjG6UzOcjBNWM9Swkof8u18%2Fmr7Rxo0Lr%2F5vs1ZP%2BASAPCXhM8Jzl54LH5%2BVQckqi0yo9T3%2BUSlmnmr5q0v24QFHfxsSaTueQsS2OHhl7DyzfK7Hxo1LV9bErh8YkewdKjUcomyfUVAZW%2FzX7FNo6uDShZy6IHKajeuhfzQdyHKRmNXyY2zcp6ew%2Fya23cpn5op%2BSD3SgrJBO%2BpMouw2swV9qfiNTiGMTsqgIV8thFEHxpilEJSfkQ2JM%2F0ly%2BVaqLZD91m79SSRRfXRCvAwqXYQH3SW7sgP22bHhTErj2QSQThOIYvoTyhAivHn5T9Elxxlkl9oMmwV5F0qZRhHIa5IVq5jRIdEgdt54szIwiOQTaO%2F%2BMtQYSHVnGMIT8mL0GOqUBX%2BZ0dUZrhSmKrpdm%2BoZeLsEdYJPcNA%2BgTqJaomQJXHW1JdAkAwT20%2BjRT%2FxBH54IIOf7VgO4hhxc9U5r85C9rqGxUxoD%2Bn7y1PsLEDaQeeCx5RcCWF92p60Ba1FDuE17dZApSX%2FnqSrF6KVl0pjAoyqaTn4O%2BGkOdKv9wLWoHm4qGa8wyrwAMC8lnzcGsaqROZ1Hdsgxz2DE2XeUELty2I4jb7gW&X-Amz-Signature=bc1b419b37efa45b31dcf3dcfb36e639bbd8b6da4e26bbfa2dd0e94eb839297a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC357APT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC6P5lvtfD4UqaLGHnR8%2F%2FoKi3XvLNAVlQy2y3P7pbYsQIgZtbCT3ejpquW4LnS6oM2WCFxAmLwliBUS%2BPhtb2kVzgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDG8WlBx%2BKXwAez%2B6QyrcA5kkcOzav7Ei2mUHP3%2FT4Y%2F8IMWJZcleRVE2X%2BkjqvEbYUy2bsQ4Ymck2%2Bu6PXWiscCMq3sy3vQeuuqMGDvxWEQMIomA1kCXW2tv7MeqdSRUnod4nze35uIlfdFK2b0EVj5sZEN7anWAotjsaP6LubmifTHWj0K%2Fpn%2BgtKsYJvuFyoPVrI7XCtqT06mPowD8hvokQmpTI5iaZVerqUsWhmVekB1CXYJ497lM9K5jqRSYjRBasjHpmHaLBRszqFLDZkyjG6UzOcjBNWM9Swkof8u18%2Fmr7Rxo0Lr%2F5vs1ZP%2BASAPCXhM8Jzl54LH5%2BVQckqi0yo9T3%2BUSlmnmr5q0v24QFHfxsSaTueQsS2OHhl7DyzfK7Hxo1LV9bErh8YkewdKjUcomyfUVAZW%2FzX7FNo6uDShZy6IHKajeuhfzQdyHKRmNXyY2zcp6ew%2Fya23cpn5op%2BSD3SgrJBO%2BpMouw2swV9qfiNTiGMTsqgIV8thFEHxpilEJSfkQ2JM%2F0ly%2BVaqLZD91m79SSRRfXRCvAwqXYQH3SW7sgP22bHhTErj2QSQThOIYvoTyhAivHn5T9Elxxlkl9oMmwV5F0qZRhHIa5IVq5jRIdEgdt54szIwiOQTaO%2F%2BMtQYSHVnGMIT8mL0GOqUBX%2BZ0dUZrhSmKrpdm%2BoZeLsEdYJPcNA%2BgTqJaomQJXHW1JdAkAwT20%2BjRT%2FxBH54IIOf7VgO4hhxc9U5r85C9rqGxUxoD%2Bn7y1PsLEDaQeeCx5RcCWF92p60Ba1FDuE17dZApSX%2FnqSrF6KVl0pjAoyqaTn4O%2BGkOdKv9wLWoHm4qGa8wyrwAMC8lnzcGsaqROZ1Hdsgxz2DE2XeUELty2I4jb7gW&X-Amz-Signature=9deb1de330fe5d02a9f710de1d3b596305e4b8e4303144dbf89298e3bd3a2c34&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC357APT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC6P5lvtfD4UqaLGHnR8%2F%2FoKi3XvLNAVlQy2y3P7pbYsQIgZtbCT3ejpquW4LnS6oM2WCFxAmLwliBUS%2BPhtb2kVzgq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDG8WlBx%2BKXwAez%2B6QyrcA5kkcOzav7Ei2mUHP3%2FT4Y%2F8IMWJZcleRVE2X%2BkjqvEbYUy2bsQ4Ymck2%2Bu6PXWiscCMq3sy3vQeuuqMGDvxWEQMIomA1kCXW2tv7MeqdSRUnod4nze35uIlfdFK2b0EVj5sZEN7anWAotjsaP6LubmifTHWj0K%2Fpn%2BgtKsYJvuFyoPVrI7XCtqT06mPowD8hvokQmpTI5iaZVerqUsWhmVekB1CXYJ497lM9K5jqRSYjRBasjHpmHaLBRszqFLDZkyjG6UzOcjBNWM9Swkof8u18%2Fmr7Rxo0Lr%2F5vs1ZP%2BASAPCXhM8Jzl54LH5%2BVQckqi0yo9T3%2BUSlmnmr5q0v24QFHfxsSaTueQsS2OHhl7DyzfK7Hxo1LV9bErh8YkewdKjUcomyfUVAZW%2FzX7FNo6uDShZy6IHKajeuhfzQdyHKRmNXyY2zcp6ew%2Fya23cpn5op%2BSD3SgrJBO%2BpMouw2swV9qfiNTiGMTsqgIV8thFEHxpilEJSfkQ2JM%2F0ly%2BVaqLZD91m79SSRRfXRCvAwqXYQH3SW7sgP22bHhTErj2QSQThOIYvoTyhAivHn5T9Elxxlkl9oMmwV5F0qZRhHIa5IVq5jRIdEgdt54szIwiOQTaO%2F%2BMtQYSHVnGMIT8mL0GOqUBX%2BZ0dUZrhSmKrpdm%2BoZeLsEdYJPcNA%2BgTqJaomQJXHW1JdAkAwT20%2BjRT%2FxBH54IIOf7VgO4hhxc9U5r85C9rqGxUxoD%2Bn7y1PsLEDaQeeCx5RcCWF92p60Ba1FDuE17dZApSX%2FnqSrF6KVl0pjAoyqaTn4O%2BGkOdKv9wLWoHm4qGa8wyrwAMC8lnzcGsaqROZ1Hdsgxz2DE2XeUELty2I4jb7gW&X-Amz-Signature=487588b83f3de724e1dab4d5b9ce63361275bc8697fea741f85f59d547fde239&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCSQ43M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFxlBB4zxwdRMbOFN3uBKgMiBxXa7YwQL15IEhRwlFltAiEA7PvF%2Bei9cqTTfXy9GymRQT0vrvwHjs7vrlCVX9iksH4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLsnz%2BWmJ62fznZ8QyrcA%2Buag72MxA3l4hv15lOPkNRaPB9atwfXXft5uW9hxsPEubhmLAhB4MAEGzkMz%2B%2BDHu9Ryeh%2FB%2BCIbmw%2FbxCvVv7eQhwBoY6yY8eDhJwLEAwuwChtQz1W5Tg65Z01rLxu8yTUgL17UkrblPOYltZjClgnKvMQ5fQ6sLC%2Bwdg8olpWH%2Fn%2F7PzU0XZnlQozLh8w%2FTLDjC82LQzmrTig7TnBJV9lepSWtUHxAeJFvS5DXEpRGs%2Frzc5cygcw85C9%2BCvrh8OBRSedj9Bgok55pk33T8i0F7IBrJQWduGYMou1NEb%2F8fU200ZTcy%2BrCIgSFu5e5bjwdRS6V%2BlMSkAwFwzuHZtIqsVxV3%2BUKWi%2BFyhiDFuijApVcAfu%2BhsrIpLr9SiM2enWX3aK4Xh3IrO1A7pyHlY8zAtXdqNNGL%2BtZj8KVQgTZbHMYlVgVt5EIR%2Fyrf7HrCjumiqCTxWoSs%2FZC7DSZOAm5%2B2qIWj8K7gS76QUYBKQJO6%2BrAIniuUj5qLlvsza4TN3dZ1lPVICexTLLaSSQFSgjXvSwS14ilKs0u3ECFoOa01MW1N7JjzzJKOr9QBlTgb7vBv%2BYxVUqNBAw1t7xpVjNJWBvkDpAnr5cdOguWi2iyINLP%2BmCZ6ZjwXyMPL7mL0GOqUBQs1axPAzyC8xNBajvGM3P%2BxT4ZUgkgt4%2B7fCLzVpUmPL2oJfOYpgIM86zok8v1ckXc9Xx2byj9tp8C7MwWPzVPaWmalbOp7DmGiGs05PERvOmYZBE7EoDkpL3zq77MZmkBSkSYQLnH%2F11kdWMMX6yE%2BF4vCAt%2Fji0c2Eoa1wflOwalrQV7g9cEkNCLf4PodBsl%2BPzPbPJMp%2BUZYFyE1aHCXegOPI&X-Amz-Signature=0ba2476efdcf0e2f62c736fdfdcb097db68b5c54d6b06777eba4ddb7418ecaeb&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCSQ43M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFxlBB4zxwdRMbOFN3uBKgMiBxXa7YwQL15IEhRwlFltAiEA7PvF%2Bei9cqTTfXy9GymRQT0vrvwHjs7vrlCVX9iksH4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLsnz%2BWmJ62fznZ8QyrcA%2Buag72MxA3l4hv15lOPkNRaPB9atwfXXft5uW9hxsPEubhmLAhB4MAEGzkMz%2B%2BDHu9Ryeh%2FB%2BCIbmw%2FbxCvVv7eQhwBoY6yY8eDhJwLEAwuwChtQz1W5Tg65Z01rLxu8yTUgL17UkrblPOYltZjClgnKvMQ5fQ6sLC%2Bwdg8olpWH%2Fn%2F7PzU0XZnlQozLh8w%2FTLDjC82LQzmrTig7TnBJV9lepSWtUHxAeJFvS5DXEpRGs%2Frzc5cygcw85C9%2BCvrh8OBRSedj9Bgok55pk33T8i0F7IBrJQWduGYMou1NEb%2F8fU200ZTcy%2BrCIgSFu5e5bjwdRS6V%2BlMSkAwFwzuHZtIqsVxV3%2BUKWi%2BFyhiDFuijApVcAfu%2BhsrIpLr9SiM2enWX3aK4Xh3IrO1A7pyHlY8zAtXdqNNGL%2BtZj8KVQgTZbHMYlVgVt5EIR%2Fyrf7HrCjumiqCTxWoSs%2FZC7DSZOAm5%2B2qIWj8K7gS76QUYBKQJO6%2BrAIniuUj5qLlvsza4TN3dZ1lPVICexTLLaSSQFSgjXvSwS14ilKs0u3ECFoOa01MW1N7JjzzJKOr9QBlTgb7vBv%2BYxVUqNBAw1t7xpVjNJWBvkDpAnr5cdOguWi2iyINLP%2BmCZ6ZjwXyMPL7mL0GOqUBQs1axPAzyC8xNBajvGM3P%2BxT4ZUgkgt4%2B7fCLzVpUmPL2oJfOYpgIM86zok8v1ckXc9Xx2byj9tp8C7MwWPzVPaWmalbOp7DmGiGs05PERvOmYZBE7EoDkpL3zq77MZmkBSkSYQLnH%2F11kdWMMX6yE%2BF4vCAt%2Fji0c2Eoa1wflOwalrQV7g9cEkNCLf4PodBsl%2BPzPbPJMp%2BUZYFyE1aHCXegOPI&X-Amz-Signature=97d520b43d92e5293ad3faf0d1a6bf34f8ee9814c87ca130146962021c07f434&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCSQ43M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFxlBB4zxwdRMbOFN3uBKgMiBxXa7YwQL15IEhRwlFltAiEA7PvF%2Bei9cqTTfXy9GymRQT0vrvwHjs7vrlCVX9iksH4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLsnz%2BWmJ62fznZ8QyrcA%2Buag72MxA3l4hv15lOPkNRaPB9atwfXXft5uW9hxsPEubhmLAhB4MAEGzkMz%2B%2BDHu9Ryeh%2FB%2BCIbmw%2FbxCvVv7eQhwBoY6yY8eDhJwLEAwuwChtQz1W5Tg65Z01rLxu8yTUgL17UkrblPOYltZjClgnKvMQ5fQ6sLC%2Bwdg8olpWH%2Fn%2F7PzU0XZnlQozLh8w%2FTLDjC82LQzmrTig7TnBJV9lepSWtUHxAeJFvS5DXEpRGs%2Frzc5cygcw85C9%2BCvrh8OBRSedj9Bgok55pk33T8i0F7IBrJQWduGYMou1NEb%2F8fU200ZTcy%2BrCIgSFu5e5bjwdRS6V%2BlMSkAwFwzuHZtIqsVxV3%2BUKWi%2BFyhiDFuijApVcAfu%2BhsrIpLr9SiM2enWX3aK4Xh3IrO1A7pyHlY8zAtXdqNNGL%2BtZj8KVQgTZbHMYlVgVt5EIR%2Fyrf7HrCjumiqCTxWoSs%2FZC7DSZOAm5%2B2qIWj8K7gS76QUYBKQJO6%2BrAIniuUj5qLlvsza4TN3dZ1lPVICexTLLaSSQFSgjXvSwS14ilKs0u3ECFoOa01MW1N7JjzzJKOr9QBlTgb7vBv%2BYxVUqNBAw1t7xpVjNJWBvkDpAnr5cdOguWi2iyINLP%2BmCZ6ZjwXyMPL7mL0GOqUBQs1axPAzyC8xNBajvGM3P%2BxT4ZUgkgt4%2B7fCLzVpUmPL2oJfOYpgIM86zok8v1ckXc9Xx2byj9tp8C7MwWPzVPaWmalbOp7DmGiGs05PERvOmYZBE7EoDkpL3zq77MZmkBSkSYQLnH%2F11kdWMMX6yE%2BF4vCAt%2Fji0c2Eoa1wflOwalrQV7g9cEkNCLf4PodBsl%2BPzPbPJMp%2BUZYFyE1aHCXegOPI&X-Amz-Signature=9f54a15ad9973bf0764fc65a2b4be878ff74b934c571872b73282d7adf0de4ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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

