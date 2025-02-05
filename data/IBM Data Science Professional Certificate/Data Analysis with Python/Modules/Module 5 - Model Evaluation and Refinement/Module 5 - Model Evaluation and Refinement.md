

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=b6667505d9f2a0f312f71bc3a408441eb32349cbad733b37c69c5392fed59da1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=98ff3d31bff0bdc3d53b842fe008a206697e72428eb61be063baf5ba518fbce8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=96d09530e316294b15b843378daee2fb5921b5a85cc8e7d5c9c181c4fe57d1cc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=728f9387f34633ed364fbb8f5b1fef0e0e2ba258731f4697bd28cbf51eaece93&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=57261b9922873531c2fa80512bbd8d586666cc18c400cb07248b718ecf3e864b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=8646c78d49fa71ac65a4324162d1fd23c194ef3f46e0db4923a0acef410e7573&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=0c59b665be3e31311788727d5f20f641b42e007a5d462b7a9862ca2780c91ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=b991af477a9148dea8cea11197e15e627a3fb05004f189d1b8087dfa32b6d5de&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=4e3c31803243460e65f364e6789e1b1e0b52319c77ea59aa98aeb0402b7db30a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5PXYWFJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD548lt1w8%2Fm7c57BOSJmCMd%2BLOlrT%2B6BXa3J7PjW9GYQIhANUO6nTIsYdj%2BaXuO%2ByuRVcqZ%2FQ4SK0O6v2b5I9f9MgrKv8DCDkQABoMNjM3NDIzMTgzODA1IgyzIP4PTBxDnajEvBAq3AOA3TxrTUl7qZDiydNvNZWV%2Bx%2B8v9AhxmvpiBOFEbdtpXDR3ju30V%2FIATozJCmKBYHQTSnRm8Kx0sFqvd1XCgdX5SfQIn04jW333ESqZ2QvMrABKKVoYrj8Kf8xpARS2%2BlpfYjHDbkD2QPe1O7dh8YPPq6I4XLlxa1SWoKe3xHOs1vOK541PgFQKoCIpIQSfkhvrEFZuXAaTss6YCP4%2FIchO2%2BUthjg6IHIb04A%2FoHPdcGP0dU3aFxIcvGXsmX%2BLC%2B7Fn79dJk%2FukDvt9waITkYcuXhE%2BXCrBykZ%2BlxCVAFXgty0KuWu3%2B55G%2BySWpmMwdJgZ5u9DJWj1Lb1rHq15EoL2Dn%2BcimNIxUs%2Fsl9Tk71Qf%2BVKy7dP5TgYUvt%2FXbOTJkb2QaqjzSO4xaSmzcPiFC%2FP7q0wmsQ2%2BAYpLmcV47my5L%2Bv4a2j2nAQZRlOP7Hk8oWddcECReIip4o%2B2kAQG4Bnz4nVC5KUjnWBeB6Ytln8lDS8ChsdwJVlDfq3iGbQ5RA%2Fkxfn5ZArElYauD5n1%2FuRVJKYcFp%2B8Z3SNL0Wf6OR42Fgk7R0TOU3a4OuhyIoJKCmZk0mJS%2FAdVe5EdDW7a4qMroG3xuBXMcVZT7lU4HmMy5ucOCmtpr%2Fy%2FTjCkzYq9BjqkAVgwTUK6Gk1Q7F6HnduVUgKGYpo1hKp85hALiNQOGHSJ8DmZQlXzfJtpXwSkKF57LyCX63CKXDwAit9HoPMyRAVwkaVBNSy4V7FGPOjlw9wfwPP3JSz9BivYmaCiqKIuw9eN8Xc1oWT6FelUz14nzqT%2Br4xLgJBNNK40eyEC2B202Oi7yEinEWOddie4uDSEmEALMlBifV3HaTtGoy%2BB5aXAo4El&X-Amz-Signature=0b6268971f1621c93ea4708ee03541852a499cfa98dd6b853a5b0c985425bce8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5PXYWFJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD548lt1w8%2Fm7c57BOSJmCMd%2BLOlrT%2B6BXa3J7PjW9GYQIhANUO6nTIsYdj%2BaXuO%2ByuRVcqZ%2FQ4SK0O6v2b5I9f9MgrKv8DCDkQABoMNjM3NDIzMTgzODA1IgyzIP4PTBxDnajEvBAq3AOA3TxrTUl7qZDiydNvNZWV%2Bx%2B8v9AhxmvpiBOFEbdtpXDR3ju30V%2FIATozJCmKBYHQTSnRm8Kx0sFqvd1XCgdX5SfQIn04jW333ESqZ2QvMrABKKVoYrj8Kf8xpARS2%2BlpfYjHDbkD2QPe1O7dh8YPPq6I4XLlxa1SWoKe3xHOs1vOK541PgFQKoCIpIQSfkhvrEFZuXAaTss6YCP4%2FIchO2%2BUthjg6IHIb04A%2FoHPdcGP0dU3aFxIcvGXsmX%2BLC%2B7Fn79dJk%2FukDvt9waITkYcuXhE%2BXCrBykZ%2BlxCVAFXgty0KuWu3%2B55G%2BySWpmMwdJgZ5u9DJWj1Lb1rHq15EoL2Dn%2BcimNIxUs%2Fsl9Tk71Qf%2BVKy7dP5TgYUvt%2FXbOTJkb2QaqjzSO4xaSmzcPiFC%2FP7q0wmsQ2%2BAYpLmcV47my5L%2Bv4a2j2nAQZRlOP7Hk8oWddcECReIip4o%2B2kAQG4Bnz4nVC5KUjnWBeB6Ytln8lDS8ChsdwJVlDfq3iGbQ5RA%2Fkxfn5ZArElYauD5n1%2FuRVJKYcFp%2B8Z3SNL0Wf6OR42Fgk7R0TOU3a4OuhyIoJKCmZk0mJS%2FAdVe5EdDW7a4qMroG3xuBXMcVZT7lU4HmMy5ucOCmtpr%2Fy%2FTjCkzYq9BjqkAVgwTUK6Gk1Q7F6HnduVUgKGYpo1hKp85hALiNQOGHSJ8DmZQlXzfJtpXwSkKF57LyCX63CKXDwAit9HoPMyRAVwkaVBNSy4V7FGPOjlw9wfwPP3JSz9BivYmaCiqKIuw9eN8Xc1oWT6FelUz14nzqT%2Br4xLgJBNNK40eyEC2B202Oi7yEinEWOddie4uDSEmEALMlBifV3HaTtGoy%2BB5aXAo4El&X-Amz-Signature=155e0733f98982500b0de3441ead51293093257df2acae41406c166bbf8b39c7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5PXYWFJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD548lt1w8%2Fm7c57BOSJmCMd%2BLOlrT%2B6BXa3J7PjW9GYQIhANUO6nTIsYdj%2BaXuO%2ByuRVcqZ%2FQ4SK0O6v2b5I9f9MgrKv8DCDkQABoMNjM3NDIzMTgzODA1IgyzIP4PTBxDnajEvBAq3AOA3TxrTUl7qZDiydNvNZWV%2Bx%2B8v9AhxmvpiBOFEbdtpXDR3ju30V%2FIATozJCmKBYHQTSnRm8Kx0sFqvd1XCgdX5SfQIn04jW333ESqZ2QvMrABKKVoYrj8Kf8xpARS2%2BlpfYjHDbkD2QPe1O7dh8YPPq6I4XLlxa1SWoKe3xHOs1vOK541PgFQKoCIpIQSfkhvrEFZuXAaTss6YCP4%2FIchO2%2BUthjg6IHIb04A%2FoHPdcGP0dU3aFxIcvGXsmX%2BLC%2B7Fn79dJk%2FukDvt9waITkYcuXhE%2BXCrBykZ%2BlxCVAFXgty0KuWu3%2B55G%2BySWpmMwdJgZ5u9DJWj1Lb1rHq15EoL2Dn%2BcimNIxUs%2Fsl9Tk71Qf%2BVKy7dP5TgYUvt%2FXbOTJkb2QaqjzSO4xaSmzcPiFC%2FP7q0wmsQ2%2BAYpLmcV47my5L%2Bv4a2j2nAQZRlOP7Hk8oWddcECReIip4o%2B2kAQG4Bnz4nVC5KUjnWBeB6Ytln8lDS8ChsdwJVlDfq3iGbQ5RA%2Fkxfn5ZArElYauD5n1%2FuRVJKYcFp%2B8Z3SNL0Wf6OR42Fgk7R0TOU3a4OuhyIoJKCmZk0mJS%2FAdVe5EdDW7a4qMroG3xuBXMcVZT7lU4HmMy5ucOCmtpr%2Fy%2FTjCkzYq9BjqkAVgwTUK6Gk1Q7F6HnduVUgKGYpo1hKp85hALiNQOGHSJ8DmZQlXzfJtpXwSkKF57LyCX63CKXDwAit9HoPMyRAVwkaVBNSy4V7FGPOjlw9wfwPP3JSz9BivYmaCiqKIuw9eN8Xc1oWT6FelUz14nzqT%2Br4xLgJBNNK40eyEC2B202Oi7yEinEWOddie4uDSEmEALMlBifV3HaTtGoy%2BB5aXAo4El&X-Amz-Signature=f32756257cd7804d252d93c44d7a31c276d786926bdb6f6785617b13cc3e1ea3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=aae93b87559aac8cda6ca0aac7ea97558ad4798efabb05faca116ea0c772b749&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=0c4857ddd5c145baac725ae031967bb4f97f65508ab6bb513337da8621f30dae&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=0cf5d68ac6a645f9a2bb323e0e18e2bc412755a53e5a1a98cf4db97e1cbeda45&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=0d6b1675582ed291e0e6e0ee20b3775fc1b23b10c20730dcc97c49b43d7d3c1a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=d6f7a05b3e5f32c5fab6e0580f80b4afe7e8fd90a1316aa6e2ccbcc890c61688&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7OKHBFM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIEiajMIp6ug1JVlYsxf%2BdfUURRLbgxn6D6%2FTWmy9yK8ZAiBq6%2FOjOxXrNOdjGtnYEgnmLobJJDG30VJMreHM0MjLxir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMqDY7P1rI3qFEqqZ3KtwDsRZcSYUeT1AWpF6TIVkWazvRM9iUycWv%2Fshw58%2Bod04JDBqbqO1znZUPYRAGTI2VPsaygd6AGAW6w6gMHKAsranUNj6qKu1vMpVZBjuc8Jai0CwqTmRkXqIOiNIMOH%2B7AE1rv6owLQQappLT8dgDIpnbdyviWXSSmjuUwtWQjFXDtvd3Za8hvMuP00gKanVCCybgZBNbE5yrWg5F8kRTC%2BAmpKm1ln6flkQSOQgz9petyM3Bu9%2Fp7aA%2F7fXwSyabgPhOw4%2Bciy8I%2FszZbsp6f88pi2kyFg0umLI8LPusIdiLyJcr2ZQCtAjqPazTAnDtRi3nfITV3acZHTyObyl6df%2FAuz1diiidw2jUfJnhq30REAZuwTGT7BOGHWgBLx7tlUfYuSqVGi%2BNFHiBf8CQR6nXurO6XNWSr3v9vUOzdiBM78A93tLDLCSzhUGkgldjJAvSD1D7UdV5GeJHz0s4fqnGBaI7xtPFi7FQYUCoo79WpZqUfYbPwustA6qAbrjZvolTG5kW5xSnjLnJ9UhavtjoCNm15mNawCs8qsmt4baIGwr09w95fbWTdaASLLgtLREsweuhmrXRxngYsOPbz0Q2x4ejKw%2FXMSsHRIEEYlvlEgAmrcML1CKvhbMwpM2KvQY6pgFrsZ2NQ7B1J9o%2BuUzf7qfuzLy8%2BwgnnNQU5oN%2B4Vt3dBNCTkrgyUHuBWWX6mYcakIqu%2F%2BlCZv66c0ZLiC4o%2FsKoTOANDP6NGgph2q6rwVa9TZo1MB%2BfxhM2KUxH0L8%2F5u12kKzfoAxfr7QSHiGuyTbxmFQntOzvj2B44%2Fg%2BpNYixbNkeXoq4GevZBZJitb%2F6Dk7n3h%2FEtLxVMKCzIrRNDS4Z%2B5yEPM&X-Amz-Signature=8b5537c68cfd358650f8d1e1b6c228241df632650f7c2230870ad79df7fac43e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDVGJTZD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIEOqfMb7qvTCQ%2FlmUQv6bv%2B1PkmPM%2FhggMIZW%2BUnirs%2BAiB7cwThgnNQtwZtn7W6KmWWDcPmaGgBdfvTDWgTyj1ziSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMrnDeEli8jWrj2O1FKtwDEQMOVTMvHekJ8jNTHhIXR0WiRfzOINziGAOcMpNRT4TFicFACulMgC%2BenlT2Apg6SeinM2vOyk8jmIa2WbuQFWSZ7Q7eMqnvDUG0srPMWR1P3r0oMFZrEizqnQqs2Mf1jDMtsuday9%2BO1d4co0nWglRGJf25L6e4otf3bJTx8y2OxV1nFJ73XtSY%2BHj5gLSF%2BoJ97JoGI89Wg3V%2FRXzOXwTcYJD%2FRs4yKpWScGExJjICAUfkK4Yq%2BJ6eHir%2FMvH3V6dWjxtIcyzknlwRxj0rblbcQ7uGkfAdwpjqckmtHURzigzkV9BSOfyXdcIwhM%2B71edr%2B9nj4EtTXw5RH7V9vBs99vF7BLRC86pfBeFzbB4ml7GJ8aHTi7UNQsxpHWhSOnKNF6vlGsu1fXzI5bMgv1Ta1bJKyF8lZp1l6GLmEQ3v5c0l77HLxRaDWtIIzfi%2BqXd00hr5zbK1EywlmQn1LU%2BZZroIAooI0gwzGs4jXKHpzjdJuRoZ%2FZCfcgsysEdflPWDsw7%2FO87yskTZO6Un477MHCw48zHlaBw9%2B99yMhofhvbiLx8CukyCDSLQCU2LS17tXQx%2Fe8ThLVlcDQbTDKfi4FU3iiPI4m5VvDa3MEOwHWM%2BfVuJ9pvMSl8wrM2KvQY6pgFo9uldTsOS92vDjOfnZvId%2FxKxoDiVuAa7Kcjmi377GbIn%2FP%2BnImwgUVdwbu16L5m%2FSlP9Pvm%2BAaMN54VXh3SEYKC4gU4mpzRY%2BJA311ydoM9pG1VDlCKROWddSL5naWtIPvn4nInnQND2JraVhgoCKoC4%2FdaaRhF2CyYBBiXamHXRKMlrek%2BKRiRT1BBKrSzfX67gNyXmpY2F1A%2FIuNIbSeZaAMsy&X-Amz-Signature=cd013fa945c4c8382e68e2a3a5433966376289257aa74e317ebedb77b6c9ed71&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDVGJTZD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIEOqfMb7qvTCQ%2FlmUQv6bv%2B1PkmPM%2FhggMIZW%2BUnirs%2BAiB7cwThgnNQtwZtn7W6KmWWDcPmaGgBdfvTDWgTyj1ziSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMrnDeEli8jWrj2O1FKtwDEQMOVTMvHekJ8jNTHhIXR0WiRfzOINziGAOcMpNRT4TFicFACulMgC%2BenlT2Apg6SeinM2vOyk8jmIa2WbuQFWSZ7Q7eMqnvDUG0srPMWR1P3r0oMFZrEizqnQqs2Mf1jDMtsuday9%2BO1d4co0nWglRGJf25L6e4otf3bJTx8y2OxV1nFJ73XtSY%2BHj5gLSF%2BoJ97JoGI89Wg3V%2FRXzOXwTcYJD%2FRs4yKpWScGExJjICAUfkK4Yq%2BJ6eHir%2FMvH3V6dWjxtIcyzknlwRxj0rblbcQ7uGkfAdwpjqckmtHURzigzkV9BSOfyXdcIwhM%2B71edr%2B9nj4EtTXw5RH7V9vBs99vF7BLRC86pfBeFzbB4ml7GJ8aHTi7UNQsxpHWhSOnKNF6vlGsu1fXzI5bMgv1Ta1bJKyF8lZp1l6GLmEQ3v5c0l77HLxRaDWtIIzfi%2BqXd00hr5zbK1EywlmQn1LU%2BZZroIAooI0gwzGs4jXKHpzjdJuRoZ%2FZCfcgsysEdflPWDsw7%2FO87yskTZO6Un477MHCw48zHlaBw9%2B99yMhofhvbiLx8CukyCDSLQCU2LS17tXQx%2Fe8ThLVlcDQbTDKfi4FU3iiPI4m5VvDa3MEOwHWM%2BfVuJ9pvMSl8wrM2KvQY6pgFo9uldTsOS92vDjOfnZvId%2FxKxoDiVuAa7Kcjmi377GbIn%2FP%2BnImwgUVdwbu16L5m%2FSlP9Pvm%2BAaMN54VXh3SEYKC4gU4mpzRY%2BJA311ydoM9pG1VDlCKROWddSL5naWtIPvn4nInnQND2JraVhgoCKoC4%2FdaaRhF2CyYBBiXamHXRKMlrek%2BKRiRT1BBKrSzfX67gNyXmpY2F1A%2FIuNIbSeZaAMsy&X-Amz-Signature=78732b393eabcf9ef1cecd36db1112ac9b0c11b39cb059deb352b6ec8a1830c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=5a1c7b13043f367cceb9f0ebd7fcd595daff9d5690774185c7418a6ff3f1b92a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HUACAQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDbCHe06v7hEwmY76%2FmVWaVUemljcBgUXfF6p29VXQ%2BLAIhALUqOj49zoATaLpcdDE%2BeINHWLzvmOoEpaIw4ow4Kb3zKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEMuAm%2BPPm8X4j%2BwQq3ANqprjtPmM9wejU%2FDFbMjjWfoHG8DwMs92FdYr13birK4lDp7SV4cDsobS1OmvmaPGzquKdJViQfFLTJlTwJWX3Lrif7eHWKt2Nf%2BeB7v91IUJKWY3YzS6gqJp6NzE%2BQ5%2F2s5wk3FI%2B9raA0iSnSWj3pBVEwp0XuG7SnslSo4o6RELHSa3iHWmc97a0wQ%2BveAlvLwWRC560Yma5kbf316XPST6MXGCLaoHkSHOEttR8sdI45eBm8hJZGdMEKEPPGNRLCVRy4YxK6Njwb4Rz%2FCq7UDjm5UQRd2%2FSWdpp51v59iDD1CV2gVy%2FCQCxqN3ZT3sY2cyQY8V8YKCaCxZzPP%2B7LMP7yQgOyfF1X3IXW2RQ7QAew6x9KNo5TtAaZSAkgG7iIHQs3MhmaRZukGC1jX6vqV0%2BtXvAIgOLmnWb0whareN%2Bs8V7C7%2BIsrUlXD4ouLK%2FX2Q%2F7rZ4tc8mqatYvWLTkUlnp%2BqRThPN9dPu6Pp65Nrse7WOtOJdGXmhzHBjd6os6Vl7P9i%2BvCnJ005UiqzXgpGYez3x%2F4oh74AWdluPYe5NYQ%2BlBlr%2FmwUz0%2Bj2y40x%2FgOWhMvmeeGOfg%2BEg%2FG0%2FvTlbl6ADzP9XKSXKy2MkKYJUXaAChZgGAoAkzC8zYq9BjqkARoQophTb9TOvSXL8tEXYAbdWPBdQHtgQojqaY4Tf6cSuFx%2FLUDWriE138yL1MJujVAVujl6Ve3IeXp9BidwWyOKlBEiV1ZpUNIbxAhtlqfCKIzKp0N0w0qmVrypcysw5LxBu2w854EW7%2B2CeF6k7e7r2cobiB5jz0VQg2cNMm%2BOjvJcyX9OUKmD4PKjr5BnMMO3FC0ABdDks%2Be0%2FFmm7y0QHH7X&X-Amz-Signature=a0e23a6a841975ff0c76792d2747789586ee9017236b91cba567f140b5e9e914&X-Amz-SignedHeaders=host&x-id=GetObject)
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