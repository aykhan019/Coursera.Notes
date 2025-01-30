

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=7bb4a62c95f87994e36b3f062c15047e95f9db3bc163262c450f7324b0e0d284&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=81ba0001d2a028c1a80e4c0c0798a22f224d0f90d3edace5351ae2e5b7e56dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=8a7e4aac3ccc9c3dbc793337c39457acd327d94fe45e7ee8517f8a3bc51a1fa0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=358153343939611721d678e155c43f415d40f234267cc1d87295c654a55f7a49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=9f6b8efa2e9f24202a2dfeff7386e7aa796e334ed5d11696de162adbea10d10a&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=34ba1d965484a38993a560c36b9a879e079c6aa291609f71d9b794fcf6b228dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=449037c0464ae76fee18f643f15eb3d35ea56a309c63cb9e34f317dcf2560123&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=c5af391208b872bb781561161960ea7746da9498a46db9b44698eb2a92f44676&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=f8ae1c22aa98809894fe315afb331a51b3e6cfc0d28c57bfeb47718af2fed9c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=2f6e741f17596fc872610e31c3123ddbcac6a32f1701edadc022a245197f8b92&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJT7OPPK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe9nToEZNJm2GZu6HOGvY42z3sNFOLsyFdivsNy1DHKAiBQBMF1wguEolMo4Qj%2BrfEtR5%2F1hOnouSCUblh%2FUxJQFCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbPW0mbpl%2F7oEqq7KKtwD7vAH5n8X%2FxW8CpA%2FKhOM8%2F0okwAt7PeFqQvTU32A%2BlBlbqkwhnCiqIJ35gsP6HVMOQY2%2BGVlE14wtvBbMPtzJkmG2M7ffTKP9HxsfB0UTlNbvzxMq06ukomM3DeWDlfcm3%2FDTq8P3Rz0ajKsBL2XBA9IjZw1xD1d628asfFFs5yNDbopzK8coLnscGI5f7RR1eeEKZ%2BJcgwj2Fe8vi5iD2%2FP0Z1LMz037SmMlKAuTKM1Tqm1aZdpx4hZYsTEfNd2nNQzrynhC2KePZNPru0p0FS4QnJU4nrQOFnG2NlkaF7JcCBWUdsGAl6MG9rvAmYpOv7ZDMxUckHedvT3bQEW37Sc0rd8WVk82So19LPvk%2F4Igqv%2BOmce2iYe2603qWK%2BwRKyLMoAMrvPfe9tWDf1LDOLHIL1PC81wnFupOtpEU8wajjK2UIW1JPH7C%2BEIhj%2Bdsb7zUUIB24nJJWfmHyZELhXmdKhBX52egz0vaOYPOSXBPQSeGT5pdci%2BTMYktEXiuNpBT1wIsdRwSdd3aX8lVURuJINq19BEae4ysPkM8DndYBEr9M4T2HQaFfBYf6RwlvkrY4LZnzHCVeKKaqanAqKX3uoWDxXUwcpTU2PNcEJuONdUutbsgIX%2FcEwlIfsvAY6pgFi1dIkak%2FVt34qov%2B2aUYG8OTXXnbFQbW1zUf5DeN3cMAEmIpWVnZ%2BfmYpNmxJgDEMoycsbLY7EaZvVzghTnpBJWmLCVYDhHb%2BbPBC2Ym7BQtZKn2fgOx0Gvi%2FzIcPAZwaxqmx7AifTB98ETSkIL%2Bs0w1K57F5SpLW90C1U6c9wu%2BUAG1B%2Fiaa%2FtliQbSOB23v4lVmtDJrd8nGwOP9Gpp3dC0cZKVC&X-Amz-Signature=3838af3e5086b0bf28530e397ed53d005d25c0fbd3c8725414a947e1666585d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6SLIU6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2M%2BYnZeADSjyVS0Xz%2FA76I1yOJGJKNTX9b6cFgtaCjAIgfrCoFrKkvJuZLXBi%2FpeRlnRwIvlJ0jaco61%2BuPTBJMAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfQxTUgSyOHHPdMfyrcA9LBP2Bg2PkOVxM0iH3V2JwReSDFXOwNvt6TDXO8NR9zvr95b0JQHGB894cuPAmBgofu%2BWWbecNuRkng1BBJ2nIlOJ1KzPmKuQROuHfm5gnm8K%2BS5yUlhvvJMGGxMm8XOwMcTgeaDMPEpdF%2Fuy%2FOyUw8yVxm%2F3dPrgb%2F5dwPjJjpWw5o9dT884zPX3%2BNOD7V4ajQya%2FukuyIadG3PAUDI4PzL1glR%2FoQI7bT3wrghtitNv0RCXvqkmNPlA0iZw%2FLYtM0vcWR6k2fQJvkzGfLxA6EVtn%2B4bjZmq8XeyPQ5R4P4GtqFiYPWWy43p9BaHMny0KM9wS%2FRM3GCGv4SBb%2BJM3msXbMyfCHNrkCtDZzmejHqZvEUO8WuDZvgGZubCZT5WEfwmCI38cUnHLczovAygxTnCBYCWbeOkM6hT024D16uk4AO4v4sqYjSdblPE17iL%2BHdAFbq8YA0B39C7K7ezrejirjwSaseaY7DNbdW64XcYggZJDgzRmuZ0LuTzg%2BS748aa8zfnEq51xPvI4IHyiOJGH2JtNcoSZ7lZwAsbLbqMaSmT8hGfRVC5%2FuRpKKMjSfplxh%2F%2FZeG5pOiamVw9DfObGLRgS82reE%2BjDSzm5t5x2qXXHfNS1azkn0MMOG7LwGOqUB%2Fk50VSF%2Fv561WtkUyolcLFVEfWdQx7vXIjYkx9PhmgxhZ4dRuCtfp0%2BgOLPiOVAM3RwaszL2C7cRtOZ%2Fp5tQoV32s99dj1rXthQgBh%2Fu4Otf%2FNYVbv4Z5U%2FMbXLyobCccR5GXg3KlYc%2FyIWNNEwaBbsrnPkRIZabPHWeBJlPY4U%2BUTeP4ujsar0tjsxxd5x2T5fjzadjb7PWPnnlXu%2BgC%2BPYEmjg&X-Amz-Signature=5ff769aa08e7cfa235fcdb57c2fb172d4ccbd7a2c3e58b24fa977a203a86917d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6SLIU6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2M%2BYnZeADSjyVS0Xz%2FA76I1yOJGJKNTX9b6cFgtaCjAIgfrCoFrKkvJuZLXBi%2FpeRlnRwIvlJ0jaco61%2BuPTBJMAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfQxTUgSyOHHPdMfyrcA9LBP2Bg2PkOVxM0iH3V2JwReSDFXOwNvt6TDXO8NR9zvr95b0JQHGB894cuPAmBgofu%2BWWbecNuRkng1BBJ2nIlOJ1KzPmKuQROuHfm5gnm8K%2BS5yUlhvvJMGGxMm8XOwMcTgeaDMPEpdF%2Fuy%2FOyUw8yVxm%2F3dPrgb%2F5dwPjJjpWw5o9dT884zPX3%2BNOD7V4ajQya%2FukuyIadG3PAUDI4PzL1glR%2FoQI7bT3wrghtitNv0RCXvqkmNPlA0iZw%2FLYtM0vcWR6k2fQJvkzGfLxA6EVtn%2B4bjZmq8XeyPQ5R4P4GtqFiYPWWy43p9BaHMny0KM9wS%2FRM3GCGv4SBb%2BJM3msXbMyfCHNrkCtDZzmejHqZvEUO8WuDZvgGZubCZT5WEfwmCI38cUnHLczovAygxTnCBYCWbeOkM6hT024D16uk4AO4v4sqYjSdblPE17iL%2BHdAFbq8YA0B39C7K7ezrejirjwSaseaY7DNbdW64XcYggZJDgzRmuZ0LuTzg%2BS748aa8zfnEq51xPvI4IHyiOJGH2JtNcoSZ7lZwAsbLbqMaSmT8hGfRVC5%2FuRpKKMjSfplxh%2F%2FZeG5pOiamVw9DfObGLRgS82reE%2BjDSzm5t5x2qXXHfNS1azkn0MMOG7LwGOqUB%2Fk50VSF%2Fv561WtkUyolcLFVEfWdQx7vXIjYkx9PhmgxhZ4dRuCtfp0%2BgOLPiOVAM3RwaszL2C7cRtOZ%2Fp5tQoV32s99dj1rXthQgBh%2Fu4Otf%2FNYVbv4Z5U%2FMbXLyobCccR5GXg3KlYc%2FyIWNNEwaBbsrnPkRIZabPHWeBJlPY4U%2BUTeP4ujsar0tjsxxd5x2T5fjzadjb7PWPnnlXu%2BgC%2BPYEmjg&X-Amz-Signature=8b3a1e7752f9128d395838a38e8718ac5b9d45deb597b7a82584837749ccdbd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6SLIU6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2M%2BYnZeADSjyVS0Xz%2FA76I1yOJGJKNTX9b6cFgtaCjAIgfrCoFrKkvJuZLXBi%2FpeRlnRwIvlJ0jaco61%2BuPTBJMAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfQxTUgSyOHHPdMfyrcA9LBP2Bg2PkOVxM0iH3V2JwReSDFXOwNvt6TDXO8NR9zvr95b0JQHGB894cuPAmBgofu%2BWWbecNuRkng1BBJ2nIlOJ1KzPmKuQROuHfm5gnm8K%2BS5yUlhvvJMGGxMm8XOwMcTgeaDMPEpdF%2Fuy%2FOyUw8yVxm%2F3dPrgb%2F5dwPjJjpWw5o9dT884zPX3%2BNOD7V4ajQya%2FukuyIadG3PAUDI4PzL1glR%2FoQI7bT3wrghtitNv0RCXvqkmNPlA0iZw%2FLYtM0vcWR6k2fQJvkzGfLxA6EVtn%2B4bjZmq8XeyPQ5R4P4GtqFiYPWWy43p9BaHMny0KM9wS%2FRM3GCGv4SBb%2BJM3msXbMyfCHNrkCtDZzmejHqZvEUO8WuDZvgGZubCZT5WEfwmCI38cUnHLczovAygxTnCBYCWbeOkM6hT024D16uk4AO4v4sqYjSdblPE17iL%2BHdAFbq8YA0B39C7K7ezrejirjwSaseaY7DNbdW64XcYggZJDgzRmuZ0LuTzg%2BS748aa8zfnEq51xPvI4IHyiOJGH2JtNcoSZ7lZwAsbLbqMaSmT8hGfRVC5%2FuRpKKMjSfplxh%2F%2FZeG5pOiamVw9DfObGLRgS82reE%2BjDSzm5t5x2qXXHfNS1azkn0MMOG7LwGOqUB%2Fk50VSF%2Fv561WtkUyolcLFVEfWdQx7vXIjYkx9PhmgxhZ4dRuCtfp0%2BgOLPiOVAM3RwaszL2C7cRtOZ%2Fp5tQoV32s99dj1rXthQgBh%2Fu4Otf%2FNYVbv4Z5U%2FMbXLyobCccR5GXg3KlYc%2FyIWNNEwaBbsrnPkRIZabPHWeBJlPY4U%2BUTeP4ujsar0tjsxxd5x2T5fjzadjb7PWPnnlXu%2BgC%2BPYEmjg&X-Amz-Signature=d2d8f2e17bacd81de90d72a52a7d386becc54a9249e3cec8670b54d238de1894&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6SLIU6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2M%2BYnZeADSjyVS0Xz%2FA76I1yOJGJKNTX9b6cFgtaCjAIgfrCoFrKkvJuZLXBi%2FpeRlnRwIvlJ0jaco61%2BuPTBJMAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfQxTUgSyOHHPdMfyrcA9LBP2Bg2PkOVxM0iH3V2JwReSDFXOwNvt6TDXO8NR9zvr95b0JQHGB894cuPAmBgofu%2BWWbecNuRkng1BBJ2nIlOJ1KzPmKuQROuHfm5gnm8K%2BS5yUlhvvJMGGxMm8XOwMcTgeaDMPEpdF%2Fuy%2FOyUw8yVxm%2F3dPrgb%2F5dwPjJjpWw5o9dT884zPX3%2BNOD7V4ajQya%2FukuyIadG3PAUDI4PzL1glR%2FoQI7bT3wrghtitNv0RCXvqkmNPlA0iZw%2FLYtM0vcWR6k2fQJvkzGfLxA6EVtn%2B4bjZmq8XeyPQ5R4P4GtqFiYPWWy43p9BaHMny0KM9wS%2FRM3GCGv4SBb%2BJM3msXbMyfCHNrkCtDZzmejHqZvEUO8WuDZvgGZubCZT5WEfwmCI38cUnHLczovAygxTnCBYCWbeOkM6hT024D16uk4AO4v4sqYjSdblPE17iL%2BHdAFbq8YA0B39C7K7ezrejirjwSaseaY7DNbdW64XcYggZJDgzRmuZ0LuTzg%2BS748aa8zfnEq51xPvI4IHyiOJGH2JtNcoSZ7lZwAsbLbqMaSmT8hGfRVC5%2FuRpKKMjSfplxh%2F%2FZeG5pOiamVw9DfObGLRgS82reE%2BjDSzm5t5x2qXXHfNS1azkn0MMOG7LwGOqUB%2Fk50VSF%2Fv561WtkUyolcLFVEfWdQx7vXIjYkx9PhmgxhZ4dRuCtfp0%2BgOLPiOVAM3RwaszL2C7cRtOZ%2Fp5tQoV32s99dj1rXthQgBh%2Fu4Otf%2FNYVbv4Z5U%2FMbXLyobCccR5GXg3KlYc%2FyIWNNEwaBbsrnPkRIZabPHWeBJlPY4U%2BUTeP4ujsar0tjsxxd5x2T5fjzadjb7PWPnnlXu%2BgC%2BPYEmjg&X-Amz-Signature=412a3623474a36bf55409c0a6e388d3cd293b167bc9fa5a3b9fccdf598c756ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PUCZAX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFsyaIDlcH%2BmD1j73MsglIhztuE2YfSaHv2%2FAheWm0XAiAB5wtR3uH6Q8P%2BYuPNkSm9Q4bVlZdk9qFuQHHDaxEmniqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUyLeNJ0Gowgqh88KtwDrqvYVcBUtWTQbSeId93PM%2BfVsLrc%2BH8zsFRjCG5QTinPuQ536sJ5qR2nna0koFJBOpJ%2BR0tRGZEawjnd6XwHW3IQSFjkK9lBsd%2BFZHOWZe0AR3%2FTlLN%2F72FBsMvdmhAPe1W8SS7drVYd5z3K%2Bw4LiY0QhFHtJSkimvc0TWp6bfrRCiEjHzVg1Jz8s0SNH7gdA%2BTzCMeSjX1tX%2By%2F00TmfI3uQ0SIcgnS1WxI8LWXs5BJ4350iBjkQ%2Bkf%2Fgwf1HDPAPgmIgsSoXn45frrYc30ItKOZlczz2ag98Xx8lPsxKLhzRbJW1UfFG%2B2PIbI32tLL1e1NSXQLwdzXFRZrcHh%2FmA5q45MNwBVr%2FsKI6KOa10035uSASXc0jwDE4K5w4uVNTt4vOK9Zdl24n%2FT4CgBkwijjNtnyeABL%2BJXj0N5K05tSFjbVcYEHs8WjOS3QYjbEUuZndQZuBgBrqOB%2FfUwEiCLQyzXX3mnEoymDnrw8tcneEmleMcJNLiMBZBMd0OjUwos3yW85LlhMBPQ81L%2Bg%2F1auKCbqPwJdbMxove%2FjRt3iiwJMgaWl4N1afNJ2Dq6%2Fp1ixAFvJqe%2BZRKzSbdut3OlX%2BAC2ZaEIz8FAyc434TAyzD4rxR1z3PVEWUwlIfsvAY6pgErH57WJaAudF5LV%2BogIVMkEYr3mcy6%2F%2FCXVtwlP2svJ0pHV9%2BKUuImqv6C5bxZePjnDmms4AMDon%2FwiCZYzFtx2WQ3exHeu9Ia7OB8gE71sKvqwfJaYTpGydeW7gPxyAQN8OXkSHyIxaQvhPXAkBdcL3RowZOOndIrzilmhbjqVKSgjQGLfKSpJ7zQxOcub4CLJD0IgvqEhlo0tneWq6FBlQEa5Rhn&X-Amz-Signature=7e74f59cb6133aa1e9414036ea6d0e46191614906d31114b474e01ef05c5ea8f&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PUCZAX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFsyaIDlcH%2BmD1j73MsglIhztuE2YfSaHv2%2FAheWm0XAiAB5wtR3uH6Q8P%2BYuPNkSm9Q4bVlZdk9qFuQHHDaxEmniqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUyLeNJ0Gowgqh88KtwDrqvYVcBUtWTQbSeId93PM%2BfVsLrc%2BH8zsFRjCG5QTinPuQ536sJ5qR2nna0koFJBOpJ%2BR0tRGZEawjnd6XwHW3IQSFjkK9lBsd%2BFZHOWZe0AR3%2FTlLN%2F72FBsMvdmhAPe1W8SS7drVYd5z3K%2Bw4LiY0QhFHtJSkimvc0TWp6bfrRCiEjHzVg1Jz8s0SNH7gdA%2BTzCMeSjX1tX%2By%2F00TmfI3uQ0SIcgnS1WxI8LWXs5BJ4350iBjkQ%2Bkf%2Fgwf1HDPAPgmIgsSoXn45frrYc30ItKOZlczz2ag98Xx8lPsxKLhzRbJW1UfFG%2B2PIbI32tLL1e1NSXQLwdzXFRZrcHh%2FmA5q45MNwBVr%2FsKI6KOa10035uSASXc0jwDE4K5w4uVNTt4vOK9Zdl24n%2FT4CgBkwijjNtnyeABL%2BJXj0N5K05tSFjbVcYEHs8WjOS3QYjbEUuZndQZuBgBrqOB%2FfUwEiCLQyzXX3mnEoymDnrw8tcneEmleMcJNLiMBZBMd0OjUwos3yW85LlhMBPQ81L%2Bg%2F1auKCbqPwJdbMxove%2FjRt3iiwJMgaWl4N1afNJ2Dq6%2Fp1ixAFvJqe%2BZRKzSbdut3OlX%2BAC2ZaEIz8FAyc434TAyzD4rxR1z3PVEWUwlIfsvAY6pgErH57WJaAudF5LV%2BogIVMkEYr3mcy6%2F%2FCXVtwlP2svJ0pHV9%2BKUuImqv6C5bxZePjnDmms4AMDon%2FwiCZYzFtx2WQ3exHeu9Ia7OB8gE71sKvqwfJaYTpGydeW7gPxyAQN8OXkSHyIxaQvhPXAkBdcL3RowZOOndIrzilmhbjqVKSgjQGLfKSpJ7zQxOcub4CLJD0IgvqEhlo0tneWq6FBlQEa5Rhn&X-Amz-Signature=e2bd10fd0d6946def900636e7b026da8e511eaeb532cd13d500c14147cf1e96a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PUCZAX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFsyaIDlcH%2BmD1j73MsglIhztuE2YfSaHv2%2FAheWm0XAiAB5wtR3uH6Q8P%2BYuPNkSm9Q4bVlZdk9qFuQHHDaxEmniqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUyLeNJ0Gowgqh88KtwDrqvYVcBUtWTQbSeId93PM%2BfVsLrc%2BH8zsFRjCG5QTinPuQ536sJ5qR2nna0koFJBOpJ%2BR0tRGZEawjnd6XwHW3IQSFjkK9lBsd%2BFZHOWZe0AR3%2FTlLN%2F72FBsMvdmhAPe1W8SS7drVYd5z3K%2Bw4LiY0QhFHtJSkimvc0TWp6bfrRCiEjHzVg1Jz8s0SNH7gdA%2BTzCMeSjX1tX%2By%2F00TmfI3uQ0SIcgnS1WxI8LWXs5BJ4350iBjkQ%2Bkf%2Fgwf1HDPAPgmIgsSoXn45frrYc30ItKOZlczz2ag98Xx8lPsxKLhzRbJW1UfFG%2B2PIbI32tLL1e1NSXQLwdzXFRZrcHh%2FmA5q45MNwBVr%2FsKI6KOa10035uSASXc0jwDE4K5w4uVNTt4vOK9Zdl24n%2FT4CgBkwijjNtnyeABL%2BJXj0N5K05tSFjbVcYEHs8WjOS3QYjbEUuZndQZuBgBrqOB%2FfUwEiCLQyzXX3mnEoymDnrw8tcneEmleMcJNLiMBZBMd0OjUwos3yW85LlhMBPQ81L%2Bg%2F1auKCbqPwJdbMxove%2FjRt3iiwJMgaWl4N1afNJ2Dq6%2Fp1ixAFvJqe%2BZRKzSbdut3OlX%2BAC2ZaEIz8FAyc434TAyzD4rxR1z3PVEWUwlIfsvAY6pgErH57WJaAudF5LV%2BogIVMkEYr3mcy6%2F%2FCXVtwlP2svJ0pHV9%2BKUuImqv6C5bxZePjnDmms4AMDon%2FwiCZYzFtx2WQ3exHeu9Ia7OB8gE71sKvqwfJaYTpGydeW7gPxyAQN8OXkSHyIxaQvhPXAkBdcL3RowZOOndIrzilmhbjqVKSgjQGLfKSpJ7zQxOcub4CLJD0IgvqEhlo0tneWq6FBlQEa5Rhn&X-Amz-Signature=08a2bdb4af26f500fb1c20b3478de8dd8135149ad2eaf08cad1d6895333b8cbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

