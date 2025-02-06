

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=cbcee08996de4020e465796ff1012a659d1c92606d9acbdeb8379027adf9ba68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=a4981bdb39c0db7146a568bf5fb2a2867ffaf517e72d98426412592b3761c311&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=a1ba385ec2d278a8b523a4d056c39837c2af4bab3fd8dbfa78506ecb9c863c00&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=62cd703ab3931b879670ace48d2775af73dba43e6b72eec3d2b3f6885d04fa87&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=f49f8ce683927b93187c849236336011cf3216704f83b119bc1e52040f58d771&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=e9db13c52dacc3d335358493481a1225780c627e422622974ef8f90d791f6e5d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=aad269e7706f280e65ad0ff4dea7ca05d5c46e46405d5f9152030599909727bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=6df1390c2eb617efd31fd3da4722666014c5d60493a99d931a3ab43fffff00ec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=5055f4a37fbcbc319131fe1f4c11b0598f49e6e0981ddbc52f47f608c9733b43&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5VP7VF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDcsG%2FPz7VZV2D1BD7CDrMgOh1c3byZHh6qj3MZaKkU7AIgJIoO8FnyU8B3IoduxWQFtQl93uwrGbe9yWG0UzJ3taAq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDKCaoWsdc7BVlmqk1yrcAziO%2B%2B%2F3lDWn5jUePyq4tN3awppHiskFzX5hhICtv1ZPKwYd1G%2BWEw9Dz2YIHgHuZxIGTDXmKzgH2IvOa3sRooGOLfd3x1tlEBiIfGU4u06j0N%2F%2Fmf0Cy%2FK5Ldoios0y0DbUxliASUptSA%2F83Mt3ksCC78ZYAepuR5wA8AuTa8wEheup%2Fw9TtvSuzag5TE9bQMU5SQS4GtRiX%2BWOxnO0IoWRi2Iv9yEeQ8QelmgwmL0gX1l2%2BLWmkuAlG7hkT600M0cH1%2B9CBg85wLO0VfkuRD0do3YXDGb6G%2BY%2BPlRRDby2zd0Zea4tvBjQbTJQz%2FoJq8OGr5EqUrjwo1JSObk5CeGGWjjMmbY5vbqTlN6QhrEDzmKxuYtDxibDAE6sM6hpt6hQN0Y%2BZlowY884aeQ8sHzBvS%2BFLEoDYE44RK9Swjcst3Zz7zOW7F46WPwnPp0GemVNDD1HcCBro4cEQHLq02ZpaUEqVkq5247NTDyXvRXNrrImuOCDhlJlKpM%2FSult6NB1f6%2B9rpFzSeOlkECgOx%2FN1kr%2FjHEdAAqSAn6cFtW3zvhPJwyCmJ0WkShOfiV2u2ygeLnZcquXffetAbe345HFmAfkMD5PqEv1lNhLfX039YALh08AJXkkKrCyMM6Zkb0GOqUBKGHUmofWHD8VeVgeP9CHk9D1xPfGc5LLAIA19YgY%2BYRnhhdCxIMqyyYoWDg%2BkLTyU2P51Ow4kQj18LDrYZPiroGJsFtWcJlfSbXqTndMfAxmIwkSJzn9XIKy3mdZIR%2BnJzpTXTjtCmbcZIrRiSWW3degGvnzB849olnVDST58Av6xaZmiu%2BBXMMYAvxcYiFwIRu4MGhCUV%2BMa53mKwsXkQA%2FoG%2Bd&X-Amz-Signature=6e98505843c1633c8a3c25036733ead86c8f41530bcbfdede42c1eb3fbb83a03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5VP7VF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDcsG%2FPz7VZV2D1BD7CDrMgOh1c3byZHh6qj3MZaKkU7AIgJIoO8FnyU8B3IoduxWQFtQl93uwrGbe9yWG0UzJ3taAq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDKCaoWsdc7BVlmqk1yrcAziO%2B%2B%2F3lDWn5jUePyq4tN3awppHiskFzX5hhICtv1ZPKwYd1G%2BWEw9Dz2YIHgHuZxIGTDXmKzgH2IvOa3sRooGOLfd3x1tlEBiIfGU4u06j0N%2F%2Fmf0Cy%2FK5Ldoios0y0DbUxliASUptSA%2F83Mt3ksCC78ZYAepuR5wA8AuTa8wEheup%2Fw9TtvSuzag5TE9bQMU5SQS4GtRiX%2BWOxnO0IoWRi2Iv9yEeQ8QelmgwmL0gX1l2%2BLWmkuAlG7hkT600M0cH1%2B9CBg85wLO0VfkuRD0do3YXDGb6G%2BY%2BPlRRDby2zd0Zea4tvBjQbTJQz%2FoJq8OGr5EqUrjwo1JSObk5CeGGWjjMmbY5vbqTlN6QhrEDzmKxuYtDxibDAE6sM6hpt6hQN0Y%2BZlowY884aeQ8sHzBvS%2BFLEoDYE44RK9Swjcst3Zz7zOW7F46WPwnPp0GemVNDD1HcCBro4cEQHLq02ZpaUEqVkq5247NTDyXvRXNrrImuOCDhlJlKpM%2FSult6NB1f6%2B9rpFzSeOlkECgOx%2FN1kr%2FjHEdAAqSAn6cFtW3zvhPJwyCmJ0WkShOfiV2u2ygeLnZcquXffetAbe345HFmAfkMD5PqEv1lNhLfX039YALh08AJXkkKrCyMM6Zkb0GOqUBKGHUmofWHD8VeVgeP9CHk9D1xPfGc5LLAIA19YgY%2BYRnhhdCxIMqyyYoWDg%2BkLTyU2P51Ow4kQj18LDrYZPiroGJsFtWcJlfSbXqTndMfAxmIwkSJzn9XIKy3mdZIR%2BnJzpTXTjtCmbcZIrRiSWW3degGvnzB849olnVDST58Av6xaZmiu%2BBXMMYAvxcYiFwIRu4MGhCUV%2BMa53mKwsXkQA%2FoG%2Bd&X-Amz-Signature=6b0be2fc2bdda3cb22ef8fc32412f35269b610381fb0e024acd5762f6194937f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5VP7VF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDcsG%2FPz7VZV2D1BD7CDrMgOh1c3byZHh6qj3MZaKkU7AIgJIoO8FnyU8B3IoduxWQFtQl93uwrGbe9yWG0UzJ3taAq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDKCaoWsdc7BVlmqk1yrcAziO%2B%2B%2F3lDWn5jUePyq4tN3awppHiskFzX5hhICtv1ZPKwYd1G%2BWEw9Dz2YIHgHuZxIGTDXmKzgH2IvOa3sRooGOLfd3x1tlEBiIfGU4u06j0N%2F%2Fmf0Cy%2FK5Ldoios0y0DbUxliASUptSA%2F83Mt3ksCC78ZYAepuR5wA8AuTa8wEheup%2Fw9TtvSuzag5TE9bQMU5SQS4GtRiX%2BWOxnO0IoWRi2Iv9yEeQ8QelmgwmL0gX1l2%2BLWmkuAlG7hkT600M0cH1%2B9CBg85wLO0VfkuRD0do3YXDGb6G%2BY%2BPlRRDby2zd0Zea4tvBjQbTJQz%2FoJq8OGr5EqUrjwo1JSObk5CeGGWjjMmbY5vbqTlN6QhrEDzmKxuYtDxibDAE6sM6hpt6hQN0Y%2BZlowY884aeQ8sHzBvS%2BFLEoDYE44RK9Swjcst3Zz7zOW7F46WPwnPp0GemVNDD1HcCBro4cEQHLq02ZpaUEqVkq5247NTDyXvRXNrrImuOCDhlJlKpM%2FSult6NB1f6%2B9rpFzSeOlkECgOx%2FN1kr%2FjHEdAAqSAn6cFtW3zvhPJwyCmJ0WkShOfiV2u2ygeLnZcquXffetAbe345HFmAfkMD5PqEv1lNhLfX039YALh08AJXkkKrCyMM6Zkb0GOqUBKGHUmofWHD8VeVgeP9CHk9D1xPfGc5LLAIA19YgY%2BYRnhhdCxIMqyyYoWDg%2BkLTyU2P51Ow4kQj18LDrYZPiroGJsFtWcJlfSbXqTndMfAxmIwkSJzn9XIKy3mdZIR%2BnJzpTXTjtCmbcZIrRiSWW3degGvnzB849olnVDST58Av6xaZmiu%2BBXMMYAvxcYiFwIRu4MGhCUV%2BMa53mKwsXkQA%2FoG%2Bd&X-Amz-Signature=ed88d381e10c5aec8efd47544e5b2873156ae6fa9cd1276d969a8fdfef186af2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=938afb4875bb8348a9575943411cf2d710bec0208026bcde966100772b17dcc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=ee0aa17326b5f226f3a538d8e190226e0262e1f197503021e9f4b33fab577908&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=8386d7f4d8acb4a49c4e857ba9363bb5488f0475003acbd1167043ff8aeb56bb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=0d30b40526bdba24e50afee5cfb1b0e70450d56b37228895eabdd70408cdb582&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=83ea4ad4d923732404655e554ad681b7bffbf664b5a636880002a2a798367a93&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DQ32GDZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCCBG%2Bu2M4t8mXSkircTgnXsjEbgktAR8TrEql%2F8f8u9QIgDdCJhM3lrNnjCQQ%2FupKkQ0zdziwdRr3UloZV%2F%2Bnpx0Aq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJ7326HKGWz8A%2B%2FvlircA96Aq%2FczPYFARUHzISKJMZUpQbN0g0qvsTxTadSvcSs%2BQq2xS8JuFj8H4SItMS6b%2F74V33qhvar7uyBBCKvz%2FEeznlB62rCwcxlxYu1ognWpTWTdJ8P4qxxBHb1FGsT85ABq55%2BSviHE1u06yTnE8wRTTiXTRM498jXANRQo0B0rhKijRk9946zV58ZxgAN%2Fd3T6PSCwSQPNu1XRE5QUX4WzinqDWHk2Zb5g1ybqKS%2BmxQUHVROpYXagm%2ByTbgWshUVKkbxU3UjcvhDnAEVObrnmRf%2Bd6rsAMnz46%2BfBHi2l1gVWOWkcoJJO%2FTAAWNoH65YSmGPtu6ZYZd4%2B%2FG6IUHa3eGLUmGxsJxH5ksLsmaxxl9r4t6AKB84c2436znsIygr1wU6wr0zh%2FgrJDgMBB1taAE587GgEhcYBpp4UXAifyAPSluasS9AwVoZ5zQC0lD8NH%2Fmgaxh1Jkc%2Ffb2E%2FHbnfd4ofnOTPDszihe5%2BatrfS8dg6QlJX3FqsVSrVLUJrZqYxfDm3HZh66k3hQHOJXz6EQpjKJDgaL2Me5e2nJAdEc4Fy1tkfX3HCAE3hDgr7NisoBzNjOOWMdwYWlpnaN%2FzmjWrQc9EoXuV1GDH6oUN%2F%2BvNo8x3VARFXUQMKuZkb0GOqUB%2FjKVON2rbpAgRgc24CM7%2FhHcT1xnmnYY9of5%2BHhx6e26g%2FlYU4soi4gpiAIeQI9MmGk50rAoleochdmB2Tb6cjTLTu3lP7MN2drvUeOC1J0xAW%2BGWdK187vyl7vqlxS%2F14CzjQKWHaKRYefn9RwpzYbl23HruDooabcXejUkysMhn%2FJkt%2BkA4yloPF6VeDDkgrLBwBv3fRlJcnEKAbxKsGVRd5K8&X-Amz-Signature=a606cb47b7da3d825dd1ce59227f3339a92c3a15d968a1b05e2b2d6c03bf5a46&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OQKZJ52%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIB8nP6J0zJu8ZcPjObuhUWpdt4CZ%2BqHxt2OF7z%2FHastUAiApsVyryR4XEhbJQY1qTFbbGVrMe6i3NVGOn%2Bu9GcE01Cr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMVhyv%2FX7N0GGYIDeiKtwDHfouJRoDCUUJ2%2FWSuKCB1YkZHy2Uj0TtNUAe0pMu94Zef6bMWLO0LShZNS%2BtdJaw4jWIoqBNz%2Bik5Zt8oacyL3xLG73kqLmevQ%2FmrhivgT4efbJZ0urHq5WdikP52Ei3khIwMHm6nTfuZvEdh4KzsRMBtwccwVxmQDQbsZgbIy6VXsjtI5AeJhOpKEq5V1A949HzikJ9Gldk8VuxurdCuDBOR9gqaF8qJgJkcaSvGNdd5kZBgQqdHBegV8DwIltuQUW7fWidKTQy%2Fg16anBy0erffqlDF1%2F0S4lr7LgaId9egOTL%2Fjv%2F8RY3DV6dt0%2FB1riVNmGv0IhPOlf8VuDBbyQh0EVpplzVBn7ScZ%2BqURicmojuvn3RIDkhV5TjHCZx%2Bxed4K8tw0lW2hYQbWOtGK%2FuMwxbXJNSahRqT67JzTMSEe4C8ISnGg5uVijHAJHa5Rg%2FyJqDypD%2B0zwYRGruuiV20gnkklzRq3PDEGCdbNyBbBdpGoC2sZyQ0c0Uk3J9oJ69qVzC9%2BlC1PMj4gnFviHnKIqxetDInNmtLScUtuB7gXYU35cgE29OamtM0fZEh4RpbkGRjh%2FR85Uyrn5Sj73QbL8tVHI7stWqx0btf4CEHKG%2BU%2BAbRl1szpcwqZmRvQY6pgELRhGx7JNoIZWEZqki7543%2B7%2FuZxMvXiEhrvOoyD2y4JFM24B78OHjuYy%2BIkuVHYccdZuE7K4%2BJzMtffemBJa0rs8sPGh41k8vvhDrhxgb8cHU7bBv%2FP0VBlEiBFgkLec2yViohDB3Vm7Pji99mwfZ2rzoH%2FXyPT8tNgTIbwEb8YAe6oZjxaOfm2EI3w9%2BOQnnsQcpacvTAv7rGntint28zrJVbqPP&X-Amz-Signature=71df4c85e70ccc74ea64888412026ad6b25e2d960e13619a94beba134bacaadd&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OQKZJ52%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIB8nP6J0zJu8ZcPjObuhUWpdt4CZ%2BqHxt2OF7z%2FHastUAiApsVyryR4XEhbJQY1qTFbbGVrMe6i3NVGOn%2Bu9GcE01Cr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMVhyv%2FX7N0GGYIDeiKtwDHfouJRoDCUUJ2%2FWSuKCB1YkZHy2Uj0TtNUAe0pMu94Zef6bMWLO0LShZNS%2BtdJaw4jWIoqBNz%2Bik5Zt8oacyL3xLG73kqLmevQ%2FmrhivgT4efbJZ0urHq5WdikP52Ei3khIwMHm6nTfuZvEdh4KzsRMBtwccwVxmQDQbsZgbIy6VXsjtI5AeJhOpKEq5V1A949HzikJ9Gldk8VuxurdCuDBOR9gqaF8qJgJkcaSvGNdd5kZBgQqdHBegV8DwIltuQUW7fWidKTQy%2Fg16anBy0erffqlDF1%2F0S4lr7LgaId9egOTL%2Fjv%2F8RY3DV6dt0%2FB1riVNmGv0IhPOlf8VuDBbyQh0EVpplzVBn7ScZ%2BqURicmojuvn3RIDkhV5TjHCZx%2Bxed4K8tw0lW2hYQbWOtGK%2FuMwxbXJNSahRqT67JzTMSEe4C8ISnGg5uVijHAJHa5Rg%2FyJqDypD%2B0zwYRGruuiV20gnkklzRq3PDEGCdbNyBbBdpGoC2sZyQ0c0Uk3J9oJ69qVzC9%2BlC1PMj4gnFviHnKIqxetDInNmtLScUtuB7gXYU35cgE29OamtM0fZEh4RpbkGRjh%2FR85Uyrn5Sj73QbL8tVHI7stWqx0btf4CEHKG%2BU%2BAbRl1szpcwqZmRvQY6pgELRhGx7JNoIZWEZqki7543%2B7%2FuZxMvXiEhrvOoyD2y4JFM24B78OHjuYy%2BIkuVHYccdZuE7K4%2BJzMtffemBJa0rs8sPGh41k8vvhDrhxgb8cHU7bBv%2FP0VBlEiBFgkLec2yViohDB3Vm7Pji99mwfZ2rzoH%2FXyPT8tNgTIbwEb8YAe6oZjxaOfm2EI3w9%2BOQnnsQcpacvTAv7rGntint28zrJVbqPP&X-Amz-Signature=8ce6aaa43b713dfb927975c92b1a6c8743b25c85e73b01cfc0421a4b9eb709cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CPSE73X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCUzCENc%2FLVNhL%2BJ%2BvoRxrtrfHw1HnNmu63oET3HFiIUAIgc32UA4Jx7iN8aCSacQhidJTbncgwcAcdxJg24XM0oGgq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDCDxt1V7Y%2F0%2B66UheyrcA5YUTAC2tvmhpZsgLN2wWT%2Br1YnfIkSZ48To0OQ3S5fsHyRNt1m%2BlZWNuTtkV1mk1oWBcldneFtxo5SFJKV6vSE8%2F6l9EVzfYZK0LL7Os87WIwjGfpn1%2BPBjLRAoVoXbshVCZx5dYGURauWimIIi6q%2BzLLgsV7chwaHFtTTDpHIJHPAInu9p%2FxHcuxKRhsJAN6YDxunixQewu3pPsrGu%2FnbWbnqkgF1OuRJSePYG9ym2nz%2BJFmCY3wj%2FEtms6HNro9i46dmqlJiZE6aIE6VHNmZDmPj%2BZJFCIE%2FG4pQBVOU74lb5OBjQP7ubg8%2F%2B7Eh4DGCc9GPcGFX6PHVodA1BjYbOHpP5V3UwLjg7llnJJL0feBWB7F4M1b7557xDBTXE2lZv1czP%2B6cVSUsXMCN7PJtVweVGX2jIgaEVQCo5DcSlCcgL%2BwF6eTwukvm4mG7vIIbCIOb1gwHm1FQEXDvmkYUZSdJtsBz%2FSTYjlgOo%2BLoq0ELSKJ2E0YA3W3ow2L4i07qah7mabAcw%2FrAX4BXycQhNSshwqc4%2BHju7FEMrZtQ7c35YudCfVbbUW9nBX90p4DvV0qagrCTVvaUnleyHSQX0ulrZS4u5rtend62SGsxEuPo4DGFt2tEuSjyMMLKZkb0GOqUBd8a3d0Nlh4l4Czeqa3l1RxRyJRX8Iyx4mbAp059J2n7DnL6TdsMMRsTSVkXV1FtDpVNJ2eNKAeIAhoFNf8JwAmBie%2Fg28ou5qsdLrf7oWLHuryzQfYMFpmvQVmotuidF1bbL7WKhV%2FIZhbS19WfXT9GssTf2pJ9UoWocgpfjppRHZ1SpruhDO5MTEJSYy77WTrR4K6G0kRkUY0H5H%2F%2FEl59MBViA&X-Amz-Signature=bd35699de33a7c2c8f48e65f800cf8952af62566af875a429dde98ba0ca9ba23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRSMP6L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDsA2k%2B2r98hxxWAvpGhh3eSoerL9oMoS%2Bn1UqM4R7EtgIgOFLBTFgRltuz2iLgZhKWp7s3a5HrccTTut6z54%2FlUloq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFVcR8TGO3BmOQfCDCrcA5jCXo6UhwUkOQGpAKL1z3D08dads4iMCsUTAgVSsYOSs3jIPaLhkxQ3i3cLmQB8wVWvVQEyE7CxncCTMztEmqIubm9R%2BNkBi0wo2OYtqqSLlAYsCr82Vyqzjsu4rlg8u5zgvGelpsLlWsxZJfSeNDORUD7zldxm0dxSMmMHWQ4RtY7G%2FYIfM2ZbZCuuNVw%2BIfSB1HarSFMSV4Pjbot4LTLyela1yextmcFcLuGiSVI7FHqDrTq6%2FC69VC7ynnqI6NBcNhXytTWEIt1fxeRSZuhelGyjGH4G8f%2FFnvl%2B8rlsrfkTbJlZeImG2G%2FtJ%2FQg6Z4WCflE90Vtpzx82Tv2nzfh20OOWtlUsDJaBVECKIaLU4IF0y1v4ZCAIuzPc6gSHLADm7zRe3Bh7DpPKIBBHrawZcdbwUYP4OV%2BE%2FYsIpu7GvXIXY6QZX29U80DLr8%2BaHlCBmUoI4YiXdV01x6iQl%2B%2BvGMMdF%2BxUbf7o7wvrVJQWcSGSnf6SR6Sk6RwtWnT1c2x9nCmGRb3mCpaBvchw06%2BVW19HiVJuDbGmJpvAcOBsRtYykuKCo31n7b4DfbYryCFP4nlk39XfKIth%2FWz3L9uFAxOaRSlYvztfJvKTEKCsVVb9WGVwKcUFpqMMKeZkb0GOqUBNVQDvrxFMfYDPj0f8ipTjJpqNL%2FeenYBcc%2FgLeZX%2FAdFxt%2FzWdbjBEpH%2BJ3hzPX32L3GtfDZJofPOAzdfbA4Er7PJf%2BKfHPzPtzU5J1uww7%2FymsInGIS%2FF2ZGjADqfqnvejzuEQ4R5bsVvb9tTh7fe5%2BrKa0c3j8NgX2LI%2B3E6wqu%2FJy1g%2Fq55dFiNkPMK1t6FaPXdiMab0MiSBUViOmkWRCkykt&X-Amz-Signature=ff466fda35050760a0836523e1147de7a342dd0af3f46f7b27c304db9a547538&X-Amz-SignedHeaders=host&x-id=GetObject)
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