

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=50bdad6f6cad2aee83dbc0d146f353f3550a04040ec96355e0fd39eb098f9351&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=5af92781bb5c32a16d074b602c46083bc93718800b75a6b1ad246c4c3a3d0f50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=dc8c2fcf5efce05cb6dd92ed6e41fe4a355a01772eef2d68350dfadac03c7925&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=4095a56a8be20e46b910797bafa0986db8b0864b7ec7d88b14f57c6a7089cb34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=f78ab02098b7f26d7d1c1b837e77b442071074f81d8740cbc572c070ba60bda1&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=4aa529e7aca2b50b08ae4c97167b6b3ee8ed480789dc7670afe1f6660d11c323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=af62faaa53f38835840bf99e1e2badd0f24cbe43204d95f19dbfc1fa173301e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=9c6202913ef7f0a2661cac3901639fa04ae867da641e5624df90182bdd9886df&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=0dc57abe7044bb5cf0a690c70d9727b5caa2c5e2729ba502d85730be93a18970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=951df755728397d0268561ae0e90c7315d2a990d1bea98be8a4ae71c2d036f12&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQLQNW3%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9MaoYrjOXfs%2Fdg6m6JZZP8Xlds29foJ91uX65GnGffAiEAhyIQsa5IPZQRnceYGWwtFj1bEhM59KkEQWV4NgWzl5gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIzpVRibiOoOhC%2BBCrcA8Z9rnzMPKPvCzOjEZehn9Iatkho7LI7mv7RhB0wvNG4pcMsMG4LeXH2A9gbrMldoQbtwBJtsvicGSe66k44zqQHKghXgpvI5LtFza9CZXtU5jhKSY%2FxMguy9CrZl4J6V8x9j%2Fr2cp6VsQtvqDFjtGWDf3O7IZ6audG5hGVMVTNTX6S%2FGycJ01Xy9yNdBBLB3Lp8rxCkj0moaCpYCjr5z8spEB6OsD8pu%2BoSXcrTkiSgpp%2B%2B51KsNhHGdZQb3%2BqXyAKMo%2FG3haVTI5sD%2FF41Dj7ZBhIu9Emmgk1luqbg3MahPyXfsjxcI1mw1%2Fjm0Zfzq6JesILcAvP3f7etiFLuEYUd0LJ4uEdzhbAnqIACNejqznFjQ7yaA9LfKD135dZmawlmfv0LVe8Jdi74MGctzYbpIEBH4JmJHFaciSeHhEGTsJXgNM8oJMG792SmkPXz6k%2BaxQnVKJhdsA9fmQb78iIz1zUAg59HNsR%2FWJ%2BcWTG3HKSrbYI%2FAzIJSURXOvf%2FUqa3kIU1KaY%2BQhjkfLx5J80jFAFzv74AmGzSnSO1910Rq8DL%2FuAqJzt95Yno15t1MHJh6JgeWOk6v4R2%2BsV10nSM0z1vhYuyv3cpYhir6QfOP9nfbsATcEyRVtHkMIWr6b0GOqUBxXEwNkifi%2FSoHoKaS7wyNs6u1cUGZEU3AjFfKI8OvDIpEN9Ko%2Bg7Pdz%2FxN1%2Fjj7Wh14psQeu3cZlIOifxeaRIpWn3BfbmzxRbZtVkrmPRLwysirjDrTszQ230fonMqswcIfZG1Vy7Ddo4Akxemk6AxZMMb6e5apyuaKnbCxN0yScYJ%2FnnPZMteX7SUnmLZYNFXbmrgf6LnHIJtgQjFdiCGTm3rDK&X-Amz-Signature=d5cca039fb64aa255c9f5ffdd9e31cbbb1faf13eacb6e6a8c17f714c0414b887&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIEPPE5X%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BbWw95t%2BCZMABkOzJJdNJ%2FR9%2BEqjyRM7%2F5zK4AxOYvAiBXyCdUVP9IKxOXtl%2BHSvT3XZe2IN9RoqNe5YBzB4hCwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEm7KVpMD3XJ%2FiNrpKtwDqMcjnyv9%2FnYYwcA9ID87KcMDs7LnJg8oMKwTbVmYxbIfJnYMmV6gQ5HKdxx6FdO3VhY4GaPgTjrnQLIPdNb%2F6X9Bmvn0cYQ3EdJe4klsiu2w0BY%2FidMCuUXhgLVJT4MtTWciGg26z7XuUrq1%2B%2BDCt7%2BHpqrRWC1XOf%2BMOVrYGV3KEYi5ufmLoeQq55%2BaeITE9QeP1TOVC5esOz3qiSXaUww56rVSclCusCITuHrl6jymDHeuY5Bnj8Y7dqTynKdKKduiHmY2fv9z5zPWgwy5LBgR9zID3aZUuoneXQMdBUTeVYqAOQv1Wsa%2B92w5aC3PzW%2B82msMpeOK2ctwexHw2JtLzBg4pJtvJ4642922oV%2BsvBLvGmUeYTBxd%2Bau8%2FisQjsRG9CLj%2BgFoaWPcScstyzWencwXOhOz4jLHvdOIlF7wGYsCjtktW6LZXXgzKmL5OlcMuQdLmT30Ig4nspT9pmgzKAlJ9j0A6yqzL%2BgnFu8WjMdl%2Bb2G8t38DPjL13CSLwU2YEu%2Ffi68agnoItBO9LR3hDqNOTxl%2FHGY7j0zp6Rrt%2F7IHNubsaZQ4dHVgpWnbnNbRHMBaqVO77BD%2FAF99WbHxbyIWBNdY0UneONdRJc%2FhFC6OK5ghYqQLAwk6XpvQY6pgH0dhkxwXS9X%2BgYNlrr8R0cjww0LyvubWxMSA6KocoHxHuVwe4IdvB3%2FjFrIm36%2BYL7C9o%2Bpdm6f9ebzill9TtiY9n3UWX5kxmABx3xO2p0uyq%2FLJPXzeAE1OTsHOT%2F0%2BvYpook0j3FZQfsemxy4plDRdxcf%2BFJ2bl2ZMl1gXV9I2vgOj2m9ZkAXKIm7hMj7A5UHI3jOftJRpxJi3D8fXVy0V4aCF%2FM&X-Amz-Signature=0c031a30cf718b7315ffe1f0798ecb6ba5cf759943198fb8d1e29ea3c4ed4da4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIEPPE5X%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BbWw95t%2BCZMABkOzJJdNJ%2FR9%2BEqjyRM7%2F5zK4AxOYvAiBXyCdUVP9IKxOXtl%2BHSvT3XZe2IN9RoqNe5YBzB4hCwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEm7KVpMD3XJ%2FiNrpKtwDqMcjnyv9%2FnYYwcA9ID87KcMDs7LnJg8oMKwTbVmYxbIfJnYMmV6gQ5HKdxx6FdO3VhY4GaPgTjrnQLIPdNb%2F6X9Bmvn0cYQ3EdJe4klsiu2w0BY%2FidMCuUXhgLVJT4MtTWciGg26z7XuUrq1%2B%2BDCt7%2BHpqrRWC1XOf%2BMOVrYGV3KEYi5ufmLoeQq55%2BaeITE9QeP1TOVC5esOz3qiSXaUww56rVSclCusCITuHrl6jymDHeuY5Bnj8Y7dqTynKdKKduiHmY2fv9z5zPWgwy5LBgR9zID3aZUuoneXQMdBUTeVYqAOQv1Wsa%2B92w5aC3PzW%2B82msMpeOK2ctwexHw2JtLzBg4pJtvJ4642922oV%2BsvBLvGmUeYTBxd%2Bau8%2FisQjsRG9CLj%2BgFoaWPcScstyzWencwXOhOz4jLHvdOIlF7wGYsCjtktW6LZXXgzKmL5OlcMuQdLmT30Ig4nspT9pmgzKAlJ9j0A6yqzL%2BgnFu8WjMdl%2Bb2G8t38DPjL13CSLwU2YEu%2Ffi68agnoItBO9LR3hDqNOTxl%2FHGY7j0zp6Rrt%2F7IHNubsaZQ4dHVgpWnbnNbRHMBaqVO77BD%2FAF99WbHxbyIWBNdY0UneONdRJc%2FhFC6OK5ghYqQLAwk6XpvQY6pgH0dhkxwXS9X%2BgYNlrr8R0cjww0LyvubWxMSA6KocoHxHuVwe4IdvB3%2FjFrIm36%2BYL7C9o%2Bpdm6f9ebzill9TtiY9n3UWX5kxmABx3xO2p0uyq%2FLJPXzeAE1OTsHOT%2F0%2BvYpook0j3FZQfsemxy4plDRdxcf%2BFJ2bl2ZMl1gXV9I2vgOj2m9ZkAXKIm7hMj7A5UHI3jOftJRpxJi3D8fXVy0V4aCF%2FM&X-Amz-Signature=5e34c6d00fd427ff7ca7ca7705d1ee9f57219babbaebb48a0e5910963b538312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIEPPE5X%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BbWw95t%2BCZMABkOzJJdNJ%2FR9%2BEqjyRM7%2F5zK4AxOYvAiBXyCdUVP9IKxOXtl%2BHSvT3XZe2IN9RoqNe5YBzB4hCwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEm7KVpMD3XJ%2FiNrpKtwDqMcjnyv9%2FnYYwcA9ID87KcMDs7LnJg8oMKwTbVmYxbIfJnYMmV6gQ5HKdxx6FdO3VhY4GaPgTjrnQLIPdNb%2F6X9Bmvn0cYQ3EdJe4klsiu2w0BY%2FidMCuUXhgLVJT4MtTWciGg26z7XuUrq1%2B%2BDCt7%2BHpqrRWC1XOf%2BMOVrYGV3KEYi5ufmLoeQq55%2BaeITE9QeP1TOVC5esOz3qiSXaUww56rVSclCusCITuHrl6jymDHeuY5Bnj8Y7dqTynKdKKduiHmY2fv9z5zPWgwy5LBgR9zID3aZUuoneXQMdBUTeVYqAOQv1Wsa%2B92w5aC3PzW%2B82msMpeOK2ctwexHw2JtLzBg4pJtvJ4642922oV%2BsvBLvGmUeYTBxd%2Bau8%2FisQjsRG9CLj%2BgFoaWPcScstyzWencwXOhOz4jLHvdOIlF7wGYsCjtktW6LZXXgzKmL5OlcMuQdLmT30Ig4nspT9pmgzKAlJ9j0A6yqzL%2BgnFu8WjMdl%2Bb2G8t38DPjL13CSLwU2YEu%2Ffi68agnoItBO9LR3hDqNOTxl%2FHGY7j0zp6Rrt%2F7IHNubsaZQ4dHVgpWnbnNbRHMBaqVO77BD%2FAF99WbHxbyIWBNdY0UneONdRJc%2FhFC6OK5ghYqQLAwk6XpvQY6pgH0dhkxwXS9X%2BgYNlrr8R0cjww0LyvubWxMSA6KocoHxHuVwe4IdvB3%2FjFrIm36%2BYL7C9o%2Bpdm6f9ebzill9TtiY9n3UWX5kxmABx3xO2p0uyq%2FLJPXzeAE1OTsHOT%2F0%2BvYpook0j3FZQfsemxy4plDRdxcf%2BFJ2bl2ZMl1gXV9I2vgOj2m9ZkAXKIm7hMj7A5UHI3jOftJRpxJi3D8fXVy0V4aCF%2FM&X-Amz-Signature=02c2325f22d88fc449804646db51b4d375a21ebec0d2acd570931832f4401008&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIEPPE5X%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BbWw95t%2BCZMABkOzJJdNJ%2FR9%2BEqjyRM7%2F5zK4AxOYvAiBXyCdUVP9IKxOXtl%2BHSvT3XZe2IN9RoqNe5YBzB4hCwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEm7KVpMD3XJ%2FiNrpKtwDqMcjnyv9%2FnYYwcA9ID87KcMDs7LnJg8oMKwTbVmYxbIfJnYMmV6gQ5HKdxx6FdO3VhY4GaPgTjrnQLIPdNb%2F6X9Bmvn0cYQ3EdJe4klsiu2w0BY%2FidMCuUXhgLVJT4MtTWciGg26z7XuUrq1%2B%2BDCt7%2BHpqrRWC1XOf%2BMOVrYGV3KEYi5ufmLoeQq55%2BaeITE9QeP1TOVC5esOz3qiSXaUww56rVSclCusCITuHrl6jymDHeuY5Bnj8Y7dqTynKdKKduiHmY2fv9z5zPWgwy5LBgR9zID3aZUuoneXQMdBUTeVYqAOQv1Wsa%2B92w5aC3PzW%2B82msMpeOK2ctwexHw2JtLzBg4pJtvJ4642922oV%2BsvBLvGmUeYTBxd%2Bau8%2FisQjsRG9CLj%2BgFoaWPcScstyzWencwXOhOz4jLHvdOIlF7wGYsCjtktW6LZXXgzKmL5OlcMuQdLmT30Ig4nspT9pmgzKAlJ9j0A6yqzL%2BgnFu8WjMdl%2Bb2G8t38DPjL13CSLwU2YEu%2Ffi68agnoItBO9LR3hDqNOTxl%2FHGY7j0zp6Rrt%2F7IHNubsaZQ4dHVgpWnbnNbRHMBaqVO77BD%2FAF99WbHxbyIWBNdY0UneONdRJc%2FhFC6OK5ghYqQLAwk6XpvQY6pgH0dhkxwXS9X%2BgYNlrr8R0cjww0LyvubWxMSA6KocoHxHuVwe4IdvB3%2FjFrIm36%2BYL7C9o%2Bpdm6f9ebzill9TtiY9n3UWX5kxmABx3xO2p0uyq%2FLJPXzeAE1OTsHOT%2F0%2BvYpook0j3FZQfsemxy4plDRdxcf%2BFJ2bl2ZMl1gXV9I2vgOj2m9ZkAXKIm7hMj7A5UHI3jOftJRpxJi3D8fXVy0V4aCF%2FM&X-Amz-Signature=620fbf82436da2824adb4ec12989e66d5596e46b546d0d67f27f95cd28f28480&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RVHLGQ4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICh6bYzLjKIomZUU9QMji5SluuwJe460AKLXy9Qv%2Fp1AAiEA2RzUKQ%2BApH2qk%2FnLfIJKbzsRaPMcKvhzGL%2BjMCOOkJIqiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDZZ0cBT8B2OpRF63ircAxv%2FXTKzBWXR7L6DpwoEfOYuA32sZxemIhE54l34gFkBvufW8MWKKmxzYEqe4etoNIvFNkbcTQ3s3R6Ui1vnUDVSqmfTEisNN0IIFfM3AXQCpPQOLLlp6UxWTl3aeYo2PBB6Ic%2FgeIJm39cNsG0bM8YP7%2F6STMAYoNRVtcNSObzxzRrF%2FrlJvOmMnHjUzgqpCmTC0C44ZYMYdXlgpd52ZnUPWk6LER282ygJ0xK7iAbjWyZrwAjoD3fWLf2XJVUqNo1Yx%2Fl62%2BHDupEZz18FG8xhJyBIssZEoHxf0gCpYrsQo9uX68%2BrIKINKL0eLBZcCb%2BzZhryHtYp%2BrfW1Oy0oQwwfCGG407z6XL%2F%2BZmGCUEYV14IKsJZFT%2FBj%2BXAxOa4HGXayq5ujJpBMo9MMGsG4bJZ%2BrZgpNySBdJJrJ4Y1kgF5u2qNUxKGXuRsURZWsJSPpv%2FOkQtKiKQXcb5wssvQCRAje9YvIeiCHzFbY03N6VmYVau6aOVy7f83buPyKNcq0PNs4h9qKfAaS%2BhjGENXdW%2F%2B15cftCyaywhOw891jXRhXJ69OBst2qqQWWybX0c%2BDPPcQyRdiu%2Bc%2Bw72Los4UGVKEPk7Zw6rU6%2BjyYSQjz0ZaObjQ1BKnnLHZq2MIvQ6b0GOqUB%2F7Vbzyy1m1dAFDHIS527Opud%2FAomNvXxODkjQUb4vMssxiEdGavSgqWz89SzbUFvoQDlsIH%2B1y50hhrD0hQqE61B329yJStM%2BnG47YXkAwpunIonGJZLLhuJzlFdHflNC77wLxs1vZQ9w9RSD%2FrwOyw5wySnm%2B3CMCy0ZFcZ3TgmgVOn1K626S%2BJEApJB7hbt4uH1NiaJqkcvCkatwjSoc7eZuID&X-Amz-Signature=ea365fa8513af5c4d9ae380468a77320f73c1750df3bb53b942aa99b0f48fdc0&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RVHLGQ4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICh6bYzLjKIomZUU9QMji5SluuwJe460AKLXy9Qv%2Fp1AAiEA2RzUKQ%2BApH2qk%2FnLfIJKbzsRaPMcKvhzGL%2BjMCOOkJIqiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDZZ0cBT8B2OpRF63ircAxv%2FXTKzBWXR7L6DpwoEfOYuA32sZxemIhE54l34gFkBvufW8MWKKmxzYEqe4etoNIvFNkbcTQ3s3R6Ui1vnUDVSqmfTEisNN0IIFfM3AXQCpPQOLLlp6UxWTl3aeYo2PBB6Ic%2FgeIJm39cNsG0bM8YP7%2F6STMAYoNRVtcNSObzxzRrF%2FrlJvOmMnHjUzgqpCmTC0C44ZYMYdXlgpd52ZnUPWk6LER282ygJ0xK7iAbjWyZrwAjoD3fWLf2XJVUqNo1Yx%2Fl62%2BHDupEZz18FG8xhJyBIssZEoHxf0gCpYrsQo9uX68%2BrIKINKL0eLBZcCb%2BzZhryHtYp%2BrfW1Oy0oQwwfCGG407z6XL%2F%2BZmGCUEYV14IKsJZFT%2FBj%2BXAxOa4HGXayq5ujJpBMo9MMGsG4bJZ%2BrZgpNySBdJJrJ4Y1kgF5u2qNUxKGXuRsURZWsJSPpv%2FOkQtKiKQXcb5wssvQCRAje9YvIeiCHzFbY03N6VmYVau6aOVy7f83buPyKNcq0PNs4h9qKfAaS%2BhjGENXdW%2F%2B15cftCyaywhOw891jXRhXJ69OBst2qqQWWybX0c%2BDPPcQyRdiu%2Bc%2Bw72Los4UGVKEPk7Zw6rU6%2BjyYSQjz0ZaObjQ1BKnnLHZq2MIvQ6b0GOqUB%2F7Vbzyy1m1dAFDHIS527Opud%2FAomNvXxODkjQUb4vMssxiEdGavSgqWz89SzbUFvoQDlsIH%2B1y50hhrD0hQqE61B329yJStM%2BnG47YXkAwpunIonGJZLLhuJzlFdHflNC77wLxs1vZQ9w9RSD%2FrwOyw5wySnm%2B3CMCy0ZFcZ3TgmgVOn1K626S%2BJEApJB7hbt4uH1NiaJqkcvCkatwjSoc7eZuID&X-Amz-Signature=9ea3df3ab0f10a1b22757b9ddd8a76d984d1669ccd30a50889f93cc7a6121881&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RVHLGQ4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICh6bYzLjKIomZUU9QMji5SluuwJe460AKLXy9Qv%2Fp1AAiEA2RzUKQ%2BApH2qk%2FnLfIJKbzsRaPMcKvhzGL%2BjMCOOkJIqiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDZZ0cBT8B2OpRF63ircAxv%2FXTKzBWXR7L6DpwoEfOYuA32sZxemIhE54l34gFkBvufW8MWKKmxzYEqe4etoNIvFNkbcTQ3s3R6Ui1vnUDVSqmfTEisNN0IIFfM3AXQCpPQOLLlp6UxWTl3aeYo2PBB6Ic%2FgeIJm39cNsG0bM8YP7%2F6STMAYoNRVtcNSObzxzRrF%2FrlJvOmMnHjUzgqpCmTC0C44ZYMYdXlgpd52ZnUPWk6LER282ygJ0xK7iAbjWyZrwAjoD3fWLf2XJVUqNo1Yx%2Fl62%2BHDupEZz18FG8xhJyBIssZEoHxf0gCpYrsQo9uX68%2BrIKINKL0eLBZcCb%2BzZhryHtYp%2BrfW1Oy0oQwwfCGG407z6XL%2F%2BZmGCUEYV14IKsJZFT%2FBj%2BXAxOa4HGXayq5ujJpBMo9MMGsG4bJZ%2BrZgpNySBdJJrJ4Y1kgF5u2qNUxKGXuRsURZWsJSPpv%2FOkQtKiKQXcb5wssvQCRAje9YvIeiCHzFbY03N6VmYVau6aOVy7f83buPyKNcq0PNs4h9qKfAaS%2BhjGENXdW%2F%2B15cftCyaywhOw891jXRhXJ69OBst2qqQWWybX0c%2BDPPcQyRdiu%2Bc%2Bw72Los4UGVKEPk7Zw6rU6%2BjyYSQjz0ZaObjQ1BKnnLHZq2MIvQ6b0GOqUB%2F7Vbzyy1m1dAFDHIS527Opud%2FAomNvXxODkjQUb4vMssxiEdGavSgqWz89SzbUFvoQDlsIH%2B1y50hhrD0hQqE61B329yJStM%2BnG47YXkAwpunIonGJZLLhuJzlFdHflNC77wLxs1vZQ9w9RSD%2FrwOyw5wySnm%2B3CMCy0ZFcZ3TgmgVOn1K626S%2BJEApJB7hbt4uH1NiaJqkcvCkatwjSoc7eZuID&X-Amz-Signature=e6906c5ee8357a931a9292403cd23435d1efba6a03ab8a880d924c9388253fb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

