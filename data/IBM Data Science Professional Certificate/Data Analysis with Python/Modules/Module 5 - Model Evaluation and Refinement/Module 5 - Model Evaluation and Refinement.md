

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=57d6167d927f979f50f377428a9ed62bdd6faf183713a836d4596ac19fa27394&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=cb768ad7dbf8a6e6675d30b44e1008e2e352cc67ad7d3d107babd33a1c185f12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=51e70cbd89fc34390e6273e652f7d01b1c2ff7ae2c2716628866269c9c644b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=4d3805dd8e71bbfd363d85c6b85cea6488d21c512bda1e1904ebbdffe1908069&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=9369bbb8c8cf11c3115915e9c448ab385a58e923486a8e129b515b658a21403f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=628a4587af3381ab8df0f0ab9158ed36500f90db62242ed006b6b199eac9b7fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=eead44c1e37fabb8ceb8cd2187ffa2a0166899a21ae8c8671bfdf9301131f7a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=61c7e184f26aea0a6a9da3d481f42cad9d5c638d1fa4c1e31eb9818abbd0992a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=313f808e91c9dcb06ba8c973c362aad66c8f195e4d8cec06068fb5906279e307&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCXHEOC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7fa9XJp2bwwaKz43OkTW2eND3ccbw1Vzy3VSVF%2BhSjgIhAKwuG6cPwjGa4Fy5vV90Cs7bJkH%2BIyIbj3H1pLUAnNZTKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbbTrUDTe0UygSOrEq3AOzdcIHHMtNvoeKBwhHfYDQUpsKzTIpRHiH76trR2JAYTeoz8mT%2F96URzqrwf68JLVSuCwbXfYVDwWFE9ZQXWSypXzSy5xowAwDXKIFUsKHXNPyWmLcMkFnrdT6pg%2B3E0bOEqd6vsgr0%2F2FezLxSQyPLbdvB1kS8CtkH1ys0s3CmpSOrOwTLSrMbDQQUpDICHIpGCav5Q11LWCGGcFnk0bXY8%2BHqTbPS%2BK%2B%2B52v12YjlM14sDIGPu8QpjPHotRx2AmjEmWib%2BU3xfbUEWlrb9juIiKefHmv06wb%2BnJhIT5MdzE%2FJfaY3lovla3fgM5eWO0FaHwtaPzM%2Fk7Y7laalkxxJRr1CbmF66YEL7ErNDk7owo12UzAUkzOezlFxk2av3uzvlX7g%2FSbmsQowoKXPOp5PWY98wvrXxFHqQC9YQYCkufvsoz060%2F3UkRNZvysn6ovyrZw1wwBI2q5LCtT%2F%2B25utOYAIP%2BMJRLOk9hThIyXUARz2q7SZsdvNt1RUBW1r9M9pGdgvhVke873fBQuNLlB%2F12lC%2FQxGjYIHZUsduldXVR%2BG2Yvbjb1GEJ%2BDJNzJ8C6OsBsEbGYLUVs8r8S4lkH0rg%2BW3qkdDrg6fIDTJ2ikQYQCM%2BO5oKK9zZnTCIyPi8BjqkASIxCWDcKcO6CVDI1LV6CNk8asjE5FF%2FzbKm2pnjeFOMEfbLsE8cljqs9kDeYgvQzy4y2bG8PxawEpI0GXu5Dn%2B5gSJHk6%2FtSXjylXRKICWbR39NTpQWGi1TSvgQ8yo7Ap5ZcDdsaorYgIX0qkkrzvYFP6GJGZZmTs6ZEP%2Fik7KHvU1fpFzX9pKtBOX9zBhMmdou%2FkXddby4L2dCttVzSSIr4GmC&X-Amz-Signature=02b02ca8e28c25987d2f993438e49948070bada5cb8ab309302984661983ef0b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCXHEOC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7fa9XJp2bwwaKz43OkTW2eND3ccbw1Vzy3VSVF%2BhSjgIhAKwuG6cPwjGa4Fy5vV90Cs7bJkH%2BIyIbj3H1pLUAnNZTKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbbTrUDTe0UygSOrEq3AOzdcIHHMtNvoeKBwhHfYDQUpsKzTIpRHiH76trR2JAYTeoz8mT%2F96URzqrwf68JLVSuCwbXfYVDwWFE9ZQXWSypXzSy5xowAwDXKIFUsKHXNPyWmLcMkFnrdT6pg%2B3E0bOEqd6vsgr0%2F2FezLxSQyPLbdvB1kS8CtkH1ys0s3CmpSOrOwTLSrMbDQQUpDICHIpGCav5Q11LWCGGcFnk0bXY8%2BHqTbPS%2BK%2B%2B52v12YjlM14sDIGPu8QpjPHotRx2AmjEmWib%2BU3xfbUEWlrb9juIiKefHmv06wb%2BnJhIT5MdzE%2FJfaY3lovla3fgM5eWO0FaHwtaPzM%2Fk7Y7laalkxxJRr1CbmF66YEL7ErNDk7owo12UzAUkzOezlFxk2av3uzvlX7g%2FSbmsQowoKXPOp5PWY98wvrXxFHqQC9YQYCkufvsoz060%2F3UkRNZvysn6ovyrZw1wwBI2q5LCtT%2F%2B25utOYAIP%2BMJRLOk9hThIyXUARz2q7SZsdvNt1RUBW1r9M9pGdgvhVke873fBQuNLlB%2F12lC%2FQxGjYIHZUsduldXVR%2BG2Yvbjb1GEJ%2BDJNzJ8C6OsBsEbGYLUVs8r8S4lkH0rg%2BW3qkdDrg6fIDTJ2ikQYQCM%2BO5oKK9zZnTCIyPi8BjqkASIxCWDcKcO6CVDI1LV6CNk8asjE5FF%2FzbKm2pnjeFOMEfbLsE8cljqs9kDeYgvQzy4y2bG8PxawEpI0GXu5Dn%2B5gSJHk6%2FtSXjylXRKICWbR39NTpQWGi1TSvgQ8yo7Ap5ZcDdsaorYgIX0qkkrzvYFP6GJGZZmTs6ZEP%2Fik7KHvU1fpFzX9pKtBOX9zBhMmdou%2FkXddby4L2dCttVzSSIr4GmC&X-Amz-Signature=4aff9e8e46b6aa8e85b635c941d2bd9248177e9ad5c61d36ce6cea22b52243bc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZCXHEOC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7fa9XJp2bwwaKz43OkTW2eND3ccbw1Vzy3VSVF%2BhSjgIhAKwuG6cPwjGa4Fy5vV90Cs7bJkH%2BIyIbj3H1pLUAnNZTKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbbTrUDTe0UygSOrEq3AOzdcIHHMtNvoeKBwhHfYDQUpsKzTIpRHiH76trR2JAYTeoz8mT%2F96URzqrwf68JLVSuCwbXfYVDwWFE9ZQXWSypXzSy5xowAwDXKIFUsKHXNPyWmLcMkFnrdT6pg%2B3E0bOEqd6vsgr0%2F2FezLxSQyPLbdvB1kS8CtkH1ys0s3CmpSOrOwTLSrMbDQQUpDICHIpGCav5Q11LWCGGcFnk0bXY8%2BHqTbPS%2BK%2B%2B52v12YjlM14sDIGPu8QpjPHotRx2AmjEmWib%2BU3xfbUEWlrb9juIiKefHmv06wb%2BnJhIT5MdzE%2FJfaY3lovla3fgM5eWO0FaHwtaPzM%2Fk7Y7laalkxxJRr1CbmF66YEL7ErNDk7owo12UzAUkzOezlFxk2av3uzvlX7g%2FSbmsQowoKXPOp5PWY98wvrXxFHqQC9YQYCkufvsoz060%2F3UkRNZvysn6ovyrZw1wwBI2q5LCtT%2F%2B25utOYAIP%2BMJRLOk9hThIyXUARz2q7SZsdvNt1RUBW1r9M9pGdgvhVke873fBQuNLlB%2F12lC%2FQxGjYIHZUsduldXVR%2BG2Yvbjb1GEJ%2BDJNzJ8C6OsBsEbGYLUVs8r8S4lkH0rg%2BW3qkdDrg6fIDTJ2ikQYQCM%2BO5oKK9zZnTCIyPi8BjqkASIxCWDcKcO6CVDI1LV6CNk8asjE5FF%2FzbKm2pnjeFOMEfbLsE8cljqs9kDeYgvQzy4y2bG8PxawEpI0GXu5Dn%2B5gSJHk6%2FtSXjylXRKICWbR39NTpQWGi1TSvgQ8yo7Ap5ZcDdsaorYgIX0qkkrzvYFP6GJGZZmTs6ZEP%2Fik7KHvU1fpFzX9pKtBOX9zBhMmdou%2FkXddby4L2dCttVzSSIr4GmC&X-Amz-Signature=5df5cafc3c4801aec1a8c9ce7502b8832736386b68e4aa3193bc2925642e82a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=d4522725a56f0c420732263e5bb0693b61a24a8d5ca18d6f05dc9e5993c06993&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=40ca865606378c2c128c2992475c8890ee998dcaa38d25876ea02144ec643b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=5fa1125d6f16565de67b54d089e87d2170e1621c8af55d045da2646306a0981a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=3b60362ad7c916e1df5c2cf154a088cc790144aa673e23173cf454bb79bcfee1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=682615e233dc07c97f9334c65879adde68f8bfc62e0f5a777fec4770414a94b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NMJTEIL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9kzjRe25RfGbsRA1cP0R3G95nNrZNHe9Czg87deGIMAIhAPTTlrF60%2FBqW80xGd5eFVwsMCdxK0yXyuhN9rdcjtutKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4NDYgOU6LOACJuIkq3AN%2FXdb7nlbhxYD%2FHiFEU5B713UyUqG7ieIM%2F9iYN4nh17eqNqXtW6pCq32jlrEZ4cDxDl44wzGvHEYV3OMOMXMcgGFlhNZX8s1%2BpXZipxxoNuAbo7a0N2y%2F1dtW73UQYzs7C8VfcTKcqqVc1CMmjjvHZ87HcH9%2F3bF0bln7N0cIIbzYdwwOIkNTRAXmY9XUfLZHnZ6cX%2FhlTfxkoGs00mBG37oSEChCt5VsDHXq9zUFAA9MxBoiUJxmNphpmQXcHrLIwmAIC1kyn6qzsILU6lijRIOIFpMutxIcUPhEjUdY2UCWhO3QNBJZIwHwKLRegV%2BnZgK%2BumajyaTFXbSX3JHlb4MR8o0qHoiVt3b6co2i7AzcPxzFh%2BsOBzi%2FgMIDgfCh07WTrjaVRJOYnJD%2BD39F%2FPB5UiH7g5dCUTfFONhlx3UaBtHsGJcH%2FdTpVYPxyN8atuLw0redA%2BpRd3ac8CSC5ZDPl%2BoAhaZuYxDJURrvqIX1NHqZmk2%2FyYiL6qHIYVpWnTQlPI1rDjrLuYNX1bjwxGvSy42tX79K2N2%2FSsKUaXXVfNRWD5T%2Fh3m2ON2eKD9m7Y64u0gqhwyfHPGplUaDaEwVHWkcdERg0DgXwXYWhLPMdaIJURIAsRQzfjC7x%2Fi8BjqkAb4KWyGeOuwc8RBgWkdkf8DqysRzZPAXI%2BQCaYuK0nbQAnIro%2FA4fB0Z9Qxn66iHFZABiTurAqTzy1VTz58iKFIKFfwLU5yFSKxV%2BlOrK9Y%2FdKlHcUPe54x7lP5Xb9%2BB%2BKClzetGYim5fAcH9xh0viT3%2BYn7xtr56FI7dLKjau1P0Ni%2Fwfena%2FOXEU3TBL5YkTjRGC%2BMmrPVtropns2D6dePGfaV&X-Amz-Signature=7980a5a1f68ab07f0521cc841068f04ee10eeddc052eccb5e24b7029825c827b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636F3UPB7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuHmt%2BF8mHephpHehXMqoWoTOX0%2Bz2exDY9ykmekx%2BeQIgBDDlhTLvXRyUabmLMAJtcjv8bbe5BX4tT8Y2c%2F1pQioqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKWukwNmu3GEN54loSrcA4bMPCk6Qx5gGOcRJMdt9SzbeJ%2FLLKAOwN92gSB%2FdTUnk9IEH8IEQuP4hs2Fs9tnw9P4kksfL1%2BKCE9QjYkxaK7bDYJYAyobtq7mk1pJhQnQD1hi3SnONjpg37bGw%2FeAHUudUt%2Fo6P1OC3QRvi793sdiUGr3ewVclzEkM3ORwPHuZiTlW7NvUhWWYFeKeXQO0efUkT9PAkZ0Hq5kMnCxLAziJWYiRz1v%2BbVhs4xc2UqRuV2nYrs0tF%2FJ5VWUaRSmZpw2cQjsHcqcKM8TFXX6Abvg6d4%2BQkiYejLhWyE8yOQB85n%2FluLoqha9alHMvzv0am%2FtFeRN0YGD6%2F5EC4Erzz%2BCsN6bMMbHdMb0Tb2T0%2B%2FxqAjH031B7%2Bar44btBeVvwc%2BDBuMwfEYms%2BUQZzpi8qw2k3d48QWJEAXuamS6zRb9%2BlEI%2FRt1q%2FsuqF6IDzkxFeB0C%2FtALYm4ggFWKd%2BcON9SdJ1Ur9hmW0gslsEgEMCYxDqHh9%2FOpua22%2Bs1YjeF%2BR1wkskofutc4AEKukcwvuFElAnAwRlSHvOAATSo33Dm7cLDmaGqEWQDetoDe6Cs6Q6%2B8uPKtCZS3V4SFWib%2FQXGeI9GNF7%2FEAe5sCpeHEdszB%2Bx1Z0yJCrLBtyNMLrL%2BLwGOqUB0k3VznSIuAaAgIM1tFoxwaZH9zCNwgUOSrtda0yz4bEzJqlwOdYKGpzGaHhdTdMGrkObX3zq0qSutoO0t0ud4nM2CE0Z6GfhLWuyepUqiWmktgmFMr9PLAqj4NgECLRhZ6BXarYxUB0sMAnaPe3iqNScQ4AGAp1Sf1G631LW9TfwL%2Fikrjwbcwx6mdxzVNE1pXM2aMXxcUVCLDEhlU1VuI8go7gP&X-Amz-Signature=d37a87e72c34f30e97cf6de2266d82852ab511dde819c4446f60c05b65365a94&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636F3UPB7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuHmt%2BF8mHephpHehXMqoWoTOX0%2Bz2exDY9ykmekx%2BeQIgBDDlhTLvXRyUabmLMAJtcjv8bbe5BX4tT8Y2c%2F1pQioqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKWukwNmu3GEN54loSrcA4bMPCk6Qx5gGOcRJMdt9SzbeJ%2FLLKAOwN92gSB%2FdTUnk9IEH8IEQuP4hs2Fs9tnw9P4kksfL1%2BKCE9QjYkxaK7bDYJYAyobtq7mk1pJhQnQD1hi3SnONjpg37bGw%2FeAHUudUt%2Fo6P1OC3QRvi793sdiUGr3ewVclzEkM3ORwPHuZiTlW7NvUhWWYFeKeXQO0efUkT9PAkZ0Hq5kMnCxLAziJWYiRz1v%2BbVhs4xc2UqRuV2nYrs0tF%2FJ5VWUaRSmZpw2cQjsHcqcKM8TFXX6Abvg6d4%2BQkiYejLhWyE8yOQB85n%2FluLoqha9alHMvzv0am%2FtFeRN0YGD6%2F5EC4Erzz%2BCsN6bMMbHdMb0Tb2T0%2B%2FxqAjH031B7%2Bar44btBeVvwc%2BDBuMwfEYms%2BUQZzpi8qw2k3d48QWJEAXuamS6zRb9%2BlEI%2FRt1q%2FsuqF6IDzkxFeB0C%2FtALYm4ggFWKd%2BcON9SdJ1Ur9hmW0gslsEgEMCYxDqHh9%2FOpua22%2Bs1YjeF%2BR1wkskofutc4AEKukcwvuFElAnAwRlSHvOAATSo33Dm7cLDmaGqEWQDetoDe6Cs6Q6%2B8uPKtCZS3V4SFWib%2FQXGeI9GNF7%2FEAe5sCpeHEdszB%2Bx1Z0yJCrLBtyNMLrL%2BLwGOqUB0k3VznSIuAaAgIM1tFoxwaZH9zCNwgUOSrtda0yz4bEzJqlwOdYKGpzGaHhdTdMGrkObX3zq0qSutoO0t0ud4nM2CE0Z6GfhLWuyepUqiWmktgmFMr9PLAqj4NgECLRhZ6BXarYxUB0sMAnaPe3iqNScQ4AGAp1Sf1G631LW9TfwL%2Fikrjwbcwx6mdxzVNE1pXM2aMXxcUVCLDEhlU1VuI8go7gP&X-Amz-Signature=8441779962bc521f0b746beb9f70c49c27800867ee2f08508dae223deb660e55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STPV5WID%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEr3vLFuKU9h4SHNu8C%2Flly%2FFKz8TEBnsJk6F51kwojmAiAOhwthXEkSv7m7uTwTkR%2BnPwUC5MiLQps6SuWcCJgj1iqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtgfSPy7h%2FglvwIfVKtwDWcGGlKoE0%2BOOemdhzy7jKncAE4h9sWhJhB87yijV64JBNEuRUXQh786ffv3R2L8JWDxATSYjviSbLOXkwogDvT9ajaU7DOtjDodYeVVa8BKF%2FxluaRzlRjjsxKECr6JuDSsZQzebk09GaChnnSrEkPrBiVX%2F6J8LEwdmv27%2BAmE8HZEZW%2F0zCPgOcQs91cbFBFeKnJZ0gNuXF%2FqW0CxZV4X5MTYi1TeRpd3dFa9M0zFs8DQfcaekRRjYVpLxWJ8XZp4MSXaNZW9mlaNDoLF5qS%2F%2Bv6%2BPUzmKolJTRoS2hhMbZnqF%2B1QneSHGxckLyYCs5FcA41jW5ppLB7OlzvuTdwwESA2QQQUn5dwvuaOxoKb9bkhJwKOQ8flPHKxRj%2BULk%2FPibjcuazaZMUBSPQOwbr8Ket8YtN2HgmrU%2F4eGzpU1JoFrT5y%2Fot9OavTEhF5cJ96DKyWJeJfx5LdMUaw0XlN8GRm5O63wT6B1jmo8G%2FmllkdKMK1F8%2FzU%2FCLkRoCelYZj39vBTJj7hBSw0xK7gutjDLMD%2BmbcjhDrs5mJ%2BgI2OUlVMCyR3RWMXBdvjfgzJV%2FzueGUyN5jWbfUWugbyEr5jiu%2F8v9pXLD0y2TQKQ%2Fz7b9AihM%2FRX6QwtswnMb4vAY6pgGadUTkOdH%2B78F4eA99Pfim9vGdexmxCV81nKCkHSTJ0JwEmuA1OwYcYyDCCJ71M77ta2Rg3Dsa5nM9QtBwrz8Uc6PPXsx6323WzA8JpyKGx8xmvuSGaaFt2xZurvYsnlOowxnFCil%2FBrvZfTYxyfms3ZnGBIYRMiPEXbYqB9NNeGOM%2BuPbi%2FmZQX9DD2kA0ecEVjpRMjRJhNv%2FYqnLx%2BCa%2FJfEEdaQ&X-Amz-Signature=bd14206c3fe261e4254bd74d442ff8b74ee02d983565cab40e92e741945ed33f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTIHZHV3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFw%2FHQ8z7x0atOPFP8uBcUfegwyoRHrkZGFXTWSBy8scAiEA44TIiP0TIl9mKqK9PQzlF3mwn7bZs2zgphTzt1IkYJoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdYYNqJzNgsKhAtTyrcA%2FgmvUZN4E1b9SQd0E0EdGCnsmG2FLbYQD%2FlOfMaFhxMlBVfdlnRc8fammcViJ3i76ie3vqNPp0gFtksjmKScYRAxcoY%2BT%2FqCv9nVX%2B5fnv%2FQ%2BwagPVdiD2lobx15E0zvTdRV8bGht2WnPrp1B0LFzyJKWQVBlpv1vCU1KlG2IaX0lKq%2Fntt1fAFetSzsn8eGp1WVZ3G8gt5w6OwfBmY5Amzkt9vIXhXA0Nlwy89lxN4c%2FyH6mdBDGb8LwJ21m4yqA9nkOpeudLCrIn%2BrJ2nwAJFkI5qdQaUPzqEZTi5DIHWBIbWDJx9RQ9LaFk%2FPd%2F4qlzXsec96XUohvCHQEqVlJILOT7ZY407FxpC48nsNn3fTwmxBYlrQJiuLvV0F01c8NU%2FWqRZbXIpgBsjFwBoQ91JD%2FqE7Rew%2BURPn3uz4vdz7K6Jtts4XEg%2FEWqtXwZjDay2AWQbJT6jnFVb79p2Y6X%2BX0Xv15Q3LElPc8UUspP0sBuDYuyTt7onSphUPcyIfiOcFhpyTaxLOynO79OyB3R0BGL7LC5utkmlq4YynZpwotkQ7DZLJCv8qC8KN%2BxVfromlKA89KTUfGki6H6Qdhw9kukdPQNhQZB1o3bvHyW4QeWWIia9cgsP7MC%2FMMnB%2BLwGOqUBjtaFp4daSTG4sodMmvixRCp8kDVQzJZdLi2qgAC%2Fy6xT6W0KMXY5BfLC6%2Fqjpif3Jm0u7%2FLyoDWIiYPzKSRTHAMpykAbWth1jr9qHc2NLzxKOMZBrlBAalyO%2BM5QGxii4kmpplCCjVx1MX0hUrRgsxI16F4Z5IVAqrbaYPr6pXhEk85Gkr8qLY5f3EdWSKuS501XEJ72j4sZh%2FraiI0mc%2FW1bAxe&X-Amz-Signature=d4b27583dee0fd31384aeb10d4b9501304b1f36656ba670e78e0e77bd55085ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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