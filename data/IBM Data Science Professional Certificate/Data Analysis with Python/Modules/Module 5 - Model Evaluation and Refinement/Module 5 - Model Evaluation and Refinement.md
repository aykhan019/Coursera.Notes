

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=2377e0f43160122968a12cce709e1e37156ee9983e546a4d922a3beeab55c4de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=576b9ff8a30e1472e3b3ed0ad2fc00c60f95bb1e7a2495c0750b41cc0c66daae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=8d3756a04dd69159236b1b914015cea182edd2286a53fa1da9e1ef37ed0fde65&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=263cb8bd54258af4068c0c3e902ea65f68b71c37c8f72f3e623a54472dae9342&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=c324e308d1af2b5de8648dd556384ae3fb7a1e55ebd248c861cda0163438e263&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=24ce2c4ef96fec7463377db68a18d304ba2928e12e1368639333c96ad211d9a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=39588fc4912153ab7f0fd3b0f1790ff983edbf94cef4978450f730a47c8d59be&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=664216877cd0d24502fafe68720783b114b25a87a1f1aa1542f7f82ad5765549&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=54def1100d7665bedba8011ce2045187fc0fbae3ec8b4b0942494deed8727009&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBIPKWE5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIA5IJaMprkl7Wc2XVhUU34yHyW0rRNJA57ox7i5nug8YAiEAgtw3U9qio%2B2IA7V7XivzswxvPQG3p256paTEDCywuDQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGcjkCRW%2FjjwD7FErircA%2Bs0lxHiXKBoSi1FUHigeYIpwcQumJqMDc0oUDEjt0y8OKdXbFB5Z7EiV%2B6Kp0uqlJu%2BjKOunKs1Zs%2BM496vuMz0XpofP3KNK5LIZRahPpZNNAftS2oLcntpLxbmAzeOgx%2Bf2wwuG%2FgcMqiJ3reLaDBkNYfdWiUQKt2Qi7HX4HEsZdrmCOl37RgLQWQkJSa3QhpOuntGcJt8Wvc5tMsuQUvVuSgA%2Fs8Nnev4JObgdO2sn75XK9qHhcUjzAeq6OnLBg9QOYbPzZnkNS9PJQa5Qg4a%2FEDuCOQEl73ScIevqJUAFcUUln0e%2BbgF6%2BBuJ7z0b3nm8OR9LCRxxVfZ0C%2F4jfXCjdTAedUa%2BvVqEU8F1BkcK%2BUcIeYzTiCLUxYPXxb3RZQfabVAuXuBHBCOnNj%2BvtUpJIMS4l1WkgIWLPJ6lmRUsbD%2BHU4BUbvzNURJse21uwHaF1gPnv99ALlQH6WXpAHckx74cB5kyYXNn5GO5J0h7NOyoV7dMWBZEzQpnkwJcOFLSFkHjrPC1YtJfRgMoLiYK3jPJX4luM3cZUtXGeNkRqfKlsiq0BP5MezWFJ7KxCfBQbJW167G3gEHJ2U2afsIOlMpExVjbgm18GyWS5W4oP9mMSqXQNEaKMqKMN7Kg70GOqUB5SLAf9UqeEmf9oXiURgsI%2FldnuHpUlTHMHgCRht7lxNLahpsiQMTGnbzh%2Fl6J51nztEUKCnKbUPoQfvvANDaO0fK8QuCzZuvb98g4X%2B1KdAPSwyVkgZjhlfWa0lA7Rn2JfqK5c8UhLDREMFh%2BftHiiILvUKYJAtbuT9uXp9BuJYHnYMv7jl1wLci0vJkTinu9GSvWjuw2R1FsSQygn08%2BEweguON&X-Amz-Signature=0405b8aeb9d7f23f358a0d68af1e34d71cce527b25dbfd082f4358d4e05d769c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBIPKWE5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIA5IJaMprkl7Wc2XVhUU34yHyW0rRNJA57ox7i5nug8YAiEAgtw3U9qio%2B2IA7V7XivzswxvPQG3p256paTEDCywuDQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGcjkCRW%2FjjwD7FErircA%2Bs0lxHiXKBoSi1FUHigeYIpwcQumJqMDc0oUDEjt0y8OKdXbFB5Z7EiV%2B6Kp0uqlJu%2BjKOunKs1Zs%2BM496vuMz0XpofP3KNK5LIZRahPpZNNAftS2oLcntpLxbmAzeOgx%2Bf2wwuG%2FgcMqiJ3reLaDBkNYfdWiUQKt2Qi7HX4HEsZdrmCOl37RgLQWQkJSa3QhpOuntGcJt8Wvc5tMsuQUvVuSgA%2Fs8Nnev4JObgdO2sn75XK9qHhcUjzAeq6OnLBg9QOYbPzZnkNS9PJQa5Qg4a%2FEDuCOQEl73ScIevqJUAFcUUln0e%2BbgF6%2BBuJ7z0b3nm8OR9LCRxxVfZ0C%2F4jfXCjdTAedUa%2BvVqEU8F1BkcK%2BUcIeYzTiCLUxYPXxb3RZQfabVAuXuBHBCOnNj%2BvtUpJIMS4l1WkgIWLPJ6lmRUsbD%2BHU4BUbvzNURJse21uwHaF1gPnv99ALlQH6WXpAHckx74cB5kyYXNn5GO5J0h7NOyoV7dMWBZEzQpnkwJcOFLSFkHjrPC1YtJfRgMoLiYK3jPJX4luM3cZUtXGeNkRqfKlsiq0BP5MezWFJ7KxCfBQbJW167G3gEHJ2U2afsIOlMpExVjbgm18GyWS5W4oP9mMSqXQNEaKMqKMN7Kg70GOqUB5SLAf9UqeEmf9oXiURgsI%2FldnuHpUlTHMHgCRht7lxNLahpsiQMTGnbzh%2Fl6J51nztEUKCnKbUPoQfvvANDaO0fK8QuCzZuvb98g4X%2B1KdAPSwyVkgZjhlfWa0lA7Rn2JfqK5c8UhLDREMFh%2BftHiiILvUKYJAtbuT9uXp9BuJYHnYMv7jl1wLci0vJkTinu9GSvWjuw2R1FsSQygn08%2BEweguON&X-Amz-Signature=ac2f07e684287db9336c9613224d44a7f853e9d144166fec817eaf60e781a143&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBIPKWE5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIA5IJaMprkl7Wc2XVhUU34yHyW0rRNJA57ox7i5nug8YAiEAgtw3U9qio%2B2IA7V7XivzswxvPQG3p256paTEDCywuDQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGcjkCRW%2FjjwD7FErircA%2Bs0lxHiXKBoSi1FUHigeYIpwcQumJqMDc0oUDEjt0y8OKdXbFB5Z7EiV%2B6Kp0uqlJu%2BjKOunKs1Zs%2BM496vuMz0XpofP3KNK5LIZRahPpZNNAftS2oLcntpLxbmAzeOgx%2Bf2wwuG%2FgcMqiJ3reLaDBkNYfdWiUQKt2Qi7HX4HEsZdrmCOl37RgLQWQkJSa3QhpOuntGcJt8Wvc5tMsuQUvVuSgA%2Fs8Nnev4JObgdO2sn75XK9qHhcUjzAeq6OnLBg9QOYbPzZnkNS9PJQa5Qg4a%2FEDuCOQEl73ScIevqJUAFcUUln0e%2BbgF6%2BBuJ7z0b3nm8OR9LCRxxVfZ0C%2F4jfXCjdTAedUa%2BvVqEU8F1BkcK%2BUcIeYzTiCLUxYPXxb3RZQfabVAuXuBHBCOnNj%2BvtUpJIMS4l1WkgIWLPJ6lmRUsbD%2BHU4BUbvzNURJse21uwHaF1gPnv99ALlQH6WXpAHckx74cB5kyYXNn5GO5J0h7NOyoV7dMWBZEzQpnkwJcOFLSFkHjrPC1YtJfRgMoLiYK3jPJX4luM3cZUtXGeNkRqfKlsiq0BP5MezWFJ7KxCfBQbJW167G3gEHJ2U2afsIOlMpExVjbgm18GyWS5W4oP9mMSqXQNEaKMqKMN7Kg70GOqUB5SLAf9UqeEmf9oXiURgsI%2FldnuHpUlTHMHgCRht7lxNLahpsiQMTGnbzh%2Fl6J51nztEUKCnKbUPoQfvvANDaO0fK8QuCzZuvb98g4X%2B1KdAPSwyVkgZjhlfWa0lA7Rn2JfqK5c8UhLDREMFh%2BftHiiILvUKYJAtbuT9uXp9BuJYHnYMv7jl1wLci0vJkTinu9GSvWjuw2R1FsSQygn08%2BEweguON&X-Amz-Signature=0cbab580ae1de8ad66d272d9b854c58b0d329f1ae610a7382479c747f1df85dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=892a15de9cd370604cbe05334d03bb7dc14b77cd08ccc739c3865a8b8b95447d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=270fd308831cd1b1a56b822cdf2fdc0f84604a97c6ea1da48ede2050a2b2e5a4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=4209d62ea7f5607dd06b5876b0f2736573e6171b613e0f4106850e1c635fd9d4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=28e9fb532f5959f8d6accf9a85eed7f5418f768b3a162187f309ddc144c3487a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=cfa68e0fa1ace78a647bda701911b0d6996348f32283c2d0a526fd97ef14da8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNE3XLOA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQChwIpn7%2Fi1%2Fs%2B%2F%2FPlw6fpAms5x2D96uTiKjQW%2F%2FuOH9wIhAMh9eRM%2FYuMMtSzRittJH3RcuTelLqbFDQY1DHqUVhn8Kv8DCBkQABoMNjM3NDIzMTgzODA1IgyXDcn7b9gymIKLasIq3APq7%2Ft3dJyy7Xm5fStPznbk6EIE75TTRx1rTUTx6CgUZpnUDYCOcQBwG68suniHgAMlq42GTFRHyXVwRuiR6VySebCsDgd9NEuvUc44Mu7tgmhbxcdB6chwa%2BLdgzwRh9H0FUKKGOfZ9ja4uw9x06z1sxJN2v502vHmZnidzxhTD8LI7ZIZ0aLNQ%2FRDvoNO4FvGt8OtzLsD1xHAS6qwZ%2BUTdgfagmvIK3KXnMJk4tESlX0t1MFcOb1CooVOaGO9H3aPY%2FtEnTZm4QbUjC3XtJLlz%2BkyiLIqOd%2FI5SMYbTiXbtqlSdKJkU6CHzY9b8iu6irS%2FHglJ%2BBBBWabFz7iOkLR%2BccMtCulaYMnFmvAi0%2BV3NDk4UeuAXjT01pCGsU6WwDVqYohyehwVVhLUcJc6DzepLTLmTPHwiYiQfw9a41OPdSvYZJV5AKerMrwfk%2Ba5MnzR9wv8b%2BqNnO%2B1rHSqJIBe7JBhmYKSPA9XQrcdXCkowgKiemESxabYvuJUXLQIgRh%2F%2BNh747N2XlDDPlFxu2S7mK25iUZOG%2BTg3MRoFVxv9C776UP8G0CmreaEDFR5WMeswjUmCJt%2Fusa8%2FGQ2D2bnq9vEm0UjapLcQdkt9v4V%2FgrNnhFZvXfkQymSTCxyoO9BjqkARAd2iGUBRcOvIj6z%2Bxcze6CuhuYpSGxokHjvmH%2FgVac7JcmdwfYnpBOT%2BWEiK5sTJChYwdCUdzU%2Btd9PSWP34DKnEEZdnEjOJfExX3NR9gnuEQMJTsJ2rap%2FHUInZjnOpRxsOqjB9HA2SuNVBrdmK4fBm%2BuUf9yWHaR3zjawbuNTjJALfVy54iJW9HkbTzbR27aP2iOAVbs1lQnVEhCf5xQFjsP&X-Amz-Signature=c90ca05cb5fc9d8a3d099b6e4a8bf73e99d6ae80613a19b595cf8d1b1d6864b3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQNQOXIC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCWVir0%2FakswoMAL2HItXq5OMTEaB3gH8iwmP%2FgnV4BLAIgOXfxXbKW6QVpr8sLAD%2BOKzpCv13BSR0bPpz%2BVivw%2BZoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDPidjt3L1CXufNCGZSrcA7uI0BVIKcEnRLlTQfkd%2FHdAPJqEjUirc2weNt5H%2FvtzknAisXvor2F1iZKww6IVnW%2FpJiGpQJe5OC3DrYNbzhv2SWKuy%2BFsDFDIc3lNvnM%2FJkhaESAxlgJmetPWzoxihzuqfi%2F16zBW15fz1LLP6tJlpLZkYmFrrCjDo2FVVNLwgS%2B%2F0blosBZHngXqunRBTAVshIzdMhc2tw7HKQZHBHFkvKGbHFD0iDImDwtfqvu3Sakd5JW863GSqZh0ex9z%2BqfUr9zGWMpqjPIXy8ifiAh42juuOIVTWy9dRf%2F00HnMaXhkJPVMA%2FsBnmS7zxCOiJ0bNvHda4hsvedsKAtm9GkLEjvmTa47aKWnj3c6F4cneKFMfLak%2FiQ2YY2MPUPwt9s1l7TlwQARit6lZgMl7emvFMwoO8d1Yi0M92QoYcQIfXz%2BF1YOpSCMdHF68YJCVgcXN8nc6pEarckehk%2FuOjqPkkqmB2u8KdLrYG576VM%2BKxSrmp2SEb6K941pDQpnqARgzO8%2BkUgiZHLpgNOOWP7S7%2B7GmnxEBUtVoS0GutTmYCDCJ6SqFpQ1%2FBmObtWopMTKK5MrygqRZO2wk6x9mwEy0%2F%2B%2BNlRUJujw%2FvguVN0YrWtDeZFJEQfqC6SoMO3Kg70GOqUBymeJaZeJmCoja9tlb%2FMHnlFAbuSX9GKHryBMbWNJys0tzSOY8DPdOuoU%2Fkiiz0a%2B2wetZtEdDh6g6YPalVjUsGeUNbZFxX70JvsdR9qr8%2BkPCz1Q52ODG9g948yT%2BgKE5bK0WUHC18sQzT2O0oyglzkEeJtn%2F%2FDqacvt4OyPKaqCfbVPUYffgkbONtP5B8%2Bxwa%2BEMTA0oePp6l6ErJ%2BnT5hf%2F8fw&X-Amz-Signature=a49a7726a6f9b4c42b7f2f819369fdb89697f3b079dcd2c00b2920d027af7eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQNQOXIC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCWVir0%2FakswoMAL2HItXq5OMTEaB3gH8iwmP%2FgnV4BLAIgOXfxXbKW6QVpr8sLAD%2BOKzpCv13BSR0bPpz%2BVivw%2BZoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDPidjt3L1CXufNCGZSrcA7uI0BVIKcEnRLlTQfkd%2FHdAPJqEjUirc2weNt5H%2FvtzknAisXvor2F1iZKww6IVnW%2FpJiGpQJe5OC3DrYNbzhv2SWKuy%2BFsDFDIc3lNvnM%2FJkhaESAxlgJmetPWzoxihzuqfi%2F16zBW15fz1LLP6tJlpLZkYmFrrCjDo2FVVNLwgS%2B%2F0blosBZHngXqunRBTAVshIzdMhc2tw7HKQZHBHFkvKGbHFD0iDImDwtfqvu3Sakd5JW863GSqZh0ex9z%2BqfUr9zGWMpqjPIXy8ifiAh42juuOIVTWy9dRf%2F00HnMaXhkJPVMA%2FsBnmS7zxCOiJ0bNvHda4hsvedsKAtm9GkLEjvmTa47aKWnj3c6F4cneKFMfLak%2FiQ2YY2MPUPwt9s1l7TlwQARit6lZgMl7emvFMwoO8d1Yi0M92QoYcQIfXz%2BF1YOpSCMdHF68YJCVgcXN8nc6pEarckehk%2FuOjqPkkqmB2u8KdLrYG576VM%2BKxSrmp2SEb6K941pDQpnqARgzO8%2BkUgiZHLpgNOOWP7S7%2B7GmnxEBUtVoS0GutTmYCDCJ6SqFpQ1%2FBmObtWopMTKK5MrygqRZO2wk6x9mwEy0%2F%2B%2BNlRUJujw%2FvguVN0YrWtDeZFJEQfqC6SoMO3Kg70GOqUBymeJaZeJmCoja9tlb%2FMHnlFAbuSX9GKHryBMbWNJys0tzSOY8DPdOuoU%2Fkiiz0a%2B2wetZtEdDh6g6YPalVjUsGeUNbZFxX70JvsdR9qr8%2BkPCz1Q52ODG9g948yT%2BgKE5bK0WUHC18sQzT2O0oyglzkEeJtn%2F%2FDqacvt4OyPKaqCfbVPUYffgkbONtP5B8%2Bxwa%2BEMTA0oePp6l6ErJ%2BnT5hf%2F8fw&X-Amz-Signature=4cbfecea3cb49e2bfa3db8f5bac18ac02574aad413aafad2f4ffe125880bbb3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM4DAPON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIGfgTu54womFzEspTB7Qhf0yw11lL0TkgG7Q1BDHfljuAiEA28BHCpFW8iPZmHcR6A4oLBwQd%2FMilnu%2BoWDyjEr02moq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDBUdYpYR5bnGuTWqcSrcAwdSpqmck97HQZgTMqBO%2BFJabdDlG07C1mD6ZCmJwatZrvjMsJdA6rLzjz935Hb8CIkOPaXn0kOcFUXOVZWojXZqB1VoOp597ZxE%2Be2LxdjfFjnUUS6bJ9zftE8rS6uaKL3VwCZ9P5hBpFWx1doxbo11kKMcmQavSHirDhZhNDJ9rW1OjrP%2Bi5qpWfOEy1EJQvN7%2Fr6YJuJqFMrGg5ziBRoUFga4qP6ir28LuvhsryHuH7fCotBmTChnioBf4rsRXh2iMsbDJdnTzMoinjuIhYC1S0CEUTUDkZl50QU2WQA1a1qT9fRs9DM3eyT%2BL%2Ft9%2F7wl94cty5Jz5m9By%2Bs%2Blp7YgoDQzaAIlAYPDfoIQ3RQi5x5gMY8i6Rm53kjusgzNtT%2FadWQ2KyTOjgFsL4b%2BuM%2BnDQVAJTBqq7Awx75E7Jo3uS8wByefMtFxbCczP4lfNmcSqWBiiAyRB6sA0QNM6hThWm2mbz7zVBBSHrwiKjqCX5GCIo6OJghOklaie8jYFpsifh4LQg307fzrIPAc0%2Ff%2B9%2FOUuqY0RNEmyfI0FBVgqwANVydadXENROB%2BC7q5P4BYMgFNLXW6n9QDgJJ3HG5ysQbwIumckLg0buQt2KMkUu2c7LG8JnMcMdCMNbKg70GOqUBgwnRI5veriHHMEBHjFrFbyGgULiA1cY07r5Ji7JPUokw2kLz0C9IIZC2anpvPEeXBRG0gUovKW%2BZ61JYUdJp6vOBFbpFWMdPcmaKz24zHi8YIEetGP83AsAk%2FLyYTE5GmEUo8A3DBGiAP8oDR39Jyv1i0yadOfKB92hRoTh%2Fgqw1ZUu1Ez1QiFAAvBYtR3nzs23Gcr5hYNnzjmKphisj8%2Fdp7evL&X-Amz-Signature=d9a70fdad7ec5e33309371e3e92608d791b1be539327765bff2e7675ba08e948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C2DOYXA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCIFfftayw%2B1OqKev%2FNiCnpobulCM6z%2BfKIyt8%2F%2BIo459KAiABJe%2FVg47yQtEFzlGsZVGcrNeGEpE6j6X8X8CqT9Bj4yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMVAY%2BA9L5wGhOPjtxKtwDUOho64tiKtO25BET9wvrfSITXb1PSUHHPM5oDiCzFe4gOAC3NK0oGEk0v3a750NOttBdBYSyjqKdqAOfDyeCl%2BPbpsS89yKHzyrNNKnouYhvAoXIMjafsyJMUJIJZ9dTEA5Y7cF2jtLYLMjvOG%2F3ULdjnJN8gsp8YveVrzr%2FJy2b4sZcjONk6f%2FmuDNyqlGamGvYe60wSkhMdQRCSm3GLdevjhvI%2FC%2FKiUq%2Bp%2FI0UnVOi50q1M%2FHqmn8oJbHrZi1evn6IdPK3pQN%2FMKaQIikmKs%2BeVNRk0O%2BRC79LPeflKfoVWll4wSQiHcTTRdZBUnm7WEEeltkS3iSwCfIrr83%2BoWdGcrmreD%2BgLbRpfWiOe0Apzc9E3cgPjKOw3JyhUgU9ndEPK0em32HIb3or3yKiju8WOJdaVTZgFz8RkWi51Bxo5D5ft55xpiQ%2Bv6NL3b2QrM86rK2K7EdmHlkK7JPGHaAOh64Y2dBDmHks7BrI7Po9J7Z%2BN30N%2FULYxSdHaoCZFyvr3kGjktV4MrsE45CJy8iA%2BFEnhUaEGOqHpP6jJbr%2BD71J30mW2p%2FEne2RE2b%2B18JGiJuu12WakdAjG3zLG1Uu2eMiz%2B6gLcCLFOPU5W9rMc%2FaU8ksCRMhb0w0sqDvQY6pgE%2Faiw0FJpZYXLEx%2BU1yQtLxGKcKJ7LZ%2BJwpOUxOxut9Kd7I6HylzW%2F%2BxitssQ4y5kJdCgK4R3RDo%2FiMrFXlK9ndfuQFOH4Ci8ohBEZX%2FsxD69d6CWs0%2B7R1AM8gZva9W3LNUlNwweyIKOkBikyrddNaR2d20OwRZLrMdRZc1wNben7MzUCuz91HtugMzBVM929A7CGRwaJWthKUusOK9SVtX5Iufyw&X-Amz-Signature=f078b752b98ac7a3ea9e495f1cf439cfbeecb38770d10afb2191bcd064f864f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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