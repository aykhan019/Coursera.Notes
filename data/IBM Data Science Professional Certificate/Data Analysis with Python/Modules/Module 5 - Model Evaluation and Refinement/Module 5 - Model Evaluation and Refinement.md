

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=9d51c73ac41b2fde622083d673efa93811c604f4dd9db11d97eae84af71f5893&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=36480bd238e9d363b9218fb16098a0d73a0d6c2c2b6f0b5346a088537baa4cb5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Example Code**:
```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# X_train: Training data for the predictors
# X_test: Testing data for the predictors
# y_train: Training data for the target variable
# y_test: Testing data for the target variable
# test_size=0.3: 30% of the data will be used for testing, and 70% will be used for training
# random_state=42:Ensures reproducibility of the split. Using the same random state will produce the same split every time
```
### Generalization Error
- **Generalization Error**: Measures how well the model predicts new data. The error obtained using testing data approximates this error.
### Cross-Validation
**Cross-Validation**: A technique to assess the model's performance and estimate generalization error by splitting the data into multiple folds.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=02a3e119303724dd7978de662f5c69c8e0cd99153eb2e2109146c946a28182fe&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=bacf6e8c548ee8e38c2dad7c015461d066482142dba144307bdb3a7965e241ed&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=f8b0f851e6a3eadd4de48719d3cef30ad3ca1891743e7a1a2294b83adac69d51&X-Amz-SignedHeaders=host&x-id=GetObject)
### Cross-Val Predict
**cross_val_predict** is used when you want to obtain the predicted values for each test fold during the cross-validation process. It returns the prediction for each data point when it was in the test set. This is useful for:
5. **Visualizing Predictions**: You can plot the predicted values against the actual values to see how well the model performs across the entire dataset.
6. **Diagnostics**: It helps in analyzing the residuals (differences between actual and predicted values) to diagnose model performance.
#### Example in Python
Here's an example using `cross_val_predict`:
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Initialize the model
model = LinearRegression()

# Get cross-validated predictions
y_pred = cross_val_predict(model, X, y, cv=5)

