

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=8b5e11078f4930744122ccb484b8aed096ff2af724cdcc3b38a5a85e0576ff6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=c76d57d017d942f3ea81d3ce66d52894a832e1639f54917e53017c3e32b8a6cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=0b82b599675685a7139400a2b36851aec763447637743c828111ebe7cc96595c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=d0156e368b01142fdaba3dc613b8639ae2d186ba563ec0fc4cca430089482094&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=40079f089fa7ab65d0d563f5f9175bf56a86212e5ce20304e647fe435d736b7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=72374b9367358834ebe5222e3f5527416fd0ffbad434f710add96d4f35725a41&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=ca407ad507bd2b9cf108f5dedbe5146c13121f2d6e3c4297e6ace2dd8d80d083&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=28427134e5c66c0265eea3471619cae7bdfe8dc9070d83e8e17a7ec84d5528f8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=4253407c907be04d18d99246ff66ee9cf5caf559496d2504d30d33f52a0bd0f6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KXY2AD7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEaOpWZq%2BC0jLt6FK3BI9dPbNVLNdp6Bji11Ehjt9rO3AiA1PkAvg3W9tQT8f1gMVRuDxbgevVBwDKft9wI0a3csmSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUcztUwApT1j%2FNghaKtwDx4YBFttPehSvqUFCH1crBB4FPHdcsW5ygGyVbFnxPYYRhSbtOd23Qjyem3ImTj%2BfvIEgd3bHRD0ei98u2ZQMUcMlTE8NXf8K%2Fz%2F7IoOwU494tvsbThU7hm7068QLRgBHNLME1uPHOzeHCtPnyZIxzx3y%2B%2FVcUkaQaQPxCOYxQDySQRlDPSVYeXSKQjIIIho7IXhMjZn2UJ2ZwxxoAwvfUEki7A03TNfNIRcNcqMh57sE79amssoEgpakor6krRPA0e4ML3MZsKvTEn6BQPeOMzcB0t7DH4SvPKWGNXEqiYU479s0KUdOa9PKSvTeiwsmUvY1X2nkzvDmEAYM9UxZM64vbXpxKt1Z7U0SP0J7xnoSkAHIFVtdUQDU8bNPkV1dlhpMyrbCUgvh1vPHYe%2F1vwTZAefgIXgj4W9DE9TofYXZ0Z96gRx9owrgNs3KE6WU8G2MFOtNt%2BX%2FJnzL4xFXq1oKZjho9brZ%2BGLMiT6sH7sh9Vgbso7EDzAp8ReupjFrNC%2FcD1%2FpXenq%2B5DmOjvhpOyVaW8ydPb5n4GkOB9kzLTfzb72okQdodtJNNYRKwuwMfRuXvTS%2F2gEs1VggbbLIucGdroxRNt6tpMszaOdHtpo%2BuqED%2BgkUICnV2gw5qT3vAY6pgFvKtd2JcKGnySTv5n8ACjwL9%2BDKO3bcff%2FYzsrfcNUU3Ow1jkpY%2B23NQYnVvk9QuaTHEnVFqRCzgQylerKa1MMjzCEs1brtdtIG%2ByNV0NAcs6TVxAs8ztAUXp%2Bwf%2BAt63%2BGD5CBKiJR6Ex%2Fb0I7yp4tQGABzknXFeX%2Fo0a7zE9iOJVD6NTdW77A3dOjbk8B5%2BbGsAkpPP3DgxKVsXPLpIw%2BW6dEmyQ&X-Amz-Signature=b2d50e65706427d24c52a60aaa8f0a6a290842ce091560e220c37b5708b86450&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KXY2AD7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEaOpWZq%2BC0jLt6FK3BI9dPbNVLNdp6Bji11Ehjt9rO3AiA1PkAvg3W9tQT8f1gMVRuDxbgevVBwDKft9wI0a3csmSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUcztUwApT1j%2FNghaKtwDx4YBFttPehSvqUFCH1crBB4FPHdcsW5ygGyVbFnxPYYRhSbtOd23Qjyem3ImTj%2BfvIEgd3bHRD0ei98u2ZQMUcMlTE8NXf8K%2Fz%2F7IoOwU494tvsbThU7hm7068QLRgBHNLME1uPHOzeHCtPnyZIxzx3y%2B%2FVcUkaQaQPxCOYxQDySQRlDPSVYeXSKQjIIIho7IXhMjZn2UJ2ZwxxoAwvfUEki7A03TNfNIRcNcqMh57sE79amssoEgpakor6krRPA0e4ML3MZsKvTEn6BQPeOMzcB0t7DH4SvPKWGNXEqiYU479s0KUdOa9PKSvTeiwsmUvY1X2nkzvDmEAYM9UxZM64vbXpxKt1Z7U0SP0J7xnoSkAHIFVtdUQDU8bNPkV1dlhpMyrbCUgvh1vPHYe%2F1vwTZAefgIXgj4W9DE9TofYXZ0Z96gRx9owrgNs3KE6WU8G2MFOtNt%2BX%2FJnzL4xFXq1oKZjho9brZ%2BGLMiT6sH7sh9Vgbso7EDzAp8ReupjFrNC%2FcD1%2FpXenq%2B5DmOjvhpOyVaW8ydPb5n4GkOB9kzLTfzb72okQdodtJNNYRKwuwMfRuXvTS%2F2gEs1VggbbLIucGdroxRNt6tpMszaOdHtpo%2BuqED%2BgkUICnV2gw5qT3vAY6pgFvKtd2JcKGnySTv5n8ACjwL9%2BDKO3bcff%2FYzsrfcNUU3Ow1jkpY%2B23NQYnVvk9QuaTHEnVFqRCzgQylerKa1MMjzCEs1brtdtIG%2ByNV0NAcs6TVxAs8ztAUXp%2Bwf%2BAt63%2BGD5CBKiJR6Ex%2Fb0I7yp4tQGABzknXFeX%2Fo0a7zE9iOJVD6NTdW77A3dOjbk8B5%2BbGsAkpPP3DgxKVsXPLpIw%2BW6dEmyQ&X-Amz-Signature=b6541c72a2eaaf83523a42205e2de538d2903983439df96431d1956f52e11e5c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KXY2AD7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEaOpWZq%2BC0jLt6FK3BI9dPbNVLNdp6Bji11Ehjt9rO3AiA1PkAvg3W9tQT8f1gMVRuDxbgevVBwDKft9wI0a3csmSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUcztUwApT1j%2FNghaKtwDx4YBFttPehSvqUFCH1crBB4FPHdcsW5ygGyVbFnxPYYRhSbtOd23Qjyem3ImTj%2BfvIEgd3bHRD0ei98u2ZQMUcMlTE8NXf8K%2Fz%2F7IoOwU494tvsbThU7hm7068QLRgBHNLME1uPHOzeHCtPnyZIxzx3y%2B%2FVcUkaQaQPxCOYxQDySQRlDPSVYeXSKQjIIIho7IXhMjZn2UJ2ZwxxoAwvfUEki7A03TNfNIRcNcqMh57sE79amssoEgpakor6krRPA0e4ML3MZsKvTEn6BQPeOMzcB0t7DH4SvPKWGNXEqiYU479s0KUdOa9PKSvTeiwsmUvY1X2nkzvDmEAYM9UxZM64vbXpxKt1Z7U0SP0J7xnoSkAHIFVtdUQDU8bNPkV1dlhpMyrbCUgvh1vPHYe%2F1vwTZAefgIXgj4W9DE9TofYXZ0Z96gRx9owrgNs3KE6WU8G2MFOtNt%2BX%2FJnzL4xFXq1oKZjho9brZ%2BGLMiT6sH7sh9Vgbso7EDzAp8ReupjFrNC%2FcD1%2FpXenq%2B5DmOjvhpOyVaW8ydPb5n4GkOB9kzLTfzb72okQdodtJNNYRKwuwMfRuXvTS%2F2gEs1VggbbLIucGdroxRNt6tpMszaOdHtpo%2BuqED%2BgkUICnV2gw5qT3vAY6pgFvKtd2JcKGnySTv5n8ACjwL9%2BDKO3bcff%2FYzsrfcNUU3Ow1jkpY%2B23NQYnVvk9QuaTHEnVFqRCzgQylerKa1MMjzCEs1brtdtIG%2ByNV0NAcs6TVxAs8ztAUXp%2Bwf%2BAt63%2BGD5CBKiJR6Ex%2Fb0I7yp4tQGABzknXFeX%2Fo0a7zE9iOJVD6NTdW77A3dOjbk8B5%2BbGsAkpPP3DgxKVsXPLpIw%2BW6dEmyQ&X-Amz-Signature=c248bbe2ec68ff35f9111dd0fcc944c969f256314d769c93a95bbc0d6ddc283c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=c8d4403d6d5b10f2b7e4b4fd75b4f2b2a872110fd2094252ff2f0c4a12cb6ae3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=db67ae43e3100a41eca0f7f24044fab370b8b0c1fd5b88393aac8cbb96f287ea&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=89f0c819f98e716ce2727adfe22341596e75a5dad81494a52dafc04941f4c174&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=91e01899de323a11ff845ebbdaddc5bb864b40c08f0caab38ec70bfe3ac5ffdf&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=b314ea7fbc45bbf22dd8ce4684e5ee8c15f6fea44fadd9a61ec9221812be71df&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV5X3R36%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICnv1XJMFWpa4BpdC%2FaqKucH7lWNr37IZn5ysu7%2F%2FdOZAiBWho5i%2BhZOhEAGimiNW9KNylCVsnSfyIT0bDCoOU%2BQXSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF25meQ1V5CxFKvBTKtwDlltwaevX%2F7B2IcnIEljRJnS2YvnB53kdVLLWpvWIokkzt5a8Y4AL%2BhcpbpGnNJ8XrsyVM240pwGFx5H%2B64CdblqQTpqBKXb5lJHZSRqnaMaZaY377jMXDsiA%2Fc%2B%2BsDPGu5ENfQb70jJIRQoo5ePV8RoYWcrOijsXMTkFYVnLn1ZDwYs3j19hz9eVJwdT9bHtvSuNJLpmfTXe9wOIp7Y782fyucLRfi6a%2Bufkn5Vr2%2BLsaRK%2Fvh1MGk67qZiNTJNDXG28iruQvwyxOFG%2B75%2Bl6bOp6BvOH305gXP1RAT7Rdh932XJnN%2FxYtZUoQAYfxa6xOExS8sHcaNINFjvC7ka5ODK0ikj%2BHALnZjBid6ZsvZ21nCX2TchcphCrvZF2N1RIVnV3UpT9xhl%2FtVpZ9fACHKe05Jlls4%2BumjwDtS6DE6KIm%2BTAkUJGp%2BG4p%2FIiVghrNv3D6oCELwBzXRmazzWXKGzYRw1s22k2zCmPmmV3UwRkF16JsdLGvIA5cxBzfHRSbSbkRf7wyh5pm68r2snSUDN26JIWNvSX8VqvoMgPSMWfPiuZ9eTpih6dMgnE0bkmAEGfqIqwNuQF1RMjnpYaHrdstxCF9%2B%2FFzogt%2FVpjsR6bDt06kwhX17FjI0w5qT3vAY6pgFHUsOnRvshACwO%2BgMIzlK%2FEL2cQu1OOnjgI%2FQph2adcAYTWjHeC3%2BTw3%2FqT9ifPRf6S1gWyE1mHzp4xetLFN%2FeT53SInPNA5VWK5ERc%2BOZGRAQvw8TthoQhcn%2FEUd%2F6WtHL%2F2C8TURkPitNec5wjtatDJ35j0uMajT%2F78M%2BFQ%2Bk8cRUJNuZ%2FcKFm2UT4UaASkhyEM2GXCMFhwy8I9%2BK5unTdsSTDOx&X-Amz-Signature=1fd3ac716b80c70a702782917ced233b990906e404d3060397c7d6dedd6da129&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UYUUSDV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBe5rWJS5jjM0Y7rWU5hbc5IBCUrNEnLP0uloUgrafEtAiEA39jPorzmaEN%2Fk1geaZdkLn6am0g9igzrAEd2H94QdSYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBMZF5kRy%2BPc5tRHyrcAzxPlM7spcjKfYjnuxyZf%2B%2BrQsTsWX4PJSCcWrsImnmZSgbbCRM4JqSZSEeFIsvySEMSQULniMCU5Vjkiq%2BqKpPv4exh2WbkYMTfEVmTXtOcPHatrSTGT4VDZFSUNmIk4gwtw8CImHg7hpxqtO2fAJ3CzgyLYNmnuh57XJg2Jw1jW78XvvoXtSo7ykB5VF8v%2FHEw18xWYWrSUUaz3v%2FXrouwtj31FgElY9qxuT%2FI%2BNsWvHeK0QT%2BmhTihaCvaF6yYm1jF62Hq7vErWgoKYlOd%2FSORxMIGItvYdkUGXx5MOaM%2FPeO%2B4FvCawXQIhtqys0X1hRPfNp3yrFgj%2FWupDWycuF8tv9DWrZqr3G08wB7AOgAHPg25CaSrugXPDXvLL%2FL6PFP9HwD7oaaEZg0Y%2FcOm3MBk4vYPXTPl3dnE2Mzdm9Cg8fuKWboco8B0Zmmakouhwl04wajgkc8jsDqQENKaOob0kOprZAEE8mlphOn%2BFu%2FV6ZZtziMkSgNrJBbGwfS4CovwIzWgzVOlk1F6AX6hloFcTxwrWC6d3Wqh%2BccMYJ2yQo2GMb7y8YVhHMHTAVJbluko4TuXGdU1SNPTX2ED66BoI7Q%2Fdgwldt2A3VZW0sX7ahRZFip8mybEwcMPfN97wGOqUBv5QrgRkScvXrk%2FaglKuhXWuhPiOS6knkiH75EbN46YpDuHHVmPopcC3%2BaqVM9ndgc2x3Kmcbeh1sVrKpYHh0ambrPau3mZgevOZv8KyAvqPIPXj%2BofMLwWqB395nw2QMfgLgV%2FWObrOIWlvFjAZ9bGFEXd9DdOgwZ6OWVJ5QQvzYWIFYeAQKXLMOijgaxaI7QROP403jCbgs9wheJSVnfoBOx4JG&X-Amz-Signature=edef8d96f66273e42a494a426b2ae35482cc93f0aa07f8e02da99564c9176c2f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UYUUSDV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBe5rWJS5jjM0Y7rWU5hbc5IBCUrNEnLP0uloUgrafEtAiEA39jPorzmaEN%2Fk1geaZdkLn6am0g9igzrAEd2H94QdSYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBMZF5kRy%2BPc5tRHyrcAzxPlM7spcjKfYjnuxyZf%2B%2BrQsTsWX4PJSCcWrsImnmZSgbbCRM4JqSZSEeFIsvySEMSQULniMCU5Vjkiq%2BqKpPv4exh2WbkYMTfEVmTXtOcPHatrSTGT4VDZFSUNmIk4gwtw8CImHg7hpxqtO2fAJ3CzgyLYNmnuh57XJg2Jw1jW78XvvoXtSo7ykB5VF8v%2FHEw18xWYWrSUUaz3v%2FXrouwtj31FgElY9qxuT%2FI%2BNsWvHeK0QT%2BmhTihaCvaF6yYm1jF62Hq7vErWgoKYlOd%2FSORxMIGItvYdkUGXx5MOaM%2FPeO%2B4FvCawXQIhtqys0X1hRPfNp3yrFgj%2FWupDWycuF8tv9DWrZqr3G08wB7AOgAHPg25CaSrugXPDXvLL%2FL6PFP9HwD7oaaEZg0Y%2FcOm3MBk4vYPXTPl3dnE2Mzdm9Cg8fuKWboco8B0Zmmakouhwl04wajgkc8jsDqQENKaOob0kOprZAEE8mlphOn%2BFu%2FV6ZZtziMkSgNrJBbGwfS4CovwIzWgzVOlk1F6AX6hloFcTxwrWC6d3Wqh%2BccMYJ2yQo2GMb7y8YVhHMHTAVJbluko4TuXGdU1SNPTX2ED66BoI7Q%2Fdgwldt2A3VZW0sX7ahRZFip8mybEwcMPfN97wGOqUBv5QrgRkScvXrk%2FaglKuhXWuhPiOS6knkiH75EbN46YpDuHHVmPopcC3%2BaqVM9ndgc2x3Kmcbeh1sVrKpYHh0ambrPau3mZgevOZv8KyAvqPIPXj%2BofMLwWqB395nw2QMfgLgV%2FWObrOIWlvFjAZ9bGFEXd9DdOgwZ6OWVJ5QQvzYWIFYeAQKXLMOijgaxaI7QROP403jCbgs9wheJSVnfoBOx4JG&X-Amz-Signature=7f60addc193ddc0f9e053cb9a1a09f07044fc6561920d1dff28d2dad016e407a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NHLDRTI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGlC%2F7MrQBGRynVMmuyzIRFvSdjyppaYtIHF34NM%2BNaGAiEAlP%2FIHvGTJtEpIfZFZWqj3sfddLNRlV0ZeIBNDXAoo0IqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCi7xsRLkMQR5GNwFSrcA6PQuLxyVOM9czOsn6m5yG37F2%2F8Cp0pQdKk4DGxDL5NMUVpmZYg68BIaDupJxzTZaTpMCA%2FDd7QXHX%2BtziCfQ2lb3sxzA9Xidckkavt%2B00Cz8WKP1VnYnS2E0L8iYfnPx%2FpVW06h0QNqskLyR%2FIy2lgbRmvoGkpVqiGFIi8aD25xSHuHO801289KP5fcxsMD7AUz%2FkaaTnME5ihD0qF%2FBtl%2BG0zfuh%2B00dc69nzsFsbeInpQzx8tNfyn1QAEs%2Fa%2FU6k2sRXZLi2x%2FicQulQ154C1uACTYBI5DjJW36nYFMD5gFEpkfdjQoplA3V8C7Mb4qea1mc7AwBt4zMWFlFwKvpJrCbScH9lmZQldZ5u5LNOhWjYQ4StXX6XIQqpPo7BrE2qU%2BIeuosv%2B7rvGQz1c1j%2Fmc%2B8xnQCqsgA%2FFsR45Vap4ne6N0XfMjI%2BcgDr9UhlpMMQHh6k63PrsN3XiyxGM2FbX6VMJWi1V4JJVMNhRmJCPyKdPpeCKARumsm0NAA01V4QiEp6sDC7WS3Mlw9pP3rOaJw6XOJyEUR%2BqeEGLV2yNv1Zg6ebbSlHpKLJf49kFFiJ4rtkF29rIBJRYpO6PflCsucl8KVg6UuPXisQR%2BJr%2BV29rPQgHVoFriMMCk97wGOqUBoXvZC6qev0HOwjw98Egd%2F2%2FWfkzOFyTXt0lnE%2FmTz56FslutgOECNyqOEaRsm7jQFT%2FJMM1%2FshbfvWCkTvGCjiI8ji0flXNtJ4PcelvRu%2FGD%2Fd2dkTn3WAEHzMcqyf7UefzG9OrhfWCOCbV%2FYWUePHgw%2BNlZc2Xzdg7QZ2aAWU8AFM1%2FCOcPQfW0DqH9DiK6XxEQNcPdFEyMMbVWvi7D7K3ihK0W&X-Amz-Signature=a6687d1650f9f512dfc2eaa8fff284c0eaa0ba450c4094571a7c1974d23bd945&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=6208d2216131df6817ec65336470d463f24de223be1802bfb9f6408c3b2a5369&X-Amz-SignedHeaders=host&x-id=GetObject)
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