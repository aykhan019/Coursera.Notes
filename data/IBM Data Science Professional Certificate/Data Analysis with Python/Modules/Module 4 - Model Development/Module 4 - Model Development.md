

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=1d412be195c9d10ad1fc1db19cefb69d84df62ddaf1d51e5e081ad9bf4f74658&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=a5c0ee0210da9d1175b7ede4c47e2ac143c34d49b5c69296527e15979fb8f087&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=3b49f05a106e502fa564140cefd4d66928e0d832e76a1ebb5cd8479ec1a7aebb&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=23d1a8847898b720ac9643edcc96745155148ec306ad51695cdb1dc0204bc374&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=5e9ec919935be608bee1ca2fad6c89ebf921c711fc86d65bcf369ed99fdc941e&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=85a65ce04a7185019883e5d6cbc1f2881495b856c77e896fd00c2f4c4c945000&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=14119a80028072013b6555f4cb4d2d091146160dd9b5c4c0bba0419072757b41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=079fb442d0b1bd0565f90d86fa3aca0685a3883e9f23e240f16a7d63caeb0b09&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=bf1b9c9a4567d103e132eb76740cfb0a3c9bcbcd778410735a9eae30df7195a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=4eb533386ae81bb6440e83e65071f64fb2b2e2f8c58e4413c896cb6a58cfdbdb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEHF35E7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCsFWErBGsmODJcRFu2rzpyZoQ31pvJ6Y8%2BI%2FwvkTTzMQIhAIIw9%2FbeJO8N8%2BucnSr%2BtkM9dkU%2FjYSRAKthLfh%2B1YAUKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0J3OuBSNIVqKoJVQq3AO9jzlB3gQey9kXcHoBhw7JfHYNTAV%2FBYw%2F8sS7HF2KnA10gzY6rxJ9zdW3hKCXOgBQ6CgdkKWmIFoGoQFrCvBkC8Gp42%2F21cimd%2B2RhiP4JIBKqbd%2FwEk7j%2BK5GqqlUnO%2BCbg%2BsDnDPxcgr%2BcjU5ckHb61pEIvcNrYTSMWyRyG9BrFEw6nVkcVd9UwyUYEqHBrPmfK6%2B3o7sLqfEYEHjTNR6cxXzI1dTPyaB5%2FiJEFRFxOtGjJThHtcXYxW8BNb7iLJAy3Taem6swyFKyT8HllSlHRWajxcvZpGZR76En76pUSc%2Fsx9jjVSb%2FMcdbQX%2BnG8VlBBvuuNMO3tX0vTOr%2FdrpAZXTYhMd5WJCM3QnJm3arT7aJV6%2FxoAaGoiDVISlFQif8htDqPZ6USWzsecFJIe5%2FPdrkVKX0j%2FqCw1EdNGs6%2Fq8Fu3QFUslSvYOCKcm%2FD0aqEaaOZ1VASDqL96UO2VQWxcsVgOH%2F88MsYDiMA4ADoucEL8J1%2BVXDCoEqvbfoqTrqonZ%2FcR1CNBkUwXU4%2F1TgeAAgl3WWczEdl3%2BPw%2BSTKUiP2vUKkaN5oZmvU4QMoDQ%2F%2Ff57ibDJp3LdSqzCRhFS%2Bfd5o1O0efYGQ%2FJYNBkBTEEevaPvRShlbjDV65G9BjqkAeQJ%2BHAj19%2BnDqX1X%2F91%2BQxVh%2Bh3VqZ3NdbAs8uiUAEvHSsDjlhJ5r1m9pTzQXJMIX1nll693x4KGUdInJAUH9cKaXGP3akzIwtiizWJ%2FgMuZAFXxFLZQd5aPdTcKhiuMbZWHbKC%2Bbh3C79MeariTOmmQ1HoPVQjERYfxvQJTaXuJ8xiUD0uXe0mSCCBfhsCBmuRXTRIACbbEZ3BcmX8lbVG3pTR&X-Amz-Signature=30d4b1f47fc06271926d4a3bf0f50b312c08ab06f4bdb12c93c84a6ef8748baf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RATFABKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiGSIT3RssjjL7m3%2BHHkYY8qWBW4wImvXQf3UjES97GwIge86T%2FKD%2Fdv%2BBNUtttp2A%2FwOXCLFZkC0LsenL8IxxsuUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDEXs4H0uTnuPJDz7xyrcA86hRd88cc87THANt9sBOaCOyK5GX9molLu2%2B7I77f1YZDWkkbYGh6fDE2aYUi2LNcApRlPrE1yz8WEebgrF0Ujl%2FultJ4EKOmWn2hUlqmFb7Lk4R3%2FQPC9i8c1h8sdgjht80eFYIa4so8VWB1D1JvLbT0NxOxvE%2BcokkDQEIROB2WxRHZu%2BJIvJPTljYaqiP23U%2FAXs%2B3L16NYovfVou04p9jSha%2BTvdacnQf0yj9BCvq0If5dBcYK%2BGS1G1U%2Fr%2B%2Bhv8Ug80HL0HsEZV5AjsuyxjfAgzcloTDM1ZCoDeicZGfiQk5Rsl3xh6zMU%2BcByeaqwccw9%2F8HHA84rmRuWIRIbJvzq3kX1Ci8ScvEUzTirenTmog6t8czg1jS4IyrveXod4BopkY5X%2FQCgUwx3leF4iiQFQ%2Fg76nBj4VKs7RnIj71mgJuzTtvroPCZZ4VXckam2PervQlUbjCyPg5VIUGklaNG6HGnXRaVfGlIc29q4SjlVxK%2FRFhCdpn0zmakLQGn5iswhku2jogF3Xa0pdtr4CnFuCmxtu%2BFuN8oq8prLHXXUsCbu2wmvTo0fRYhM11mng606jbaIm8Km45K3PKV%2FyUYfi4y4Rb%2BCwJcTg9AD%2Fwdu56L8KTXeuziMJPskb0GOqUBrW5Ny%2BG8dRRS0HI2dX3PV056mMLhsFoC%2Fwr%2BtJCk%2BCXu6Z70gRe42EOgH7LRlWAxyzd7Pyibb35lQBLuvUNGq1nXlYMHuOFoe7G0vGXz4xTFJ0mvf29ng3vtzEMSTI8l2aEMzYTUbJn1L8XN9eZBGV0EaC4%2FOW5vJ5i%2F1KhtXElxP0AKsN2H8IVCGfFJDWr8UWGZBaMeyc8w7wIptTx2TqDSrTii&X-Amz-Signature=75b365bd8183deec36e7e0ebc92e774055dff2c7210d4477feecd7d3ee12cdbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RATFABKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiGSIT3RssjjL7m3%2BHHkYY8qWBW4wImvXQf3UjES97GwIge86T%2FKD%2Fdv%2BBNUtttp2A%2FwOXCLFZkC0LsenL8IxxsuUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDEXs4H0uTnuPJDz7xyrcA86hRd88cc87THANt9sBOaCOyK5GX9molLu2%2B7I77f1YZDWkkbYGh6fDE2aYUi2LNcApRlPrE1yz8WEebgrF0Ujl%2FultJ4EKOmWn2hUlqmFb7Lk4R3%2FQPC9i8c1h8sdgjht80eFYIa4so8VWB1D1JvLbT0NxOxvE%2BcokkDQEIROB2WxRHZu%2BJIvJPTljYaqiP23U%2FAXs%2B3L16NYovfVou04p9jSha%2BTvdacnQf0yj9BCvq0If5dBcYK%2BGS1G1U%2Fr%2B%2Bhv8Ug80HL0HsEZV5AjsuyxjfAgzcloTDM1ZCoDeicZGfiQk5Rsl3xh6zMU%2BcByeaqwccw9%2F8HHA84rmRuWIRIbJvzq3kX1Ci8ScvEUzTirenTmog6t8czg1jS4IyrveXod4BopkY5X%2FQCgUwx3leF4iiQFQ%2Fg76nBj4VKs7RnIj71mgJuzTtvroPCZZ4VXckam2PervQlUbjCyPg5VIUGklaNG6HGnXRaVfGlIc29q4SjlVxK%2FRFhCdpn0zmakLQGn5iswhku2jogF3Xa0pdtr4CnFuCmxtu%2BFuN8oq8prLHXXUsCbu2wmvTo0fRYhM11mng606jbaIm8Km45K3PKV%2FyUYfi4y4Rb%2BCwJcTg9AD%2Fwdu56L8KTXeuziMJPskb0GOqUBrW5Ny%2BG8dRRS0HI2dX3PV056mMLhsFoC%2Fwr%2BtJCk%2BCXu6Z70gRe42EOgH7LRlWAxyzd7Pyibb35lQBLuvUNGq1nXlYMHuOFoe7G0vGXz4xTFJ0mvf29ng3vtzEMSTI8l2aEMzYTUbJn1L8XN9eZBGV0EaC4%2FOW5vJ5i%2F1KhtXElxP0AKsN2H8IVCGfFJDWr8UWGZBaMeyc8w7wIptTx2TqDSrTii&X-Amz-Signature=9062fb054aba087087d89ff4ce7e1d60dd8de547003893bf3bc35c5a3ff321d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RATFABKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiGSIT3RssjjL7m3%2BHHkYY8qWBW4wImvXQf3UjES97GwIge86T%2FKD%2Fdv%2BBNUtttp2A%2FwOXCLFZkC0LsenL8IxxsuUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDEXs4H0uTnuPJDz7xyrcA86hRd88cc87THANt9sBOaCOyK5GX9molLu2%2B7I77f1YZDWkkbYGh6fDE2aYUi2LNcApRlPrE1yz8WEebgrF0Ujl%2FultJ4EKOmWn2hUlqmFb7Lk4R3%2FQPC9i8c1h8sdgjht80eFYIa4so8VWB1D1JvLbT0NxOxvE%2BcokkDQEIROB2WxRHZu%2BJIvJPTljYaqiP23U%2FAXs%2B3L16NYovfVou04p9jSha%2BTvdacnQf0yj9BCvq0If5dBcYK%2BGS1G1U%2Fr%2B%2Bhv8Ug80HL0HsEZV5AjsuyxjfAgzcloTDM1ZCoDeicZGfiQk5Rsl3xh6zMU%2BcByeaqwccw9%2F8HHA84rmRuWIRIbJvzq3kX1Ci8ScvEUzTirenTmog6t8czg1jS4IyrveXod4BopkY5X%2FQCgUwx3leF4iiQFQ%2Fg76nBj4VKs7RnIj71mgJuzTtvroPCZZ4VXckam2PervQlUbjCyPg5VIUGklaNG6HGnXRaVfGlIc29q4SjlVxK%2FRFhCdpn0zmakLQGn5iswhku2jogF3Xa0pdtr4CnFuCmxtu%2BFuN8oq8prLHXXUsCbu2wmvTo0fRYhM11mng606jbaIm8Km45K3PKV%2FyUYfi4y4Rb%2BCwJcTg9AD%2Fwdu56L8KTXeuziMJPskb0GOqUBrW5Ny%2BG8dRRS0HI2dX3PV056mMLhsFoC%2Fwr%2BtJCk%2BCXu6Z70gRe42EOgH7LRlWAxyzd7Pyibb35lQBLuvUNGq1nXlYMHuOFoe7G0vGXz4xTFJ0mvf29ng3vtzEMSTI8l2aEMzYTUbJn1L8XN9eZBGV0EaC4%2FOW5vJ5i%2F1KhtXElxP0AKsN2H8IVCGfFJDWr8UWGZBaMeyc8w7wIptTx2TqDSrTii&X-Amz-Signature=d359f086d76e260032e07e9082ef1851bd124ebbf10e75278e888fa226b462d4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RATFABKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiGSIT3RssjjL7m3%2BHHkYY8qWBW4wImvXQf3UjES97GwIge86T%2FKD%2Fdv%2BBNUtttp2A%2FwOXCLFZkC0LsenL8IxxsuUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDEXs4H0uTnuPJDz7xyrcA86hRd88cc87THANt9sBOaCOyK5GX9molLu2%2B7I77f1YZDWkkbYGh6fDE2aYUi2LNcApRlPrE1yz8WEebgrF0Ujl%2FultJ4EKOmWn2hUlqmFb7Lk4R3%2FQPC9i8c1h8sdgjht80eFYIa4so8VWB1D1JvLbT0NxOxvE%2BcokkDQEIROB2WxRHZu%2BJIvJPTljYaqiP23U%2FAXs%2B3L16NYovfVou04p9jSha%2BTvdacnQf0yj9BCvq0If5dBcYK%2BGS1G1U%2Fr%2B%2Bhv8Ug80HL0HsEZV5AjsuyxjfAgzcloTDM1ZCoDeicZGfiQk5Rsl3xh6zMU%2BcByeaqwccw9%2F8HHA84rmRuWIRIbJvzq3kX1Ci8ScvEUzTirenTmog6t8czg1jS4IyrveXod4BopkY5X%2FQCgUwx3leF4iiQFQ%2Fg76nBj4VKs7RnIj71mgJuzTtvroPCZZ4VXckam2PervQlUbjCyPg5VIUGklaNG6HGnXRaVfGlIc29q4SjlVxK%2FRFhCdpn0zmakLQGn5iswhku2jogF3Xa0pdtr4CnFuCmxtu%2BFuN8oq8prLHXXUsCbu2wmvTo0fRYhM11mng606jbaIm8Km45K3PKV%2FyUYfi4y4Rb%2BCwJcTg9AD%2Fwdu56L8KTXeuziMJPskb0GOqUBrW5Ny%2BG8dRRS0HI2dX3PV056mMLhsFoC%2Fwr%2BtJCk%2BCXu6Z70gRe42EOgH7LRlWAxyzd7Pyibb35lQBLuvUNGq1nXlYMHuOFoe7G0vGXz4xTFJ0mvf29ng3vtzEMSTI8l2aEMzYTUbJn1L8XN9eZBGV0EaC4%2FOW5vJ5i%2F1KhtXElxP0AKsN2H8IVCGfFJDWr8UWGZBaMeyc8w7wIptTx2TqDSrTii&X-Amz-Signature=538bc80018a2ed64f9338a73f4dde3346d01df11da9ee1c4500e0fa9c18acc29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LVWECBI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCjLRAMtAp%2Fp%2BxnmemvMjOC15kMbA0V5OeGEC4I9XLkJQIhALJYufWut%2F7fE6DvhFZleDJZUjy%2FgluhZWqroXSzrvbsKv8DCFoQABoMNjM3NDIzMTgzODA1IgwDPSpfk8Z1NGE47Ksq3APhEQ0HN6ggG%2FliJS1erKn3chFSQ6e22zbWMWhegSgcdHHcQvq1a%2Fy84L7DD%2FPR3vYCgcA56g9e5ntAV647igHZmMdycnhvjqkF3Dzqdjf3syI3MjW%2FR0EaaRWRd231psKI%2BP%2FvhaUHTIxVxExEHpDCkLkc1sGEL7s8iURsQOIAE8ZmOYAyBXjegswIZSX8gdfpBDGPGmE%2B0h2Vwa0z3SKKfP5WA6ExAEozkh2CLHnyvPgzjJdDLkyMx%2FV2zwJ3JFPkZ66DPj3aDMACrCutd6gtQYT5iam5yUGzolD8em0T2AyEmJfFHhPD4MitvXBcJ4E%2B3QZ2%2Ftg5%2BX54u1M%2Ff6A2e0u3O1G72fXun%2FngJ4nXVMEkVYCkviTFWQ%2FPro6KovMPAoi9h9JAY%2BiJgNfa8SMWqVdq8l5d0K9%2Fu7clcTSH6naDWi5EaKqjl4dMgGrtNc33U4mVyZ8yLESMyZG6tlybiK%2BKB8FyF322d%2FDIwnHIPCr2JVA98OYXqZuNtWQA8NBtgMDOZnD9V2MwNhHMQfIf%2BZk0s0PrxGtnr5ujJlEu5Vqg9YkO4sWnlLNPtcuGYaYAfGnjwMeNKxUyJZ79hLCawNn2mnAq7SVrLdbs2lWZ%2FQd55pySOodjUL6hCTCr7JG9BjqkAflgpF5VraP6uAnVj3yiJIZ5mH31%2Bt0C9ex9GPbVWGl%2FVQ%2FQtX31lPY33beSvXeecghw18LbEPztAB%2B3N9GQIUbZoGuQtjWDK4jPOiVcM5NfXX5tsWZ0WToDCQy3tVig5t5UA6%2B8VExVnweV2V1oH8Ah7ciy56TeeI2lht9mbq4MlBi9FhzDkDtMB33BFZm3ZkUx00LBdcyccR7Qysd5U3Ub2e0b&X-Amz-Signature=812075faa8b002dce360781c813c4d1176c21418652206634a090f5c2b4f48aa&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LVWECBI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCjLRAMtAp%2Fp%2BxnmemvMjOC15kMbA0V5OeGEC4I9XLkJQIhALJYufWut%2F7fE6DvhFZleDJZUjy%2FgluhZWqroXSzrvbsKv8DCFoQABoMNjM3NDIzMTgzODA1IgwDPSpfk8Z1NGE47Ksq3APhEQ0HN6ggG%2FliJS1erKn3chFSQ6e22zbWMWhegSgcdHHcQvq1a%2Fy84L7DD%2FPR3vYCgcA56g9e5ntAV647igHZmMdycnhvjqkF3Dzqdjf3syI3MjW%2FR0EaaRWRd231psKI%2BP%2FvhaUHTIxVxExEHpDCkLkc1sGEL7s8iURsQOIAE8ZmOYAyBXjegswIZSX8gdfpBDGPGmE%2B0h2Vwa0z3SKKfP5WA6ExAEozkh2CLHnyvPgzjJdDLkyMx%2FV2zwJ3JFPkZ66DPj3aDMACrCutd6gtQYT5iam5yUGzolD8em0T2AyEmJfFHhPD4MitvXBcJ4E%2B3QZ2%2Ftg5%2BX54u1M%2Ff6A2e0u3O1G72fXun%2FngJ4nXVMEkVYCkviTFWQ%2FPro6KovMPAoi9h9JAY%2BiJgNfa8SMWqVdq8l5d0K9%2Fu7clcTSH6naDWi5EaKqjl4dMgGrtNc33U4mVyZ8yLESMyZG6tlybiK%2BKB8FyF322d%2FDIwnHIPCr2JVA98OYXqZuNtWQA8NBtgMDOZnD9V2MwNhHMQfIf%2BZk0s0PrxGtnr5ujJlEu5Vqg9YkO4sWnlLNPtcuGYaYAfGnjwMeNKxUyJZ79hLCawNn2mnAq7SVrLdbs2lWZ%2FQd55pySOodjUL6hCTCr7JG9BjqkAflgpF5VraP6uAnVj3yiJIZ5mH31%2Bt0C9ex9GPbVWGl%2FVQ%2FQtX31lPY33beSvXeecghw18LbEPztAB%2B3N9GQIUbZoGuQtjWDK4jPOiVcM5NfXX5tsWZ0WToDCQy3tVig5t5UA6%2B8VExVnweV2V1oH8Ah7ciy56TeeI2lht9mbq4MlBi9FhzDkDtMB33BFZm3ZkUx00LBdcyccR7Qysd5U3Ub2e0b&X-Amz-Signature=fa145109e4811d7163ff7f782f35a292c81341533cab1b185da0ee742b39a56a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LVWECBI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCjLRAMtAp%2Fp%2BxnmemvMjOC15kMbA0V5OeGEC4I9XLkJQIhALJYufWut%2F7fE6DvhFZleDJZUjy%2FgluhZWqroXSzrvbsKv8DCFoQABoMNjM3NDIzMTgzODA1IgwDPSpfk8Z1NGE47Ksq3APhEQ0HN6ggG%2FliJS1erKn3chFSQ6e22zbWMWhegSgcdHHcQvq1a%2Fy84L7DD%2FPR3vYCgcA56g9e5ntAV647igHZmMdycnhvjqkF3Dzqdjf3syI3MjW%2FR0EaaRWRd231psKI%2BP%2FvhaUHTIxVxExEHpDCkLkc1sGEL7s8iURsQOIAE8ZmOYAyBXjegswIZSX8gdfpBDGPGmE%2B0h2Vwa0z3SKKfP5WA6ExAEozkh2CLHnyvPgzjJdDLkyMx%2FV2zwJ3JFPkZ66DPj3aDMACrCutd6gtQYT5iam5yUGzolD8em0T2AyEmJfFHhPD4MitvXBcJ4E%2B3QZ2%2Ftg5%2BX54u1M%2Ff6A2e0u3O1G72fXun%2FngJ4nXVMEkVYCkviTFWQ%2FPro6KovMPAoi9h9JAY%2BiJgNfa8SMWqVdq8l5d0K9%2Fu7clcTSH6naDWi5EaKqjl4dMgGrtNc33U4mVyZ8yLESMyZG6tlybiK%2BKB8FyF322d%2FDIwnHIPCr2JVA98OYXqZuNtWQA8NBtgMDOZnD9V2MwNhHMQfIf%2BZk0s0PrxGtnr5ujJlEu5Vqg9YkO4sWnlLNPtcuGYaYAfGnjwMeNKxUyJZ79hLCawNn2mnAq7SVrLdbs2lWZ%2FQd55pySOodjUL6hCTCr7JG9BjqkAflgpF5VraP6uAnVj3yiJIZ5mH31%2Bt0C9ex9GPbVWGl%2FVQ%2FQtX31lPY33beSvXeecghw18LbEPztAB%2B3N9GQIUbZoGuQtjWDK4jPOiVcM5NfXX5tsWZ0WToDCQy3tVig5t5UA6%2B8VExVnweV2V1oH8Ah7ciy56TeeI2lht9mbq4MlBi9FhzDkDtMB33BFZm3ZkUx00LBdcyccR7Qysd5U3Ub2e0b&X-Amz-Signature=8c6ec4b56ea143c0ad96c562087e406df6d6d12f7f248ac20f665a729979731b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

