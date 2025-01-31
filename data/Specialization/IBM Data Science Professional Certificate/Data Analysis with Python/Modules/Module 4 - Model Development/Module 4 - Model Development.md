

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=5ed42f11388c69b02289804f6b933c769d619589dc7a6b18e844811459d11232&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=c773a6d9d20a56bcc4bf76de722699547bda9b4ed749a78b2e78469396571aad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=ca788302da62af5b08907c6c137ffa8f32bc6b817ab9be67f289a0a55f8fd291&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=af8a0d89d2f4f31b9765834d9f006e378572c6f8c50d60c194d64e80db7f45a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=a24a28a283e0e96b950e3a21a002d51d1fae447c16513bfc3c12c1576d2bce0f&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=d82fad91b4d49981ec15ef621c8c72dbe612d5e31e2fd1d26480ff7491de30f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=f60dfe449ac46426411ff68377c91d73e447690e2cc734e68a0156b0597c4430&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=be3df4783442f8c829b2dc975a423b8ccaa02c3c47bc5ea5abbda71159a8e82f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=a788bed83d0d76f1595ebd8538541627d0a7894c1f882e1277d62ad9360b7ded&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=6528ddb15e41d22c6bf50da006457c640da667f09bb449ffca22d6ed28cce280&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672WJAR23%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNvCU%2BKL3yVypfYkN%2BB3Y3Uw7UHwBN1yev1%2FGRilggGAIhAM%2BeN%2BB3se6yp625TIz4bmrr%2FNziQJQtI%2BOycOjGftDvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvR9unr67wk%2F3Disq3AOAycreUGPwLUyZdsnwcuOR3JO7RrlCOuheKun%2Fpd5EcVFMGqKl%2BmP4sJPlZj7o0BQBv8RwXqHJfVfeCUmOIINz3BL6LXNYAD6MNs94ijt0Ir%2B4pToWROB7k76oIwaCXf3caQfRs8A57CTQlx4I6stPVyijKsVt1hpKu3dCt8OKdyjlr%2F10yXnhGQBtkHKIxJfUrWw5dTGoqqg0Z5IxkLtwWb7jYC5GQTj7j9hEUCIw4oMDzFwg9YhGhWvVzF1J0S7BbWuN0P9jwIckOH8BwYBUi1pKMOH35QQXQ%2Biid3zk8E6%2F8xTM8pCtLZ%2BG6V949IEES9c2FIiD01x1fDhtZIuaiFs%2BEIujR1G8PaO8mUfN4l3IY8d4UGA%2FUcH13vY0z6iRfcrN0QmX4cX5gqreaepOFoPKjdITT7IF12DwSR6SpKyF4N4l7LK0lnf0kHNigOt%2FRREJ3nOBKvUWpTi%2BYuPvBGNCc%2BgOG%2F2A%2BScjAXHHeG9aFFYdzHLaBgTm3r%2FmmwEDrhNgL5%2BaggirxS%2FAedAkQBa7WrGDG2uYWpc0SZu2H7XO6SQS9X49TxrXVGwbNCaCqNldXlrHPsX2xk2OZ10gIjguVrUp0mhZjdMrLXB00tIZOUPASRI1GIDREjDhtvK8BjqkAQaLoAe7rWZfpzs3IeKmZ3JUBgShIElfNEtyqdnYnzGbhpC3u3kL2jTdEmlRrZn9ri%2FrSaV8aqcV4%2FaT2ndw0Haz0k3CvBIBnI60iYgvGK%2FLKiplveCRH43e8Tge7CtbBu6QNyFw3ULI8xGFm7L%2BYI0CMYjK1fz2m2Y7UOjnoYdSScR2a6uUvxY2g4qBqiEMBavJfGJ6rPA7YrLqOOv0ZYujZmNO&X-Amz-Signature=a06c4a69ac4e42a4b4bb7c35184eb8c2145820b226d8668152ad960ea5fb1bba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXNFVYR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDckymUmfASbCzTQ4ge7o7%2Bmq4br9N56BntUGQrp96NYwIhAKm2zunIidNuYHZmySH9yVw2ltHv7d77XJRWw%2FzEU7ipKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcPshNcctPJzW8a%2BIq3AOdOud6KOtOftQKSpJ9dRsIQs%2Fuu62mOrLEllEwOgU5nGjY6IEqn1TQE6E1V8VEjoBeuuu2l1rcQjx%2Bf5KLjFuyY8EntckHH83yZFXE4rBIfjeZzpKWRQew9nM8saSR4gHcRyFv%2B8QohwlV36han7F4FyA8k5JE9VBXGll9CsM8UWwRthwZbrz2pMbwFmClXmzwRLH%2BqDEq2BrdQ%2BDL5NP8%2B7z4lFCKtZelFX864oajfB%2BR%2BNY4bdsOPBkVHpJOlKlJg6Y%2FTqo0lx7%2BivmN5lzi6JRDw1XaxXecdYMUN6nE5vmO7M89Woe6jenXpdTHGfsIaqRRF%2FEw5DaaiOrYCqn%2B4aQubkmL%2F9mWJh7VuR8c%2F2%2BCL991nBNKItJqFMnU9MLbOQkTnmWqY6l0oRECfLW6%2BWaNh2tJ8As5h99EbuKQMMhNG54h5ZsH84W1o6V4XYYqoreS7C1SL%2FqagejBoEGMjAlYd6HFRA74AmQvKLlFE5bD8pCRMpCABZWolMBtj%2BRF9yBMZBaOaZ2U8Nbm28WcX8UtIqrxkp%2BfGy%2FIpWliKy%2BQyoJsL4FQlrrQC6hiyCXQiNEsEf%2B%2BHC6TNfppBOOapch9PZ31yxQO62ZGiqqDYOfl6nqWKdH2yo4ugjCQtvK8BjqkAYhfNLeBy%2BRJ4T3xd%2BlpnQ7CZZeR4SGfGRnrqsYdtJzJKXBc9sM%2FeLC%2BOoacQk29n6B838qPwVfg9Zrusxa9zvgqTJojtJnlq2w9Nfm7EviE7ptAF%2B17v6OnhPoiok69FbUKyeAP0T%2Bsikx%2Bq3CCfyYc4iWH1OyVbHolLDB8ae02YQ22R5VooGcLDoa4ijwYZkd8xLJQP4PBQy%2FGK88Kp6wxBAMw&X-Amz-Signature=0398e61c8090ed8601264837316e91234772dc61bd0b1f4b3b10bb73c05df8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXNFVYR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDckymUmfASbCzTQ4ge7o7%2Bmq4br9N56BntUGQrp96NYwIhAKm2zunIidNuYHZmySH9yVw2ltHv7d77XJRWw%2FzEU7ipKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcPshNcctPJzW8a%2BIq3AOdOud6KOtOftQKSpJ9dRsIQs%2Fuu62mOrLEllEwOgU5nGjY6IEqn1TQE6E1V8VEjoBeuuu2l1rcQjx%2Bf5KLjFuyY8EntckHH83yZFXE4rBIfjeZzpKWRQew9nM8saSR4gHcRyFv%2B8QohwlV36han7F4FyA8k5JE9VBXGll9CsM8UWwRthwZbrz2pMbwFmClXmzwRLH%2BqDEq2BrdQ%2BDL5NP8%2B7z4lFCKtZelFX864oajfB%2BR%2BNY4bdsOPBkVHpJOlKlJg6Y%2FTqo0lx7%2BivmN5lzi6JRDw1XaxXecdYMUN6nE5vmO7M89Woe6jenXpdTHGfsIaqRRF%2FEw5DaaiOrYCqn%2B4aQubkmL%2F9mWJh7VuR8c%2F2%2BCL991nBNKItJqFMnU9MLbOQkTnmWqY6l0oRECfLW6%2BWaNh2tJ8As5h99EbuKQMMhNG54h5ZsH84W1o6V4XYYqoreS7C1SL%2FqagejBoEGMjAlYd6HFRA74AmQvKLlFE5bD8pCRMpCABZWolMBtj%2BRF9yBMZBaOaZ2U8Nbm28WcX8UtIqrxkp%2BfGy%2FIpWliKy%2BQyoJsL4FQlrrQC6hiyCXQiNEsEf%2B%2BHC6TNfppBOOapch9PZ31yxQO62ZGiqqDYOfl6nqWKdH2yo4ugjCQtvK8BjqkAYhfNLeBy%2BRJ4T3xd%2BlpnQ7CZZeR4SGfGRnrqsYdtJzJKXBc9sM%2FeLC%2BOoacQk29n6B838qPwVfg9Zrusxa9zvgqTJojtJnlq2w9Nfm7EviE7ptAF%2B17v6OnhPoiok69FbUKyeAP0T%2Bsikx%2Bq3CCfyYc4iWH1OyVbHolLDB8ae02YQ22R5VooGcLDoa4ijwYZkd8xLJQP4PBQy%2FGK88Kp6wxBAMw&X-Amz-Signature=ca78d2412b20c2853fcbb20504b6a45f0553dc22c786682c43cac960d6e9ddcc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXNFVYR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDckymUmfASbCzTQ4ge7o7%2Bmq4br9N56BntUGQrp96NYwIhAKm2zunIidNuYHZmySH9yVw2ltHv7d77XJRWw%2FzEU7ipKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcPshNcctPJzW8a%2BIq3AOdOud6KOtOftQKSpJ9dRsIQs%2Fuu62mOrLEllEwOgU5nGjY6IEqn1TQE6E1V8VEjoBeuuu2l1rcQjx%2Bf5KLjFuyY8EntckHH83yZFXE4rBIfjeZzpKWRQew9nM8saSR4gHcRyFv%2B8QohwlV36han7F4FyA8k5JE9VBXGll9CsM8UWwRthwZbrz2pMbwFmClXmzwRLH%2BqDEq2BrdQ%2BDL5NP8%2B7z4lFCKtZelFX864oajfB%2BR%2BNY4bdsOPBkVHpJOlKlJg6Y%2FTqo0lx7%2BivmN5lzi6JRDw1XaxXecdYMUN6nE5vmO7M89Woe6jenXpdTHGfsIaqRRF%2FEw5DaaiOrYCqn%2B4aQubkmL%2F9mWJh7VuR8c%2F2%2BCL991nBNKItJqFMnU9MLbOQkTnmWqY6l0oRECfLW6%2BWaNh2tJ8As5h99EbuKQMMhNG54h5ZsH84W1o6V4XYYqoreS7C1SL%2FqagejBoEGMjAlYd6HFRA74AmQvKLlFE5bD8pCRMpCABZWolMBtj%2BRF9yBMZBaOaZ2U8Nbm28WcX8UtIqrxkp%2BfGy%2FIpWliKy%2BQyoJsL4FQlrrQC6hiyCXQiNEsEf%2B%2BHC6TNfppBOOapch9PZ31yxQO62ZGiqqDYOfl6nqWKdH2yo4ugjCQtvK8BjqkAYhfNLeBy%2BRJ4T3xd%2BlpnQ7CZZeR4SGfGRnrqsYdtJzJKXBc9sM%2FeLC%2BOoacQk29n6B838qPwVfg9Zrusxa9zvgqTJojtJnlq2w9Nfm7EviE7ptAF%2B17v6OnhPoiok69FbUKyeAP0T%2Bsikx%2Bq3CCfyYc4iWH1OyVbHolLDB8ae02YQ22R5VooGcLDoa4ijwYZkd8xLJQP4PBQy%2FGK88Kp6wxBAMw&X-Amz-Signature=3b48368a72bcebef27d44f084f9fc63faf316a51b4c352a564cbd7d97c5ecb2d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXNFVYR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDckymUmfASbCzTQ4ge7o7%2Bmq4br9N56BntUGQrp96NYwIhAKm2zunIidNuYHZmySH9yVw2ltHv7d77XJRWw%2FzEU7ipKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcPshNcctPJzW8a%2BIq3AOdOud6KOtOftQKSpJ9dRsIQs%2Fuu62mOrLEllEwOgU5nGjY6IEqn1TQE6E1V8VEjoBeuuu2l1rcQjx%2Bf5KLjFuyY8EntckHH83yZFXE4rBIfjeZzpKWRQew9nM8saSR4gHcRyFv%2B8QohwlV36han7F4FyA8k5JE9VBXGll9CsM8UWwRthwZbrz2pMbwFmClXmzwRLH%2BqDEq2BrdQ%2BDL5NP8%2B7z4lFCKtZelFX864oajfB%2BR%2BNY4bdsOPBkVHpJOlKlJg6Y%2FTqo0lx7%2BivmN5lzi6JRDw1XaxXecdYMUN6nE5vmO7M89Woe6jenXpdTHGfsIaqRRF%2FEw5DaaiOrYCqn%2B4aQubkmL%2F9mWJh7VuR8c%2F2%2BCL991nBNKItJqFMnU9MLbOQkTnmWqY6l0oRECfLW6%2BWaNh2tJ8As5h99EbuKQMMhNG54h5ZsH84W1o6V4XYYqoreS7C1SL%2FqagejBoEGMjAlYd6HFRA74AmQvKLlFE5bD8pCRMpCABZWolMBtj%2BRF9yBMZBaOaZ2U8Nbm28WcX8UtIqrxkp%2BfGy%2FIpWliKy%2BQyoJsL4FQlrrQC6hiyCXQiNEsEf%2B%2BHC6TNfppBOOapch9PZ31yxQO62ZGiqqDYOfl6nqWKdH2yo4ugjCQtvK8BjqkAYhfNLeBy%2BRJ4T3xd%2BlpnQ7CZZeR4SGfGRnrqsYdtJzJKXBc9sM%2FeLC%2BOoacQk29n6B838qPwVfg9Zrusxa9zvgqTJojtJnlq2w9Nfm7EviE7ptAF%2B17v6OnhPoiok69FbUKyeAP0T%2Bsikx%2Bq3CCfyYc4iWH1OyVbHolLDB8ae02YQ22R5VooGcLDoa4ijwYZkd8xLJQP4PBQy%2FGK88Kp6wxBAMw&X-Amz-Signature=bde411ce7e1992b95526c907d8c05596f2b8468f34e0b06cded1a68c662c974a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W4JIUJX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvHBaotDA4O%2Fqx6QI2JfJJs39Z61nGBGIIANBKSaa1NQIgNdj4azNLPe5Cn0U2zlIOb4FbRf0yZjv7Edq7e5s%2FSyIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsnJ%2FBAf0%2F0l801HircA2qLAlMSmH9EeRxCPzmfuEr62cTjUDINiLkwWjvMc6ATSgSXZtK%2BdVmFcGFecTi0ysmYyrr8Rb9eX8jvrhvD%2FTeHZkw34aYf8uQM2S%2BEUNY5%2BDshGTi2CaRBXEUuRaQU%2FDwxPO2YXuHlFaAcvuYCWL2QmhpuWVUtRuvj2j%2FwInKmqXKIQ3qooLQBPDf5TMO1yh%2FaQQSWd4LdGd5kj%2BdF6Wl8DVgNwx5JrXKFDyhEYaBRZ4ZZIib3EXxkT1JezuJQWJgv3LTLhXlxt%2BPfu2gj7x8CIXxFyV7qSUh2Y5ShTS3BrAYraxmOcxtQKU52PaGHeYJN0CTqFu%2FTkJt9eV0kc%2F8YiGsCBu%2BcRF9JeBQMi1RhRAC85JQGXuuoadnho5vqpD4peI5aX5n13sM6tOu3iWZy%2BWH%2BjVrOkl%2Fim3IdleJVPUyslG8oVt%2Bi7lO5p6JFz%2F3WmOxPkbbxIAS0f95A2IA7DJ1EZaF07ESij0myDYBc09x0hzYvss70qwL2N8a3R%2F50BKfHzsj9Ly6ClTd%2B%2FHwCUuqcEgZE0415calB7a8Zi6xWa9dmlqBMrwfK0n3GydKaVeBfgDDmerZOe33Vkn8IzgeOG0DzW05NFsPLRdZCf3AT52YYLbqII92wMPC28rwGOqUBKO%2F3YmFp2gCas141fzRpdCiX1dTBFtBI%2Bxf0ATU7iIqf1Tz84EROcsNVnPjqwc%2BdAheGVe%2FwYAj5CG01w48cxWcIW%2FzLV2xUysdRAjJwd%2FTNP%2BxY%2BN11B4PXphvf1Wu8wLrQ0YznVkk5a95VnYae7HXEbJW9e%2FzPD06NkC91FEkwPkFaherkjKTMVNwNODz3EmKcpgIGqML1EhCPySp2r5x8r1%2Bz&X-Amz-Signature=394c071f5051d6bf27f5c285f3fe29db870bcb1d1a1be04dd1fd9cf7291fafee&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W4JIUJX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvHBaotDA4O%2Fqx6QI2JfJJs39Z61nGBGIIANBKSaa1NQIgNdj4azNLPe5Cn0U2zlIOb4FbRf0yZjv7Edq7e5s%2FSyIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsnJ%2FBAf0%2F0l801HircA2qLAlMSmH9EeRxCPzmfuEr62cTjUDINiLkwWjvMc6ATSgSXZtK%2BdVmFcGFecTi0ysmYyrr8Rb9eX8jvrhvD%2FTeHZkw34aYf8uQM2S%2BEUNY5%2BDshGTi2CaRBXEUuRaQU%2FDwxPO2YXuHlFaAcvuYCWL2QmhpuWVUtRuvj2j%2FwInKmqXKIQ3qooLQBPDf5TMO1yh%2FaQQSWd4LdGd5kj%2BdF6Wl8DVgNwx5JrXKFDyhEYaBRZ4ZZIib3EXxkT1JezuJQWJgv3LTLhXlxt%2BPfu2gj7x8CIXxFyV7qSUh2Y5ShTS3BrAYraxmOcxtQKU52PaGHeYJN0CTqFu%2FTkJt9eV0kc%2F8YiGsCBu%2BcRF9JeBQMi1RhRAC85JQGXuuoadnho5vqpD4peI5aX5n13sM6tOu3iWZy%2BWH%2BjVrOkl%2Fim3IdleJVPUyslG8oVt%2Bi7lO5p6JFz%2F3WmOxPkbbxIAS0f95A2IA7DJ1EZaF07ESij0myDYBc09x0hzYvss70qwL2N8a3R%2F50BKfHzsj9Ly6ClTd%2B%2FHwCUuqcEgZE0415calB7a8Zi6xWa9dmlqBMrwfK0n3GydKaVeBfgDDmerZOe33Vkn8IzgeOG0DzW05NFsPLRdZCf3AT52YYLbqII92wMPC28rwGOqUBKO%2F3YmFp2gCas141fzRpdCiX1dTBFtBI%2Bxf0ATU7iIqf1Tz84EROcsNVnPjqwc%2BdAheGVe%2FwYAj5CG01w48cxWcIW%2FzLV2xUysdRAjJwd%2FTNP%2BxY%2BN11B4PXphvf1Wu8wLrQ0YznVkk5a95VnYae7HXEbJW9e%2FzPD06NkC91FEkwPkFaherkjKTMVNwNODz3EmKcpgIGqML1EhCPySp2r5x8r1%2Bz&X-Amz-Signature=b3d2d0d9fe74014345e29afc5a0d738aae627789661c9170324d94b55523bdd3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W4JIUJX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvHBaotDA4O%2Fqx6QI2JfJJs39Z61nGBGIIANBKSaa1NQIgNdj4azNLPe5Cn0U2zlIOb4FbRf0yZjv7Edq7e5s%2FSyIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsnJ%2FBAf0%2F0l801HircA2qLAlMSmH9EeRxCPzmfuEr62cTjUDINiLkwWjvMc6ATSgSXZtK%2BdVmFcGFecTi0ysmYyrr8Rb9eX8jvrhvD%2FTeHZkw34aYf8uQM2S%2BEUNY5%2BDshGTi2CaRBXEUuRaQU%2FDwxPO2YXuHlFaAcvuYCWL2QmhpuWVUtRuvj2j%2FwInKmqXKIQ3qooLQBPDf5TMO1yh%2FaQQSWd4LdGd5kj%2BdF6Wl8DVgNwx5JrXKFDyhEYaBRZ4ZZIib3EXxkT1JezuJQWJgv3LTLhXlxt%2BPfu2gj7x8CIXxFyV7qSUh2Y5ShTS3BrAYraxmOcxtQKU52PaGHeYJN0CTqFu%2FTkJt9eV0kc%2F8YiGsCBu%2BcRF9JeBQMi1RhRAC85JQGXuuoadnho5vqpD4peI5aX5n13sM6tOu3iWZy%2BWH%2BjVrOkl%2Fim3IdleJVPUyslG8oVt%2Bi7lO5p6JFz%2F3WmOxPkbbxIAS0f95A2IA7DJ1EZaF07ESij0myDYBc09x0hzYvss70qwL2N8a3R%2F50BKfHzsj9Ly6ClTd%2B%2FHwCUuqcEgZE0415calB7a8Zi6xWa9dmlqBMrwfK0n3GydKaVeBfgDDmerZOe33Vkn8IzgeOG0DzW05NFsPLRdZCf3AT52YYLbqII92wMPC28rwGOqUBKO%2F3YmFp2gCas141fzRpdCiX1dTBFtBI%2Bxf0ATU7iIqf1Tz84EROcsNVnPjqwc%2BdAheGVe%2FwYAj5CG01w48cxWcIW%2FzLV2xUysdRAjJwd%2FTNP%2BxY%2BN11B4PXphvf1Wu8wLrQ0YznVkk5a95VnYae7HXEbJW9e%2FzPD06NkC91FEkwPkFaherkjKTMVNwNODz3EmKcpgIGqML1EhCPySp2r5x8r1%2Bz&X-Amz-Signature=9e931cd0e6d10b9ae1b808d29d5ec4df38f195ee6670689f17a501a2e03bdb8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

