

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=30738f86b69230c0c4a181850228f5c67947db4b735dd063da36b424030afe21&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=c0736d4c99f736a03a120b0635fc821b2b0c6ef44cbf74e8d79d863e437af2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=e2065eed7a495a46f6eba1b953b075a856ac72edcb9ab673a74a018d51dcde85&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=3c6b0df32e0a395a51351ca8da3393fd489e9e2614c2cd2a440317a3b1a8194d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=5e499aa8e297e439043fca19bcd655b66f0abb6bc25280992f93c0e368b751e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=ceb016fa5a6d3ee47dd52d13fd02ccd5b9ec3a0f85a031f9008cd2bd7fb21b58&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=33c2cd87b0b4dd5aeeb9fb11a16c3017515eddcf5757b2e91a0a70b040d9a35c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=b63addd0024273a7a4a492e46bfc101e3ee3f39a14973ef33dc3517b9fe22138&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=bc637a02058d0a13e4bfe03f666ec66cf9de8ff29d888a9d3497b6989e26e067&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466724SOMRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIGk15cJwTMcdYE7fUT%2B02XeoOdCsgon1r3kU74NE6DIiAiEA3WqoinVTYaSQh3UyWP8do%2BNMVgL%2FzUR9G9JCXc7wkUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMNSsur2kPA7vx%2FAmyrcA24JZaIWqBjpkY8G4XCUvjcnpiAH%2ByQToIxt0cdgOlkjTxH81NAX52fVYrPaMyBlSdU6%2BSp8Ow9htb9z14TAYsdEK5DOezZ2Ei99niwoQP%2FSpmQkeiuY7HFeotxv10n%2BoqRXm95cgTMaYpFcDX%2F%2Bd19xMDsukhQlKIsxwdd51S0e9%2B%2FGOvUzl7MdbRwVvVyfanH2u05qPZZaMW2Aia6XMvXsAcaZG7JDFteMlwPYGLvciC3f0ijoj2wA%2BEh45geQ%2BFbzJCexU7n98xKOgJohF2qbx5249KvFeN%2BV1%2Fh2wbz7FA%2FU6z2XWc9pXWs0Un0MHxiOGIH38IkkPmibiyePBjinPGzUBpQ0voN8pntn9bXZe9KMJ8Gp8VQjQpLPEU5NBD4B6HhUrGabDJORubPHMqQSkbU%2FM0nrkRIDKO%2B54PZD1pxfMO4UrTKNeJbbhesuh5hf29giYGqTcUGqEfZTnc%2BC5lwPskmhWvx2uK%2BPtXxvTg1NRFJaVAEmfZgXroKBPZo%2BVK627I%2BiDS050reu6V2nXMbuUaUua%2BYHLWT69qTC4TjUw7Fvm3hsBTyq0qg9Tg1HRCqjjrZBXl9nnbifyxaFRyuuabe9g2%2F0mVDDsutI9X%2BXcJT7jRDhgsKAMIT8mL0GOqUBkD%2B0748G9qunJSTmLb3M6Q3Q5SXGvxdwC7KSJTV2L%2BQYSpEQWw1aFdHo05MFfCEKhHIJmrEmOXhp9MZHSWqLOjUd59Koc6wxgvxjQLpaU9ThB7I62JxJLkqWeAEdVKTvmZZr1p86bENBEmhRchx4W88TbshDUbSYFKv9GbmENrnyKyEXAgA8fwX%2FGE215VsFruYc%2FCXKRr7XDfOq0jAmqozoJF63&X-Amz-Signature=767480611197f5e4fe6e76c601c54ff3938c2b8d282b706310322f850d1852b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466724SOMRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIGk15cJwTMcdYE7fUT%2B02XeoOdCsgon1r3kU74NE6DIiAiEA3WqoinVTYaSQh3UyWP8do%2BNMVgL%2FzUR9G9JCXc7wkUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMNSsur2kPA7vx%2FAmyrcA24JZaIWqBjpkY8G4XCUvjcnpiAH%2ByQToIxt0cdgOlkjTxH81NAX52fVYrPaMyBlSdU6%2BSp8Ow9htb9z14TAYsdEK5DOezZ2Ei99niwoQP%2FSpmQkeiuY7HFeotxv10n%2BoqRXm95cgTMaYpFcDX%2F%2Bd19xMDsukhQlKIsxwdd51S0e9%2B%2FGOvUzl7MdbRwVvVyfanH2u05qPZZaMW2Aia6XMvXsAcaZG7JDFteMlwPYGLvciC3f0ijoj2wA%2BEh45geQ%2BFbzJCexU7n98xKOgJohF2qbx5249KvFeN%2BV1%2Fh2wbz7FA%2FU6z2XWc9pXWs0Un0MHxiOGIH38IkkPmibiyePBjinPGzUBpQ0voN8pntn9bXZe9KMJ8Gp8VQjQpLPEU5NBD4B6HhUrGabDJORubPHMqQSkbU%2FM0nrkRIDKO%2B54PZD1pxfMO4UrTKNeJbbhesuh5hf29giYGqTcUGqEfZTnc%2BC5lwPskmhWvx2uK%2BPtXxvTg1NRFJaVAEmfZgXroKBPZo%2BVK627I%2BiDS050reu6V2nXMbuUaUua%2BYHLWT69qTC4TjUw7Fvm3hsBTyq0qg9Tg1HRCqjjrZBXl9nnbifyxaFRyuuabe9g2%2F0mVDDsutI9X%2BXcJT7jRDhgsKAMIT8mL0GOqUBkD%2B0748G9qunJSTmLb3M6Q3Q5SXGvxdwC7KSJTV2L%2BQYSpEQWw1aFdHo05MFfCEKhHIJmrEmOXhp9MZHSWqLOjUd59Koc6wxgvxjQLpaU9ThB7I62JxJLkqWeAEdVKTvmZZr1p86bENBEmhRchx4W88TbshDUbSYFKv9GbmENrnyKyEXAgA8fwX%2FGE215VsFruYc%2FCXKRr7XDfOq0jAmqozoJF63&X-Amz-Signature=8a4ebf2ef8e552f5903eddcade068d6424d2d85a3daca3b126d52f47f7420c95&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466724SOMRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIGk15cJwTMcdYE7fUT%2B02XeoOdCsgon1r3kU74NE6DIiAiEA3WqoinVTYaSQh3UyWP8do%2BNMVgL%2FzUR9G9JCXc7wkUEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMNSsur2kPA7vx%2FAmyrcA24JZaIWqBjpkY8G4XCUvjcnpiAH%2ByQToIxt0cdgOlkjTxH81NAX52fVYrPaMyBlSdU6%2BSp8Ow9htb9z14TAYsdEK5DOezZ2Ei99niwoQP%2FSpmQkeiuY7HFeotxv10n%2BoqRXm95cgTMaYpFcDX%2F%2Bd19xMDsukhQlKIsxwdd51S0e9%2B%2FGOvUzl7MdbRwVvVyfanH2u05qPZZaMW2Aia6XMvXsAcaZG7JDFteMlwPYGLvciC3f0ijoj2wA%2BEh45geQ%2BFbzJCexU7n98xKOgJohF2qbx5249KvFeN%2BV1%2Fh2wbz7FA%2FU6z2XWc9pXWs0Un0MHxiOGIH38IkkPmibiyePBjinPGzUBpQ0voN8pntn9bXZe9KMJ8Gp8VQjQpLPEU5NBD4B6HhUrGabDJORubPHMqQSkbU%2FM0nrkRIDKO%2B54PZD1pxfMO4UrTKNeJbbhesuh5hf29giYGqTcUGqEfZTnc%2BC5lwPskmhWvx2uK%2BPtXxvTg1NRFJaVAEmfZgXroKBPZo%2BVK627I%2BiDS050reu6V2nXMbuUaUua%2BYHLWT69qTC4TjUw7Fvm3hsBTyq0qg9Tg1HRCqjjrZBXl9nnbifyxaFRyuuabe9g2%2F0mVDDsutI9X%2BXcJT7jRDhgsKAMIT8mL0GOqUBkD%2B0748G9qunJSTmLb3M6Q3Q5SXGvxdwC7KSJTV2L%2BQYSpEQWw1aFdHo05MFfCEKhHIJmrEmOXhp9MZHSWqLOjUd59Koc6wxgvxjQLpaU9ThB7I62JxJLkqWeAEdVKTvmZZr1p86bENBEmhRchx4W88TbshDUbSYFKv9GbmENrnyKyEXAgA8fwX%2FGE215VsFruYc%2FCXKRr7XDfOq0jAmqozoJF63&X-Amz-Signature=fb859004deeeedc70aa525ec6f52cdfd89e9596e2a64d95dbf30d464ce774c42&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=27de8a1be4c9396233ffa893681204dc69fab9b29d8228df03af7bf06372978b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=3ff586c47f4ddd43c816760a4a0fa46a7f414aaa490605e7902bc8ac5f27059b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=d4e029813a4bd80f9f6fd9b2cd797fd192b87a1c39cc0f926b3a4af75ec8a700&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=efd00c5bd40a580e727deec838fa0a5cf798a79cedc9083f7fbddc2b8451ba2c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=1dc80444a31cf935ec4b3193ea9355d9e6c05e1b737ae3bc0cfc1b29c21067cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEPVYHZ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDzSR4G7ZSD%2BY0ArbMGbirPGJfvjYrK4wo23GtIHnkEAwIhAPCSGI3%2FvYp1J%2FPE9VY6MFJN6sSeGRKysd3qjQvX%2BiVhKv8DCHoQABoMNjM3NDIzMTgzODA1IgxMvoxwTDgCLoJBAQQq3ANFOg4%2BzgRT1vdptPGfJ4IgvYIiGIIM6iELykUnnkmkGanSs86zm4KjORJ1LXCqEzBC2IKSGxbSsWtqyRopCajr0sTD720BvFDLYQgM%2BGQt43c6lyOcNH3VsAqcTC92EEPpo%2FcLEfbBWmCi3oUv%2BEr6sXJdYpVrreNXiHBj8ClA7UBxR8uDYh0AfBhpEPYamPC4FtamB5%2FlsEOcyjWvJBppwKUVMgmacEvhAvmb8%2FY0B3agc%2BFEx2Vkj3DFcgkBPOvi%2FhlVNHhRpJsPQYFnYdhXpiBZwCrrLkBAFn02oNDkFh9ksGpP7u5V68Hy%2Fh%2Bt7linXBbHhDrkwMUGeRNPyNE1pqc%2BOeamyJbDEU%2FZ6b05XF%2B4Ax9iTiIy%2F8hFLDFPTbVtZv3SKBmZzzyha0k3hfUtifNnbgaYGXEc6aIChnVO2i%2B4rtIsAPnZ2JTOkHMzCcBufGYe4d9gYe3yyMXJeHIX6kvQpvhaioXttJPJQYqdL3tY7KKL1fcbOWOpVQCBvNd%2BDaIFy3LVA4U00omQMSbxMwVnaoVBqkQ%2F5WN4%2Bim6WSsNf30nY9DXU9A4JifmisW7BJRr5C5smv0AQnnINtsbVDSsOH%2BW3OlcsUrSlGf0N8%2FBYUpNlWVwPCDOyTCi%2FJi9BjqkAe65N3Llo8yBH0aqUQAVD29p%2FrdT7wuCYyeAr1GRMQrbRsJDh6tDd45Zy%2BlnDkqaSpMhmKBjRvmR7J1%2BEAOVPyIog%2B8eOTklYHgJjGPXYFtVNzc5cjAVH%2BgExMScplg0m8oS2w4AJtxakqliTHE5ZCDjig%2FpiRbnEWUe%2BaLLCThLOqemKCarwl%2BB%2BJc6AWkOVyJQOByuWiWgU9RgoOmyo8EIeHEx&X-Amz-Signature=89d08dfb95a59c06d24a28c1cda04e1aa46ae595a7c6f9e0ba747a889da427f3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AU5NF3F%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIELlzifwxxLfKIm%2FaFTEey2TgI7PykzpTsp10dDvhUt%2FAiEAhG%2F9vEnkohM5dM4BsCDTLAANNCshLsygJWq%2BDbJDUR4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDD9Nh4hJ8iDKnBSv9SrcA5a%2Bwnwo4XYpP%2B3QrfFUEJXInPpvJPxOHwAfbM9XrtHoCy64gQ4D4plm9hnB01kTA85h4tPSeIP%2FtJodu6OMpjPqMS6tXH8u7LppWjkhhHOKlL35BX5PlNb35cy9t7n7de6XrIEJA%2BrH4EpWnyTBp52CSnOu4p8xxX4GxFoOD64WF397gSuCm9waa1vpxQR%2BJQUxeAQ4c54iBbGgPX%2Bf55CGs3J8pE9RZdWVehdggF23E3COs5IqYkpODHSTPma66rbyIA3LPIfNG%2B3t2YENKvwDMYGvtjdBOdNmyKq%2FfLV2GB3dMe4UYXR23SzcxoKtJHDaHN%2FouyWfrlvBcwCMVqFJsYMPnbG6dHC8nvPg3KWo1ecPP6y4o3UWQ8ONAG0Oxc3re4E0bxf8BbPzL2Ub5qmt65yB%2F541ieNv%2FGcWaglVLmnXxlgQbbQf%2BAVpqoPwdzdf%2BL1EFQM9ZXNIWdZzntyozM72JpeGCiUOLk%2BgiyJKAA7fe7CZdF4jtlimdyq4Z3USV9XKIH8%2FGxiXVpayz%2F%2FiIoJwQfki9s5OPocGf88NdpNQxYIUun19EB9XkNlYof0FuWkNqfjyi7SyG7zlpGy2pZ8r%2BVOzBvUUWA34d5tXAsnJCdxU7AlxDRZXMPL7mL0GOqUBpm2cJFJQ1ANx3MuT%2FVGmzw0w504gsW606jjZVllbwdo%2FnGNOGik76vxPLXTB6WVeDEBZZHQied9so69xtxg4xMxk2zm5wL8wud7QVQP%2BzVKeAhIHXnAtlnmB6RgZe5gqmR%2BKOr7HsipEWLutvCeSCAcv%2Brza5SFVsOXRFIYh5jHL%2FT%2BF3KPSYlDuuIAC2Zf9%2BXa4hmavITU%2BaqQMpnxdxEEogxQA&X-Amz-Signature=25cc8df384cb65607c65ec3d349ef892baf78d8b755bcb2b5a59d10b5fb0a146&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AU5NF3F%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIELlzifwxxLfKIm%2FaFTEey2TgI7PykzpTsp10dDvhUt%2FAiEAhG%2F9vEnkohM5dM4BsCDTLAANNCshLsygJWq%2BDbJDUR4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDD9Nh4hJ8iDKnBSv9SrcA5a%2Bwnwo4XYpP%2B3QrfFUEJXInPpvJPxOHwAfbM9XrtHoCy64gQ4D4plm9hnB01kTA85h4tPSeIP%2FtJodu6OMpjPqMS6tXH8u7LppWjkhhHOKlL35BX5PlNb35cy9t7n7de6XrIEJA%2BrH4EpWnyTBp52CSnOu4p8xxX4GxFoOD64WF397gSuCm9waa1vpxQR%2BJQUxeAQ4c54iBbGgPX%2Bf55CGs3J8pE9RZdWVehdggF23E3COs5IqYkpODHSTPma66rbyIA3LPIfNG%2B3t2YENKvwDMYGvtjdBOdNmyKq%2FfLV2GB3dMe4UYXR23SzcxoKtJHDaHN%2FouyWfrlvBcwCMVqFJsYMPnbG6dHC8nvPg3KWo1ecPP6y4o3UWQ8ONAG0Oxc3re4E0bxf8BbPzL2Ub5qmt65yB%2F541ieNv%2FGcWaglVLmnXxlgQbbQf%2BAVpqoPwdzdf%2BL1EFQM9ZXNIWdZzntyozM72JpeGCiUOLk%2BgiyJKAA7fe7CZdF4jtlimdyq4Z3USV9XKIH8%2FGxiXVpayz%2F%2FiIoJwQfki9s5OPocGf88NdpNQxYIUun19EB9XkNlYof0FuWkNqfjyi7SyG7zlpGy2pZ8r%2BVOzBvUUWA34d5tXAsnJCdxU7AlxDRZXMPL7mL0GOqUBpm2cJFJQ1ANx3MuT%2FVGmzw0w504gsW606jjZVllbwdo%2FnGNOGik76vxPLXTB6WVeDEBZZHQied9so69xtxg4xMxk2zm5wL8wud7QVQP%2BzVKeAhIHXnAtlnmB6RgZe5gqmR%2BKOr7HsipEWLutvCeSCAcv%2Brza5SFVsOXRFIYh5jHL%2FT%2BF3KPSYlDuuIAC2Zf9%2BXa4hmavITU%2BaqQMpnxdxEEogxQA&X-Amz-Signature=c50940a6c6079da7c83a530aa7d37114db7b172f66f56cc28b84ed8d59a4d200&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNJI7AVH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIGQTAKskk0BTTOfPyt%2FQpTLWiALi6HOGStGVazrM2I9gAiAU9jedimobjVxAZYirkHu8IDYZ5Uj7z7rUnRjL6Ba2Jir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMOw5NDP9Qf4XqotE3KtwDXNUey%2ByFkJXlFBuvylxvzYvpxneUjVFAk3NC0eLOt5QsYB95n%2BEpEX%2BpbSWCMbFKG2v59crKwMPAJ393eeQJLTFqV9oIMqMu8QJAQlzCqi2ckykvaGMOzGPZkjV1kvkLXGNrSDTHaWvEjJs1vEH92Sg%2BSGDue4M20TZiboLXQdV1WmRekEK2TWDlDWLHK3RrZAVnhYcS61%2FKv2geOqlZMPqtswchzHTJBqLPLX5m21%2FvQglLZNArMqnVnpudwsaRaBv2dgl6F89awpSo5wqwQ9JJaCFkat9%2BFggBUXn9TNA9MEBdoC3%2FycsT25yCKT7aDV8d%2F6RcG1bUTMVfYGrMJ%2BHrFwwpGnFPj%2BWDLj4Ws5M2c%2Bs0ClT9vDJNVYe5x%2FRauWvmzJ9Ru6I2Ci1IHKrT8uosUeibsgA6gpt%2BQ8KhLGqBkYQDBfWpAz6rEpTepQ4OgyQfKeCRFwtIQdTg6qU%2F2BlqBhypT9qSQcWl8aCd%2FFC%2BmonrnUjQAMgUU265zg82lMrK%2Bp9%2Fxa4ZLyYq%2BtC4hYzMy2Y15w6uoBmuhQmZvtTXnpFZlnLV2YpS56BLJWU5tatLkjE6WEsyxhEYlYBfOcK%2BaV1vP8PWjMiBNfOY655JNuOwmaVxGaoUQyQw8fuYvQY6pgG8zyMvZ8ahC5lyBxPhARO65HddnqTWbjo1IUamBgBT2Q0Qw%2BEjwMknSd5h%2BaAlx58Ums674lUJWrWOahITZrfnjaWUMkdrmHfS7tJiY7AofPTrFNNyMCCxEPylRoxYwYAOXITlmAQhCwdoGFYXnHoRVguL6u6WZ8jZDOgaSy85Su0sLdP%2BgA1RMao%2BZTZ0oQ%2FKsi4zywcoB4ayDDN2YgVCSg%2BMB7cP&X-Amz-Signature=ee83d5092957ef20b8b16f7987e7dd3934f340ccf03b6a0612ad0bc823608322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KR7BFQG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICO6NYP64yTBEcNXOgHoB4O5l%2Fa%2FvspCYD3AL8u8vaUqAiEAzau3BRWv7%2Fgd%2BWiIA7bGTtKzUQBzKoHJfSGG6XdXoU4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDCLBn91Jfjp910v2uSrcAylkLLqGZRKxDfW91wbtEx7hWyjPPAhdZcERKwnh7GBM9LV9QihS2WMZXtm7InWyWQWBChkJWvX9qBxTWC8J7nXfgW6%2FIzeqZu4G8%2BatDa4%2BcO1Xfzq7MVTUrmJF86wB7ynSOcsSH%2BQH2pmMezMW%2BL0kVavFUehOU5%2FfgrWT9JGfP0mwEvBJ6oPRuMlyDjmzz4f3r7BZpRcAu2V5qDcReZrZpFUn3PGkwvqDSTL97t7FMDETA6HH2Fzyif%2F9s8KOEbPzNlGY0UVSFHFCJBWdrM7NuMB9PYrFoxkOqHG1ArxRyD8%2BsX1%2F4vB%2FONq6Qobd1TT4zviPNvw4p%2BtSAonWQOq3rXeV3yXbdeH%2FtDxI1zzJaMeygy8QGFJe8Pvtg6DbWvxwabqTtEpVBnbtWTAckhZDV6ujNq0vcQ05lVUsFZsiLoS3kil12qyAL7nshAGtWzfQaV%2FLcem%2Fi%2Fq4M6tCMvaPbGYleyp1sC8KhUk6TJLaU4yq26sr3%2BG6GPcExZuctKoKvNTFCdxkG9Y9QLxsVKQueNfDxRgjqZ5TjuhiJ8aQtBGp5GuFGGtUV%2Fg86vYrSIAtf1GmeB%2BGUV%2BVppS%2BZ6xCYJ0VHUo%2BLg1UluwZjC1JLiqBqUU55aCbftBYMMb7mL0GOqUBWOVfr7hmLTr%2F30%2BgtHQ1XswJuBJxVA%2BBNScXWFHCZcn1T9ye7Ymh7ijq4JysUSVXrR%2FnHnOnXeWxO1%2FMwxy8Pjogt1OimQtcM80GEFtDFZLhuU3zDiOSDIeXVGnE3POZ47SbfqUu%2FOMtuQATFE4QJ%2FbBlzwPcprLQ9M6Yy3Hd%2BIH1duJGGMwmGA2HOQfHR2cdn5ClcCDCo9nly28e6M0ym2gfF%2FB&X-Amz-Signature=a4f6181b8545bb71b8c6fbb8356047e1519255abd16d3e4bcaf8258ebe169718&X-Amz-SignedHeaders=host&x-id=GetObject)
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