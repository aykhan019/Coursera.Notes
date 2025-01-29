

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=718980d2ade6a44ce6873a4f2ca612582e1edfda320a2b1528b7ebba659b44f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=c20ad6e659ea1a3b7d21bca8698feaf74b01f54fe06c1299bd0748c25c221d19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=99bb0a0400cb78ddad4de8ef22f846faad60832f2af9b3219c7ac74e0543099f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=3e29754f8bf452e684f5fa26dbb52d18187914f14b11c7c4871d85ca017d0762&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=1961b153b42254e934d096cfbd337bb48df24e1123eb7975fcb03dc4e88e36e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=7c80181d57db3339ee95e23dca764b05d519fd04ede556ef23af024007e3d21a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=6c7fb7d601297c10604592959b0c1c897d53256382e3d4a0370e07a9b849b654&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=33fdbcfc06b0cce10d5dcc00d320378f9a32d1346ea42acec8538ddda7dec651&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=4f4d31c76fbbdd8cce17cfb40114a6599f2dbdb83a32aa3fc3bab5539d859ea7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKMU6XU6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhaZdwDH3R%2FHLOqSQprcCQzuL%2F8Ol5al5ytdDHQI%2F3XAIhAM9rBFz2DwpUGRPFKPxfvUJdpupXhEtfTVc1lYOb%2FtkNKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJMIxYVyFsPm4vzhoq3AMlQj0kl2yUzdS0BnmOtJzzJro4C9%2FDiFbcQrqWwVrASULRlkf0usYkbxQdNPGohrZvbbp%2Fq3xtwHXK2nE3kQzrku9%2FG0HlkOtCS5J6XOBk6f2WaGOqZZVCIGDLo3BFhj14cgsC31H3f0P9uHsPXLQcgLaQizOj6pZt%2FvrP1aQk54WGE9j9e0WD9J6qeAmPZz%2F9umYQ7fW8S5dVBAiVxNmFDF7YtmWgaiYJdzChHuyrYSEX7B6Q8VOEjoPAL%2Bvgr4zetm6XI1xv46DQs4zSRNGXxL9Z54%2FyUM7ted9ewz8eepJJQ4MTQzjb2mUqfUlXe3clvuikQG3V09VK5AhFSwqvJ%2Fpt8cmOGlwKjaPN6QHypYV%2FPJ1ZwFHTWYz1BbpvGuHVDzNN8EwvNggHdbhBEw1XND3UhtL2o0wwV4AeZF4pmOclsGAu9c7xpmT%2FQX7Ohjt24b%2B1yhDTAdjcTiiG6IWySMUBIs0KYbiJN6CoxahZeueEnmhR0kihJcp%2BDWH71UbGMed6ppvm5LsYbB9Oii7ClBmUqI%2BMAzxMbdk4gn3b%2B6U2baqrfcZXLrAsOCVdbvUNkcBcyEdu1z9HhvqJ7r1xOYzXiPm%2F03d585SdghQgjncoNEEuEJ1Zy%2FRyCTD9qOq8BjqkAearWlqHK5%2BursPCOdjbPJRKIPsg8YvCfAdxLjIrdxNa7nbKJPbLIW9h3Nz8CiPSxV%2FK%2BQ%2BS%2Bsz0b%2BxAlNA%2B25jqGWp93CAZNW%2BnL90qyoAyAPN6KFKWqgFH0DiGQXq6sY00xdfOPUiNNiC%2B2zQOy0J61TRCYMahREk6SGqmmf89MXyVPryYOvr0V2AJz0qOsN0iCCJ3GJZAAGoAa%2BrRdJIPwoPG&X-Amz-Signature=f43ebf51c6a03d29342d69550a4d8ca42cadbb1604aa88c99125d7cdff553a52&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKMU6XU6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhaZdwDH3R%2FHLOqSQprcCQzuL%2F8Ol5al5ytdDHQI%2F3XAIhAM9rBFz2DwpUGRPFKPxfvUJdpupXhEtfTVc1lYOb%2FtkNKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJMIxYVyFsPm4vzhoq3AMlQj0kl2yUzdS0BnmOtJzzJro4C9%2FDiFbcQrqWwVrASULRlkf0usYkbxQdNPGohrZvbbp%2Fq3xtwHXK2nE3kQzrku9%2FG0HlkOtCS5J6XOBk6f2WaGOqZZVCIGDLo3BFhj14cgsC31H3f0P9uHsPXLQcgLaQizOj6pZt%2FvrP1aQk54WGE9j9e0WD9J6qeAmPZz%2F9umYQ7fW8S5dVBAiVxNmFDF7YtmWgaiYJdzChHuyrYSEX7B6Q8VOEjoPAL%2Bvgr4zetm6XI1xv46DQs4zSRNGXxL9Z54%2FyUM7ted9ewz8eepJJQ4MTQzjb2mUqfUlXe3clvuikQG3V09VK5AhFSwqvJ%2Fpt8cmOGlwKjaPN6QHypYV%2FPJ1ZwFHTWYz1BbpvGuHVDzNN8EwvNggHdbhBEw1XND3UhtL2o0wwV4AeZF4pmOclsGAu9c7xpmT%2FQX7Ohjt24b%2B1yhDTAdjcTiiG6IWySMUBIs0KYbiJN6CoxahZeueEnmhR0kihJcp%2BDWH71UbGMed6ppvm5LsYbB9Oii7ClBmUqI%2BMAzxMbdk4gn3b%2B6U2baqrfcZXLrAsOCVdbvUNkcBcyEdu1z9HhvqJ7r1xOYzXiPm%2F03d585SdghQgjncoNEEuEJ1Zy%2FRyCTD9qOq8BjqkAearWlqHK5%2BursPCOdjbPJRKIPsg8YvCfAdxLjIrdxNa7nbKJPbLIW9h3Nz8CiPSxV%2FK%2BQ%2BS%2Bsz0b%2BxAlNA%2B25jqGWp93CAZNW%2BnL90qyoAyAPN6KFKWqgFH0DiGQXq6sY00xdfOPUiNNiC%2B2zQOy0J61TRCYMahREk6SGqmmf89MXyVPryYOvr0V2AJz0qOsN0iCCJ3GJZAAGoAa%2BrRdJIPwoPG&X-Amz-Signature=9d77069827ba90629226b27cf032d653d76856fc4defa7738933d577985d1685&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKMU6XU6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhaZdwDH3R%2FHLOqSQprcCQzuL%2F8Ol5al5ytdDHQI%2F3XAIhAM9rBFz2DwpUGRPFKPxfvUJdpupXhEtfTVc1lYOb%2FtkNKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJMIxYVyFsPm4vzhoq3AMlQj0kl2yUzdS0BnmOtJzzJro4C9%2FDiFbcQrqWwVrASULRlkf0usYkbxQdNPGohrZvbbp%2Fq3xtwHXK2nE3kQzrku9%2FG0HlkOtCS5J6XOBk6f2WaGOqZZVCIGDLo3BFhj14cgsC31H3f0P9uHsPXLQcgLaQizOj6pZt%2FvrP1aQk54WGE9j9e0WD9J6qeAmPZz%2F9umYQ7fW8S5dVBAiVxNmFDF7YtmWgaiYJdzChHuyrYSEX7B6Q8VOEjoPAL%2Bvgr4zetm6XI1xv46DQs4zSRNGXxL9Z54%2FyUM7ted9ewz8eepJJQ4MTQzjb2mUqfUlXe3clvuikQG3V09VK5AhFSwqvJ%2Fpt8cmOGlwKjaPN6QHypYV%2FPJ1ZwFHTWYz1BbpvGuHVDzNN8EwvNggHdbhBEw1XND3UhtL2o0wwV4AeZF4pmOclsGAu9c7xpmT%2FQX7Ohjt24b%2B1yhDTAdjcTiiG6IWySMUBIs0KYbiJN6CoxahZeueEnmhR0kihJcp%2BDWH71UbGMed6ppvm5LsYbB9Oii7ClBmUqI%2BMAzxMbdk4gn3b%2B6U2baqrfcZXLrAsOCVdbvUNkcBcyEdu1z9HhvqJ7r1xOYzXiPm%2F03d585SdghQgjncoNEEuEJ1Zy%2FRyCTD9qOq8BjqkAearWlqHK5%2BursPCOdjbPJRKIPsg8YvCfAdxLjIrdxNa7nbKJPbLIW9h3Nz8CiPSxV%2FK%2BQ%2BS%2Bsz0b%2BxAlNA%2B25jqGWp93CAZNW%2BnL90qyoAyAPN6KFKWqgFH0DiGQXq6sY00xdfOPUiNNiC%2B2zQOy0J61TRCYMahREk6SGqmmf89MXyVPryYOvr0V2AJz0qOsN0iCCJ3GJZAAGoAa%2BrRdJIPwoPG&X-Amz-Signature=2733dca4e6ce7113fbcc3fa33c02cb593d69115ac7f579bcd0a96547e3f36a28&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=af43ffd963dabafc631a58b7015f543ccef1045460209faf04de43b9ee584a3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=b2c9cfcc6920505aa983c49574797680dbd1aca7719effbe5daddcdbecf22d6b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=89e27f3f96bcb41fe7af4dd6d135248297a67cfbbded2daa816b3858a57755db&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=aede924bd94324722cb4db022ab0ec5475c62f657019cbcbd7c23380e37a9449&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=aa280a67c7900bb57d4667bada6ba69198e0fedfe071da0487ef22974e3ed36f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6QZBN55%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSZXf1KoVNytD%2BJOoTCGcOze%2FMoAtEpKmqOjj%2F2glu7QIgGTeO7r6S9UejK1%2BEcFkfPIIfBd9USLdR%2BmC0xXFs2pUqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOC7XKH0Bzq1TAjfFircA5JMFkuQDUM8oTJiXjhTyBQwcsKRaecoJHdOSw8OaFFvpzw%2BT3X1XqH8eiw18cTd4O4qL70BLqnTIjZYnH08XgvlWDHUxs4qvWOtPpwm1ySAWSzoNr6284wiubpfarCVFMKBFoyrwtMo6PpeROGvSDE7%2BQ8u5fjt7Dq2XvWpLadn%2Bw%2BwZfbjZp7wOYVJhxAUk5coM7%2BR8wMUl9qO53d6MnU3FLGmzYyTMHbm7gRAv2iARq0FFVM2%2Baj%2FRfx79vSdmhOlSU6%2BHWycJ1h4OCBhUgC2LzapbGx%2BoV3QGa1N31mLSmtWvJ7tWZhq0ws1pgOktQuJmFdelhh3qlsjVqndlqxe5zcmlwrZvBbBhwnLoDRvFRJpgVQ%2BIWsWYAQ4IONOW1LOTO2HCXQcFZvG1Y6BcYSREC9DGRHEmJcjuJvPR7jnHCdMi98w3wXctD7164%2FgW5S0KNAVyRgLErnIesFhWPl4HzVRyfWrEN0rPtSPAxo71zJrlBraDk604gTPDrB0cMLZ%2FLIC9CwNmeNcsOTaLGSoKX%2BmYf95rEcN9fyZIyR2l1srQ9tLoBn3XjteLD5XVQp8mbE8Rg8Yt3coReo1IisZy9hIPQ162DrQbfIZ4TJOnqaCMLRgBkVS%2FsTfMKqp6rwGOqUB5Q8P9Oq9CZJs%2BZVCxgHwits0kjeOR2K6jKX9cBSUh52AsgJq%2F53WuircMcev367w2J6Z6GArAiQ2aQ00p4FUEZ8A5tDAeNifuRG%2FKiocxkxDCuu7G%2BHRoikqVWRD18MxYjs7Gw4QrkJjeg5xSwhyIeN6xkCxOK9gbHNK9hJfYuwoEgVI1sDEyKC8UIDgtadq5W02nIdUqOvMj96eVHQLJLN0RI%2B3&X-Amz-Signature=cd8b59ea265049ac17f1f636ed916532d26253b33c59dec40ea011f1e97e35cf&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VD7XI5Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgdxjeuEy%2FlHJD7IlPq9Tthpy%2FZRt95fFZAP22PrjONAiBsTDiaAHPbUxu%2B9GUzYIJHEudcQ6RLkRxsG7bfjQDKaSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXoLUqFrGbm4MAuRKtwD6OzHCrRqDUd7rh%2Fp%2BIo82%2FzlPTI3xBZT5s67TqLbc8xlL8SMOmWp6I%2Fcab1jz7%2FKmBn2FTfW%2Bj1GkavwQxt7o1cdJTY%2B%2FdcWcjoD236B1mZa4HUmq9JJkPhrgB78DhVjk8tN2Lb1%2FTY240CkWbHl1I%2F%2BQQiZrLyEnzptUgldrxoeBlUPHPZt5mpgj3kOI%2BEtUcRXEtrsH%2FxDfFDfeETBag%2BHM0Eg0QcVUTxWG%2FONUY7Fmv91iSsi%2BXxmJf44i9Egmnoz7IohjEvczBRdV3EWfvuzaZY44sQfHRgZgkpfILeDNIxOYZweZphiBiZMQIn9aMla%2B2AULQfafa8KXykDWnA9IOMVM2oEVxfcRg4Qr7UvvuViQztFucjpVOk7f0YV2Sy%2FXrVAXJMcYxNNMxCEvMTLGIyYFdj7u1G%2FqK36tNsexlKPilpH%2BcLXdrsYuaAmk06cIjxd7%2BdjcC8tjPTXQanQMOZ9KuxJa4tgYQgxlqXNiRC4YBORyd1UX65o3VaENMH1ZVlQtRiDwYJ%2FbORllO1j2S278aoqb%2F%2FVXYUtj0It8dtdj7SsdKJFykNQmpYivOW4qmRvfat%2FSkmpsrVlKrG53lts3h73yYtNchN%2FVpCmRnDV7Fp4kFr%2BVYgwl6nqvAY6pgGun5DY5ZzFDAgEV6B5qYVUMgDcmjc7P%2BQZUA%2FNxWwHyJzHVfpJv1b2fj4k1iFWxjNrBGPL19oO%2B4mw65Qq%2BckPICHnUr6kokpUrXGOzJVEZtRbO6NRLiJbDum2Asx1RZGshOVnYieW0AZThzTyWcdbbBmQyh27y0C8XtTcrgm5F0zHrDjmfMn4l0b4rIc6DtR6q7EfCLnpU0kRitQJaXnJ%2Bk8zdPG4&X-Amz-Signature=508e7e5dd217d773768d58672b83e284fb087a208ef09208858419e0c8371b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VD7XI5Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgdxjeuEy%2FlHJD7IlPq9Tthpy%2FZRt95fFZAP22PrjONAiBsTDiaAHPbUxu%2B9GUzYIJHEudcQ6RLkRxsG7bfjQDKaSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXoLUqFrGbm4MAuRKtwD6OzHCrRqDUd7rh%2Fp%2BIo82%2FzlPTI3xBZT5s67TqLbc8xlL8SMOmWp6I%2Fcab1jz7%2FKmBn2FTfW%2Bj1GkavwQxt7o1cdJTY%2B%2FdcWcjoD236B1mZa4HUmq9JJkPhrgB78DhVjk8tN2Lb1%2FTY240CkWbHl1I%2F%2BQQiZrLyEnzptUgldrxoeBlUPHPZt5mpgj3kOI%2BEtUcRXEtrsH%2FxDfFDfeETBag%2BHM0Eg0QcVUTxWG%2FONUY7Fmv91iSsi%2BXxmJf44i9Egmnoz7IohjEvczBRdV3EWfvuzaZY44sQfHRgZgkpfILeDNIxOYZweZphiBiZMQIn9aMla%2B2AULQfafa8KXykDWnA9IOMVM2oEVxfcRg4Qr7UvvuViQztFucjpVOk7f0YV2Sy%2FXrVAXJMcYxNNMxCEvMTLGIyYFdj7u1G%2FqK36tNsexlKPilpH%2BcLXdrsYuaAmk06cIjxd7%2BdjcC8tjPTXQanQMOZ9KuxJa4tgYQgxlqXNiRC4YBORyd1UX65o3VaENMH1ZVlQtRiDwYJ%2FbORllO1j2S278aoqb%2F%2FVXYUtj0It8dtdj7SsdKJFykNQmpYivOW4qmRvfat%2FSkmpsrVlKrG53lts3h73yYtNchN%2FVpCmRnDV7Fp4kFr%2BVYgwl6nqvAY6pgGun5DY5ZzFDAgEV6B5qYVUMgDcmjc7P%2BQZUA%2FNxWwHyJzHVfpJv1b2fj4k1iFWxjNrBGPL19oO%2B4mw65Qq%2BckPICHnUr6kokpUrXGOzJVEZtRbO6NRLiJbDum2Asx1RZGshOVnYieW0AZThzTyWcdbbBmQyh27y0C8XtTcrgm5F0zHrDjmfMn4l0b4rIc6DtR6q7EfCLnpU0kRitQJaXnJ%2Bk8zdPG4&X-Amz-Signature=c8340fdeef36d0ef34df4f4c078867953c0a56ac57210a134938c3b2e476d6b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636F6FYIQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7Ct0o%2F3WEDU1DwOA4lqXE8E3oCxFj19dO64O1Tn4c%2FAIgYlvTwOmw3ALR8bXiRRpSX7Hf%2BoyJZB2SuCcr8k6WLdoqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNiCQTQ7iBD%2FTFqOTyrcA01rejWKvqjQ1zRc4aztA3%2BVvYVirIowNMO4nUZrywP7zZbLXYBfQw5HLjrawywjrpTDo%2Bp6MT7MQACKN%2FP5RUb34I0Rk5ckRdx9VwP%2FcSNDCpxSol%2FZBxU6l9hvsGXxxn8AH3N8DjgKPgMI4styF7ngkKUqzjZJz17t6EH4TWnCu3DU7Ns2woL5YEj9%2BOq2q1ay8O6l9QFDDryD8KKNLKqet9Vr5HBwZvVfPI9kH%2Fo31%2FFQk8tn2chV8AfbG4leebrw%2F8WLtewF%2BPeNw%2Bu4BB6ZcWPF9f4POpzaYXA%2FpT4bXbElnzjD15GPykwJiKzYnJSVB%2BnHd8uzuOvSD4oZIaoFKJhDrHX1sdAgK9gIAQnPFTSdpu%2F86izeX0swMMylCOKaUhvKSzJjKp6kGyyc2bwGSKebOsEx6%2F4Bk3F6WGOt3%2BSP%2Fshx3r9b50KQHcRhzKYWjJ5rbTlLU4h4vGurRm25ObwFeYehtzUOc6DLwkISz1IHrYNRVB%2BXjvR5ErR4umobPyWGliq%2BsVClMutGQT0R8DapL27z0%2BUkp5SnFX3xs6ezyyL8mFJ9ObiC5JFVv%2Fhnk1zpKAxXNpJ%2BkH%2FcK8zapOF0%2BBzPS4JBy4rRLXaurRDWcuINXliLmg%2FKMOGo6rwGOqUB%2B74VEavOPMWNBurhunuj%2Fr5%2FzHrccgs%2BFXAEGp1WlxuaCbqY77lBbZZSvYDUC5UEFaV%2FZpB0icslWSKgd%2FNyrXsfwhwhl4u8YWDltZXS7ViiFOgTIAUYttoJSS83u2wr8Pso5a8vAHuz9vhOdg9U26eHGDVdd5FeCdn2rdVHNDNM1SJrqwWpdRGAOKVLRIDAiuJC9y%2B7gA2rFXgwCLgeo6fpD%2BGs&X-Amz-Signature=67e9e7862c900759918d445cb4168dfcf0db3a27237bb2cd7441c13a8b90ece7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNDODFBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuutAyDubFrUKUzA4JHnDzbe3vr5BaXe%2BABh0LwkmGWAiEA%2BWRlQmBf6%2F1Pl6eo6a%2FVF7ZqGRYTXesToGRjFNPrMTcqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0KN7bg14FG9Gub4SrcA5VMQaN153nqWl4kuVTvKLW8%2BrzURsH%2FIEwZ3q2%2BjsLWtjAPbfkWf2BPylFwrs7%2F0b8uRN8JcAvRymiZNcC%2BB4PiL9NbJeeK96fWzxRlqLPEAC4mPQ7K4E4EbPFCtgAzpaeh7jUoObYIkSp6X3jVNlTFpI44ocGKFgEGYUTceOoj8Go%2B1%2FKsICFQdI5hvhZD77Qlyol%2FZ4%2F%2BIu4092fOiAHgYxekwBwHA9ePSxKk%2FJckSvErXo1qBpT81NnUcIQxhudw5H3Mfz0m7LrSF70b4rcy9iaplrOMRiBctz%2FDgBrSrAM%2Ff0mTIwH2z6NQ0wvF9Z2%2BBB6xxd9BzXM6uaea3OLoeNtLpCZhrQNakMyJzEdCDvptR4Pl7rcIzWourkTbt4%2BSRMQKdWHvum6S9O8hgo9PnSn5FGdyYU52eCRCTgpXmnXjsyafePT4Hul6z7j%2BTcyWEq7lhy03BogSoJBn0o3OggyawAPrjOaHqhBabo4NNhMWwO8%2FCCsFvXOOLk053nLD%2FRaS%2Fq0MP7uJBLOS90J21tbjjQZ%2FK%2FrGr26TErQjErR%2FADl5zmcidRJAfHKgkcZz54Jd0Q16dAw89tNZZ%2F2Z3IlZXd3MKYPgUnnnXzBIdcGI3ViuOrpiKnbUMMSp6rwGOqUBx%2B08LNBzIa1MDLa%2BrzNr6zCJFDSilJuDeBPfjSQNLua%2Fv6kCfQrYo%2FyCFvJZd7Qteh87VP%2BorX1He1%2FUvtiI6A4BQsyT06KNksMU6XS6moofUHaEfLeoh0Ybv9q8F0DOol7Zk5i1lV0D8hcCydG3%2Fr2rXnNihhg8oQ9zFtYGGKXyvfVe91URrpLt%2BAijksQfqiSAPPa2nrcR7NpoH3jYbl9nbkVe&X-Amz-Signature=9937b92ed71d3598b17c83a4f12099c2f0a1758b07f47e1cb717b7738b6918c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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