

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=e802b25f4e5ba4baca814218823faae0cbd7e65ebadc1f7f4e7e8760c8db3424&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=f4213be287eb317217390ef2bc1d42e2c1908500ebf07bcf0e7dbe5b961ee12c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=76394ab76b22d6e912fa835fdd84070e14578bf443f5c28047c8e0a4e397b620&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=444d32c8c7d6a55763966c5134d2d929c569917011b147c718f0a83c46f98491&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=02db7c810b42707f7bd7309d97115f0e92ddce6d2cea3093cfd8b27d686b450c&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=0d9a30c3a7d2e6287e06281cdf382df1569c370e62c06851c726fdfc93c5f16c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=e6cb6b7719892f3dc71d500d2b99bcdb2c5a623e059374f1cd90e09c746b1405&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=669f8b0c85d4a5171cf3999ee30b51934dd026bf25343cae9b644bf75f6aeda1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=9b40f1d4b695f8924059a297cbdb61263c986d15e59ba719be04f5359e44a321&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=a1083abcd57e06e53a8649952e31fe419f3effc8c72e67f1ae18f097c9dad618&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHGS7S5O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDBA%2BdK7N3b%2FS903%2Bm5CKokbRreun92Lr%2B0MgyD9YMTPQIhAP39nacSzj6ey2hxFeT6C5dux5tLfI%2BiVb2aFIvTlLSsKv8DCCsQABoMNjM3NDIzMTgzODA1IgyQ8KGpozHQSqzNkTcq3APTAc3BBRgEuZ5kdx%2BujLz8aVwemi2gdno%2FwPM5eYhc9wR%2F4n%2BHzsORjKmVZ41FZe314ZBsS%2BKT9n%2BPF9nisTCZnmG8jMquOsf3wTI48YdSS9FfdFziMvRv9AA%2FnnYdSSa5lhvafE4qIEvFW7pkCpjcBgBEYmvYflzo9Mpb9T8VpEthlJvXUPtsqlEm8lVgJM1K8Gd6Li6eYtQjYvFT%2BM5z0OQxjGwo2dWiYwv0g2LR8xQhcAEkJJmOlKxOypHxJlzDC1xcMWD%2Bnt4VnVprh%2BRdDGmLliwaPnU2shBuW3nwAf%2FRoDfIvTE4dA1B65Q1QINvFMs%2BosqOMjLWrCD7v0ZO1KRUgui%2BUW2vBOLBl3qAgVnx7BgaoucSNhjkTrrj1yqeKwnf0k%2F2fgbmYwsvwAq5RM1p6M7R5AiBQ%2FcpDpN7fYmelJRskAHB55YP1IEm30qFNZQGJ7s5e1LsxBUmUgGjgbp7mKvKMiS%2F5xim8hhEtfPh72AO9FXbZ72a2wbAcynB6%2BzS3Z%2FyOMPNEe7HFwFlOkPmGkuIqIGWjngPS7%2FkXxlQWWzfUscR6MEMa5WXBMKg5vU6LrEFRnEmGvsdbvHUs1uYnhz0y%2FnzXC6TZT%2FkP5Ns0KCU3PeLH4%2F3UTCNyoe9BjqkAb1n%2F%2B9DuifGKDUNzxy%2F5dQU38au2HzxuG%2FATeueV5mBVHr8gmhfWP9KKfZEBqDu2UI%2BGWxYl1N%2BlqSbqnktsfmkKml7E%2BipR2DIydb%2BGfIaZvahPTlAX%2BhDhgYJBj0so3usrY2KfGIXDGXOsa3Mjs%2Bw1EFxb6LKqKL06GbtjRlXa5uKcdMU9pBDTvzRGX%2BniCDQc1IPsOiz3r2ZT%2FFOAcD8hFu%2B&X-Amz-Signature=8984252b2c51483570de5222dd356e72440d91e057f2d3d65661ce0dbb8ac44e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C5SN4L6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCICCB9MOo66YfbVLkxKsWgG4dAs95A6n4%2Bjhq7nZygc7fAiBZmrSeAo992kA8R41bd40Tvf2iIOQm969ApfQ2Elv5bCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMDEhlvE7yAjkgOZPiKtwDIllPjYNKxtl7cedKEmpnSVVX1Nkeg7rwjDkaHBdRbPAY1ezwcnGk1QQuCQqKUMpUO%2B3Wj6kv7RFc9%2FuTfLLMdwIUXDWwp7%2FYdFIsH5MpH%2BEnHKXsmVk%2BNNLkaa86nxyTaLGh3ADqdvd1SIQB1wVvE8AW6yLk7FxiWgfR8MDsiGkEYERs%2Fq9q69uwGWIqKVg87KDyIUjUwy%2FCuD%2BHrPJPZy3eGUsjoVgq9xVZPLRL7lnxCjLKEdbMEXiJ4VhELPQJNhxLh9BbFef9J2q%2FjfzRjQJlDT5LBRR%2B8ZqV6ndQ4sE97%2BdoIB3KxVr5zb2IA1LaXC2IO6OuMnqmF%2Bj0KJFlnNuehzRnpEwFn0ty8%2F42JUGXizhXw2SxLcZNnM3ZLbXcPZNrThWyy44rnabdYqr6n3D1yz5N%2F2EVt%2Fjc7WVNT2tHzZqoKf%2BQv%2Bg7lNzUvTZvPZZT7Lu5ypPmBstREqKrsofWW4lYPgLI2IwRhPO4%2BynhKgYLZS9EctHdJSEKW7pguzT9H00KHsnJQvsHnFDOEOm4PSpieaTh4cQQKQIxY%2BE0FV5DpYNXRE8IlFqvrNuIArKY6MLEIlnbKvtgiQOr%2FqMVrs9Q6RfUBIwOwsVVmOMe9dBD6sgQ%2BWtFfMkwycqHvQY6pgHfXhXT1avZbJfoRgi5ii6XwE%2FsouYaWJv%2Fgepaxk49sALIxCNmbd9U%2BO3njYEg3Wdb2ZWgFQxAbDjUexz5iEvPb%2BFgrl4LxbIHSSamusJJct%2FgmN7PujpQvnH%2Bt9%2Bd2butwn91gGvcQ8GSk7vxewGkjSxw50DgcqiFUJKUfe1YTdbd5Z7qDLSm2rj1L7OWYyxNqGEWb4h6eHbW9kSK%2BirL8ySn6QVD&X-Amz-Signature=7ac51532d0aeeb6915214d3d18a6d199075fe18fa6f4a460b695b8bead6513ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C5SN4L6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCICCB9MOo66YfbVLkxKsWgG4dAs95A6n4%2Bjhq7nZygc7fAiBZmrSeAo992kA8R41bd40Tvf2iIOQm969ApfQ2Elv5bCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMDEhlvE7yAjkgOZPiKtwDIllPjYNKxtl7cedKEmpnSVVX1Nkeg7rwjDkaHBdRbPAY1ezwcnGk1QQuCQqKUMpUO%2B3Wj6kv7RFc9%2FuTfLLMdwIUXDWwp7%2FYdFIsH5MpH%2BEnHKXsmVk%2BNNLkaa86nxyTaLGh3ADqdvd1SIQB1wVvE8AW6yLk7FxiWgfR8MDsiGkEYERs%2Fq9q69uwGWIqKVg87KDyIUjUwy%2FCuD%2BHrPJPZy3eGUsjoVgq9xVZPLRL7lnxCjLKEdbMEXiJ4VhELPQJNhxLh9BbFef9J2q%2FjfzRjQJlDT5LBRR%2B8ZqV6ndQ4sE97%2BdoIB3KxVr5zb2IA1LaXC2IO6OuMnqmF%2Bj0KJFlnNuehzRnpEwFn0ty8%2F42JUGXizhXw2SxLcZNnM3ZLbXcPZNrThWyy44rnabdYqr6n3D1yz5N%2F2EVt%2Fjc7WVNT2tHzZqoKf%2BQv%2Bg7lNzUvTZvPZZT7Lu5ypPmBstREqKrsofWW4lYPgLI2IwRhPO4%2BynhKgYLZS9EctHdJSEKW7pguzT9H00KHsnJQvsHnFDOEOm4PSpieaTh4cQQKQIxY%2BE0FV5DpYNXRE8IlFqvrNuIArKY6MLEIlnbKvtgiQOr%2FqMVrs9Q6RfUBIwOwsVVmOMe9dBD6sgQ%2BWtFfMkwycqHvQY6pgHfXhXT1avZbJfoRgi5ii6XwE%2FsouYaWJv%2Fgepaxk49sALIxCNmbd9U%2BO3njYEg3Wdb2ZWgFQxAbDjUexz5iEvPb%2BFgrl4LxbIHSSamusJJct%2FgmN7PujpQvnH%2Bt9%2Bd2butwn91gGvcQ8GSk7vxewGkjSxw50DgcqiFUJKUfe1YTdbd5Z7qDLSm2rj1L7OWYyxNqGEWb4h6eHbW9kSK%2BirL8ySn6QVD&X-Amz-Signature=93047eb202cb4f463ffceca51501d28ad5b8219c1f19f2c1406e8e4213fa61f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C5SN4L6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCICCB9MOo66YfbVLkxKsWgG4dAs95A6n4%2Bjhq7nZygc7fAiBZmrSeAo992kA8R41bd40Tvf2iIOQm969ApfQ2Elv5bCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMDEhlvE7yAjkgOZPiKtwDIllPjYNKxtl7cedKEmpnSVVX1Nkeg7rwjDkaHBdRbPAY1ezwcnGk1QQuCQqKUMpUO%2B3Wj6kv7RFc9%2FuTfLLMdwIUXDWwp7%2FYdFIsH5MpH%2BEnHKXsmVk%2BNNLkaa86nxyTaLGh3ADqdvd1SIQB1wVvE8AW6yLk7FxiWgfR8MDsiGkEYERs%2Fq9q69uwGWIqKVg87KDyIUjUwy%2FCuD%2BHrPJPZy3eGUsjoVgq9xVZPLRL7lnxCjLKEdbMEXiJ4VhELPQJNhxLh9BbFef9J2q%2FjfzRjQJlDT5LBRR%2B8ZqV6ndQ4sE97%2BdoIB3KxVr5zb2IA1LaXC2IO6OuMnqmF%2Bj0KJFlnNuehzRnpEwFn0ty8%2F42JUGXizhXw2SxLcZNnM3ZLbXcPZNrThWyy44rnabdYqr6n3D1yz5N%2F2EVt%2Fjc7WVNT2tHzZqoKf%2BQv%2Bg7lNzUvTZvPZZT7Lu5ypPmBstREqKrsofWW4lYPgLI2IwRhPO4%2BynhKgYLZS9EctHdJSEKW7pguzT9H00KHsnJQvsHnFDOEOm4PSpieaTh4cQQKQIxY%2BE0FV5DpYNXRE8IlFqvrNuIArKY6MLEIlnbKvtgiQOr%2FqMVrs9Q6RfUBIwOwsVVmOMe9dBD6sgQ%2BWtFfMkwycqHvQY6pgHfXhXT1avZbJfoRgi5ii6XwE%2FsouYaWJv%2Fgepaxk49sALIxCNmbd9U%2BO3njYEg3Wdb2ZWgFQxAbDjUexz5iEvPb%2BFgrl4LxbIHSSamusJJct%2FgmN7PujpQvnH%2Bt9%2Bd2butwn91gGvcQ8GSk7vxewGkjSxw50DgcqiFUJKUfe1YTdbd5Z7qDLSm2rj1L7OWYyxNqGEWb4h6eHbW9kSK%2BirL8ySn6QVD&X-Amz-Signature=c243dbedded287b0610b4e95a71f7aa7a9da822d1687cc97fcb427ba21024d22&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C5SN4L6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCICCB9MOo66YfbVLkxKsWgG4dAs95A6n4%2Bjhq7nZygc7fAiBZmrSeAo992kA8R41bd40Tvf2iIOQm969ApfQ2Elv5bCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMDEhlvE7yAjkgOZPiKtwDIllPjYNKxtl7cedKEmpnSVVX1Nkeg7rwjDkaHBdRbPAY1ezwcnGk1QQuCQqKUMpUO%2B3Wj6kv7RFc9%2FuTfLLMdwIUXDWwp7%2FYdFIsH5MpH%2BEnHKXsmVk%2BNNLkaa86nxyTaLGh3ADqdvd1SIQB1wVvE8AW6yLk7FxiWgfR8MDsiGkEYERs%2Fq9q69uwGWIqKVg87KDyIUjUwy%2FCuD%2BHrPJPZy3eGUsjoVgq9xVZPLRL7lnxCjLKEdbMEXiJ4VhELPQJNhxLh9BbFef9J2q%2FjfzRjQJlDT5LBRR%2B8ZqV6ndQ4sE97%2BdoIB3KxVr5zb2IA1LaXC2IO6OuMnqmF%2Bj0KJFlnNuehzRnpEwFn0ty8%2F42JUGXizhXw2SxLcZNnM3ZLbXcPZNrThWyy44rnabdYqr6n3D1yz5N%2F2EVt%2Fjc7WVNT2tHzZqoKf%2BQv%2Bg7lNzUvTZvPZZT7Lu5ypPmBstREqKrsofWW4lYPgLI2IwRhPO4%2BynhKgYLZS9EctHdJSEKW7pguzT9H00KHsnJQvsHnFDOEOm4PSpieaTh4cQQKQIxY%2BE0FV5DpYNXRE8IlFqvrNuIArKY6MLEIlnbKvtgiQOr%2FqMVrs9Q6RfUBIwOwsVVmOMe9dBD6sgQ%2BWtFfMkwycqHvQY6pgHfXhXT1avZbJfoRgi5ii6XwE%2FsouYaWJv%2Fgepaxk49sALIxCNmbd9U%2BO3njYEg3Wdb2ZWgFQxAbDjUexz5iEvPb%2BFgrl4LxbIHSSamusJJct%2FgmN7PujpQvnH%2Bt9%2Bd2butwn91gGvcQ8GSk7vxewGkjSxw50DgcqiFUJKUfe1YTdbd5Z7qDLSm2rj1L7OWYyxNqGEWb4h6eHbW9kSK%2BirL8ySn6QVD&X-Amz-Signature=61725663b9862b57b90ec4fa1e279b255644d6972d03927d9cae2dc2583d98f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WSBDEED%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCbkla2zr5HEsLmo0iVxKd5V79FmNh%2BRPAdy2t2jalCZAIgc48AJ7koORwriLtFrxiQbRTdt1qgTZuDAXYyeUyd4D0q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIJw5ZaG0IHUAZiv0CrcA2%2Bfcz3yUEz2SB3TI4TwKi%2FlHZPJoSn1QREVx48rNrnNWX3wySRi2I1w6o6%2FZ6WI4AvAPlP%2BUPJtJl%2BZkfiuY%2B9BgxLyfyFqHXqp%2BEtwfk%2FPoPW3bRTl3cmAhUMmHbVNvJs%2BV%2BBc0NMcv49TMgugvJhe5dh7QUx8sLLjo3O2yctJRMdjxdFmqnC1vYDEh1psREhgF1eEhVqhMmjRCQlqFqF8pmtzhQm8tUC6cZrGMUZd9CzYM%2BjitBti7BrLCWAD0qAxE4E5TFGXe8SBIPLQdO%2BVN45w4sVLRAI%2BLBREd%2BnZtEcX7f3AoVcgu8oknlW3jU7cKE74mILzpS06Cgf8sXOTl6lO6F6IYGjlngXlgwZ2cWQgBluuk0SQwy7wUuB%2B3GKvlZAw75CEgki79Pgw%2FEfWRXQiWlkKD7JGcCxoq1%2FxcGFGHdl8ez55qOh%2FEvvWCtlgM5buMkt0VrOwdBX7Yzlq4WtPsDfUiMmC8igYD3vVgwuPf91UxbLfqKQ00MsyVLDUNWjl6Rc4rYdt2iMAkDrQp7pXgYmb7X9QqW2XmDuCmvEnBKJYmOmSHmALOw8hFcISHH31qmy%2B1USTi8a8pknve3LhLPPOGgcagkHyPo2Fa0TKR%2BNMD7FrZDZ3MOLKh70GOqUB3P5aBvBbgZL7MELM3Hb59DHWT2n6S7clPTooV0t%2B7MAP5041QcvnGcKSa20lfdksNzF7aq0CIJ5imSjWjyLol9HYWziAddfYo5QOkqijbDquZv3kqn4p6uLW%2Fe8Q2%2BS07ahUah7eH%2FL8y8sGw1Ol9CsLspKwF7JAMMmRPh0SYebrAqNRx4p%2F7jMGPLZ1dU5Q6nJtWL28t1o7%2Bjg5cmES1ueYobnM&X-Amz-Signature=be0994a12b6c2329bc33cc860c6e550d71ac7438e23f210447b286c6a0c281b4&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WSBDEED%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCbkla2zr5HEsLmo0iVxKd5V79FmNh%2BRPAdy2t2jalCZAIgc48AJ7koORwriLtFrxiQbRTdt1qgTZuDAXYyeUyd4D0q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIJw5ZaG0IHUAZiv0CrcA2%2Bfcz3yUEz2SB3TI4TwKi%2FlHZPJoSn1QREVx48rNrnNWX3wySRi2I1w6o6%2FZ6WI4AvAPlP%2BUPJtJl%2BZkfiuY%2B9BgxLyfyFqHXqp%2BEtwfk%2FPoPW3bRTl3cmAhUMmHbVNvJs%2BV%2BBc0NMcv49TMgugvJhe5dh7QUx8sLLjo3O2yctJRMdjxdFmqnC1vYDEh1psREhgF1eEhVqhMmjRCQlqFqF8pmtzhQm8tUC6cZrGMUZd9CzYM%2BjitBti7BrLCWAD0qAxE4E5TFGXe8SBIPLQdO%2BVN45w4sVLRAI%2BLBREd%2BnZtEcX7f3AoVcgu8oknlW3jU7cKE74mILzpS06Cgf8sXOTl6lO6F6IYGjlngXlgwZ2cWQgBluuk0SQwy7wUuB%2B3GKvlZAw75CEgki79Pgw%2FEfWRXQiWlkKD7JGcCxoq1%2FxcGFGHdl8ez55qOh%2FEvvWCtlgM5buMkt0VrOwdBX7Yzlq4WtPsDfUiMmC8igYD3vVgwuPf91UxbLfqKQ00MsyVLDUNWjl6Rc4rYdt2iMAkDrQp7pXgYmb7X9QqW2XmDuCmvEnBKJYmOmSHmALOw8hFcISHH31qmy%2B1USTi8a8pknve3LhLPPOGgcagkHyPo2Fa0TKR%2BNMD7FrZDZ3MOLKh70GOqUB3P5aBvBbgZL7MELM3Hb59DHWT2n6S7clPTooV0t%2B7MAP5041QcvnGcKSa20lfdksNzF7aq0CIJ5imSjWjyLol9HYWziAddfYo5QOkqijbDquZv3kqn4p6uLW%2Fe8Q2%2BS07ahUah7eH%2FL8y8sGw1Ol9CsLspKwF7JAMMmRPh0SYebrAqNRx4p%2F7jMGPLZ1dU5Q6nJtWL28t1o7%2Bjg5cmES1ueYobnM&X-Amz-Signature=ea61d05696de03958c118a5c1014e1ac43919417ce88d91081ea3d35a1a5dc18&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WSBDEED%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCbkla2zr5HEsLmo0iVxKd5V79FmNh%2BRPAdy2t2jalCZAIgc48AJ7koORwriLtFrxiQbRTdt1qgTZuDAXYyeUyd4D0q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIJw5ZaG0IHUAZiv0CrcA2%2Bfcz3yUEz2SB3TI4TwKi%2FlHZPJoSn1QREVx48rNrnNWX3wySRi2I1w6o6%2FZ6WI4AvAPlP%2BUPJtJl%2BZkfiuY%2B9BgxLyfyFqHXqp%2BEtwfk%2FPoPW3bRTl3cmAhUMmHbVNvJs%2BV%2BBc0NMcv49TMgugvJhe5dh7QUx8sLLjo3O2yctJRMdjxdFmqnC1vYDEh1psREhgF1eEhVqhMmjRCQlqFqF8pmtzhQm8tUC6cZrGMUZd9CzYM%2BjitBti7BrLCWAD0qAxE4E5TFGXe8SBIPLQdO%2BVN45w4sVLRAI%2BLBREd%2BnZtEcX7f3AoVcgu8oknlW3jU7cKE74mILzpS06Cgf8sXOTl6lO6F6IYGjlngXlgwZ2cWQgBluuk0SQwy7wUuB%2B3GKvlZAw75CEgki79Pgw%2FEfWRXQiWlkKD7JGcCxoq1%2FxcGFGHdl8ez55qOh%2FEvvWCtlgM5buMkt0VrOwdBX7Yzlq4WtPsDfUiMmC8igYD3vVgwuPf91UxbLfqKQ00MsyVLDUNWjl6Rc4rYdt2iMAkDrQp7pXgYmb7X9QqW2XmDuCmvEnBKJYmOmSHmALOw8hFcISHH31qmy%2B1USTi8a8pknve3LhLPPOGgcagkHyPo2Fa0TKR%2BNMD7FrZDZ3MOLKh70GOqUB3P5aBvBbgZL7MELM3Hb59DHWT2n6S7clPTooV0t%2B7MAP5041QcvnGcKSa20lfdksNzF7aq0CIJ5imSjWjyLol9HYWziAddfYo5QOkqijbDquZv3kqn4p6uLW%2Fe8Q2%2BS07ahUah7eH%2FL8y8sGw1Ol9CsLspKwF7JAMMmRPh0SYebrAqNRx4p%2F7jMGPLZ1dU5Q6nJtWL28t1o7%2Bjg5cmES1ueYobnM&X-Amz-Signature=8469b12a74a215dc39a0396846d6874fea0886f2684e4357c554c7017987756c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

