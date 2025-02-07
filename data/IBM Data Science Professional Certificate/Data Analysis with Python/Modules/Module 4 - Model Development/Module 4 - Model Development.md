

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=06046d65c5dc33e8d23f2d4fdb0468c58a90f8dc6d0e3f9deddedb4990198f1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=fc65c26fd7cc2056c27ef9e43d3fa4c1e14a10ce14daae0ad94164796fa15f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=b2c7d0491906bbc94b2ac602abe34984a4512bd816c7c557a71d2ae74c4d8e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=f5b8293d13e33b17f44c8ed3330302aae5893e3f62fbe14f0400794104e86246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=d5f6ab957ee7bb8896bf34772975a02a6b38e2adc390385bdc54309821b8557f&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=b9ad58986fbca8db53cfe8e433eb610161b7ef49479fa30a16dd04a2dea7f59c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=49f7cee2f40d91419a6c541c3d755df52967f9d0c1caa05281579587c6ff4c81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=ecc78b516bb9c8da57d10358cfa2281752d5efd68b7f1996625ab9b52ada0fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=3982eba465aebc9afee3f45689d2f8219432d9ef9327a2cd7d0ab8d17fcdef71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=74d83a37dd9338502a7b619c00598c9ef761bd9d07cbe23d5a85837b43ef5bac&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QXSWKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCH6tdz2xqZDqaLWTxnOQ6zu0MQtqJAxKqIMcrUkmvc5gIhAL2GG9hUmesmoYvD0QynIWuGJmOcVrap6%2BJuRD6ui447Kv8DCHEQABoMNjM3NDIzMTgzODA1IgzNA5dcEcMB%2B915qKIq3AOkK5RGKm4P41C9kFbKnm1swpqplx1PE%2F1Hec5eQm8uEqDT%2Bi%2BT%2FnjD%2BYROUMXx9LtT2Lr%2BhfXmcAHrI04G3vaYUmZA1RJ1Vb7v4e%2BSN8WurZzxtIoH9DarpL4PCJKIr83Ed1T1%2FevT3AM%2F47GGG9%2F9KfpXU0YpXnu%2FGiS%2B4kTJMQE%2BX0Y5zLzOTL1d9rJYhh5l%2FM4KfU88BFpd80GFnRyIJ7FcJtqHQKoNUstbFaNbX%2BRRSfDrRIeZpqzIBJWQomabWAN2gmUmGvvaDcpIMaT7dNLiGXGXPJaYiC8hg8%2B8J7qiF15rxHHQUL%2BjmBpad7%2B6EI%2F4AN5dFiTYsugUiMUoDrZLaMnZcI0oO71Mq0a6t%2F1HXhEpRLEzQGk3LbChPaNMhzKegQuDuXN%2BDwa7YsyPTWcLQTokUAP0zdQoK%2FfZsg8F2AaWNHl%2FQPx1YKwKzu43ee%2BBGxXYAuTMV%2F20L%2BogiOe4VhIWEqKydolyf11YvgNieZHRb1jkWkvyUQQuxYWgRXExO2Nw3G6rjL8lmG1y1wwYbkZvXxiTxaFPzj6yq2D7pgOb9EIc6%2Be4bCTGW2zETsNWshXuYBQjLt5ymCFR%2FKaQi9q3Fa0GNml5AXBnQ6WKixbmIksiKrRNvzCP%2Bpa9BjqkAR5C5EyfWq062OaUSVMHYNgyJNfOF7dN2TOurdQtG8sKlRr4KNkhWsU%2BrEDLgB5mNRo6b80LFGBpJD074nXKzmFrJAtWuEkARHIAxtjo8ViFt5oHnGvk4CZJbn%2FASUMtsQCybxP0c%2FtOD7VIcVSULn3BBffWFHssbTvmhgQwa4ARmRnfWonmTTLbEs6Ga9gYmFLFRW2TrtlXUtmKUDWk4O6zY%2B8I&X-Amz-Signature=ee79d32765ae04f72ae71583569453e5c170fa31e1f9f1c31ef071adcb4ed587&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJHGAWZC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXb7bWNUyPlGRZy8HfsK6vk6wOO0P34bHV3i9Fb%2BjSAAiBaKwPf1tLqf%2Fk7%2B4OaVMU%2B%2FidV6OPCMFwXhBifFo0%2BrCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMq%2FLskwvL1xErtzuyKtwDE2FW1EsYooneCHjc0CzaV0f6ViGZ9ihlRFAQEf4HzhEB5Y1%2BfSaURvNNd17BMlS7ntZaZE9u7RIKAGWGPFeg%2BwG%2Bc%2FfybO6lVRxnkBYcSp1deKhQx9NzDV8AVJGB8C8utyyESZpsn1boBJ68WE%2Bb7LHycHd2GXj6aIfXN%2BSC4Z358pCownKgD%2FP9182OpL4qkWb6M4Rhw7mPrz81jXfCweT6pCzu7JRWONKnBVT4fXw4%2F9zQrD2cwAylD%2BDaMDqbSi7U5Pu8CWsydMysSTtsmuUYA9VXZmgXLWpB2tl%2FqJzIANsWvE9Y2ZuxqG5JyTiEO9pREBNRqNpjG38ziqoRD0E6Fc2urOT%2BkgPMEsCEXPBZjVuP04j0PRxDZFKaWf6kh%2BSuAAeCZ1lK7n0gok6hjhBTsNqYSNQtHWMRdQ1kkiqOlEHlPn547qDbavLaNXoiZvpJwoU2vIXP81GQOpF%2FhK841pk2Tls2odkzQ63gTy5kuH55hOkygwn0aB%2BBW8Gv9n3NCXzh8xEWLhTv1FECNUcMuta2tWRbQSoQ1Pcupv8iz07UV2oBqWHYdksgXStE4h4r1sDiMLHWhBjUGM%2BdUWKfFtW0PIqgq%2FBWEzCvfgbf7Wur5%2FZiv%2BahEhYw%2FfmWvQY6pgHK17RqLNMwcRrKIEzreq3HOyLYn1keg%2FXcjaAtz526P7wgBRY2OznEFUgpSrjyUY9k7LCdWYDqxcy9Khn6G1lRXtU9pHLo209tu15M7RpmuVU99xKoJIXbLaHXJ86ZtPexXe9j2z0FCaRMJbu%2FGQ3N5xUXvHo8rEZ5gym6MNDsWl3ZgWpYtWakvGlhq2vDm%2FGYXUC5VYj9hqFYo14OQxQowID71Lqa&X-Amz-Signature=6b2879ef2c22041d2299ae2d233f7bb2cae513ddeb668baf6b40c9ee9c4047ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJHGAWZC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXb7bWNUyPlGRZy8HfsK6vk6wOO0P34bHV3i9Fb%2BjSAAiBaKwPf1tLqf%2Fk7%2B4OaVMU%2B%2FidV6OPCMFwXhBifFo0%2BrCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMq%2FLskwvL1xErtzuyKtwDE2FW1EsYooneCHjc0CzaV0f6ViGZ9ihlRFAQEf4HzhEB5Y1%2BfSaURvNNd17BMlS7ntZaZE9u7RIKAGWGPFeg%2BwG%2Bc%2FfybO6lVRxnkBYcSp1deKhQx9NzDV8AVJGB8C8utyyESZpsn1boBJ68WE%2Bb7LHycHd2GXj6aIfXN%2BSC4Z358pCownKgD%2FP9182OpL4qkWb6M4Rhw7mPrz81jXfCweT6pCzu7JRWONKnBVT4fXw4%2F9zQrD2cwAylD%2BDaMDqbSi7U5Pu8CWsydMysSTtsmuUYA9VXZmgXLWpB2tl%2FqJzIANsWvE9Y2ZuxqG5JyTiEO9pREBNRqNpjG38ziqoRD0E6Fc2urOT%2BkgPMEsCEXPBZjVuP04j0PRxDZFKaWf6kh%2BSuAAeCZ1lK7n0gok6hjhBTsNqYSNQtHWMRdQ1kkiqOlEHlPn547qDbavLaNXoiZvpJwoU2vIXP81GQOpF%2FhK841pk2Tls2odkzQ63gTy5kuH55hOkygwn0aB%2BBW8Gv9n3NCXzh8xEWLhTv1FECNUcMuta2tWRbQSoQ1Pcupv8iz07UV2oBqWHYdksgXStE4h4r1sDiMLHWhBjUGM%2BdUWKfFtW0PIqgq%2FBWEzCvfgbf7Wur5%2FZiv%2BahEhYw%2FfmWvQY6pgHK17RqLNMwcRrKIEzreq3HOyLYn1keg%2FXcjaAtz526P7wgBRY2OznEFUgpSrjyUY9k7LCdWYDqxcy9Khn6G1lRXtU9pHLo209tu15M7RpmuVU99xKoJIXbLaHXJ86ZtPexXe9j2z0FCaRMJbu%2FGQ3N5xUXvHo8rEZ5gym6MNDsWl3ZgWpYtWakvGlhq2vDm%2FGYXUC5VYj9hqFYo14OQxQowID71Lqa&X-Amz-Signature=d2fa8f9f638c5ef89b5aa40d67dfef4df7535b7695beddb348050e687480d127&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJHGAWZC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXb7bWNUyPlGRZy8HfsK6vk6wOO0P34bHV3i9Fb%2BjSAAiBaKwPf1tLqf%2Fk7%2B4OaVMU%2B%2FidV6OPCMFwXhBifFo0%2BrCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMq%2FLskwvL1xErtzuyKtwDE2FW1EsYooneCHjc0CzaV0f6ViGZ9ihlRFAQEf4HzhEB5Y1%2BfSaURvNNd17BMlS7ntZaZE9u7RIKAGWGPFeg%2BwG%2Bc%2FfybO6lVRxnkBYcSp1deKhQx9NzDV8AVJGB8C8utyyESZpsn1boBJ68WE%2Bb7LHycHd2GXj6aIfXN%2BSC4Z358pCownKgD%2FP9182OpL4qkWb6M4Rhw7mPrz81jXfCweT6pCzu7JRWONKnBVT4fXw4%2F9zQrD2cwAylD%2BDaMDqbSi7U5Pu8CWsydMysSTtsmuUYA9VXZmgXLWpB2tl%2FqJzIANsWvE9Y2ZuxqG5JyTiEO9pREBNRqNpjG38ziqoRD0E6Fc2urOT%2BkgPMEsCEXPBZjVuP04j0PRxDZFKaWf6kh%2BSuAAeCZ1lK7n0gok6hjhBTsNqYSNQtHWMRdQ1kkiqOlEHlPn547qDbavLaNXoiZvpJwoU2vIXP81GQOpF%2FhK841pk2Tls2odkzQ63gTy5kuH55hOkygwn0aB%2BBW8Gv9n3NCXzh8xEWLhTv1FECNUcMuta2tWRbQSoQ1Pcupv8iz07UV2oBqWHYdksgXStE4h4r1sDiMLHWhBjUGM%2BdUWKfFtW0PIqgq%2FBWEzCvfgbf7Wur5%2FZiv%2BahEhYw%2FfmWvQY6pgHK17RqLNMwcRrKIEzreq3HOyLYn1keg%2FXcjaAtz526P7wgBRY2OznEFUgpSrjyUY9k7LCdWYDqxcy9Khn6G1lRXtU9pHLo209tu15M7RpmuVU99xKoJIXbLaHXJ86ZtPexXe9j2z0FCaRMJbu%2FGQ3N5xUXvHo8rEZ5gym6MNDsWl3ZgWpYtWakvGlhq2vDm%2FGYXUC5VYj9hqFYo14OQxQowID71Lqa&X-Amz-Signature=64268d1765876440dcbb36cfab0ab8785a1d7eee7e8a434adad0a52b3e542b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJHGAWZC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXb7bWNUyPlGRZy8HfsK6vk6wOO0P34bHV3i9Fb%2BjSAAiBaKwPf1tLqf%2Fk7%2B4OaVMU%2B%2FidV6OPCMFwXhBifFo0%2BrCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMq%2FLskwvL1xErtzuyKtwDE2FW1EsYooneCHjc0CzaV0f6ViGZ9ihlRFAQEf4HzhEB5Y1%2BfSaURvNNd17BMlS7ntZaZE9u7RIKAGWGPFeg%2BwG%2Bc%2FfybO6lVRxnkBYcSp1deKhQx9NzDV8AVJGB8C8utyyESZpsn1boBJ68WE%2Bb7LHycHd2GXj6aIfXN%2BSC4Z358pCownKgD%2FP9182OpL4qkWb6M4Rhw7mPrz81jXfCweT6pCzu7JRWONKnBVT4fXw4%2F9zQrD2cwAylD%2BDaMDqbSi7U5Pu8CWsydMysSTtsmuUYA9VXZmgXLWpB2tl%2FqJzIANsWvE9Y2ZuxqG5JyTiEO9pREBNRqNpjG38ziqoRD0E6Fc2urOT%2BkgPMEsCEXPBZjVuP04j0PRxDZFKaWf6kh%2BSuAAeCZ1lK7n0gok6hjhBTsNqYSNQtHWMRdQ1kkiqOlEHlPn547qDbavLaNXoiZvpJwoU2vIXP81GQOpF%2FhK841pk2Tls2odkzQ63gTy5kuH55hOkygwn0aB%2BBW8Gv9n3NCXzh8xEWLhTv1FECNUcMuta2tWRbQSoQ1Pcupv8iz07UV2oBqWHYdksgXStE4h4r1sDiMLHWhBjUGM%2BdUWKfFtW0PIqgq%2FBWEzCvfgbf7Wur5%2FZiv%2BahEhYw%2FfmWvQY6pgHK17RqLNMwcRrKIEzreq3HOyLYn1keg%2FXcjaAtz526P7wgBRY2OznEFUgpSrjyUY9k7LCdWYDqxcy9Khn6G1lRXtU9pHLo209tu15M7RpmuVU99xKoJIXbLaHXJ86ZtPexXe9j2z0FCaRMJbu%2FGQ3N5xUXvHo8rEZ5gym6MNDsWl3ZgWpYtWakvGlhq2vDm%2FGYXUC5VYj9hqFYo14OQxQowID71Lqa&X-Amz-Signature=dc705af112cb3015bd40dc69b0e4d2894abe104e33a07fec410cb8be40e84831&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z46RFDDW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAHBwecHSuBDxAuGvnVuIu0BnfbVDhvgm%2FHDwjvNaCHgAiA%2BQsQtjeFFrLP8%2F7mSD7tfcS6ZttcdPEyR16MrfeP77Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMIghzFz0Z9BHSNZMhKtwDWkgQgl%2Bc%2Bc0xGOeFZIICp%2B1Ldxy982aPshJNEsHYbJqLbJiLO5NCTZFIpbeZ%2B%2F12oYZCVQUhWfSGV3moeF%2FXg%2BuiJW1AZHVYaY6wAEuHJJ%2Fvgyvr%2B5QIOoq%2BXRYMm5SRnnfP47s1JoRTNikHaLswHWRhZWN08EUU2q0JBESt4ZjvOnKCXzoPPZb%2BubrSwWK0Sjd98KSg31YbfAsHvFNSVnfvrCse7qCcccKHOH9sbK6lfyYx2hVb4xVq9eDBNrNEa7SAJybG9sdi3vGBKVy7RW0nzvCR7xeMmil5P3GrWVeQHctWD2HGFwk3HYMh1wIQcmjcYE0XBZFPO2GvmHoNSrgBQ9QfFgbdE6eYFG2LXn00KU1BtIcEGPB9%2FICdtLxvjsATzmJuS2kM%2B7I2vdovuyJHRmIZViN3E%2FcHNuwuzcooGCgBA5LryIjFI1VwDNUIZLm%2B60jbrYu3p5zQG8NF1lfNut0IL3A5KLN4Mn0j5TM6EzhfEd0AtRvl3QY6d80NhU8mPtx4F1YiyVQxalk56uvDRipg7xM43es4nCOJCkorIwAwMZkDcWVpl3%2BimUaX37d4Nj8w8ZFgb82GXuU%2FFkzjKkgpEMfuzdfcPjWtJCzeJfHGOzY%2B3nEx9j8w%2BPmWvQY6pgHHEwUtkRf4SrtQRotZZtQHVbDogqfHdqhuWRFaeC82IJAfMQj6f8sN2vThVM%2BjXkP4cHxdKPe1kYUSap5yEFANWOPS8g7bTXzhgJ%2B7IUBVjDUqMURHPetH%2BizC4KEvOzcIouIlIzEpq5QsIgjbDlJaBWQKMMfqmLTDsyACZ3lASnbHTr4RddBk9nsfjpYTEzI3YEeEjVhGLoLiPj9dUyOyUTRt79W9&X-Amz-Signature=f15a916b7ec94c11dfcf152f40809187f40930711937c6ecff78466a672f71ba&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z46RFDDW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAHBwecHSuBDxAuGvnVuIu0BnfbVDhvgm%2FHDwjvNaCHgAiA%2BQsQtjeFFrLP8%2F7mSD7tfcS6ZttcdPEyR16MrfeP77Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMIghzFz0Z9BHSNZMhKtwDWkgQgl%2Bc%2Bc0xGOeFZIICp%2B1Ldxy982aPshJNEsHYbJqLbJiLO5NCTZFIpbeZ%2B%2F12oYZCVQUhWfSGV3moeF%2FXg%2BuiJW1AZHVYaY6wAEuHJJ%2Fvgyvr%2B5QIOoq%2BXRYMm5SRnnfP47s1JoRTNikHaLswHWRhZWN08EUU2q0JBESt4ZjvOnKCXzoPPZb%2BubrSwWK0Sjd98KSg31YbfAsHvFNSVnfvrCse7qCcccKHOH9sbK6lfyYx2hVb4xVq9eDBNrNEa7SAJybG9sdi3vGBKVy7RW0nzvCR7xeMmil5P3GrWVeQHctWD2HGFwk3HYMh1wIQcmjcYE0XBZFPO2GvmHoNSrgBQ9QfFgbdE6eYFG2LXn00KU1BtIcEGPB9%2FICdtLxvjsATzmJuS2kM%2B7I2vdovuyJHRmIZViN3E%2FcHNuwuzcooGCgBA5LryIjFI1VwDNUIZLm%2B60jbrYu3p5zQG8NF1lfNut0IL3A5KLN4Mn0j5TM6EzhfEd0AtRvl3QY6d80NhU8mPtx4F1YiyVQxalk56uvDRipg7xM43es4nCOJCkorIwAwMZkDcWVpl3%2BimUaX37d4Nj8w8ZFgb82GXuU%2FFkzjKkgpEMfuzdfcPjWtJCzeJfHGOzY%2B3nEx9j8w%2BPmWvQY6pgHHEwUtkRf4SrtQRotZZtQHVbDogqfHdqhuWRFaeC82IJAfMQj6f8sN2vThVM%2BjXkP4cHxdKPe1kYUSap5yEFANWOPS8g7bTXzhgJ%2B7IUBVjDUqMURHPetH%2BizC4KEvOzcIouIlIzEpq5QsIgjbDlJaBWQKMMfqmLTDsyACZ3lASnbHTr4RddBk9nsfjpYTEzI3YEeEjVhGLoLiPj9dUyOyUTRt79W9&X-Amz-Signature=f9c12801cf5c0cdcb102dfb23443652aaf2f6e2b5b7a65eda9a51fe5cad6ae65&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z46RFDDW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAHBwecHSuBDxAuGvnVuIu0BnfbVDhvgm%2FHDwjvNaCHgAiA%2BQsQtjeFFrLP8%2F7mSD7tfcS6ZttcdPEyR16MrfeP77Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMIghzFz0Z9BHSNZMhKtwDWkgQgl%2Bc%2Bc0xGOeFZIICp%2B1Ldxy982aPshJNEsHYbJqLbJiLO5NCTZFIpbeZ%2B%2F12oYZCVQUhWfSGV3moeF%2FXg%2BuiJW1AZHVYaY6wAEuHJJ%2Fvgyvr%2B5QIOoq%2BXRYMm5SRnnfP47s1JoRTNikHaLswHWRhZWN08EUU2q0JBESt4ZjvOnKCXzoPPZb%2BubrSwWK0Sjd98KSg31YbfAsHvFNSVnfvrCse7qCcccKHOH9sbK6lfyYx2hVb4xVq9eDBNrNEa7SAJybG9sdi3vGBKVy7RW0nzvCR7xeMmil5P3GrWVeQHctWD2HGFwk3HYMh1wIQcmjcYE0XBZFPO2GvmHoNSrgBQ9QfFgbdE6eYFG2LXn00KU1BtIcEGPB9%2FICdtLxvjsATzmJuS2kM%2B7I2vdovuyJHRmIZViN3E%2FcHNuwuzcooGCgBA5LryIjFI1VwDNUIZLm%2B60jbrYu3p5zQG8NF1lfNut0IL3A5KLN4Mn0j5TM6EzhfEd0AtRvl3QY6d80NhU8mPtx4F1YiyVQxalk56uvDRipg7xM43es4nCOJCkorIwAwMZkDcWVpl3%2BimUaX37d4Nj8w8ZFgb82GXuU%2FFkzjKkgpEMfuzdfcPjWtJCzeJfHGOzY%2B3nEx9j8w%2BPmWvQY6pgHHEwUtkRf4SrtQRotZZtQHVbDogqfHdqhuWRFaeC82IJAfMQj6f8sN2vThVM%2BjXkP4cHxdKPe1kYUSap5yEFANWOPS8g7bTXzhgJ%2B7IUBVjDUqMURHPetH%2BizC4KEvOzcIouIlIzEpq5QsIgjbDlJaBWQKMMfqmLTDsyACZ3lASnbHTr4RddBk9nsfjpYTEzI3YEeEjVhGLoLiPj9dUyOyUTRt79W9&X-Amz-Signature=ae631d4b32d86a0eb294f4d6a879bff92ff94dc07d4f39c76ba6dff897cdbb8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