# Plot actual vs. predicted values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Cross-Validated Predictions')
plt.show()
```
In this example:
- `cross_val_predict` returns the predicted values for each test fold during the 5-fold cross-validation.
- A scatter plot is created to visualize the actual vs. predicted values.
#### Summary
- **Training Set**: Used to build the model.
- **Testing Set**: Used to evaluate model performance.
- **Cross-Validation**: Provides a robust estimate of model performance by averaging results across multiple folds.
___
## Model Selection and Polynomial Regression
When selecting the best polynomial order, our goal is to provide the best estimate of the
function $ y(x) $.
### Noise in Data
**Noise** in data refers to random variations or errors that obscure the true underlying patterns or relationships. It can come from various sources and affects the accuracy of models.
### **Underfitting** 
**Underfitting** occurs when the model is too simple to fit the data:
- Example: Fitting a linear function to data generated from a higher-order polynomial plus noise results in many errors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=5e0cf38bffc9eb59a58cef18817c3985c75357d4f1a6821817a7c725996f9613&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=0b648c53139d1aad968663d4e25f40b21d97be68b0c35ac024b033c40159c481&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=bedd175e0eae66d1add58dfb9a20878b8eacec915219de6fe128b8205fd58a75&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=07b45951bc45c5d23f41471643d8f609af9a96bd08e0d5997a101a6256ee317b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQKWQMD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIF7LpGYvBaWmA%2B0Xd7Nj9qCkBWnoZLfIQoXGJaxBTRSNAiEArYMa0elADPgBdr489vFqZeZeKAAb1D21fxDcvDgrf6Uq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDE0fUG%2Fa3SVYB0KCtyrcAxNTZzLV5dXaN3ZJRI%2FpOYw6Psm3Ou3Wuazv6lptyzLTTtJXN0lG78bienSCuBEUXe1y%2FcTGsa7ZQvei51R%2FXKKE7uxgCV8ERsmheL5cIoi64AtbYcMZwc65a7d0H1VUGB98XgZP6blRBAKsIOaisMW8eLr19pAYL2usLPlXscYNQBrYX62PhrHO470%2BqNV2WsMHWkbGGysJFyttInwgOLS7BViDJkQc%2FC7MWAAbN8OIRbvgsDK19BR9xZK8W0dh%2B8dmUxhI6urf%2BQLsfySwdhQ%2BPnT2E%2Fupn7lm5ANCzLIqgOYUDOHULGINju0zJTUOcvJVN3W1Cu4kYPkGKmWGuXEeuz4NNfYaNTsWtmim6elu30kaM%2BVlCw6PzOb44FEF7NU2pez3cwgq7KTocM05XDWwgctU0szF8%2FGwDVTRiIk6XLCCMIy225Tp8LJ%2FkgKPTu4mEZA%2F%2BgtGrxXJVpJbV%2FJZdKP7dOuitjD07OyBidY%2FKrCAqPz2IPqn70br5gbJzeZBsMt7eC6G3ugOGXpM71iYY3KvQj%2F8ofx9YCDm2T8jESeVTuH57o0T7jbu1IXBQ4Q%2B27u8zJ2%2B5LqeyrPGo%2BYA8Fi%2FiNvM%2Fz5DL%2FzRQgWx5OweoSeI3YUnhuNpMJr6lr0GOqUBIBSYVpT3KfSHtl1XrYSMQCQhiLYk%2BYHJ1Ayjh90nXT9NtZ1mxguhHHSoF3RVbtAs7aOpMAxQu0gUf6%2BlIomFbYavaa%2BXmSsyPXaCNvpCKg1sPXew1Ieia2cbwYy8fON1QslWuoFX9O7AV77TjozU2WcaWAqPZPPAX0RmUxRMwye2%2FOgVPBgux3D%2BR2eu%2F%2BdY01yzNfb1OXXTJX92MbNQgo3LGbiy&X-Amz-Signature=22f380c3523cc6d10df13c7a566dcb6e7967050e8fe97723363174312fe43004&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQKWQMD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIF7LpGYvBaWmA%2B0Xd7Nj9qCkBWnoZLfIQoXGJaxBTRSNAiEArYMa0elADPgBdr489vFqZeZeKAAb1D21fxDcvDgrf6Uq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDE0fUG%2Fa3SVYB0KCtyrcAxNTZzLV5dXaN3ZJRI%2FpOYw6Psm3Ou3Wuazv6lptyzLTTtJXN0lG78bienSCuBEUXe1y%2FcTGsa7ZQvei51R%2FXKKE7uxgCV8ERsmheL5cIoi64AtbYcMZwc65a7d0H1VUGB98XgZP6blRBAKsIOaisMW8eLr19pAYL2usLPlXscYNQBrYX62PhrHO470%2BqNV2WsMHWkbGGysJFyttInwgOLS7BViDJkQc%2FC7MWAAbN8OIRbvgsDK19BR9xZK8W0dh%2B8dmUxhI6urf%2BQLsfySwdhQ%2BPnT2E%2Fupn7lm5ANCzLIqgOYUDOHULGINju0zJTUOcvJVN3W1Cu4kYPkGKmWGuXEeuz4NNfYaNTsWtmim6elu30kaM%2BVlCw6PzOb44FEF7NU2pez3cwgq7KTocM05XDWwgctU0szF8%2FGwDVTRiIk6XLCCMIy225Tp8LJ%2FkgKPTu4mEZA%2F%2BgtGrxXJVpJbV%2FJZdKP7dOuitjD07OyBidY%2FKrCAqPz2IPqn70br5gbJzeZBsMt7eC6G3ugOGXpM71iYY3KvQj%2F8ofx9YCDm2T8jESeVTuH57o0T7jbu1IXBQ4Q%2B27u8zJ2%2B5LqeyrPGo%2BYA8Fi%2FiNvM%2Fz5DL%2FzRQgWx5OweoSeI3YUnhuNpMJr6lr0GOqUBIBSYVpT3KfSHtl1XrYSMQCQhiLYk%2BYHJ1Ayjh90nXT9NtZ1mxguhHHSoF3RVbtAs7aOpMAxQu0gUf6%2BlIomFbYavaa%2BXmSsyPXaCNvpCKg1sPXew1Ieia2cbwYy8fON1QslWuoFX9O7AV77TjozU2WcaWAqPZPPAX0RmUxRMwye2%2FOgVPBgux3D%2BR2eu%2F%2BdY01yzNfb1OXXTJX92MbNQgo3LGbiy&X-Amz-Signature=ffef570a237dbcbd2d466de6aa317735e57b1da469c1fffab4797a2703fa0692&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQKWQMD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIF7LpGYvBaWmA%2B0Xd7Nj9qCkBWnoZLfIQoXGJaxBTRSNAiEArYMa0elADPgBdr489vFqZeZeKAAb1D21fxDcvDgrf6Uq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDE0fUG%2Fa3SVYB0KCtyrcAxNTZzLV5dXaN3ZJRI%2FpOYw6Psm3Ou3Wuazv6lptyzLTTtJXN0lG78bienSCuBEUXe1y%2FcTGsa7ZQvei51R%2FXKKE7uxgCV8ERsmheL5cIoi64AtbYcMZwc65a7d0H1VUGB98XgZP6blRBAKsIOaisMW8eLr19pAYL2usLPlXscYNQBrYX62PhrHO470%2BqNV2WsMHWkbGGysJFyttInwgOLS7BViDJkQc%2FC7MWAAbN8OIRbvgsDK19BR9xZK8W0dh%2B8dmUxhI6urf%2BQLsfySwdhQ%2BPnT2E%2Fupn7lm5ANCzLIqgOYUDOHULGINju0zJTUOcvJVN3W1Cu4kYPkGKmWGuXEeuz4NNfYaNTsWtmim6elu30kaM%2BVlCw6PzOb44FEF7NU2pez3cwgq7KTocM05XDWwgctU0szF8%2FGwDVTRiIk6XLCCMIy225Tp8LJ%2FkgKPTu4mEZA%2F%2BgtGrxXJVpJbV%2FJZdKP7dOuitjD07OyBidY%2FKrCAqPz2IPqn70br5gbJzeZBsMt7eC6G3ugOGXpM71iYY3KvQj%2F8ofx9YCDm2T8jESeVTuH57o0T7jbu1IXBQ4Q%2B27u8zJ2%2B5LqeyrPGo%2BYA8Fi%2FiNvM%2Fz5DL%2FzRQgWx5OweoSeI3YUnhuNpMJr6lr0GOqUBIBSYVpT3KfSHtl1XrYSMQCQhiLYk%2BYHJ1Ayjh90nXT9NtZ1mxguhHHSoF3RVbtAs7aOpMAxQu0gUf6%2BlIomFbYavaa%2BXmSsyPXaCNvpCKg1sPXew1Ieia2cbwYy8fON1QslWuoFX9O7AV77TjozU2WcaWAqPZPPAX0RmUxRMwye2%2FOgVPBgux3D%2BR2eu%2F%2BdY01yzNfb1OXXTJX92MbNQgo3LGbiy&X-Amz-Signature=3d24f1d85442c9b5830a000ce67043b7f3ff9a9e65ce5f1d63f75e0a80c2d073&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=d39bb7759e5112fac08d37f1a64e40928cb2b83b33559a0221afc310ca838a1d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Calculating R-squared Values**
7. Create an empty list to store R^2 values.
8. Create a list of different polynomial orders.
9. Iterate through the list using a loop:
	- Create a polynomial feature object with the order as a parameter.
	- Transform the training and test data into polynomial features using the `fit_transform` method.
	- Fit the regression model using the transformed data.
	- Calculate the R^2 value using the test data and store it in the list.
Here's an example of how you can implement this in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Store R^2 values
r2_values = []

# List of polynomial orders
orders = [1, 2, 3, 4]

# Iterate through polynomial orders
for order in orders:
    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    x_poly = poly.fit_transform(x.reshape(-1, 1))

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Predict and calculate R^2
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    r2_values.append(r2)

# Plot R^2 values
plt.plot(orders, r2_values, marker='o')
plt.xlabel('Order of Polynomial')
plt.ylabel('R^2 Value')
plt.title('R^2 Value vs. Polynomial Order')
plt.show()
```
Output:
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=6853b344df4b3f4e79f7eeb59c7a6729ec276bf939d0e6d8960c721402dbac45&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=5d11fb65b22c14d0127268291ed432f8f50eb3a71e8948d30bcfd457924f36b7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=314f5628faa036b04904903766a1e0be7a2126e00c35c868471deb3bb3a63e6a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=2f80b9955147bcf50b19fd1d0aff7aa594fdd75e1ab229c03384948d3c698de2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVXZT2KD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC6ENfrU4PXx9aJULAu%2BCQNgKQWQf39kg%2F6DdKpPfKBjwIhALaKWEGTlMO%2FAZJkQqx7zcwKP%2BfNtl5tfCcXHfRR9dwGKv8DCHEQABoMNjM3NDIzMTgzODA1IgwjLViF8hf0sgA4XAUq3AODny1xjCHSk%2FMZtJpaTctECWVuu5egxFspK8AM99RdkshoKeEiZy8YaWypIGhl2IMGO%2Fe9wsJm%2FFg2YVqAigPvrj03dNuOvC1SMa4vEdnzqdT%2F%2FZSQgNwrnbtiynQOr9jg9uLiQtWhRCymj35JHNNLfCMK%2BS0asjzNRuVipY%2B5p4nszXD9ihLxWElCHPXTOfz14fk6mrwlUPQfyMBmkmnA9Ev63lIIgadCWu9sZu29T1wzuOQod5vguf4uI0X8LhB7yInztroD56TcV%2FDKfsYycMfBaPvs2Zx45z7mvYFonv29ORXbSDZdtCq0Z%2FQJzKTAvC7189SoILhLUbEy53rfU6IUciWAARkbAYGCZMQCwSADsDTV6jkovJ1xqeHhcRNx0VCAYyFbYOqgkqLECeG%2BU%2B9tpSg64fSbe4GvOsEvZ8HrfgKGfxm40ti9pSt2Aj9rPdUAP8GkRHueuwC09Udp0uo6xwvTu3nMjqFDWjJjqVelqHM8XGDoX99qMBeZCtHjdOGcEQpQAjOw9IyOO%2FQuQkP7vm6gxmpsqr3H4MfIEUmcsQNlLEqjDP%2FHU44qHeGXeUU%2BSBMFyoYhU7YRVul2LRm4JEIz7%2F44V0OL60YsIcSK%2FiDsdfrX7hvQCjDL%2BZa9BjqkAeLfLldpuuXHzM%2BKcjiVvnZ%2Bbn21xmmbd6xA27VNCIQxnnPDc%2F57RqceEu7c1A%2FPgOS8XwncVrU9aTPpQTtx%2BHluKIIfYYBFdjED%2B6EwYDmp8VAgA7z4ZWG6Wwmw4GyZIkI9RuuyJjySA9CxfgAsXmjoAbgUh7n7nMdYVnnZlTOPfhUXPGCcekYy89HbJso22kIZ8k3eDWyOwaAnI5oOReWUVSRB&X-Amz-Signature=a1d445e12c3ebd508ee23e020cb33cfbc00a20e960192661f3f1af4216e04d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6ZARWFZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCZrVZGrO8OwncL0bn4sXDZ7gJhmR8ciLqzhKZunYqrcAIhAJGFZ933MhiSn74YwIwjY0dbQLargxjqzp%2FMkcEc77w9Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVF53XMzD2kpz9l8q3AOyY8UlixBnwP5ClXfZ3BbS8S2qJJa5As%2F0yBCN4ScAo0MmV2pv58p%2B2VwW59nqTik%2B0%2Bc2BpQxhd8F1rTjWOUqZVFIFnPWrfoEdEGW3Qck5TDrGRIC0DDw3dAgUMzE7PaUEEmt18XOKjWgOUL%2FT60HatEhf8yAjqMkidQpdAETf1%2B0RB6a%2FzXc%2FnctKcH1A6rkO%2BfDvVM6fuh%2BZuftDj6EvZrhYCdt1hEfhmafywjrB68RYL%2FaAbfp06VCLnGaxdeUTY8FuxCZgTUKSN9cnrHIioHfv5o0T3COcqztjUYkVBz%2BCYrQNV%2B2S0RnVXR8Onks5nlcvGd0TAW8sjmx2PGCOPuRpedCsXYYpfJPtVbABvq9bcv%2FLHPF8lJ9oA6YWyY48CPhL1OPMNZ7Dq2rYYENMzB9qIofRbDTFo9wpdWNFZAiDCzNh0PQ1uXtpAEMEfcXjT4cxjBZThGnRMh5vTrZLgVGeAk18%2FyUbEX4AyCKO34sLRFHzeTYGpCX0Tf4b%2FlfG7Po9MNztJUd5OTAe2P0jAx%2FzxqqylbRF7kYa6O19KuetBHlxY4SmKKY%2Fedz6TfTV2Y99s60oacZsJNvz2tZVRP1%2BHFEb2cIXl8YN2b4z6aa9qlN9DGbByEtYDCB%2Bpa9BjqkAf4GxxJZiOWIpwjdrP6OW4vEgJKCZ4JB%2FNUcxadBmTqsqMPVEDk1ZCEpLVZaNak2JLZj6G3NbNHxrzfueJJDunRNNQufs1vLqb4blM0yaiV4m8Z23TqHNXKBzvJSHQxLLrlBf7O4hLahDV%2FWpsfd0xq4p7Ypzamy%2BWs2uQCIipC%2FOjCT5yPDliVvcQS9tDCmn6ZF50pgDr7hDF3ZwFVzbtf1WqG7&X-Amz-Signature=fbfc1c4587901c8c0c42f60512cbd0942068103ce1733b5efdea4bc3bc4e8861&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6ZARWFZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCZrVZGrO8OwncL0bn4sXDZ7gJhmR8ciLqzhKZunYqrcAIhAJGFZ933MhiSn74YwIwjY0dbQLargxjqzp%2FMkcEc77w9Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVF53XMzD2kpz9l8q3AOyY8UlixBnwP5ClXfZ3BbS8S2qJJa5As%2F0yBCN4ScAo0MmV2pv58p%2B2VwW59nqTik%2B0%2Bc2BpQxhd8F1rTjWOUqZVFIFnPWrfoEdEGW3Qck5TDrGRIC0DDw3dAgUMzE7PaUEEmt18XOKjWgOUL%2FT60HatEhf8yAjqMkidQpdAETf1%2B0RB6a%2FzXc%2FnctKcH1A6rkO%2BfDvVM6fuh%2BZuftDj6EvZrhYCdt1hEfhmafywjrB68RYL%2FaAbfp06VCLnGaxdeUTY8FuxCZgTUKSN9cnrHIioHfv5o0T3COcqztjUYkVBz%2BCYrQNV%2B2S0RnVXR8Onks5nlcvGd0TAW8sjmx2PGCOPuRpedCsXYYpfJPtVbABvq9bcv%2FLHPF8lJ9oA6YWyY48CPhL1OPMNZ7Dq2rYYENMzB9qIofRbDTFo9wpdWNFZAiDCzNh0PQ1uXtpAEMEfcXjT4cxjBZThGnRMh5vTrZLgVGeAk18%2FyUbEX4AyCKO34sLRFHzeTYGpCX0Tf4b%2FlfG7Po9MNztJUd5OTAe2P0jAx%2FzxqqylbRF7kYa6O19KuetBHlxY4SmKKY%2Fedz6TfTV2Y99s60oacZsJNvz2tZVRP1%2BHFEb2cIXl8YN2b4z6aa9qlN9DGbByEtYDCB%2Bpa9BjqkAf4GxxJZiOWIpwjdrP6OW4vEgJKCZ4JB%2FNUcxadBmTqsqMPVEDk1ZCEpLVZaNak2JLZj6G3NbNHxrzfueJJDunRNNQufs1vLqb4blM0yaiV4m8Z23TqHNXKBzvJSHQxLLrlBf7O4hLahDV%2FWpsfd0xq4p7Ypzamy%2BWs2uQCIipC%2FOjCT5yPDliVvcQS9tDCmn6ZF50pgDr7hDF3ZwFVzbtf1WqG7&X-Amz-Signature=8a13b5b57a05fcdee487cc733694ba118ecdd76c5b20d4668a8c8282854ec1b9&X-Amz-SignedHeaders=host&x-id=GetObject)
12. **Model Training**:
	- **Procedure**: Use cross-validation to select the optimal Alpha. Split the data into training and validation sets.
	- **Steps**:
		1. **Train Model**: Fit the model using different values of Alpha.
		2. **Predict & Evaluate**: Use validation data to make predictions and calculate the R^2 or other metrics.
		3. **Select Alpha**: Choose the Alpha that maximizes the R^2 on validation data.
