

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=e910c2af2089a96d8292db5bd4f6629e5600a53fd3b4174cb410cdafbaf08616&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=cfa3081fcd35c5f52b73f00f9b1445689f8a361de4c643eb97a12fcd991764ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=80bc751edd5f2264ef3b06a04d2820a95aa47b8a50b2947b76390cebdffa062d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=0fe003374fd4e77f73f635a142b51897df092a71f2be548a75ff7199e87d8f93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=f30badd2e0c7ad003efaa6277e230b149dc654ba64dfa8c77aa04abf7e77ca4f&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=88efc79bca7afa3030f3c7cce09cfce0e4862aecb3fda0fa0dcd449d146939ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=61462a886047fa3acab7b3225ca61d4c5577eb732d4e5938eaf19ee47d18fe7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=0905f69ae768f98ee4889f13d047cc48d449503d1f519633f5781b538a752798&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=8d547bda47579a4fd0efe54d47eed39a783ceb8c99527d7e769d9584a8d17a6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=36134754368943e143bf52e5b985aba2782d23b142bc147fbcd2c96ebc09f521&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGOAXFUB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4vRpVV3pzrPrnapEjovyL7g0ZZlLif6ZRW8en4CIsjAIhAIIwbXg3W2SH8om5pTKK4z8gAZNa1d5Rd1oGDAQo6sBRKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzax5f%2FBaHWmJk3Q3Qq3AMf42RNCuoLuKtYovJeNNOmVp7BQJSZTiYAFOUSv2DRflaQvkUG1%2BXDF3tcbPKfeM2V6iZGgGohgQFgXBOhl6iijJs0msIRtA1YYX3pKpd1h8NV5utZaU9E3bYNWgboVh4eJP336eW6f%2BLndyAWxxZm5Vluxh8v65C9zcTzTvOwENJKm0%2BW%2BxhaDm62Xu9stEynsgix2S89pwLraiq9IOkTiKZXYBP3qkxEsfhDSNdpwB4G4O6ROdkEiBBNQzAqxrPjyV4SACy2zqhkhdcsyBx%2FHitqo51u6jHAnYBCrBm9KhBXdBDR6LIYZB5%2BWkdEhAMMcQv279YcWP%2B%2BZ5PLOVYoYbAvuGGmVttgQhmWxEaZPACypDlLxgBIOCJAqFgp0q2JgcxWSstromy6WAuCXgPJT%2Bb1sI7vg2SHdkirtzvhCbRfO3d4RPmCmwdvA0qkIrxDPxkJsXjEnS3hr2xJniIolRv5N9R93z7ugU6dqc0by2Zi26gWzhas0T%2BTO%2F3jmkYs8wP5%2BiuitHi94nMAgZmiXRINIuQz2%2Fya70FbF6N3%2BPmChmwc8P0tyND4n5RZUzLEw36w1uQD9M9ChpF2aVwU%2FKevfcnRvGGoUkMaXDjGg1gzXcCM7KqVerxP%2BDD%2Bsfq8BjqkAWixO3AtK%2BezwbX2IhBcDWn2cqhZBYGAeGJpfZKJOd9m6W9nWOLr5huKc47b5m07GPupAA7J%2B0iUVQwh%2FSz0%2ByYYDXCSCDh3x09q1dsWSbtIpi%2BIN5CqVtkU%2B21f2OjNIIeXtbM54zkfiAZTfwIQtXwOoM0DsgiBk9q1o07RbTkWA8R9y2ENkDWjaDziwvRVjvHe%2F2pnssn2Tf7JPFDefqdOHudQ&X-Amz-Signature=2f30a68200fc2ad0a8d10f26b9fcdac3a0b38cb48fe1d7dcf2ce1a18d19404f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U5IPVSD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOhE2yfZfjqWxPs5E5dy3viQFzjZ%2FPQ%2BPwOO4dEbFA5AiARAvk3c6n4sLQaQ0nJ2tAlDIwZkjXqrpe%2BPPPy1%2Bp%2B1CqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp12MrArAWOG5aipuKtwDpJL5%2FaxFH4Vlrvnlks9vPMHBc5YJ%2F16r6BO%2B64UI%2Bud2zPs%2FCsBof6udK8UKxFBFp06iNzYtzXU8NI6cA5O3%2BoTzec8tWmjpwZDYaGr2PoSduG90zWao6IBYXb08dYDxkCK6UQ5wF1GJJUniOPZczRhajwA7rJSlcCJanrYBE%2Bw0ftTIF5JVEl6SbyRe4veDoTF6p%2FopQwjpwF6%2FSaPAEs%2FcgbdXPsTg0Fk3AajmuHAKrT7im%2FFJ1vxzgil8H%2Bin1h%2B4CXul6Z55i6F0mVU2%2B0D1Q%2FHZqVh%2BABQXm2KEfPlWf35JTow1cxaDjbqhKvK8C%2FR8uhmhWtZOgFlct%2BbHvDRH1coff45FjmwwBiramX1jUijvAUu6kGobEoC%2BM%2FB54PTCAZn81tTOCWLrVcaYFHNs5X6l5%2Bf7CHV4uRoCw1EeWOs0dmsAyy7MKG5hc1bZG0Kah%2FFhQVCTQKeQ2Xf2fida2Zm1kFewUeTg98eNq9Kn6Ujg2nE738ryBMknQDUSL7NH5PuXcYrjXKpI2kdQAFAfZI3pAlmUqgIHXboTDY%2FIh08A6BHkdHODEUFV3Qjm5LmcCtaOTyAB90tAxDwj1Qel6L5tiITSA5c4Yt5HKeeFKV6HOXLudZtba7swv7H6vAY6pgFbdE4Ap67rpHK%2BSakrLuu5omgu5mrL6z%2FJ4jA%2FnOf2IgV%2FRwnpXLbE8XLHhfMUXU5GhRo7xA0zZpwThn2R2EC3XvqfH8ZtUlcpQ5eMbrw2PRCDz%2BibqHL3hOKnl3vlbZMpYJUvmfrQKz4f9L%2BR1vxmmntVByTdsa9XTQ5v0g5s0jwdPzse%2BEr3zQ2nIxgLi1xl6CxLPyVzTP6s9SqJHSHsDizdskd9&X-Amz-Signature=8e6f408c93f2dec56d65eefa25731802316fa257de39772e6508b1af6969c882&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U5IPVSD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOhE2yfZfjqWxPs5E5dy3viQFzjZ%2FPQ%2BPwOO4dEbFA5AiARAvk3c6n4sLQaQ0nJ2tAlDIwZkjXqrpe%2BPPPy1%2Bp%2B1CqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp12MrArAWOG5aipuKtwDpJL5%2FaxFH4Vlrvnlks9vPMHBc5YJ%2F16r6BO%2B64UI%2Bud2zPs%2FCsBof6udK8UKxFBFp06iNzYtzXU8NI6cA5O3%2BoTzec8tWmjpwZDYaGr2PoSduG90zWao6IBYXb08dYDxkCK6UQ5wF1GJJUniOPZczRhajwA7rJSlcCJanrYBE%2Bw0ftTIF5JVEl6SbyRe4veDoTF6p%2FopQwjpwF6%2FSaPAEs%2FcgbdXPsTg0Fk3AajmuHAKrT7im%2FFJ1vxzgil8H%2Bin1h%2B4CXul6Z55i6F0mVU2%2B0D1Q%2FHZqVh%2BABQXm2KEfPlWf35JTow1cxaDjbqhKvK8C%2FR8uhmhWtZOgFlct%2BbHvDRH1coff45FjmwwBiramX1jUijvAUu6kGobEoC%2BM%2FB54PTCAZn81tTOCWLrVcaYFHNs5X6l5%2Bf7CHV4uRoCw1EeWOs0dmsAyy7MKG5hc1bZG0Kah%2FFhQVCTQKeQ2Xf2fida2Zm1kFewUeTg98eNq9Kn6Ujg2nE738ryBMknQDUSL7NH5PuXcYrjXKpI2kdQAFAfZI3pAlmUqgIHXboTDY%2FIh08A6BHkdHODEUFV3Qjm5LmcCtaOTyAB90tAxDwj1Qel6L5tiITSA5c4Yt5HKeeFKV6HOXLudZtba7swv7H6vAY6pgFbdE4Ap67rpHK%2BSakrLuu5omgu5mrL6z%2FJ4jA%2FnOf2IgV%2FRwnpXLbE8XLHhfMUXU5GhRo7xA0zZpwThn2R2EC3XvqfH8ZtUlcpQ5eMbrw2PRCDz%2BibqHL3hOKnl3vlbZMpYJUvmfrQKz4f9L%2BR1vxmmntVByTdsa9XTQ5v0g5s0jwdPzse%2BEr3zQ2nIxgLi1xl6CxLPyVzTP6s9SqJHSHsDizdskd9&X-Amz-Signature=82cd85c87d7cce3ddaa948235ad585f5007e3aafac825def2ce1da3d72a519c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U5IPVSD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOhE2yfZfjqWxPs5E5dy3viQFzjZ%2FPQ%2BPwOO4dEbFA5AiARAvk3c6n4sLQaQ0nJ2tAlDIwZkjXqrpe%2BPPPy1%2Bp%2B1CqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp12MrArAWOG5aipuKtwDpJL5%2FaxFH4Vlrvnlks9vPMHBc5YJ%2F16r6BO%2B64UI%2Bud2zPs%2FCsBof6udK8UKxFBFp06iNzYtzXU8NI6cA5O3%2BoTzec8tWmjpwZDYaGr2PoSduG90zWao6IBYXb08dYDxkCK6UQ5wF1GJJUniOPZczRhajwA7rJSlcCJanrYBE%2Bw0ftTIF5JVEl6SbyRe4veDoTF6p%2FopQwjpwF6%2FSaPAEs%2FcgbdXPsTg0Fk3AajmuHAKrT7im%2FFJ1vxzgil8H%2Bin1h%2B4CXul6Z55i6F0mVU2%2B0D1Q%2FHZqVh%2BABQXm2KEfPlWf35JTow1cxaDjbqhKvK8C%2FR8uhmhWtZOgFlct%2BbHvDRH1coff45FjmwwBiramX1jUijvAUu6kGobEoC%2BM%2FB54PTCAZn81tTOCWLrVcaYFHNs5X6l5%2Bf7CHV4uRoCw1EeWOs0dmsAyy7MKG5hc1bZG0Kah%2FFhQVCTQKeQ2Xf2fida2Zm1kFewUeTg98eNq9Kn6Ujg2nE738ryBMknQDUSL7NH5PuXcYrjXKpI2kdQAFAfZI3pAlmUqgIHXboTDY%2FIh08A6BHkdHODEUFV3Qjm5LmcCtaOTyAB90tAxDwj1Qel6L5tiITSA5c4Yt5HKeeFKV6HOXLudZtba7swv7H6vAY6pgFbdE4Ap67rpHK%2BSakrLuu5omgu5mrL6z%2FJ4jA%2FnOf2IgV%2FRwnpXLbE8XLHhfMUXU5GhRo7xA0zZpwThn2R2EC3XvqfH8ZtUlcpQ5eMbrw2PRCDz%2BibqHL3hOKnl3vlbZMpYJUvmfrQKz4f9L%2BR1vxmmntVByTdsa9XTQ5v0g5s0jwdPzse%2BEr3zQ2nIxgLi1xl6CxLPyVzTP6s9SqJHSHsDizdskd9&X-Amz-Signature=d8d73f5e8152ab32faf4f5ea156f7273519e16367cf4d5326dca201439d5ddcd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U5IPVSD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOhE2yfZfjqWxPs5E5dy3viQFzjZ%2FPQ%2BPwOO4dEbFA5AiARAvk3c6n4sLQaQ0nJ2tAlDIwZkjXqrpe%2BPPPy1%2Bp%2B1CqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp12MrArAWOG5aipuKtwDpJL5%2FaxFH4Vlrvnlks9vPMHBc5YJ%2F16r6BO%2B64UI%2Bud2zPs%2FCsBof6udK8UKxFBFp06iNzYtzXU8NI6cA5O3%2BoTzec8tWmjpwZDYaGr2PoSduG90zWao6IBYXb08dYDxkCK6UQ5wF1GJJUniOPZczRhajwA7rJSlcCJanrYBE%2Bw0ftTIF5JVEl6SbyRe4veDoTF6p%2FopQwjpwF6%2FSaPAEs%2FcgbdXPsTg0Fk3AajmuHAKrT7im%2FFJ1vxzgil8H%2Bin1h%2B4CXul6Z55i6F0mVU2%2B0D1Q%2FHZqVh%2BABQXm2KEfPlWf35JTow1cxaDjbqhKvK8C%2FR8uhmhWtZOgFlct%2BbHvDRH1coff45FjmwwBiramX1jUijvAUu6kGobEoC%2BM%2FB54PTCAZn81tTOCWLrVcaYFHNs5X6l5%2Bf7CHV4uRoCw1EeWOs0dmsAyy7MKG5hc1bZG0Kah%2FFhQVCTQKeQ2Xf2fida2Zm1kFewUeTg98eNq9Kn6Ujg2nE738ryBMknQDUSL7NH5PuXcYrjXKpI2kdQAFAfZI3pAlmUqgIHXboTDY%2FIh08A6BHkdHODEUFV3Qjm5LmcCtaOTyAB90tAxDwj1Qel6L5tiITSA5c4Yt5HKeeFKV6HOXLudZtba7swv7H6vAY6pgFbdE4Ap67rpHK%2BSakrLuu5omgu5mrL6z%2FJ4jA%2FnOf2IgV%2FRwnpXLbE8XLHhfMUXU5GhRo7xA0zZpwThn2R2EC3XvqfH8ZtUlcpQ5eMbrw2PRCDz%2BibqHL3hOKnl3vlbZMpYJUvmfrQKz4f9L%2BR1vxmmntVByTdsa9XTQ5v0g5s0jwdPzse%2BEr3zQ2nIxgLi1xl6CxLPyVzTP6s9SqJHSHsDizdskd9&X-Amz-Signature=8a7f075ffd503c213a27c14e753f6143d034085318418de299110ecbbf20cdc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWOG7WO6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF5pUu%2BHj%2BolOavWAtKWUOgBSETnyHNPksOl%2Fe6iS04tAiBMJg6%2FrdRytmq5NmVxnWZ2TFPqtS3OOz1%2BqUw4wysGuiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWqItPs6CadIA6P8KtwDWDdjLpJiH6WOg7oCSOWYdLFoMPrTtyr5Qjt0%2FgeM6H8oWw3eRWKii102WQdWV5cwoxKKw2ISXKeOV9HaildSkiiCPD3MYc6WejC3V4mh2nKt%2F%2F8%2B3Vj9PSVH%2BWdfTevHzH3JlESHFjSeWOiq7AvcNZLiMr9cP6v61JvFPprqfUsgQkQh6JE6Kbbgd8dHm5XWyiHYOK1WArBS6IBxYJ7nv7M%2B44bukUTpheODM7fP6Lf41IwlivnEf5lOHI%2BgE0uI1dHUPMcot6J51rbaEKlCEVRJ8wtZVi7JP%2F7E1Dy6xWKIgOZ1bKBf5garWQJ0iamN%2BMdVNXpmiqnUn8EgSgXrgmg5QFTJrDSPr7pIO1ldu%2B7mRBIsAkz5%2Bd0%2BU9OJBhzyzdR0%2B%2Fz4ER2E90T0zIz%2BNeuQKq6syXpZ7usSYbZQUmXPsIU0WxWz9pRVWjPFLT0QgWmkUPCRd8zLoWsnS%2BNNHjHqtmZzp%2BRwMUBgfZst1pLWbckzqTp4Knsny9s4ReVm1TyYZPw9EwFZcXT9UPZ6xsA6NRXiOOXZuRK0h5zYk69VdttGpYbfoX0VVK0sMCjEwobFnadQRIVbM%2Bk7x0LlCRTHOxonWr7vjn5oNalHfIY6YtulZ0ADzkBAxZAwtrH6vAY6pgE2lyqCHEFKwEXcQOVZcj5xgUESvfWHA65FhCBjFgGErI%2Fu8Ea1336ITGdrS62P03SnIHmgVS2nuz3lQ7uvnqfKvD7ceXvz%2FGo0%2FL0GnflweNwqjLkwA8vVJccYPkKadINpBn%2FUwVqUVoWWSRWkodZYrh3k6dV%2F7IGHSUu7SeAW6SFvU62gKPZyLzznYftR7zgNKS3sMwDf7Hro1GclTxubFH3JQAkY&X-Amz-Signature=a88c61948a540dcf3ae4b13000b3449c0d5619a455cd6f3de77348fd76bd32d2&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWOG7WO6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF5pUu%2BHj%2BolOavWAtKWUOgBSETnyHNPksOl%2Fe6iS04tAiBMJg6%2FrdRytmq5NmVxnWZ2TFPqtS3OOz1%2BqUw4wysGuiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWqItPs6CadIA6P8KtwDWDdjLpJiH6WOg7oCSOWYdLFoMPrTtyr5Qjt0%2FgeM6H8oWw3eRWKii102WQdWV5cwoxKKw2ISXKeOV9HaildSkiiCPD3MYc6WejC3V4mh2nKt%2F%2F8%2B3Vj9PSVH%2BWdfTevHzH3JlESHFjSeWOiq7AvcNZLiMr9cP6v61JvFPprqfUsgQkQh6JE6Kbbgd8dHm5XWyiHYOK1WArBS6IBxYJ7nv7M%2B44bukUTpheODM7fP6Lf41IwlivnEf5lOHI%2BgE0uI1dHUPMcot6J51rbaEKlCEVRJ8wtZVi7JP%2F7E1Dy6xWKIgOZ1bKBf5garWQJ0iamN%2BMdVNXpmiqnUn8EgSgXrgmg5QFTJrDSPr7pIO1ldu%2B7mRBIsAkz5%2Bd0%2BU9OJBhzyzdR0%2B%2Fz4ER2E90T0zIz%2BNeuQKq6syXpZ7usSYbZQUmXPsIU0WxWz9pRVWjPFLT0QgWmkUPCRd8zLoWsnS%2BNNHjHqtmZzp%2BRwMUBgfZst1pLWbckzqTp4Knsny9s4ReVm1TyYZPw9EwFZcXT9UPZ6xsA6NRXiOOXZuRK0h5zYk69VdttGpYbfoX0VVK0sMCjEwobFnadQRIVbM%2Bk7x0LlCRTHOxonWr7vjn5oNalHfIY6YtulZ0ADzkBAxZAwtrH6vAY6pgE2lyqCHEFKwEXcQOVZcj5xgUESvfWHA65FhCBjFgGErI%2Fu8Ea1336ITGdrS62P03SnIHmgVS2nuz3lQ7uvnqfKvD7ceXvz%2FGo0%2FL0GnflweNwqjLkwA8vVJccYPkKadINpBn%2FUwVqUVoWWSRWkodZYrh3k6dV%2F7IGHSUu7SeAW6SFvU62gKPZyLzznYftR7zgNKS3sMwDf7Hro1GclTxubFH3JQAkY&X-Amz-Signature=c7642de69fe370321d07883cfdcee1243f0b71f8ed95d4b1ffc567f9b8009d3b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWOG7WO6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF5pUu%2BHj%2BolOavWAtKWUOgBSETnyHNPksOl%2Fe6iS04tAiBMJg6%2FrdRytmq5NmVxnWZ2TFPqtS3OOz1%2BqUw4wysGuiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWqItPs6CadIA6P8KtwDWDdjLpJiH6WOg7oCSOWYdLFoMPrTtyr5Qjt0%2FgeM6H8oWw3eRWKii102WQdWV5cwoxKKw2ISXKeOV9HaildSkiiCPD3MYc6WejC3V4mh2nKt%2F%2F8%2B3Vj9PSVH%2BWdfTevHzH3JlESHFjSeWOiq7AvcNZLiMr9cP6v61JvFPprqfUsgQkQh6JE6Kbbgd8dHm5XWyiHYOK1WArBS6IBxYJ7nv7M%2B44bukUTpheODM7fP6Lf41IwlivnEf5lOHI%2BgE0uI1dHUPMcot6J51rbaEKlCEVRJ8wtZVi7JP%2F7E1Dy6xWKIgOZ1bKBf5garWQJ0iamN%2BMdVNXpmiqnUn8EgSgXrgmg5QFTJrDSPr7pIO1ldu%2B7mRBIsAkz5%2Bd0%2BU9OJBhzyzdR0%2B%2Fz4ER2E90T0zIz%2BNeuQKq6syXpZ7usSYbZQUmXPsIU0WxWz9pRVWjPFLT0QgWmkUPCRd8zLoWsnS%2BNNHjHqtmZzp%2BRwMUBgfZst1pLWbckzqTp4Knsny9s4ReVm1TyYZPw9EwFZcXT9UPZ6xsA6NRXiOOXZuRK0h5zYk69VdttGpYbfoX0VVK0sMCjEwobFnadQRIVbM%2Bk7x0LlCRTHOxonWr7vjn5oNalHfIY6YtulZ0ADzkBAxZAwtrH6vAY6pgE2lyqCHEFKwEXcQOVZcj5xgUESvfWHA65FhCBjFgGErI%2Fu8Ea1336ITGdrS62P03SnIHmgVS2nuz3lQ7uvnqfKvD7ceXvz%2FGo0%2FL0GnflweNwqjLkwA8vVJccYPkKadINpBn%2FUwVqUVoWWSRWkodZYrh3k6dV%2F7IGHSUu7SeAW6SFvU62gKPZyLzznYftR7zgNKS3sMwDf7Hro1GclTxubFH3JQAkY&X-Amz-Signature=6a0f41e49cc76dd76918f49ac63c0b2461afac1042489799fc45e66baf82c60e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

