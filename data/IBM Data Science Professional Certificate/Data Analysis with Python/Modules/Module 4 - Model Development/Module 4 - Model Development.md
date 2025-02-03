

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=8705f1c6f5be3778b6768b3b1a92d6610630f60d325984d2c903c6e3c8dc0cd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=d4586415b9c51f65308211eb4351f5d5ff11158ccd311bf2cb812be5ea12bcbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=b33642ad052def52077571e244d3a56abac0d34bff8f9ba1682a538430078c5c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=4219412d6a3627629c027579b750a788bfacea7e1d9262233ec7a0c16760a638&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=2faf30e8719cbe62e4963fe3d2b01e5be8fcf37e642e9a4ae3e635cfcb2f4e31&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=efd2b22f6d9f549b690ad7aed551be158bc8078d4561c617ee398a831117f35f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=a7f68599ebe119ebe9516b5610848514151ff76405db3c9593aa3d83102ca1f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=9f92f8e113e2ea1e15b49a14ee28927d2d3f406babf439d7f7846aedf1ad6332&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=f0c192fc355417ca4227c04f0de5f2b56b29369e6f827fd6ba6446314a48ee06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=e7d1c9f75a2ebff21d24a06d09f5fc390e98abc1c0c6baa7bff32cf1c2109531&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4W5VPT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC18tTHmZWhK1YWFqnO6MMxF1aR2t0W%2FmtMDgkzOU2iQgIgb%2Bk9RRzSHlHwLNvVJQLvUesyTJDf8gu4FHNH6Ki3Xq8q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDslhJ6S6kOWrpUIayrcA%2FGFYhbcttsCpII1pMRIk0gOaqJDkOGjY2Y9Kby%2Bpde2wBE0Up%2Bs08IrSuqv6xPEmUKebA%2BI8qJh27LkY7%2BgcpQKXIZ4EYV3lHHAMg3ZnDqJHqEeHvA3U1PUJCYLKjTMyAdoUDcYgxAup8rvTrYR0f45PizKvMDrfaSA1zjmIBw901EvS9%2F8cL0Lcfof6udf%2BNlxP3TnK8DWCrE8bsjrCXRKhIYTqdrtbAQcVZUyxyoA0%2FfrzIoIwWC7RpqorcSoSUvdviqh5SK0%2FZRX07acf4Sa7Kj1nmrcv1j6vtseesgSxSObQQEfJDL7ejahRztlARENOKZ%2BJD8JXtJX7JkhIXNbWCxQrXNqf5M3zlp0KqDXWx%2F24lbi7HyBomdPN20%2F23oxb%2BNI6xFG5UJtB7BZbVnDlvNC33ADtRnK6vA%2BACRAUEKzoPSX8uMr1q8lySNyzFNF0guru2ZM%2BReNqINtvqSkVAsdnT63wTiGoF3mFSZT7Xty0zj%2FItV3GVArDEbM%2FTYdpGQouPHwBC%2F%2BC56DbZRFuKyX88zcxMk71BJ3yEB3yXqNDnGb5rdzr7zHaxmUrSlFhnN1ssfgPXn%2FXFj797WsJ8hOhWToNkNn13sKg4p81DSrXqBlXHiKyBtUMPnZhL0GOqUBCicrH1PEVklc%2FCfmzqKKnFxLam30y4wqck9WIG%2BtlCHr8qi4sbTEYS3pbr3s2l5pqrUbo1VtfFhPiP9nBwZsaFp2Rd%2BQeMkemsefkakIY6pTeix6yWNCjeREI83wzJJnedlkVt5Mc8Qriytb0%2F%2BnkK639kEHTnXZ5mTQzWNEcAX5Kv9ciMlE%2B%2Bn2vPIy3kxeRexREkPZm83Awu1pfRxz%2FMzANkKu&X-Amz-Signature=e6ca67585653f803cd29f864b075591a26082c31bc7ebee8d8950a641385dd46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I75I2VK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIDnNqTUprtvLa2jF%2FAQudenP%2FT4oruTq7a03cLKTmsW6AiB1vxSnWyRQflyAAn8%2F1JaRNwyn7jI22PxGeJGmKc804Sr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMZWR%2BW3VSWn3G%2FP1XKtwDU%2Fw2kDp%2FBPmVueYaFOrk495gBbRGG5lX12AuD889RUuiniRK8V%2FON6b5kUf9al1Hd5hzr0iJDM8u6wllXY%2Fkg%2FQuN4N2ocTtniNp0YjPKeA6b8EoF4HpQIn1odVlo0cO0sjiATNr3%2BjkXVoetA9XZ29Pcs0zl68pyxf0K3fAiW5NQ83vaIAGBY0l02YLVNZIVxU1EQ87KfixpxObKEWQFmpUQz2Q5S1hqzaIvFv70kSjuRBfXP%2FbPvpNX6kzccq%2BsgeKFWMva7FU%2FQmDmGEqGbna1OJvDi%2FLvoGnmUCl6Tv76HJrX1lJll7X0McSniY8lxJE7TaX3QSDD916qiU4Z6deG3z2JuoPLvXS9LBKUld%2FSp44stGt19aU2v3DLsJt6YD%2BUFu48zVkiHXKAozcKxAylQ8uldLWuzCVJnD3kCAXPpOCFyiyhSpUcvltvibxLKlk5cQ95PbPK9k3Q6BJStUYqMTH7RAXRxAsz3aIzMGCLBZ5x676h2usIEN%2FFGnEVpKqSpxwwZt%2FjMq52yDpx8dpT9f2idtBsukzUgsQkojY6PBj8HdbrtqDz%2FhuGRwQpVns2hqyY5Waj7eV8cvyPbYp9%2FYhTmIFbcBVmaol7AjoExI0DoklMK9WimIws9mEvQY6pgFowo3Vg8WW5kP%2F3HYcPWZ1KAcJXYKXrrQb4ReXAkwScDm0fNeYL%2BBKiQAEifkyWG9TDJYF%2FiYOJJ0FDMvJNc11a6MsXA9aw9ATWkuoiUHTDaJrRo%2FZGL3o%2FomECnSVtnLLzI93fEjj9qLtk%2F8jJxyp%2FLKEcIgf0Yl%2BNJ%2BZ2LSu2ptRRI2%2BJohx4r7397qCTceSkZr5kgo2WbN9jielujKc4sqrvfhJ&X-Amz-Signature=2e3d1d947697480ac14b51a0deb6bc90a1165119ddc80d604f7326e0165ee2a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I75I2VK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIDnNqTUprtvLa2jF%2FAQudenP%2FT4oruTq7a03cLKTmsW6AiB1vxSnWyRQflyAAn8%2F1JaRNwyn7jI22PxGeJGmKc804Sr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMZWR%2BW3VSWn3G%2FP1XKtwDU%2Fw2kDp%2FBPmVueYaFOrk495gBbRGG5lX12AuD889RUuiniRK8V%2FON6b5kUf9al1Hd5hzr0iJDM8u6wllXY%2Fkg%2FQuN4N2ocTtniNp0YjPKeA6b8EoF4HpQIn1odVlo0cO0sjiATNr3%2BjkXVoetA9XZ29Pcs0zl68pyxf0K3fAiW5NQ83vaIAGBY0l02YLVNZIVxU1EQ87KfixpxObKEWQFmpUQz2Q5S1hqzaIvFv70kSjuRBfXP%2FbPvpNX6kzccq%2BsgeKFWMva7FU%2FQmDmGEqGbna1OJvDi%2FLvoGnmUCl6Tv76HJrX1lJll7X0McSniY8lxJE7TaX3QSDD916qiU4Z6deG3z2JuoPLvXS9LBKUld%2FSp44stGt19aU2v3DLsJt6YD%2BUFu48zVkiHXKAozcKxAylQ8uldLWuzCVJnD3kCAXPpOCFyiyhSpUcvltvibxLKlk5cQ95PbPK9k3Q6BJStUYqMTH7RAXRxAsz3aIzMGCLBZ5x676h2usIEN%2FFGnEVpKqSpxwwZt%2FjMq52yDpx8dpT9f2idtBsukzUgsQkojY6PBj8HdbrtqDz%2FhuGRwQpVns2hqyY5Waj7eV8cvyPbYp9%2FYhTmIFbcBVmaol7AjoExI0DoklMK9WimIws9mEvQY6pgFowo3Vg8WW5kP%2F3HYcPWZ1KAcJXYKXrrQb4ReXAkwScDm0fNeYL%2BBKiQAEifkyWG9TDJYF%2FiYOJJ0FDMvJNc11a6MsXA9aw9ATWkuoiUHTDaJrRo%2FZGL3o%2FomECnSVtnLLzI93fEjj9qLtk%2F8jJxyp%2FLKEcIgf0Yl%2BNJ%2BZ2LSu2ptRRI2%2BJohx4r7397qCTceSkZr5kgo2WbN9jielujKc4sqrvfhJ&X-Amz-Signature=10565f911c05a21df48ff520eb9b7c9fa073cd271fcfab3a7c036f1782173a6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I75I2VK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIDnNqTUprtvLa2jF%2FAQudenP%2FT4oruTq7a03cLKTmsW6AiB1vxSnWyRQflyAAn8%2F1JaRNwyn7jI22PxGeJGmKc804Sr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMZWR%2BW3VSWn3G%2FP1XKtwDU%2Fw2kDp%2FBPmVueYaFOrk495gBbRGG5lX12AuD889RUuiniRK8V%2FON6b5kUf9al1Hd5hzr0iJDM8u6wllXY%2Fkg%2FQuN4N2ocTtniNp0YjPKeA6b8EoF4HpQIn1odVlo0cO0sjiATNr3%2BjkXVoetA9XZ29Pcs0zl68pyxf0K3fAiW5NQ83vaIAGBY0l02YLVNZIVxU1EQ87KfixpxObKEWQFmpUQz2Q5S1hqzaIvFv70kSjuRBfXP%2FbPvpNX6kzccq%2BsgeKFWMva7FU%2FQmDmGEqGbna1OJvDi%2FLvoGnmUCl6Tv76HJrX1lJll7X0McSniY8lxJE7TaX3QSDD916qiU4Z6deG3z2JuoPLvXS9LBKUld%2FSp44stGt19aU2v3DLsJt6YD%2BUFu48zVkiHXKAozcKxAylQ8uldLWuzCVJnD3kCAXPpOCFyiyhSpUcvltvibxLKlk5cQ95PbPK9k3Q6BJStUYqMTH7RAXRxAsz3aIzMGCLBZ5x676h2usIEN%2FFGnEVpKqSpxwwZt%2FjMq52yDpx8dpT9f2idtBsukzUgsQkojY6PBj8HdbrtqDz%2FhuGRwQpVns2hqyY5Waj7eV8cvyPbYp9%2FYhTmIFbcBVmaol7AjoExI0DoklMK9WimIws9mEvQY6pgFowo3Vg8WW5kP%2F3HYcPWZ1KAcJXYKXrrQb4ReXAkwScDm0fNeYL%2BBKiQAEifkyWG9TDJYF%2FiYOJJ0FDMvJNc11a6MsXA9aw9ATWkuoiUHTDaJrRo%2FZGL3o%2FomECnSVtnLLzI93fEjj9qLtk%2F8jJxyp%2FLKEcIgf0Yl%2BNJ%2BZ2LSu2ptRRI2%2BJohx4r7397qCTceSkZr5kgo2WbN9jielujKc4sqrvfhJ&X-Amz-Signature=c910e3375dee579bfdd06bf923aeaf054f2ba10c25f2be55e138ba4dde148655&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I75I2VK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIDnNqTUprtvLa2jF%2FAQudenP%2FT4oruTq7a03cLKTmsW6AiB1vxSnWyRQflyAAn8%2F1JaRNwyn7jI22PxGeJGmKc804Sr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMZWR%2BW3VSWn3G%2FP1XKtwDU%2Fw2kDp%2FBPmVueYaFOrk495gBbRGG5lX12AuD889RUuiniRK8V%2FON6b5kUf9al1Hd5hzr0iJDM8u6wllXY%2Fkg%2FQuN4N2ocTtniNp0YjPKeA6b8EoF4HpQIn1odVlo0cO0sjiATNr3%2BjkXVoetA9XZ29Pcs0zl68pyxf0K3fAiW5NQ83vaIAGBY0l02YLVNZIVxU1EQ87KfixpxObKEWQFmpUQz2Q5S1hqzaIvFv70kSjuRBfXP%2FbPvpNX6kzccq%2BsgeKFWMva7FU%2FQmDmGEqGbna1OJvDi%2FLvoGnmUCl6Tv76HJrX1lJll7X0McSniY8lxJE7TaX3QSDD916qiU4Z6deG3z2JuoPLvXS9LBKUld%2FSp44stGt19aU2v3DLsJt6YD%2BUFu48zVkiHXKAozcKxAylQ8uldLWuzCVJnD3kCAXPpOCFyiyhSpUcvltvibxLKlk5cQ95PbPK9k3Q6BJStUYqMTH7RAXRxAsz3aIzMGCLBZ5x676h2usIEN%2FFGnEVpKqSpxwwZt%2FjMq52yDpx8dpT9f2idtBsukzUgsQkojY6PBj8HdbrtqDz%2FhuGRwQpVns2hqyY5Waj7eV8cvyPbYp9%2FYhTmIFbcBVmaol7AjoExI0DoklMK9WimIws9mEvQY6pgFowo3Vg8WW5kP%2F3HYcPWZ1KAcJXYKXrrQb4ReXAkwScDm0fNeYL%2BBKiQAEifkyWG9TDJYF%2FiYOJJ0FDMvJNc11a6MsXA9aw9ATWkuoiUHTDaJrRo%2FZGL3o%2FomECnSVtnLLzI93fEjj9qLtk%2F8jJxyp%2FLKEcIgf0Yl%2BNJ%2BZ2LSu2ptRRI2%2BJohx4r7397qCTceSkZr5kgo2WbN9jielujKc4sqrvfhJ&X-Amz-Signature=3e6975cc39db0879b0cc48ad1c0656f40e3f7080536f981ba9fff4d39fd62342&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LTZJVWE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIHWdTbKKIKc7ku9eM6GvZLoHW4aaMJDxbtH4xKwBprkqAiEA%2FVpHaFMSze9TWeUwmXrBuDlsmu2ZL%2BoAEhXT%2Bosi3RAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCvx3ECAfwZomauJbyrcA0KWZS0iQAqQ9Z%2F9XKgqSExTCOHIHNTp8AQcQTYXxXkOCGGanNy2SSP2reESk2%2FNoETklka5amTdCAKzX3uRwPfl5TrD9zt4NuFwDmneXTd6DXt1tsKUw%2F3IXFnUeNmrHeAOICa%2BpBchZf0UqmZ6Qfa%2BpX7n96%2FfLuVHxi9BNmoCxyCCF8Bgl%2FBOm9e9vJThcmuiSgJmoWPZaf6a6QdOG1cmwXUyQPmnDfolpZbmUrNhPN1DORBlhqP8BffvQqUv%2B9159LAvYjTTDiAi5qc5M1Y3HGaUAAGrFM2t8j%2B3DTIG%2FtZ1egh9%2FUZssV%2FkUo0iqxz9%2BsKErcryyMyYnRW9FNLXfXAEaVLnMl3NG149PeFaSk%2BwxmyVEp8s8P91GM%2FnEEeZcPXXX8pw3Fc7klJUlko0v3p6DSQ51q4xOmR%2Bcix9GnbSAourRoiUPMKgQxRYdYE2d7woHPZE957GTm9dMcFSNuFhSGyTODrIimearDsuo2bKabG21RGyU2bqjFbjRbx4ZKrXkJxvRY5ImBmNPcsu0ETs9W1GJWOCx5LvO81rRiXu8aaqDeEFoXiCOQKlQ0Ypk3HUljqPz6tF7X4KHiZrodVc6ePn5wy7WBVsUJ%2BXuWjrbnJngZlksLMXMP%2FZhL0GOqUB3B8tihKTF28gyIW%2Fns47a3kfuNTk9wT9zbaGhN3xAv20Wp1eB1lwiLyksEP3lbIqUcR017dMpawVxaTUJRF0tcTvgxUAIdsmsHOB5SCqk3V50JPVgo4mbuIJuZQUa5GWHtRZTIJejf%2Bci1l6MDjrvhDdN0KI4d4d00F7j5DunXXZhQzte9pgK%2FZaNixu9v7ZdYGpz6zvzJDYzho511%2FknRrOWRPL&X-Amz-Signature=249c2fca935f673dfae9e2b25fba96456271c3fda07a0c7d55531d44e5f8986f&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LTZJVWE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIHWdTbKKIKc7ku9eM6GvZLoHW4aaMJDxbtH4xKwBprkqAiEA%2FVpHaFMSze9TWeUwmXrBuDlsmu2ZL%2BoAEhXT%2Bosi3RAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCvx3ECAfwZomauJbyrcA0KWZS0iQAqQ9Z%2F9XKgqSExTCOHIHNTp8AQcQTYXxXkOCGGanNy2SSP2reESk2%2FNoETklka5amTdCAKzX3uRwPfl5TrD9zt4NuFwDmneXTd6DXt1tsKUw%2F3IXFnUeNmrHeAOICa%2BpBchZf0UqmZ6Qfa%2BpX7n96%2FfLuVHxi9BNmoCxyCCF8Bgl%2FBOm9e9vJThcmuiSgJmoWPZaf6a6QdOG1cmwXUyQPmnDfolpZbmUrNhPN1DORBlhqP8BffvQqUv%2B9159LAvYjTTDiAi5qc5M1Y3HGaUAAGrFM2t8j%2B3DTIG%2FtZ1egh9%2FUZssV%2FkUo0iqxz9%2BsKErcryyMyYnRW9FNLXfXAEaVLnMl3NG149PeFaSk%2BwxmyVEp8s8P91GM%2FnEEeZcPXXX8pw3Fc7klJUlko0v3p6DSQ51q4xOmR%2Bcix9GnbSAourRoiUPMKgQxRYdYE2d7woHPZE957GTm9dMcFSNuFhSGyTODrIimearDsuo2bKabG21RGyU2bqjFbjRbx4ZKrXkJxvRY5ImBmNPcsu0ETs9W1GJWOCx5LvO81rRiXu8aaqDeEFoXiCOQKlQ0Ypk3HUljqPz6tF7X4KHiZrodVc6ePn5wy7WBVsUJ%2BXuWjrbnJngZlksLMXMP%2FZhL0GOqUB3B8tihKTF28gyIW%2Fns47a3kfuNTk9wT9zbaGhN3xAv20Wp1eB1lwiLyksEP3lbIqUcR017dMpawVxaTUJRF0tcTvgxUAIdsmsHOB5SCqk3V50JPVgo4mbuIJuZQUa5GWHtRZTIJejf%2Bci1l6MDjrvhDdN0KI4d4d00F7j5DunXXZhQzte9pgK%2FZaNixu9v7ZdYGpz6zvzJDYzho511%2FknRrOWRPL&X-Amz-Signature=43e40bc42415e048b87b2c3fe8a5098a9731189296bc13d0a8c3f5ab94e15a5e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LTZJVWE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIHWdTbKKIKc7ku9eM6GvZLoHW4aaMJDxbtH4xKwBprkqAiEA%2FVpHaFMSze9TWeUwmXrBuDlsmu2ZL%2BoAEhXT%2Bosi3RAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCvx3ECAfwZomauJbyrcA0KWZS0iQAqQ9Z%2F9XKgqSExTCOHIHNTp8AQcQTYXxXkOCGGanNy2SSP2reESk2%2FNoETklka5amTdCAKzX3uRwPfl5TrD9zt4NuFwDmneXTd6DXt1tsKUw%2F3IXFnUeNmrHeAOICa%2BpBchZf0UqmZ6Qfa%2BpX7n96%2FfLuVHxi9BNmoCxyCCF8Bgl%2FBOm9e9vJThcmuiSgJmoWPZaf6a6QdOG1cmwXUyQPmnDfolpZbmUrNhPN1DORBlhqP8BffvQqUv%2B9159LAvYjTTDiAi5qc5M1Y3HGaUAAGrFM2t8j%2B3DTIG%2FtZ1egh9%2FUZssV%2FkUo0iqxz9%2BsKErcryyMyYnRW9FNLXfXAEaVLnMl3NG149PeFaSk%2BwxmyVEp8s8P91GM%2FnEEeZcPXXX8pw3Fc7klJUlko0v3p6DSQ51q4xOmR%2Bcix9GnbSAourRoiUPMKgQxRYdYE2d7woHPZE957GTm9dMcFSNuFhSGyTODrIimearDsuo2bKabG21RGyU2bqjFbjRbx4ZKrXkJxvRY5ImBmNPcsu0ETs9W1GJWOCx5LvO81rRiXu8aaqDeEFoXiCOQKlQ0Ypk3HUljqPz6tF7X4KHiZrodVc6ePn5wy7WBVsUJ%2BXuWjrbnJngZlksLMXMP%2FZhL0GOqUB3B8tihKTF28gyIW%2Fns47a3kfuNTk9wT9zbaGhN3xAv20Wp1eB1lwiLyksEP3lbIqUcR017dMpawVxaTUJRF0tcTvgxUAIdsmsHOB5SCqk3V50JPVgo4mbuIJuZQUa5GWHtRZTIJejf%2Bci1l6MDjrvhDdN0KI4d4d00F7j5DunXXZhQzte9pgK%2FZaNixu9v7ZdYGpz6zvzJDYzho511%2FknRrOWRPL&X-Amz-Signature=c276438513f48598c8b0042cb6c1dffa2b038b89420843d68221b59f7bbcaeb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

