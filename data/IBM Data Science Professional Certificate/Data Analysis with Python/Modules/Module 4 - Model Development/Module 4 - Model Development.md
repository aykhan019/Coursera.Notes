

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=a36ac04415a71b3b06111872554bf009c205b1ce41d1fa18a1e5117364a8087a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=a10eecc04e1a134ebd2cef87054020de1995dda717f45006647c62053a8115c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=8715fb13d7248c41fa83a6cf26a5d4431197b6a10428bf1226635df1166a8bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=a72c3b5b75ad62cc9c91a8196f6a72f92eb08f61be7a47b8d2d1e08a4318f9ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=0a89584eed5ef47eea7e6e6b7c7443a707525525b627232283a468f548213dde&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=a343a3af9ce0a5696de458c5d04cc89665499ca108581e5e94b3a07385080912&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=c960ce49159a3c2af29e6e8677642f0e74d55948e06c00f5a65d25a28e7cf046&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=2d3118ddf72186003c9e91e00bfd34130e07c97e0488fb0fe516885a30b6d562&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=b0cf4b7a34907873b90784951790e25d9943691ed97176d5ffbfc3c7b538a6a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=6efc47de61a9f53b4105ec64591fb95d6a0528616c8c46136f971638bb32be85&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646E5MZXB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIFoxA0uFCfKKp9yMt%2BskmsDtWIbhJND6ZYJa%2BM3356rAAiAMAxZ6fMeLNxL%2F%2B3lYLaSZ1JKOm7H05ZL2Rt5nysSJfCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMlDQGCpEWJwXk4WXZKtwDeuxx4ZhyYSaJ%2FCawtvC5rrf4HonYM3ggBw%2ByVPdYLGj3DveMwJ9D7yvRsadzy2OrI4A9F46FDbFNoJjVk9JZOCCWuSZGaf9lrsB6ex41dukNW2G7Js2eEYFDi6OBhgQxxrGMXpHT9v%2FDt0ZYiNPiQcOVL5LfcGWQM1GWb3tNlJqbu%2FxLXsytFVe%2FEIhqGwR%2FK8wKnr8fgVcrNvMRhzHn9wr%2BiluTyFdYiw4%2BR9zEUKBgvn92p5kUO8OWrsO0fqH7vakiIHXYioFZ1CS3ZygNntR9maC6IkS9T6gXoeyKVMtiU46Em7ACEjjwXL7Akou%2FM9UiOsWDreer5CBZ2t0kA%2FelYFJWaWsT3%2BVyWFy1LPSVQ%2BMQZoFw1kPjfkocz%2Bw5yhxpvFGecrz4%2BM3pQLg05nZq%2BPPUqMh%2F0uYk%2BRyrMOsQ9VKuqxJojYQY33nsGT7QxGSSAHgeX6w2gQ08UFlyCih6r4p0BVIFEy%2BCELyqtn%2FUHpvjTK%2FWS4n3zKDhtzPph6La%2FmrM7HON0BHLjw3WSsxsDmP9lTz72%2FbvYTkh5ijrCf58TtRte4W6QHL8NhYb45fnDhhsrwGCmvKcYqBuEBQDLFuK6hBImfqn%2BhvHytD%2ByAeDnYUzxWhQ9wgw8aCJvQY6pgH3bQ1U8JKXch37kARDPP4sR7QT760hy4uV9xEbQKjAFKFRmv%2Fbqkke%2Fm313pJ22lr%2B4vLb9OfG2pYshsJaFAUzmbfsFLGrWtOohkDrXxogeAJAMVRWm866KFSaKlAKPUHhDD8bNnUqjATEsYwHhi5fu70YMHDFosEUREJzqOx%2F%2BlYQQMr%2BFapA6c%2FaaDqlV%2FEeSjpJxfP9LiIJLXV%2Fvojy6%2FcUZw8X&X-Amz-Signature=50bb5e1cf9ccd5bd81410fe1b3f785aeb48fbbcf283aaed8733ed066644cce4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDWSRQSY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCKMmBJUex2BJFZ1hC5vdFjGBBtfC7s4Iwf8ubvp5%2F05wIhAK6AkEvbU3vESK3MkIzH4Uke98Jogum2etRANc0QdY%2FFKv8DCDMQABoMNjM3NDIzMTgzODA1IgyRIf3vVdEw32xdjTsq3AMe07RB7G1hG2UnI0KExyIymSMPPS5ff2WGgd90qOMlBg5eAxvWBhRbGq7pgxLr99GkmJAO9MvCJVAKlZUD3C%2BjZA3eO3W1lD2MNziygn2pdrVpbj55JCKIYzyNxlxHGRs97DJrM9xpvxYXnv7yyYun6xucGn3pK%2BTCbFS6Ox6fVIlV974OfqIrZkBET9RbTQWJqdXTrnWQ5YjzDt%2FI7HO06SvpzTDFTGC1sDOhT6NCHbFYJVKXkvskauCqK5vCehCOmmce15D1v10%2FhTpjLYJthdHDiw4zlpVg6uDy%2BhCxK3IDMFMO%2FpWoFG2F0nG3x%2BT0z0VZn6cu%2F1s82QhyXxcU4fSButdIZ053bgVVs6xtGZ5z6HmVwj3T2Gmi96X4z%2F%2FOQn9hicQ%2FzDpWKP8p1fNOrm%2Bs%2B%2BiD8eaRe2AB%2ByGj%2BtJq6baolvSmTc2TqjxgZymjGyd7BohYGpHGtF6BiBuVx%2FA6r3%2BE00UaFbSE1HlUs5y8Sv3IzpHqS662tLLg%2Fdy1M1KlnYjOV2c8RDzKJ%2BftbfKVmWfPdI8eKOo49NcVTue9ucP8znvoF%2FpMpWa9Yqhiq1wveqbhEWJqUWT%2BAoUUQUiwkNMBkPrN8rK5q7vMzy93b%2FxasH27TaaXmTDZoIm9BjqkAefz1G17vvTFA8X7T84lJtViKRDIEAJgXDchu8DbGAtIPQodATXq5XzDMKQF5VAe34EwlQN1Los8TB75XorkRjF%2BM8UoFK2ImHvnfXWRolFELrGX%2B9pbnFR7AXTt2B45O2gy5RPVjCwJp2KDznoqwZzAO1RLZgvn%2BqQpS%2F2BVru4OP6x%2F8oxpwvMK0%2B92uoUCiUS18vkUmgxvkvfeqm7sz0DSguj&X-Amz-Signature=910f49d2db69e19e83735d03e5c34d8f17857d652f068bb4c410ec2a7177dc81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDWSRQSY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCKMmBJUex2BJFZ1hC5vdFjGBBtfC7s4Iwf8ubvp5%2F05wIhAK6AkEvbU3vESK3MkIzH4Uke98Jogum2etRANc0QdY%2FFKv8DCDMQABoMNjM3NDIzMTgzODA1IgyRIf3vVdEw32xdjTsq3AMe07RB7G1hG2UnI0KExyIymSMPPS5ff2WGgd90qOMlBg5eAxvWBhRbGq7pgxLr99GkmJAO9MvCJVAKlZUD3C%2BjZA3eO3W1lD2MNziygn2pdrVpbj55JCKIYzyNxlxHGRs97DJrM9xpvxYXnv7yyYun6xucGn3pK%2BTCbFS6Ox6fVIlV974OfqIrZkBET9RbTQWJqdXTrnWQ5YjzDt%2FI7HO06SvpzTDFTGC1sDOhT6NCHbFYJVKXkvskauCqK5vCehCOmmce15D1v10%2FhTpjLYJthdHDiw4zlpVg6uDy%2BhCxK3IDMFMO%2FpWoFG2F0nG3x%2BT0z0VZn6cu%2F1s82QhyXxcU4fSButdIZ053bgVVs6xtGZ5z6HmVwj3T2Gmi96X4z%2F%2FOQn9hicQ%2FzDpWKP8p1fNOrm%2Bs%2B%2BiD8eaRe2AB%2ByGj%2BtJq6baolvSmTc2TqjxgZymjGyd7BohYGpHGtF6BiBuVx%2FA6r3%2BE00UaFbSE1HlUs5y8Sv3IzpHqS662tLLg%2Fdy1M1KlnYjOV2c8RDzKJ%2BftbfKVmWfPdI8eKOo49NcVTue9ucP8znvoF%2FpMpWa9Yqhiq1wveqbhEWJqUWT%2BAoUUQUiwkNMBkPrN8rK5q7vMzy93b%2FxasH27TaaXmTDZoIm9BjqkAefz1G17vvTFA8X7T84lJtViKRDIEAJgXDchu8DbGAtIPQodATXq5XzDMKQF5VAe34EwlQN1Los8TB75XorkRjF%2BM8UoFK2ImHvnfXWRolFELrGX%2B9pbnFR7AXTt2B45O2gy5RPVjCwJp2KDznoqwZzAO1RLZgvn%2BqQpS%2F2BVru4OP6x%2F8oxpwvMK0%2B92uoUCiUS18vkUmgxvkvfeqm7sz0DSguj&X-Amz-Signature=d9aa5dc6f199ee9497d42209cb32319cf2856239eb7368f81caee845b69a800e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDWSRQSY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCKMmBJUex2BJFZ1hC5vdFjGBBtfC7s4Iwf8ubvp5%2F05wIhAK6AkEvbU3vESK3MkIzH4Uke98Jogum2etRANc0QdY%2FFKv8DCDMQABoMNjM3NDIzMTgzODA1IgyRIf3vVdEw32xdjTsq3AMe07RB7G1hG2UnI0KExyIymSMPPS5ff2WGgd90qOMlBg5eAxvWBhRbGq7pgxLr99GkmJAO9MvCJVAKlZUD3C%2BjZA3eO3W1lD2MNziygn2pdrVpbj55JCKIYzyNxlxHGRs97DJrM9xpvxYXnv7yyYun6xucGn3pK%2BTCbFS6Ox6fVIlV974OfqIrZkBET9RbTQWJqdXTrnWQ5YjzDt%2FI7HO06SvpzTDFTGC1sDOhT6NCHbFYJVKXkvskauCqK5vCehCOmmce15D1v10%2FhTpjLYJthdHDiw4zlpVg6uDy%2BhCxK3IDMFMO%2FpWoFG2F0nG3x%2BT0z0VZn6cu%2F1s82QhyXxcU4fSButdIZ053bgVVs6xtGZ5z6HmVwj3T2Gmi96X4z%2F%2FOQn9hicQ%2FzDpWKP8p1fNOrm%2Bs%2B%2BiD8eaRe2AB%2ByGj%2BtJq6baolvSmTc2TqjxgZymjGyd7BohYGpHGtF6BiBuVx%2FA6r3%2BE00UaFbSE1HlUs5y8Sv3IzpHqS662tLLg%2Fdy1M1KlnYjOV2c8RDzKJ%2BftbfKVmWfPdI8eKOo49NcVTue9ucP8znvoF%2FpMpWa9Yqhiq1wveqbhEWJqUWT%2BAoUUQUiwkNMBkPrN8rK5q7vMzy93b%2FxasH27TaaXmTDZoIm9BjqkAefz1G17vvTFA8X7T84lJtViKRDIEAJgXDchu8DbGAtIPQodATXq5XzDMKQF5VAe34EwlQN1Los8TB75XorkRjF%2BM8UoFK2ImHvnfXWRolFELrGX%2B9pbnFR7AXTt2B45O2gy5RPVjCwJp2KDznoqwZzAO1RLZgvn%2BqQpS%2F2BVru4OP6x%2F8oxpwvMK0%2B92uoUCiUS18vkUmgxvkvfeqm7sz0DSguj&X-Amz-Signature=edf4613a6199ca99955f4a803eba60ba2be90cabe9d11be4f9e78b28d802dfb1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDWSRQSY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCKMmBJUex2BJFZ1hC5vdFjGBBtfC7s4Iwf8ubvp5%2F05wIhAK6AkEvbU3vESK3MkIzH4Uke98Jogum2etRANc0QdY%2FFKv8DCDMQABoMNjM3NDIzMTgzODA1IgyRIf3vVdEw32xdjTsq3AMe07RB7G1hG2UnI0KExyIymSMPPS5ff2WGgd90qOMlBg5eAxvWBhRbGq7pgxLr99GkmJAO9MvCJVAKlZUD3C%2BjZA3eO3W1lD2MNziygn2pdrVpbj55JCKIYzyNxlxHGRs97DJrM9xpvxYXnv7yyYun6xucGn3pK%2BTCbFS6Ox6fVIlV974OfqIrZkBET9RbTQWJqdXTrnWQ5YjzDt%2FI7HO06SvpzTDFTGC1sDOhT6NCHbFYJVKXkvskauCqK5vCehCOmmce15D1v10%2FhTpjLYJthdHDiw4zlpVg6uDy%2BhCxK3IDMFMO%2FpWoFG2F0nG3x%2BT0z0VZn6cu%2F1s82QhyXxcU4fSButdIZ053bgVVs6xtGZ5z6HmVwj3T2Gmi96X4z%2F%2FOQn9hicQ%2FzDpWKP8p1fNOrm%2Bs%2B%2BiD8eaRe2AB%2ByGj%2BtJq6baolvSmTc2TqjxgZymjGyd7BohYGpHGtF6BiBuVx%2FA6r3%2BE00UaFbSE1HlUs5y8Sv3IzpHqS662tLLg%2Fdy1M1KlnYjOV2c8RDzKJ%2BftbfKVmWfPdI8eKOo49NcVTue9ucP8znvoF%2FpMpWa9Yqhiq1wveqbhEWJqUWT%2BAoUUQUiwkNMBkPrN8rK5q7vMzy93b%2FxasH27TaaXmTDZoIm9BjqkAefz1G17vvTFA8X7T84lJtViKRDIEAJgXDchu8DbGAtIPQodATXq5XzDMKQF5VAe34EwlQN1Los8TB75XorkRjF%2BM8UoFK2ImHvnfXWRolFELrGX%2B9pbnFR7AXTt2B45O2gy5RPVjCwJp2KDznoqwZzAO1RLZgvn%2BqQpS%2F2BVru4OP6x%2F8oxpwvMK0%2B92uoUCiUS18vkUmgxvkvfeqm7sz0DSguj&X-Amz-Signature=98bbaf6cf73f1b9aea0c3a4f77dfbd187a027758840beb17a15e017e2c1fedec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCQS6LXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDq4udJ%2B3rT7J0AWIv7eBaR4k0LFtVOlzVDrVbu838hGQIgBvfOBVYZWEtHEKzdpCMOBKPXoGQs39ZSR3vbu9RCbQkq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFt7wXax2Y8%2Fzp5hZyrcA8t6D%2FxvwzeV0SzGngmJskF25xg%2FeRy%2Fv93vZHSDoCKctIRaQXX6F%2F0FJ0TE%2BSu1hlzSw4JRjyOYLcmwNmaikJ7fMpf%2Bs1G5%2BRnUD%2Fbf4tpn%2BHutNJqwlRAOHAdqeM5TQZ7ma4E%2FHxOi8V1wh%2F5GWGisNpyZeUHUHY7Svdm1Tc7Wu6yNDKfmvvjd8QN%2BukFch4rUmuqbtPZsk7ad9Mnr4tthfTG6Zms5spZvjnW2DTw3c63ckSvsBN4OlMDoqEObg8s%2BdnSFecjAFH1yvPPijOMH9xtm06T%2BrPWK%2Bck33UoDbnNKR7db53W05ETZyKhpTY5uMYqa4%2BLr9y4QR9kOcFEkNXU%2BwaEgxrzctzb3nxUMULz805TTOoxVpPndzX2Ps7KGQSXAdx8TeE9gO2PkMm0UI1YOa7G5OKPV49Juvu8zsI2RPrhMgcXQYzJ4M26rdZ9QG70U%2FCdr25t7jLB890X%2BJl62MfC8pA9UEPl6n1ShAjnt8tiae1RLzpgy1EvqS3OGy4iVO3sOeL7kb45srLwxGJCYrzF174VNvXZwWGxv4%2B64mPTmw7Qr2aEYiYc7XFsOWZmhXxzMCseJQ%2B9%2BYwPnOu5kCzLoqq%2BtLajafeJ6udar1s94Bqz1mRurMLKhib0GOqUBzeE6z0gHqrL%2BRoNlxM9yACgWVVPCuS4%2B0UMaTd9jYYUTgZrRpWbhLLSt4otxhDeTI%2FKeY48xG6pxs8dY83vrih2NUvKkLJJqAzaR54xEYyaewPY2NZWdY2ZFMkvl3Wp25bjUt8%2BAl%2BINm3hrvh4EYz7%2FcT5uALW0mG59tmTRdua0ISZDCHMNemYuopSGZBm%2FxZMI0C7b4iIlCA1JBL%2FdkdqVXF1O&X-Amz-Signature=b3fb619478ed1fe8650736d7d6f9de894ef730d9d9d54855523f4d1123d78605&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCQS6LXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDq4udJ%2B3rT7J0AWIv7eBaR4k0LFtVOlzVDrVbu838hGQIgBvfOBVYZWEtHEKzdpCMOBKPXoGQs39ZSR3vbu9RCbQkq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFt7wXax2Y8%2Fzp5hZyrcA8t6D%2FxvwzeV0SzGngmJskF25xg%2FeRy%2Fv93vZHSDoCKctIRaQXX6F%2F0FJ0TE%2BSu1hlzSw4JRjyOYLcmwNmaikJ7fMpf%2Bs1G5%2BRnUD%2Fbf4tpn%2BHutNJqwlRAOHAdqeM5TQZ7ma4E%2FHxOi8V1wh%2F5GWGisNpyZeUHUHY7Svdm1Tc7Wu6yNDKfmvvjd8QN%2BukFch4rUmuqbtPZsk7ad9Mnr4tthfTG6Zms5spZvjnW2DTw3c63ckSvsBN4OlMDoqEObg8s%2BdnSFecjAFH1yvPPijOMH9xtm06T%2BrPWK%2Bck33UoDbnNKR7db53W05ETZyKhpTY5uMYqa4%2BLr9y4QR9kOcFEkNXU%2BwaEgxrzctzb3nxUMULz805TTOoxVpPndzX2Ps7KGQSXAdx8TeE9gO2PkMm0UI1YOa7G5OKPV49Juvu8zsI2RPrhMgcXQYzJ4M26rdZ9QG70U%2FCdr25t7jLB890X%2BJl62MfC8pA9UEPl6n1ShAjnt8tiae1RLzpgy1EvqS3OGy4iVO3sOeL7kb45srLwxGJCYrzF174VNvXZwWGxv4%2B64mPTmw7Qr2aEYiYc7XFsOWZmhXxzMCseJQ%2B9%2BYwPnOu5kCzLoqq%2BtLajafeJ6udar1s94Bqz1mRurMLKhib0GOqUBzeE6z0gHqrL%2BRoNlxM9yACgWVVPCuS4%2B0UMaTd9jYYUTgZrRpWbhLLSt4otxhDeTI%2FKeY48xG6pxs8dY83vrih2NUvKkLJJqAzaR54xEYyaewPY2NZWdY2ZFMkvl3Wp25bjUt8%2BAl%2BINm3hrvh4EYz7%2FcT5uALW0mG59tmTRdua0ISZDCHMNemYuopSGZBm%2FxZMI0C7b4iIlCA1JBL%2FdkdqVXF1O&X-Amz-Signature=31e1ae18ef2cd5f9ff0a61656acfba7d6d4445a56639a2fcf31f91cd3b7e854c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCQS6LXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDq4udJ%2B3rT7J0AWIv7eBaR4k0LFtVOlzVDrVbu838hGQIgBvfOBVYZWEtHEKzdpCMOBKPXoGQs39ZSR3vbu9RCbQkq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFt7wXax2Y8%2Fzp5hZyrcA8t6D%2FxvwzeV0SzGngmJskF25xg%2FeRy%2Fv93vZHSDoCKctIRaQXX6F%2F0FJ0TE%2BSu1hlzSw4JRjyOYLcmwNmaikJ7fMpf%2Bs1G5%2BRnUD%2Fbf4tpn%2BHutNJqwlRAOHAdqeM5TQZ7ma4E%2FHxOi8V1wh%2F5GWGisNpyZeUHUHY7Svdm1Tc7Wu6yNDKfmvvjd8QN%2BukFch4rUmuqbtPZsk7ad9Mnr4tthfTG6Zms5spZvjnW2DTw3c63ckSvsBN4OlMDoqEObg8s%2BdnSFecjAFH1yvPPijOMH9xtm06T%2BrPWK%2Bck33UoDbnNKR7db53W05ETZyKhpTY5uMYqa4%2BLr9y4QR9kOcFEkNXU%2BwaEgxrzctzb3nxUMULz805TTOoxVpPndzX2Ps7KGQSXAdx8TeE9gO2PkMm0UI1YOa7G5OKPV49Juvu8zsI2RPrhMgcXQYzJ4M26rdZ9QG70U%2FCdr25t7jLB890X%2BJl62MfC8pA9UEPl6n1ShAjnt8tiae1RLzpgy1EvqS3OGy4iVO3sOeL7kb45srLwxGJCYrzF174VNvXZwWGxv4%2B64mPTmw7Qr2aEYiYc7XFsOWZmhXxzMCseJQ%2B9%2BYwPnOu5kCzLoqq%2BtLajafeJ6udar1s94Bqz1mRurMLKhib0GOqUBzeE6z0gHqrL%2BRoNlxM9yACgWVVPCuS4%2B0UMaTd9jYYUTgZrRpWbhLLSt4otxhDeTI%2FKeY48xG6pxs8dY83vrih2NUvKkLJJqAzaR54xEYyaewPY2NZWdY2ZFMkvl3Wp25bjUt8%2BAl%2BINm3hrvh4EYz7%2FcT5uALW0mG59tmTRdua0ISZDCHMNemYuopSGZBm%2FxZMI0C7b4iIlCA1JBL%2FdkdqVXF1O&X-Amz-Signature=c06c605da4a6fc7ad5b66a089e7cf9f798dd6db7375d9e22da5c47fdb584fa6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

