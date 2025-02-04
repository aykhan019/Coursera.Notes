

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=864d1ded0c6eeaed30fc050eaa397a7adcc0c3d915e497888c27b9d630f9d39a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=c1c4ac3b8c5ea4885e207a260cbe30d614d90ba2ffde862871e0181127906978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=aa27910214ca42e3d9654f4435a36d0abb4e712ab2a09112355c9e1fb24f242a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=c6204d9dba719e5334439797f3c6ff242d2eebe22114cb2bf6d6b873edf09c00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=d5b8f2a6cf7aa76f1471b85889663cfab8f90261760f49a2905d50dd07558468&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=35e6924fe78130489fa9799f8f0c1d552469accf5b04b1eee867d3ba162ee1a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=53332b52031481fdf9cce5e14b0a14d5b1fd4fd72f8ac96aaa5df3254778b3a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=0aaeb3bf59109649b65ffdecb8eb0f446bf9311db0ffc81d1d05af8cbb85d761&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=b889efd6126303e5b3760460188e3b15ef84df8e4c5ef9a1ce464d8ea470774a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=5c9e69e5f79c048d3a391612aee73153b2e11a89e532f4a70aacd2e517aca53f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRYXXA5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFVEMEOd%2F6bb9CmUrDOq0Uw3MaVvMpBBQ0MZwVZQQ0IhAiEA6bamU%2FwQN5VxSMWdLiyCkGAeT0Eohd9vYXl8pxaMkckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIy65J5TCwU9lnG5ECrcA96fagl5Ov%2FqNvYNJEt3jl1XboyeeVitO0aRAFD8jqlsvuYxJtWJxf4wegh%2F822rpFIvrOCrtYKYd9ympSjcq8pluSsJIDe%2Fzm6Q9v292V9U17Nji2KYlmT5gQF8MNuKRSbFckFjIiaOwIaGl4Aehy%2F3fNY3fciOfUHaB5qf0cEnFWkFrSRaLU6eogxAHD78whCLEZwxLT75O8AmcyYGqU3PN0hDDDPMcr2BwTiUUhyQt16o%2BniF23j7ctXXr00eyBPk5Gcxsjs48LzgSsszqQW5Er39t9TxVGmdwYk2FRQUrL2I6kGeVzhkh%2FBE6J4iCPNwuKGBTbRIa9ZkKS3qLuld6xrmpmTDU5hh30LVlsmZ7u5AGFrzATIxwMBigBecwVIVHxKgbpNY2drCRx%2F5sIYjz53VHoPoGJFjFgcpZVU%2FQilu7sshVO%2FpfOHB7Y7Pi8mO%2FUPljVj1YM9k1nX47sh%2BvZs%2FJLPiDOYHoGddk03%2F7n2qeL4TpA5T%2FgYQqASo7mVngRT97IlvZtrE3TBAx8C5T%2BzxDn0lGXz%2F%2Bg8vanzghqS7RAcSwS2LXJycemTm%2FJggN4lX7JvX2IX18iuWeh%2BHnfehh1ic%2FHGJbITZsEUp0YHgGJL1PA09ibGnMOjlh70GOqUBdrYDafJz9UuSirz6QxNR2laLRJ82%2F0y8OSOfA%2Fgr1PuIt68EcZ6zmt%2FyoASXo2W5vozL7NPbuf8xSgb91w0EvMa%2BECLlLng0GGkHG6SQtScxodbFlkuorhhO6u5pQ0e2QPjVYt4CUiOTuIkqoIeZn%2B7SZ0CmkAH%2BnEE9WJieQ7V7UmwRaU%2BOD%2Bs6xnhhwrfrO%2BpOGM8CyMLGXK2bBMMgV5nUevIK&X-Amz-Signature=71204463a39cd8d3f58fff6cab44ee5e1111904b0252403bbb27d9cf92a83374&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHHREPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAYn6xnIDkQowG3TFLolkmPqFR2w2v9szMpw1lA%2FJPjrAiEAu3XkYa43gsRrLcovuYugVJ26ClaSa%2Bg%2F2Poj%2BkX%2BfkQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDL3d4LM51V%2BArcTqFircA3dn6OP6YS0Foq1u0csOoxvG2e9%2Ff%2FaIIhy5yOfqojIF3D6O9I6qITNdbwzidGEz0E7girzuI5%2BumQELQcJk8tzDjFEzDoyUbCjBvTjE%2BCSl1ROt6rw9Uc%2BbVWCpEOcRY2MXlgpkEBZcJYGMhawrs4zVPAyq4g6ZLLBJHOCGqL3rBctKxR7Pvdyqpq%2BWbOuKlfaHxj%2Fi1dw7f3FzNFNw7Z2Nzxnb5%2FLdpbyyGorJY3owJK5TNThOeU8408lVcykT4bLdHGGR8MV4kmiVCC%2Fwet%2BeyryAUDYsondBItgLjAEaFnEJ2EVw7WVDiq9lgindK%2FPLp9z%2F8T2XkmJUk%2B4UyAzsZgvRABZX2r9NJc%2FSe5HrSuwYG8tgDA75FmChquPOyrZTsOC9Lh7bLszDK9MuDNfAQqTG4fWe7z2oN6u1bHWumhalCcivLnZiDzF8sw7t6cpHU3%2Bs5Mr8lJ7d8ANIwRwGgNwoP1p46jWKxHSc%2B%2B1hZBTZVxq%2Beixd381K0cIPhtJnBq9N4RVbjjKRY%2FiBydUEbJ9EunBM6PI%2BD0mQ24RTN6ZUVYyx%2Fzy436kHD%2FEwuqQOSbAaDWd%2FLEgSeLSXmL504uLc7L7674ugGDd15pAC9kbzoEcSzMOMUbYAMOvlh70GOqUBl4fJrm%2BMDTLmXfjbjwQpfFOXqoQ9ncRluBR11d5XMF1tv8ZhHyBOG2KTz929i2vzgSWVhIp3lZY6eY5pspYyuyxjHy5qL01YYMy9Lth9vb9mSkHtanBy6HASiiHn6t5GUXhpxKm9lEWkcEEavRNEBPAfMz%2FTGlbmCatnKWBRk3eLjkIU36y1nBw%2BYlmbjmXAOqWoXIxR5r5nmtgS18OCdo2lqiul&X-Amz-Signature=23c06dcbb54e9f46a2647d3501d0dbd8ba305a4bb710eadf8e72ca8c8a70c6b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHHREPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAYn6xnIDkQowG3TFLolkmPqFR2w2v9szMpw1lA%2FJPjrAiEAu3XkYa43gsRrLcovuYugVJ26ClaSa%2Bg%2F2Poj%2BkX%2BfkQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDL3d4LM51V%2BArcTqFircA3dn6OP6YS0Foq1u0csOoxvG2e9%2Ff%2FaIIhy5yOfqojIF3D6O9I6qITNdbwzidGEz0E7girzuI5%2BumQELQcJk8tzDjFEzDoyUbCjBvTjE%2BCSl1ROt6rw9Uc%2BbVWCpEOcRY2MXlgpkEBZcJYGMhawrs4zVPAyq4g6ZLLBJHOCGqL3rBctKxR7Pvdyqpq%2BWbOuKlfaHxj%2Fi1dw7f3FzNFNw7Z2Nzxnb5%2FLdpbyyGorJY3owJK5TNThOeU8408lVcykT4bLdHGGR8MV4kmiVCC%2Fwet%2BeyryAUDYsondBItgLjAEaFnEJ2EVw7WVDiq9lgindK%2FPLp9z%2F8T2XkmJUk%2B4UyAzsZgvRABZX2r9NJc%2FSe5HrSuwYG8tgDA75FmChquPOyrZTsOC9Lh7bLszDK9MuDNfAQqTG4fWe7z2oN6u1bHWumhalCcivLnZiDzF8sw7t6cpHU3%2Bs5Mr8lJ7d8ANIwRwGgNwoP1p46jWKxHSc%2B%2B1hZBTZVxq%2Beixd381K0cIPhtJnBq9N4RVbjjKRY%2FiBydUEbJ9EunBM6PI%2BD0mQ24RTN6ZUVYyx%2Fzy436kHD%2FEwuqQOSbAaDWd%2FLEgSeLSXmL504uLc7L7674ugGDd15pAC9kbzoEcSzMOMUbYAMOvlh70GOqUBl4fJrm%2BMDTLmXfjbjwQpfFOXqoQ9ncRluBR11d5XMF1tv8ZhHyBOG2KTz929i2vzgSWVhIp3lZY6eY5pspYyuyxjHy5qL01YYMy9Lth9vb9mSkHtanBy6HASiiHn6t5GUXhpxKm9lEWkcEEavRNEBPAfMz%2FTGlbmCatnKWBRk3eLjkIU36y1nBw%2BYlmbjmXAOqWoXIxR5r5nmtgS18OCdo2lqiul&X-Amz-Signature=55639f035fea2089b9c70e8d4e0b24c9ea129cb6b22a077d35dc39a9a545dfad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHHREPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAYn6xnIDkQowG3TFLolkmPqFR2w2v9szMpw1lA%2FJPjrAiEAu3XkYa43gsRrLcovuYugVJ26ClaSa%2Bg%2F2Poj%2BkX%2BfkQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDL3d4LM51V%2BArcTqFircA3dn6OP6YS0Foq1u0csOoxvG2e9%2Ff%2FaIIhy5yOfqojIF3D6O9I6qITNdbwzidGEz0E7girzuI5%2BumQELQcJk8tzDjFEzDoyUbCjBvTjE%2BCSl1ROt6rw9Uc%2BbVWCpEOcRY2MXlgpkEBZcJYGMhawrs4zVPAyq4g6ZLLBJHOCGqL3rBctKxR7Pvdyqpq%2BWbOuKlfaHxj%2Fi1dw7f3FzNFNw7Z2Nzxnb5%2FLdpbyyGorJY3owJK5TNThOeU8408lVcykT4bLdHGGR8MV4kmiVCC%2Fwet%2BeyryAUDYsondBItgLjAEaFnEJ2EVw7WVDiq9lgindK%2FPLp9z%2F8T2XkmJUk%2B4UyAzsZgvRABZX2r9NJc%2FSe5HrSuwYG8tgDA75FmChquPOyrZTsOC9Lh7bLszDK9MuDNfAQqTG4fWe7z2oN6u1bHWumhalCcivLnZiDzF8sw7t6cpHU3%2Bs5Mr8lJ7d8ANIwRwGgNwoP1p46jWKxHSc%2B%2B1hZBTZVxq%2Beixd381K0cIPhtJnBq9N4RVbjjKRY%2FiBydUEbJ9EunBM6PI%2BD0mQ24RTN6ZUVYyx%2Fzy436kHD%2FEwuqQOSbAaDWd%2FLEgSeLSXmL504uLc7L7674ugGDd15pAC9kbzoEcSzMOMUbYAMOvlh70GOqUBl4fJrm%2BMDTLmXfjbjwQpfFOXqoQ9ncRluBR11d5XMF1tv8ZhHyBOG2KTz929i2vzgSWVhIp3lZY6eY5pspYyuyxjHy5qL01YYMy9Lth9vb9mSkHtanBy6HASiiHn6t5GUXhpxKm9lEWkcEEavRNEBPAfMz%2FTGlbmCatnKWBRk3eLjkIU36y1nBw%2BYlmbjmXAOqWoXIxR5r5nmtgS18OCdo2lqiul&X-Amz-Signature=8d7864b1f7c0a2ebb75e4bb307fe5258688846351b0f8a9097481502d1a69865&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHHREPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAYn6xnIDkQowG3TFLolkmPqFR2w2v9szMpw1lA%2FJPjrAiEAu3XkYa43gsRrLcovuYugVJ26ClaSa%2Bg%2F2Poj%2BkX%2BfkQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDL3d4LM51V%2BArcTqFircA3dn6OP6YS0Foq1u0csOoxvG2e9%2Ff%2FaIIhy5yOfqojIF3D6O9I6qITNdbwzidGEz0E7girzuI5%2BumQELQcJk8tzDjFEzDoyUbCjBvTjE%2BCSl1ROt6rw9Uc%2BbVWCpEOcRY2MXlgpkEBZcJYGMhawrs4zVPAyq4g6ZLLBJHOCGqL3rBctKxR7Pvdyqpq%2BWbOuKlfaHxj%2Fi1dw7f3FzNFNw7Z2Nzxnb5%2FLdpbyyGorJY3owJK5TNThOeU8408lVcykT4bLdHGGR8MV4kmiVCC%2Fwet%2BeyryAUDYsondBItgLjAEaFnEJ2EVw7WVDiq9lgindK%2FPLp9z%2F8T2XkmJUk%2B4UyAzsZgvRABZX2r9NJc%2FSe5HrSuwYG8tgDA75FmChquPOyrZTsOC9Lh7bLszDK9MuDNfAQqTG4fWe7z2oN6u1bHWumhalCcivLnZiDzF8sw7t6cpHU3%2Bs5Mr8lJ7d8ANIwRwGgNwoP1p46jWKxHSc%2B%2B1hZBTZVxq%2Beixd381K0cIPhtJnBq9N4RVbjjKRY%2FiBydUEbJ9EunBM6PI%2BD0mQ24RTN6ZUVYyx%2Fzy436kHD%2FEwuqQOSbAaDWd%2FLEgSeLSXmL504uLc7L7674ugGDd15pAC9kbzoEcSzMOMUbYAMOvlh70GOqUBl4fJrm%2BMDTLmXfjbjwQpfFOXqoQ9ncRluBR11d5XMF1tv8ZhHyBOG2KTz929i2vzgSWVhIp3lZY6eY5pspYyuyxjHy5qL01YYMy9Lth9vb9mSkHtanBy6HASiiHn6t5GUXhpxKm9lEWkcEEavRNEBPAfMz%2FTGlbmCatnKWBRk3eLjkIU36y1nBw%2BYlmbjmXAOqWoXIxR5r5nmtgS18OCdo2lqiul&X-Amz-Signature=78558d0060764e494ff60de7d4b915d4de53a97c171f807dc0a35717237c6b66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDNU524P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDpCLAVMzjgAgweDBqN0Sh7P2pDi7U9vZkUCmBpcAUixQIgHZK31J3Abdc%2BSguf6QnEGpTYxFRZ%2F1Ny3Z6JqiJmzTUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDN%2BmkU%2Fht7PAqHryOCrcA7XcdLQnPu8flh0USzNV%2Bco6bftPgoVZM8sWctZwyOchW3CHBdOeXFmHiUWjwYx%2BRF7D1Y7uyg0u4px2oye8a4%2FnWRA%2BeDIqy7XcvzuwTcjYj4R4Ok9atJFNME7wXBR6p%2Bp%2FL52U4xYBVNQQrHli8jqGJFo%2BiG7y5mFWao27qKc4sFuTWXKcf0CwDvbWz2DCOnMwku7P9w0%2FJpiuIlwbc3F0y75hzCdCk4v1bqC0plmJ%2FFzTue6CrymFPaP67XWDN%2BM36w8JUVfUU23P%2FO9cgvlmOVl6nODhf%2BfnwDZ9HrnUB4V3ZNTGj0BeMT1hVpPLNYdFJGIY%2BuZPY5FFJ0ZB6qQpmzwxy8DobyjMfn4miQjmBi1XvW6mUQwdZmdwPqjFgTgW7sJLH6rhcwmPATpQT%2FTXnJ5kZCrdGfj5hr7ERbiTOsPNSmR2t7bKzKJOTku6%2Be0U9HHRTYo2%2Byrwad%2Fr%2FO9XCsuMeysOesCSJA8sUkZ%2FMyfEY0GHVt6FtKAeWH0PpBH3YIinCnjgGQ0T618I7B2aAHQp0GuQw9VwHEWQPE0eEfkdH2UW4yVa8CQwENvet5K1uld8BzdBJ9mBwF%2FMjTXZI%2F%2Bwh8bx5WqrfmDw9BXbXAO9CQmpTm6L8%2FnAMJ3mh70GOqUBi4FJ84xWr9782cXcZzNOyMmSfBv2txiXEPrDCG2FVFr%2F9CNxZCGR5FWdIprX8fge3WyfNuufZh3qY6yf17bYSWJtURGGhCGvJuj3JcQtt44l6BcBjDPLKrLnt1mEPlpf%2BT3yZ1N5BV1UhEC9jUyLpaSD0luXdSd99PUttW9aqc58GEkmw6xjiDudRlXs%2F9fKK9L2BiI8XkI1VYSChxPvHHTpWoHp&X-Amz-Signature=c8d5cca8050e99b7f2602912cb0db62f7c947348c5ad12499baee1e5a19cd706&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDNU524P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDpCLAVMzjgAgweDBqN0Sh7P2pDi7U9vZkUCmBpcAUixQIgHZK31J3Abdc%2BSguf6QnEGpTYxFRZ%2F1Ny3Z6JqiJmzTUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDN%2BmkU%2Fht7PAqHryOCrcA7XcdLQnPu8flh0USzNV%2Bco6bftPgoVZM8sWctZwyOchW3CHBdOeXFmHiUWjwYx%2BRF7D1Y7uyg0u4px2oye8a4%2FnWRA%2BeDIqy7XcvzuwTcjYj4R4Ok9atJFNME7wXBR6p%2Bp%2FL52U4xYBVNQQrHli8jqGJFo%2BiG7y5mFWao27qKc4sFuTWXKcf0CwDvbWz2DCOnMwku7P9w0%2FJpiuIlwbc3F0y75hzCdCk4v1bqC0plmJ%2FFzTue6CrymFPaP67XWDN%2BM36w8JUVfUU23P%2FO9cgvlmOVl6nODhf%2BfnwDZ9HrnUB4V3ZNTGj0BeMT1hVpPLNYdFJGIY%2BuZPY5FFJ0ZB6qQpmzwxy8DobyjMfn4miQjmBi1XvW6mUQwdZmdwPqjFgTgW7sJLH6rhcwmPATpQT%2FTXnJ5kZCrdGfj5hr7ERbiTOsPNSmR2t7bKzKJOTku6%2Be0U9HHRTYo2%2Byrwad%2Fr%2FO9XCsuMeysOesCSJA8sUkZ%2FMyfEY0GHVt6FtKAeWH0PpBH3YIinCnjgGQ0T618I7B2aAHQp0GuQw9VwHEWQPE0eEfkdH2UW4yVa8CQwENvet5K1uld8BzdBJ9mBwF%2FMjTXZI%2F%2Bwh8bx5WqrfmDw9BXbXAO9CQmpTm6L8%2FnAMJ3mh70GOqUBi4FJ84xWr9782cXcZzNOyMmSfBv2txiXEPrDCG2FVFr%2F9CNxZCGR5FWdIprX8fge3WyfNuufZh3qY6yf17bYSWJtURGGhCGvJuj3JcQtt44l6BcBjDPLKrLnt1mEPlpf%2BT3yZ1N5BV1UhEC9jUyLpaSD0luXdSd99PUttW9aqc58GEkmw6xjiDudRlXs%2F9fKK9L2BiI8XkI1VYSChxPvHHTpWoHp&X-Amz-Signature=7d410ea1a0aab7d95f876a40f670f2de2e547cd51145b78b60f6900a40e5cefb&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDNU524P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDpCLAVMzjgAgweDBqN0Sh7P2pDi7U9vZkUCmBpcAUixQIgHZK31J3Abdc%2BSguf6QnEGpTYxFRZ%2F1Ny3Z6JqiJmzTUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDN%2BmkU%2Fht7PAqHryOCrcA7XcdLQnPu8flh0USzNV%2Bco6bftPgoVZM8sWctZwyOchW3CHBdOeXFmHiUWjwYx%2BRF7D1Y7uyg0u4px2oye8a4%2FnWRA%2BeDIqy7XcvzuwTcjYj4R4Ok9atJFNME7wXBR6p%2Bp%2FL52U4xYBVNQQrHli8jqGJFo%2BiG7y5mFWao27qKc4sFuTWXKcf0CwDvbWz2DCOnMwku7P9w0%2FJpiuIlwbc3F0y75hzCdCk4v1bqC0plmJ%2FFzTue6CrymFPaP67XWDN%2BM36w8JUVfUU23P%2FO9cgvlmOVl6nODhf%2BfnwDZ9HrnUB4V3ZNTGj0BeMT1hVpPLNYdFJGIY%2BuZPY5FFJ0ZB6qQpmzwxy8DobyjMfn4miQjmBi1XvW6mUQwdZmdwPqjFgTgW7sJLH6rhcwmPATpQT%2FTXnJ5kZCrdGfj5hr7ERbiTOsPNSmR2t7bKzKJOTku6%2Be0U9HHRTYo2%2Byrwad%2Fr%2FO9XCsuMeysOesCSJA8sUkZ%2FMyfEY0GHVt6FtKAeWH0PpBH3YIinCnjgGQ0T618I7B2aAHQp0GuQw9VwHEWQPE0eEfkdH2UW4yVa8CQwENvet5K1uld8BzdBJ9mBwF%2FMjTXZI%2F%2Bwh8bx5WqrfmDw9BXbXAO9CQmpTm6L8%2FnAMJ3mh70GOqUBi4FJ84xWr9782cXcZzNOyMmSfBv2txiXEPrDCG2FVFr%2F9CNxZCGR5FWdIprX8fge3WyfNuufZh3qY6yf17bYSWJtURGGhCGvJuj3JcQtt44l6BcBjDPLKrLnt1mEPlpf%2BT3yZ1N5BV1UhEC9jUyLpaSD0luXdSd99PUttW9aqc58GEkmw6xjiDudRlXs%2F9fKK9L2BiI8XkI1VYSChxPvHHTpWoHp&X-Amz-Signature=ebe1b6128dfd08be45953c10b5907731fbc84386ab60fcfbe5df16aec5c42457&X-Amz-SignedHeaders=host&x-id=GetObject)
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

