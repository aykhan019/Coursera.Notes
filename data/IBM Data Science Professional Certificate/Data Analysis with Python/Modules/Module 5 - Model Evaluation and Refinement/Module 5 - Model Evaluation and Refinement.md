

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=98441e91c68220c41e17ccddf7cefeb0b68e5edb9bb90a8f8a44e808716b7d84&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=fa6733cc54dc6e7c724599746d33384444eacd65faaf58190c320359032396a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=0c6cf42cf3cb7cd914576c60c4f18f87969ad430bbdf156a3cd661b70bd9be7a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=63e9d62d5dca825034451f6ebefc5a367aa64ab43430f8de5138b26f8144a275&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=ce7de45bc853a0f7d82bdb4d8014fbca8f008a3ba57246091cefe2c6aac792a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=318435cc6341d3a26d1e8956998db2ecd48b5cef4b4834420d093cac9e784529&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=b1fd075ce077d16ba0cf86607a8610baac46a012d9319b7df692baa53aa43fe0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=3990fe3c9e2b30ee649e5bb755b94fabd01f782f8c258a3f8ab88e6f7184ed31&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=fba427b7222705c139ee45ba28f931fb8080acf376e9f7924d95bed98865aac1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY5TD3LU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCnuE9Saw6xz1vTTLMoXjZ%2Ffz0%2BgKVuA%2FkGcIXTipr%2BaAIgX0Wk%2FprC1MbG9j1%2FNO3U8xMWopgUsEIH4Zf6GSuGkxMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCua2zirU88g12bZUCrcAzemGQ2T6vrUxqIZYLyS%2BnQoiBrmF9y3Q3DNddxD%2FfzDfg%2BSQVzIe0C1YXSfDuBj68FUYz8ZYOkTYU2vW7gqfBr%2BeNeqJdPU30Fo9bbrGYW7m4WAEinOK6Gsde9RRYCFwubtTrnQ2gY5CxV7ybPYPMc1yQwHcTEh7QKhrupJH4xDwhKGQ%2FI%2BXZ4QlE2919lYWRAGx8CUGMBY9oVVhcHVFPqbnEG8bxg%2B%2B4VH4M5S7Fv%2FfWLqAKFYPhUNe3c3mEuhHMlnsRraFP43Drb2HFEe08YA8f6Qp3byplK8gCt%2BD7rpilveM3wXeNBfCSgC9Fgto9aZv94dqRzCp06lf%2FcqisEnYY7Sw4TGtzhPzlKswEcAqE%2FWf9d8rFPwGHx5vllLIHhZjI9VEDTfPoXlr7YCsFMxCFPfuoKCGChtFGs5Oy6u%2FU%2FWmckO89ZAHFuXUS%2FZOra4cqfxwpW%2FBzXs44ORcjLqc6RHYX%2FrgZ%2FIouP6cQXFB35uHb0qTjepcrbT53pOnR6DtxttLA1ZDvPzuW8p84GlvwXIpEEnxjYlB6U49wL0Sqcwesfkc6axUIizwJqxAAvl4LB5lCT%2FpZOXEqzTsgBacwAtRnjXzHwnNGzG8QjiE%2BSIozTGHZNzvLztMOjfkL0GOqUBtZbTliI7IpOQWtoPmHSjPTdCqGQmDWBuECNHkrHdsorABMd4tmhaBbu%2BA5LnOfZwOrYFdgHWA00Co2OXcyut%2F7yBmkDkprrzOGXpt%2FxPTM0HG0ocQ9ABkkt8JRu6WD6h25hJLTqAoJrkLTR1EpfqxmQI2%2BJoMvp15NagvZd4dehDwkEsX3fqMFMSpbTwpjRXarhqKMP8Q84DJF1Qmw7ryf0M%2BScU&X-Amz-Signature=69cefbf9462bbff5555af321a59f4bf0918126276ae3d5b6da534ebc951ed86f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY5TD3LU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCnuE9Saw6xz1vTTLMoXjZ%2Ffz0%2BgKVuA%2FkGcIXTipr%2BaAIgX0Wk%2FprC1MbG9j1%2FNO3U8xMWopgUsEIH4Zf6GSuGkxMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCua2zirU88g12bZUCrcAzemGQ2T6vrUxqIZYLyS%2BnQoiBrmF9y3Q3DNddxD%2FfzDfg%2BSQVzIe0C1YXSfDuBj68FUYz8ZYOkTYU2vW7gqfBr%2BeNeqJdPU30Fo9bbrGYW7m4WAEinOK6Gsde9RRYCFwubtTrnQ2gY5CxV7ybPYPMc1yQwHcTEh7QKhrupJH4xDwhKGQ%2FI%2BXZ4QlE2919lYWRAGx8CUGMBY9oVVhcHVFPqbnEG8bxg%2B%2B4VH4M5S7Fv%2FfWLqAKFYPhUNe3c3mEuhHMlnsRraFP43Drb2HFEe08YA8f6Qp3byplK8gCt%2BD7rpilveM3wXeNBfCSgC9Fgto9aZv94dqRzCp06lf%2FcqisEnYY7Sw4TGtzhPzlKswEcAqE%2FWf9d8rFPwGHx5vllLIHhZjI9VEDTfPoXlr7YCsFMxCFPfuoKCGChtFGs5Oy6u%2FU%2FWmckO89ZAHFuXUS%2FZOra4cqfxwpW%2FBzXs44ORcjLqc6RHYX%2FrgZ%2FIouP6cQXFB35uHb0qTjepcrbT53pOnR6DtxttLA1ZDvPzuW8p84GlvwXIpEEnxjYlB6U49wL0Sqcwesfkc6axUIizwJqxAAvl4LB5lCT%2FpZOXEqzTsgBacwAtRnjXzHwnNGzG8QjiE%2BSIozTGHZNzvLztMOjfkL0GOqUBtZbTliI7IpOQWtoPmHSjPTdCqGQmDWBuECNHkrHdsorABMd4tmhaBbu%2BA5LnOfZwOrYFdgHWA00Co2OXcyut%2F7yBmkDkprrzOGXpt%2FxPTM0HG0ocQ9ABkkt8JRu6WD6h25hJLTqAoJrkLTR1EpfqxmQI2%2BJoMvp15NagvZd4dehDwkEsX3fqMFMSpbTwpjRXarhqKMP8Q84DJF1Qmw7ryf0M%2BScU&X-Amz-Signature=92a3fba35c19d46e5afac8410704a0d8401f86ef761cae7e895c8f8d5fa3a557&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY5TD3LU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCnuE9Saw6xz1vTTLMoXjZ%2Ffz0%2BgKVuA%2FkGcIXTipr%2BaAIgX0Wk%2FprC1MbG9j1%2FNO3U8xMWopgUsEIH4Zf6GSuGkxMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCua2zirU88g12bZUCrcAzemGQ2T6vrUxqIZYLyS%2BnQoiBrmF9y3Q3DNddxD%2FfzDfg%2BSQVzIe0C1YXSfDuBj68FUYz8ZYOkTYU2vW7gqfBr%2BeNeqJdPU30Fo9bbrGYW7m4WAEinOK6Gsde9RRYCFwubtTrnQ2gY5CxV7ybPYPMc1yQwHcTEh7QKhrupJH4xDwhKGQ%2FI%2BXZ4QlE2919lYWRAGx8CUGMBY9oVVhcHVFPqbnEG8bxg%2B%2B4VH4M5S7Fv%2FfWLqAKFYPhUNe3c3mEuhHMlnsRraFP43Drb2HFEe08YA8f6Qp3byplK8gCt%2BD7rpilveM3wXeNBfCSgC9Fgto9aZv94dqRzCp06lf%2FcqisEnYY7Sw4TGtzhPzlKswEcAqE%2FWf9d8rFPwGHx5vllLIHhZjI9VEDTfPoXlr7YCsFMxCFPfuoKCGChtFGs5Oy6u%2FU%2FWmckO89ZAHFuXUS%2FZOra4cqfxwpW%2FBzXs44ORcjLqc6RHYX%2FrgZ%2FIouP6cQXFB35uHb0qTjepcrbT53pOnR6DtxttLA1ZDvPzuW8p84GlvwXIpEEnxjYlB6U49wL0Sqcwesfkc6axUIizwJqxAAvl4LB5lCT%2FpZOXEqzTsgBacwAtRnjXzHwnNGzG8QjiE%2BSIozTGHZNzvLztMOjfkL0GOqUBtZbTliI7IpOQWtoPmHSjPTdCqGQmDWBuECNHkrHdsorABMd4tmhaBbu%2BA5LnOfZwOrYFdgHWA00Co2OXcyut%2F7yBmkDkprrzOGXpt%2FxPTM0HG0ocQ9ABkkt8JRu6WD6h25hJLTqAoJrkLTR1EpfqxmQI2%2BJoMvp15NagvZd4dehDwkEsX3fqMFMSpbTwpjRXarhqKMP8Q84DJF1Qmw7ryf0M%2BScU&X-Amz-Signature=826f7e2f09ae0b4af7f18a17e0b390e9cdf7f3aa6d257ac3bfb69e03f7d5997b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=d4918b5dbcc7b59accf963bdd3822add417a8b450b64e8b530ac081d08f1a014&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=7100b1b3bf64b3d1424888d69a55978f33bdad8be91a0103e685d0d7d2f2b3fe&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=a69859d951042e33e226a91b946bc3717758f19cd990c7f5e1746c12ea248a41&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=930214c968371d9d8f2815d1aec364e206e607ce834abcdbb9665d8a7df71c86&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=52277e0311465077ccd2824b35e4df25d678db0bda234a9909790acd508a01ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN2KC3SL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCQVXjlGUQlY3R9%2Fy3jO4ssZ7Mmbjf1fTsBtGeYBXLTlwIgNTi8lFXLh5jN4T9MnplBwPZJxFRlkMkGq%2F6FhxcgilMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDHbOeIKzg3hDRGgfdyrcAwHC4nDY%2FS2rBberdgGEFuvuCyKfl05Aw%2FMQbbrB82Tuh%2F4dk2GkS7oRKXP%2FKSnbBdAJCRs0vMF9SSZhCcJ4SjJkF%2Fp27OVGSboo5YbUh5TYGRB%2FK74%2FPVR%2BHOrGWhj5QVcYYh5kv1FVFV52SGc%2FfgkaIoCK2JnGuDdCMlppqISGugvZQdAjWwuPJbgB%2Byca6cvCUF6faGmtdRfvrZJRfVt3ocEIK86QavtUEfOJVNulNOBPvC3nL19USiVejhy0AVwL7TraLJNU4zaAejVcrQ9fsACL4PUOyIDi8QEk0PqmnbPI0bGMW0FUStiXWqUBUJ8qLKFGECbqMYdWcbChFcJLcjfuIhNDAwOjXzLyEoGrnk6xdD22wMD1GLl1dFieK9YRPYPYLR72hcxv%2BWg8IRwg4S1s%2BFOsrsQZdYnoswzRLb6ZzQiYfM3p%2Fnh9JsMwXIZD8dmemEopO92y6gLGqf3gQ9pThV46qnG3FIKaRs4wV6DfGoHV1AXtesDKbRnfmbpHJi0sO9KMYxnQobYR4D2%2FoaRVWicL6CngjdwtN1Rq7dqA3qHuV1XLy5gKpOkJCYP8NBmd0edaO%2Bg3OuYJ4kIfnqGZoJxsjCW6Y1Z8%2BSHiGzSB%2FADvNYELP0rbMNXfkL0GOqUBZMHBt0mvML0rbUGDJa3jaARtdRyqS7JP2xUpa8J19Fj85ZyFQYQSIT6TPQwBsFmDEUeOEPJCF5Hdje%2FeHVU9rSjfKF0uLd4ifPkHvhzB4E7e8asfY9oeZngH4soDTAA5Ww4O5XjORnrojq6FTk6h%2FdlerD4R1E83lyc2xiUuDOw5MCvHKgnKqg12i%2BmmNJYwu%2FBxuwx9wIJxpYh%2B%2F1s81eck4G7K&X-Amz-Signature=1dd6259e3547b6d3a9661559b4564e449e4bc46d0874cd3027d25fae7911160f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EYZR3QZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIGCQSqoPkUUUK6AtrgWObW75NIrKgCEMhyl9bEaclKBcAiBHaVUOMbuUj6%2Fg3yOSYueRfyDZ%2Bk6Pz4wHTGpeTXP79Sr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMUqf5p6ko7FPf%2FhpkKtwDQxT6zQhRqzVhBhBNENay396G4MkQSxsWTDPfw9MDm2RtJT%2FIrFaxv29dvUj1xUgQ7uFIbayPiKFWuPm03ndXyqB89cekh7POj5c5eP%2FNEgQOKrsx81%2FR6nlrI6GJ6X6c9dL2c4FvtipGMIPAasXZSk7ip7SxoXHCp3KnPtbsiq2AmA3%2FjlM6UFtKzBDyOJeIC%2B41BtQ7EklGUBsPJCy%2BnyAIyudInxPwS5fIlXUYpfsHr3PrKcv0sj1qP2t34HkXnFIxk%2BTctswcYjixvlcDmQmFP0Jzb%2Bhbd2kFXcK3LCTuERXu%2FSwfphuRQzsLwcBFFxdeAZ4jKIJXyWm3VLV3%2FEkqSSRuEmr%2BTQ7SFUNNQmSpCwg9ndxMjZYP3%2F%2B2ZjE8TL%2BhKcJXuK%2BjqkafEeGHCwnWKH2I9c2x%2BT6EQv20IqP4UJKt86e3rDLTBKVPRfFZdKDgEFE7gS7vHMY30%2FWtST%2BStHA0rfOZpPUFxzneTiqwJCEi8kNd46xhOL4OZ3v8NtuzkeRPyOBAH9NbHg9mEDlKVay5fg9Mu3DiEYSLd5WvRbPLY2BZ7L6rSKQkrSkKCAOg42ZoLCBvv2%2BS1DA7rG8OJ9BvwKARNUh%2F%2B%2FlyO%2BTQiDTur5dTbGPujlcwiuCQvQY6pgEJY%2BfLxk6hIQGvjJPx%2FdW1Y4z1M0Phm54SZ3DlTDY4wiEsPt6zdsAY7asj7YXP45PxSIrstcry4HttR%2BCYHssmQyiyMc4G40kjIoDshqkW%2FyaAFXIOsqGZYcBjBw%2FNYm8tzzSarm1mKbeNlflZDE%2FxinIh2PSNBs%2Fi485%2FjiSX8b7bqle58FlinA06G10N92s8MFwtWPnKYgphgEyVsEAvYnYHhCRF&X-Amz-Signature=37a83025bf3a28fb559d683f28f9e7b6df9c67ada4d507dc9709fd0554c0204e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EYZR3QZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIGCQSqoPkUUUK6AtrgWObW75NIrKgCEMhyl9bEaclKBcAiBHaVUOMbuUj6%2Fg3yOSYueRfyDZ%2Bk6Pz4wHTGpeTXP79Sr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMUqf5p6ko7FPf%2FhpkKtwDQxT6zQhRqzVhBhBNENay396G4MkQSxsWTDPfw9MDm2RtJT%2FIrFaxv29dvUj1xUgQ7uFIbayPiKFWuPm03ndXyqB89cekh7POj5c5eP%2FNEgQOKrsx81%2FR6nlrI6GJ6X6c9dL2c4FvtipGMIPAasXZSk7ip7SxoXHCp3KnPtbsiq2AmA3%2FjlM6UFtKzBDyOJeIC%2B41BtQ7EklGUBsPJCy%2BnyAIyudInxPwS5fIlXUYpfsHr3PrKcv0sj1qP2t34HkXnFIxk%2BTctswcYjixvlcDmQmFP0Jzb%2Bhbd2kFXcK3LCTuERXu%2FSwfphuRQzsLwcBFFxdeAZ4jKIJXyWm3VLV3%2FEkqSSRuEmr%2BTQ7SFUNNQmSpCwg9ndxMjZYP3%2F%2B2ZjE8TL%2BhKcJXuK%2BjqkafEeGHCwnWKH2I9c2x%2BT6EQv20IqP4UJKt86e3rDLTBKVPRfFZdKDgEFE7gS7vHMY30%2FWtST%2BStHA0rfOZpPUFxzneTiqwJCEi8kNd46xhOL4OZ3v8NtuzkeRPyOBAH9NbHg9mEDlKVay5fg9Mu3DiEYSLd5WvRbPLY2BZ7L6rSKQkrSkKCAOg42ZoLCBvv2%2BS1DA7rG8OJ9BvwKARNUh%2F%2B%2FlyO%2BTQiDTur5dTbGPujlcwiuCQvQY6pgEJY%2BfLxk6hIQGvjJPx%2FdW1Y4z1M0Phm54SZ3DlTDY4wiEsPt6zdsAY7asj7YXP45PxSIrstcry4HttR%2BCYHssmQyiyMc4G40kjIoDshqkW%2FyaAFXIOsqGZYcBjBw%2FNYm8tzzSarm1mKbeNlflZDE%2FxinIh2PSNBs%2Fi485%2FjiSX8b7bqle58FlinA06G10N92s8MFwtWPnKYgphgEyVsEAvYnYHhCRF&X-Amz-Signature=77f063ec4f3cebde037fdbb42df7374e3c855221b66f48ee6217848e3dc48c65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HY2Y5KP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEL99KguV9u6IiPavt1h4r1eYhAQtp2jh6d%2Fpa%2FcLrb7AiEAoCyg6gVdV95ktalQAIJgHknhdpy80DVyG2sTeCrWnRAq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIMiAhDLOqluWEMmOSrcA8a%2BVqBg%2BfeiSd%2FAmyorrRe9p%2B%2FxWPiP4ElluL3UwZRh26AouFgl9xAurCtHksUn58Paaj7pxsNSU8tpA2wpsr9%2FnboRNud8par66Nyt0gEDXrWoarRFKGajGzzXETldNXcmxYLRLmfxKM5IqPNGbkEKcbCaDDyKnOPGHApIvVT7D7lli5AAS0refayK2Wlr0bwgoykAiPUfJgAUErltYaKqFrSDym64Ld%2BwpIvuTynCXmNSNJiOgQyu1a9W%2BACbOJ8cMQ7L4nSGs7%2Fx3OM%2BGkm%2Fh2cTqItmqq7lRCZR6kT%2BmT%2B%2BS3kuKPZ5F%2F1hXd%2FdI95BRErL8%2Buoyj2nNDjTTmH2pfz%2BVgDf5fLnksydU1EVoIZqFvpJmX9Q1nLUiv90IQ77tYt8%2FTcyXWwj%2BJbpG3PpHqS6%2Fwb5PTpUB5D8l741eeBbS9CKfjX6FtNTiyEW5HJlqtnxywg3B3XHsrZHROfgvLRpy88ouU66IAEH4LYCNmx9t4hcIss19G7wnSaqegos%2FSWNH4LIFcA72D%2BuV%2Fr5cL3FCVRKA9Knw8UZD8I73Bw%2FQ6gTcZ9ADjD%2FlXDZnSmCve5tW1LrZV7SQ0AJhkJnUktwq7NFpuEOfktzJSI97Lq2xELhjtntY%2B3GMOjfkL0GOqUBgTLXFG2YbiHnsdcR86dDzLifutlqOEM4V4qObR%2FM49M8dkNO2YoA3qRxOm8ORlvD8vLpfS4YZa53Ojl8%2FuVbNeFHIPJHF%2BmPUMyOSORhs98BYmppdbaRr7EaO1qZlLBfqrFhWOUn1wp%2Bg4fEFu0yEbtZ61kKRFiaUYKebahsjmAbCroXABMMzznm%2FMH2lDIo1%2BIAAx%2BOAvZzSaGqbArq54172xPa&X-Amz-Signature=58e76619f946574b61f0e35ab87d7986b99ea7c39d5208ab157b9a1844ad4504&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJWNCLO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCID1df4htYfWxMHtEU7j%2BEqyEHhrnEJYwvkIRDV0PvzkAAiBjZPWrArXKPjY4QVMQqriaddgB4D8E2GEnsoo6Kay3cCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMNeHj5%2F9xtRmkNORIKtwDz5cmEmVuIjyhL2INbOiXGWDOsJE94q3Y7eC3SJHE%2B25IggswZ6W03EvYfWT9MhDtaIUwfBtTfMfyc5o1dsm6OYInBQhryJ6CaUChCFesyw2yafmDiL%2F1TwfqnDgSyKqsPsvW0kqzYTFanJzCA0G4w1VipmzREnn8x%2BHbfa0hydTwePh7Ufu88mLUT%2BmW2hB4z9z41VQBxz2cqYf1Ag3SdSy%2FjTwWJj7xTfjldjebJxwFeqiObd9tIqz2L0okPfDF8sqUZ7C4jpBQiWogxhuNK7s001XHCLs5xAIldFDU3AtXX0xr10odmTsm6r6IEozkVIasX3MVut0VeDgVAjSIpzv0OjfFbImZzPan0SJdea4lkpKPTNCE0JouvFFJebj72urKY2TKNYwkXLEMcu1jc4%2B12lbYZQxGaJ8ZahINki4g6Hz8ud%2BQFh0eSFX1rC%2F9HL6J%2FlgeCReTrvXdSi%2BylwjIXXe2hQi%2B5Wy68HsM5NQVSL3lAXYZLfrcQxqZqZJNQLPGI6zTpFOpwtDz9LkaOwkTjYip47tQkEWyTcspA5s7MuJKzZjXERDPsyQLU1cqJ7j22U57r5AccnYZCsZHtBgH3y5HdUkCzSnFzMea%2BI0kQsCmPWWwHgxiqdUwwOCQvQY6pgH9eATTamo%2BKXcyAGQRiDiwnDEawu4DnINqzpUU22pl4iWTytFCcc4sDmg3yaIJZsvsHZXWK%2BuNI%2BPbYastzd04n2launy8LKkPf2SpyQqh%2BbWDZ9C5kYRbB0lydVYicVn04bAuE2Yg05h1RR%2BVOhMmJP6%2FsYUI4c%2Bx%2FE9qUS%2BePeAcFyUY9uOv%2Bx%2BWi2IaC2EnQCshCOOI1nk%2Fj0BXpAtdsB%2FMKaZW&X-Amz-Signature=9b8b5d8315aaf0595c78e1010956d2b81ae0dc46493705096601b4099676076b&X-Amz-SignedHeaders=host&x-id=GetObject)
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