13. **Implementation in Python**:
	- **Import**:
```python
from sklearn.linear_model import Ridge
```
	- **Create & Fit Model**:
```python
ridge = Ridge(alpha=1.0)  # Set the desired alpha value
ridge.fit(X_train, y_train)
```
	- **Predict**:
```python
y_pred = ridge.predict(X_test)
```
14. **Cross-Validation**:
	- **Purpose**: Used to determine the best Alpha by comparing performance metrics (e.g., R^2) across different Alpha values.
	- **Process**: Train with various Alpha values, evaluate with validation data, and select the best-performing Alpha.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7W5WLF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCKa4h1O9b6ZYvbNAWZcThEqmjJ9JaGYcgMBQCPiethVQIgJuW4Wy1pf%2BrTYbI6gUh4YpX5ELi26h7AAejEGtuke8Mq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOYCbpM6aBUT7I9uICrcA5VkFLpQJBVrUtllpN6yhw31dBa%2FHAUmwXhhjvo7kcrq0Qt7DwqNqr07nZHe2QjWmULQ8rSPKB7JQZW9o4LICWQuq%2B9Z3Ze3FCNQj2Se%2BDDoO64GaRN5%2FHCsUuhzfZQDsqofaqHsSOCFBFvddlPrFti4ZiqqvM9a%2FD4%2BTTj7SyYqWuR45sOTCH%2BvFGYfS%2Fg6HgdZW8rxLOjINY1E8btMvPzJfoeRhUvRyDhb1LtZuHbRHaxsLbt86UvfTw2yOXtQySwYoc3v%2FGlRjZ%2FCCKafHZiBcYWx59R5xz1%2FQYtr6uCMPXcw4M5hFb%2BOo%2BteV3uT%2Fr2qT4kHIFCQNxCOBJ%2F8jyassQVFMi9BMCLQsmsy4DGUL%2BnXLzG17sYWULWfGSKvIDLp8mgNXsC1YoN%2FQbvsWXeP%2BJVFINjxvhNpsN4KQE4h4iyM95deTsT4dvnjnoAZpwgOnDAgpv8OuDg%2FiDqfcw1VmfK8qw5AH%2Bv2259PsZSxFrRWpcVkR%2Bev2DvcPu109XExWWozdC5fS0LiRATCanL6s4CK5GMo3akRYAKJrcd8QWxa6X9p6Otfy%2F8G%2FhLlfSbyGVK2yShHMaUfBd2okfFVb9VHgcGRae7AhKSVFyTZYobYX3FUF16rdSLnMIP6lr0GOqUB5I5RuvlpzeUY%2BVvZLNuK6rMQz4nGOk%2F5eAxLFfPj%2FTN9UyZprThM7ShOr5mu1ERjKDSz%2FcNo0z%2BcVkrQ5aiYDw3ZtMsbbTiUoE5OT19brr%2BR8Dgocx9Vkvs3jXtNVq86iHASPZn04nfD3o9ikVYqLoMlUf1x6zlN%2F4%2FEhfZndmOka1MMx7BAsv5SW%2BKQqc4tZ0ybXHIC0X9%2BL90GVEZXpmaBrHvR&X-Amz-Signature=e60c0ce4a276962d4e3a1f434168cb8d8204167172141704a0e473f61d6756d6&X-Amz-SignedHeaders=host&x-id=GetObject)
