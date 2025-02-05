

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=0d427cf40dc6e80adedf200e59b6c1dcb0c416505a1a20cafe06aa89c8a1ccf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=c5248e8c26a5aff58abb9b81f9ebc8195f8c74c40acf9aa539d29c7e44c776e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=f10ca1235d4c6d07d319ff95603f085a9551a1a82b839a0df155937da6e50302&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=6f7f72d4169845a189b76ea3d1e6c8d5b3c0e7668e54404d643d3f144114114b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=9eb02f3c7d8d440736605fafdf7b20f31f8c7675d6599bea52065d660e66b10b&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=d53240262e6da0b4de8d06fd23ef43c2bf849659dc4a411d807ee7d446d9cf6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=a89398294460ced11b6a09cb7d42984b8e1a90c3373923b44ab43b10466fe5f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=4582c3d275195173c31d6bba52ca806c4b6f2b56ebd6cc3122ddc1b5dfa8e417&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=eb256b6b8400b55295e964fccbf5bcc4e5cfdc5e71543061307606aa8fa4a9bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=4bfe178fa18ef7905cb1f44b363f3ff720b4abba4d6cb008f8cdfca148286c88&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZZ6DKT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD4jdjVvuSl5piFRg93xBmz5CeFgr%2FsWgSdFpwUzOHVnQIgeV6P9LcYsxjQ0T2vfrIbvqecCw5uMDNv0ETjhh2zATQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKEBfjzf7p1tpTafWircA2yxg%2B44jCzRS1D9uY8wjvMApt%2B9WMAupoYktcT9Mmp0dZPikk2qsP%2F4zYzDFGqAU3Nc2Q%2FQ2SS0PQbre9fKgX2Hkdll7x3WzkHMUBLzJsEZhVUxd83elpDTOPSqAJX04RvvFiEMEgzdLBabfU5WsuJu5wyEoPCGsT8dxRGJtDtdAKUcGGVsK2GZO1NoNZPt3JIbqjiu%2Fx0czpbTJbA6SGN3r11oj0UpyeR76IBM3jmNRWwQYpIrln73XbsNypEnUBl2l8mdDcAuNLcidYVYDlrKnBpK0PxGcnYcGSuFeI6Mq%2FpfuD3x7CoZUUa6fhRdAAmniWxwQyHS4ntuBRQ7aUQeU9cOTjZaj1hEYWrYuTAbqDdn0%2FQKMy8EZyRFikFnz9tkJ1dyV5anJ%2BOR2WatXmJv6bIpouI87JKkzCbs%2F4Nrt%2FhMyt0OXuTCSUb8DKDlfQhYoKsPP9o9aZKQFmv8eSb6O7L7ZJkkyHhEcifGJL29rEcotGh1HMF1qinqd3yGVXeHyGdasQawGfzZXx8kO22Xezl95YpIiR7dUyen9wOo6HzHXhaTmrFT4%2FzwbSnkdqkUEokECuVYabVrs7Y5Up9jP%2B0oHfbdIjER08BG2L6CgcoQ6IOgeCGOTLXKMLq6jr0GOqUBXI6Zkd3uEOEUPvHEZaCp3CNUxIJer9vcA2sMMLZ8Vo8X2y1ZZkJ7lef%2F46RtUuc5aMq300R4TjLlUfTcJLzDIalTPqSqtSeWuv7FXRW6PyEcsAIESOrXddATehryy7f58N6CNJY%2FpHFsXwBsQDnS1jPOri8sa%2FHjzEK87%2BZkl42l5IzKTd%2BX1LZ81L9UQxzTawYxVLgsMG%2B4DXiaePt6MjeWTsoK&X-Amz-Signature=f91d9d6b26776ac855b982885be844218fb072ceb0862b8d845999a98c71622e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR7GBWA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCl%2FxSRQe5lokLDS5q1YarXM8L7LAUUMqC%2Fr6Z858w7%2FAIhAOwGuVfpE9kloN5T4HtcA2%2BfNaFmDhgf5EgtEsUPpMs%2BKv8DCEoQABoMNjM3NDIzMTgzODA1IgyOTUHnJ6AmLo0j8Pwq3AO5Kq5iFjYqJuwzgqQqKSaVB1Wgz%2BSgF2CISbvxei5IhT07Xuj9pnx4sQQC9wICZs6XQDVDf%2FvtvqtQjPVdoq5VoPzDa0LNPtaAnCcV0SaUGovxLsUWFMjbTBtIP0mlOvh8ir%2FzIcpC25QdQYGKiy5xjkelV9eq69XGve90m3xWHu7ipF65b%2FrUYj%2Fpn86xdjBqZdsiPtBjLf%2BQy0rCLWkGg52pgA29xiRTYmO52eF0kaDOuDePbhIScpShzYAp4hc4rteSJNTXBftcQrdImThxWoCXuwRJrbsQOHZHhnw19%2FMNF9FwFgPcOVO4jyB4bGokzi0jlf2axwcSmr8fCffSVPeyEuKoSkosVB093IjZ%2BgaGC5wbxHzUEoBKxF3r%2BaEaUseg4erKhtDOdQT9dOIlVXEnZH2DWSvL4xfcm8%2FHc66qTGgAra2bgnQTnjUXOgRFb2IAuja%2Bm%2BEAh7lZohxphtvQpAJB5AkZFJXmSzrNJeuDEQ3IZ3WNniGNDgtPoYIvOpnVpo%2FOrMfZpQB8hrwGQEV6MoGtheXpK0Dpq4QFr%2FkDPC8bJkAEn00p5vXG2lmMUF9JbxizGvxSnmre2doUcUxiLYaJXWnSwn6SRFfeoVAMAYBLktDdHhh7eDC3uo69BjqkAQXEOBt7TO2VtkJIar%2FCrDX31rqBfz1mvENGitzI11mo4IGRo6Hk8b6IYkaYCDMOP8LQZz3nWpMOpPEJxUkaNgVc92pQs%2F%2BvunNKVoxAD6fsIEHVio%2FmgRvAV94wEmqbEosaT7vvWqrHd8paC6kZbcCthNdNCgqbFxJXGeceicS5JTbujS5%2F5kyG%2FtO6tZMUYTq%2BgVocN0Bntw%2BtkabFYLEESyzS&X-Amz-Signature=9dd97cbf0e2cbbfc55837d16447dd5659422599c1ae0b271a79d5b132e4d9839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR7GBWA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCl%2FxSRQe5lokLDS5q1YarXM8L7LAUUMqC%2Fr6Z858w7%2FAIhAOwGuVfpE9kloN5T4HtcA2%2BfNaFmDhgf5EgtEsUPpMs%2BKv8DCEoQABoMNjM3NDIzMTgzODA1IgyOTUHnJ6AmLo0j8Pwq3AO5Kq5iFjYqJuwzgqQqKSaVB1Wgz%2BSgF2CISbvxei5IhT07Xuj9pnx4sQQC9wICZs6XQDVDf%2FvtvqtQjPVdoq5VoPzDa0LNPtaAnCcV0SaUGovxLsUWFMjbTBtIP0mlOvh8ir%2FzIcpC25QdQYGKiy5xjkelV9eq69XGve90m3xWHu7ipF65b%2FrUYj%2Fpn86xdjBqZdsiPtBjLf%2BQy0rCLWkGg52pgA29xiRTYmO52eF0kaDOuDePbhIScpShzYAp4hc4rteSJNTXBftcQrdImThxWoCXuwRJrbsQOHZHhnw19%2FMNF9FwFgPcOVO4jyB4bGokzi0jlf2axwcSmr8fCffSVPeyEuKoSkosVB093IjZ%2BgaGC5wbxHzUEoBKxF3r%2BaEaUseg4erKhtDOdQT9dOIlVXEnZH2DWSvL4xfcm8%2FHc66qTGgAra2bgnQTnjUXOgRFb2IAuja%2Bm%2BEAh7lZohxphtvQpAJB5AkZFJXmSzrNJeuDEQ3IZ3WNniGNDgtPoYIvOpnVpo%2FOrMfZpQB8hrwGQEV6MoGtheXpK0Dpq4QFr%2FkDPC8bJkAEn00p5vXG2lmMUF9JbxizGvxSnmre2doUcUxiLYaJXWnSwn6SRFfeoVAMAYBLktDdHhh7eDC3uo69BjqkAQXEOBt7TO2VtkJIar%2FCrDX31rqBfz1mvENGitzI11mo4IGRo6Hk8b6IYkaYCDMOP8LQZz3nWpMOpPEJxUkaNgVc92pQs%2F%2BvunNKVoxAD6fsIEHVio%2FmgRvAV94wEmqbEosaT7vvWqrHd8paC6kZbcCthNdNCgqbFxJXGeceicS5JTbujS5%2F5kyG%2FtO6tZMUYTq%2BgVocN0Bntw%2BtkabFYLEESyzS&X-Amz-Signature=92f81dfc1bba3fb45f636e2528682a8c8e4449ba8e0d6fd93667446fdd79e0e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR7GBWA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCl%2FxSRQe5lokLDS5q1YarXM8L7LAUUMqC%2Fr6Z858w7%2FAIhAOwGuVfpE9kloN5T4HtcA2%2BfNaFmDhgf5EgtEsUPpMs%2BKv8DCEoQABoMNjM3NDIzMTgzODA1IgyOTUHnJ6AmLo0j8Pwq3AO5Kq5iFjYqJuwzgqQqKSaVB1Wgz%2BSgF2CISbvxei5IhT07Xuj9pnx4sQQC9wICZs6XQDVDf%2FvtvqtQjPVdoq5VoPzDa0LNPtaAnCcV0SaUGovxLsUWFMjbTBtIP0mlOvh8ir%2FzIcpC25QdQYGKiy5xjkelV9eq69XGve90m3xWHu7ipF65b%2FrUYj%2Fpn86xdjBqZdsiPtBjLf%2BQy0rCLWkGg52pgA29xiRTYmO52eF0kaDOuDePbhIScpShzYAp4hc4rteSJNTXBftcQrdImThxWoCXuwRJrbsQOHZHhnw19%2FMNF9FwFgPcOVO4jyB4bGokzi0jlf2axwcSmr8fCffSVPeyEuKoSkosVB093IjZ%2BgaGC5wbxHzUEoBKxF3r%2BaEaUseg4erKhtDOdQT9dOIlVXEnZH2DWSvL4xfcm8%2FHc66qTGgAra2bgnQTnjUXOgRFb2IAuja%2Bm%2BEAh7lZohxphtvQpAJB5AkZFJXmSzrNJeuDEQ3IZ3WNniGNDgtPoYIvOpnVpo%2FOrMfZpQB8hrwGQEV6MoGtheXpK0Dpq4QFr%2FkDPC8bJkAEn00p5vXG2lmMUF9JbxizGvxSnmre2doUcUxiLYaJXWnSwn6SRFfeoVAMAYBLktDdHhh7eDC3uo69BjqkAQXEOBt7TO2VtkJIar%2FCrDX31rqBfz1mvENGitzI11mo4IGRo6Hk8b6IYkaYCDMOP8LQZz3nWpMOpPEJxUkaNgVc92pQs%2F%2BvunNKVoxAD6fsIEHVio%2FmgRvAV94wEmqbEosaT7vvWqrHd8paC6kZbcCthNdNCgqbFxJXGeceicS5JTbujS5%2F5kyG%2FtO6tZMUYTq%2BgVocN0Bntw%2BtkabFYLEESyzS&X-Amz-Signature=f1088a1edfdc95521806d27256f1ad6fed40d00b245a1d0ef88ce369c9d280ef&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR7GBWA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCl%2FxSRQe5lokLDS5q1YarXM8L7LAUUMqC%2Fr6Z858w7%2FAIhAOwGuVfpE9kloN5T4HtcA2%2BfNaFmDhgf5EgtEsUPpMs%2BKv8DCEoQABoMNjM3NDIzMTgzODA1IgyOTUHnJ6AmLo0j8Pwq3AO5Kq5iFjYqJuwzgqQqKSaVB1Wgz%2BSgF2CISbvxei5IhT07Xuj9pnx4sQQC9wICZs6XQDVDf%2FvtvqtQjPVdoq5VoPzDa0LNPtaAnCcV0SaUGovxLsUWFMjbTBtIP0mlOvh8ir%2FzIcpC25QdQYGKiy5xjkelV9eq69XGve90m3xWHu7ipF65b%2FrUYj%2Fpn86xdjBqZdsiPtBjLf%2BQy0rCLWkGg52pgA29xiRTYmO52eF0kaDOuDePbhIScpShzYAp4hc4rteSJNTXBftcQrdImThxWoCXuwRJrbsQOHZHhnw19%2FMNF9FwFgPcOVO4jyB4bGokzi0jlf2axwcSmr8fCffSVPeyEuKoSkosVB093IjZ%2BgaGC5wbxHzUEoBKxF3r%2BaEaUseg4erKhtDOdQT9dOIlVXEnZH2DWSvL4xfcm8%2FHc66qTGgAra2bgnQTnjUXOgRFb2IAuja%2Bm%2BEAh7lZohxphtvQpAJB5AkZFJXmSzrNJeuDEQ3IZ3WNniGNDgtPoYIvOpnVpo%2FOrMfZpQB8hrwGQEV6MoGtheXpK0Dpq4QFr%2FkDPC8bJkAEn00p5vXG2lmMUF9JbxizGvxSnmre2doUcUxiLYaJXWnSwn6SRFfeoVAMAYBLktDdHhh7eDC3uo69BjqkAQXEOBt7TO2VtkJIar%2FCrDX31rqBfz1mvENGitzI11mo4IGRo6Hk8b6IYkaYCDMOP8LQZz3nWpMOpPEJxUkaNgVc92pQs%2F%2BvunNKVoxAD6fsIEHVio%2FmgRvAV94wEmqbEosaT7vvWqrHd8paC6kZbcCthNdNCgqbFxJXGeceicS5JTbujS5%2F5kyG%2FtO6tZMUYTq%2BgVocN0Bntw%2BtkabFYLEESyzS&X-Amz-Signature=9b59bc18998e19a849743c08864209bb04018e56a1481128840b7526b9c9ac03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MLMLU2S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCklOPeCVbZKw7T1NctFDbMAth%2FFN%2ByeETT5kExLDJXcQIhAM9LBKHQtgytsB27TMysUGTz%2B9OpjvZ83wiicRtcbKK0Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxVTB%2Bb1k6gqZuzfNsq3AOVYjS48hAR1o36Ym1TTKH3fsPLBQTW6tro12JC8SeGSpQjEfFF%2B6dYA%2F64x3H6ihlby5eobZHeyqww%2B3%2FGXo7rGfiLVYRQ%2FcHBJYTwloFLdNJbXhMCIboQcW7ljn4Lx6kayyoB5gt2AGFyP%2BuixDX3EWKJbzYb7KCFGHbPzCkmoXIFulX95U62uXIPar4PRMAD%2BMEu7qgFIazWfdT1wrZSmSGGpm%2FUNEkBWFZvBW8OiqSptUmUbBedWHQHnka6%2FSPlYa%2FYgZiuNmYG4J1yP%2B02gLeJzc%2Bkp0mWhgFHUIHT4EQHy3swrnA3U0sxhwiatNl3biecfsXfJDrIaTznoScgb8jhjlR6Lp9aV05SDPLI9IId1g4XL08MLiPrzxAP%2BXEB32aLNK0400nhWY6I5Od0hPSuT%2BSdBLD50X8K7WCj%2FmvtAsYVX%2Brms%2Bb40u6CQW%2BGk22KQ4irMFcS8oyRitsAtmF0HzdNeO5ZmBD5y45GAyIdmGlBGUNBbqlpcE6OE5xGBIyIA78nue19xeWR4h3yKIfl4aoLuqcasKJbc8xPPk3QHYpYIn%2F1%2BCv%2BAmzU1dwD2xf2vT1LSP9XW4ZjzQgCoc%2F7HSrlj8Da6DFRWPXOoafZ4U%2F9OUW2O4O9XTDBuo69BjqkAa%2F%2FsdxgzgS5gd1bEHnAlFQWa0cb%2BOESOD5BWd%2F1S5%2FSrnPCNvbsIr9XXVDEO%2FXD%2B827z09NGkQxvq72Fn0bvt%2FiQShvtvgQzn9DKrPC2O%2F7MN07K8mx5JmKq%2BKrrpRQdX06YU6bj4TwubNPxE4trqtKuXdWCq65NlE4Q%2FfA2O%2BFJ9u%2B3iQMR6lauFN21%2FDmLDGxRvUiYr9%2B5YyV9FE9kZbP%2B7im&X-Amz-Signature=2bd120fd85fdcb07a9ee5125215ff8e12a21368e81671ca2b294d8d5d91d172d&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MLMLU2S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCklOPeCVbZKw7T1NctFDbMAth%2FFN%2ByeETT5kExLDJXcQIhAM9LBKHQtgytsB27TMysUGTz%2B9OpjvZ83wiicRtcbKK0Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxVTB%2Bb1k6gqZuzfNsq3AOVYjS48hAR1o36Ym1TTKH3fsPLBQTW6tro12JC8SeGSpQjEfFF%2B6dYA%2F64x3H6ihlby5eobZHeyqww%2B3%2FGXo7rGfiLVYRQ%2FcHBJYTwloFLdNJbXhMCIboQcW7ljn4Lx6kayyoB5gt2AGFyP%2BuixDX3EWKJbzYb7KCFGHbPzCkmoXIFulX95U62uXIPar4PRMAD%2BMEu7qgFIazWfdT1wrZSmSGGpm%2FUNEkBWFZvBW8OiqSptUmUbBedWHQHnka6%2FSPlYa%2FYgZiuNmYG4J1yP%2B02gLeJzc%2Bkp0mWhgFHUIHT4EQHy3swrnA3U0sxhwiatNl3biecfsXfJDrIaTznoScgb8jhjlR6Lp9aV05SDPLI9IId1g4XL08MLiPrzxAP%2BXEB32aLNK0400nhWY6I5Od0hPSuT%2BSdBLD50X8K7WCj%2FmvtAsYVX%2Brms%2Bb40u6CQW%2BGk22KQ4irMFcS8oyRitsAtmF0HzdNeO5ZmBD5y45GAyIdmGlBGUNBbqlpcE6OE5xGBIyIA78nue19xeWR4h3yKIfl4aoLuqcasKJbc8xPPk3QHYpYIn%2F1%2BCv%2BAmzU1dwD2xf2vT1LSP9XW4ZjzQgCoc%2F7HSrlj8Da6DFRWPXOoafZ4U%2F9OUW2O4O9XTDBuo69BjqkAa%2F%2FsdxgzgS5gd1bEHnAlFQWa0cb%2BOESOD5BWd%2F1S5%2FSrnPCNvbsIr9XXVDEO%2FXD%2B827z09NGkQxvq72Fn0bvt%2FiQShvtvgQzn9DKrPC2O%2F7MN07K8mx5JmKq%2BKrrpRQdX06YU6bj4TwubNPxE4trqtKuXdWCq65NlE4Q%2FfA2O%2BFJ9u%2B3iQMR6lauFN21%2FDmLDGxRvUiYr9%2B5YyV9FE9kZbP%2B7im&X-Amz-Signature=df3007d15e13385ee293e3a86874d6375a5776bda5fb32cbca4252bf2540bd60&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MLMLU2S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCklOPeCVbZKw7T1NctFDbMAth%2FFN%2ByeETT5kExLDJXcQIhAM9LBKHQtgytsB27TMysUGTz%2B9OpjvZ83wiicRtcbKK0Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxVTB%2Bb1k6gqZuzfNsq3AOVYjS48hAR1o36Ym1TTKH3fsPLBQTW6tro12JC8SeGSpQjEfFF%2B6dYA%2F64x3H6ihlby5eobZHeyqww%2B3%2FGXo7rGfiLVYRQ%2FcHBJYTwloFLdNJbXhMCIboQcW7ljn4Lx6kayyoB5gt2AGFyP%2BuixDX3EWKJbzYb7KCFGHbPzCkmoXIFulX95U62uXIPar4PRMAD%2BMEu7qgFIazWfdT1wrZSmSGGpm%2FUNEkBWFZvBW8OiqSptUmUbBedWHQHnka6%2FSPlYa%2FYgZiuNmYG4J1yP%2B02gLeJzc%2Bkp0mWhgFHUIHT4EQHy3swrnA3U0sxhwiatNl3biecfsXfJDrIaTznoScgb8jhjlR6Lp9aV05SDPLI9IId1g4XL08MLiPrzxAP%2BXEB32aLNK0400nhWY6I5Od0hPSuT%2BSdBLD50X8K7WCj%2FmvtAsYVX%2Brms%2Bb40u6CQW%2BGk22KQ4irMFcS8oyRitsAtmF0HzdNeO5ZmBD5y45GAyIdmGlBGUNBbqlpcE6OE5xGBIyIA78nue19xeWR4h3yKIfl4aoLuqcasKJbc8xPPk3QHYpYIn%2F1%2BCv%2BAmzU1dwD2xf2vT1LSP9XW4ZjzQgCoc%2F7HSrlj8Da6DFRWPXOoafZ4U%2F9OUW2O4O9XTDBuo69BjqkAa%2F%2FsdxgzgS5gd1bEHnAlFQWa0cb%2BOESOD5BWd%2F1S5%2FSrnPCNvbsIr9XXVDEO%2FXD%2B827z09NGkQxvq72Fn0bvt%2FiQShvtvgQzn9DKrPC2O%2F7MN07K8mx5JmKq%2BKrrpRQdX06YU6bj4TwubNPxE4trqtKuXdWCq65NlE4Q%2FfA2O%2BFJ9u%2B3iQMR6lauFN21%2FDmLDGxRvUiYr9%2B5YyV9FE9kZbP%2B7im&X-Amz-Signature=869b284f136cb5e111a4cc46618705af7a97a4eb965af50e3c751a3e32e9db5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

