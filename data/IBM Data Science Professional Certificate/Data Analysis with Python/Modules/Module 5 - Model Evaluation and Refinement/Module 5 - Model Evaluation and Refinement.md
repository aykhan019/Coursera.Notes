

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=f5003c8947e085e141dbc4cb302bce62c135efade0354ebe3d7e538cbbd64742&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=b06b80e4badf30954eccbdf29b2da5d6a96671c7b234e7331f6b48c0d1cf6d26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=1b22f6fcabf41e4476609095027344d7be4700b7d209b3c220c8f7a378fba91e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=bc35b773a459fac540ab205e9a588ac9b35bbb000fef961896f8a5b9aa34d842&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=b46b5074bcf63db4c1880a22c45123fb75334e60b870838aa2b1b9d62cd1a8bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=f503b7eb5be76ef2221c7305e15b389492f2fb2e91a8ed809a60ae4c163db0d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=9459df3eea8b1a0b360c53416346965ba2e6ea6118ff987adee6f082dd2eb4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=750bcae64c99224281a7e824f21b468d260ba5322d068064d56c1e7fb22b2773&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=28de83d65ad6adfbb918cbfcdfdacf5443c1d34eb2275fd05d65af674b43d771&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LMGDZNQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIEhmBEc7vX%2F0%2BYBQu2Iv7PLwKN6rFEm26JkaYdxOsS9AAiEAwgH1eVg%2FBrrcKIT2RNx%2FM1kN5aFnBHVYLPGnnciGA9Eq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDPB%2BsR%2BRhB%2Bd64YEYyrcA%2FT3qOr21afbFgHRPEUo%2F5njJ%2FWfZ%2F%2B5O7x00wDAw7LRZLMZHb1LseeaqJ4RsefCYB9uoQ8sJ1r75ZkJdBzTcKSBm6uvF%2BnDwWplth6Lj3heLrFnfN7aSYTS%2FRyhmHapZXJgVa3JivYarlt2hG5Pu%2FPvTUIp2O6PGtAO9r7OuhFfV6ar%2BKC1gS5F23dxQ6piYClRFuMxIxO5%2BgB%2B30Ym71vfu3jtCDrrkhdxNs3S6AJjiLpTjeyQO8ckVUWpO3rDlZ%2BGa6NBMyJiBX4%2FA1kBL%2FT3vcN7Z87ayk3X5J1o4ftMRrtL9ulk56Jzradi8IItkmmYNl%2BiOJqYPWLKbBQhOlRNt4Rb4ohziyxUMnpIQXS9rwvIlXwv3Jh970nrEG9S3s5cZAyuUdHm%2FkZyTMR1EurgNnZq1a3Sh5KjKFAXSaO7GkxpFI97bWnHBsDM1HbdJ64nuKz0D4rIBMTOmZLGZ8lk25ZiYz46NyWEHJpf%2FPBSHSvl5p4VeNlWb6pTLT6%2BXJen46N5OhYxBqXItoIsZOUXBcMb8SmT82mhbtYDHsi6sBUx3XPMqIr1kNJfL2K3L%2Fi9qDiLxSOCMo2Xq2FLadY1CCVz3V4HImrrF5uU9MR68B2Czd%2B3SLThJrfuMMzgmL0GOqUBIVhHNModcKSG5iDnefpGdXjww%2F4ah%2FfkQ%2BuiiwGhjjLNQBDIn5znHCUpe5uZWwJkl0kICzJxfaP6VDU4rzFWF8%2B9LimxUiV3P1jBsGj7sFqPZWU%2BM12nsX4egJf%2FRY84V%2F1C8mv6f7xDsZpDuPiLA%2FMKdFpEhBHGEwHvUCtiKPa%2BAREAbU2KMC6HLzZkRh6LUrJKMSo2eIP%2F1tN8Pp6%2BHcr%2F8oo6&X-Amz-Signature=e56f74b0a26abd3bddd71866b899290517acc07404a248ff8391dc10c1c95b32&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LMGDZNQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIEhmBEc7vX%2F0%2BYBQu2Iv7PLwKN6rFEm26JkaYdxOsS9AAiEAwgH1eVg%2FBrrcKIT2RNx%2FM1kN5aFnBHVYLPGnnciGA9Eq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDPB%2BsR%2BRhB%2Bd64YEYyrcA%2FT3qOr21afbFgHRPEUo%2F5njJ%2FWfZ%2F%2B5O7x00wDAw7LRZLMZHb1LseeaqJ4RsefCYB9uoQ8sJ1r75ZkJdBzTcKSBm6uvF%2BnDwWplth6Lj3heLrFnfN7aSYTS%2FRyhmHapZXJgVa3JivYarlt2hG5Pu%2FPvTUIp2O6PGtAO9r7OuhFfV6ar%2BKC1gS5F23dxQ6piYClRFuMxIxO5%2BgB%2B30Ym71vfu3jtCDrrkhdxNs3S6AJjiLpTjeyQO8ckVUWpO3rDlZ%2BGa6NBMyJiBX4%2FA1kBL%2FT3vcN7Z87ayk3X5J1o4ftMRrtL9ulk56Jzradi8IItkmmYNl%2BiOJqYPWLKbBQhOlRNt4Rb4ohziyxUMnpIQXS9rwvIlXwv3Jh970nrEG9S3s5cZAyuUdHm%2FkZyTMR1EurgNnZq1a3Sh5KjKFAXSaO7GkxpFI97bWnHBsDM1HbdJ64nuKz0D4rIBMTOmZLGZ8lk25ZiYz46NyWEHJpf%2FPBSHSvl5p4VeNlWb6pTLT6%2BXJen46N5OhYxBqXItoIsZOUXBcMb8SmT82mhbtYDHsi6sBUx3XPMqIr1kNJfL2K3L%2Fi9qDiLxSOCMo2Xq2FLadY1CCVz3V4HImrrF5uU9MR68B2Czd%2B3SLThJrfuMMzgmL0GOqUBIVhHNModcKSG5iDnefpGdXjww%2F4ah%2FfkQ%2BuiiwGhjjLNQBDIn5znHCUpe5uZWwJkl0kICzJxfaP6VDU4rzFWF8%2B9LimxUiV3P1jBsGj7sFqPZWU%2BM12nsX4egJf%2FRY84V%2F1C8mv6f7xDsZpDuPiLA%2FMKdFpEhBHGEwHvUCtiKPa%2BAREAbU2KMC6HLzZkRh6LUrJKMSo2eIP%2F1tN8Pp6%2BHcr%2F8oo6&X-Amz-Signature=2dc81cc15e39cc828e6568015c7374c30e583162a66cb353e373c543d6e55aaa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LMGDZNQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIEhmBEc7vX%2F0%2BYBQu2Iv7PLwKN6rFEm26JkaYdxOsS9AAiEAwgH1eVg%2FBrrcKIT2RNx%2FM1kN5aFnBHVYLPGnnciGA9Eq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDPB%2BsR%2BRhB%2Bd64YEYyrcA%2FT3qOr21afbFgHRPEUo%2F5njJ%2FWfZ%2F%2B5O7x00wDAw7LRZLMZHb1LseeaqJ4RsefCYB9uoQ8sJ1r75ZkJdBzTcKSBm6uvF%2BnDwWplth6Lj3heLrFnfN7aSYTS%2FRyhmHapZXJgVa3JivYarlt2hG5Pu%2FPvTUIp2O6PGtAO9r7OuhFfV6ar%2BKC1gS5F23dxQ6piYClRFuMxIxO5%2BgB%2B30Ym71vfu3jtCDrrkhdxNs3S6AJjiLpTjeyQO8ckVUWpO3rDlZ%2BGa6NBMyJiBX4%2FA1kBL%2FT3vcN7Z87ayk3X5J1o4ftMRrtL9ulk56Jzradi8IItkmmYNl%2BiOJqYPWLKbBQhOlRNt4Rb4ohziyxUMnpIQXS9rwvIlXwv3Jh970nrEG9S3s5cZAyuUdHm%2FkZyTMR1EurgNnZq1a3Sh5KjKFAXSaO7GkxpFI97bWnHBsDM1HbdJ64nuKz0D4rIBMTOmZLGZ8lk25ZiYz46NyWEHJpf%2FPBSHSvl5p4VeNlWb6pTLT6%2BXJen46N5OhYxBqXItoIsZOUXBcMb8SmT82mhbtYDHsi6sBUx3XPMqIr1kNJfL2K3L%2Fi9qDiLxSOCMo2Xq2FLadY1CCVz3V4HImrrF5uU9MR68B2Czd%2B3SLThJrfuMMzgmL0GOqUBIVhHNModcKSG5iDnefpGdXjww%2F4ah%2FfkQ%2BuiiwGhjjLNQBDIn5znHCUpe5uZWwJkl0kICzJxfaP6VDU4rzFWF8%2B9LimxUiV3P1jBsGj7sFqPZWU%2BM12nsX4egJf%2FRY84V%2F1C8mv6f7xDsZpDuPiLA%2FMKdFpEhBHGEwHvUCtiKPa%2BAREAbU2KMC6HLzZkRh6LUrJKMSo2eIP%2F1tN8Pp6%2BHcr%2F8oo6&X-Amz-Signature=90b5cefce08a487a503b0314234aa6e3ce084a310a7eb56c94d966d3710c848d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=1376fa7957de83b124fda315fa6e9d3f088fda4fe73ffb91ee256d52c66e9b6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=db3ab524fb555e89dded9e4547fd16ba4809838cfaf0303779dbc78d2781f3db&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=68372a66392b33eb539ce185c857ea16ef5ce93ad90f5fa03cef90d168ee7f84&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=78ba15239000a6c295630b7a3132263fcec4bea535951b560e18a7d8881c172a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=54bee7c198936aa66a41ad404a1add5aec357725088af5e2b39fa89e9c354a37&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWS3WVRE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCICDdTCQ25vruBPbIIelRxYWPrFfzDMEno68jF%2BklRXLtAiEA1OvfDrSRqe6%2BiMDuquw0nLE%2Fsfyn0iTcHP0r67%2FVFB4q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDOPsiEuVt2r%2FPGW%2BhSrcA%2BfLTdeskoCZlT%2FxnruklRu%2BAIiuSxZXqp1VzoiJ%2F6ATcQQFmmWsOjrnk3XjVvh2%2B%2Bi2iGwToRQJfWtzBWRGxT1PfZz934eq%2BZ8jLb6Jsut8yy7X0ZC5skBujRC5BLgd6d3io7YCuvnPxBufjiV2G8mJPGKy5EIusQmepGcaLW44RpfzxGk7bJBhKHaX3nREdRiBNUUoYW5xzek%2FqD2jMIdQr88lywjdibl8K1vjNW4QHYvPXTBpHhuv8RwJk294OqZrvT2zht5mDOpwBmwE7nIRlxinzZY%2F0zFa1%2FoG1ptJDOpa1RWbmPRmwRXA8xm%2FiOtjdZq%2Bu7QYEPioIjctalAnTlqAo%2BH70iKxBWz2Iii59DdTKiGvWO1kVN%2Fgxym3Yqm1SspjM%2BNokJTZ8JT5OsfP6smxPrt7KUPOx5DiGsmtvTjSYz4V4Siokt06CmAscdLSFk5%2FKK4h5N8IzQ2h6C2oWIRt7XJbp%2B5D4ycnENXBdcZCb32j9kIcJhEHRZvZKUvltyT1MPo63yNVVEgYLfD4TZ%2BnUJtkwUopyLV7BhDKgY%2Fw1SdRnZit3z%2FPg73hXPShOzH%2FaqSD5pw6nuwzcaelDjGfTR8ugyeP5MG9FKWROOkR9i2JxF3jH9DkMMbgmL0GOqUBX4aesjSpUa7Vup2Q7HheSmUYmse%2FmtzeCqlQ5X30zggcrbbCcbPKI6KQQyeDQ%2B%2B13NDz33xxTcgT0zoPLL1onBW652F3jKihaBpdkIey43kmZ7gTCMeIiQqIRE0PuAgJR9lYIca9xMTLKT8LNHqiU591q3MujOWR8GnLIncjSX6z5N9mrMcbUQYP1HN8qgaDSOGaaFdVLtEr7AgDy%2BFKnKuP8BfD&X-Amz-Signature=50a41934deed7237ed62962a8484024334841c89af4a49ad0ed3c4d689830bdb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BRKF747%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIC3pS6xzr1fZCeIIdu7h4hnGSyoC59Q1GCxNQ2krcQg0AiEAsjQke8Ru2JJ%2Bs2zvPp9y7BARzyaSCHZJsOPgYTOFHdYq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNf%2BsMIBUFhhk%2FmJzSrcAwKYTg3ujEmG8wBZfiyxdxHwbCHe%2FMuo9DMKqRK%2F3EsP94PIfEbWzANMmgjHknpEwwS4sXHEzc7qGn4eJC%2FcKItqNbC3OVo5DGzahghmvYcosfhguofWkjhGpDMPgLWZDcGyBu3Oh0s%2F%2BklEO3GI6eiVjjPBQmibsm%2FH2%2FeriK0yJe25tlwLMI%2FDOON8sXgjSCtJt5KsA5NKJXiTAGq6Ntkubzmsab%2B5jZjf39PCUpJHMsCTKisxzB7eumGB22sqr1gT5cpDDinj%2FBT5GUB2Px76J%2FmNiyJtINs6ZENztKCcTEfix3l2Ryw4XgZOXhBXEgc3UxcmmgPZzEhRn6C14KvU45dz%2FrheP0LrF4KEUGBNVnP3b16zzT02MITd9MZJ1g7VL5sAw49p6mKe0Mh04ZRSegT%2F4CA94cxD1RZbGsiLo2pacnrlDi9BXEosveTZwp3feym2mXxdbny1Q%2F%2F7pJJ776GWz9hX5ToG%2FdW6ab1d8lCiYkR8KaNMXGOmaH7QeeZpbNgtcNtPIHvvkOV0q7lZ4T28eAln7RP4hwHowEGFPdxHGRRVLyyRG%2BwuyQdS1yM0Aap5EB8I7Jaeyf8zGo5KmF%2BSZ%2BJiq4IAEAfWdrIUlWitbUG606yn4nWtMMjgmL0GOqUBNYJcJBdbS66Rk3FF%2F8onot8SJ9n%2FZ0iCP%2Fo4VgRTK4LH14sWJuI0Y8UFqGRHNFcJfmOTLWmfrQwWGhQ3P%2F76B%2BZFT7uF1vW8g%2F4Il%2Bm%2Bqhr2%2FYZdC9Biha34Fp1284dA0o6%2FlkiA0UvEeCzv4exG4UPRIQUbdai0jpYr6XT0qC4ntmFYfJg%2FO0%2BKX0o3JX46l%2B9joL4%2BS0boC7em8%2B9dvIrYPMtn&X-Amz-Signature=08d18e5aafb5da91f3feda27be8f44970b245fcecd4f6d6e37d7466cab9d6f74&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BRKF747%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIC3pS6xzr1fZCeIIdu7h4hnGSyoC59Q1GCxNQ2krcQg0AiEAsjQke8Ru2JJ%2Bs2zvPp9y7BARzyaSCHZJsOPgYTOFHdYq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNf%2BsMIBUFhhk%2FmJzSrcAwKYTg3ujEmG8wBZfiyxdxHwbCHe%2FMuo9DMKqRK%2F3EsP94PIfEbWzANMmgjHknpEwwS4sXHEzc7qGn4eJC%2FcKItqNbC3OVo5DGzahghmvYcosfhguofWkjhGpDMPgLWZDcGyBu3Oh0s%2F%2BklEO3GI6eiVjjPBQmibsm%2FH2%2FeriK0yJe25tlwLMI%2FDOON8sXgjSCtJt5KsA5NKJXiTAGq6Ntkubzmsab%2B5jZjf39PCUpJHMsCTKisxzB7eumGB22sqr1gT5cpDDinj%2FBT5GUB2Px76J%2FmNiyJtINs6ZENztKCcTEfix3l2Ryw4XgZOXhBXEgc3UxcmmgPZzEhRn6C14KvU45dz%2FrheP0LrF4KEUGBNVnP3b16zzT02MITd9MZJ1g7VL5sAw49p6mKe0Mh04ZRSegT%2F4CA94cxD1RZbGsiLo2pacnrlDi9BXEosveTZwp3feym2mXxdbny1Q%2F%2F7pJJ776GWz9hX5ToG%2FdW6ab1d8lCiYkR8KaNMXGOmaH7QeeZpbNgtcNtPIHvvkOV0q7lZ4T28eAln7RP4hwHowEGFPdxHGRRVLyyRG%2BwuyQdS1yM0Aap5EB8I7Jaeyf8zGo5KmF%2BSZ%2BJiq4IAEAfWdrIUlWitbUG606yn4nWtMMjgmL0GOqUBNYJcJBdbS66Rk3FF%2F8onot8SJ9n%2FZ0iCP%2Fo4VgRTK4LH14sWJuI0Y8UFqGRHNFcJfmOTLWmfrQwWGhQ3P%2F76B%2BZFT7uF1vW8g%2F4Il%2Bm%2Bqhr2%2FYZdC9Biha34Fp1284dA0o6%2FlkiA0UvEeCzv4exG4UPRIQUbdai0jpYr6XT0qC4ntmFYfJg%2FO0%2BKX0o3JX46l%2B9joL4%2BS0boC7em8%2B9dvIrYPMtn&X-Amz-Signature=76a278bbe5413e073efdfafb51c4c239aed9e6a97eaf4cede5a65499dd6e8500&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655LDLJF6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIAsD8r210cu3dGycR0d27J6R%2BPtd%2BhDg7irlYENocAm1AiAFORdpv1TBOxblSFZTyr%2BU%2BDcY9lDryxPt6EY5a%2FmJ8Cr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMmHXCAQ61LuI%2FjgvbKtwDqp%2FDyVdzQ7q1yvDjqMsJ5Coju%2FBV9Dt%2BorHPC6RDMWi0ZOnkiudpE7dA%2BKjGIcINZ1cN5wtPwNTXvGfWRqZ9MLaUHZ2da9vTP2jR0Winv8bPk%2FKTopm2otPRB6zHw%2Fh62IFLNWptQTMUll3RlA88RUH7gO2O81dSRz0ELuCUjboCJuu1tRNSj6P29lsu9z4RnCNj21Hbp5M7SJg9OH1ttFKqvgVq6PUdBFRL%2FjSyXyQD%2F1StlH0uUjfACRvko0O4MeiIKm5ZKywnqGBpJa%2F1ErqmQRAnQ0c2lQwbNpNaAV%2Fn0dM7ruPb8utF%2F32tMGYOqrCI%2F3gZM3VujwBcfnnoCUEzNrQL8XcaK52OolRmaGtqjOTj%2FNtyMWvGpJ1DTPo3f7bofTPJjMBns0lOTY95oAC08FwBZcZCwb25JwrNebkxPo5bFQX%2B%2BnV6OTI8CK42PRaue6fPFePeJZBmTQ99SvBajWodq6jhIrU7CNxVHowhR7FLuDAQIAhQXoO4GFEHvMbFEGRdla9Z17u8%2BU%2Bo9LNdOmRz3EnrbTTepSi0wvjiYGrn0vAXRsBUoiid%2FaAVBXQ0xv6Y4OY8vev3zZyfmNVZJLlZTQ8fsrsk%2FcMan1AheFYPftVz8km9utQwteCYvQY6pgEvBmd3tATdti6rmXBHhatB%2BnEgBJIr1MVZCjrZpdtehl%2Bdp3tX2jyMEY5jcpgntpEeBaYsVwH%2BjikVbrAjW3WtIVyWsTsNIia07ACvv3Xvt4N5sHBrvefbCMAWfUJeQZBrIvVG01SIZIYfok%2F%2FzplVIe8e2AXc5ZatvJT44p1YYS0dK6NLoxxXYIgAwkJfEJUTe8HpbEF4wDKn%2FmX6r5RGTZK17w5E&X-Amz-Signature=ba8e1ce5be15ebe57954905455390127409599ce0c7b27b3fcff2fe769929bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=4b34641e39db29fffb73098c2ed3cdc4944d66ffb9a6c55813543c09ae89a6cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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