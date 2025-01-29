

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=b1d85360bc241e693037dbb93c1388dc18b5eb54d301e75abd6e7a4539e649d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=9b90389b3e9119becc2df0ce902f9f17d7cc977c2e202315c846c30b9765f035&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=b97d8c9ad64ccaa6ab8c66e14281e2d9365a13af526a75834bb355c478e35de3&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=acb6b76ed8489ab9c893e05c791f6ebc3da4b31b49be2e7cca181de7d688b4a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=75afa40d68bc86e5476d6b178afd21409ccc8331b75f1227b6798ba7e638bae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=74531283903cafa55698704032f4e5d77ff5864a323ee0308da31025ce168ce2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=cc2f17f379ddd249268bd449a2040f9f586cb8bf4e59887241a055d712d17c34&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=1b74749c677bbc91f0daf15f75605659b879167bd984d703d58a8e9ed52a03a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=62d0debd68832c90859db6ca6e06fc5b0eb13dc86cab4591bff558913f7c12e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665475TPCH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmNgPq93KZ8qwpPbi3qINsQj3i24aM%2BnVFm37DXS39sAiEAnZdOy2i4tYhSiXpZsV%2F6B43UkWYAHq0%2B4qk8Y2arP7cqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCPaesHOm%2Blmte6KyrcA5mxdi8sIyr526eXMFGO4Ov8%2BF6%2BHxdaEDLRW2fveqJYgc%2BYU9nyAGNowLb4HSS1mRN92tRKiQe5HfIxPLtCqNTnXUKguX2gwGnqxJT8ws3nviPit0fkwOIXjj6CaKLuXyvpOhCfU6%2F069tkbSpev%2FkDo4CwjgG%2BLW2rNeRjpe5CYh4F1jEC1WTagFQtY4pa2XRd0tu%2FMHL3w7r6VXNOk0RSUcjsZuiurMBP3LbkqmsXbpATMO%2FZQwh31%2BLh7DHHbUcVCuwkXzS0ww%2BVaRJ9rvkKm5kf%2B2s3kE2hdk7PuOkIZabQqkz13iBQVRwLqLO4QAsjz6SCnyk02G2bi6%2FfoJjCX6%2F1Q3hLEtbGbZmODoHvQDYT7fp58Q9rGxBbY2abay%2BO%2FaGlzQE1MfGAM7Fzwks2cjs%2BU14gg0RyC%2Fo5bSpnr4gSMa7%2FbRwI6HBzRMgfx6aDyXQG7D4YMAacFHQlPPfI5YS3B5TnFVhBD2nyGbi7DXVrpoQwZ00%2B2m7DK22gFdcJYhooHiAV95qE7AuBrV9SMNgLKejXoIkhA4HvTD4aiN%2FLxwngdAJLsLVOny7zr%2FSPxCzPiPkrhy%2FicDnW0MyHpQvyTY0m8rKVuiG5EKmJRTGw7bE%2Bri5hqTy9MMvF6rwGOqUBXvMk%2Fa38TyyiI%2Fk5QP30HBmkYtLgzCX4vW52kH52uTWXZMxtuqIhX6s6Vg3GlfWKGzEJYJ6wo5BHoM5TiaIuwX89V42dDR8VIoPxhSost6m%2BiqLV%2FSpo9cVMeuiUO4eI5APVnM5CaAfVIU4729bHjxT%2FooI7HXRW3bL4%2FN398Zj9zN42CBqT8mP9XgAyR53uSFYgkSfe69JOPA2gBICG81zfxgXZ&X-Amz-Signature=82c17d3f22e194d318bde0fa5ca370900b19fdd10b54afc3eb604b321e102144&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665475TPCH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmNgPq93KZ8qwpPbi3qINsQj3i24aM%2BnVFm37DXS39sAiEAnZdOy2i4tYhSiXpZsV%2F6B43UkWYAHq0%2B4qk8Y2arP7cqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCPaesHOm%2Blmte6KyrcA5mxdi8sIyr526eXMFGO4Ov8%2BF6%2BHxdaEDLRW2fveqJYgc%2BYU9nyAGNowLb4HSS1mRN92tRKiQe5HfIxPLtCqNTnXUKguX2gwGnqxJT8ws3nviPit0fkwOIXjj6CaKLuXyvpOhCfU6%2F069tkbSpev%2FkDo4CwjgG%2BLW2rNeRjpe5CYh4F1jEC1WTagFQtY4pa2XRd0tu%2FMHL3w7r6VXNOk0RSUcjsZuiurMBP3LbkqmsXbpATMO%2FZQwh31%2BLh7DHHbUcVCuwkXzS0ww%2BVaRJ9rvkKm5kf%2B2s3kE2hdk7PuOkIZabQqkz13iBQVRwLqLO4QAsjz6SCnyk02G2bi6%2FfoJjCX6%2F1Q3hLEtbGbZmODoHvQDYT7fp58Q9rGxBbY2abay%2BO%2FaGlzQE1MfGAM7Fzwks2cjs%2BU14gg0RyC%2Fo5bSpnr4gSMa7%2FbRwI6HBzRMgfx6aDyXQG7D4YMAacFHQlPPfI5YS3B5TnFVhBD2nyGbi7DXVrpoQwZ00%2B2m7DK22gFdcJYhooHiAV95qE7AuBrV9SMNgLKejXoIkhA4HvTD4aiN%2FLxwngdAJLsLVOny7zr%2FSPxCzPiPkrhy%2FicDnW0MyHpQvyTY0m8rKVuiG5EKmJRTGw7bE%2Bri5hqTy9MMvF6rwGOqUBXvMk%2Fa38TyyiI%2Fk5QP30HBmkYtLgzCX4vW52kH52uTWXZMxtuqIhX6s6Vg3GlfWKGzEJYJ6wo5BHoM5TiaIuwX89V42dDR8VIoPxhSost6m%2BiqLV%2FSpo9cVMeuiUO4eI5APVnM5CaAfVIU4729bHjxT%2FooI7HXRW3bL4%2FN398Zj9zN42CBqT8mP9XgAyR53uSFYgkSfe69JOPA2gBICG81zfxgXZ&X-Amz-Signature=309cb370bfdbfcebc959c33820f2e55fcc9347cf68ffc333887a48c18d7d30bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665475TPCH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmNgPq93KZ8qwpPbi3qINsQj3i24aM%2BnVFm37DXS39sAiEAnZdOy2i4tYhSiXpZsV%2F6B43UkWYAHq0%2B4qk8Y2arP7cqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCPaesHOm%2Blmte6KyrcA5mxdi8sIyr526eXMFGO4Ov8%2BF6%2BHxdaEDLRW2fveqJYgc%2BYU9nyAGNowLb4HSS1mRN92tRKiQe5HfIxPLtCqNTnXUKguX2gwGnqxJT8ws3nviPit0fkwOIXjj6CaKLuXyvpOhCfU6%2F069tkbSpev%2FkDo4CwjgG%2BLW2rNeRjpe5CYh4F1jEC1WTagFQtY4pa2XRd0tu%2FMHL3w7r6VXNOk0RSUcjsZuiurMBP3LbkqmsXbpATMO%2FZQwh31%2BLh7DHHbUcVCuwkXzS0ww%2BVaRJ9rvkKm5kf%2B2s3kE2hdk7PuOkIZabQqkz13iBQVRwLqLO4QAsjz6SCnyk02G2bi6%2FfoJjCX6%2F1Q3hLEtbGbZmODoHvQDYT7fp58Q9rGxBbY2abay%2BO%2FaGlzQE1MfGAM7Fzwks2cjs%2BU14gg0RyC%2Fo5bSpnr4gSMa7%2FbRwI6HBzRMgfx6aDyXQG7D4YMAacFHQlPPfI5YS3B5TnFVhBD2nyGbi7DXVrpoQwZ00%2B2m7DK22gFdcJYhooHiAV95qE7AuBrV9SMNgLKejXoIkhA4HvTD4aiN%2FLxwngdAJLsLVOny7zr%2FSPxCzPiPkrhy%2FicDnW0MyHpQvyTY0m8rKVuiG5EKmJRTGw7bE%2Bri5hqTy9MMvF6rwGOqUBXvMk%2Fa38TyyiI%2Fk5QP30HBmkYtLgzCX4vW52kH52uTWXZMxtuqIhX6s6Vg3GlfWKGzEJYJ6wo5BHoM5TiaIuwX89V42dDR8VIoPxhSost6m%2BiqLV%2FSpo9cVMeuiUO4eI5APVnM5CaAfVIU4729bHjxT%2FooI7HXRW3bL4%2FN398Zj9zN42CBqT8mP9XgAyR53uSFYgkSfe69JOPA2gBICG81zfxgXZ&X-Amz-Signature=a2a6a31c8a16586c92a17fa23985c09dc56d4c5ad5979eb1b4d66fc45bb57213&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=f78de7fbb8893d4344abe6816383b0e2fdcea5d9ed0516416ea79407df11e1c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=1fa41ffa39ed42a3ca59a36933f9dc5ab084834d3da229649e294a333441f6ca&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=89166ae78806eff0988827a384e34b35a86783f4da16db12d598fdae706f58d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=390c3a403b49feea1328ea02bf68664a51ab7fa4722109bd41a6d2b2797aa17f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=725ccfe066bbf8bbaad1c879d195a785685e8310311bbb7a98ef9cb25a160b4c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LFRUA3O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY58gUPTQ1992pVmSvI79lHFsZiGVMUpXFDqmYKLsX%2FgIhANK0Gd0zpGkRKwYv6snkm1yNnTGKZdpAec5y5p%2BQrzMyKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2FO8RmpYfZUImYwq3AONqQ8qKvsv%2BCRf8QXWgpPg25Ece2BOe%2FHmYLfQFwj25JY5NzNRc5gwIHgmByf7AcnNHosLGV%2BSEA6aT1ot0ZGbH8hCVfK4MaQciUspvtAD2jywXuWkw48uCUdPLWbOmUbb61ahtc3UhlwkU6rh6wvIlYAfWaEkCMbG6EZPc96ItPQdoUhrL69PZyOsiQ8COkOdXMtB9pqJcLZ2MOWXX5NKZHlnxdNZZJThOsuUc4f8Ne2rMm2aGB0%2BRfZzlg7QxOPJUSS4QzEZtJn2xX3jjoqPp9t9neH3Bhysw%2FuSa3CLN8RHHq8hkS%2BTlhQxmwhqcVMKnmcNpwMyUqTDniPCsq%2BDC3VXgIQdVqKQZdu%2FI%2Fa1KzIOJQ9rgBZkFRE0MBw5gLtll1PFBpe1MZjIAF9FQrDUE8i8sn%2Fw%2BuihHklKoR1jlLXYbd%2FC6jg1rCv54PiXdURz4aRHFhmY5r91bKiP1LvgyEQ%2F%2BX6XkWSBON2U4tULlxIDqS5oIUN1JDHAuKBdUlsUH0O%2FJPT0LMlrQHV1O8cggeLf%2F1jhkHG7WGIdn1DX2JcAj7aZz4u09MN%2Fx%2FQUEpmIHbF75768F6IH2fgszoSf%2FqAwLm2d0at8N0rrARbkZWY6zUNaZ0XxSedZijCRxuq8BjqkAWqmsEDKudBMw0vqm8mNkVBRRzyoW2%2F1Wdd8FuBgHtjjbs933BVzZpVOTGYXi9BWMFsATcxDggkTXcF2fz%2BrFGpYtagBCnohP6aNpU6FobqEwYU%2BnNit71Dg44XS69KUobF%2FcA9mL1Ni5JjteJI0uEYiyUJxFWwG%2Bs51SfMEuxDtpGmOSBtKnpEWDxR9Q5aH4PbRu8BImLlViaeZPrcszZmvwdz0&X-Amz-Signature=79848b9bcaedd9815e2f30984d2feea7d3adc7614cccb926378145b22635d804&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3ST3UI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGeAPHJppY70NTpm0Dt2CfTlhH7Fx7Y7VwA6WETIUGEWAiEAokCwnO%2Bc38OlwdUSppANntv8AtmuHjS8L6girRJtibMqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG3%2BkT4%2FwhI43ysATyrcAwIXmRerGvJpf6huwjd7gAkAu3rezZdpLIcKYqL4W4Ouh1Tg7xg5r7aCyjuMDatmk2nOdozMMkoTavELCqkjy8jyeMwNazsg4J%2FpT6hEPycDkACjMf1s1fSUTbQj45jjccxgA%2BuEFsUeyBtruPscDo5NQRGg6BzhwUSQ0NEya3RfbucCb8YwkHQGTJzaJ0OScvj3nSKHxL3BJ3QujB3oEgzLxMgqrm5k%2B9oK3txWcFe8jOEVHfA4M%2FYa5M1Dt8WeNYENa8qRcUpk4RBKkSxt8dLzIknF6Jh0kV%2BSuRPsf8EKpXAvvIVmZcZFjfWLdrZd7FG0HR6TVIc4fEDIzxQYHCLoY1fsjS2HS2nN7TNTPTf9CGkGoUMFMxo9szwb3QCBV86Ya%2BH4HqZauYJrLE2cwqg7ckhinKlcsOgykRBNNsoO1g8wAS0YbxGvowxEivkyf%2FA1eyyIgTAopB3dhu19RjbwDNtWaLyhBlDVUYsnFEtLNbvszqG0eXPUg2kejIqJ9DlFaph4WxlhvdHpGmcbHFJ%2F3Q0F41h0QV%2FJvXQw0gxFqXMT%2BihYAl4WMRLXkBaC0JN%2FLLvmMNeLowzhs9n5xernyTVmxqu5Km1%2Fel%2BDn8%2FybivEdbOoA347F5SiMN3F6rwGOqUBktHGbiAJ8PKyqhkSFx6eiDe4XFoles%2BZMwC627Uz2l1keEwdNeTHeDsTPKD999n7to58Ss%2B%2BtBjDYhJF92Rbyl349QvuhVxCoFnsA3CYhEZBYdnpJCu8fREWgXf9%2FYwTKSvn%2FfUj8hmJfJMaT3GZafNFy9hCsDY%2FkBnQl7HfdPWO9QZU9sQUOriRO5QTRrLZANRd8VoHZ9PgJMQKWHAWYshuyIYY&X-Amz-Signature=22923d295eaadf8664b85881e9ba387a11a14b734efbe8bc5b982b7b9ac76d0e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3ST3UI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGeAPHJppY70NTpm0Dt2CfTlhH7Fx7Y7VwA6WETIUGEWAiEAokCwnO%2Bc38OlwdUSppANntv8AtmuHjS8L6girRJtibMqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG3%2BkT4%2FwhI43ysATyrcAwIXmRerGvJpf6huwjd7gAkAu3rezZdpLIcKYqL4W4Ouh1Tg7xg5r7aCyjuMDatmk2nOdozMMkoTavELCqkjy8jyeMwNazsg4J%2FpT6hEPycDkACjMf1s1fSUTbQj45jjccxgA%2BuEFsUeyBtruPscDo5NQRGg6BzhwUSQ0NEya3RfbucCb8YwkHQGTJzaJ0OScvj3nSKHxL3BJ3QujB3oEgzLxMgqrm5k%2B9oK3txWcFe8jOEVHfA4M%2FYa5M1Dt8WeNYENa8qRcUpk4RBKkSxt8dLzIknF6Jh0kV%2BSuRPsf8EKpXAvvIVmZcZFjfWLdrZd7FG0HR6TVIc4fEDIzxQYHCLoY1fsjS2HS2nN7TNTPTf9CGkGoUMFMxo9szwb3QCBV86Ya%2BH4HqZauYJrLE2cwqg7ckhinKlcsOgykRBNNsoO1g8wAS0YbxGvowxEivkyf%2FA1eyyIgTAopB3dhu19RjbwDNtWaLyhBlDVUYsnFEtLNbvszqG0eXPUg2kejIqJ9DlFaph4WxlhvdHpGmcbHFJ%2F3Q0F41h0QV%2FJvXQw0gxFqXMT%2BihYAl4WMRLXkBaC0JN%2FLLvmMNeLowzhs9n5xernyTVmxqu5Km1%2Fel%2BDn8%2FybivEdbOoA347F5SiMN3F6rwGOqUBktHGbiAJ8PKyqhkSFx6eiDe4XFoles%2BZMwC627Uz2l1keEwdNeTHeDsTPKD999n7to58Ss%2B%2BtBjDYhJF92Rbyl349QvuhVxCoFnsA3CYhEZBYdnpJCu8fREWgXf9%2FYwTKSvn%2FfUj8hmJfJMaT3GZafNFy9hCsDY%2FkBnQl7HfdPWO9QZU9sQUOriRO5QTRrLZANRd8VoHZ9PgJMQKWHAWYshuyIYY&X-Amz-Signature=1cb0506eff4290a6f33f705cf85a6508fe0b3d42c9796e5f9b2787951009130f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FDTPD2T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXeqAtBnqo5z4Z6WaLCbmYKgZMia6PYZaVT3fJMIruQgIgaya0%2B5YFjvHwEGyW6YgOmh8rhBd539ulA9cxGeLe6IEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJP%2Fe%2BBnmgJ4%2FdUSuircAw771XwHSO1225djlrF%2FKb4Z0Dm%2F2GxE1y%2B%2B80MHDOQao9nji5wAQ9X3GegtI5Cza7wtHIpRXTyqLdffMDrzOlgpi4zt7%2FXTW1wPFxG5VU6D0plX%2FYJifIwfVW08s9%2B9wg%2FtAzAC7KrRTzrAaRYHMWW9xpk5KmeTwQVAWKuv9R1lUccwPMGiGxDISjCReFAOI146jGePfjw6ij0VZpAnO6ZV3Jxv6LkS9y8YTocY235uDQwvpcUDAML9DTQO426NWNSuDseN2R1vCKlV3rsKMAEiJWe5zUg66SlmGox2c%2BXn9Zq%2Bn2CdXWSxVJz4xEj72lnRBqhde8Z8eLlMagQyMs7OxJN063oAI4jOEjydqTzVy3JPn6r4SFjOj5tPRSHShVibbJc2Lh7hkGrFPwywCi5FCrXpuQt6nEmfPmYe%2BNkomadFj2i6V0Dl7jeIkKUDu3vBc%2Bdl83mpkbcvMEaQt3lxnOccch0SV8c8wsIQmXWmydQNYxR7EOt2TSPZbTjhcY0H3SmzA9e%2Bk8ai1F6uqtzoVLzwubJEW%2B9SkIio38m0wlYqJAPIq3WCUHlRllWQ99uXGfDscFTah1GSejI2F98lYPn1M5mLpHNuasSt1jJ0Oa%2FDMiis5eqXV9vKMPfG6rwGOqUBfNSNp4dN5vfIYmRP%2BQVObKyegpHS8nUGDEa%2B5%2BS8HN%2B7FeLRF82BJSd3u14q2K2JK6NkrwvcVHjj18QLfja6TaUMrFA%2B5Sr%2BlzbgFPSG2Jc7GnkI1YVCDpGzoMy8F8dn182r1FzU3H0YzNHJCO8HyNj%2FFHqFkc9gvkD3rEZiBzqS7kP8XrMrYyWWJ9eE5%2BlJz1irFHzLxVLj%2BR6O6OjkxghUhB%2Bg&X-Amz-Signature=040bc027eced33c568060db3843f405de43b069973ed4c84e332637b5d389dad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUHWSDN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FCyYuPoaehhRjvD2SdRm8rXh6sZTWobKXUI1cgf7EwIhAJ4JiilVS6x2z%2BvX%2Fa9m%2FgeaeLQDhiNK3u3%2FLmOLit8HKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOUhIoT%2BVpdnfcmpQq3AN%2BGiHn2uzXAVhpnM%2Bwi9ZsBdvGBvvkcV7zxpXYQ6AOIV5FG9CQdWs3Ndy3HqL0kIlTWyEQQ5XwggTrCu15yZMxeTEkP3RPUxsJJTykEM6BTchV89ZjHZ4TuYjKQXX0Zu1qf%2Bndwk32yFxiaq9rn%2BfphqiiqMzilfQCn5drgzsUDaNaUt57r7iU16zhXUClFOmSgcCs6NN35uljOxcKrKY0jjwsWiGVx%2BEMMIDO8GqPdW%2BFPGmoc4eX7gJtJ6pS29JTyzf%2FMHlk2GvXOAi2K690nClsSXmDzmfrbQde9yieIfxsJr0kAUj6VyqdflHsTwYaDTUpe98JzYOkBRpQnsKFcqn5By40YXZvCxAgBpgrpa7HfAHona4LhRRHmGSR7h39X6fc2E8oksTxT2uIImF1m%2BkzPMBcu30AB%2F3hZ88DulRYYeITXaPEof2nSrMO47m7b8tsn0YIckJh9u9OgF7BBG9P1eS%2BBrREv7CuygARo1f4qwn0Ts2MBNULs3vWPnwelB%2B%2BQqnVfjLz4fM0ENvpQMUJO93gYNjJM23HcI7MXGNUaiMc0cDpIoiMnn3dpLTg%2F4Zm1Iou%2BgYWYc%2BCJPHLSzxiRDNVdGWFur%2BSd7tGkE%2BrLalg%2BaEWhW9onjDfxeq8BjqkAQIB98KKr2HOmGk1iJiONaxOcTAKzhIeLopwsRFE2KQXDeR3Q1SDE%2B74RsjFaUc1J0aWB3d7zRE%2Bcr2oJ50rV147eW1fFLCqjU%2FxVhIT2pAR9f9h0NXGdHjxj3J6im0S%2F8XMhd%2BGnk2t8WYvWP7NC789Xxcg8HMZ%2BKB2HUiGmE5vy5sNreQplARCWfaCDrqEU1Zj5Yj2rrKt8GJbXQYyZRQH26xO&X-Amz-Signature=32d027201e81ea0bc40587d41218b0a99f1daff3761d348d151732e2d3ca512b&X-Amz-SignedHeaders=host&x-id=GetObject)
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