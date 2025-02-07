

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=43e87f83349d70c8b5dd30f3d5f41261361aee793942c7aaae4e4a500ea30558&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=ab0adb7197a36172d504a49d3a9bc94731c89124c6fb773201b032aa2d009d5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=7725cffd00cf620148aa1c5801820b51c56461d5c0f2f9b658e637c085b1fc1e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=967982b552718a8d2f1d6e0fe273193f2b62290f93fa0848185e871ff0275e4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=ae9c43bf077bb13606f810114e816603e0fd0f2d8897f3672b6ec46e2591e242&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=5cc46d3315f6570981288eec5ad77225353841ca428af762d4ec7db120413d66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=88168950cf477a502c84c2bec1f8ecccb2b6d4d906712b7cf357346d9c52f97f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=77fd7ea5760eec8bff0c5971c4422743c4cd0ec56b4f15a65979659d947e1f25&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=3f3dff747376f77b479cd418fcd2e8c8e032c8d486307835d7126ec3ee21c311&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=1d3461d7b63099ba2d8f2806800eb099c75e88139e185e05cc58d18c1a6c8483&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKL2K7DG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDGJSWblj85d4RPEavsICIyb70ea7%2BvNxIO5%2BgveZXmpAiEAhFdOmTY%2FOiy0aarQDnLMr4H%2FM%2Bw7N1FF8xlHiTCRspQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGS3eZzO3L%2BH6w%2BcUyrcA59%2F181ITMoH82NbWzAcgUuDOgePTGVsS8vWj23fUGTgDP%2Fw3I6q3%2FrnnODEGad0I%2BQ1%2FEJUCGMmS3QbbcxSTAfoskDzoFEz%2BB11x0%2FyWRJ1E3M5iDbNwVrmvG8TjhGAsywQhHL8lAb%2FmuHqaK6OcyQian%2FhCxc43%2FwQ6hYKNr61LKG3IRgPDThSkEu%2B1TG8f6br49889LRzzKQWTcj0xyW9iF%2B%2FI9qr0AXLo%2BHVYL7UVHCxJFADRIe1Pq8STrXhbpVAt54ya5NP9Nis6pgVi8%2FtNwek%2FXTgZw8mOp7s5qRRaKTChBeKYI4i0tbP7k0UjYBd5VGwA%2BJ12EWlDFs863Dr9ZbjejFzi90eapXiROn%2BeDw80zIv%2BspFA53n%2BOxC6u69dqYLaPw7CFNGeZOpWO%2FovaAnD1flutcmym%2F9b8Ss3OlIAdFiF8JIbTV53nXY1J4HI%2FcUqnnHjkilL6iVcZ6b37iTGMrYOZIndji3nD57%2FcN2SH98Ra9pGtDauKoqg8FUwpcu8yrtOHMPfScwpw62euqWBmBw%2FprAfF0IAEoOZYl%2BiTEuy0JIPhoLw84snEuDvh5RDOro3%2FfwfEV8c2wiR%2B3p%2F7jHlnza6MDU9TJ9tMwm2eZ%2BMkOKoTG3MNWZmb0GOqUB7sElHqBmPLRYLCdY%2BQWg7hHCFEElAk7UCl3aCMQHeezIbSE%2FY5IipuMX48PoBSqnUig9UwgriW5OaIyGr%2BoKv9I39oXEdDzGsnUZNFBRJTUSx3lyThjC1KuYJNx7%2Fiy5mxC%2BB7lwkzEmd6Yg%2FHFg%2FRcUoRnZGR0Hznf6aMl24xSC5Je5KBREaa8FM5o%2FLkDlZaRExDbav26RrtFOF4AE32edqiFI&X-Amz-Signature=24a0c0a76a80ea302547e339451fccb69f3cf213003dec1f9b26712ae611fa2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFR6DUH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFUb1Sn45L2s0AuvwbgtOaHKe1ts6jbAnxJoZphH1uhcAiEAloYFl23u3TV8m%2FcDtQZwevB74cbpkdnBTYM5%2FWQA7Noq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMIslebPqyafCcNDFircA5PNgverPa9t34mcsHDstEReLVThgcRn7nBqnWJmnvwBThXALJa1vwNGKYiZ6EzhJ0hCSPZlos7eOUIXzvaGdTmg3HmoZOHelBKU8cmJFWP%2BLwvgsAK%2Ft02A2OoGZbVkEP1XRxanj%2BkaAY4WNo6DwqezBnWGTmdhulN1Bxpp6cB9H7xQQIDpd9jtppZf6ZanElKUXelfh3umVCtSH7O4PQRWW5AIuV4NRGVgSfCUT7fhDot%2FYHCr4KzPV7NnLyJTvRtqyxUDNhwUXnV08uZwWIQJMLCTUKJwPUhxR3dII%2FKb9HaxohPjaWuZpgv7up5eIoMD43Qx8Z8ch4xiBqU4Wk27F1BtFo0LQUZthPjqp3%2BQ9OxD2S2GAr0L1v%2BgSJ%2BRhQVeMWtGAetPiFP3Y2fil%2Fz3IedepVlORjcpVucgHNrTP6%2FGpARkX4a1Q3FC%2FzL8mOGlOUFzuwEyTqpn36fqHPfXxPjblhHYhQ%2F8%2FZF7MTk0Jx1469IfV106YNQgS%2FCaTRiTCe%2FVcNRWuumcq4rVHM%2FpDmToJT3lZiKlZX1RpDvwvZOjybKEZ3H%2Bep1cONs0zZpUgEGMSwaGDRhtOJSwe9VfBmiakSedwc0CtoYIV%2Fxt8OtMjd%2B7Qu8KQ%2B%2BJMPGZmb0GOqUB8KqcqMj7LWa81jln1ABJgP9mChObb6qJuS0tkRvys7R5WGQsWRU2u0Qxu6cYrMQPbXT%2B9ivTU8RshAzGCXNx69xKUNiHBS6Pm2bhC%2BpH6JJXgkRjk6vwHqzfQJzy%2BlZlY%2FZbbtKPPC9z2IDr678OaqXs%2BmC9LBmYsoEm2C0UVIrF3HLeyYy6KXXmm8ffEOesAPZORMYzmuD8jWfeXI61n0f8UwHE&X-Amz-Signature=0937b6b8c1b328e4ceea12f8c549bdb80368e71459f7dfff1d4eca8354682c89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFR6DUH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFUb1Sn45L2s0AuvwbgtOaHKe1ts6jbAnxJoZphH1uhcAiEAloYFl23u3TV8m%2FcDtQZwevB74cbpkdnBTYM5%2FWQA7Noq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMIslebPqyafCcNDFircA5PNgverPa9t34mcsHDstEReLVThgcRn7nBqnWJmnvwBThXALJa1vwNGKYiZ6EzhJ0hCSPZlos7eOUIXzvaGdTmg3HmoZOHelBKU8cmJFWP%2BLwvgsAK%2Ft02A2OoGZbVkEP1XRxanj%2BkaAY4WNo6DwqezBnWGTmdhulN1Bxpp6cB9H7xQQIDpd9jtppZf6ZanElKUXelfh3umVCtSH7O4PQRWW5AIuV4NRGVgSfCUT7fhDot%2FYHCr4KzPV7NnLyJTvRtqyxUDNhwUXnV08uZwWIQJMLCTUKJwPUhxR3dII%2FKb9HaxohPjaWuZpgv7up5eIoMD43Qx8Z8ch4xiBqU4Wk27F1BtFo0LQUZthPjqp3%2BQ9OxD2S2GAr0L1v%2BgSJ%2BRhQVeMWtGAetPiFP3Y2fil%2Fz3IedepVlORjcpVucgHNrTP6%2FGpARkX4a1Q3FC%2FzL8mOGlOUFzuwEyTqpn36fqHPfXxPjblhHYhQ%2F8%2FZF7MTk0Jx1469IfV106YNQgS%2FCaTRiTCe%2FVcNRWuumcq4rVHM%2FpDmToJT3lZiKlZX1RpDvwvZOjybKEZ3H%2Bep1cONs0zZpUgEGMSwaGDRhtOJSwe9VfBmiakSedwc0CtoYIV%2Fxt8OtMjd%2B7Qu8KQ%2B%2BJMPGZmb0GOqUB8KqcqMj7LWa81jln1ABJgP9mChObb6qJuS0tkRvys7R5WGQsWRU2u0Qxu6cYrMQPbXT%2B9ivTU8RshAzGCXNx69xKUNiHBS6Pm2bhC%2BpH6JJXgkRjk6vwHqzfQJzy%2BlZlY%2FZbbtKPPC9z2IDr678OaqXs%2BmC9LBmYsoEm2C0UVIrF3HLeyYy6KXXmm8ffEOesAPZORMYzmuD8jWfeXI61n0f8UwHE&X-Amz-Signature=f1a2373d24017fc0bafb245245ef3b1cc5d068beb658f2295ceffa5d78c91ea4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFR6DUH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFUb1Sn45L2s0AuvwbgtOaHKe1ts6jbAnxJoZphH1uhcAiEAloYFl23u3TV8m%2FcDtQZwevB74cbpkdnBTYM5%2FWQA7Noq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMIslebPqyafCcNDFircA5PNgverPa9t34mcsHDstEReLVThgcRn7nBqnWJmnvwBThXALJa1vwNGKYiZ6EzhJ0hCSPZlos7eOUIXzvaGdTmg3HmoZOHelBKU8cmJFWP%2BLwvgsAK%2Ft02A2OoGZbVkEP1XRxanj%2BkaAY4WNo6DwqezBnWGTmdhulN1Bxpp6cB9H7xQQIDpd9jtppZf6ZanElKUXelfh3umVCtSH7O4PQRWW5AIuV4NRGVgSfCUT7fhDot%2FYHCr4KzPV7NnLyJTvRtqyxUDNhwUXnV08uZwWIQJMLCTUKJwPUhxR3dII%2FKb9HaxohPjaWuZpgv7up5eIoMD43Qx8Z8ch4xiBqU4Wk27F1BtFo0LQUZthPjqp3%2BQ9OxD2S2GAr0L1v%2BgSJ%2BRhQVeMWtGAetPiFP3Y2fil%2Fz3IedepVlORjcpVucgHNrTP6%2FGpARkX4a1Q3FC%2FzL8mOGlOUFzuwEyTqpn36fqHPfXxPjblhHYhQ%2F8%2FZF7MTk0Jx1469IfV106YNQgS%2FCaTRiTCe%2FVcNRWuumcq4rVHM%2FpDmToJT3lZiKlZX1RpDvwvZOjybKEZ3H%2Bep1cONs0zZpUgEGMSwaGDRhtOJSwe9VfBmiakSedwc0CtoYIV%2Fxt8OtMjd%2B7Qu8KQ%2B%2BJMPGZmb0GOqUB8KqcqMj7LWa81jln1ABJgP9mChObb6qJuS0tkRvys7R5WGQsWRU2u0Qxu6cYrMQPbXT%2B9ivTU8RshAzGCXNx69xKUNiHBS6Pm2bhC%2BpH6JJXgkRjk6vwHqzfQJzy%2BlZlY%2FZbbtKPPC9z2IDr678OaqXs%2BmC9LBmYsoEm2C0UVIrF3HLeyYy6KXXmm8ffEOesAPZORMYzmuD8jWfeXI61n0f8UwHE&X-Amz-Signature=8eb67774cfc2da9df13d347aac17be046e75d600debc2fd77052d48658b3348c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFR6DUH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFUb1Sn45L2s0AuvwbgtOaHKe1ts6jbAnxJoZphH1uhcAiEAloYFl23u3TV8m%2FcDtQZwevB74cbpkdnBTYM5%2FWQA7Noq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMIslebPqyafCcNDFircA5PNgverPa9t34mcsHDstEReLVThgcRn7nBqnWJmnvwBThXALJa1vwNGKYiZ6EzhJ0hCSPZlos7eOUIXzvaGdTmg3HmoZOHelBKU8cmJFWP%2BLwvgsAK%2Ft02A2OoGZbVkEP1XRxanj%2BkaAY4WNo6DwqezBnWGTmdhulN1Bxpp6cB9H7xQQIDpd9jtppZf6ZanElKUXelfh3umVCtSH7O4PQRWW5AIuV4NRGVgSfCUT7fhDot%2FYHCr4KzPV7NnLyJTvRtqyxUDNhwUXnV08uZwWIQJMLCTUKJwPUhxR3dII%2FKb9HaxohPjaWuZpgv7up5eIoMD43Qx8Z8ch4xiBqU4Wk27F1BtFo0LQUZthPjqp3%2BQ9OxD2S2GAr0L1v%2BgSJ%2BRhQVeMWtGAetPiFP3Y2fil%2Fz3IedepVlORjcpVucgHNrTP6%2FGpARkX4a1Q3FC%2FzL8mOGlOUFzuwEyTqpn36fqHPfXxPjblhHYhQ%2F8%2FZF7MTk0Jx1469IfV106YNQgS%2FCaTRiTCe%2FVcNRWuumcq4rVHM%2FpDmToJT3lZiKlZX1RpDvwvZOjybKEZ3H%2Bep1cONs0zZpUgEGMSwaGDRhtOJSwe9VfBmiakSedwc0CtoYIV%2Fxt8OtMjd%2B7Qu8KQ%2B%2BJMPGZmb0GOqUB8KqcqMj7LWa81jln1ABJgP9mChObb6qJuS0tkRvys7R5WGQsWRU2u0Qxu6cYrMQPbXT%2B9ivTU8RshAzGCXNx69xKUNiHBS6Pm2bhC%2BpH6JJXgkRjk6vwHqzfQJzy%2BlZlY%2FZbbtKPPC9z2IDr678OaqXs%2BmC9LBmYsoEm2C0UVIrF3HLeyYy6KXXmm8ffEOesAPZORMYzmuD8jWfeXI61n0f8UwHE&X-Amz-Signature=30caeae23193c53b95c2791e3a1f15fbe124c54243bcccfeeb84f9331c4a2764&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ROZZ2ZL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC4y30L8tm8JUI15oUrosigfNuZYP4bYPcTf0JfiZjXqQIgK4CswKNfVj2Q%2FcwhPQggapPJlrorxh46vyjiQrpYsB4q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNkv77CKhYHz5GrYSSrcA9Ny7AUW%2FKx7sDwT6vCcpsV19fOLX0XYdBMAvl0bI449%2F9PkUkOnXpDN2zSklXtAgAcq7UuWrWFx1JjA5RRjH6IJgrJ8ZWxHKSd4Bdd6YIMjVOLzN41soO1GZat5knXy9P%2B2PENCjC935oqreVa268gYJIS9lLJJEmGCEa6rEBlL23o%2Be2m%2Bkv04TLTbtQzdIX1wRaDV4kA8N%2BlzOSnlE7MqOV4EST8DH3d9QZl6z%2BU5sGL%2BI%2FVEMdFjkESY%2BhooZhpbmXZEWFTLNdJG1pWzcMTScZNRB3Wl%2F%2BzKY8QYtDEX9E6K893kZ9hL%2Fcq3Fg%2FfUpvBvl48oRa6d05dTYAOgs1qJJTGeqHS%2FIwwBQi%2FJVOHHD%2FWbzoSPJIrwAJBwBs6dBnMwN4WbmqPggdzkx3utamQpnwUIX7P%2BX8QOstrNhLhcoOzMEyS%2FAbcd2cFo5okWsj%2BUDRYDbfY0dWmzHhUsZ5IMyv3q%2BhRARVg403eaDU5cGggtu43ove%2ByS%2BAit5NMSPB7YxjGO%2FCpkfY9KkgrJzFxYqEeABS3bvNR1SE6BLag6IwjZJnf2Jvv5Kc0CbWJ1%2FXAS6mQbvtdpX%2Bosuw2zhRl10ZpeB1DNj0j4bps43XwZo9QyHWrXmzVVSrMMOZmb0GOqUBZLXtKUTBiaPKiDFbW3xPvyZE1%2FZOvDGxgWQUH5HHkZsRgja6%2FULjvxj1uHydvq5a05z8Xu%2F4FDVpuA8mNMGvoES6mgZwhkCOgfh2MjEIr4FLBmbO1DARJJhUs%2FzJiiClo%2FLAQ1B%2FOZtmCV0%2BpDzhtF7i0qjUVQNomrdzmvcv8wY3ND7z7332fEWj0PxuiUFMtuH4aYBPqeoqzyIDYOGZTR4tLMkL&X-Amz-Signature=9e07e6c25376bba660400c9f9e883002edc292b4856663fe0fb310bd49177fff&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ROZZ2ZL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC4y30L8tm8JUI15oUrosigfNuZYP4bYPcTf0JfiZjXqQIgK4CswKNfVj2Q%2FcwhPQggapPJlrorxh46vyjiQrpYsB4q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNkv77CKhYHz5GrYSSrcA9Ny7AUW%2FKx7sDwT6vCcpsV19fOLX0XYdBMAvl0bI449%2F9PkUkOnXpDN2zSklXtAgAcq7UuWrWFx1JjA5RRjH6IJgrJ8ZWxHKSd4Bdd6YIMjVOLzN41soO1GZat5knXy9P%2B2PENCjC935oqreVa268gYJIS9lLJJEmGCEa6rEBlL23o%2Be2m%2Bkv04TLTbtQzdIX1wRaDV4kA8N%2BlzOSnlE7MqOV4EST8DH3d9QZl6z%2BU5sGL%2BI%2FVEMdFjkESY%2BhooZhpbmXZEWFTLNdJG1pWzcMTScZNRB3Wl%2F%2BzKY8QYtDEX9E6K893kZ9hL%2Fcq3Fg%2FfUpvBvl48oRa6d05dTYAOgs1qJJTGeqHS%2FIwwBQi%2FJVOHHD%2FWbzoSPJIrwAJBwBs6dBnMwN4WbmqPggdzkx3utamQpnwUIX7P%2BX8QOstrNhLhcoOzMEyS%2FAbcd2cFo5okWsj%2BUDRYDbfY0dWmzHhUsZ5IMyv3q%2BhRARVg403eaDU5cGggtu43ove%2ByS%2BAit5NMSPB7YxjGO%2FCpkfY9KkgrJzFxYqEeABS3bvNR1SE6BLag6IwjZJnf2Jvv5Kc0CbWJ1%2FXAS6mQbvtdpX%2Bosuw2zhRl10ZpeB1DNj0j4bps43XwZo9QyHWrXmzVVSrMMOZmb0GOqUBZLXtKUTBiaPKiDFbW3xPvyZE1%2FZOvDGxgWQUH5HHkZsRgja6%2FULjvxj1uHydvq5a05z8Xu%2F4FDVpuA8mNMGvoES6mgZwhkCOgfh2MjEIr4FLBmbO1DARJJhUs%2FzJiiClo%2FLAQ1B%2FOZtmCV0%2BpDzhtF7i0qjUVQNomrdzmvcv8wY3ND7z7332fEWj0PxuiUFMtuH4aYBPqeoqzyIDYOGZTR4tLMkL&X-Amz-Signature=a831e9ec475cdf0562ddcfd3ae940319d3bbf27ba5d90d8632a66b1c5c68b689&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ROZZ2ZL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC4y30L8tm8JUI15oUrosigfNuZYP4bYPcTf0JfiZjXqQIgK4CswKNfVj2Q%2FcwhPQggapPJlrorxh46vyjiQrpYsB4q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNkv77CKhYHz5GrYSSrcA9Ny7AUW%2FKx7sDwT6vCcpsV19fOLX0XYdBMAvl0bI449%2F9PkUkOnXpDN2zSklXtAgAcq7UuWrWFx1JjA5RRjH6IJgrJ8ZWxHKSd4Bdd6YIMjVOLzN41soO1GZat5knXy9P%2B2PENCjC935oqreVa268gYJIS9lLJJEmGCEa6rEBlL23o%2Be2m%2Bkv04TLTbtQzdIX1wRaDV4kA8N%2BlzOSnlE7MqOV4EST8DH3d9QZl6z%2BU5sGL%2BI%2FVEMdFjkESY%2BhooZhpbmXZEWFTLNdJG1pWzcMTScZNRB3Wl%2F%2BzKY8QYtDEX9E6K893kZ9hL%2Fcq3Fg%2FfUpvBvl48oRa6d05dTYAOgs1qJJTGeqHS%2FIwwBQi%2FJVOHHD%2FWbzoSPJIrwAJBwBs6dBnMwN4WbmqPggdzkx3utamQpnwUIX7P%2BX8QOstrNhLhcoOzMEyS%2FAbcd2cFo5okWsj%2BUDRYDbfY0dWmzHhUsZ5IMyv3q%2BhRARVg403eaDU5cGggtu43ove%2ByS%2BAit5NMSPB7YxjGO%2FCpkfY9KkgrJzFxYqEeABS3bvNR1SE6BLag6IwjZJnf2Jvv5Kc0CbWJ1%2FXAS6mQbvtdpX%2Bosuw2zhRl10ZpeB1DNj0j4bps43XwZo9QyHWrXmzVVSrMMOZmb0GOqUBZLXtKUTBiaPKiDFbW3xPvyZE1%2FZOvDGxgWQUH5HHkZsRgja6%2FULjvxj1uHydvq5a05z8Xu%2F4FDVpuA8mNMGvoES6mgZwhkCOgfh2MjEIr4FLBmbO1DARJJhUs%2FzJiiClo%2FLAQ1B%2FOZtmCV0%2BpDzhtF7i0qjUVQNomrdzmvcv8wY3ND7z7332fEWj0PxuiUFMtuH4aYBPqeoqzyIDYOGZTR4tLMkL&X-Amz-Signature=30f133751623de890fd5026c133552a1ced0f982a65e19f09f8d0e69d6da59fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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

