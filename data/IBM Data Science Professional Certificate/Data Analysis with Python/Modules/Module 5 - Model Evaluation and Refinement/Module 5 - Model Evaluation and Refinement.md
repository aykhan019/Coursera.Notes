

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=57297665d932896d95d085256ec9b5eccc8ad16005f1d0b6da9e20c85f093494&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=e81a67bc8e559468bc424512a182f203c0b045d98850755e86ccfe0f975ed8c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=0235805642ece8d8dd55e40391744dbef2799af6921edf1980b74339e1fca348&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=e6f591d604ec5d038cbf946bb307c6507312d6a030dbacd1d50479fe822e4b23&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=03777f770c8591061eebc2f9da1e472d60865e6feb7a9bd33770106e0d1bee80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=030aed129c25341e22d28882d6ce2b34f29d26103878830e86923f7e517d19cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=12b8187c89984df0dbadbcc3932e125c796e228733879fc5381d6150b8d0d362&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=108371ce6a22fc43c0723f57dcf106db46707edd63bce950e25b4db9886bc3c0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=9c4c832ed5f8798d5d53d2fcbd1f3b8fe27d8f1082dcc1543970d72d33b182e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6CIAY5V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr8X6yKPkGWuM8CLr8ib%2Fr5rPwrndUEcbpytI35RAAsQIgLmoUVXp5yCAZy%2FsjkcQvedfeIKjJBz%2B5bSSC%2FlqWYi0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8p5Y%2FDF90SJGiueSrcA1WoH1K72bzsutW1OqlPiiwJHhaDGn2qgf0yQ0SBawXBbb6UzlO5vyT28A55MOanI5GnsZ%2FA1OVmU8QSSuo%2BIru9IHiMTSeebMqqkJVbfJEFkX%2FH56A52ALmi50JehsF2X8HCE3ngA6ztoBqq5pWas6VJ8Ga8cGencfefm%2BmAjei4j40IHDmDppc06gcSIpdDKxqEXQXBhDr4nhK0t09mxkOO1ZZW7DL4LvH0QAJJ%2FyBmtGG6i11%2FTO%2FEgNAIUPdstFPzeDfuZCGJBi40eXK7f2p72E%2BrDi2zVQOfoKFw%2FBh7j1rGSqlzijlIlMofr5M3cc1OKXZ%2FrcvOKQTVPCY8ErGGLR99frUe1%2FYXQJjA3ySY5WRMjuDYp28%2BUFxHmActk4ZOBHR8ElwhYCeGBMFk7iqgS5B8Zrf0DYIBnany8%2BJsEfueL%2BcooF0P%2FGyqq%2Fcwl21gJIkzRBmj9zftWON2pGU5prI%2Bj6ehMr7uSfMsc3Wk5DLpeJcXNWmlMaOxWJwfqegIMq0Y10JZBbMxK1RIPENwKmYrWVKc7XRhe84f4wsxcjndOmd0Ezkk6gs1Pb3LxDL3JcUzFzyYrgYSGXN6LrvrD%2BnbcIzOrzLHCBSSH7zdymiYcJSOEB%2BI7ItMPza9LwGOqUBlj%2FNEWMTZVg9biqdnsMzgfYXM1vfJBkMRQwzhRmKaU0iHmPg6FX%2BGFECJ4sHPX8mSnX74Yx%2FvUJ1Fyd9rWVPrYV%2BJfnBVpLEwnT1f3068v3%2FQJ1xD6mE02pUEitiRL0g1HefDY5krEvKcqmt%2BLnHpOKjnV3bc7T2YWolgmQC4JqfsoVwl0RQftoPMK8ZfRKId6bJ0s%2FEiV%2Fvi2%2BG9N87UV0IX9yp&X-Amz-Signature=5b9d06e65586f7d8fe55bbb801b2b33dccb7ba0233d97056d0cfaac821bff410&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6CIAY5V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr8X6yKPkGWuM8CLr8ib%2Fr5rPwrndUEcbpytI35RAAsQIgLmoUVXp5yCAZy%2FsjkcQvedfeIKjJBz%2B5bSSC%2FlqWYi0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8p5Y%2FDF90SJGiueSrcA1WoH1K72bzsutW1OqlPiiwJHhaDGn2qgf0yQ0SBawXBbb6UzlO5vyT28A55MOanI5GnsZ%2FA1OVmU8QSSuo%2BIru9IHiMTSeebMqqkJVbfJEFkX%2FH56A52ALmi50JehsF2X8HCE3ngA6ztoBqq5pWas6VJ8Ga8cGencfefm%2BmAjei4j40IHDmDppc06gcSIpdDKxqEXQXBhDr4nhK0t09mxkOO1ZZW7DL4LvH0QAJJ%2FyBmtGG6i11%2FTO%2FEgNAIUPdstFPzeDfuZCGJBi40eXK7f2p72E%2BrDi2zVQOfoKFw%2FBh7j1rGSqlzijlIlMofr5M3cc1OKXZ%2FrcvOKQTVPCY8ErGGLR99frUe1%2FYXQJjA3ySY5WRMjuDYp28%2BUFxHmActk4ZOBHR8ElwhYCeGBMFk7iqgS5B8Zrf0DYIBnany8%2BJsEfueL%2BcooF0P%2FGyqq%2Fcwl21gJIkzRBmj9zftWON2pGU5prI%2Bj6ehMr7uSfMsc3Wk5DLpeJcXNWmlMaOxWJwfqegIMq0Y10JZBbMxK1RIPENwKmYrWVKc7XRhe84f4wsxcjndOmd0Ezkk6gs1Pb3LxDL3JcUzFzyYrgYSGXN6LrvrD%2BnbcIzOrzLHCBSSH7zdymiYcJSOEB%2BI7ItMPza9LwGOqUBlj%2FNEWMTZVg9biqdnsMzgfYXM1vfJBkMRQwzhRmKaU0iHmPg6FX%2BGFECJ4sHPX8mSnX74Yx%2FvUJ1Fyd9rWVPrYV%2BJfnBVpLEwnT1f3068v3%2FQJ1xD6mE02pUEitiRL0g1HefDY5krEvKcqmt%2BLnHpOKjnV3bc7T2YWolgmQC4JqfsoVwl0RQftoPMK8ZfRKId6bJ0s%2FEiV%2Fvi2%2BG9N87UV0IX9yp&X-Amz-Signature=2f40197bec67084020aabfbbc2726ab90285e82c341cbee67959197d0fba274c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6CIAY5V%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr8X6yKPkGWuM8CLr8ib%2Fr5rPwrndUEcbpytI35RAAsQIgLmoUVXp5yCAZy%2FsjkcQvedfeIKjJBz%2B5bSSC%2FlqWYi0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8p5Y%2FDF90SJGiueSrcA1WoH1K72bzsutW1OqlPiiwJHhaDGn2qgf0yQ0SBawXBbb6UzlO5vyT28A55MOanI5GnsZ%2FA1OVmU8QSSuo%2BIru9IHiMTSeebMqqkJVbfJEFkX%2FH56A52ALmi50JehsF2X8HCE3ngA6ztoBqq5pWas6VJ8Ga8cGencfefm%2BmAjei4j40IHDmDppc06gcSIpdDKxqEXQXBhDr4nhK0t09mxkOO1ZZW7DL4LvH0QAJJ%2FyBmtGG6i11%2FTO%2FEgNAIUPdstFPzeDfuZCGJBi40eXK7f2p72E%2BrDi2zVQOfoKFw%2FBh7j1rGSqlzijlIlMofr5M3cc1OKXZ%2FrcvOKQTVPCY8ErGGLR99frUe1%2FYXQJjA3ySY5WRMjuDYp28%2BUFxHmActk4ZOBHR8ElwhYCeGBMFk7iqgS5B8Zrf0DYIBnany8%2BJsEfueL%2BcooF0P%2FGyqq%2Fcwl21gJIkzRBmj9zftWON2pGU5prI%2Bj6ehMr7uSfMsc3Wk5DLpeJcXNWmlMaOxWJwfqegIMq0Y10JZBbMxK1RIPENwKmYrWVKc7XRhe84f4wsxcjndOmd0Ezkk6gs1Pb3LxDL3JcUzFzyYrgYSGXN6LrvrD%2BnbcIzOrzLHCBSSH7zdymiYcJSOEB%2BI7ItMPza9LwGOqUBlj%2FNEWMTZVg9biqdnsMzgfYXM1vfJBkMRQwzhRmKaU0iHmPg6FX%2BGFECJ4sHPX8mSnX74Yx%2FvUJ1Fyd9rWVPrYV%2BJfnBVpLEwnT1f3068v3%2FQJ1xD6mE02pUEitiRL0g1HefDY5krEvKcqmt%2BLnHpOKjnV3bc7T2YWolgmQC4JqfsoVwl0RQftoPMK8ZfRKId6bJ0s%2FEiV%2Fvi2%2BG9N87UV0IX9yp&X-Amz-Signature=430f74403f1d7e881a0d03d96d50a3d9b00a61969032f3f0539c66385547dbc0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=18474f6b321e35996493c9d6bd6b05e43ef6cfc4fa2154485f128ee1f0848029&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=a437b7f1247854b0fdf688eecce500c76768db2db4d7a52c11848f28d4dda232&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=f0c27b2a7409794e0ae4338ecd9d9a5ab40100643d4b806652648372c3630b07&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=7e127da342644abd976e500c3ebe359fef34061555777a1d9e103baa467298f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=faec114b43386d8e73bbf46bea2cac4f33b202434c6e8dd2750e195d5ded5377&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQG3KQ2R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk%2Fq8DuT8zqKbvRfKkose%2FTio7UnBT57ihy1kjEgVP%2FAiAi8n9B8oowzIv%2BqswufLhrOxCHFe8%2BgtnJfMsWn%2BGuBiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdI7by8XtJsNNgCv6KtwDBAPZVjVhcJcpd%2B3wrMDUMntvd0uCwdPyAf7cUFLzgHeTUjeo3rA0esfcKgsc3lqg9UaUojBaw8sb7zxhI4rIO82fmE6vwvX6qPe3QS6c7EYsq5dR7rz7Vacx1nyETab3Z572%2Figs7Omiz1vnTlXB8H%2BSWOweaZbHzqWsXJP%2BU5qnXwR1kGO5ffqU6ezfovVrt%2FcwYROMztbxHSjFkbrDXBtkEnaCuJzCPWcO1H45fDM6Jbw0752UlybqmoudA72y5mJoDweB5QHliw4z9RkmgJVdgWKN5oWzLEIQQBV90bfutBIpvezgQ8D5XKDbCxcueBITcltUbWxfiTYeZMzKmVyEyzvfUBJiHUGO0Qify0a3x%2FeuHKui%2FkM%2BCOT6I1jxcOgv4b%2FgbJWpEXB0mRUkKDjz%2BawDHHSX0264hst3c8tF255HNk%2BAF6G0G4O8TQXBe5gF%2Fk7A2UpWlBMUpJuTqOT403jyi%2B1jtiar3nwfMy7%2FQFbJNxE3pFxPkUCOtabIClXS%2Beku%2FUp%2Fjfl9vaHPSpCLiVwOyJmMQlqG%2FG5ihP%2BOw1hWEM5PdYOcIRwktVL%2B%2FSAh4L4nZQWzSk2VSGAn1EhzjWyXlrQKVlJ1bawScC8at50HjbmdqkrK7NQw1Nv0vAY6pgFUgPCEHPbcRzJkJsqh2YfIoEqPoYJHJerfvzSBB%2B2DJcSI6oYe5p7sJNYF5k2AzQLka9FrmPty8ckf7riu8SZKPqbuyy8FLZiyAQp3YCTUvgiIbFDjgLF6W3ClI9Ulm6YNZm%2FnW%2BOS%2FJxTxP%2BLxqZFpiQ8QVKG57xk1YkGcxK%2BCyUNbZntSpkpijf3DVC9XZDRkao3meQdXrE6%2BbaZ1qtRAnexTHO%2B&X-Amz-Signature=689af44c331f6f9a9aa1f8c1a78d110940cdfcf5e38dd00eede05739153b330e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCGJQS3J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bu2puyBWR%2BrRS8lR3Xfjjxv0vPmxilsSyzyZvlX0JXwIgWlJ758GZkcZQLghp0h%2Bv%2BBCFmBSfTnXDWtYWkrZy9U0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPS7JiKrZM1wLEM4ECrcA3pvk6OyQV9H3EvHup%2B1yLGtWlErEeFCSw4ZDASTvN39sqQlx1vFQKCT%2Fi5BPRXKvnHyo%2FyDq6wpZ11AhAKovOkemNuHgfHgakU2U8gL9AL5qllqqbmsHjuHeS8A4RHPrHVKsZrxutmtYQwqo2FwOzRW%2Fb%2F%2BsJrFFtnU6D1hYOXVijDLE7BNfVDNgLoXiKZq42SaiL7uzVp5T2O0W%2FgIQhY38xC4vjvz%2FGwGugrm7gmfowYVrGOL7wFHWpLbTPRTrBv44NtriIm5DISxvhNiuE3QwxgN2A9AP7apQYfHVQWxTKFZHzJ4rwqHiCy569u65EJnXueTdp6xblOwENvJqqkB7907T8FwklMCsu1tNSd75Ah33F7Ijh29fYQ5wZYgBvtasoG7WbZQk7MIk1ACumPngWoevVrTZN6u60LKgxdq4TjE2enInSZE%2BdaEUrXeuk7OjPx1p8UYsBPS52M%2F4IrUBL2J%2FR8%2BGxONLDxMHRj1Tl7O%2F5%2B%2Fee0VAUxplDfz5nIL8N%2BaammorcHBdq8G3i4b6jTuGNiDLd%2FRDeQcSHXmjGMTBZ6bh0K8%2BUWSPwf8i%2F3NlLDDzTgfdCna5CzRdpIjFztnji%2Fyck57kilehTtoI5imdsEsapMAJ6K6MJHb9LwGOqUBFfYA%2BIoqyRN2Fb6QXXt8Ps%2BTdqKDSy412hZh1X0pPALPdk4jAoNfOkDVzBwxvZ9bXeYlEli0RtelHbIO5O5VXl1HI1UddQayEwuZXHlhG5hbK2HD4tgPLwY7DMpznK70amMZpPmO15m99blngLpKlI7clDjfqxYJiuSY2DqrIf2wwxorpgjVUAR%2BU8wpfSxoCRL%2FW%2FNzT4xp4CoJ79m%2F7gf%2FIy8R&X-Amz-Signature=cfdb8b675479bde493ecd0ba565447765e279898fd24318715424fe9c36724c3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCGJQS3J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bu2puyBWR%2BrRS8lR3Xfjjxv0vPmxilsSyzyZvlX0JXwIgWlJ758GZkcZQLghp0h%2Bv%2BBCFmBSfTnXDWtYWkrZy9U0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPS7JiKrZM1wLEM4ECrcA3pvk6OyQV9H3EvHup%2B1yLGtWlErEeFCSw4ZDASTvN39sqQlx1vFQKCT%2Fi5BPRXKvnHyo%2FyDq6wpZ11AhAKovOkemNuHgfHgakU2U8gL9AL5qllqqbmsHjuHeS8A4RHPrHVKsZrxutmtYQwqo2FwOzRW%2Fb%2F%2BsJrFFtnU6D1hYOXVijDLE7BNfVDNgLoXiKZq42SaiL7uzVp5T2O0W%2FgIQhY38xC4vjvz%2FGwGugrm7gmfowYVrGOL7wFHWpLbTPRTrBv44NtriIm5DISxvhNiuE3QwxgN2A9AP7apQYfHVQWxTKFZHzJ4rwqHiCy569u65EJnXueTdp6xblOwENvJqqkB7907T8FwklMCsu1tNSd75Ah33F7Ijh29fYQ5wZYgBvtasoG7WbZQk7MIk1ACumPngWoevVrTZN6u60LKgxdq4TjE2enInSZE%2BdaEUrXeuk7OjPx1p8UYsBPS52M%2F4IrUBL2J%2FR8%2BGxONLDxMHRj1Tl7O%2F5%2B%2Fee0VAUxplDfz5nIL8N%2BaammorcHBdq8G3i4b6jTuGNiDLd%2FRDeQcSHXmjGMTBZ6bh0K8%2BUWSPwf8i%2F3NlLDDzTgfdCna5CzRdpIjFztnji%2Fyck57kilehTtoI5imdsEsapMAJ6K6MJHb9LwGOqUBFfYA%2BIoqyRN2Fb6QXXt8Ps%2BTdqKDSy412hZh1X0pPALPdk4jAoNfOkDVzBwxvZ9bXeYlEli0RtelHbIO5O5VXl1HI1UddQayEwuZXHlhG5hbK2HD4tgPLwY7DMpznK70amMZpPmO15m99blngLpKlI7clDjfqxYJiuSY2DqrIf2wwxorpgjVUAR%2BU8wpfSxoCRL%2FW%2FNzT4xp4CoJ79m%2F7gf%2FIy8R&X-Amz-Signature=76c23aa04182f65022adc961bc7c1fc42f2d84b5e94c605f405a053825e28235&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJH7ZIY3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3HMQNAXS8gpOW6qc4MaQRveXrVRj088nPHuoEaDDVlAiAVIdP2Y6CJXrWt2NbFN%2BMfFIn4N%2FkNmeJoO86M2q0qXiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNOoAwfm5faGV%2BiqWKtwDKG2bSw9V2YWLNg5GJLhrpilBl37eQQ0kGCC4f84XN9lNMSryrImf0DwZXXevRjTClmwtSF1cE1W0cJMNo%2BMaSCeINyGLUAZBKmHaqVBhc4qwB6k%2Fdbk%2BJx7UIfyku0Oo%2B%2Ba2Fy8cPdYdop8%2FEop6boYvk44F13gdqQF8lO6BIoYt1sh4TO14AyL2u78RYX9gAGN1864EC1g%2FQA4lxLEmh2dDPK%2BsQ9bfscnyqN92i8VnJtwob69KRpK6wujCpg3dqxXGqafT59TKXaUI0WKiGaiqUi%2BSd3tqYGR%2FAZk6%2By25lXevo6Dvaq95cEP2s2%2B5IQe8kAzml26Q2j5TBCUzF%2BXuSwZ7Jtg7C0t5Gz3vabrRT5j%2BaTRSNsXDOvyyr5tSAImt5VO48WyA%2F9%2F8t32MtioRcO8DABha92IlGzN9Cdi0MUG6o2qXLPym0rUigCyzU6%2B8j84kC2tvsi2ra0Fx66Sfa%2BK3hDhLBfFrvavhBZIUHxvcdjVhPM6IYzNTNwa7KM1Wbyv38PRZB5NO5kYh0tL%2BVB16RlE%2FxJ98NFh2C6E7rNHnB7lDWYyGa%2BJN%2Fmxuty2fSPj3SPWCI3wHLYSSpAR9Q2AoIb2gGepd3WVYzyizOGHN0dnjNOwX7%2FQwxdv0vAY6pgELGJi7zm1dThewupzJvFexbY7LkAliBd3%2B4axVhY9qgzOL9zIyPitIOrAF%2BL%2FZvVQJr%2FnV1iOIclS9oki4XcYHov1vxflpGyRYdZUhjFeIzCM9qLuA8XvPXg1gm77C%2FaQ2G%2BKmxmVEJUHmoEbzBq3lTeGthfP9TN4FA1F5qOw61tvA8nUMkwuToQh4ydi18kvs07kIX5u9nxfpE2Q3M2xXXkXB%2FRtL&X-Amz-Signature=842a5e640e61674c07c9290dcde893aa5c74d9c7cabfb69a33d51c2d6201daa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMYG7UM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFWk4b%2BvFsxqCXFtL25H6JOAgVTvPww7cuSqTDsZ%2BLkAiAmE6hjx9vhuaak7ywp9PnlOw7LUed%2FKe18MCVIPDYQ5SqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeuISXRc4%2FESgbW7aKtwDUoo%2BsHtuGP1IdqZgxizGQqaRavPt2gDbf%2BkskjExth%2Bb7wcBBl2W4aDjA2e5WX0dwT21UrcK5LZedmL191ldmLMjB0Za9guQcj0iB8X0eG4zm12uVfxbZ1Bu5S%2FT4pQkI9ZDkRvd0W9EqAGJMMZg6g0jmbPIZt7wQMuQQE2KNta2OpThqa2DFyVxuShMi7h7PZPq4SlEejMX6df99mYDLLMhdYtyMgdnCVmk%2Fni59H3uWPzsAQZZgftkb%2FKkj5x1hjEilAheBTezNT3zi6JRTVAWwbfzIUOQf0POZGy1jr%2BjXl%2BO87Gl24kK1iuH2x5vGYEEXVEgsqJGf60kpGXubGIwUp6U%2Brd%2FplQaAmS1ZuCQLMCVdTrMLw3Il3l3HYC8nZh%2FtBzUAGwBOAcmGALqF8HcEjD%2FRUUcCu8eDLIyulkpV%2Fbgt0D5hTHBhrj2%2FDstYLkYfus5P43%2FhunlQnwwIgOoLyr9Th6slaDXcBzizGfhy4iVNR7TXqd5v4EKnMXffT3VrJLaXXkzmbbYSm26VD28SFwLpdC4JNcnoP1Ad08atV7bJXJrWwdl%2B83RJJBnYgW1pD2E%2BKuzACl20GBDFd6evYYGqrGNZPhz99Sv08ApjVBZAyiDVFXIOEQwqdv0vAY6pgGjlyXiZLUQfcn2X3Hj5dkTFl3DstNdsMQqrgkbd1mMuDDo0HSskhW1O2EW%2FbbJLkILj%2FbK%2F7k3bAeaYotbCT%2FP%2F3JFfL83qWWvwmaMA3PpAr4NfGWs0Dr18lE72%2FsixaWfxPjArwdBEDf8M%2FtzdebrucNViYs17Pg1jolzQ3wzj69yF349K2vJkiIYh1a%2BceQThm0ehfiUb2aeOT9ko8kib%2FlIGMgj&X-Amz-Signature=683e987529ee3e9118cfe2ccbc659f0d9ba04e2f7eb5d74d0de49a3e565df0fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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