15. **Example Visualization**:
	- **Plot**: Shows R^2 values vs. different Alpha values for training and validation data.
	- **Interpretation**:
		- **Training Data**: R^2 might increase with Alpha but eventually converge.
		- **Validation Data**: R^2 may decrease with high Alpha due to reduced model flexibility.
___
## Grid Search for Hyperparameter Tuning
### **Grid Search**
A method for finding the best hyperparameters for a model by systematically evaluating different combinations.
- **Hyperparameters**: Values like Alpha in Ridge Regression that are not learned from the data but set before the training process.
- **Process**:
	1. **Define Hyperparameters**: Set up a grid of hyperparameter values to test. For Ridge Regression, this might include values for Alpha and normalization options.
	2. **Train and Evaluate**: Train the model using each combination of hyperparameters. Evaluate each model using cross-validation, typically using metrics like R² or Mean Squared Error (MSE).
	3. **Select Best Parameters**: Choose the hyperparameters that give the best performance based on the evaluation metric.
### **Implementation in Scikit-learn**
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Define parameter grid
param_grid = {
    'alpha': [0.1, 1, 10],
    'normalize': [True, False]
}

# Initialize Ridge model
ridge = Ridge()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, scoring='r2', cv=5)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_
cv_results = grid_search.cv_results_

