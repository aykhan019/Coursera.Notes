

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=50c0c3d3cb23b212be669ac72b4ce7d56d31c5d4b24c5f6dcbd3cd6c41fda17d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=425ecc954d683d1ab644edb7ee92fc07eefbeec41160b1810be977343c165aab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=b62bce450e7d218004f9312dd484e92d885f3900eb44995b0fde52d478dc3935&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=c0d93c2367a992a322893cbfd7480a13ed8ada3562eb92f890333af58c5f0c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=42fba94b7914e7f8c2247472adea77cccab318e67ac040e7b14fa9191f41d65d&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=44fc5f28615c4db47b98dff8a386217775d1c9339f2e578bb1693c16b71c90f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=bb6070d6cf2b8d08b1e3d0ba033e9049650d0cbb644476027262988ef06e28e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=a61bf0c9d3a51cc5c7a5a2c8e1b070bc71a0e117ac9296453a28749b76de7e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=d2b44f42d8829000242d3437480b4feeb144c624b7c924294132691905a260dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=6fe88e99c91325abf35a54ac805885b4495d1fb2f928552f318aa5944c269b32&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PWHSKC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGAknsbVW9KKULMsm0sseC7yUbAOMPie4UjQMmy%2BY2kQIhAJC07qOvP0dnoNtQP%2FT5so1K6DuN7a04nZrTLZb9AKIMKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyhXYYInQKjIZXMMIQq3ANhsOvWM2MTLqFoTZACKaDzJwuhpe50fNaHLJ1NgDcaCXIFqNTowTEul2QuyHJOxIuSdpoHejb0IvyhVXijiHxFoiqa929mX9dUn9cqaASsfh5pxXIAJ3GejC1Wsswt%2F2zuSpF1PWbcGQUlyutrNV63iZQe7Pm0LOEbtZ9Zu1VuGXWFqf3Jy7rExIJ%2FnsgtbFqVgi1dvXPZIu3JJ7ImSXq5RroqJmh2kdnLe%2Fe1rREGiQ5EPU1IXLcFYYMt0MMNiEq3qUnW8pbwYTGPosiU1pNWmd75TG4yvhLeE93sd1VyL1dK5C1qxzFdeG%2FDrT2WpwtyP1fp5s8WG5ROmKLDun86Lap%2Fhf4BfZjEE7jc163c8Ox%2BwjyGXXWZQGI5d61r7qVQZqgqqFWF0FyMggHc7oBbDiR%2F2l9N5r9N9c2amfwbkgIjjee8U69fiEnUBR5xxMVPRpMbYcMeZdAHgvHW6SdvST4%2FsyMbCBn%2B6WusfoKDhXyTjzPVHi6fAQW4ZciXzpma%2FjaxzxNIgLOtknJFMTxWgl4UO9POtSFhfVey4wWSKMluadZbwMztuDRnD42gx%2Fx%2Fq4qSJLXBLTHRgu0%2Fj5ODh5VS2ldk7WFzfbi1HeDZU45ExQdYnGN2eorbCzDYwfa8BjqkAe6OU7q%2FZ02IsThNFtOoPXsr7GI6IURXJh6MfCpLaxwzPnV3yCtRJ3VJKNDF%2FyDKOeJUGg1xA%2FTR8XATapeGs3GLdyXQihZkVas0gRSerMz8ipBc3O8%2FY5XMxrNDn2vJj72o2qoB%2F3EvKdqPMaDchIRn4%2BGCAul%2BInWnzmfhlBl2z%2Bbn%2Fi4f2pIZ8yKfarq9zUYKjLgDIsltMQBQtfBwYp00k3q0&X-Amz-Signature=abc72288276616b82861aae7c6d0a748f4f86f626bc20c2c2458b8fc2f9682a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV2BSAZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEARbM1ttYQnAgsocBEbFuATSqu2uMcXcfQ%2FPylptvW8AiEAw1%2Fwf5llaA0FYojerfEsLSX11bM0SU9UyIhq9HhfiCYqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZo44SrugxvbIALlyrcA6%2Fffr5g%2B7FHnPCK%2F7VobcQMZdt4X084DE1XYWj5Wl99LTYFy%2F2Th6CTjth9kMPrd%2Fpcgpw0%2B0SqMER87Mjw409sv1V3e8yOX9nF95o27OqqNm80szY%2Fucz7b8FI7Cjt8Ez3BlgzoCi6wmYR9LUlBpudEUd5iwJOGOeXyyOugoIf2CIERt6Zc%2B%2F8dMMyxcbHLeIUIBTvQ2d6M0IFRmi7Kk56eJqXC%2BeFOKoT%2B4eDVMPyq%2F6EFfMByuBX3VhYjjWKLJz9EsvxJpDeVd1f9LWlM7EhTkMJjEd5Oxn3CXH764i2MyXklLyJT2a4MlOsRzqwP993bD%2FzzAMK82AoRUR4uGGXudQNkQ1ChrwSYZUmxna%2BkFuviSDoYzvCEzWwHvQpu%2FzIcpanj0helZy6Tb5D%2FgtLAD6F7Zot69aprX%2FNWbvzaoBFn1ADCePAC0d0vfC1CUrcedNfJ3KTF20svQVrpJhVTDE2gFqcEPocB6CUoenf7bKtRgwdIHDwgeWMS9KmP%2B7vMWWz7lvp9k4Xrt8SXVFg%2FBQ4uZ3Q%2FiDnq8tEAIESB7l%2Be2E9ioGnmru07hpr3y3NMkjp8duCDGocv%2FH8ngKXo2KsNhDVKKmti1ys3K3GGRy2wg3%2BCtxCBxQYMN3B9rwGOqUBL2UnubdZ2HHRTxGAv0HqObP3GPZiUtp9iFK91M5QapssFL34xIfxXDak3tKttxrUwsEGoq08DYWv9YV3t6uUBDPsC4T0u2RO9Q5vRqpfbbdKH0rF8S9FK0%2FkXn5lo3BPZd3Px5snCBFoC0gxsF4t8ew85ARm3u5yxJS%2B7Hxh8yO0wGJ5L2Rlu7lzEAqGOQMF%2F%2BxR8chn7vydBIAzwosE%2F3trsvYb&X-Amz-Signature=98c01f686564bafe62ebbdb774dfe8e14820088be671089950bf2be65883553c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV2BSAZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEARbM1ttYQnAgsocBEbFuATSqu2uMcXcfQ%2FPylptvW8AiEAw1%2Fwf5llaA0FYojerfEsLSX11bM0SU9UyIhq9HhfiCYqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZo44SrugxvbIALlyrcA6%2Fffr5g%2B7FHnPCK%2F7VobcQMZdt4X084DE1XYWj5Wl99LTYFy%2F2Th6CTjth9kMPrd%2Fpcgpw0%2B0SqMER87Mjw409sv1V3e8yOX9nF95o27OqqNm80szY%2Fucz7b8FI7Cjt8Ez3BlgzoCi6wmYR9LUlBpudEUd5iwJOGOeXyyOugoIf2CIERt6Zc%2B%2F8dMMyxcbHLeIUIBTvQ2d6M0IFRmi7Kk56eJqXC%2BeFOKoT%2B4eDVMPyq%2F6EFfMByuBX3VhYjjWKLJz9EsvxJpDeVd1f9LWlM7EhTkMJjEd5Oxn3CXH764i2MyXklLyJT2a4MlOsRzqwP993bD%2FzzAMK82AoRUR4uGGXudQNkQ1ChrwSYZUmxna%2BkFuviSDoYzvCEzWwHvQpu%2FzIcpanj0helZy6Tb5D%2FgtLAD6F7Zot69aprX%2FNWbvzaoBFn1ADCePAC0d0vfC1CUrcedNfJ3KTF20svQVrpJhVTDE2gFqcEPocB6CUoenf7bKtRgwdIHDwgeWMS9KmP%2B7vMWWz7lvp9k4Xrt8SXVFg%2FBQ4uZ3Q%2FiDnq8tEAIESB7l%2Be2E9ioGnmru07hpr3y3NMkjp8duCDGocv%2FH8ngKXo2KsNhDVKKmti1ys3K3GGRy2wg3%2BCtxCBxQYMN3B9rwGOqUBL2UnubdZ2HHRTxGAv0HqObP3GPZiUtp9iFK91M5QapssFL34xIfxXDak3tKttxrUwsEGoq08DYWv9YV3t6uUBDPsC4T0u2RO9Q5vRqpfbbdKH0rF8S9FK0%2FkXn5lo3BPZd3Px5snCBFoC0gxsF4t8ew85ARm3u5yxJS%2B7Hxh8yO0wGJ5L2Rlu7lzEAqGOQMF%2F%2BxR8chn7vydBIAzwosE%2F3trsvYb&X-Amz-Signature=780582f3df49bca2e3ca9ff94a13ebd1760e59e0f70942b7c53d38bb2b61e658&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV2BSAZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEARbM1ttYQnAgsocBEbFuATSqu2uMcXcfQ%2FPylptvW8AiEAw1%2Fwf5llaA0FYojerfEsLSX11bM0SU9UyIhq9HhfiCYqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZo44SrugxvbIALlyrcA6%2Fffr5g%2B7FHnPCK%2F7VobcQMZdt4X084DE1XYWj5Wl99LTYFy%2F2Th6CTjth9kMPrd%2Fpcgpw0%2B0SqMER87Mjw409sv1V3e8yOX9nF95o27OqqNm80szY%2Fucz7b8FI7Cjt8Ez3BlgzoCi6wmYR9LUlBpudEUd5iwJOGOeXyyOugoIf2CIERt6Zc%2B%2F8dMMyxcbHLeIUIBTvQ2d6M0IFRmi7Kk56eJqXC%2BeFOKoT%2B4eDVMPyq%2F6EFfMByuBX3VhYjjWKLJz9EsvxJpDeVd1f9LWlM7EhTkMJjEd5Oxn3CXH764i2MyXklLyJT2a4MlOsRzqwP993bD%2FzzAMK82AoRUR4uGGXudQNkQ1ChrwSYZUmxna%2BkFuviSDoYzvCEzWwHvQpu%2FzIcpanj0helZy6Tb5D%2FgtLAD6F7Zot69aprX%2FNWbvzaoBFn1ADCePAC0d0vfC1CUrcedNfJ3KTF20svQVrpJhVTDE2gFqcEPocB6CUoenf7bKtRgwdIHDwgeWMS9KmP%2B7vMWWz7lvp9k4Xrt8SXVFg%2FBQ4uZ3Q%2FiDnq8tEAIESB7l%2Be2E9ioGnmru07hpr3y3NMkjp8duCDGocv%2FH8ngKXo2KsNhDVKKmti1ys3K3GGRy2wg3%2BCtxCBxQYMN3B9rwGOqUBL2UnubdZ2HHRTxGAv0HqObP3GPZiUtp9iFK91M5QapssFL34xIfxXDak3tKttxrUwsEGoq08DYWv9YV3t6uUBDPsC4T0u2RO9Q5vRqpfbbdKH0rF8S9FK0%2FkXn5lo3BPZd3Px5snCBFoC0gxsF4t8ew85ARm3u5yxJS%2B7Hxh8yO0wGJ5L2Rlu7lzEAqGOQMF%2F%2BxR8chn7vydBIAzwosE%2F3trsvYb&X-Amz-Signature=c943b19e0dbb7f3fe66133bc8796c1c198ac6acb587e25cbe945226b9dbc5ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV2BSAZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEARbM1ttYQnAgsocBEbFuATSqu2uMcXcfQ%2FPylptvW8AiEAw1%2Fwf5llaA0FYojerfEsLSX11bM0SU9UyIhq9HhfiCYqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZo44SrugxvbIALlyrcA6%2Fffr5g%2B7FHnPCK%2F7VobcQMZdt4X084DE1XYWj5Wl99LTYFy%2F2Th6CTjth9kMPrd%2Fpcgpw0%2B0SqMER87Mjw409sv1V3e8yOX9nF95o27OqqNm80szY%2Fucz7b8FI7Cjt8Ez3BlgzoCi6wmYR9LUlBpudEUd5iwJOGOeXyyOugoIf2CIERt6Zc%2B%2F8dMMyxcbHLeIUIBTvQ2d6M0IFRmi7Kk56eJqXC%2BeFOKoT%2B4eDVMPyq%2F6EFfMByuBX3VhYjjWKLJz9EsvxJpDeVd1f9LWlM7EhTkMJjEd5Oxn3CXH764i2MyXklLyJT2a4MlOsRzqwP993bD%2FzzAMK82AoRUR4uGGXudQNkQ1ChrwSYZUmxna%2BkFuviSDoYzvCEzWwHvQpu%2FzIcpanj0helZy6Tb5D%2FgtLAD6F7Zot69aprX%2FNWbvzaoBFn1ADCePAC0d0vfC1CUrcedNfJ3KTF20svQVrpJhVTDE2gFqcEPocB6CUoenf7bKtRgwdIHDwgeWMS9KmP%2B7vMWWz7lvp9k4Xrt8SXVFg%2FBQ4uZ3Q%2FiDnq8tEAIESB7l%2Be2E9ioGnmru07hpr3y3NMkjp8duCDGocv%2FH8ngKXo2KsNhDVKKmti1ys3K3GGRy2wg3%2BCtxCBxQYMN3B9rwGOqUBL2UnubdZ2HHRTxGAv0HqObP3GPZiUtp9iFK91M5QapssFL34xIfxXDak3tKttxrUwsEGoq08DYWv9YV3t6uUBDPsC4T0u2RO9Q5vRqpfbbdKH0rF8S9FK0%2FkXn5lo3BPZd3Px5snCBFoC0gxsF4t8ew85ARm3u5yxJS%2B7Hxh8yO0wGJ5L2Rlu7lzEAqGOQMF%2F%2BxR8chn7vydBIAzwosE%2F3trsvYb&X-Amz-Signature=b6c9120906932d5f280cb95a1a912478ce03d56b2722fd6d48f1e1646212114b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZNG4IXD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGA%2BUe7BtMEFQl%2FQKxbLRnlF0NqLjprWd7bqCKnu97cZAiEA%2FTe2M7%2B3o%2BVAyTAWZ3sc4yse8x9KIJrkyQogP%2FLWIlIqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIX9klyIAdgXDf6v4SrcAxw0TCBxQfj5AL6ZbmYYpAe%2F1%2Fb3A7owbg53x47RUD441bqBomzuVYyPR4GRTKZG1URX6XtrpevevU%2FcDPXxFKo934rV18Pntsiod8nlTTMKYb8zVQWsYIGWo9N2yN862AWlqo9kwFLQjNIjcmajDyB5OZCFBAv%2Bzfs%2FWgglGl7xSH7V4fZZW2REZ%2BgbZuc0H0gmSG%2FQDUXuXgpUyq0vU9dBuZ0Tpl7LeSsKmNSFLuxT4Hon78M6qnUhhAvVGllfOkGC8Ev50uuMKNPfhs2TMcoqQviK%2FjHB5ctcT%2FZ2%2FJDKcd4zAzdJeA%2FLP7fgNICvHhLvVS0M6lqW%2FkDSyL7R8i2gz1WLn8rkC7%2FMI1jUK4C1wsDMsWmr%2Bn8Uh5bL%2FpzCQfZtfwztAbMNlkSyaUSt5fhrN8pYrurivNAShOlZ6J87vE3vaJn6IcX8pwQ5UCGHGfGkbRI%2BBrSLL%2Fd8VOwmuMsRhbSdUXYAUK2KtSghfnnjF7yd6fQuKbbJHIwcgKP30eCJioJbFhVrR9MDGPCy6tt9VSPJl%2F%2BRSGcTeqBvEDpDQDFdzd00agDp33eOHDNbWSBfg4AID42lili20QeT5DuEim%2FjOIf%2FKAXLPragQguHBlT7ovhN7lHDd6ibMLzB9rwGOqUBA1Lr2%2BW83vInD7ZZcT0dy9bJlzKeV38UK8oueyr4hu10O5ZTJpdNn57Lq02pqRHIkZbFdUfWBSNLFUH3DFu9doGy4rTn27aPC%2Ff7pcbVFnTJZt8ndSVilAEQPPzMA4MbtWEI%2B5%2FbairVfrGWDxoQchRTSxKkU%2BlujjiRFx4veYIqrsH9glZM2NRVAk%2Fq3XYtu8oBZQhX9Ec2WyqyDjl3RQiytG0n&X-Amz-Signature=19888abbda6f022dc267518c3cc2e0a43e1713006ecb14364395bfbcd5725f09&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZNG4IXD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGA%2BUe7BtMEFQl%2FQKxbLRnlF0NqLjprWd7bqCKnu97cZAiEA%2FTe2M7%2B3o%2BVAyTAWZ3sc4yse8x9KIJrkyQogP%2FLWIlIqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIX9klyIAdgXDf6v4SrcAxw0TCBxQfj5AL6ZbmYYpAe%2F1%2Fb3A7owbg53x47RUD441bqBomzuVYyPR4GRTKZG1URX6XtrpevevU%2FcDPXxFKo934rV18Pntsiod8nlTTMKYb8zVQWsYIGWo9N2yN862AWlqo9kwFLQjNIjcmajDyB5OZCFBAv%2Bzfs%2FWgglGl7xSH7V4fZZW2REZ%2BgbZuc0H0gmSG%2FQDUXuXgpUyq0vU9dBuZ0Tpl7LeSsKmNSFLuxT4Hon78M6qnUhhAvVGllfOkGC8Ev50uuMKNPfhs2TMcoqQviK%2FjHB5ctcT%2FZ2%2FJDKcd4zAzdJeA%2FLP7fgNICvHhLvVS0M6lqW%2FkDSyL7R8i2gz1WLn8rkC7%2FMI1jUK4C1wsDMsWmr%2Bn8Uh5bL%2FpzCQfZtfwztAbMNlkSyaUSt5fhrN8pYrurivNAShOlZ6J87vE3vaJn6IcX8pwQ5UCGHGfGkbRI%2BBrSLL%2Fd8VOwmuMsRhbSdUXYAUK2KtSghfnnjF7yd6fQuKbbJHIwcgKP30eCJioJbFhVrR9MDGPCy6tt9VSPJl%2F%2BRSGcTeqBvEDpDQDFdzd00agDp33eOHDNbWSBfg4AID42lili20QeT5DuEim%2FjOIf%2FKAXLPragQguHBlT7ovhN7lHDd6ibMLzB9rwGOqUBA1Lr2%2BW83vInD7ZZcT0dy9bJlzKeV38UK8oueyr4hu10O5ZTJpdNn57Lq02pqRHIkZbFdUfWBSNLFUH3DFu9doGy4rTn27aPC%2Ff7pcbVFnTJZt8ndSVilAEQPPzMA4MbtWEI%2B5%2FbairVfrGWDxoQchRTSxKkU%2BlujjiRFx4veYIqrsH9glZM2NRVAk%2Fq3XYtu8oBZQhX9Ec2WyqyDjl3RQiytG0n&X-Amz-Signature=d32f9ea2df68848664fb0fef0e5799445124f78f67bdcf9b7bdb57239e2f7a83&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZNG4IXD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGA%2BUe7BtMEFQl%2FQKxbLRnlF0NqLjprWd7bqCKnu97cZAiEA%2FTe2M7%2B3o%2BVAyTAWZ3sc4yse8x9KIJrkyQogP%2FLWIlIqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIX9klyIAdgXDf6v4SrcAxw0TCBxQfj5AL6ZbmYYpAe%2F1%2Fb3A7owbg53x47RUD441bqBomzuVYyPR4GRTKZG1URX6XtrpevevU%2FcDPXxFKo934rV18Pntsiod8nlTTMKYb8zVQWsYIGWo9N2yN862AWlqo9kwFLQjNIjcmajDyB5OZCFBAv%2Bzfs%2FWgglGl7xSH7V4fZZW2REZ%2BgbZuc0H0gmSG%2FQDUXuXgpUyq0vU9dBuZ0Tpl7LeSsKmNSFLuxT4Hon78M6qnUhhAvVGllfOkGC8Ev50uuMKNPfhs2TMcoqQviK%2FjHB5ctcT%2FZ2%2FJDKcd4zAzdJeA%2FLP7fgNICvHhLvVS0M6lqW%2FkDSyL7R8i2gz1WLn8rkC7%2FMI1jUK4C1wsDMsWmr%2Bn8Uh5bL%2FpzCQfZtfwztAbMNlkSyaUSt5fhrN8pYrurivNAShOlZ6J87vE3vaJn6IcX8pwQ5UCGHGfGkbRI%2BBrSLL%2Fd8VOwmuMsRhbSdUXYAUK2KtSghfnnjF7yd6fQuKbbJHIwcgKP30eCJioJbFhVrR9MDGPCy6tt9VSPJl%2F%2BRSGcTeqBvEDpDQDFdzd00agDp33eOHDNbWSBfg4AID42lili20QeT5DuEim%2FjOIf%2FKAXLPragQguHBlT7ovhN7lHDd6ibMLzB9rwGOqUBA1Lr2%2BW83vInD7ZZcT0dy9bJlzKeV38UK8oueyr4hu10O5ZTJpdNn57Lq02pqRHIkZbFdUfWBSNLFUH3DFu9doGy4rTn27aPC%2Ff7pcbVFnTJZt8ndSVilAEQPPzMA4MbtWEI%2B5%2FbairVfrGWDxoQchRTSxKkU%2BlujjiRFx4veYIqrsH9glZM2NRVAk%2Fq3XYtu8oBZQhX9Ec2WyqyDjl3RQiytG0n&X-Amz-Signature=e48a665b9eb1fe2827b547517d75c4e2eccb24dddd68ac6e3ff5527319d4d7aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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

