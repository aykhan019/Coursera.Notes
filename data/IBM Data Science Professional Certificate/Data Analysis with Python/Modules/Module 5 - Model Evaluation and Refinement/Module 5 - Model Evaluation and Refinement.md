

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=ebe01647eeddf20e813ae6bceaf80951b24c67cb63df8316898479e50c21afc7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=e1f6b14b30c4b2b368f8e7a723c3a0a52c2dc540ca19bf2c088b05589a32f482&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=f518ff6c1e327db5657986d60efbc701b2f64428a6c151eb230f987bf1e19327&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=cab46eaa17baad0f9df5e7a9692b7f579b258ef8aaf0ba2f7bfdf68daff75d2d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=16770add2b937abab03a0688997b1663bef68a62b719b7f56c0e56c0377484f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=bab610503a1c3c4bdbc4e7508240e86feaeffaa0412681f44e86692fa0908e03&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=29ea5d3ba9e0cd3fe65f8de536777df7abc45ee0a7bd81b22b536ebf6af440ad&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=2689ef3a155545d12cd53e91aeef49bfe14b662d9df664928c24fc37285bd221&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=0bdf6a6fdfbcda8145a50be7eef45c58c462d7ab9dff1b7fa77ee4eacfcde6e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKVNDO2U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDnYlUhISgg4xjYY61XIwv%2FxXR2i5XhmP%2FRcKnVFAkAYQIgFz99SRSb0vN7plP525FKwGqTDSSn8AbQ9QYaoUPPOkEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDLfcbEZZekg00E92DSrcA1ad7LVeg219CU%2BiLOiEbWWdTP57iXY%2FomJ218fiMLl%2FbmGrTV%2FxY18L%2BQgxytbjlsMGPe3lOZXzlOrc9nL9Vz9mCkGR6gXaDBkwkKk4vtCBybnDInF7jJDli3rVOAIklSpbV%2BmBoi%2BYC4Yz6U5ZbZUNKwW9z8aG6K7rMjBEQJPtKqjBrBPKbxesbHdiKvrMpGFszf6TkMAw1lOnoH06WIKYwefw37OZVnHDMxdthxUHl6EFk%2FoHQ%2FHYnDMGy9C%2BzjS0p0gNnn6T%2BH%2Fau1QZQnplm0fcK7YoX%2FnbdTT8LCm9nZ6s%2FYWACR06bIu9yOBg2Wsfh5rlYbM1LLewleJwwVM9pygG7e%2Fa7FOEaHlp6pX2zH2kb7PeXVn7vOJ%2BGJPwiGHLJ%2BB6LTHnakpWLvrgfnldUEYX9QQWLHLW1TYK%2BhOZYVxhmKxD6LLnxNBltOxq8DQuJDqxDoIG29V2U6qX0htAK9ZjnQnHoie97XSBFEwKIas01opXTE1Z0X6DlpTHX1AVoPwKoTitOuS46M1spO0%2FGjPC5%2BZ02WGm0bhAI0w%2FLivLgyxPPwRrOVLkskOsDOKqYdpy5r0nzuO6Y6EEXi%2FWIvYFAClq0ML0MoqRIXRwZv%2BgYUfiJxX0fGlEMPjdi70GOqUB87qHb0BxpFLIpSUQF59mFRDZP0bsBnR5WMHVCgfXoKC2zoY7tW%2FrXxm25MstiE5Yekwscu%2FUB%2BVhsQBxITWngCO4YRvMq5OEBmmks%2F9Q6JLBMqSNTuWtbaXVCe328LMEuwcUkjrPt45GZWLdCrJqGbvzDr2lPJaSDO5tngFRiRPomPkh%2Bl87dilZ4fQMRnQhmG7CiTrtaBkNaouQiReBh30FhuUH&X-Amz-Signature=aff4a3c05e06e64b71a5e3adbbc61924137165a45027171e70784f428fe8dc85&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKVNDO2U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDnYlUhISgg4xjYY61XIwv%2FxXR2i5XhmP%2FRcKnVFAkAYQIgFz99SRSb0vN7plP525FKwGqTDSSn8AbQ9QYaoUPPOkEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDLfcbEZZekg00E92DSrcA1ad7LVeg219CU%2BiLOiEbWWdTP57iXY%2FomJ218fiMLl%2FbmGrTV%2FxY18L%2BQgxytbjlsMGPe3lOZXzlOrc9nL9Vz9mCkGR6gXaDBkwkKk4vtCBybnDInF7jJDli3rVOAIklSpbV%2BmBoi%2BYC4Yz6U5ZbZUNKwW9z8aG6K7rMjBEQJPtKqjBrBPKbxesbHdiKvrMpGFszf6TkMAw1lOnoH06WIKYwefw37OZVnHDMxdthxUHl6EFk%2FoHQ%2FHYnDMGy9C%2BzjS0p0gNnn6T%2BH%2Fau1QZQnplm0fcK7YoX%2FnbdTT8LCm9nZ6s%2FYWACR06bIu9yOBg2Wsfh5rlYbM1LLewleJwwVM9pygG7e%2Fa7FOEaHlp6pX2zH2kb7PeXVn7vOJ%2BGJPwiGHLJ%2BB6LTHnakpWLvrgfnldUEYX9QQWLHLW1TYK%2BhOZYVxhmKxD6LLnxNBltOxq8DQuJDqxDoIG29V2U6qX0htAK9ZjnQnHoie97XSBFEwKIas01opXTE1Z0X6DlpTHX1AVoPwKoTitOuS46M1spO0%2FGjPC5%2BZ02WGm0bhAI0w%2FLivLgyxPPwRrOVLkskOsDOKqYdpy5r0nzuO6Y6EEXi%2FWIvYFAClq0ML0MoqRIXRwZv%2BgYUfiJxX0fGlEMPjdi70GOqUB87qHb0BxpFLIpSUQF59mFRDZP0bsBnR5WMHVCgfXoKC2zoY7tW%2FrXxm25MstiE5Yekwscu%2FUB%2BVhsQBxITWngCO4YRvMq5OEBmmks%2F9Q6JLBMqSNTuWtbaXVCe328LMEuwcUkjrPt45GZWLdCrJqGbvzDr2lPJaSDO5tngFRiRPomPkh%2Bl87dilZ4fQMRnQhmG7CiTrtaBkNaouQiReBh30FhuUH&X-Amz-Signature=5631da564b42891ed03c34e676a9317a30f7a98bb3347edc86c5e16defb44660&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKVNDO2U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDnYlUhISgg4xjYY61XIwv%2FxXR2i5XhmP%2FRcKnVFAkAYQIgFz99SRSb0vN7plP525FKwGqTDSSn8AbQ9QYaoUPPOkEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDLfcbEZZekg00E92DSrcA1ad7LVeg219CU%2BiLOiEbWWdTP57iXY%2FomJ218fiMLl%2FbmGrTV%2FxY18L%2BQgxytbjlsMGPe3lOZXzlOrc9nL9Vz9mCkGR6gXaDBkwkKk4vtCBybnDInF7jJDli3rVOAIklSpbV%2BmBoi%2BYC4Yz6U5ZbZUNKwW9z8aG6K7rMjBEQJPtKqjBrBPKbxesbHdiKvrMpGFszf6TkMAw1lOnoH06WIKYwefw37OZVnHDMxdthxUHl6EFk%2FoHQ%2FHYnDMGy9C%2BzjS0p0gNnn6T%2BH%2Fau1QZQnplm0fcK7YoX%2FnbdTT8LCm9nZ6s%2FYWACR06bIu9yOBg2Wsfh5rlYbM1LLewleJwwVM9pygG7e%2Fa7FOEaHlp6pX2zH2kb7PeXVn7vOJ%2BGJPwiGHLJ%2BB6LTHnakpWLvrgfnldUEYX9QQWLHLW1TYK%2BhOZYVxhmKxD6LLnxNBltOxq8DQuJDqxDoIG29V2U6qX0htAK9ZjnQnHoie97XSBFEwKIas01opXTE1Z0X6DlpTHX1AVoPwKoTitOuS46M1spO0%2FGjPC5%2BZ02WGm0bhAI0w%2FLivLgyxPPwRrOVLkskOsDOKqYdpy5r0nzuO6Y6EEXi%2FWIvYFAClq0ML0MoqRIXRwZv%2BgYUfiJxX0fGlEMPjdi70GOqUB87qHb0BxpFLIpSUQF59mFRDZP0bsBnR5WMHVCgfXoKC2zoY7tW%2FrXxm25MstiE5Yekwscu%2FUB%2BVhsQBxITWngCO4YRvMq5OEBmmks%2F9Q6JLBMqSNTuWtbaXVCe328LMEuwcUkjrPt45GZWLdCrJqGbvzDr2lPJaSDO5tngFRiRPomPkh%2Bl87dilZ4fQMRnQhmG7CiTrtaBkNaouQiReBh30FhuUH&X-Amz-Signature=69764cd4c763f7fb8f6be31012f0b4e1638fd579d2b0c5c99a1ce5ecb84fd8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=9c7fe4e6bc9740b64b30a42c23cc57d4ac0aa8a4e4059eb8ba032f358e8e97b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=b317e855cef953034ac35bb4a9341c01c1ec99706f35360315f0bd80bf27f99c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=88efc2c041d9518525134af3c2c661733fc43a5812f8bb9cb223ce522a715b05&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=eb925c4daf2c030b82058124b368c92848422ba7377dbc99813a78d9e94c8d36&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=4d12b3b39d940bb5f7a602e68e203e1433c9c05056c9f361edbd0c8ff0c33418&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MCIAM62%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIFD86qY2oASOZZXjhrWv6D1fz8%2FGlUXsMBy6joCwPOqlAiAdj%2BXgpmu%2FIf4cj5VhDss94nlq6qbKyCjA9RW61MkLcyr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMmVVxsmpdR0SpcQEEKtwDpGjMMUkjs4RBqyhywOLWesW%2F%2BadLLgUZnoRZ0JQK%2FZ80m2GOb8WgJzv28j44jh4cWed%2B9Ccak1Mpe1q42wnca28OCUSY0g3kai4UIC6GgY3zqXLbvbVDkFbOuBSpbD0rm%2BEGiCce0%2FQi%2BQssFtJXmc6nnb88SJCJsKHSQ2DWNWwFKi9Nvxbu4Z77fZW7eKE85QJv5HHD7FkVRO%2FCu8QurP8YC23DUDnux6Q91ziZf2YcM0ICYNPYuDE2SxFX%2FdGHd7B7KqF1ky5Uz1NjlBBDgiYnZA8pDFEIrOCmXpqrTgST6tcEqX208xI772bvBJibINSCiFOxtk0WHMjzDwKJk1rv%2Ftat1DAxzOd6GOAVIfBQ4CMVxn%2BkW%2B0YinrfOcj73AxD7MqQYszYV9ApOqNv8oXAWqew8vAwhTO99MrmSRHiVtgEh6PevigVuWPsQpSsLjtkde8AL4sYrF4wXXMHiAeou1eRAhRa0I%2FGWIbHFmjOETTxFZ09yGu96eO3LbJxhSSFa953VGgd5lx48X%2FCpeDK5Zria%2FJaqddHsEM%2B5TjZmTcpXNENFPqI2F3zAYnZIA5SPBWxUGhu1Zkv4hbxN%2B4WSYXK6nptBzAtAwsS6nPgS2O0f0wEvhdJDhQw%2Bt2LvQY6pgEiNJfV0Fd3gC8OrcdhtnsP9jR76jdDrIznMXyp7mo8JSJasu4OcVt0oKpTk%2BWQuhv%2F%2FwzlJrfoKILQ1CqV4gGIVnVPpyhKdVQfasE02iMeKiWlO2RGBevED0%2FvoklIL3ZdOftgKQ0C%2BBZIocQHr%2FkLwl0GkOV%2FHWkXPBG2eOyXFi46mmb%2FPHcAfw2S3Ty7aD3Eyo0y%2FSS1374qeOgiaNT37Ocx6uAd&X-Amz-Signature=13daf98f4f3e4f0da92a03592cf7c5a674dfe94f3d4f2faaafc82913caf32965&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEHO3XIU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQC0MFnvm3zKR22oNuzwRsR9jcyjINU%2B94zKXW%2FtPvVUKQIgL5PeX%2BeeliUcmnQhQBtG4YO9K8Tw2lDrySl5Lg%2BOQ9Aq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDMsjxfEkdC1sbnO5eyrcA6c6AByaYgshXTK0FO147Z%2BPfYS%2BHN8Osv3p25tmWkAsQVf2jRIzfHiR4taKcCV4jIdaS8SxURj3bpMbrxlQqM%2BsjQBv2QN4Zxw0vqBZJHJjJxkZOtIv9kibFb%2Bfv9OZaeQuB%2F40JXP8E4MxhBEMgeBPbUI0uXEnlEsieDTcoQ9It8nUWBchGVjWPNBACTwTMeHWOh9eR1v246MZl9SHwEIRIN%2BMI8UzmkYTeR%2FsFKUGqokG2eP5sVHCI9YNCLZ%2FaUrZ7VNn%2FAwjkDlOT4RgCu30ExhEqKsg1OwL8AgHhqV1Vh3lSLEh2NhifawPL%2FoOvQXhxzJk7iNhhRv3LU5UuK28Cwev9l4FgH4abK9%2BaTU3H8%2FbyUQ3%2ByavG0SOy8qgVIbHrrotb2U%2F4WVpZwhSVI3EQu%2Bz%2B6lPkbsUuQRPYk5uISEFU8li1P1QPNEN%2B29gp12JGQjcPlgHGJkEYdjS4%2BJrXqBvUPK9KqbijdLSYLb92DPwzQJG6wGf2pmUv8gkAgV4PKnM6HEDAIalJ95mYemGYprF3mH7R5ICunRprKc77VLxHfkTQtQR06vBJgpNS9OlZVdVqB4Pgj4EGdUT3HVMRH2IDdkQN3G3Lj184ku1EW54hy%2BsK192A9zbMOLdi70GOqUBlC3wL7TJWBcv7HaXtGPA2eQmRZ3agiTAZOfhRLCuZ4uMb9tBwiw8lIh1sAjcJlaRzsnd9e6MQHdlHeF58kJGmMFvv9sClobstxajNXl6poVHh1BLwnV57w9Nqejmcz9XGWgdcBTbyClVoUEqhiG0UvjF2o0Qb%2FD5pZ1uHWAL5GRhFcMVaeB%2FihUSuWCd1P89iinvYgrrBL2BlnUbnLYk2MCKgO1K&X-Amz-Signature=8620daf5bc0121c8128e63052eb1660b0ed42a81bf75adeabc8bc8735d8566d3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEHO3XIU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQC0MFnvm3zKR22oNuzwRsR9jcyjINU%2B94zKXW%2FtPvVUKQIgL5PeX%2BeeliUcmnQhQBtG4YO9K8Tw2lDrySl5Lg%2BOQ9Aq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDMsjxfEkdC1sbnO5eyrcA6c6AByaYgshXTK0FO147Z%2BPfYS%2BHN8Osv3p25tmWkAsQVf2jRIzfHiR4taKcCV4jIdaS8SxURj3bpMbrxlQqM%2BsjQBv2QN4Zxw0vqBZJHJjJxkZOtIv9kibFb%2Bfv9OZaeQuB%2F40JXP8E4MxhBEMgeBPbUI0uXEnlEsieDTcoQ9It8nUWBchGVjWPNBACTwTMeHWOh9eR1v246MZl9SHwEIRIN%2BMI8UzmkYTeR%2FsFKUGqokG2eP5sVHCI9YNCLZ%2FaUrZ7VNn%2FAwjkDlOT4RgCu30ExhEqKsg1OwL8AgHhqV1Vh3lSLEh2NhifawPL%2FoOvQXhxzJk7iNhhRv3LU5UuK28Cwev9l4FgH4abK9%2BaTU3H8%2FbyUQ3%2ByavG0SOy8qgVIbHrrotb2U%2F4WVpZwhSVI3EQu%2Bz%2B6lPkbsUuQRPYk5uISEFU8li1P1QPNEN%2B29gp12JGQjcPlgHGJkEYdjS4%2BJrXqBvUPK9KqbijdLSYLb92DPwzQJG6wGf2pmUv8gkAgV4PKnM6HEDAIalJ95mYemGYprF3mH7R5ICunRprKc77VLxHfkTQtQR06vBJgpNS9OlZVdVqB4Pgj4EGdUT3HVMRH2IDdkQN3G3Lj184ku1EW54hy%2BsK192A9zbMOLdi70GOqUBlC3wL7TJWBcv7HaXtGPA2eQmRZ3agiTAZOfhRLCuZ4uMb9tBwiw8lIh1sAjcJlaRzsnd9e6MQHdlHeF58kJGmMFvv9sClobstxajNXl6poVHh1BLwnV57w9Nqejmcz9XGWgdcBTbyClVoUEqhiG0UvjF2o0Qb%2FD5pZ1uHWAL5GRhFcMVaeB%2FihUSuWCd1P89iinvYgrrBL2BlnUbnLYk2MCKgO1K&X-Amz-Signature=4c93951d38d6d7b0776664ba8f0a8a75290f661199c1cabde5999bf34ea8b02e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZY4O6X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCQyxMmEVWCwC6Z%2FfPdEDHp3JvOGf6VgWGUK3hl1szzOwIgPQQzOp83isqc2MmiHXGVgtRuA80fRv3Y6kqnLCGc8csq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDFA2a0jcLkzWp%2BPrOyrcA9owyHQ7b5wvxOss7cD9cUqdAweCDTR%2FcLbfodEHCE%2ByoGev%2BMVEDvcNR2C4MEBs%2FXGYF8h7WJ75JocViXf237lsWElJ%2BsKZVVuu4s2CpGdDsofN8yw%2Fy1v4sY1gI3IEcGYewj9AJ5jabxYpit0oehantMERF7gBMJsQ3cTOLUtgTiWuv2kRgiqSe5JYsa51RwEQ5fL9uBujIMFPZr6PB2GRuV3aPU5nC%2FjJUBNiy%2FZVW5%2FouZBtNN8Bh3mbl0cy9%2BS3PDiXTLdRGwEBR%2FMR5pFK7WXpCSTsdRNFyt2Ei%2FOkJXsb3tyGGHJ6orC%2FCfL%2FU9YksWj3%2BYrCNjV9WCV%2F5s5YErM8d8KIYYouLxq%2FiEJjMGbTHuMHSaQoI1w4q3rbtOomZX0zX8gSMzDbscX2hS6AA6rtMeinpVSh6FVM3djfToQ6KWoRqK5IA6%2FPzClD4wUeCFdkylhc09MDoQQt3fEaZNpVry2guNo4tk%2Bd6JFtN%2BuqFldp2Vb50R%2FDYqkgHVbKonkGlYmTKr2sQHE6mTvlbIyDI65b9Gci0Dj8q2xZQPeMBbb4ESDU%2FfXuVaRjXTGzPhJHCCIvpMcElF%2FvIWV2ccjn5hWuALa21Wr5mHG3emK%2FqU2hVggZm%2B62MLvdi70GOqUBe5kq2ShZ1Jiguj%2FGl2GkHmlhfTVqnP6JfKA7LjjUoSQ3fgeVgG%2F0Fhvzdxc%2FMA72MAUAjXy0Wau28QB%2B38cejPiWrlNxnhy1JoRxScxxUEPR3VlmQa1%2F4tmPAaXuZUJV1HZXq5D6aJ3%2BvrnFzcSV9Pe6j3WGbNB8ksSl%2BhYOE2YQC39ArH%2F1Jm8UDQaacl9CbjRgCLltsT3blEJ%2FfQTh%2FkaulBjC&X-Amz-Signature=0458305ac304cca2b970b41a902d3ce57f81ab1640ca94bbe0905b5d880e1822&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFBQFE43%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAQBG0UdQvM0GG3%2FCgiaNOjbTO1Kynsl2kzI3BejUeWIAiAtsH5R72%2BXcJwnaFfTew15y8woYIy0dEy%2BOE6VtvLYIir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMnzEUSTZj237u%2BpLMKtwDlUN7xxdK1vomQP9%2B52bSLGJiQewFQqnpvCa89JjUNv1H%2BbkbMdsoPbi4cdD5nyHLDsTIZiezYhIPBkf07YZDS1GhhblEMmpgNuwxYIqmqkmp0wM1AjSRrOOK9%2FTzT1gFKcyuM8E0ZNqHly7ZQC2h%2F%2BDMqPFT2brOc3SUtkh%2BFhOOg85PEiRjJSFnCRVuJQShXStJGGr5tXhYVIA2JbGLv7qvetxWlfj0jkSGo%2B9aDpnaZu2P%2BzejRM229quWnJETY7yE9MdZqCEQ8GUTSEnla6XrDGGqFx%2FD%2FxHRiHg3sy2eVn%2BVa3xA5V9%2Fr%2FJz%2BmGOwKLLYgxtZ9dqCsJwtEgCfqly9JypENettB8dzOdxa3FiWLaa1Iwsmzs0BEUv2qKoQENEccxSYFy7Zy4rZfQdYvnmKH5RrgV3S1U7jJe%2FVkutzv4bJ17B9jYj2DED3fu5GcWoNBFt7UgRdismf75ETn%2BvDKau1tDoSQAIEv%2B6IDu8yN4yutC507HGLjNb1rNqee1VNCPfgxj97WjalnQtGV%2FLP9BAihQMWXillDgt%2FlvmF3114V%2BkI3Hzti6xEKsxuNK9MTJJL5N8bH26hpXYqa5%2Fs9l8YnOqblIi8u9rSby4ywVG2McMjOAl9r0wxN2LvQY6pgFO3vTeSfkaZ9q8iAwXawwtjEfHsRORdfIJz03jeJfbiE1aKiHRvRV2cxUAV3crNFWASyhPTU8WjOrrXAdj5s1F56CGSQtauFnutqL2zK%2Fq%2F0y7%2BTSReosz71IpUKv%2FN5bsPSrzojfFE39zbvpsDTIfJRf2tpo7EaNN9toHp3vDyOqyM6gO9yjZfrAiRoII7%2FfwzwsJxM3lh8mcMVyHix1hTDIBf64C&X-Amz-Signature=8a1fc1e5edcfd2b698c705522522518f922c68a3bfb5da1e34729f4d7333f457&X-Amz-SignedHeaders=host&x-id=GetObject)
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