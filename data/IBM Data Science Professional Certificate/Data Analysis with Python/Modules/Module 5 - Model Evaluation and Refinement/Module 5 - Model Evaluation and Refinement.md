

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=83d28231b3805872775ad308f20c120df6cbc0a9f4d2ee844a1b8c3f9a9ceaf8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=d4c68ea6d1fed6ebfb711332df932b7c6950078791573a79f34a926e97e198ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=7e928384e9504ead4d0181aa6681b730ac1efc1ca4c6e11b8708b7636de1ada4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=bcdb10471666833f9670f582c62418c2840bb2705747c97cba3f2db48e97a239&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=83811a0f1c66cadfb8c362c0f143decde6d1722232630361d36f4de06156a984&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=be8f45a523f5157043c0d34c334e35242eaa4d1fd742bd9814520599d822305d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=2d54a4b3ea0571140fcaa01e0d3a158bc41d785734c92be3b498c9fc6faa4c46&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=2997a5222694142d2d5baf982cb9b44ca96f9fb54d6f9155845597130baf03fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=ea8c4a581609db4bdcbbc8f4c07cc013e425ca3d5730f9b4533c4bf9ed7f4f68&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466264R22XK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWlRE6eK8DULxDSyM2lGk0WfVxhRO2JimcN4FsKApU%2BAiBBW6CQeDCN6m6BvkuvStigN3Mf9lSTuEwErgjM6f%2FwdiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJVGmLxmOY0soN8FRKtwDwImLFrA561Nv1EHm7Q48oGEVxp5gLF1wDYpV9O%2BnuwXFPyDGrKc8syziCONd7ldK%2Bbnx9YKpfwhux0Gi2lA5dngba4dKSsWm7U2pXqndXjdU%2FXP4OkCanCtMA4S4BVGdwBxKqfwOF5HRzViVZgj%2BurJHCiS6BQMFRsDyCbZR%2FfpLCTixr7nmA5npIOuHcIwEhEcaq5v2PCHgSpm0v5t10E1Pq7Om1hAtIe4NKqq92O9rt1FNqN50mzMQTrU5qxfXTtC3wjHIN1QKkKixIkJKmMziQtWDSiRiECj61PPXGWDKmaw1pTVrJZ9%2BwFdNRvqYDU%2F%2Ff076gYWw2sh8Lg%2BhOognuQqcw518hcAeR%2BEAWccwXF5mHjo2XgcwEc3LBpMN1M6iMmRIjjvHNdSF7nPbhaAly3kPw9cSXQotHXWGXs62lXBPpEz9Bf7XdMyV2KxxfjKG6q192mjJvHccaPCsxjclgpoM1qlVIXy%2F9UAljJE4XL5sQDYNZIa%2F70Ke6WRnwk%2BXPDvs6UOYs3whN1Yo7sRt3P0R0MgOXbxnCJhj8Th0%2FUiBlJ2PKwkv6bN3RbdgOdFYzulsOwjxDs0so8vfofUsiixnV8qWTD7j33xhUC0te%2Fppi11Zy71Amnkwtcr4vAY6pgFu6k25B40%2FZwDol5T52Dtsevzn%2FKzyM0nbHZiF8To1FMFbuA8Izpz41ael0vZXerNNXNlfLtd4cqwPe9tlH6RD%2Bl%2F0cx3f7nrL%2FbQNzdiElTCjpHtTN9c7CwJU6bhUn8nhO6XGlXUNafgODEAyaOX%2BpYIgax7WaQOmsWxurDCK5kKRxH7A0eIeIgf8rSKkKNVn1nh514sh8F7c9EV29b3TN257Qcj7&X-Amz-Signature=a0364a2629bbc7125dc63b1132a0fa40a8f32fdfc1b40d8b04fab26d327bbb42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466264R22XK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWlRE6eK8DULxDSyM2lGk0WfVxhRO2JimcN4FsKApU%2BAiBBW6CQeDCN6m6BvkuvStigN3Mf9lSTuEwErgjM6f%2FwdiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJVGmLxmOY0soN8FRKtwDwImLFrA561Nv1EHm7Q48oGEVxp5gLF1wDYpV9O%2BnuwXFPyDGrKc8syziCONd7ldK%2Bbnx9YKpfwhux0Gi2lA5dngba4dKSsWm7U2pXqndXjdU%2FXP4OkCanCtMA4S4BVGdwBxKqfwOF5HRzViVZgj%2BurJHCiS6BQMFRsDyCbZR%2FfpLCTixr7nmA5npIOuHcIwEhEcaq5v2PCHgSpm0v5t10E1Pq7Om1hAtIe4NKqq92O9rt1FNqN50mzMQTrU5qxfXTtC3wjHIN1QKkKixIkJKmMziQtWDSiRiECj61PPXGWDKmaw1pTVrJZ9%2BwFdNRvqYDU%2F%2Ff076gYWw2sh8Lg%2BhOognuQqcw518hcAeR%2BEAWccwXF5mHjo2XgcwEc3LBpMN1M6iMmRIjjvHNdSF7nPbhaAly3kPw9cSXQotHXWGXs62lXBPpEz9Bf7XdMyV2KxxfjKG6q192mjJvHccaPCsxjclgpoM1qlVIXy%2F9UAljJE4XL5sQDYNZIa%2F70Ke6WRnwk%2BXPDvs6UOYs3whN1Yo7sRt3P0R0MgOXbxnCJhj8Th0%2FUiBlJ2PKwkv6bN3RbdgOdFYzulsOwjxDs0so8vfofUsiixnV8qWTD7j33xhUC0te%2Fppi11Zy71Amnkwtcr4vAY6pgFu6k25B40%2FZwDol5T52Dtsevzn%2FKzyM0nbHZiF8To1FMFbuA8Izpz41ael0vZXerNNXNlfLtd4cqwPe9tlH6RD%2Bl%2F0cx3f7nrL%2FbQNzdiElTCjpHtTN9c7CwJU6bhUn8nhO6XGlXUNafgODEAyaOX%2BpYIgax7WaQOmsWxurDCK5kKRxH7A0eIeIgf8rSKkKNVn1nh514sh8F7c9EV29b3TN257Qcj7&X-Amz-Signature=a09ddd225ab431dfdd3b57454191a8389789eaab3a87ae1f2ddc218df99c6492&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466264R22XK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWlRE6eK8DULxDSyM2lGk0WfVxhRO2JimcN4FsKApU%2BAiBBW6CQeDCN6m6BvkuvStigN3Mf9lSTuEwErgjM6f%2FwdiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJVGmLxmOY0soN8FRKtwDwImLFrA561Nv1EHm7Q48oGEVxp5gLF1wDYpV9O%2BnuwXFPyDGrKc8syziCONd7ldK%2Bbnx9YKpfwhux0Gi2lA5dngba4dKSsWm7U2pXqndXjdU%2FXP4OkCanCtMA4S4BVGdwBxKqfwOF5HRzViVZgj%2BurJHCiS6BQMFRsDyCbZR%2FfpLCTixr7nmA5npIOuHcIwEhEcaq5v2PCHgSpm0v5t10E1Pq7Om1hAtIe4NKqq92O9rt1FNqN50mzMQTrU5qxfXTtC3wjHIN1QKkKixIkJKmMziQtWDSiRiECj61PPXGWDKmaw1pTVrJZ9%2BwFdNRvqYDU%2F%2Ff076gYWw2sh8Lg%2BhOognuQqcw518hcAeR%2BEAWccwXF5mHjo2XgcwEc3LBpMN1M6iMmRIjjvHNdSF7nPbhaAly3kPw9cSXQotHXWGXs62lXBPpEz9Bf7XdMyV2KxxfjKG6q192mjJvHccaPCsxjclgpoM1qlVIXy%2F9UAljJE4XL5sQDYNZIa%2F70Ke6WRnwk%2BXPDvs6UOYs3whN1Yo7sRt3P0R0MgOXbxnCJhj8Th0%2FUiBlJ2PKwkv6bN3RbdgOdFYzulsOwjxDs0so8vfofUsiixnV8qWTD7j33xhUC0te%2Fppi11Zy71Amnkwtcr4vAY6pgFu6k25B40%2FZwDol5T52Dtsevzn%2FKzyM0nbHZiF8To1FMFbuA8Izpz41ael0vZXerNNXNlfLtd4cqwPe9tlH6RD%2Bl%2F0cx3f7nrL%2FbQNzdiElTCjpHtTN9c7CwJU6bhUn8nhO6XGlXUNafgODEAyaOX%2BpYIgax7WaQOmsWxurDCK5kKRxH7A0eIeIgf8rSKkKNVn1nh514sh8F7c9EV29b3TN257Qcj7&X-Amz-Signature=0b048c9c770786a0a0471f6e53e61fd77f06b569c19bdb230b58baab5733514c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=60f7c4d0e88cde654eb66da737d738827c65c4deb50e14ec31f00c726e66e615&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=cf4f2383a290353e786e08a1af15336617d28866c06f37aee8fdf3e2cae260ea&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=dca419d0bb2ceabc9e18f1885f181093d17d38c4c5281715c232ad9b5666cb73&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=b683a978743ccc18af5573ff4adb326dc4cb3abba45a0a32a0ae497b0f818a93&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=9cd44e6ce96d77386780970071c39307c6a5865b5e1bf6680eefe06f9697e2ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLQM7YH6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCECQi7EEhW4diU5%2BZbjLPLOFgEasjijk7wARy0b5qHpgIhAIjtNp0si5E1Tb6PlcQfL4N8OF9b7XbtWCrH2uDVnobSKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFWEmGY4RwGTRYfz4q3AOSQ9%2FlZWB3xM%2B4ilgpZOIReXYogVurPpDTO2jFlvKHKkxHmX5OXD1s3e7z0VMxO1LD1pLoHyVLpuJLID6fnIrkshAyi3jBTaaHjX2PhvYSiYb9dG2N8WhWTakoDiMmft9og1307RuU7Cvu%2F4eqpr1xRSwmnAuy9U1hzjDSS2WwkHuZbTND0Ey75nkHuAYvWYNh18fwX0IVCAbBo1OSw%2BOLVu0QlyodqPGG6mhe6wGQzxzfXCRc3KOwihjy7SGZsiOki1w070d971JHic939PtThG7XFgx6AD3KA7LvgB%2FfJCvfao5tB94JY%2Bgb%2FhVfcQUPw1N9M45WULXegyb2%2FjpPcsrGlO4OeBvKwVUDZOphtQ08nqsi32g8AaFCDspVFk0Sk1pUlHXlyE9Yb9jazj4QsDzQulV8YyIk87Px1JR7%2FCmmdZ%2BngNNIE7efadcjrlCUp982a7fuRfAgYO875U1uYeAt5m59KNTDUZrVI1nElwoAv7f2PabjE2E%2FgOd60EICdEL9KCDORhz5yTnZwUc2tRuHwQHkgVozKfDaWOaMLr%2BfX6%2F88G0tENb6C4zFdHHGAnJd08Qs1cB7vMiMfCRewHOSTlJeBMFLGu7u88cKNiDuIA7vdcd7UsgAwjDuvfi8BjqkAd5quhDuVWoXfqTrQGNKra9FQtiIn4pxijYEWRSzR7WP7g0s%2BNWNKQKt6WKWhClW9zTppnoOudxchHah%2B8WtV7R44qs3ePcKHIXyzA%2FgdsMlNOEOwy29bV3QgMTsXete%2BwHyFFE0bea28qXwSYhwxBYpmYQeGGzINAHxJvTDxdNczrGp6gMrC9rRbuvrVlZzPL4ayR84pq8%2BKL4FZJZCPzOeu8w1&X-Amz-Signature=6a8f75982794a691df201e2fe0e7b32d33786b8121956a483f05656e7d86de4d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXUNM3Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhDycaKln%2BR9KeSdaWpeFyP%2BF%2FimbzMJWD%2BlwU9bfQfAiB5VmWEw09Cu%2BLNadKjsLQbgjhOrYMz%2FlRcEjtHQfvYECqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlhgw%2FBgvop9BrjKjKtwD%2FJ%2BAOWBcI3hCJJ0qeN3YelyH%2BVGRMLCqvVk%2BvOQXsTz1BnCcBqeMPOyO8g3%2BImZ46tsyOzHT6hffg9hIJWTnDLmoKqoaPYw%2Bbef%2FnzzoTJZUah2gJdTs%2BCuQqMOVJJppdcOy8J1oKLk9YbpN5%2Fk1MiDioB14BEKV01%2FyHR3XVA2K7sZfD2dL3brePK%2BsOOSZDzsglPx4wQdyBWIZOkJH%2FEkLPM1UmB0wSczTxjKUW4kxVcTiHxRm1N%2BQ3xsIBUkhKG4QrxjQzK%2Fn7kSwxHENfCMNz8%2BE7xvWNtkhrIonNPSxifIAP1LkTGpBKmhtPRVqNLnSFuhKKEkJT3bXNfRf%2B9vx1pjzYLvlkGzFyR6MtDoN273FcKbb9W7wNnxzwk6fnJNCXh1ConvrhR0LNP21xtGh4al9zJULDJfMnOOtWmywby%2FH9v1BB97ug6Qox4jAqDZudMCND4lL2BGhBnJqFLzGzia6Ojl%2BybkhmgEU1Muwg1UMg6UTbtHV0MruAFpazezVFP1wgmcYJbKUhHoEciVI6rT%2F0YN2xMJd4VOETBZHSY%2FYERFIxAG5WEqK8ehK8J0%2BupvuosE5jxDv33DteDd%2BGdqOpje4JgiyJjGGm2DZVoznKYrgBFcnDzwwzcX4vAY6pgHElyksTwZ%2FeTATc3n2lPSUxbLXnGOlJecaK5t%2BIyn%2FfrDLQSprBHqlsCu92Ceo1M7tun0xN4ETk8ZXuifWr%2FO4gWvIs3wmMnK5j5WL66a9GkD8ca%2BdAz1bZWjHZjYm1a2HPpikgC25W4IuxqRV0bGsJNT6WiRfbKV2n3anSh7%2BBHKaw3LC%2BiDbvzbrg0fa22XnUq1EsemZ5Ii6CRt2yz2qNlgee14e&X-Amz-Signature=c3398788eeb5a48dec28cf5a6fa45b23aa7d476c79d6ea59c2e22de9f42a37f9&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXUNM3Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhDycaKln%2BR9KeSdaWpeFyP%2BF%2FimbzMJWD%2BlwU9bfQfAiB5VmWEw09Cu%2BLNadKjsLQbgjhOrYMz%2FlRcEjtHQfvYECqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlhgw%2FBgvop9BrjKjKtwD%2FJ%2BAOWBcI3hCJJ0qeN3YelyH%2BVGRMLCqvVk%2BvOQXsTz1BnCcBqeMPOyO8g3%2BImZ46tsyOzHT6hffg9hIJWTnDLmoKqoaPYw%2Bbef%2FnzzoTJZUah2gJdTs%2BCuQqMOVJJppdcOy8J1oKLk9YbpN5%2Fk1MiDioB14BEKV01%2FyHR3XVA2K7sZfD2dL3brePK%2BsOOSZDzsglPx4wQdyBWIZOkJH%2FEkLPM1UmB0wSczTxjKUW4kxVcTiHxRm1N%2BQ3xsIBUkhKG4QrxjQzK%2Fn7kSwxHENfCMNz8%2BE7xvWNtkhrIonNPSxifIAP1LkTGpBKmhtPRVqNLnSFuhKKEkJT3bXNfRf%2B9vx1pjzYLvlkGzFyR6MtDoN273FcKbb9W7wNnxzwk6fnJNCXh1ConvrhR0LNP21xtGh4al9zJULDJfMnOOtWmywby%2FH9v1BB97ug6Qox4jAqDZudMCND4lL2BGhBnJqFLzGzia6Ojl%2BybkhmgEU1Muwg1UMg6UTbtHV0MruAFpazezVFP1wgmcYJbKUhHoEciVI6rT%2F0YN2xMJd4VOETBZHSY%2FYERFIxAG5WEqK8ehK8J0%2BupvuosE5jxDv33DteDd%2BGdqOpje4JgiyJjGGm2DZVoznKYrgBFcnDzwwzcX4vAY6pgHElyksTwZ%2FeTATc3n2lPSUxbLXnGOlJecaK5t%2BIyn%2FfrDLQSprBHqlsCu92Ceo1M7tun0xN4ETk8ZXuifWr%2FO4gWvIs3wmMnK5j5WL66a9GkD8ca%2BdAz1bZWjHZjYm1a2HPpikgC25W4IuxqRV0bGsJNT6WiRfbKV2n3anSh7%2BBHKaw3LC%2BiDbvzbrg0fa22XnUq1EsemZ5Ii6CRt2yz2qNlgee14e&X-Amz-Signature=5c84bb39f691187e28aae9315b7c3c5ef953b02ce358969fba64852d583c5112&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXUNM3Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhDycaKln%2BR9KeSdaWpeFyP%2BF%2FimbzMJWD%2BlwU9bfQfAiB5VmWEw09Cu%2BLNadKjsLQbgjhOrYMz%2FlRcEjtHQfvYECqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlhgw%2FBgvop9BrjKjKtwD%2FJ%2BAOWBcI3hCJJ0qeN3YelyH%2BVGRMLCqvVk%2BvOQXsTz1BnCcBqeMPOyO8g3%2BImZ46tsyOzHT6hffg9hIJWTnDLmoKqoaPYw%2Bbef%2FnzzoTJZUah2gJdTs%2BCuQqMOVJJppdcOy8J1oKLk9YbpN5%2Fk1MiDioB14BEKV01%2FyHR3XVA2K7sZfD2dL3brePK%2BsOOSZDzsglPx4wQdyBWIZOkJH%2FEkLPM1UmB0wSczTxjKUW4kxVcTiHxRm1N%2BQ3xsIBUkhKG4QrxjQzK%2Fn7kSwxHENfCMNz8%2BE7xvWNtkhrIonNPSxifIAP1LkTGpBKmhtPRVqNLnSFuhKKEkJT3bXNfRf%2B9vx1pjzYLvlkGzFyR6MtDoN273FcKbb9W7wNnxzwk6fnJNCXh1ConvrhR0LNP21xtGh4al9zJULDJfMnOOtWmywby%2FH9v1BB97ug6Qox4jAqDZudMCND4lL2BGhBnJqFLzGzia6Ojl%2BybkhmgEU1Muwg1UMg6UTbtHV0MruAFpazezVFP1wgmcYJbKUhHoEciVI6rT%2F0YN2xMJd4VOETBZHSY%2FYERFIxAG5WEqK8ehK8J0%2BupvuosE5jxDv33DteDd%2BGdqOpje4JgiyJjGGm2DZVoznKYrgBFcnDzwwzcX4vAY6pgHElyksTwZ%2FeTATc3n2lPSUxbLXnGOlJecaK5t%2BIyn%2FfrDLQSprBHqlsCu92Ceo1M7tun0xN4ETk8ZXuifWr%2FO4gWvIs3wmMnK5j5WL66a9GkD8ca%2BdAz1bZWjHZjYm1a2HPpikgC25W4IuxqRV0bGsJNT6WiRfbKV2n3anSh7%2BBHKaw3LC%2BiDbvzbrg0fa22XnUq1EsemZ5Ii6CRt2yz2qNlgee14e&X-Amz-Signature=d1cd39e78134bb374e26eaf7bd3851f2c60bc58851f79440a7282c61457dcdce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSUQY5YQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgCrjmXwoCkmm8lMRCoAqFJQgQd7mRmj6EUiSvK%2B6WHgIgCyDZrxZ%2BEADhKWsAJRV1kpUG2Wa%2F7G57i1v%2FlMl8odwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKge7xhSaRWfU%2BwHwCrcA84%2BzcP2Mk9N%2BY8kKrAUprLi3t9%2FbXWgQM%2F8OEq4qiTkgfRs1CJniFKhXGuLN%2BAayWoJRgwFVE72vOSjEtHu6mNPLRuNCc%2FPbCHa6VV7QvW85LtVCYOhGmsw16eumbt2rRPFHo3coaudZloAoPqoTuVU25Oh1OweMf3AKK5bUizI28bL07UmYM3p7agGGEiYWFj8FUZKyGtbk2JyoQxKk2lItsSY9RfClc%2FLAyRfxApvD9kbeYx%2F12KwZuHe4%2FxpCG1d6N%2BivSj4onDYmpIdJDwYLNiWVI3Bjtwq%2BkftrK%2FC2kywkwDiMciFLwxeCj7CSo6aCYJ3uggxaO7ffGuDvMzI6A2eKnBJaf7jtvxjqFHS3Pc8obD9c%2FYvLSnco6q9AcvJ1kncZ7W4yIsI%2BhRZY74SyAhH9ooWJHxX0IXglMKZaMyjzXg%2FG4%2BD57bw8erShTs834gpbR5v1uByBI%2BbbUF%2BR7F6ZePLOmoFwqAJ%2FaG4IGnJr%2BCIpXLXk%2FUO80aAtzoSlxXn1hm9MXxg0immEsX%2BhycvSNIVWxiVRaE%2FquQWfwyhM923XzW5R7R5jSy3rd%2BRKEazAz%2BYvooXsI%2B1P45dJRlUeGnis76tERXrfhycyUh6pI39UCx4U4%2FsMNLK%2BLwGOqUBne%2F21iGMmgD%2BLhU%2FSFMlXxEnPJBbzkc0rbdIifCKHJj3bgj1yw6nVhMHRYxqT2yhkpmRBYV%2FB6Z81ddO4AEmgQ6suHgcV64xNDl49K%2BEqUTzQow%2FLGQzp8JegsE%2FfgnnfS3REji1xHDJvdMyh4zreRlkF73W4ugiaXIA2HcDy%2F10lVNkfZBgCnDVb%2BbSbvk9hmz2lZGeTbd%2ByuiCz3fwAwMSlcY6&X-Amz-Signature=4b9f1b622ce59899dd729048ce53c42cdef37afea91bb40034e36218720d8b51&X-Amz-SignedHeaders=host&x-id=GetObject)
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