

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=12b0935859e42f843df6fb229ac411f0dc1102021d05600b3b8b5f6a2c215900&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=8663d6c7e17e78e5fcd364f243110a05189e40bb5cc9784837c69f28c946b3a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=4fcb022180d41da98c792abd60cd55b0e0e6222720db9219eb88aa89d4a46052&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=8812fb2cac1a03f54cc03825078851db0c06db37139beeba48a6f1c6c550092f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=9f2ea755ea4f4a366e698fee57df4a309710dfef78fbda4fa79a8f0884c84439&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=37cf99ab2aa537f323dc6301a620caaa15416d45af8ffc1fe65bd8f36ce1cef8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=74321f293e75350b8da7a375a70c645c70641874df4911167c96391fd602f6ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=29e203de71d63372eff8499e7ce5a72530caacf5514a3c618fcac90205aa82f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=1ecbffb480e782ce7f9bd9fdef5ff08ecc49d062b2ba3b63b1faebf9c547cd15&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJH6Q3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FB5lduwd0aY7cRFqNJCynrI7p7Gi1PiY9dKQRQVIJGgIgbiVxVr%2FJXQ9I34OQBnnW6o8HLfGRlFr6Yn2DIPBIjjIqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFV9a2iYCA5XMaLjoyrcA4EAFMPDiguTr1MPXnYcsFLPd%2FCILqzlN9fiCHkms%2FCaMFI%2FPu7kojxHKcgsjr%2BCDMRe%2B64bh%2F3Wzfkzv9OHhtEggkxOdtUmIHXbmQGCLG1Gqnv6PNgPi5I6UzNgAFJvZM1BnBc2dCjFJKhRbieH9w5wuLXdDqYKICVHJQ8mIdgyOnKWDZ8GWnA9i%2FKFPOjbuhphtdXMXkwTR7CCbrW%2B%2FiJSbVCdSYfziRkoWomy%2F1Zo6QrwBbEem4w5uoWXf%2Fek9%2F2fuAd4Absl%2FfbYgdIgCRz%2BixT5K9JgIwU1o6KAKupxw70ryisg2D8M7bkLaip35U%2FhBzhEbAlx5djHbo9aaeameOrdyZ8W29btBNRCuzMm7ASc1p%2B0XOBEWU7hoIu9wF8l6JXaBEnQ8MB7R2P0rhz%2FjBHstNHICzlSVdFq62BbTuhmK5IVI73qBAPpoCfXnbLsJB%2FsKG4Y4yOBaaGTxr1DZuxwaB%2F2U%2Bv26RRWpwOVgEWICvF6uoNMxR9XVK5kRgtkuf0EEn47V4uTybq%2FYxbj7ULKi%2B8Z3xsDkRs%2FeZxgHg1SKhvcOt7uOCDLxTshzry%2F0GdHCXjlo%2Fjv2TfC1XZ%2FS%2F6M1cIbQemr0WnRUgLrw%2F1tLX4OlB6MtpJjMOaW67wGOqUBGgE5xh6wQxmgcxMCfImlBsG55hJjdOqq4NC5y12nRJ4xdp%2B7bRbBb8leF1D7T%2F74Q3qJoEAbzIgyxz0ISRuUaQD12G2cayMeC69uzVdZ0xTlSjXrKSiW5lrkX%2Bc5IzOf5KvvkzxgBcV3cKS6%2F03U3nE%2BLAXnP64PUJyP71mHuzcVOtNr3qGlGovo1iWAjXtMjto5q4v17b9J6PdB5IJQGFsiL6nj&X-Amz-Signature=d4062c6d7bc7ad4786513f332b83f3a8ae2280cd731cde5d51649fb3634283ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJH6Q3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FB5lduwd0aY7cRFqNJCynrI7p7Gi1PiY9dKQRQVIJGgIgbiVxVr%2FJXQ9I34OQBnnW6o8HLfGRlFr6Yn2DIPBIjjIqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFV9a2iYCA5XMaLjoyrcA4EAFMPDiguTr1MPXnYcsFLPd%2FCILqzlN9fiCHkms%2FCaMFI%2FPu7kojxHKcgsjr%2BCDMRe%2B64bh%2F3Wzfkzv9OHhtEggkxOdtUmIHXbmQGCLG1Gqnv6PNgPi5I6UzNgAFJvZM1BnBc2dCjFJKhRbieH9w5wuLXdDqYKICVHJQ8mIdgyOnKWDZ8GWnA9i%2FKFPOjbuhphtdXMXkwTR7CCbrW%2B%2FiJSbVCdSYfziRkoWomy%2F1Zo6QrwBbEem4w5uoWXf%2Fek9%2F2fuAd4Absl%2FfbYgdIgCRz%2BixT5K9JgIwU1o6KAKupxw70ryisg2D8M7bkLaip35U%2FhBzhEbAlx5djHbo9aaeameOrdyZ8W29btBNRCuzMm7ASc1p%2B0XOBEWU7hoIu9wF8l6JXaBEnQ8MB7R2P0rhz%2FjBHstNHICzlSVdFq62BbTuhmK5IVI73qBAPpoCfXnbLsJB%2FsKG4Y4yOBaaGTxr1DZuxwaB%2F2U%2Bv26RRWpwOVgEWICvF6uoNMxR9XVK5kRgtkuf0EEn47V4uTybq%2FYxbj7ULKi%2B8Z3xsDkRs%2FeZxgHg1SKhvcOt7uOCDLxTshzry%2F0GdHCXjlo%2Fjv2TfC1XZ%2FS%2F6M1cIbQemr0WnRUgLrw%2F1tLX4OlB6MtpJjMOaW67wGOqUBGgE5xh6wQxmgcxMCfImlBsG55hJjdOqq4NC5y12nRJ4xdp%2B7bRbBb8leF1D7T%2F74Q3qJoEAbzIgyxz0ISRuUaQD12G2cayMeC69uzVdZ0xTlSjXrKSiW5lrkX%2Bc5IzOf5KvvkzxgBcV3cKS6%2F03U3nE%2BLAXnP64PUJyP71mHuzcVOtNr3qGlGovo1iWAjXtMjto5q4v17b9J6PdB5IJQGFsiL6nj&X-Amz-Signature=d040acee72a555ae4eb4da298486795d836689d1fa9ce7925fab130269f8d50c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJH6Q3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FB5lduwd0aY7cRFqNJCynrI7p7Gi1PiY9dKQRQVIJGgIgbiVxVr%2FJXQ9I34OQBnnW6o8HLfGRlFr6Yn2DIPBIjjIqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFV9a2iYCA5XMaLjoyrcA4EAFMPDiguTr1MPXnYcsFLPd%2FCILqzlN9fiCHkms%2FCaMFI%2FPu7kojxHKcgsjr%2BCDMRe%2B64bh%2F3Wzfkzv9OHhtEggkxOdtUmIHXbmQGCLG1Gqnv6PNgPi5I6UzNgAFJvZM1BnBc2dCjFJKhRbieH9w5wuLXdDqYKICVHJQ8mIdgyOnKWDZ8GWnA9i%2FKFPOjbuhphtdXMXkwTR7CCbrW%2B%2FiJSbVCdSYfziRkoWomy%2F1Zo6QrwBbEem4w5uoWXf%2Fek9%2F2fuAd4Absl%2FfbYgdIgCRz%2BixT5K9JgIwU1o6KAKupxw70ryisg2D8M7bkLaip35U%2FhBzhEbAlx5djHbo9aaeameOrdyZ8W29btBNRCuzMm7ASc1p%2B0XOBEWU7hoIu9wF8l6JXaBEnQ8MB7R2P0rhz%2FjBHstNHICzlSVdFq62BbTuhmK5IVI73qBAPpoCfXnbLsJB%2FsKG4Y4yOBaaGTxr1DZuxwaB%2F2U%2Bv26RRWpwOVgEWICvF6uoNMxR9XVK5kRgtkuf0EEn47V4uTybq%2FYxbj7ULKi%2B8Z3xsDkRs%2FeZxgHg1SKhvcOt7uOCDLxTshzry%2F0GdHCXjlo%2Fjv2TfC1XZ%2FS%2F6M1cIbQemr0WnRUgLrw%2F1tLX4OlB6MtpJjMOaW67wGOqUBGgE5xh6wQxmgcxMCfImlBsG55hJjdOqq4NC5y12nRJ4xdp%2B7bRbBb8leF1D7T%2F74Q3qJoEAbzIgyxz0ISRuUaQD12G2cayMeC69uzVdZ0xTlSjXrKSiW5lrkX%2Bc5IzOf5KvvkzxgBcV3cKS6%2F03U3nE%2BLAXnP64PUJyP71mHuzcVOtNr3qGlGovo1iWAjXtMjto5q4v17b9J6PdB5IJQGFsiL6nj&X-Amz-Signature=07f988e3628b30db5899e7600dc7a0987b50c274731a09ec7b006e74202204e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=8cfe510b2228c19cc042933340bd5977b2b2ddaa48874891387c60e13791845b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=2fb46d7960c3d6c394835bf85aa17dd04e6cc21dfe80fbfb74a7c535a21a4f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=e7a01aab49ad4c1c0e1fc58c80dd545b07c16539194f79042b5aba0221bc432f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=119bef9658baedb926cb78f264ad5a35ae2f9beaed9bb7c09a4b6a56da72b8a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=f9abf096e4249d34ed67c22d9af7070dd019969ff6208ed4437e14e3c3e01c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKYJLA6B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4fLHWAg3aqJ8iKhL1M%2BsaXi8ADjVFw%2Buco1ndDdPI3AiB%2BXfnlv2%2BqxQrmLgnY9snkEQ0Q%2BtDDMcS8GZ2CXItn5SqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk0XuT1Mlv9leAk0FKtwDTJuuQ521s4P1ig7%2B2GUVPMP9YB%2F%2B5QeSLo4rbGELWVE5zmcdKVLNOqibLxEjdGg13RaIqvlAfADvHHTuZyegB%2B1H9nm90BXxpOMqHeWBZd042oTzm76zwgC%2F%2BkRVx1XQJgSUvlWVM6fJhFhx8d1f5NtLiDxSNSGO1E8B4HKuhLXhva2oC9F1u4KWF3GlmaZJJA%2BQ%2B6rvcfnClYC9qaD%2FqaeUgle6aHafzHuJMuWfNbSLtmbMDKY9RZBuFwkgTu%2BLYhjnhDE4zj3MgzaQkDQHRsLYOGQIYt24mnxTV%2FI%2Fehhelc35S6Yzb930%2FIQWI7h0zDHSy%2Fbe4zvUY0OqAeN%2FxoQoEnrJ1e%2BDF2Hq8faFCqBm6Xpa5UXlxgKVHjzH0ShUx1O9gF5PXKtAypxe5UvRvn9GKZSyZ9lWTJUKxK%2FJZBgmqVePUvlvqzhDP%2BdsunKZLiFXsAwSRFslUZl4i9iRLi%2FPaULecMfUpYa1TuuDW9dOU53Gla9C5BylQ2NY26fjtspXDwkb8ldHmeV%2FPnKmhmFsGLq0OPZfh8pfzCnfaHKL1qVwiEA%2FmofY6AjyXidiZYkGtPQb0F4HGqG9aGxuz2ZZ5Lk9inP8H7ULG5RIS%2BMOr1jHuFVZHmxACfQwyJbrvAY6pgFr1u9nqCaz54%2Fehp%2FFWATaGZZggMP638c6gUSCkX7Dsffo%2BgBVtC6BxE%2FkWYis05zOyx0fonhmk2L8niyo4aLL%2Fy99IzlIFhkUYCWmLuUEqGMT5TRKfNIVbgAP%2BxfKRNYhAH%2BlLr8Junrv2qdEt6tvanFO9crodGr1D8%2FYRPjgKN%2FtOOiMsFWCyNej5ag%2FAEToJDSISJ%2BVgStgj6DWI9%2F1jwQbV9YW&X-Amz-Signature=25b3899b836c7963e63cad148276d2c61a9a3958ae7f3d83c968a0e8eb60dffa&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663L5LD45N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAW5OVWi32ofWmjB3WWo7j5tbkVvqKcoWLK2tbEeYpiQIhAPABqB9P%2F5rzTQvi%2BFRJEDq7a23O6HWM3s8o1xRcioy7KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFgw%2Bqit%2FZGtKwE%2Foq3AP09qQFA%2FERBvwdZ%2FvnPZJLtfOUch3FH8mBJYEAx4XinbbvUqCqoxX9Z7WUwjDCAsP30ZNZcrhb5hA%2FaYui9%2BeRwa19p934o%2FNb0zpxCDJlRHuQxsYKljPoY0Twvl6htRvL1vqenGK6Dhkz6WKBi4Ij57PUjsUi9liVhLaghAMEyrmNoFjDhqVVgYgPsi%2B2No67AdI5h0EF5E%2Fn9A2b%2FtNaVHZjEKsPuV7Oe6g5IARo%2BiIfSQoV9AKAt2wbCr6R9C3UpFevwAvOrL5nekG5yXK%2Fg28cyV%2BNUGVvHqqpmpK0gooxBoN5D%2FznQCY2VWR9fM8KupCrpQg3eDWQomsDEDMX0NVrRyGXLI3vjClEtDNPs3KGIjEgc7ceDaZCbJus4FLtcnpUU40z7lld0m37ZcDXAMb6N6TvSTa%2FugWW8J6HlOTcA%2B0Ii6AMWRh6d1uTR7PL%2BZDN8SMS4sRiIkKaGvbzlQospUoecamZqzioo5%2BuJUvm25RW5CtjOSYJMrjy7VhZ2pbEX3%2B1ppX1j67mhTvJlzh3BhWYqpucUALOgSnbNemUJcEL%2Bf8RVByTS26g6kt3VqcQc6C0F7WVfRDatXS3Af9M1gqjXdeN7JWw8DeiYEqFNoU55UAzGPN0fDCUl%2Bu8BjqkAVFmT%2Fnh0Rpr2TPVjNNpsY7rjds5K85Oibsli5AwF%2F3GRyk%2FM6BRzrYQ%2BUQp8hWDLCc6wiyMuS%2BT9SCXh%2F28nutc0IB1s4Ldkj4Db4fdbQwXnf9g%2F07xyrVjy1lLksKYqiTkL9cNNBrKZGJUJjLsOwFQocLMUg7pH19Wq4cLbv%2Fqabd9nUZnD1bVjOUrhd3snAEpk%2Bk9PKm9AAbV84X5eP5apM5K&X-Amz-Signature=a7fca8f7971f235ab83e3434297ea0b65cffad2925495bba958f805ad43b1e1d&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663L5LD45N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAW5OVWi32ofWmjB3WWo7j5tbkVvqKcoWLK2tbEeYpiQIhAPABqB9P%2F5rzTQvi%2BFRJEDq7a23O6HWM3s8o1xRcioy7KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFgw%2Bqit%2FZGtKwE%2Foq3AP09qQFA%2FERBvwdZ%2FvnPZJLtfOUch3FH8mBJYEAx4XinbbvUqCqoxX9Z7WUwjDCAsP30ZNZcrhb5hA%2FaYui9%2BeRwa19p934o%2FNb0zpxCDJlRHuQxsYKljPoY0Twvl6htRvL1vqenGK6Dhkz6WKBi4Ij57PUjsUi9liVhLaghAMEyrmNoFjDhqVVgYgPsi%2B2No67AdI5h0EF5E%2Fn9A2b%2FtNaVHZjEKsPuV7Oe6g5IARo%2BiIfSQoV9AKAt2wbCr6R9C3UpFevwAvOrL5nekG5yXK%2Fg28cyV%2BNUGVvHqqpmpK0gooxBoN5D%2FznQCY2VWR9fM8KupCrpQg3eDWQomsDEDMX0NVrRyGXLI3vjClEtDNPs3KGIjEgc7ceDaZCbJus4FLtcnpUU40z7lld0m37ZcDXAMb6N6TvSTa%2FugWW8J6HlOTcA%2B0Ii6AMWRh6d1uTR7PL%2BZDN8SMS4sRiIkKaGvbzlQospUoecamZqzioo5%2BuJUvm25RW5CtjOSYJMrjy7VhZ2pbEX3%2B1ppX1j67mhTvJlzh3BhWYqpucUALOgSnbNemUJcEL%2Bf8RVByTS26g6kt3VqcQc6C0F7WVfRDatXS3Af9M1gqjXdeN7JWw8DeiYEqFNoU55UAzGPN0fDCUl%2Bu8BjqkAVFmT%2Fnh0Rpr2TPVjNNpsY7rjds5K85Oibsli5AwF%2F3GRyk%2FM6BRzrYQ%2BUQp8hWDLCc6wiyMuS%2BT9SCXh%2F28nutc0IB1s4Ldkj4Db4fdbQwXnf9g%2F07xyrVjy1lLksKYqiTkL9cNNBrKZGJUJjLsOwFQocLMUg7pH19Wq4cLbv%2Fqabd9nUZnD1bVjOUrhd3snAEpk%2Bk9PKm9AAbV84X5eP5apM5K&X-Amz-Signature=318293ddceb3ddef4f7cdd909f6cc797a7202cde1d24dbeac5863f2ef956e284&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R3XM3XZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcVKQiLWE7H%2FX8%2BMHRiFncmBxHdV%2FDtROZZPB3riNNrQIgXeYBE3Vic7KaoEg0hQcq1buRQC%2F58VKOj8zgr%2FUGiv4qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOHrc0QJXz2G%2FO0j8SrcAz943qs7cCJ6QhTD7PRt2QlItJ1LeqMBBv8ls%2F4yzuMoMAWepPA%2BMXngn5dPu5rVUF7A6Bz65Rjfu%2B5xgERjn5TpcXOLUseb%2BO5sqTfWAxTTlNf4mteI7WsXm1Z5vOBbcVjF4DOg%2F9SglmlR2KcsPy2Dp5%2B4nh%2FXey2C3M%2Bidl2yd%2BLAAm125qGkTrzaKwfzMktSVXw9xEzgCJRxjv1uV0VYA70Yhr0E3jyyjJaR31S2V%2Fput2nT21813sAV7Fa0o6YiemYQz6oaPSM5vT3mv6tXsqXY%2F5IPE1COM9aLj9C31H3A%2Fx9BOR1zWIq6Qc6Tl1dPXJ8wcG%2FY1jikmVjRRGgOFo2PaOO8laZv6zXIe55x2T%2FwhTSM4ppOyHMdC5rULOBFz%2BfHXTB%2FRkYiOODHWs1uAsVIt3NFntF%2FaXnw%2Bq2gJWwLvwVFbgeZmNFQ82rZYq%2FT6VarybvbK%2BF4%2FMcaoGzv3djOMsz%2BVffwWtwg7smx8PQtKbYrnnQCInkgrlQONGj6p9LzneEIdqux9SaDFTp%2Flm9%2BCdUV%2B0THxCyiKTClTYqwWx6PPN%2B611wFaxeAEhhoekyVpapWnLqA4QJ3P1oYNtbtOToVjd4N%2FgS5HjvN4Y22NMb%2F0s7xy%2BNjMLWW67wGOqUBPbWr9tRXpgE1V1%2BsbUXLHY91x4uuWnjcgyBKjhhq6rHb1%2BvfP5jj%2Fse%2FV%2F8QYmDNlsMxUcMzyDAz7ksgNyg3aBkWRHjfhzlAzh44OPdEKVgzJ%2BHMEPseSTxXas8CbWYUT6fZFxdZCF48wORCx9VI8TkHii0TWzhZBgZfEjQmuH%2B0TLdQj4WGxrmBp7Q5v%2BWKImPb7GenLSd7wdhTp2%2Bovk0niq%2FZ&X-Amz-Signature=4e287d0be428245f8f686d363881cd7a6545423c45882b3567cbf8a85db23304&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXPKD4IX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzOOI8w9tNwTwVXZt0ZuWxCxOUXV3ERQWxB0jEC20cUAiEAp9lEYEMm7KL3t5ztaKj4CpSEbBbnucKVrKC4QZuBy60qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt6mn1DuFi%2Fr25RvyrcA%2B8Dbf2P%2BuOdktbIB8l0w5gkzFAALT886nmfs1hK%2B9pTO3eSaGHZw6YBm3seOHIbbMb%2FyWfRQJ%2FvylqZzRGX1WVxjMrQQJN%2B57JSiD%2FccQLI1fWadqLeZ85NfmIXa%2FGOcYGhgAirl2Uhh8OVsoh4MxHHloJX474uBoXsrXGg%2BH97Xh5ze39%2BbgXedhYvLRuwSmhSKfPq5ys9mA3Wdm22Xz2GFRh08HitF1jD62XLIOXEnh5IuvZbIrKxChKqaLXV7gKxORW2nsN0vIyprr839VCTY7j4Q5yrl3LTy8fWM2f53P9VKWMPMhkiS5PLXzcH79D8k%2BIR%2FcrHIxNP%2F%2B%2FiLc%2FsBePmRrDz2rrLGk6LlSyWe5FcRZar7q7iwGJTvuNUjT3OydylCgavXJDcD0v5WwXoFHr6TfjNgQTkFhq77yLzq7BPEyvMWbZPlspdxzBGY7%2BOAArw9j44ybOzWTTnRTRn84O0qCWZtVoWmZQJA%2FSD3ARfLZB4QA42CVKAFUrrUuyy%2B8cTDBGMY%2FD7KyDc%2FsOvZlzb2I0YGz1e75J2WFphRhF%2BmtAfNK8q1maaZKTqDT5s9hbqkVGnagGFnuNzQFgsVABVWcxWguywoCPqv%2BpDdLG3r86uBjLBPFQaMN2W67wGOqUBhMWeAbWS0h2rhiBWrhqfr5C7d5s7Tzcm96fDMSRPTmh5Uil%2BrfpyocFp%2BTvCMhAgUeSTHHoeVL5JX%2BCyq7EMfHud513VQSBAN4mQM6yOJJzlBPBvyoZMDyIuUi9uMyRmHuMzwgRknsFR9V6Nr651ds2HEUKaG8JYyUmVRVj%2BCaFx%2Fd65Mh84t8N4aWOANEd9f%2FczHoeiiR5rEUceIwCxWYdOZY2O&X-Amz-Signature=fdd96509497a1132846ca9b1ae4e0df0ddde8fdac948cdf819d4364381903a97&X-Amz-SignedHeaders=host&x-id=GetObject)
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