

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=bc36b6e7dd40270afe3fe4085625db97a50976a2e168eb643e61359e4950110b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=022aedf555079ab16a35937623c889e432c4f63ac1013e73be2d899ad7b1db9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=90bc7c0a18b24f62a6600d4e432cb92ee07d3857e8ab2141f271b0e957cec4b6&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=4c8aa0c2bf78fb75268d8596a4c04882c4e4fe56bcb6bb861ba20aa308f56e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=9a0bc1106963b9d2608b0652dffa851849753ab9526702f92bf3c2b365cfc08f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=144debadc7473ee9ba960cc20246cce32a2ad29df643184cf7968c242629592c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=2d52915c453c4e547d5d233cf836acaf167ffc36d9d435763c1322b5ba926e67&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=c72eb1c6e7e03dc2effa22387f01e7d7af805af930d1e8e085f0d317562211f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=e816316a2d732763b2207ed06ff7dae106357b8769483f5db4e932e2f5e74380&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZKI7EI3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGm5QAf6F5mZda28BI4kl9LpkYQ8FviOAJjbxfyl0z%2BdAiA800ArSzfr4sUwFJI3o0Y40byF1X2fydAlOoq%2F8po5lCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFBg9NVLvLf6mxEzKKtwDxXbcFPh1iTSqtx5hPjNgc6efeLPmSW0a1Rhp5oJxNpiRgXIw1Aur0XCr0SCRxShOnHhGS%2FRQBcqGuJGVjWyg6bkjcPwdQgMFbJG%2BpUrE4sd%2FHjyN2LlLXj6uE9EaZhBDBM86xkCVW21ez35RWhvjtFNh5pw%2B3uR67HQ%2Fs5HfDY7iqWFvrh8m7gKzZtJiGps4OXuVObZeNGiioqhA5cl0meBRX14OnsgD6gTTwwZ%2BaUgMke%2FzkISNDPnyKjpi2HfSodHdilmMWj7E5YjcVPWlnegQaS7vxgCgT4vaKhwHwTBg8GDEbqMDo2lE%2B7PzQaSgE03XVR%2B%2B6C8ytxa%2BpppfhebHzQKdaYW3Ku4tDtVv%2BEpo23uiDKDzbEFEgv4r%2FUXSOWrrHFodGasrWXJf1UCO49N1bUl%2ByKI70Fq4OyWOEnREq5tmV%2F0UewNkMi7Vss57X9B9cw%2FyH8HzV54Zh3SXpglXipjHJjbZPucafm4bFp2fEvH8JrTjyDIuAmbLUgW%2FeSkscM2NxfcrnrtqrgLYOewllhS2iVjf%2B8Y%2FZDalOLFm2C3upC2EIf%2BS04fwIBsQvUVm2gCxWFueWT%2BJW2f0%2BMNG2c5oHd%2FrAYjLUC3zxbMsexrahYMKQhF88n8wz4WdvQY6pgFY%2Fu5aJOt6u114cY8Czcm1R7p0VSRR7BmY8Mv%2BEONepr9HaJR7pQIYdPRKIprguwr%2FJRUecH9XgjCUWok9VGxWS%2F1Wy3V%2BArBchgYdYTHABUpufeSQYpkyiwD3tS%2F1APziBdHD5QGVXB1hid4yB6Td65NKDlL8l2bNUYAibZ52TN%2FHVbnOhHmCE%2FmFwtgTSdJ%2FlNTe2ts90SNlpHoAGYeUZF9aXTzM&X-Amz-Signature=3e5bb630a40cec5f42e1240db2c1c5377b061a61c9977c8abd874da48400d0be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZKI7EI3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGm5QAf6F5mZda28BI4kl9LpkYQ8FviOAJjbxfyl0z%2BdAiA800ArSzfr4sUwFJI3o0Y40byF1X2fydAlOoq%2F8po5lCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFBg9NVLvLf6mxEzKKtwDxXbcFPh1iTSqtx5hPjNgc6efeLPmSW0a1Rhp5oJxNpiRgXIw1Aur0XCr0SCRxShOnHhGS%2FRQBcqGuJGVjWyg6bkjcPwdQgMFbJG%2BpUrE4sd%2FHjyN2LlLXj6uE9EaZhBDBM86xkCVW21ez35RWhvjtFNh5pw%2B3uR67HQ%2Fs5HfDY7iqWFvrh8m7gKzZtJiGps4OXuVObZeNGiioqhA5cl0meBRX14OnsgD6gTTwwZ%2BaUgMke%2FzkISNDPnyKjpi2HfSodHdilmMWj7E5YjcVPWlnegQaS7vxgCgT4vaKhwHwTBg8GDEbqMDo2lE%2B7PzQaSgE03XVR%2B%2B6C8ytxa%2BpppfhebHzQKdaYW3Ku4tDtVv%2BEpo23uiDKDzbEFEgv4r%2FUXSOWrrHFodGasrWXJf1UCO49N1bUl%2ByKI70Fq4OyWOEnREq5tmV%2F0UewNkMi7Vss57X9B9cw%2FyH8HzV54Zh3SXpglXipjHJjbZPucafm4bFp2fEvH8JrTjyDIuAmbLUgW%2FeSkscM2NxfcrnrtqrgLYOewllhS2iVjf%2B8Y%2FZDalOLFm2C3upC2EIf%2BS04fwIBsQvUVm2gCxWFueWT%2BJW2f0%2BMNG2c5oHd%2FrAYjLUC3zxbMsexrahYMKQhF88n8wz4WdvQY6pgFY%2Fu5aJOt6u114cY8Czcm1R7p0VSRR7BmY8Mv%2BEONepr9HaJR7pQIYdPRKIprguwr%2FJRUecH9XgjCUWok9VGxWS%2F1Wy3V%2BArBchgYdYTHABUpufeSQYpkyiwD3tS%2F1APziBdHD5QGVXB1hid4yB6Td65NKDlL8l2bNUYAibZ52TN%2FHVbnOhHmCE%2FmFwtgTSdJ%2FlNTe2ts90SNlpHoAGYeUZF9aXTzM&X-Amz-Signature=b73b47c8a131d8c9ff763017bf8c097b5b86ea46e562da5f6f5807252b877807&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZKI7EI3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGm5QAf6F5mZda28BI4kl9LpkYQ8FviOAJjbxfyl0z%2BdAiA800ArSzfr4sUwFJI3o0Y40byF1X2fydAlOoq%2F8po5lCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFBg9NVLvLf6mxEzKKtwDxXbcFPh1iTSqtx5hPjNgc6efeLPmSW0a1Rhp5oJxNpiRgXIw1Aur0XCr0SCRxShOnHhGS%2FRQBcqGuJGVjWyg6bkjcPwdQgMFbJG%2BpUrE4sd%2FHjyN2LlLXj6uE9EaZhBDBM86xkCVW21ez35RWhvjtFNh5pw%2B3uR67HQ%2Fs5HfDY7iqWFvrh8m7gKzZtJiGps4OXuVObZeNGiioqhA5cl0meBRX14OnsgD6gTTwwZ%2BaUgMke%2FzkISNDPnyKjpi2HfSodHdilmMWj7E5YjcVPWlnegQaS7vxgCgT4vaKhwHwTBg8GDEbqMDo2lE%2B7PzQaSgE03XVR%2B%2B6C8ytxa%2BpppfhebHzQKdaYW3Ku4tDtVv%2BEpo23uiDKDzbEFEgv4r%2FUXSOWrrHFodGasrWXJf1UCO49N1bUl%2ByKI70Fq4OyWOEnREq5tmV%2F0UewNkMi7Vss57X9B9cw%2FyH8HzV54Zh3SXpglXipjHJjbZPucafm4bFp2fEvH8JrTjyDIuAmbLUgW%2FeSkscM2NxfcrnrtqrgLYOewllhS2iVjf%2B8Y%2FZDalOLFm2C3upC2EIf%2BS04fwIBsQvUVm2gCxWFueWT%2BJW2f0%2BMNG2c5oHd%2FrAYjLUC3zxbMsexrahYMKQhF88n8wz4WdvQY6pgFY%2Fu5aJOt6u114cY8Czcm1R7p0VSRR7BmY8Mv%2BEONepr9HaJR7pQIYdPRKIprguwr%2FJRUecH9XgjCUWok9VGxWS%2F1Wy3V%2BArBchgYdYTHABUpufeSQYpkyiwD3tS%2F1APziBdHD5QGVXB1hid4yB6Td65NKDlL8l2bNUYAibZ52TN%2FHVbnOhHmCE%2FmFwtgTSdJ%2FlNTe2ts90SNlpHoAGYeUZF9aXTzM&X-Amz-Signature=d3d209bc82e822f1e1280832f2cb4f79e13faba51c78c9dd2df6800f49f4919a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=4628329cf97eddba184fbdab665d5e76e8e421b70506ffc8dac99280423bac04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=396ac7e8196a3667bca5e8b1a5d1bc225edda9fca0d9c7191635cadc878eedd9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=f38683c41cd5957bfe1b846934020499590081c5979a161f25c1151899842de4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=e306caef19dbabc95a8e8204c28a9a84972940c88b6ec6113ceb126835322499&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=c87175e64bd51c3e91c02855a91e7a7c12f5773e8a9e6892c5c0a86286fed9f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX72WEB4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDIUbRxbQBAmgc1fZG9wSn0zq3BFrAZuBKgD%2FDGxmpA0gIgaUBDSn70eoOmPFiUqmv5WQ%2F%2F3Ma4Vm3njWKM9OFF9DIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCEpU%2BL%2BnZkaeHGpLCrcAyea3%2Fp0IatBnHP0GAZ%2Fc%2F8OBadQbWbbZYpaXsO8c44N0PjPiVOTlJduM0iGbAOiWf3OZE8a5SMvrlRbiBBuf3HtQbn6VRDzbkWOq%2BXwUMRKReWRxYWvbeUPNfk8tB0Zc%2BrKXeC67Iptm7y0yA6YU30lPoKhgSqOfpTY%2Bdp4%2FEcaE%2BbcIHaUl2AcdbQ6xRffv2tTSHCHE1B06d%2BMHakwy2wosCIQP7cH2KjfWB8LPebMm2MMc3SSg9nWyY2LLdPtdsxTKmibsFBzt64wTimQqawUVDHjHwJPzk5rwmlhVJk76QJBeMQH3plp%2FACGkXswdDxjllvif7Y8V%2FFYHsHJwuKHoxAZjK8jPLjPBnBt2UAYaQlQ0w%2FAmV8pe4bs8D5EyAJHhUInq3O%2BktJQJ5HzLZLiYQT8oBD9bSWZaFBXqdVWi%2BGxhn0gt0PbZhWHkNB4X2JhkQzEx%2BftRkz2bS2ULdlijVFZlc0wEMEJTId7bVbp%2FjpWieiuc4zWLtAVzzpxS2cQIqTitjhSjMNnYb4W842yq%2BOJw4cPWk7GXSG%2BgD6kSIAtuhs73tZitTmz8hnkp5811b%2FWmxvfK%2Ff0%2FLUwpxdWm9d%2BOmgQRJ3gZ8r2T0FuOpUXaehuwlmG8P0KMPmFnb0GOqUBdkMGD4E8SWisakz33D8JF%2B%2B9CZ5LgWXDHteGMH56GDr9BOV9vCYjo1cQBGKyC8zhtFH%2FrfOw0gV8igb6VHJdoAJY1doccbN2%2F0iJryYQ4Uak13Yh2tLQSZEo%2FHsifwt8sCKK2blWel%2BaUSYjGO288m576YTkva2bPqqVAgYVQO2qYJijS76QlfUBD3LChoHqR%2BkOFSAUznhlQKPlWfyia0ZGdDKU&X-Amz-Signature=b304c9d1a18f160f6de32b685e30255cbf733f38f8e1d8aa70f054b2f14a0222&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=513b213fa2422d6183b22e6290410c4836c9acabed1a55693cb0e0dc1f340fc8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=9428e1decb0ce8bf5ee67322ff5097043dcc04d3cb02a08c10974d074ccf0c44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636QON2EA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC%2BpdUxSjah77IgOEJUAtEDI6HugRr%2BpNGwYuEp%2FuDk9AIgO7SYpIl4adQnOOwBrnDuhKgDI38SIOz2k6g7DDG1X1wqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDT81ahjUmZ9hj519CrcA%2BA2B9ih9y3Gdi3aHaekQBHbOUyfYQ3ueST0MkL1%2BmzchEjGItWb4%2FerAb3Y5YAGjHMUXt1OPy%2B7TTLUN%2FXc3WL7OzkRzqfcp%2FlbcKZ4Y7SCc4%2FkK9bzISnZWYu6rRWKawaJ0lnkW4gHLfaHIDZqa5bumntxbePd8ioSw9eNTCQ8%2Bxn7Ulu8CkZfkZ%2FHx1oC4rySJcIDJkyI%2FkgLDbD8jzeAs%2B%2BcacisWoOECYOAxTj9AGBEVwBXD2tsOP7QR04Xt5OTZFH%2BXV2V9Z5OcbR84vdA0yQKDGcOqb7fxuthBzaKhn3l%2Fq07Mhdp%2BaMTJXevJqNi2ASoMs%2FUAJLaxb1VrUvSQ%2Fd3%2B4lbzDaRvaoytjUd3mjO5cnjpWqdpzYESeaTg5GO053mUFU4pCpvUbgqmCXKjIE48O0Uewz7bu4ML8jKOEgHhESuryXIPkQR6avi2rUVJoh42inj4Mg22hrVFdorpMDk9vTh8HYD8fvIDLYzShyaJMozpWEb9ZKf5MxxHsHmS2DaHUmE37tGk3rEzN1%2FkCX2Z1wzXsa2EdaTViXwipzr%2FXb2nTIieAfqt61gFfFlADzp7svt2t%2Fexf393ugZ38AVHNFz1OEMeOEXYWU9393vxmS3TsW5FSs%2BMKCFnb0GOqUB4QHz2%2FRUFfqeE2%2ForRt840S3Z0BZJ0ezspnZXqz7WqrFREWxm7A%2FKo%2FYc4UOLsItLgLp6L9998CCMB73Oh3KWUH4MonKN0Nhg05gV9gmc96vlhQeovMKjJP2iKbK0Mp9bwIrAAoBQzB2gqDEWDXNfczSFti495E3%2BPmKfxuROvawfC0nFOdCf4WxB9xtMbtZFgVRfUUC%2F8uPwCIUq6i1Fp8i55lo&X-Amz-Signature=31d97f96dea1b375caf304ed87523fadbb7b18f5692118da9ae5ad3a7aea8685&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5ERHN4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCsVewNbg3RyDP23RgKwt2kphNYjbkBFyBTmlYC1vKUkgIga5EgjVHs7v%2BHSZcTY4pEVyqYeBDqhdpsqVC8bpZ%2BJ5oqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOPMDCJ5Kf84P2pkSrcA9%2Ftl8LydZGLswSMvrUYPNTS1U%2BlKv%2B2sLdpKhWzQcrGckzoF1iF%2B%2B92VqrM51CWZbUPevnSI%2F0%2Bo2ZDCs5vPomRgsk5TqOau7Ixlmz7HKsCJj2ZImU53CziIrFTpvtKGXoauoyHcbfgQTBglfWyDDaPiTTTGERFY%2BV2FHCzdbtzm4yOhvOxt%2BdZAvxNn3L6WfbzWuOBa4IMCH1kS3HqRhKo8z3XH%2BdgOtfeiNNce7wMMXcw8BQt%2FhqaTzsVICwmez3758wFwDQMem%2FGhCQqnzSRpzwzmLXZJZOC8%2B8d0CxqebUBnX5VknPcXsNdy%2Blg0GmlFh%2B000bZ27Fq7Sb2IkBn3wQSytHbBjq3%2FfgP8rHFMlEx3Ens%2F2lkIzfdUEs4gvvtIqdIY2AEj219ot30FtnrUIVEyhdff4uof654CZEegEiZuppXXqpxb%2F%2Bgn0ByEDlV47OV5zELSoHXkNVBLhs7zcSpqTuxmMy5Yd9xQFLoa5%2Bcwg7OWo%2BBICKLMIfgk6QUzW17FOo8nDYzFz%2BE2DdR9wOpWIw0DhHhyscdFbltzUmlXhaphdjixRCqVcsVKCKZNGwH2%2B7lLWnFVb1anHgBm6NDbF9MtA9%2Fjtx29S5pMll0PiR1BhxfOItcMKeFnb0GOqUBUIWfHnDIUPBOxbCjT22COVqXLSuT7r8R5%2FpB3ctIXHPGvCQyE%2F%2FiOFCuGfQIIfrL1GceW0FF1FoBpr2KwnCEAGCCN5GsKBzqdC0mgKwrYg8u1c2kS3r2oZci87p6aMIa7svwBaqdPWc3ggJ2KfNJUKhk7zbYLp2VVMnEb7RRHdbcFej6xkvjJABrylszdcinypYSrhoM9S4%2FzEE29Fe%2BRm7UiU4o&X-Amz-Signature=4ea59175844cb034f249d4afbe75c2233b250704a55596ff0032e60c58969620&X-Amz-SignedHeaders=host&x-id=GetObject)
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