

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=dd195318f3c1091dbde9675a80aadc17a7ca39b65cac10babe3239c7d5e16e5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=8f80737444be05b0766bf9c70b99c755efaca00b28b3ab4b78a63f0b600106c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=1d96bccd1f24a4349d689d0f1c4f129e3ad9d9cf077aca3229f42bf53cf3b06e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=54f8a893dbaab1f34d193724a9f8818acb053b75925d20f025fed6fa0107619b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=d131a141cbbb02472fd99623b3a51080d26e6192612b4678668feaa958cc4e66&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=89f668f3cf6fe144019bc3f1e2e110969e24c748b15e92b2239a168303a42164&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=e265a2596038849476181c8abd09e3fa6ced83c7230b1b7b13b8392e7d3412b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=ec368a9db88c4daad969b49b181d0d1d5571e03d772aded9acf579d1e79aa3e1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=4a65d129872f5966cbecc705c8408824abadab4c984576b78be1d2ef08f79694&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=8e8588b8bc9f5671d339ea364aa828f1f36cbd6ca5741d4b3f7326b21f403c12&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGL5NO5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWy%2BzXSjrX1btEkLOB0dYpZoU1lmK4%2BbSsz9MdYE2sOAIhANTbaJNzdzfxkFEF%2FIAx%2BsqYlJtHpfDXAHQd0WMZk53oKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVyR%2F%2B9fXPvF71k4gq3AN1lFVo%2FRwUSByTgZV4sc%2BY5g%2BTdh5Z4rvo%2F%2BKlvYCc5iKcbuPc7OpMfxBa6%2Fp1q5Zu1oLPWOEnjtbo0nRhGYRzCLWYDXiA9bZwSxGSKrOIyut9%2FtRAGItuUaPUn9xuS50NYJvMzToUZQCgc6ADe2yY9QLj28wjcHOnR%2BXU2HQTzAavOpm9Asbnr8RPC%2F8%2FWIeJoxySsN489IYNRL20uv7akWcYjcckzJkUfa1601orj02dW9YaBLNENoBEZlj7%2F3sBOPrf3hfn7Lvk7A5Xb4CzFgikqerbV1GclAIbhVfbT1waxNuE7OpCjfGA9K8f2FcBuLcVIZNCmhOpE%2Br7XilOm4NIRs6H0sN%2FjM97aEUx%2Fsv19pRXpa%2BDKlLIy9GNivGLGk2JfmgHW6SwBLl%2BvfcNLZqst1rf3rBe1N3kF0kP4VgbfpO16XZ6dr6fE2juty1BSWow57AjlAKS8pKFfLkKY%2B5aUE1buRUW5sQsgyRxYyXRYwkZ0%2BT%2Bw8y0kWJgi2b0BQhHmB4eWcdl6mkPpRnXdUVm2XR51lG68Ya5aqkaoyTo6T95qUus4tm4%2BXO1%2FYqD5tNixNPRQDbuFlUcpnhBTpUZS3p3iHko3pnvqx72%2BAjRbGkHGGC0IxxWuzDA6%2FO8BjqkAfGa5NP1J27ihXV6pqiqeRUofdeHdT2rWFJSKLBZ6jFeQ95cKsSQ7i%2FcijpX%2Brv9wdLJgd9cjeUkZzmV09Ey%2F1UTZPAJVBP2IKy%2BFzUFY8bq4jGu90UqRodZxufD%2FsEh0oYSLLSEm99JdSP8hvvhy9H9KV0L4h8Ei3xkYp5atuPwsAb6esoJQhraIib4iJswxn5Clyn1%2BNzOjKav4GJPyav0trTK&X-Amz-Signature=fa155225d0b064f6298f22a72622653a826d9232947056d8d3d4dc9d51226acb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AANG6BM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTfttBSw%2FCZgwrKFJ75KJcNr6qFYuKb6iZP4QX%2B%2FoB%2FgIgUCovv1tqvDLxg0m0oLkO7yWnROf4pgziNTdcRvm14vgqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBeSzPI9iuLEMvvTSrcA%2B0iu1JGqI3GyA4w7raP2%2BQnzhiQdMWh8vBrgMKk2qYBomzkjJqkubNxtq8eRzbuaBLA%2F8%2FudkJXx%2FnqyHepV6qjnAcmSj1HWTkvFC8FMeqr%2FLFCrfGlD1jZ2zEPtiAzhWBMqXv2n58G1npMjkCectA0iy%2BjgEPQzdXDrFHYfDQnVs6c8Nef0l7I%2F39IX9cu9d2vhfcR4zekMbR0FuluyuRjAlPfIE7S0scw7xWUN7zPnSawnb0xTwkW3CW0fifSmQktzUDwBL1vWiNNS5PgV9F4z%2F1KzkKWe8TilsYiheL4pwhmzFn2bDuGjI0q6DGv%2FZCzQhSP0cm7nhzISiTBTnpLhMJXsu3S9P5HbX9d7pJYC35fJFTTHOgMoQFkybD4N15FPESFtt490D2TGXyNyMuQHIz%2FaPpFxxqpc%2BwMKFkWsfrZuE04B1w0IbC7gC3Y6JWRqqbNY54lmQvN2rYKU0SyPNCy6rZyGitJgo%2F9QNnFXoEcnKu30YFlEvURlmMnsQMmvVvrjL8b6OsrAVF5iSKkPoILv9JcDkydcNKuQhal%2FkLstCj5lVGmEmUyGDJmaEtHXh%2BXUv2QarK9LcQvNikls4XuSQ6Cp9X68BV3r3kn5Mzv6%2BFHqRLWigx2MKCI9LwGOqUBxtdwOLQcmWMqay2xhBb0aUXeX0c8h64fMVehtY0JUy2Psv5HSZ8RleKdXIja6pLhHQ7D2buNSUN59tH3fhzTkj5yynkcv8PqQdquutec%2FWwGqC1REFnBaXYmcg9MKhq96Y8uXsCZEERXnGWq9OQoz37ZQ4pqYC53gqmCNUKzdqb97e7roo7iVNzbYzUlXPsDOexd7CHNTpeOdxilH%2FJPVyvoiU2s&X-Amz-Signature=85b25e678fbb603fd945cee8a1e92e8d4ef6d4eebfa61abfd15ee135ec558b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AANG6BM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTfttBSw%2FCZgwrKFJ75KJcNr6qFYuKb6iZP4QX%2B%2FoB%2FgIgUCovv1tqvDLxg0m0oLkO7yWnROf4pgziNTdcRvm14vgqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBeSzPI9iuLEMvvTSrcA%2B0iu1JGqI3GyA4w7raP2%2BQnzhiQdMWh8vBrgMKk2qYBomzkjJqkubNxtq8eRzbuaBLA%2F8%2FudkJXx%2FnqyHepV6qjnAcmSj1HWTkvFC8FMeqr%2FLFCrfGlD1jZ2zEPtiAzhWBMqXv2n58G1npMjkCectA0iy%2BjgEPQzdXDrFHYfDQnVs6c8Nef0l7I%2F39IX9cu9d2vhfcR4zekMbR0FuluyuRjAlPfIE7S0scw7xWUN7zPnSawnb0xTwkW3CW0fifSmQktzUDwBL1vWiNNS5PgV9F4z%2F1KzkKWe8TilsYiheL4pwhmzFn2bDuGjI0q6DGv%2FZCzQhSP0cm7nhzISiTBTnpLhMJXsu3S9P5HbX9d7pJYC35fJFTTHOgMoQFkybD4N15FPESFtt490D2TGXyNyMuQHIz%2FaPpFxxqpc%2BwMKFkWsfrZuE04B1w0IbC7gC3Y6JWRqqbNY54lmQvN2rYKU0SyPNCy6rZyGitJgo%2F9QNnFXoEcnKu30YFlEvURlmMnsQMmvVvrjL8b6OsrAVF5iSKkPoILv9JcDkydcNKuQhal%2FkLstCj5lVGmEmUyGDJmaEtHXh%2BXUv2QarK9LcQvNikls4XuSQ6Cp9X68BV3r3kn5Mzv6%2BFHqRLWigx2MKCI9LwGOqUBxtdwOLQcmWMqay2xhBb0aUXeX0c8h64fMVehtY0JUy2Psv5HSZ8RleKdXIja6pLhHQ7D2buNSUN59tH3fhzTkj5yynkcv8PqQdquutec%2FWwGqC1REFnBaXYmcg9MKhq96Y8uXsCZEERXnGWq9OQoz37ZQ4pqYC53gqmCNUKzdqb97e7roo7iVNzbYzUlXPsDOexd7CHNTpeOdxilH%2FJPVyvoiU2s&X-Amz-Signature=757a4853debf6c888388e570643de6bcf3c82da084d45acc2fdbdada08ac89c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AANG6BM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTfttBSw%2FCZgwrKFJ75KJcNr6qFYuKb6iZP4QX%2B%2FoB%2FgIgUCovv1tqvDLxg0m0oLkO7yWnROf4pgziNTdcRvm14vgqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBeSzPI9iuLEMvvTSrcA%2B0iu1JGqI3GyA4w7raP2%2BQnzhiQdMWh8vBrgMKk2qYBomzkjJqkubNxtq8eRzbuaBLA%2F8%2FudkJXx%2FnqyHepV6qjnAcmSj1HWTkvFC8FMeqr%2FLFCrfGlD1jZ2zEPtiAzhWBMqXv2n58G1npMjkCectA0iy%2BjgEPQzdXDrFHYfDQnVs6c8Nef0l7I%2F39IX9cu9d2vhfcR4zekMbR0FuluyuRjAlPfIE7S0scw7xWUN7zPnSawnb0xTwkW3CW0fifSmQktzUDwBL1vWiNNS5PgV9F4z%2F1KzkKWe8TilsYiheL4pwhmzFn2bDuGjI0q6DGv%2FZCzQhSP0cm7nhzISiTBTnpLhMJXsu3S9P5HbX9d7pJYC35fJFTTHOgMoQFkybD4N15FPESFtt490D2TGXyNyMuQHIz%2FaPpFxxqpc%2BwMKFkWsfrZuE04B1w0IbC7gC3Y6JWRqqbNY54lmQvN2rYKU0SyPNCy6rZyGitJgo%2F9QNnFXoEcnKu30YFlEvURlmMnsQMmvVvrjL8b6OsrAVF5iSKkPoILv9JcDkydcNKuQhal%2FkLstCj5lVGmEmUyGDJmaEtHXh%2BXUv2QarK9LcQvNikls4XuSQ6Cp9X68BV3r3kn5Mzv6%2BFHqRLWigx2MKCI9LwGOqUBxtdwOLQcmWMqay2xhBb0aUXeX0c8h64fMVehtY0JUy2Psv5HSZ8RleKdXIja6pLhHQ7D2buNSUN59tH3fhzTkj5yynkcv8PqQdquutec%2FWwGqC1REFnBaXYmcg9MKhq96Y8uXsCZEERXnGWq9OQoz37ZQ4pqYC53gqmCNUKzdqb97e7roo7iVNzbYzUlXPsDOexd7CHNTpeOdxilH%2FJPVyvoiU2s&X-Amz-Signature=bc226a34ecc6197fcaeb5c237d25440aaa2187bd20fca6b8c8e9f2684f6f4e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AANG6BM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTfttBSw%2FCZgwrKFJ75KJcNr6qFYuKb6iZP4QX%2B%2FoB%2FgIgUCovv1tqvDLxg0m0oLkO7yWnROf4pgziNTdcRvm14vgqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBeSzPI9iuLEMvvTSrcA%2B0iu1JGqI3GyA4w7raP2%2BQnzhiQdMWh8vBrgMKk2qYBomzkjJqkubNxtq8eRzbuaBLA%2F8%2FudkJXx%2FnqyHepV6qjnAcmSj1HWTkvFC8FMeqr%2FLFCrfGlD1jZ2zEPtiAzhWBMqXv2n58G1npMjkCectA0iy%2BjgEPQzdXDrFHYfDQnVs6c8Nef0l7I%2F39IX9cu9d2vhfcR4zekMbR0FuluyuRjAlPfIE7S0scw7xWUN7zPnSawnb0xTwkW3CW0fifSmQktzUDwBL1vWiNNS5PgV9F4z%2F1KzkKWe8TilsYiheL4pwhmzFn2bDuGjI0q6DGv%2FZCzQhSP0cm7nhzISiTBTnpLhMJXsu3S9P5HbX9d7pJYC35fJFTTHOgMoQFkybD4N15FPESFtt490D2TGXyNyMuQHIz%2FaPpFxxqpc%2BwMKFkWsfrZuE04B1w0IbC7gC3Y6JWRqqbNY54lmQvN2rYKU0SyPNCy6rZyGitJgo%2F9QNnFXoEcnKu30YFlEvURlmMnsQMmvVvrjL8b6OsrAVF5iSKkPoILv9JcDkydcNKuQhal%2FkLstCj5lVGmEmUyGDJmaEtHXh%2BXUv2QarK9LcQvNikls4XuSQ6Cp9X68BV3r3kn5Mzv6%2BFHqRLWigx2MKCI9LwGOqUBxtdwOLQcmWMqay2xhBb0aUXeX0c8h64fMVehtY0JUy2Psv5HSZ8RleKdXIja6pLhHQ7D2buNSUN59tH3fhzTkj5yynkcv8PqQdquutec%2FWwGqC1REFnBaXYmcg9MKhq96Y8uXsCZEERXnGWq9OQoz37ZQ4pqYC53gqmCNUKzdqb97e7roo7iVNzbYzUlXPsDOexd7CHNTpeOdxilH%2FJPVyvoiU2s&X-Amz-Signature=8805349a867743f1963d4756863447d2693228b1ef2a7a8913cacc7f27c90b26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NR3JLHU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1weGf05UsGQSOLHbZLP6doUeK5iqG9%2Bhn2ARG0ATMhAiAQVGNB74TnDAo%2BRtAycdK4AKesKL7oOC4HaxPFd1Ym1iqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqA8069AS%2Bk%2B5oBERKtwDomAatfjqB7tTx%2FRqnBSZlPOOvWY3EdRDCYvIqkGnzMIF%2FpF85N4NjMe4%2FeANq7sBvM4%2Bnt%2FEKrB9KHliX%2F6a1759MXDv1B0aZCc2uPDaQVOdEn69qGiznBMECjl85kxyPafmlM9tl%2BvjixcuhNqhMKGSNL5Xg8lq3d5Jm%2FzN2e4nWy9fHOgzIXQBffUYOALXW32B2N6uJQJNQahTpC3yLDHsnE5N2QDyHaRmT8QuD17LKubYgpibCZ1yc8OaYwB6rVkTRUsr3HYdPOGCz214Hi%2Fwv2zeTPp7XTqUIbv%2FJ5ahM7BKrT4gBj7YoSCPPa7IAD8Zjk%2Fj3G8b2T%2F6LxyvpZgQzgBlsCCM7Ip1Hm6DGNnLZrHqid7iReUtcfAGK5zcVPg1L938URcSnrgSLb7M7x2gp37bDIF%2FAoyWDufiT8hBbUGPWdVrTpdCAiarGZ%2B8sEbd%2FZW24HWm1Fcqupwo7072W6NtfINd1ENjHHvehC0ZjsOSrw5c4tkdt8tyrCAiKKESWcbwAbCpNz3TshUScYmHmuscJpsLLMfOjTw9ZuC0rKI6hXONw5TqYka1k9e7b2hj06QbCVodm3owxDZUIdtlfkiM6AHAQmHnegUxrqVIPDN0GhYskGKFuFgw34f0vAY6pgG48g1j2Mn%2Fe1x0OuA8eOdKM8tAXkRKcKvR9PJRX244zkjfGoQAt868TdttC4Xxd0FpAWeOPu37Hmm22fv6PWfds6m%2B4a0ejQna7G5SL14t95BQC3rFjY98VzRFGMi9%2Bm98913tY2AKbS7aMVNEHGwKItfsiRpI4jiGTuSb23W5cIf6Wb5iVxXTfXLP8Q3LAL4LnAkUJMwMkGla9HVE1XOKaJape8rZ&X-Amz-Signature=d609750f7ea1e9a3e0336ff8d04d3775be8884a4b8553024fe4a14a94d208099&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NR3JLHU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1weGf05UsGQSOLHbZLP6doUeK5iqG9%2Bhn2ARG0ATMhAiAQVGNB74TnDAo%2BRtAycdK4AKesKL7oOC4HaxPFd1Ym1iqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqA8069AS%2Bk%2B5oBERKtwDomAatfjqB7tTx%2FRqnBSZlPOOvWY3EdRDCYvIqkGnzMIF%2FpF85N4NjMe4%2FeANq7sBvM4%2Bnt%2FEKrB9KHliX%2F6a1759MXDv1B0aZCc2uPDaQVOdEn69qGiznBMECjl85kxyPafmlM9tl%2BvjixcuhNqhMKGSNL5Xg8lq3d5Jm%2FzN2e4nWy9fHOgzIXQBffUYOALXW32B2N6uJQJNQahTpC3yLDHsnE5N2QDyHaRmT8QuD17LKubYgpibCZ1yc8OaYwB6rVkTRUsr3HYdPOGCz214Hi%2Fwv2zeTPp7XTqUIbv%2FJ5ahM7BKrT4gBj7YoSCPPa7IAD8Zjk%2Fj3G8b2T%2F6LxyvpZgQzgBlsCCM7Ip1Hm6DGNnLZrHqid7iReUtcfAGK5zcVPg1L938URcSnrgSLb7M7x2gp37bDIF%2FAoyWDufiT8hBbUGPWdVrTpdCAiarGZ%2B8sEbd%2FZW24HWm1Fcqupwo7072W6NtfINd1ENjHHvehC0ZjsOSrw5c4tkdt8tyrCAiKKESWcbwAbCpNz3TshUScYmHmuscJpsLLMfOjTw9ZuC0rKI6hXONw5TqYka1k9e7b2hj06QbCVodm3owxDZUIdtlfkiM6AHAQmHnegUxrqVIPDN0GhYskGKFuFgw34f0vAY6pgG48g1j2Mn%2Fe1x0OuA8eOdKM8tAXkRKcKvR9PJRX244zkjfGoQAt868TdttC4Xxd0FpAWeOPu37Hmm22fv6PWfds6m%2B4a0ejQna7G5SL14t95BQC3rFjY98VzRFGMi9%2Bm98913tY2AKbS7aMVNEHGwKItfsiRpI4jiGTuSb23W5cIf6Wb5iVxXTfXLP8Q3LAL4LnAkUJMwMkGla9HVE1XOKaJape8rZ&X-Amz-Signature=ef9e1aa04da2722980001af974c099df74cce429b4e145cd6ce027fb06bf766a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NR3JLHU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1weGf05UsGQSOLHbZLP6doUeK5iqG9%2Bhn2ARG0ATMhAiAQVGNB74TnDAo%2BRtAycdK4AKesKL7oOC4HaxPFd1Ym1iqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqA8069AS%2Bk%2B5oBERKtwDomAatfjqB7tTx%2FRqnBSZlPOOvWY3EdRDCYvIqkGnzMIF%2FpF85N4NjMe4%2FeANq7sBvM4%2Bnt%2FEKrB9KHliX%2F6a1759MXDv1B0aZCc2uPDaQVOdEn69qGiznBMECjl85kxyPafmlM9tl%2BvjixcuhNqhMKGSNL5Xg8lq3d5Jm%2FzN2e4nWy9fHOgzIXQBffUYOALXW32B2N6uJQJNQahTpC3yLDHsnE5N2QDyHaRmT8QuD17LKubYgpibCZ1yc8OaYwB6rVkTRUsr3HYdPOGCz214Hi%2Fwv2zeTPp7XTqUIbv%2FJ5ahM7BKrT4gBj7YoSCPPa7IAD8Zjk%2Fj3G8b2T%2F6LxyvpZgQzgBlsCCM7Ip1Hm6DGNnLZrHqid7iReUtcfAGK5zcVPg1L938URcSnrgSLb7M7x2gp37bDIF%2FAoyWDufiT8hBbUGPWdVrTpdCAiarGZ%2B8sEbd%2FZW24HWm1Fcqupwo7072W6NtfINd1ENjHHvehC0ZjsOSrw5c4tkdt8tyrCAiKKESWcbwAbCpNz3TshUScYmHmuscJpsLLMfOjTw9ZuC0rKI6hXONw5TqYka1k9e7b2hj06QbCVodm3owxDZUIdtlfkiM6AHAQmHnegUxrqVIPDN0GhYskGKFuFgw34f0vAY6pgG48g1j2Mn%2Fe1x0OuA8eOdKM8tAXkRKcKvR9PJRX244zkjfGoQAt868TdttC4Xxd0FpAWeOPu37Hmm22fv6PWfds6m%2B4a0ejQna7G5SL14t95BQC3rFjY98VzRFGMi9%2Bm98913tY2AKbS7aMVNEHGwKItfsiRpI4jiGTuSb23W5cIf6Wb5iVxXTfXLP8Q3LAL4LnAkUJMwMkGla9HVE1XOKaJape8rZ&X-Amz-Signature=9775d88a21a0ac4cf634c75d9ed3971be65506023b5f1025677771dfff4fb2ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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

