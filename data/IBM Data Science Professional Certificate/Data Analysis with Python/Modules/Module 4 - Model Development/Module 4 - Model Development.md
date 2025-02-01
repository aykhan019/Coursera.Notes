

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=0be7488598cdcf5ed9481e1af24666314dd8e70ffe716e10ca45b58bdadca1fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=fbcdf566977a25db9e2c5a7d0a31068368195770dd12d5f723cc67144ff389ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=dcd9a43cb3ea7db0ba791bef37ee229ac5b0d5a6ed29958b175f61330fe2f797&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=ca89b4321d06e6877999422c3dccfb41216782c0a096cb158cd129778e954ac0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=0ba21688e1d610009de8fa8940bfba9623464944d3c80d3178abf45e13c4f93e&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=3cf514ca1e8afe223d619a71874d9ae0c642d3fbcfcd486ce25fcdfe9abb5d2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=efa1bd4fba1a95ccc7d30bdc2e406afbbb04bcf50ca5f63d49c3514d6f71d053&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=155e60e0984cc46afbcfd3654e4f5cc38c0634b689855281fbd13da371203290&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=3cb18c44e64c3a7399a953fc787e1f21a2b981f43098aee1749a1206139c9ff9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=f48fe3dc9e11add5667300152f0eadeb6de63d6b6269f021e773bd4f63ebd828&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPCNNLN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEykzfUzGMXsUs80Wq8ZLMpGOkLVARXL7SXZRyDy4L%2BQIgLFBNg6oqh%2Bk3ES%2FdppwJs4ZA3IB4koxgImAaEPrh85QqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATHQp5HzTI%2BUNcw9CrcA7g98OKOiKtkceGOBlzdP4ic1umIvI47lIddFl63gS2zELsMXO%2BdRFQJfF0D5XALFpgep0AlsjlEpiJacJzN3x%2B6JDwxsldWsYdLCSUqIHy59FXsoOIVi%2F3tuh%2FKrJDoJl0cb7mNsg18pd71xd%2BhUpEJw6BYdjqZHRLZwGn%2FNB2BZCCQIgBxesuVnQSOtSaULX8jumjKaCfys6wmFHV4HF5iorcmwchC%2BmU5WJtC4JIWbHnigl24et%2FZRNSFvjlMl5z7DFrsCpoSEqCoMqUDPNw1PtXUjRr0xVxzXDYw2STCojTmoflk40ck7Dymr40%2BY1EtNfP1O95x3VQ6vJhM5mUl2hBT72bvD504fyQ%2FKL91waSBa1x7EG7Kf1zq278MzCVcifgpMpkXB4euqwpfqEIJujE8xJdP3x%2Fw3Oir%2BzaDFv9cdh4ZFk5KytRWytga9iigyTSKHEFKOvNAJx73TMePJbVlFPbgm2dPPMt3Dj%2F%2FyT2tgOflioGSp%2BNe3yCq7dM1t2UtmqWKPfBPrx%2FY5tXpD9dcYo6W7ykggAsq85tES9KpSgiMnkAcvNP6N42Y5nwJt1pqS0isvdCUYJYIh5j2WL%2BQWXlr3wn3FXh58ezF9plOmnvhXO78iia4MLix%2BrwGOqUBdtWSr1WNypSMAtOQ797iE488POmg9dbcwvbWtFxnKBpZbXIWSlI%2Fpkd8XaYcgZUR9Mi%2Fy5IF2Fey2XMJErtbFFf1dlOmebhbYdAWFjWfG7DRGvnNeMmMqL6ACB%2FZezVBgVeZA5Vi2xUTk0xD74OK8abqnDhxdF1p85z2U1P57pEcPc7UQBwnA5sRlwu0gdu8WRy%2Bz8Am8b2gCnxtjm0C2gxtQIYB&X-Amz-Signature=9185aa0aa26d6da4e916abf4538e76f4c2d686f7c4b2e0cad3a52de327507358&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGU5XK6H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCujJ0BS0Gx%2Fxt5i2z1OvFY2U1KHF9%2FoERrgSpK5VRLHwIgFMPqOCva5HDMVoWXiEQV5PlMhUvuPuaanv1vicFQinkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA6D3BfD6jtLC4xDircAzfYN%2Bo8LxTOmOIwEhSU7li8x%2FSsn8DvDdOCKiNh9nz3XpXMemXxsku9pXm7JGE4EVMwAxu7UGt5gWKbGoyYTCE99YMAY5539NbRu6PV3Zy4D7lFFbZv%2F8zS%2F6tKSXElAUGKO4zrlEcYF1oBYwO%2BBb9gldMJ7cda5frfsESKtYzYEKD65d30QLNp2aSR5p2noUxr8DsdEbbp%2FtEMo7mVmHEy2AEOfo5fHU7QYb1OOCFinh0BnqaeVhu%2BECj21xtr5ridz7dW8OKPgS%2BIdo6cf1QwQdmGNwFXwxZZw%2B7xx3rckcfpQ%2F0%2Fq7wJc6LHzCZvoYl9IBSczkkZc3kC5M1cY0ukaumxBymXxNvZOXbng6ASi9d6DXm0OqFtbvo3w61E4%2F8XAP%2BrPuVEhyT32yFbRRgWkq50x00Dw6KUY6qOOMfaDGDoIq%2FcEcN5Ad2ygWvi4hCRtYQ6kWS7RGElDkMFC0P3d1rfjtk0fnfkuDxQaPVu8i9KE%2BZEqUbX9NnlKLa8229ouVhMlFn%2FJBLdZEPmkScwW2E3ZNktfhicbmo%2BpUcPGODvO%2FviNtR04LX9xaLHoJUAz6hQJYKQ7VZn6KWqnWjQ7vGSjLUBrE0FgayvP7yAGXvuTsuZE4WVcU0xMLmx%2BrwGOqUBNbt3p5vtZm%2BxkOkBslHlw6hHNRSsijTCStfqwEqceuff5U7t%2B5wwfMN0rxQVnzGVew4JO5bItLA3V%2BAERakplKwpHdw5YTWio6OzJ8zWvLdEHqE%2BgyGCrnOwqJVW%2BwSLZPPyVbmvt9Iq7TPfwaVUYYAgyrjaRqKL87mo8CvxeNwbkr3Rb97ylQQe3bahAm0%2BeP%2BqDvxZKsyYBf93OIXYklrnaZFG&X-Amz-Signature=2f612e1be3259c21a820e3e1079dcab0d20ae01aa758be0131f67a5b0004c432&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGU5XK6H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCujJ0BS0Gx%2Fxt5i2z1OvFY2U1KHF9%2FoERrgSpK5VRLHwIgFMPqOCva5HDMVoWXiEQV5PlMhUvuPuaanv1vicFQinkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA6D3BfD6jtLC4xDircAzfYN%2Bo8LxTOmOIwEhSU7li8x%2FSsn8DvDdOCKiNh9nz3XpXMemXxsku9pXm7JGE4EVMwAxu7UGt5gWKbGoyYTCE99YMAY5539NbRu6PV3Zy4D7lFFbZv%2F8zS%2F6tKSXElAUGKO4zrlEcYF1oBYwO%2BBb9gldMJ7cda5frfsESKtYzYEKD65d30QLNp2aSR5p2noUxr8DsdEbbp%2FtEMo7mVmHEy2AEOfo5fHU7QYb1OOCFinh0BnqaeVhu%2BECj21xtr5ridz7dW8OKPgS%2BIdo6cf1QwQdmGNwFXwxZZw%2B7xx3rckcfpQ%2F0%2Fq7wJc6LHzCZvoYl9IBSczkkZc3kC5M1cY0ukaumxBymXxNvZOXbng6ASi9d6DXm0OqFtbvo3w61E4%2F8XAP%2BrPuVEhyT32yFbRRgWkq50x00Dw6KUY6qOOMfaDGDoIq%2FcEcN5Ad2ygWvi4hCRtYQ6kWS7RGElDkMFC0P3d1rfjtk0fnfkuDxQaPVu8i9KE%2BZEqUbX9NnlKLa8229ouVhMlFn%2FJBLdZEPmkScwW2E3ZNktfhicbmo%2BpUcPGODvO%2FviNtR04LX9xaLHoJUAz6hQJYKQ7VZn6KWqnWjQ7vGSjLUBrE0FgayvP7yAGXvuTsuZE4WVcU0xMLmx%2BrwGOqUBNbt3p5vtZm%2BxkOkBslHlw6hHNRSsijTCStfqwEqceuff5U7t%2B5wwfMN0rxQVnzGVew4JO5bItLA3V%2BAERakplKwpHdw5YTWio6OzJ8zWvLdEHqE%2BgyGCrnOwqJVW%2BwSLZPPyVbmvt9Iq7TPfwaVUYYAgyrjaRqKL87mo8CvxeNwbkr3Rb97ylQQe3bahAm0%2BeP%2BqDvxZKsyYBf93OIXYklrnaZFG&X-Amz-Signature=2cdafb0cd7333becb1a5e2c974d7258b98cd0d0e5d171dc1a2c5a861510d251e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGU5XK6H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCujJ0BS0Gx%2Fxt5i2z1OvFY2U1KHF9%2FoERrgSpK5VRLHwIgFMPqOCva5HDMVoWXiEQV5PlMhUvuPuaanv1vicFQinkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA6D3BfD6jtLC4xDircAzfYN%2Bo8LxTOmOIwEhSU7li8x%2FSsn8DvDdOCKiNh9nz3XpXMemXxsku9pXm7JGE4EVMwAxu7UGt5gWKbGoyYTCE99YMAY5539NbRu6PV3Zy4D7lFFbZv%2F8zS%2F6tKSXElAUGKO4zrlEcYF1oBYwO%2BBb9gldMJ7cda5frfsESKtYzYEKD65d30QLNp2aSR5p2noUxr8DsdEbbp%2FtEMo7mVmHEy2AEOfo5fHU7QYb1OOCFinh0BnqaeVhu%2BECj21xtr5ridz7dW8OKPgS%2BIdo6cf1QwQdmGNwFXwxZZw%2B7xx3rckcfpQ%2F0%2Fq7wJc6LHzCZvoYl9IBSczkkZc3kC5M1cY0ukaumxBymXxNvZOXbng6ASi9d6DXm0OqFtbvo3w61E4%2F8XAP%2BrPuVEhyT32yFbRRgWkq50x00Dw6KUY6qOOMfaDGDoIq%2FcEcN5Ad2ygWvi4hCRtYQ6kWS7RGElDkMFC0P3d1rfjtk0fnfkuDxQaPVu8i9KE%2BZEqUbX9NnlKLa8229ouVhMlFn%2FJBLdZEPmkScwW2E3ZNktfhicbmo%2BpUcPGODvO%2FviNtR04LX9xaLHoJUAz6hQJYKQ7VZn6KWqnWjQ7vGSjLUBrE0FgayvP7yAGXvuTsuZE4WVcU0xMLmx%2BrwGOqUBNbt3p5vtZm%2BxkOkBslHlw6hHNRSsijTCStfqwEqceuff5U7t%2B5wwfMN0rxQVnzGVew4JO5bItLA3V%2BAERakplKwpHdw5YTWio6OzJ8zWvLdEHqE%2BgyGCrnOwqJVW%2BwSLZPPyVbmvt9Iq7TPfwaVUYYAgyrjaRqKL87mo8CvxeNwbkr3Rb97ylQQe3bahAm0%2BeP%2BqDvxZKsyYBf93OIXYklrnaZFG&X-Amz-Signature=99110e0fb9511f94c0bc4d162fb26b52fb9f73f07a7ad6a1226b7c94acf5f7e7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGU5XK6H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCujJ0BS0Gx%2Fxt5i2z1OvFY2U1KHF9%2FoERrgSpK5VRLHwIgFMPqOCva5HDMVoWXiEQV5PlMhUvuPuaanv1vicFQinkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJA6D3BfD6jtLC4xDircAzfYN%2Bo8LxTOmOIwEhSU7li8x%2FSsn8DvDdOCKiNh9nz3XpXMemXxsku9pXm7JGE4EVMwAxu7UGt5gWKbGoyYTCE99YMAY5539NbRu6PV3Zy4D7lFFbZv%2F8zS%2F6tKSXElAUGKO4zrlEcYF1oBYwO%2BBb9gldMJ7cda5frfsESKtYzYEKD65d30QLNp2aSR5p2noUxr8DsdEbbp%2FtEMo7mVmHEy2AEOfo5fHU7QYb1OOCFinh0BnqaeVhu%2BECj21xtr5ridz7dW8OKPgS%2BIdo6cf1QwQdmGNwFXwxZZw%2B7xx3rckcfpQ%2F0%2Fq7wJc6LHzCZvoYl9IBSczkkZc3kC5M1cY0ukaumxBymXxNvZOXbng6ASi9d6DXm0OqFtbvo3w61E4%2F8XAP%2BrPuVEhyT32yFbRRgWkq50x00Dw6KUY6qOOMfaDGDoIq%2FcEcN5Ad2ygWvi4hCRtYQ6kWS7RGElDkMFC0P3d1rfjtk0fnfkuDxQaPVu8i9KE%2BZEqUbX9NnlKLa8229ouVhMlFn%2FJBLdZEPmkScwW2E3ZNktfhicbmo%2BpUcPGODvO%2FviNtR04LX9xaLHoJUAz6hQJYKQ7VZn6KWqnWjQ7vGSjLUBrE0FgayvP7yAGXvuTsuZE4WVcU0xMLmx%2BrwGOqUBNbt3p5vtZm%2BxkOkBslHlw6hHNRSsijTCStfqwEqceuff5U7t%2B5wwfMN0rxQVnzGVew4JO5bItLA3V%2BAERakplKwpHdw5YTWio6OzJ8zWvLdEHqE%2BgyGCrnOwqJVW%2BwSLZPPyVbmvt9Iq7TPfwaVUYYAgyrjaRqKL87mo8CvxeNwbkr3Rb97ylQQe3bahAm0%2BeP%2BqDvxZKsyYBf93OIXYklrnaZFG&X-Amz-Signature=8888472052b7ca66a7b1ebe9eaca29869cf4d762c82361dee4ddec3f799e806c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS2A3KOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIURHy5B2pbYnzOxaY%2BJg308TxE8eoxmQyMGplud%2FH1AiEAuFKzg9wbJhShNNWIoucFmtcPf90qqYDziAfc95vTENMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGk%2BXFfwJ3PpF9mySCrcA6SpGwtUlB6F1k8S%2BPnY0vn3Q5eVlwJV4t%2Fegws8hxzzFXincn7wF4aAXgHSKVnPoOLQYGv5XL1mgKXG8XgVKo9ba1GGk26jRIh5aRKxeV33ixxvSOBSeomDilGWzgd95u1wkeEXSws49pW7zi0mFst%2B52ke6eBnJVPiMMNdpDsHE0KkSHyV93%2B9A2Y95jf0pvs3ubZMGNosDtYWGgeaXaa3Jwb125duazDs1ll15rI9jTaWKTVqxOt%2BJQSWbZTGcq01c9Oepyc9QShMybzgFrzGfKDPgibxwpK8MNUeGr7a1yaOIg7ZQSP%2BRE9P4yuWXRsDNKcHKvoZWFf2ePngry9I%2B9hSyTLVKe1qgy%2BJXvjkz1TPnDLp85PRXHOc50c5I1FnmUrCATqOWsNzJ8yFdkKhs2FIlAoXsizXpAfR%2FcPsgM2Km4Tn4gCrFV8UHkD4Wdq2BsEydD12HmM2UUPOASCNQK6nM2E3ExIc%2FcAnHg0LY0gdgK%2FTAyCwb8MfHZbNfj%2Fqixxwq4QsgdDG8qJEvdrrwzl4ynumcGWDnycp%2BpZMh2Yqu1AvWWI3DbIUrts2OU%2FfBf3oASY%2Fp27TaoKNA72pdZeMLAp4sLr%2FpNo8QwEZqnnHZmRCNZR6ZSE%2FMLWx%2BrwGOqUBbL0cOd7D7tFuueCcqMGYqhPhbHVHlhi928uHG%2BYdMCepz5YR2M38L88TsXZ9I3xl%2Fu9PxqcMRtFqf1D0ez9%2FynwdkyOxxIxqE7sYSJ1zlUUp9pPzoAioHQzwTjx0B1aZ4vY%2FB00qH7CcWnb3mKvX%2BG2QrHPeVraBXA%2Bv%2Brcx1DeKh0IKxQjpB15wAh77ecASOeFJCvARxMcE%2BwTkA2t65ZYWWK22&X-Amz-Signature=9e35fcd90b40fad4df15c827e446850584540ea108968823e5aa10eeffd61a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS2A3KOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIURHy5B2pbYnzOxaY%2BJg308TxE8eoxmQyMGplud%2FH1AiEAuFKzg9wbJhShNNWIoucFmtcPf90qqYDziAfc95vTENMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGk%2BXFfwJ3PpF9mySCrcA6SpGwtUlB6F1k8S%2BPnY0vn3Q5eVlwJV4t%2Fegws8hxzzFXincn7wF4aAXgHSKVnPoOLQYGv5XL1mgKXG8XgVKo9ba1GGk26jRIh5aRKxeV33ixxvSOBSeomDilGWzgd95u1wkeEXSws49pW7zi0mFst%2B52ke6eBnJVPiMMNdpDsHE0KkSHyV93%2B9A2Y95jf0pvs3ubZMGNosDtYWGgeaXaa3Jwb125duazDs1ll15rI9jTaWKTVqxOt%2BJQSWbZTGcq01c9Oepyc9QShMybzgFrzGfKDPgibxwpK8MNUeGr7a1yaOIg7ZQSP%2BRE9P4yuWXRsDNKcHKvoZWFf2ePngry9I%2B9hSyTLVKe1qgy%2BJXvjkz1TPnDLp85PRXHOc50c5I1FnmUrCATqOWsNzJ8yFdkKhs2FIlAoXsizXpAfR%2FcPsgM2Km4Tn4gCrFV8UHkD4Wdq2BsEydD12HmM2UUPOASCNQK6nM2E3ExIc%2FcAnHg0LY0gdgK%2FTAyCwb8MfHZbNfj%2Fqixxwq4QsgdDG8qJEvdrrwzl4ynumcGWDnycp%2BpZMh2Yqu1AvWWI3DbIUrts2OU%2FfBf3oASY%2Fp27TaoKNA72pdZeMLAp4sLr%2FpNo8QwEZqnnHZmRCNZR6ZSE%2FMLWx%2BrwGOqUBbL0cOd7D7tFuueCcqMGYqhPhbHVHlhi928uHG%2BYdMCepz5YR2M38L88TsXZ9I3xl%2Fu9PxqcMRtFqf1D0ez9%2FynwdkyOxxIxqE7sYSJ1zlUUp9pPzoAioHQzwTjx0B1aZ4vY%2FB00qH7CcWnb3mKvX%2BG2QrHPeVraBXA%2Bv%2Brcx1DeKh0IKxQjpB15wAh77ecASOeFJCvARxMcE%2BwTkA2t65ZYWWK22&X-Amz-Signature=64793e23cbba1e0d5971932273fd0b023aa69c1f3583273e7115469b94e10db2&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS2A3KOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIURHy5B2pbYnzOxaY%2BJg308TxE8eoxmQyMGplud%2FH1AiEAuFKzg9wbJhShNNWIoucFmtcPf90qqYDziAfc95vTENMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGk%2BXFfwJ3PpF9mySCrcA6SpGwtUlB6F1k8S%2BPnY0vn3Q5eVlwJV4t%2Fegws8hxzzFXincn7wF4aAXgHSKVnPoOLQYGv5XL1mgKXG8XgVKo9ba1GGk26jRIh5aRKxeV33ixxvSOBSeomDilGWzgd95u1wkeEXSws49pW7zi0mFst%2B52ke6eBnJVPiMMNdpDsHE0KkSHyV93%2B9A2Y95jf0pvs3ubZMGNosDtYWGgeaXaa3Jwb125duazDs1ll15rI9jTaWKTVqxOt%2BJQSWbZTGcq01c9Oepyc9QShMybzgFrzGfKDPgibxwpK8MNUeGr7a1yaOIg7ZQSP%2BRE9P4yuWXRsDNKcHKvoZWFf2ePngry9I%2B9hSyTLVKe1qgy%2BJXvjkz1TPnDLp85PRXHOc50c5I1FnmUrCATqOWsNzJ8yFdkKhs2FIlAoXsizXpAfR%2FcPsgM2Km4Tn4gCrFV8UHkD4Wdq2BsEydD12HmM2UUPOASCNQK6nM2E3ExIc%2FcAnHg0LY0gdgK%2FTAyCwb8MfHZbNfj%2Fqixxwq4QsgdDG8qJEvdrrwzl4ynumcGWDnycp%2BpZMh2Yqu1AvWWI3DbIUrts2OU%2FfBf3oASY%2Fp27TaoKNA72pdZeMLAp4sLr%2FpNo8QwEZqnnHZmRCNZR6ZSE%2FMLWx%2BrwGOqUBbL0cOd7D7tFuueCcqMGYqhPhbHVHlhi928uHG%2BYdMCepz5YR2M38L88TsXZ9I3xl%2Fu9PxqcMRtFqf1D0ez9%2FynwdkyOxxIxqE7sYSJ1zlUUp9pPzoAioHQzwTjx0B1aZ4vY%2FB00qH7CcWnb3mKvX%2BG2QrHPeVraBXA%2Bv%2Brcx1DeKh0IKxQjpB15wAh77ecASOeFJCvARxMcE%2BwTkA2t65ZYWWK22&X-Amz-Signature=9d3bf9e9b37b881d032ff59e46d44ab5e2ce85d70e9f7b6562bdf5258171dd0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