# Results
print("Best Parameters:", best_params)
print("Best Score:", best_score)
print("Best Estimator:", best_estimator)
print("CV Results:", cv_results)
```
**Example Result:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT7EF22V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCqL%2FTFw%2Fh64uIkkXguBKIREJ4Y%2BfLkiEWk95mHudBZ3QIgIrrXhFiyFw%2BjtTu6P8YYSfYUKXcBOFKT8Yru3VcNr%2Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG7ZOBOBkg7seGdRASrcAyeBUOrp6lS04rJlma9mtJcsplYgrGqQKB7bcpGOv3PwRL%2Bu9CDy60Ov%2BoTBtng2xXexfCOoxHgJrH%2BOoVEcgWMx4kU7yXpW%2BQbtmVGjq6QPB3hlPEEp1BoPIFq7PMjvPkDmLTf5wengZnNxHHMqCr1aqXwlVVfyUuOV2MBVYLIjzV%2FM1iI9%2FOz88ppKLjoB73qUJyKPNRHip%2FXmlty%2B9ePdjyQmJnIFFDmA4wFb7sjgikWMgQEgXCalTicSYDTL7QI%2F3aPiL4%2FJd85xSOqXyRsb8pivYHlShyST1hWgjWAVpyL4YwbocR7P31e4ERmMKhkNGbYfrdSS%2BSjoEegKEiEt0lJgLMSvs%2BBrov5NPBtyHY9%2FyGSAPb8PTkzp0FJ72MHQKizNMT90An6yTCRjRtggoxtCj8PMX0jdXW3ZXqQQE5bQWpuhoN5o5VWwI%2F42r5nm4vj19C5u3tvAgUR8xpjSfhsAMDoQazUinKYCwR%2F1chAX16xxImMApJq88gdLF7Po5IkKiZY%2B8Pk%2F9hMMTrtUkGghWE2My0qIw3QgpNxDCxkmjGU90Ie3wxKVTxES9kVLEAi1Az5H6iumAGKDg%2Fd%2BTnKC65tPosdwZG2aC6mMDqkjY%2FjIKibkiyVsMLv5lr0GOqUBMpxQKyslTesdT6ZBgTAel3PFs4Zbu1nOItd%2FNA%2BDgOs0DWGFrnpaxM%2BNuJpwypBX1mHRxhVFORMrRDSUPhlJkszzq%2BdUlT16Np6pissfF1YC%2BvRguayEj1Mc%2BXuhQfgwFnuJJubXx3QXiZZ2WMB2VC9LzXp334tSfzCSZdK0qTSAGF2lERV2hfldAgmy7Y9DGrbqBvTBBe%2BE6aSbJQ27yJOb5chS&X-Amz-Signature=9c971325cc4c8a612e032ec2320b912882596b91491727289b0e5eb426afbb4c&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Key Attributes**:
	- `**best_estimator_**`: Best model found.
	- `**cv_results_**`: Detailed results for each hyperparameter combination, including scores and parameters.
- **Advantages**: Efficiently explores multiple hyperparameter values to find the best combination, reducing the manual effort required for model tuning.
___
## Cheat Sheet: Model Evaluation and Refinement
### Splitting Data for Training and Testing
The process involves separating the target attribute from the rest of the data, treating it as the output, and the rest as input. Then, split these into training and testing subsets.
```python
from sklearn.model_selection import train_test_split

