

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=293a0ea20a15a76af1ded43f60910cba5543958ce98ed6fa4c278e6d1d4e3c72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=e417aee89491fad27ae26cb61750c3dccc9417cf0b34443288388cbb69dfad03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=43c2d50340e5a3220847dcc4237c868e85ad7e7ccd91e64088c2dfeeb7888bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=1acbc54479c798284bb72ab7f316f1b586e7af32ed9934cfabb7bd5dbbcfec0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=2b27e3cc72800ff735a60d0ba6755106aef7464ce03700b948b32a98ab617c90&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=800e4c179e1835bdfa3866fe293f74e404e40c78937b0c5e76a1d45b4470f42a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=81296ceeb697cb92863b962996094fca18ddf02d0427b6ebca57e8adc998c6bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=ac4bd4e0ea76ad817630ae1f25fc93ef80038bc73568555bb4d60686ba5bfa8f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=d65332410697f8c83e584c8ba616a2ea8e920d71e5f90b726fc03fcd97ae888f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=dd17a3a58d20dc09abbce0776d87c55ad4435a282e73141ab0b632ee114c7649&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JEAOH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE4YCkuPaT9JLN11E5q1O%2F6NxDMtbwnbju%2Bn3ayUx65PAiEA6DTKlU4ppMs6Ro86rAFVoD7%2FgXcAdGe04ozGUlwQoT8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDBlvH0iUv0uyx2vz2yrcA4SUhPy6No2n1Y3xWOFl4KJZhD7F3aSxUPrS0pwraU7bIx83uD%2FVjiwbggbVrJ1SMnQTzAMsVe6of%2FgGPbNAtU4cl2E%2FQRLIcrQmS%2BnAmW4yloGu6fgLSxvYV1VWuRS9mxXQXGgbbSPN8ez4fLNN5uZFLC%2BevS9cPsFtT6xpnS6N9nkSL0nF39IcrhhTijJwUKnxfS7IGYJcRlrUDugnNfI%2Bdgfk0AtyqRlUTI4FlRvRFCLykaZ3%2BLyWMHJTBZhDfe7IpPoAZ8SAeRW4ZCcJzs9GowWPvTBbIfkP3IAEUVpxqNhBIb%2FuhRlJKHWz7kKt%2FVn52qsBXUEPEbqS0SvOqThoKt%2FmxcNLqh8Xcid%2B0zs976AqyNuFX%2BYJzp49RRmh%2FZhS9gRGIzd5cndsKHG8YRxsixQzBCOiw%2BtseLlbvrHuMED0KL%2FOBHHvNWlmpT0DkHL7l1mm%2BH3lSReou54UPIcrNtYZmbDKGVqBjsuoioDOtyxfsNQmokfauh6HxDDe3Wk8vZzWfX9L%2FepDVWnLVtsZ09X1NPDwCdDD80Q%2FQE5T%2FgSOS25QP0IjUPVynm1ElJz3QmyQKAsTW8GWEl%2BHMC7IwJyRvMg%2BZPfiHPFWC1hDzI5hZg3TORRCObEqMNWRh70GOqUBgMGaRhXjYO%2BVBaEz5ENLlAjk%2BgridCJyDdQbN318MGHVL5uktwGRurrkzAsIdqUfR9ENclfszVCdM5tiQtX%2BR2h590JjQlOWosBilgc4%2BB5E5r6hXoksbAk9sWJ3Whu%2BZna2I2bt8VvppUEwwNqoQRDx9%2BIDI8s%2BKMwxxvYkryWTiO1WHJpj2TiM2wzoY5JKNho7PX2GhylbVJUHOPyCIlh4mhJB&X-Amz-Signature=555e8b1ec5e574d3ec0f6c34821b1219ac717c570400d887e3fc040169650338&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TXDOFW6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIBfjgsijpJzyXGP78pbrtWtnc9bPRNZmuhcYyxIs%2BPVtAiEAoZ9XioBm9KmPtP3smmhcq2R8A0o6ne%2FZ1G1vxKJgVJQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDISvwp3utFVBWjW7nCrcA8IjIs8baUvSbWBCqSb0g7GXyHOu2cXGzRkMqfi9tRK%2FrNCH3I3nslrA9bYv4KDqMlVLeHDshGJtwgdY25SnuFb0gRitkh67UUsWOhuzu%2F1tVGOcnYYcugwg4jpXd31%2FQgSSoo4zqQXd6WF5agoHbFD80s7jUjD9clQqz%2F7Thu93HzaiqeIxnwsyoRXfybkzhgm7jBqaDJ7oz8QlxrMYQWM1QPVw1yuVVMF5jssm5jAj2qrBT7FCdaJ3jL3lSUUHeDRc%2BZdI%2FdpHAnC9G7qFSeSNP1aXPGFXEvaRgyrjEHoYw4lPRsYGd767Wy37DTaJwtai6Pw8jEPuifazKlJxTw1tlRrbecWgHoz3UUnOI0OQ%2B7rW5LLuLbgJZivqDl47%2FsqUWGxIrnNHRBvc4diCV6h4BeD%2FVMDVtcgo4gHLDLYOzYcQNfzC4Hb9U8jAhJQFEcM3ZCftg7TA1hkJdZwdTGDUnOsnWO%2FAo14ndHLX3x8NIia56Ov71T%2FRyUOqY3duQu2mU1yVghv8d46EN%2FRumFewQjf873166j3h08ynavQmPHknGhDyGzrLH8HWRfdeGW4SxW005jzKM8luxCOtxVBS6oOaC8IagaQynLb7PTH5%2BSJ2YGr7X15RSuPbMK6Rh70GOqUB9h2sHby9v%2BOXO09nIIHYbFj1EBSZHvWXqBgOv69KizvK8imUCGYzFTwpZQfHYj3f9X6hu3p10UbLMvUzoJnVeIrRpv0Bq8aBjzm5fYJWsxemogyy%2F4fsGi9HvlwGZRwQlg%2Bs%2BUOzd%2BvIqAyaVMKgArW3eNfqySalOQuqikxQ64IFWwxW8DNTeUln12dEaRxuLmpSt%2F2RwBxdak7QD5IONYhq0MoD&X-Amz-Signature=16698c3babf72f2d290a766acb0b86e84d14d70ba84b5b24ff7594942be6cb9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TXDOFW6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIBfjgsijpJzyXGP78pbrtWtnc9bPRNZmuhcYyxIs%2BPVtAiEAoZ9XioBm9KmPtP3smmhcq2R8A0o6ne%2FZ1G1vxKJgVJQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDISvwp3utFVBWjW7nCrcA8IjIs8baUvSbWBCqSb0g7GXyHOu2cXGzRkMqfi9tRK%2FrNCH3I3nslrA9bYv4KDqMlVLeHDshGJtwgdY25SnuFb0gRitkh67UUsWOhuzu%2F1tVGOcnYYcugwg4jpXd31%2FQgSSoo4zqQXd6WF5agoHbFD80s7jUjD9clQqz%2F7Thu93HzaiqeIxnwsyoRXfybkzhgm7jBqaDJ7oz8QlxrMYQWM1QPVw1yuVVMF5jssm5jAj2qrBT7FCdaJ3jL3lSUUHeDRc%2BZdI%2FdpHAnC9G7qFSeSNP1aXPGFXEvaRgyrjEHoYw4lPRsYGd767Wy37DTaJwtai6Pw8jEPuifazKlJxTw1tlRrbecWgHoz3UUnOI0OQ%2B7rW5LLuLbgJZivqDl47%2FsqUWGxIrnNHRBvc4diCV6h4BeD%2FVMDVtcgo4gHLDLYOzYcQNfzC4Hb9U8jAhJQFEcM3ZCftg7TA1hkJdZwdTGDUnOsnWO%2FAo14ndHLX3x8NIia56Ov71T%2FRyUOqY3duQu2mU1yVghv8d46EN%2FRumFewQjf873166j3h08ynavQmPHknGhDyGzrLH8HWRfdeGW4SxW005jzKM8luxCOtxVBS6oOaC8IagaQynLb7PTH5%2BSJ2YGr7X15RSuPbMK6Rh70GOqUB9h2sHby9v%2BOXO09nIIHYbFj1EBSZHvWXqBgOv69KizvK8imUCGYzFTwpZQfHYj3f9X6hu3p10UbLMvUzoJnVeIrRpv0Bq8aBjzm5fYJWsxemogyy%2F4fsGi9HvlwGZRwQlg%2Bs%2BUOzd%2BvIqAyaVMKgArW3eNfqySalOQuqikxQ64IFWwxW8DNTeUln12dEaRxuLmpSt%2F2RwBxdak7QD5IONYhq0MoD&X-Amz-Signature=94a2ecb957e73c0a2265f582c15a9a9ba6192feb217cfa5a57946640bf02fc4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TXDOFW6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIBfjgsijpJzyXGP78pbrtWtnc9bPRNZmuhcYyxIs%2BPVtAiEAoZ9XioBm9KmPtP3smmhcq2R8A0o6ne%2FZ1G1vxKJgVJQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDISvwp3utFVBWjW7nCrcA8IjIs8baUvSbWBCqSb0g7GXyHOu2cXGzRkMqfi9tRK%2FrNCH3I3nslrA9bYv4KDqMlVLeHDshGJtwgdY25SnuFb0gRitkh67UUsWOhuzu%2F1tVGOcnYYcugwg4jpXd31%2FQgSSoo4zqQXd6WF5agoHbFD80s7jUjD9clQqz%2F7Thu93HzaiqeIxnwsyoRXfybkzhgm7jBqaDJ7oz8QlxrMYQWM1QPVw1yuVVMF5jssm5jAj2qrBT7FCdaJ3jL3lSUUHeDRc%2BZdI%2FdpHAnC9G7qFSeSNP1aXPGFXEvaRgyrjEHoYw4lPRsYGd767Wy37DTaJwtai6Pw8jEPuifazKlJxTw1tlRrbecWgHoz3UUnOI0OQ%2B7rW5LLuLbgJZivqDl47%2FsqUWGxIrnNHRBvc4diCV6h4BeD%2FVMDVtcgo4gHLDLYOzYcQNfzC4Hb9U8jAhJQFEcM3ZCftg7TA1hkJdZwdTGDUnOsnWO%2FAo14ndHLX3x8NIia56Ov71T%2FRyUOqY3duQu2mU1yVghv8d46EN%2FRumFewQjf873166j3h08ynavQmPHknGhDyGzrLH8HWRfdeGW4SxW005jzKM8luxCOtxVBS6oOaC8IagaQynLb7PTH5%2BSJ2YGr7X15RSuPbMK6Rh70GOqUB9h2sHby9v%2BOXO09nIIHYbFj1EBSZHvWXqBgOv69KizvK8imUCGYzFTwpZQfHYj3f9X6hu3p10UbLMvUzoJnVeIrRpv0Bq8aBjzm5fYJWsxemogyy%2F4fsGi9HvlwGZRwQlg%2Bs%2BUOzd%2BvIqAyaVMKgArW3eNfqySalOQuqikxQ64IFWwxW8DNTeUln12dEaRxuLmpSt%2F2RwBxdak7QD5IONYhq0MoD&X-Amz-Signature=32ed7be6ec9c1175a991c59d7657eb49e9c1b04b2ee09e543feef80c25c12d17&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TXDOFW6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIBfjgsijpJzyXGP78pbrtWtnc9bPRNZmuhcYyxIs%2BPVtAiEAoZ9XioBm9KmPtP3smmhcq2R8A0o6ne%2FZ1G1vxKJgVJQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDISvwp3utFVBWjW7nCrcA8IjIs8baUvSbWBCqSb0g7GXyHOu2cXGzRkMqfi9tRK%2FrNCH3I3nslrA9bYv4KDqMlVLeHDshGJtwgdY25SnuFb0gRitkh67UUsWOhuzu%2F1tVGOcnYYcugwg4jpXd31%2FQgSSoo4zqQXd6WF5agoHbFD80s7jUjD9clQqz%2F7Thu93HzaiqeIxnwsyoRXfybkzhgm7jBqaDJ7oz8QlxrMYQWM1QPVw1yuVVMF5jssm5jAj2qrBT7FCdaJ3jL3lSUUHeDRc%2BZdI%2FdpHAnC9G7qFSeSNP1aXPGFXEvaRgyrjEHoYw4lPRsYGd767Wy37DTaJwtai6Pw8jEPuifazKlJxTw1tlRrbecWgHoz3UUnOI0OQ%2B7rW5LLuLbgJZivqDl47%2FsqUWGxIrnNHRBvc4diCV6h4BeD%2FVMDVtcgo4gHLDLYOzYcQNfzC4Hb9U8jAhJQFEcM3ZCftg7TA1hkJdZwdTGDUnOsnWO%2FAo14ndHLX3x8NIia56Ov71T%2FRyUOqY3duQu2mU1yVghv8d46EN%2FRumFewQjf873166j3h08ynavQmPHknGhDyGzrLH8HWRfdeGW4SxW005jzKM8luxCOtxVBS6oOaC8IagaQynLb7PTH5%2BSJ2YGr7X15RSuPbMK6Rh70GOqUB9h2sHby9v%2BOXO09nIIHYbFj1EBSZHvWXqBgOv69KizvK8imUCGYzFTwpZQfHYj3f9X6hu3p10UbLMvUzoJnVeIrRpv0Bq8aBjzm5fYJWsxemogyy%2F4fsGi9HvlwGZRwQlg%2Bs%2BUOzd%2BvIqAyaVMKgArW3eNfqySalOQuqikxQ64IFWwxW8DNTeUln12dEaRxuLmpSt%2F2RwBxdak7QD5IONYhq0MoD&X-Amz-Signature=e4e126369f52e4a3882534ebd6b553f4f3ae74e8fc60277f64bd5e4ed479a6a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMZWNWRB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIEf%2Fx%2BBnYeyCQj4hUl9DtNpA1Y79W3J%2F1SgWIxoaAU%2BeAiEA0cbEWiTpVHRFvDOr3vDo1YDnE2zVGK0d%2BLHy2P54zQMq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDDGcD3w4VWSHxPsD8SrcA7eQ2EgyDWVGIuyF9ZpIKpJovCERMVjrtG%2FGzrPfKriDSb0ShrXEbC3wKPLDGTpBaw0t1vvJvL54AJhKVanpc67NvBnjl9G2Hu3iKaDwHHOso1WTjgDsWf428CyjoSGD7LNc1z3YrHG534m0mODXgDvV08O53hUWL%2B7LN4Na0NsyO%2BGPWrMX117wqlX7Fijy1yl8eTuIphEvwfIHN7aNqTaIpNt1FqTiVox2lbg6w85zGi5IYhzc6%2Bt6Lly103Zkd%2FeIkK5Q1BOtBFJ5KfkTkReao%2BVMoajZvEODNjBkvFnDox6Ys7EiP5KrJ%2BDazd0xO9w%2FN7aApHgi%2FzXe3ag8t4TF0iJOIoM7uuOrCWFrXLHUxJAo6sU4Jv7gLVnTEAe%2FFSIQNCLOFBeOtLL%2BTMHOBiug8rIo5TZ%2FyZ6Z50xf%2FdmfL6KE3IKR2rDM5i66ay0qnvf47%2FnwS9%2BhyzUaD7%2BDlnqGNkF%2BKtqwt1%2B4VHd0PQAnvdjycO4%2FTeRE53q%2BwE6B4U2VOt2oWT%2BSx7di6JbIbHMeN3pUqULTKFKpciL5hoGEtuMTFrAKXr8yOeCrEj7kK6iy%2FuHnsdzWh0jtd52%2FuJ8ca%2BbPyoNxN%2Fv8p0UBr3NiOtToUPYiBPGvS%2BTZMLKSh70GOqUBHJqadOPRjGahvWF26r7Q%2FKqGNp4m5NUEHY5hVDySrlN7VIKYwqqopfeoZIf0aPy2CCtRUQ1qyO5DZHiID35WOimoHgtdvCn1j0RaLoqqXRrNsvMUw0A1g%2F7vqqBhabm0YlWQJGN2vwHgV8qPhu73C6x4aHUlS7rc5ZoqjINumnXML%2Bmk6LWzoRnNsLq7qOY6kWtQxj3UQX6bCZ87w7rMuhFiSZem&X-Amz-Signature=6eaf5df630f1f2563c5a46967bb8bc5d9497c6c89ed17e7ace004867d1e32d63&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMZWNWRB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIEf%2Fx%2BBnYeyCQj4hUl9DtNpA1Y79W3J%2F1SgWIxoaAU%2BeAiEA0cbEWiTpVHRFvDOr3vDo1YDnE2zVGK0d%2BLHy2P54zQMq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDDGcD3w4VWSHxPsD8SrcA7eQ2EgyDWVGIuyF9ZpIKpJovCERMVjrtG%2FGzrPfKriDSb0ShrXEbC3wKPLDGTpBaw0t1vvJvL54AJhKVanpc67NvBnjl9G2Hu3iKaDwHHOso1WTjgDsWf428CyjoSGD7LNc1z3YrHG534m0mODXgDvV08O53hUWL%2B7LN4Na0NsyO%2BGPWrMX117wqlX7Fijy1yl8eTuIphEvwfIHN7aNqTaIpNt1FqTiVox2lbg6w85zGi5IYhzc6%2Bt6Lly103Zkd%2FeIkK5Q1BOtBFJ5KfkTkReao%2BVMoajZvEODNjBkvFnDox6Ys7EiP5KrJ%2BDazd0xO9w%2FN7aApHgi%2FzXe3ag8t4TF0iJOIoM7uuOrCWFrXLHUxJAo6sU4Jv7gLVnTEAe%2FFSIQNCLOFBeOtLL%2BTMHOBiug8rIo5TZ%2FyZ6Z50xf%2FdmfL6KE3IKR2rDM5i66ay0qnvf47%2FnwS9%2BhyzUaD7%2BDlnqGNkF%2BKtqwt1%2B4VHd0PQAnvdjycO4%2FTeRE53q%2BwE6B4U2VOt2oWT%2BSx7di6JbIbHMeN3pUqULTKFKpciL5hoGEtuMTFrAKXr8yOeCrEj7kK6iy%2FuHnsdzWh0jtd52%2FuJ8ca%2BbPyoNxN%2Fv8p0UBr3NiOtToUPYiBPGvS%2BTZMLKSh70GOqUBHJqadOPRjGahvWF26r7Q%2FKqGNp4m5NUEHY5hVDySrlN7VIKYwqqopfeoZIf0aPy2CCtRUQ1qyO5DZHiID35WOimoHgtdvCn1j0RaLoqqXRrNsvMUw0A1g%2F7vqqBhabm0YlWQJGN2vwHgV8qPhu73C6x4aHUlS7rc5ZoqjINumnXML%2Bmk6LWzoRnNsLq7qOY6kWtQxj3UQX6bCZ87w7rMuhFiSZem&X-Amz-Signature=978d7e6eb5dfe9e65027f18f631549099a99ed08e97740f14d030b4e3aa7645b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMZWNWRB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIEf%2Fx%2BBnYeyCQj4hUl9DtNpA1Y79W3J%2F1SgWIxoaAU%2BeAiEA0cbEWiTpVHRFvDOr3vDo1YDnE2zVGK0d%2BLHy2P54zQMq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDDGcD3w4VWSHxPsD8SrcA7eQ2EgyDWVGIuyF9ZpIKpJovCERMVjrtG%2FGzrPfKriDSb0ShrXEbC3wKPLDGTpBaw0t1vvJvL54AJhKVanpc67NvBnjl9G2Hu3iKaDwHHOso1WTjgDsWf428CyjoSGD7LNc1z3YrHG534m0mODXgDvV08O53hUWL%2B7LN4Na0NsyO%2BGPWrMX117wqlX7Fijy1yl8eTuIphEvwfIHN7aNqTaIpNt1FqTiVox2lbg6w85zGi5IYhzc6%2Bt6Lly103Zkd%2FeIkK5Q1BOtBFJ5KfkTkReao%2BVMoajZvEODNjBkvFnDox6Ys7EiP5KrJ%2BDazd0xO9w%2FN7aApHgi%2FzXe3ag8t4TF0iJOIoM7uuOrCWFrXLHUxJAo6sU4Jv7gLVnTEAe%2FFSIQNCLOFBeOtLL%2BTMHOBiug8rIo5TZ%2FyZ6Z50xf%2FdmfL6KE3IKR2rDM5i66ay0qnvf47%2FnwS9%2BhyzUaD7%2BDlnqGNkF%2BKtqwt1%2B4VHd0PQAnvdjycO4%2FTeRE53q%2BwE6B4U2VOt2oWT%2BSx7di6JbIbHMeN3pUqULTKFKpciL5hoGEtuMTFrAKXr8yOeCrEj7kK6iy%2FuHnsdzWh0jtd52%2FuJ8ca%2BbPyoNxN%2Fv8p0UBr3NiOtToUPYiBPGvS%2BTZMLKSh70GOqUBHJqadOPRjGahvWF26r7Q%2FKqGNp4m5NUEHY5hVDySrlN7VIKYwqqopfeoZIf0aPy2CCtRUQ1qyO5DZHiID35WOimoHgtdvCn1j0RaLoqqXRrNsvMUw0A1g%2F7vqqBhabm0YlWQJGN2vwHgV8qPhu73C6x4aHUlS7rc5ZoqjINumnXML%2Bmk6LWzoRnNsLq7qOY6kWtQxj3UQX6bCZ87w7rMuhFiSZem&X-Amz-Signature=14b542855e64805b452f9c5d9db5ec93136cd4e605ea9222aadcfbce6f15d8f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

