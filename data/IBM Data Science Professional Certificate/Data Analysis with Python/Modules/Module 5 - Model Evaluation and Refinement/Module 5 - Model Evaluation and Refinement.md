

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=0421780c33c42642e6bb90adfa07ecc7aef8cf0ab5b4cf5780531b0eff1a959a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=9fe5dca82955c26825946f66fe6d2dbae11a01837fec64673b688489d99f80e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=83bab9d0e16751db65d9a24db6261b72afd162959d5acc59db0359efb5c559c2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=93439b84dc3c561a93135598ca6112ecfa06e2152ee8b6168bd08e060477b2e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=a4d5c57ee0d714cb34d7596eb08703ec60e95f4ba6a334ac96d2ec69248e973d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=d7a311372c553825b9bf16e8922ed73bdb5febb4f161705820604428199ff837&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=a124719920997c47f0ec8112ab38add9c4a06641b248a36a4c0636d413a37e74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=adf6ba43de76ff4343a9959de9b3185e9857e8eb892a20e43561dae76e866834&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=2e574c47e194ccc3099e3244e892690b34c269d1eb845b8c1c1a2dca5231fea8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YJMWEBQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDGoL14r%2BLrb3xQ0OfrhZRwIKijiJ8gxIgMVAmP0uS9qAIhAJug0I1iFGRY3iaIkYC5YC7UgFyIaVFx2QSO5oY7ZdgiKv8DCGMQABoMNjM3NDIzMTgzODA1IgzUHhRbbWPY4jIe4SAq3AMUe2kToDXtlHC1DWess06dFN%2FBQ95bDkpHkZwaIiu8HaaIg7FRbEwQj546Z14w9lbM724Hh1LnNPkA8geQx5II7MOLpzxgVKc1wcGYSeW7SzostyHbDlFC0DS%2BACO1eNYI8YIkCcRPDon6FCmOBgI1MzbiCidc%2B%2F%2FFrLJvePtJWLRam%2FhUg3aGEObNA2nbN6uItnYcH1xn1HGcQYyaJ25wyQIpV7hsdP8F2ZBC9FoNdn2beHJ4zLkUgBk%2FecRxZGIjfsLg56m1YD4xagVeR17pctesZ4u%2B3qmSMKO8GvrQInWCudDJvUOWLYb%2FZFE7mnt%2BBOXBXXS7us%2FRy2SovZIQXibI%2BMdSVdgnw%2B5imWD3CUvRSoDyggwvsGtlxU%2B3IGkrXRkbt3J%2F%2BHkMUohJu4rSX%2FmkfweJhCJQnNOoWRXORBK6bT6zVSjRaLwK1Kq0%2Bu6Lmv2oDtP%2Bi5FEmEGqaDu2jcqF4pX6ok8NJAoJ%2FnnoYBIa04xWwm3EAAiRrxulLv0ViRA6QLNyg5oz%2Bq%2FRgBbcHJOYSo0Ztq8c5oFHG2vHcf0OVtxdhJXXeod8IPLm89VUi6c3QST%2B15W%2Bj91xYCsjLHAYfcfXzMOR%2FD68tWA1GyZ%2F7I%2B4KkxnaZY8sTDe%2B5O9BjqkAXA3irivt6gi1aqcCvxmKtcrom4AayJyOnqI4sjm3Py3EQjmmYnuqfgt1quFqhF85402SoiPENM7I3yUDf4Ov3NkvZsGeRf3NUMsQFaqqWqWGQdJwbRD49eCmm0UC6f2cn0zdyYrsSP7Ip7u%2FIICz6Is9hfxVcI7qxTRjAL0O5uN6gzmDhsi6Z7oRkXjknfGaGCOemUdQKumsGD%2BwAmvUjABnDyO&X-Amz-Signature=62f33248a495dfa00c609a1e1faa3a17e353a1110a3e229657e300c09b5bf2b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YJMWEBQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDGoL14r%2BLrb3xQ0OfrhZRwIKijiJ8gxIgMVAmP0uS9qAIhAJug0I1iFGRY3iaIkYC5YC7UgFyIaVFx2QSO5oY7ZdgiKv8DCGMQABoMNjM3NDIzMTgzODA1IgzUHhRbbWPY4jIe4SAq3AMUe2kToDXtlHC1DWess06dFN%2FBQ95bDkpHkZwaIiu8HaaIg7FRbEwQj546Z14w9lbM724Hh1LnNPkA8geQx5II7MOLpzxgVKc1wcGYSeW7SzostyHbDlFC0DS%2BACO1eNYI8YIkCcRPDon6FCmOBgI1MzbiCidc%2B%2F%2FFrLJvePtJWLRam%2FhUg3aGEObNA2nbN6uItnYcH1xn1HGcQYyaJ25wyQIpV7hsdP8F2ZBC9FoNdn2beHJ4zLkUgBk%2FecRxZGIjfsLg56m1YD4xagVeR17pctesZ4u%2B3qmSMKO8GvrQInWCudDJvUOWLYb%2FZFE7mnt%2BBOXBXXS7us%2FRy2SovZIQXibI%2BMdSVdgnw%2B5imWD3CUvRSoDyggwvsGtlxU%2B3IGkrXRkbt3J%2F%2BHkMUohJu4rSX%2FmkfweJhCJQnNOoWRXORBK6bT6zVSjRaLwK1Kq0%2Bu6Lmv2oDtP%2Bi5FEmEGqaDu2jcqF4pX6ok8NJAoJ%2FnnoYBIa04xWwm3EAAiRrxulLv0ViRA6QLNyg5oz%2Bq%2FRgBbcHJOYSo0Ztq8c5oFHG2vHcf0OVtxdhJXXeod8IPLm89VUi6c3QST%2B15W%2Bj91xYCsjLHAYfcfXzMOR%2FD68tWA1GyZ%2F7I%2B4KkxnaZY8sTDe%2B5O9BjqkAXA3irivt6gi1aqcCvxmKtcrom4AayJyOnqI4sjm3Py3EQjmmYnuqfgt1quFqhF85402SoiPENM7I3yUDf4Ov3NkvZsGeRf3NUMsQFaqqWqWGQdJwbRD49eCmm0UC6f2cn0zdyYrsSP7Ip7u%2FIICz6Is9hfxVcI7qxTRjAL0O5uN6gzmDhsi6Z7oRkXjknfGaGCOemUdQKumsGD%2BwAmvUjABnDyO&X-Amz-Signature=c7c6e618a13e14d579b1cf356725f4b1308f559b60d9daa34a3d4a33060e0226&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YJMWEBQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDGoL14r%2BLrb3xQ0OfrhZRwIKijiJ8gxIgMVAmP0uS9qAIhAJug0I1iFGRY3iaIkYC5YC7UgFyIaVFx2QSO5oY7ZdgiKv8DCGMQABoMNjM3NDIzMTgzODA1IgzUHhRbbWPY4jIe4SAq3AMUe2kToDXtlHC1DWess06dFN%2FBQ95bDkpHkZwaIiu8HaaIg7FRbEwQj546Z14w9lbM724Hh1LnNPkA8geQx5II7MOLpzxgVKc1wcGYSeW7SzostyHbDlFC0DS%2BACO1eNYI8YIkCcRPDon6FCmOBgI1MzbiCidc%2B%2F%2FFrLJvePtJWLRam%2FhUg3aGEObNA2nbN6uItnYcH1xn1HGcQYyaJ25wyQIpV7hsdP8F2ZBC9FoNdn2beHJ4zLkUgBk%2FecRxZGIjfsLg56m1YD4xagVeR17pctesZ4u%2B3qmSMKO8GvrQInWCudDJvUOWLYb%2FZFE7mnt%2BBOXBXXS7us%2FRy2SovZIQXibI%2BMdSVdgnw%2B5imWD3CUvRSoDyggwvsGtlxU%2B3IGkrXRkbt3J%2F%2BHkMUohJu4rSX%2FmkfweJhCJQnNOoWRXORBK6bT6zVSjRaLwK1Kq0%2Bu6Lmv2oDtP%2Bi5FEmEGqaDu2jcqF4pX6ok8NJAoJ%2FnnoYBIa04xWwm3EAAiRrxulLv0ViRA6QLNyg5oz%2Bq%2FRgBbcHJOYSo0Ztq8c5oFHG2vHcf0OVtxdhJXXeod8IPLm89VUi6c3QST%2B15W%2Bj91xYCsjLHAYfcfXzMOR%2FD68tWA1GyZ%2F7I%2B4KkxnaZY8sTDe%2B5O9BjqkAXA3irivt6gi1aqcCvxmKtcrom4AayJyOnqI4sjm3Py3EQjmmYnuqfgt1quFqhF85402SoiPENM7I3yUDf4Ov3NkvZsGeRf3NUMsQFaqqWqWGQdJwbRD49eCmm0UC6f2cn0zdyYrsSP7Ip7u%2FIICz6Is9hfxVcI7qxTRjAL0O5uN6gzmDhsi6Z7oRkXjknfGaGCOemUdQKumsGD%2BwAmvUjABnDyO&X-Amz-Signature=d80ef4a09dbc18b4e6df7bf087e7090587e63da81995d3cc60e3de7c666e4087&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=6c0d1a92f3d7dc2dfcffe2a7c20f8248b0e0622989ef4278565c4d8f0831967c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=8196617afb46003a3badca7ff704911797648cdf54439b9118222ab7fff1fedf&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=d94d858dd822f1d949de01913bf187886ab6bce02a45f7dd1fed4d01c63d64b7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=b46ca1dd2286fe87d77065e5d55027d29f4d41e950ee0189dba5958fbecccd3f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=f03c678a2bd0eef08850c257ab2bd3067530a92c3d84ca6dedec3eba39e4e1e6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FDVFHRB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCVBRZo4Yx616Y7RNfgpYXVyQjx1%2FNyl29gYntSgXJoIwIhAOKvgihLs3GogtqQuuyZTorgzML%2BE3909DeWBABCkuBoKv8DCGMQABoMNjM3NDIzMTgzODA1Igys0idUCdSCHdVuEUgq3AP7k39Wnw3wg2Yf7KAhk%2BDh8OcLyZ9TyU4bztKbgphMj6dkpVTa2G9wQM%2BBywvmlBdxalc%2BA5xuiRDQlZOGVXRwF3%2FvgWQeiwVatICwN4WUiw946iUsASh4a0fW8vdKJIGxVA8VLFNVskHDNscGyOiltUJ37w8fVIlQuEIhgHpeL2vun6Q5bqSgTJssLX9ADS2ieUWgHYLZ3oIU%2FamEGq8V%2BQYOuar0env%2BujdUzzwemtqhOK5%2BYMKt%2FGwVgQdedPNOPOhVVRTl1aKKJMMj%2BkjSpHw%2BKzc%2F%2F3bgpK5qsx%2BqHIIDvuVHWmDs%2BXcKkp9hMORt910j64h1NvxgMQD16EnyeLxFAgVQMgucBtJZmkj1EX0D5f4TTNTw0bwqHdj%2BttBlaWYPg9EdT6AsHylGzrSgJ7phaWP%2BNchYtGRcBP9cFyWr2be1sO2%2Bij2YMrnpnn1r3tlQBwFkxzDGnqExQR%2BiOSbCYp6sf9xggGZJZ%2Bl0y5TGVZIG2hyejmzSku2ZxsdoTkHDWM2%2BZ%2BlGcOpOj%2FE4rxUwtIC2Ep7MYD9IXOQ%2F0%2F7QKpVyZ7pUedGh%2BqrnfVlwdPhxtqa2%2BuQRAt1z7MKi0u9WNtE%2F78pcLwx7oyOkhhwc4O1HFFuUK1zYODDS%2B5O9BjqkAU8c9GyxllegU9xZxSyiYKqn2jWZ8I0BqvlYwXkUYHbqxUGh7SQ1X%2FImntsXguYcKJd9iYxMFKeRgGb0uzVrvnQtNXVK1gftSuj2C6K%2FzDmSDo5RtWXmnhOOAk0%2F86b6v1B%2BJnh%2FTyc8%2BnttDbcN0bfVM91If87SdGBDf%2BW%2BN%2FPfZtKS6PcqaxSCRzAfzd2B7idf51jOcgDu%2BVO7yj5EuAEUtudU&X-Amz-Signature=f03839fef4fb070b34d2777586f7211a20c34f85454072ef8324d1fe95e90b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QGU5HDM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDwFGE1XENHv%2Fp9PNS6UjPyGyvb40T7RKj9QPZiSKXe7QIhAK6lU0nu4jvXa2MvUZu5gnr0G4AEIjlz%2F4P3BtjWI0CGKv8DCGMQABoMNjM3NDIzMTgzODA1IgyeQL9VQigBAvYJPHcq3AMU7MQH%2F2gobWEhgSNL0805G2TvyzSD3BNI2gP3g2BPGMT8XrkUJL0ihgJKh6l7EZfgw5I8eu1G525tJaamQ7pKuYBf9mO%2BFwSXyetralTBKYBql4bLVeBkGpD%2BvvVrjyK6YAALe2v8NdhJwF0esKA%2FpVoSWEJS%2BikU7w1ZGzTXNJ5bGCSe8lDIL9GHCa1kkjLf27cpDhedCGStCrj6mu1ekOO080odihWvcpkevGRV7v%2BLdiQdxC2v9uwEdCQEueZMzp8hCxRIr2gxNoEDlFNpkvKnhSJ5wJIHgECH%2ByhseouwH%2BBLxOf7L8eSV13NZKIvU1M%2BEm6f6rZL3pq8htgg3fAu4WQDUx1jKkNQzG4FymYhb2VD5BiKSAwWykfGJbo1CqbYYs7uzTGu0DqeVAa4xXG5rF%2FWpX4KJ%2B%2B5gki9AHQ13uXqLoesvT%2FBNBk8MoNfSjzUAaI00E6NsEzpmDaO18WT%2FFts11kbfiZwGLDhsJ3zpBspUlE%2BQlJFb8ZulHwvuPrQIIPOCzlooc2z2CIqdfFoskoXUvm2RluF73vd2%2By34rfv6Fb4O3S0cyeUGW1FFfoGh36RSevWCjeBokXanfT5P%2FjU4Ap2ITCKni4RbldEjK9zci7n8jwzPzC4%2B5O9BjqkAdt1wOI3gI0%2FQYtFYADGT4IltXYhz4kiqkUsb8fOGCQx5GGQ9cNXJ0vvDXCE3qnLvyfEqV1kBud7Tu0uRiiRBKNESidg3Kj23nssfXjqWOyV4RFxVQC8aOxbcZpEOz4K7F%2BsT1f0RhCnB1Xoq2Yq859ErUSdl9xyx8PLZxdbjmAb7hiPqEr%2BH13sAm6YX7Gh4xVbfvmKI4uO%2FgofApKziu9l2QLY&X-Amz-Signature=d9c505d49042511f0c812407a9c365c88ebfa7016ef775664ba730de7d492134&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QGU5HDM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDwFGE1XENHv%2Fp9PNS6UjPyGyvb40T7RKj9QPZiSKXe7QIhAK6lU0nu4jvXa2MvUZu5gnr0G4AEIjlz%2F4P3BtjWI0CGKv8DCGMQABoMNjM3NDIzMTgzODA1IgyeQL9VQigBAvYJPHcq3AMU7MQH%2F2gobWEhgSNL0805G2TvyzSD3BNI2gP3g2BPGMT8XrkUJL0ihgJKh6l7EZfgw5I8eu1G525tJaamQ7pKuYBf9mO%2BFwSXyetralTBKYBql4bLVeBkGpD%2BvvVrjyK6YAALe2v8NdhJwF0esKA%2FpVoSWEJS%2BikU7w1ZGzTXNJ5bGCSe8lDIL9GHCa1kkjLf27cpDhedCGStCrj6mu1ekOO080odihWvcpkevGRV7v%2BLdiQdxC2v9uwEdCQEueZMzp8hCxRIr2gxNoEDlFNpkvKnhSJ5wJIHgECH%2ByhseouwH%2BBLxOf7L8eSV13NZKIvU1M%2BEm6f6rZL3pq8htgg3fAu4WQDUx1jKkNQzG4FymYhb2VD5BiKSAwWykfGJbo1CqbYYs7uzTGu0DqeVAa4xXG5rF%2FWpX4KJ%2B%2B5gki9AHQ13uXqLoesvT%2FBNBk8MoNfSjzUAaI00E6NsEzpmDaO18WT%2FFts11kbfiZwGLDhsJ3zpBspUlE%2BQlJFb8ZulHwvuPrQIIPOCzlooc2z2CIqdfFoskoXUvm2RluF73vd2%2By34rfv6Fb4O3S0cyeUGW1FFfoGh36RSevWCjeBokXanfT5P%2FjU4Ap2ITCKni4RbldEjK9zci7n8jwzPzC4%2B5O9BjqkAdt1wOI3gI0%2FQYtFYADGT4IltXYhz4kiqkUsb8fOGCQx5GGQ9cNXJ0vvDXCE3qnLvyfEqV1kBud7Tu0uRiiRBKNESidg3Kj23nssfXjqWOyV4RFxVQC8aOxbcZpEOz4K7F%2BsT1f0RhCnB1Xoq2Yq859ErUSdl9xyx8PLZxdbjmAb7hiPqEr%2BH13sAm6YX7Gh4xVbfvmKI4uO%2FgofApKziu9l2QLY&X-Amz-Signature=8ee7ccaa538d496aaccaab7fc53b3dbbcafc27a2e6a15a9ec4d24da372c7dca7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKSWDDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGzYUQQOTxXrv%2Bu07HzVA7R8yWDk8T2CD8hSOXgzQKH6AiEA%2F8O%2FveuGK7fErDSqfmz%2B%2FuKezATNhcaZi3zAIGK%2BwlAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDJ39kglnF3H7A51EbircA1UIgw3EEpLUJpfBEo82z%2B53dafhHbvrdWJNxDzrlzduJBwF8H6%2BwPK0rAorzQ3gE6fypLu2O5krNZssCvAHnCxEeBRqZTNma21BpaQMf5iVVorlGkO4R5IW8pDhBrQA5qo8%2FC41seglRlw9NLwJMFLynu6RUOA%2BG5fIXIcoyPpEN5u1OMnjggqE1ZX7b%2FDUPw%2BlCB%2Fhz5WB0DR1npZFY1rk8WD9o0ljkHpzbUuW%2F8498RQLpA0ZbrMlinCf4r%2FdiF2em%2B05KRHKFica8KD6jIkDRvkpxgnfao5eb%2FtoyEkK%2F2NtGU17eGflZlQU8R18vSictIVtG%2FWkq2LQloUyVYwp30Jr86ZQMO9c5%2FU2rcywFrzMA4lPOrQ3RUVUOYkmSP5eGBZExIusB3sCm3%2FAuKY6sDnSkPi2ybC5FzjNqBXXKE20wW6roI2S7Q7btOA1iMks%2BSVWFkkrcrTGTGI0U3E7nhMFt2655EItcAvtjuQ3OYRw0olm964IrtutMMOWRidfHACrwPaArMz5tlSsxpa5UTV6kk2y4u06FkPJ3i%2FVZICplbpJRcUA2eb56R3jUpy1ZTUNp%2BhKKq1d%2FOz0nrL7djFLGbMt9cakLaidoslpvc96WLh%2FtIBTTRx7MPX7k70GOqUBjqeUXJbWyumfqN4ApDYnNJahqaYyItsaqp07Jy1S19qDbpG180w8UerzMa7UrsFcRqf14ojsCTxWpqlXQCWVk2dhgrHi5bKYhpe5c3Xdhv3Cx0gX2zMn%2B64X9bvnZHb4E2PkILOngGM0yenamQvsvBUtkPpyo%2Fe6uhtDp0WkD673Sd14VugfXTYMcwcpU4ZliBQKO%2FCJBVvLC9dqw8r6FhtzHZdm&X-Amz-Signature=50fcd2ffaab28382c47ef222425703630717a434f92c1b95aa1580c85d38b787&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=4aaeafba2ca277f34fbb2c09e2c5a554c7b5e6b95e02b65ccdf1b43bc1550819&X-Amz-SignedHeaders=host&x-id=GetObject)
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