# Define target and features
y_data = df['target_attribute']
x_data = df.drop('target_attribute', axis=1)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
```
### Cross Validation Score
Cross-validation involves creating multiple subsets of training and testing data to evaluate the model’s performance using the R² value.
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation
Rcross = cross_val_score(lre, x_data[['attribute_1']], y_data, cv=n)

# Calculate mean and standard deviation of scores
Mean = Rcross.mean()
Std_dev = Rcross.std()
```
### Cross Validation Prediction
Generate predictions using a cross-validated model.
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation prediction
yhat = cross_val_predict(lre, x_data[['attribute_1']], y_data, cv=4)
```
### Ridge Regression and Prediction
Use Ridge regression to create a model that avoids overfitting by adjusting the alpha parameter and making predictions.
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

# Initialize polynomial features
pr = PolynomialFeatures(degree=2)

# Transform features
x_train_pr = pr.fit_transform(x_train[['attribute_1', 'attribute_2']])
x_test_pr = pr.transform(x_test[['attribute_1', 'attribute_2']])

# Initialize Ridge model
RigeModel = Ridge(alpha=1)

# Fit the model
RigeModel.fit(x_train_pr, y_train)

# Make predictions
yhat = RigeModel.predict(x_test_pr)
```
### Grid Search
Use Grid Search to find the optimal alpha value for Ridge regression by performing cross-validation.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Define parameter grid
parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000]}]

# Initialize Ridge model
RR = Ridge()

# Initialize GridSearchCV
Grid1 = GridSearchCV(RR, parameters, cv=4)

# Fit GridSearchCV
Grid1.fit(x_data[['attribute_1', 'attribute_2']], y_data)

# Get the best model
BestRR = Grid1.best_estimator_

# Evaluate the model
score = BestRR.score(x_test[['attribute_1', 'attribute_2']], y_test)
```
___