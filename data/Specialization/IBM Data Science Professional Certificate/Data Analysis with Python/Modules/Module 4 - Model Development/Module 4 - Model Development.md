

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=2a7b82f034b7f602075bf572febb6ed2f99828416afaf93736c6e63c7677c23f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=28d5df263789dce626be9e04e8b9a7e439d03e7dd050fd3ec819efab8833f39b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=723a0d260b5b746627f5fb4f3ace38a74aab6b02fbb7110f1eeeff21e78fc95a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=31e70e45546ab2a540ed5bd75de9ded743c1e79bf4b32acebab096c3e9749135&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=74c6054d84e9334d84e6b7b39e51481a4a5a028cba4865d06d0c878fe12fcb4e&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=c1a29d56da7e3921b1a6203fc531d638faec438dea7e88ded0ddd2ce59794859&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=ed3e07f1becc0fdf931237041d10d3523de7dfb025277d7bbd40051086696d54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=0fc31505012d81d06d3da64c94fe96a7872c5ed4ac4f4fda801c2e004958269b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=93ca9f8c386cbda1fc8a4f878181faaf5de34e33b5c47d3857b16486d2f3a1b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=07160ac20fa41b498b73044e9ffb4d43d87ae4b2c95f8eb08ff3faa99dc31a22&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=7cc61f5b25d96996ae8556e4776deb647868b835d9dbf9f54fe114592a195876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644C5T6PN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM7SGMc8I1OyFzMT%2B2elFWtfyrGk4QwxEVvsaHW81m1AiAb58somW4EX%2BXL6zTZEYjLF5CDqBEAcuwTrAn%2FkSji%2BCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVzVNeOJLSYJ%2BSWLhKtwDZYKX%2BNhIM%2BVBumR7KwwEIIrvGh%2BAAy0ilauf90h6iWR35so7idltDuASC3dBhN12i9v27nz0xqUHKieg21HyCGkC9dsYukWkP7MKwmpRK499vjPEDN7359ucQ6C8iU3ikj56BcLrtxhDL%2BkSV%2BgZ%2BfLRKECcPyt2Fadsf0DcX3GqtCfYjWUnbDCnVR2ea6YwYq25ZIdroDeAjN95jMPO5WdGrjzMje9EJDQvq4TtT6kHn3msz0RELjJA2wTh5i%2BvpW6eCfYk8p4cN6t4tcy%2BVMjtKWEWPTpUzRwnn%2BJqTRXGel1NdeHbRg3Zd6DqmVnarZC8zR0vzAbFoeZn0Z0o1Z1k2aiud9o9LXnXoRMY5WoRg7nEOO5fMXlMJ44aZ9b2qqd8To%2FllTZWmFnJrrLa4nEiC3MiJpIPBdHrEn5Kf96bB88PLM176L%2BZKE5xEE5qKPt2EevYq72k%2BlkHYfchlZpyR1GeTcbSzq8sh82WERHTOHZ6fAB7VodiEq1qH7v0ODTEf3IE3mYIDap1vyaFp69hyfTyQweVUTuvd%2B0HfEFAT3kY2UPLTu2HrCDtmZ1bt78FtIVkYkRMJKDIWKQUrTEe0WmpA%2F1xFxPQUej1rHRkBTybbYRATG1hV1gwxtDwvAY6pgG53fX1lK9jlwmuJ31BgfgXPEzQdmm%2BqDDj1ItDTTshxLmTM2jSqvFmU7uPdYsYMwRBXHd4jmRREp8VDbLyr2PexG4GWGsCS2n5egAnpmQWKerIZADJrWOSYliBWkY3L0HOo9PXlFtvlJTrx64TOhUnhcGYIdgDEljYNiaf1Y85TNyLoSEo%2Bt0zZfQ4DfNayyEOBF0SgZLwcwrmVnaHAgTYbIW0ZJla&X-Amz-Signature=2d810f33d72e83f18cc07a395448387acc011843aa9b9e74e0cb56b18a001760&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644C5T6PN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM7SGMc8I1OyFzMT%2B2elFWtfyrGk4QwxEVvsaHW81m1AiAb58somW4EX%2BXL6zTZEYjLF5CDqBEAcuwTrAn%2FkSji%2BCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVzVNeOJLSYJ%2BSWLhKtwDZYKX%2BNhIM%2BVBumR7KwwEIIrvGh%2BAAy0ilauf90h6iWR35so7idltDuASC3dBhN12i9v27nz0xqUHKieg21HyCGkC9dsYukWkP7MKwmpRK499vjPEDN7359ucQ6C8iU3ikj56BcLrtxhDL%2BkSV%2BgZ%2BfLRKECcPyt2Fadsf0DcX3GqtCfYjWUnbDCnVR2ea6YwYq25ZIdroDeAjN95jMPO5WdGrjzMje9EJDQvq4TtT6kHn3msz0RELjJA2wTh5i%2BvpW6eCfYk8p4cN6t4tcy%2BVMjtKWEWPTpUzRwnn%2BJqTRXGel1NdeHbRg3Zd6DqmVnarZC8zR0vzAbFoeZn0Z0o1Z1k2aiud9o9LXnXoRMY5WoRg7nEOO5fMXlMJ44aZ9b2qqd8To%2FllTZWmFnJrrLa4nEiC3MiJpIPBdHrEn5Kf96bB88PLM176L%2BZKE5xEE5qKPt2EevYq72k%2BlkHYfchlZpyR1GeTcbSzq8sh82WERHTOHZ6fAB7VodiEq1qH7v0ODTEf3IE3mYIDap1vyaFp69hyfTyQweVUTuvd%2B0HfEFAT3kY2UPLTu2HrCDtmZ1bt78FtIVkYkRMJKDIWKQUrTEe0WmpA%2F1xFxPQUej1rHRkBTybbYRATG1hV1gwxtDwvAY6pgG53fX1lK9jlwmuJ31BgfgXPEzQdmm%2BqDDj1ItDTTshxLmTM2jSqvFmU7uPdYsYMwRBXHd4jmRREp8VDbLyr2PexG4GWGsCS2n5egAnpmQWKerIZADJrWOSYliBWkY3L0HOo9PXlFtvlJTrx64TOhUnhcGYIdgDEljYNiaf1Y85TNyLoSEo%2Bt0zZfQ4DfNayyEOBF0SgZLwcwrmVnaHAgTYbIW0ZJla&X-Amz-Signature=a3d3721735d10608e3b8f3340fe2d5ac5a0129c0d62e1934c67c468966283fd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644C5T6PN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM7SGMc8I1OyFzMT%2B2elFWtfyrGk4QwxEVvsaHW81m1AiAb58somW4EX%2BXL6zTZEYjLF5CDqBEAcuwTrAn%2FkSji%2BCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVzVNeOJLSYJ%2BSWLhKtwDZYKX%2BNhIM%2BVBumR7KwwEIIrvGh%2BAAy0ilauf90h6iWR35so7idltDuASC3dBhN12i9v27nz0xqUHKieg21HyCGkC9dsYukWkP7MKwmpRK499vjPEDN7359ucQ6C8iU3ikj56BcLrtxhDL%2BkSV%2BgZ%2BfLRKECcPyt2Fadsf0DcX3GqtCfYjWUnbDCnVR2ea6YwYq25ZIdroDeAjN95jMPO5WdGrjzMje9EJDQvq4TtT6kHn3msz0RELjJA2wTh5i%2BvpW6eCfYk8p4cN6t4tcy%2BVMjtKWEWPTpUzRwnn%2BJqTRXGel1NdeHbRg3Zd6DqmVnarZC8zR0vzAbFoeZn0Z0o1Z1k2aiud9o9LXnXoRMY5WoRg7nEOO5fMXlMJ44aZ9b2qqd8To%2FllTZWmFnJrrLa4nEiC3MiJpIPBdHrEn5Kf96bB88PLM176L%2BZKE5xEE5qKPt2EevYq72k%2BlkHYfchlZpyR1GeTcbSzq8sh82WERHTOHZ6fAB7VodiEq1qH7v0ODTEf3IE3mYIDap1vyaFp69hyfTyQweVUTuvd%2B0HfEFAT3kY2UPLTu2HrCDtmZ1bt78FtIVkYkRMJKDIWKQUrTEe0WmpA%2F1xFxPQUej1rHRkBTybbYRATG1hV1gwxtDwvAY6pgG53fX1lK9jlwmuJ31BgfgXPEzQdmm%2BqDDj1ItDTTshxLmTM2jSqvFmU7uPdYsYMwRBXHd4jmRREp8VDbLyr2PexG4GWGsCS2n5egAnpmQWKerIZADJrWOSYliBWkY3L0HOo9PXlFtvlJTrx64TOhUnhcGYIdgDEljYNiaf1Y85TNyLoSEo%2Bt0zZfQ4DfNayyEOBF0SgZLwcwrmVnaHAgTYbIW0ZJla&X-Amz-Signature=2345e6ac384ca4a08e1daa43f8df67d21b3fbaf9ab4cd4adf6d03036570ce56b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644C5T6PN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM7SGMc8I1OyFzMT%2B2elFWtfyrGk4QwxEVvsaHW81m1AiAb58somW4EX%2BXL6zTZEYjLF5CDqBEAcuwTrAn%2FkSji%2BCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVzVNeOJLSYJ%2BSWLhKtwDZYKX%2BNhIM%2BVBumR7KwwEIIrvGh%2BAAy0ilauf90h6iWR35so7idltDuASC3dBhN12i9v27nz0xqUHKieg21HyCGkC9dsYukWkP7MKwmpRK499vjPEDN7359ucQ6C8iU3ikj56BcLrtxhDL%2BkSV%2BgZ%2BfLRKECcPyt2Fadsf0DcX3GqtCfYjWUnbDCnVR2ea6YwYq25ZIdroDeAjN95jMPO5WdGrjzMje9EJDQvq4TtT6kHn3msz0RELjJA2wTh5i%2BvpW6eCfYk8p4cN6t4tcy%2BVMjtKWEWPTpUzRwnn%2BJqTRXGel1NdeHbRg3Zd6DqmVnarZC8zR0vzAbFoeZn0Z0o1Z1k2aiud9o9LXnXoRMY5WoRg7nEOO5fMXlMJ44aZ9b2qqd8To%2FllTZWmFnJrrLa4nEiC3MiJpIPBdHrEn5Kf96bB88PLM176L%2BZKE5xEE5qKPt2EevYq72k%2BlkHYfchlZpyR1GeTcbSzq8sh82WERHTOHZ6fAB7VodiEq1qH7v0ODTEf3IE3mYIDap1vyaFp69hyfTyQweVUTuvd%2B0HfEFAT3kY2UPLTu2HrCDtmZ1bt78FtIVkYkRMJKDIWKQUrTEe0WmpA%2F1xFxPQUej1rHRkBTybbYRATG1hV1gwxtDwvAY6pgG53fX1lK9jlwmuJ31BgfgXPEzQdmm%2BqDDj1ItDTTshxLmTM2jSqvFmU7uPdYsYMwRBXHd4jmRREp8VDbLyr2PexG4GWGsCS2n5egAnpmQWKerIZADJrWOSYliBWkY3L0HOo9PXlFtvlJTrx64TOhUnhcGYIdgDEljYNiaf1Y85TNyLoSEo%2Bt0zZfQ4DfNayyEOBF0SgZLwcwrmVnaHAgTYbIW0ZJla&X-Amz-Signature=18a5b756efc6a8d17c79ee900be9929477f35fee00584674fc634f261619b651&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGINNF6V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbbic3Y%2BQPmDyxs2bGOAnelyNeyuGGroq1VnanW4nawwIhAM87DrPCEYxredCUJ%2Fq%2FJ9WvoEpVx69m8qlWUmJ4obVEKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIe0dB8mdNZIEk4qcq3AOpxkGA%2FC%2FpVJPFMmpqa3y4pOIMWyNnphDnEObUZF1UubxyfBKGZWc4wMpjwpT5Yth3wiNLmB%2Bocq1I01X8C0lDbftm%2F5Fug7wOpvWcjZ4%2Fn5%2FztVIAJvIkYE50yCiob7JL%2BBijrnCNPTtQmkwWHwvoOOOqBL4HRpwLeuu6bcEb5MZj5%2F8OcTz9bASbjSy2wUnduXP8gdyhaX%2F%2BoESrK4o96oYcgbqoJ5qapZeUvn2HSiWMBHPiyYaT1Ov9GJA2urlS40vUFkbJUf%2FR320ZYoaQxmCGKmOX8nNHtpO9BRrpfw%2F%2FlFjpJ98397%2FVgnAi3bmBaL8phdGbgAo374zbesY0akzuBrFOSUOB8arF%2BiuIsQPeGHutXzEnFUL1vf2Q3rD9g%2FxbxtXCnujnYBC7bVGfOEGCGIGFLpY8QwIfNH9o%2Fq8ci7YNIT0f9uIafDeBnv3MGI3WQkpu64H9eSdDbMfWG5m0a07FcM0ZtcVB41lfmRwOq53QUo9fJ0V8zI8jf%2BhlcmL%2BEnQWtuQvaseApXDXCKMsP31oanJxfG9nxVSxyk9q%2FUZ%2FXdpPdFkcos%2FsnlCyAfTZ7yhFbTKdcekPcJI5F78uR%2FcxSuiVm3aOS%2FmgjqUzgqL53Vpzbbbv7DCH0PC8BjqkAUIhL8FYMq6Rk9yVkoXpwYDiDVeybEhmguIN7jkItRY0Tz6TfUNvN9k8nTGp3JmZ6QzLS8sn3DbxKyOPhbcyDOV9f%2FLUK8XCte7wc%2BwEQiMhHVd0NOdkdjWcosLb8qwtBFkc7%2BDJjGnqkL1yKC0Tr9DvR0xRMlaCXpW9t0kpn3bi724A6c18kXUGwzYuCUwu4krnunie0EEOr0nDOD9fu98uRxOs&X-Amz-Signature=d5416c04a3765d6e888f5a04d12333f7cb0b8de05e6d2ecaa55e1e9d6a02f74b&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGINNF6V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbbic3Y%2BQPmDyxs2bGOAnelyNeyuGGroq1VnanW4nawwIhAM87DrPCEYxredCUJ%2Fq%2FJ9WvoEpVx69m8qlWUmJ4obVEKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIe0dB8mdNZIEk4qcq3AOpxkGA%2FC%2FpVJPFMmpqa3y4pOIMWyNnphDnEObUZF1UubxyfBKGZWc4wMpjwpT5Yth3wiNLmB%2Bocq1I01X8C0lDbftm%2F5Fug7wOpvWcjZ4%2Fn5%2FztVIAJvIkYE50yCiob7JL%2BBijrnCNPTtQmkwWHwvoOOOqBL4HRpwLeuu6bcEb5MZj5%2F8OcTz9bASbjSy2wUnduXP8gdyhaX%2F%2BoESrK4o96oYcgbqoJ5qapZeUvn2HSiWMBHPiyYaT1Ov9GJA2urlS40vUFkbJUf%2FR320ZYoaQxmCGKmOX8nNHtpO9BRrpfw%2F%2FlFjpJ98397%2FVgnAi3bmBaL8phdGbgAo374zbesY0akzuBrFOSUOB8arF%2BiuIsQPeGHutXzEnFUL1vf2Q3rD9g%2FxbxtXCnujnYBC7bVGfOEGCGIGFLpY8QwIfNH9o%2Fq8ci7YNIT0f9uIafDeBnv3MGI3WQkpu64H9eSdDbMfWG5m0a07FcM0ZtcVB41lfmRwOq53QUo9fJ0V8zI8jf%2BhlcmL%2BEnQWtuQvaseApXDXCKMsP31oanJxfG9nxVSxyk9q%2FUZ%2FXdpPdFkcos%2FsnlCyAfTZ7yhFbTKdcekPcJI5F78uR%2FcxSuiVm3aOS%2FmgjqUzgqL53Vpzbbbv7DCH0PC8BjqkAUIhL8FYMq6Rk9yVkoXpwYDiDVeybEhmguIN7jkItRY0Tz6TfUNvN9k8nTGp3JmZ6QzLS8sn3DbxKyOPhbcyDOV9f%2FLUK8XCte7wc%2BwEQiMhHVd0NOdkdjWcosLb8qwtBFkc7%2BDJjGnqkL1yKC0Tr9DvR0xRMlaCXpW9t0kpn3bi724A6c18kXUGwzYuCUwu4krnunie0EEOr0nDOD9fu98uRxOs&X-Amz-Signature=498cfe974d8f74bacfde6c1632f805fed5cf1caf1e9afdca1c7e70ba327b4dff&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGINNF6V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbbic3Y%2BQPmDyxs2bGOAnelyNeyuGGroq1VnanW4nawwIhAM87DrPCEYxredCUJ%2Fq%2FJ9WvoEpVx69m8qlWUmJ4obVEKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIe0dB8mdNZIEk4qcq3AOpxkGA%2FC%2FpVJPFMmpqa3y4pOIMWyNnphDnEObUZF1UubxyfBKGZWc4wMpjwpT5Yth3wiNLmB%2Bocq1I01X8C0lDbftm%2F5Fug7wOpvWcjZ4%2Fn5%2FztVIAJvIkYE50yCiob7JL%2BBijrnCNPTtQmkwWHwvoOOOqBL4HRpwLeuu6bcEb5MZj5%2F8OcTz9bASbjSy2wUnduXP8gdyhaX%2F%2BoESrK4o96oYcgbqoJ5qapZeUvn2HSiWMBHPiyYaT1Ov9GJA2urlS40vUFkbJUf%2FR320ZYoaQxmCGKmOX8nNHtpO9BRrpfw%2F%2FlFjpJ98397%2FVgnAi3bmBaL8phdGbgAo374zbesY0akzuBrFOSUOB8arF%2BiuIsQPeGHutXzEnFUL1vf2Q3rD9g%2FxbxtXCnujnYBC7bVGfOEGCGIGFLpY8QwIfNH9o%2Fq8ci7YNIT0f9uIafDeBnv3MGI3WQkpu64H9eSdDbMfWG5m0a07FcM0ZtcVB41lfmRwOq53QUo9fJ0V8zI8jf%2BhlcmL%2BEnQWtuQvaseApXDXCKMsP31oanJxfG9nxVSxyk9q%2FUZ%2FXdpPdFkcos%2FsnlCyAfTZ7yhFbTKdcekPcJI5F78uR%2FcxSuiVm3aOS%2FmgjqUzgqL53Vpzbbbv7DCH0PC8BjqkAUIhL8FYMq6Rk9yVkoXpwYDiDVeybEhmguIN7jkItRY0Tz6TfUNvN9k8nTGp3JmZ6QzLS8sn3DbxKyOPhbcyDOV9f%2FLUK8XCte7wc%2BwEQiMhHVd0NOdkdjWcosLb8qwtBFkc7%2BDJjGnqkL1yKC0Tr9DvR0xRMlaCXpW9t0kpn3bi724A6c18kXUGwzYuCUwu4krnunie0EEOr0nDOD9fu98uRxOs&X-Amz-Signature=fba5f13c132a03f8c29ba5a7ebb79f286660e25f1f8ae2418fe87df277d9613f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

