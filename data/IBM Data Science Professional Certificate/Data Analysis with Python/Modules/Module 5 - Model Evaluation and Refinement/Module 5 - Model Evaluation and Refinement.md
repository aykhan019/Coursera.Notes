

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=325aa9a1826dfc22b1104c81be26e917ea13303ba110e7421c0d077f5883b6a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=b92fe77c3c8a24dd80ab4466342f4260c3de28c03677e423b470ba905a1c7dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=3d8e4b3822ffe4f2443e060c495636ef17ce6fd3960888eabf5f73abd232fca5&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=1e9fa1aacd9ebc2ca1db0ce16c6af7e029db6b037e2161cbecb35376b131a63d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=7496abde01adc34fcb1acc34f062e0c8c81c32b9b9dcf8c17bfcaa6e6347f515&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=2655baa82dcdf1d25fb94179f9331bcbe71e717df826256832566d628f80508b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=85d5ab624be7b51156be418513b4e05cc5a68fa82989f17e2aa561f9d3550f80&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=11f3384436b4e2c622c5a575bb43adf74fdac13fa1ece2955613232228cdc825&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=90ffd11acda4a4a68c95af6bfbf0f3f300229c30a8ce0b2950dfd3d92c4aec65&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWGO3QT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDRPgAgRE%2FMuyEnp%2FAKDcvjwHf14ohnjBwUYi9qvYt%2FoQIgZqfxW4ZF3G%2FlY9broBA3SJTfmLsZtznpr1tuISGMo3QqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI10AuXeu090ufCdZircA%2FKQnDG7mcYyp8SUfNB%2BDJ1g4q9IdqRTXayKV5PSpZW0zMHfBssBHgD8WVwEGXNQ0JCu8GHAM1l6%2B269cazBV6uXKmE3iorqUj87f8aoI7PzG1YjIXxW9IXXiFPZSrSle%2BCDdsiCYCcpxgNDJApECX47Al0aCO5LugFExoBAzJkIy23SIbenSnj8uTm2LFs9ImvfuXM39KmurGTkns6J1FWdYWbGQJeZsAEfmiixFfrsZ%2FGtoYQGQflPma2WNKrLEDn1vt7EfgCFbxzXRjIxwCflczvNeaPyKUeBFTFoDB8GrOVUzgkB8%2B64VaCynJFqGP2iEWJHFps7gIMrmLrXbwp0z9ak7CfjoTB6FPCZ%2FvJbMRuNCa8hxtKx9BbE2Tj8EKR7d2wVhD9Rh2oJ9sQmOMprcb%2F0OYE4yH%2FavvTMDtlOaxaIiW%2FlKl05XKpK7R0G%2FWSjEP2Kxj7my6dLSY3f6Rxje%2B7d%2B3x%2F3CUINrYnvlM2ImC6RM9%2Fh8GtFk5IpN2SytfVcOVlWOBBQgGL5Di5Jk1YOiIi9DO%2FzovdB%2BCq9%2BlKiOqh6WLK%2F1LyPObyWTZ405kQUwl41PqQFAXjLitUmENGhOWN9n%2BCBVTS6l8yDaVft4hYXXYbMZb9kaEbMMXUm70GOqUBZQaJhhPNZc%2FZrqrscnr42oLFlgsmT%2F0QXM758DLLbYgn%2FYRdMCuVPZ8zIDESWdbrMGE9Ltt9BRCnO9QPAuQhCbjd1ZaP3xCxsKT0jbEuay%2BsaQ1hBq8QbirrPb2D%2FqZ7%2BB5FAIkvQw8mLWTGp2%2B8PGCxU40S0pmNfceBsx65zC%2FldQN2dXGJi6fOqGWpBpeJ2oK32MA5aG%2BZebOT8TNwJLIW72Q7&X-Amz-Signature=a2fa748186941ab016fb506fe20f1acc1a0c31c63c16d5052673c080e92b1369&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWGO3QT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDRPgAgRE%2FMuyEnp%2FAKDcvjwHf14ohnjBwUYi9qvYt%2FoQIgZqfxW4ZF3G%2FlY9broBA3SJTfmLsZtznpr1tuISGMo3QqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI10AuXeu090ufCdZircA%2FKQnDG7mcYyp8SUfNB%2BDJ1g4q9IdqRTXayKV5PSpZW0zMHfBssBHgD8WVwEGXNQ0JCu8GHAM1l6%2B269cazBV6uXKmE3iorqUj87f8aoI7PzG1YjIXxW9IXXiFPZSrSle%2BCDdsiCYCcpxgNDJApECX47Al0aCO5LugFExoBAzJkIy23SIbenSnj8uTm2LFs9ImvfuXM39KmurGTkns6J1FWdYWbGQJeZsAEfmiixFfrsZ%2FGtoYQGQflPma2WNKrLEDn1vt7EfgCFbxzXRjIxwCflczvNeaPyKUeBFTFoDB8GrOVUzgkB8%2B64VaCynJFqGP2iEWJHFps7gIMrmLrXbwp0z9ak7CfjoTB6FPCZ%2FvJbMRuNCa8hxtKx9BbE2Tj8EKR7d2wVhD9Rh2oJ9sQmOMprcb%2F0OYE4yH%2FavvTMDtlOaxaIiW%2FlKl05XKpK7R0G%2FWSjEP2Kxj7my6dLSY3f6Rxje%2B7d%2B3x%2F3CUINrYnvlM2ImC6RM9%2Fh8GtFk5IpN2SytfVcOVlWOBBQgGL5Di5Jk1YOiIi9DO%2FzovdB%2BCq9%2BlKiOqh6WLK%2F1LyPObyWTZ405kQUwl41PqQFAXjLitUmENGhOWN9n%2BCBVTS6l8yDaVft4hYXXYbMZb9kaEbMMXUm70GOqUBZQaJhhPNZc%2FZrqrscnr42oLFlgsmT%2F0QXM758DLLbYgn%2FYRdMCuVPZ8zIDESWdbrMGE9Ltt9BRCnO9QPAuQhCbjd1ZaP3xCxsKT0jbEuay%2BsaQ1hBq8QbirrPb2D%2FqZ7%2BB5FAIkvQw8mLWTGp2%2B8PGCxU40S0pmNfceBsx65zC%2FldQN2dXGJi6fOqGWpBpeJ2oK32MA5aG%2BZebOT8TNwJLIW72Q7&X-Amz-Signature=a4aa071e898e7b99984e2e3bd6ce3f34df2fb3bc89fcdb69993146f737719166&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWGO3QT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDRPgAgRE%2FMuyEnp%2FAKDcvjwHf14ohnjBwUYi9qvYt%2FoQIgZqfxW4ZF3G%2FlY9broBA3SJTfmLsZtznpr1tuISGMo3QqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI10AuXeu090ufCdZircA%2FKQnDG7mcYyp8SUfNB%2BDJ1g4q9IdqRTXayKV5PSpZW0zMHfBssBHgD8WVwEGXNQ0JCu8GHAM1l6%2B269cazBV6uXKmE3iorqUj87f8aoI7PzG1YjIXxW9IXXiFPZSrSle%2BCDdsiCYCcpxgNDJApECX47Al0aCO5LugFExoBAzJkIy23SIbenSnj8uTm2LFs9ImvfuXM39KmurGTkns6J1FWdYWbGQJeZsAEfmiixFfrsZ%2FGtoYQGQflPma2WNKrLEDn1vt7EfgCFbxzXRjIxwCflczvNeaPyKUeBFTFoDB8GrOVUzgkB8%2B64VaCynJFqGP2iEWJHFps7gIMrmLrXbwp0z9ak7CfjoTB6FPCZ%2FvJbMRuNCa8hxtKx9BbE2Tj8EKR7d2wVhD9Rh2oJ9sQmOMprcb%2F0OYE4yH%2FavvTMDtlOaxaIiW%2FlKl05XKpK7R0G%2FWSjEP2Kxj7my6dLSY3f6Rxje%2B7d%2B3x%2F3CUINrYnvlM2ImC6RM9%2Fh8GtFk5IpN2SytfVcOVlWOBBQgGL5Di5Jk1YOiIi9DO%2FzovdB%2BCq9%2BlKiOqh6WLK%2F1LyPObyWTZ405kQUwl41PqQFAXjLitUmENGhOWN9n%2BCBVTS6l8yDaVft4hYXXYbMZb9kaEbMMXUm70GOqUBZQaJhhPNZc%2FZrqrscnr42oLFlgsmT%2F0QXM758DLLbYgn%2FYRdMCuVPZ8zIDESWdbrMGE9Ltt9BRCnO9QPAuQhCbjd1ZaP3xCxsKT0jbEuay%2BsaQ1hBq8QbirrPb2D%2FqZ7%2BB5FAIkvQw8mLWTGp2%2B8PGCxU40S0pmNfceBsx65zC%2FldQN2dXGJi6fOqGWpBpeJ2oK32MA5aG%2BZebOT8TNwJLIW72Q7&X-Amz-Signature=ea4128352c95bf53ff3a81708913891483168bdf9ebc224dab9599a1daff0dd0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=871d4ad8946d6d200d8a5fbc3ebaed8bfc31db5dc2254c1eeb64837e8cbb2590&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=6c7f91c801e22c36acdc7882ba7bece66246ea061eea653947c7a051b4d8a319&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=3c84ee9f21a0252ce79e52eb36e21c258030abe02f240c45a9cc3046660e9973&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=a8537081d18768a409319b8450eb010ccf2198aff957e790a10e0e64004b3e91&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=623e58fc859455dc7fb12ee53e88dfd43ca71b0b183e69fbfe895e26ac096955&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYO3DXX6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCICy%2BJb3AjlONQdqhjLuuYmp0DIyjjqPrHSgAIb4wlvDiAiBWi%2BkO7za7aNgzGIP0CHFSChJfbGJMAEnPEqLHWFsFKiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5UJMZ7RNHeLgFk8JKtwD5OTUsn5icwrqskMiCUtJJ2AScAn5nr4yV5gHEIyd%2BQoDheUAsDkkkS0YCK%2F0680r225jkBMJ0gYLiCHHv07q%2Bx1cEYX4dCvlSlbw9ciGrpKHFPdOtKUWiKP7DubK%2F26EpJEURgJUodsiBv5inSv2xWF2PeGsH9iUXwb8uCKkMDDTDhKLYKnXij30cj8HwD5Am9NlQ0ykFQP9hJMZdc2O0a1pW95%2BufZEeTfk%2FYDptFyz6SaJUDD4kEHXtUQXdwSus%2Fs6OEBJ0UaH45n61FnzRza7y3KDWMLr6sF8GEkU4M6Twgg4%2BId%2BjhMcM2uyh0%2BQG6I85KXuIJlSi9%2BqvFOp7koo6%2BY1OJxU66VvTaDv3gK%2BejAXDFrY8fbTvBRaGsdKQ0mNQTfXiCQISri3AySFzzKkIRktnk8cYxkBZEETb7fFI9UimjD98461zOAVVu1HyxnGvlumAqOvSUh9x4%2BdE32YwuMYitRbOkLa8iSdIAelwvJsm43I3iyI140BRY481YmW2sD8nPtggOdoKXCXADzqF6yHwZGgEgcOftHUf9qc8gHRl%2FsnVAUggBnjkVE%2FR7%2Bvtqkpb6jiSugTlg9arXvO%2FyaTQvWdMMrb91Oy%2FpMFWKTEx39VDSvudGgwuNSbvQY6pgFt6BFX%2FQIIrj9jvCogwjeYFtAIkDqWG7mh4djyCaPJbgrEN7CGEJC8uAkaBrVNql%2FLIQjvuL7JdWX63DVU0QWjqkleJVW451rVbtSg6zRe1oXEYiy0sQLNyOy4bcmfH9b6pDyV64lgdxhfz37WbzDckUotlKAAMFlbTWflyAbnFRyKI3fBRAthKcWcxTbW5DWaF2c%2BQzCGM5lOUtQBKbJ5EXUkiEee&X-Amz-Signature=46dd6d2ea32d4afaff2d19cb4f78d7ade270200e41d2413d386d641069d69a6e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466652NOM4L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCICvAH1ZPPqjZerI2wSRlVQowSSa%2BK9sYFDvEO8HfQMjlAiEA5N%2BbLyY8c5NvlZU0NxxocLae64C04jE0z3YZ62d8SgcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOut9W7EEmTvQ0C7TSrcA6tVRTOYN9EkonpIFRYSGW4wSwT%2FjUBDyS9JCg8XuVsfdpV9sg6dF4P8fvhJstjmt24hbLi4UnxrJ4SQx2NW%2FM7%2Fnngyv7eteXdLoJKmLp4Bu5GmuWICfPh6ny3UybRwLTjTGFkgql8rqlT9GXG%2Bx3cFTNov9%2BJDyhnDoc0cL3Aoa5hz5ohsME6%2BXc2goRralJ8iftqtu5TlI7ot%2FrxabyLwgf2u9Mat0Xn9bqztCfm7hl77%2BxKpuReFecJWOJ4cHlK4oajV8i6boS6DwwWkTqKUJN3NbCkmMpIttORtmSsEW4yEw8MWfj%2FoCiUZAJL81ARDRSx9Dz%2BQc1ncHqk3RwclJwerMFIv4g%2BrHBg%2BJnQD7jEsmcs1VkzYbhnmoaMj39S1OllStQmNlH3oA6ehW2w2N6YMsRHCuo58mLCDXsksM2o0mZxIrMfeoG%2Bx2bnzeqls%2FHsWW0jiNuR46eA2LM%2FizPOOMUqGEg5tkdx5%2FvfF%2BbnSM%2Bo7VTjpOuNObwJO%2BlOKc1mZ9Lh%2BAm7WV3%2FKzkLx76QpgBJADUVnALgD%2B0t%2BNEtzRNNyAYUnyVvUjaZij7yeWKZYdDMUshT5iu8plnNosVEA1CmxZMQHT4zSCvwSEKRk4%2BW6jO8WMDPgMPPUm70GOqUBPmTqhyLKrZaNJwIcx4Pju%2FfcI4cOucuGgeBBUbhR4QX%2FXZNuKrW8ezmPWH7pMTXlRJ%2FhXD0O%2B5ao%2B66PSlgjjTWIMrjKwQAkjiD2z0wWZSlOWEhm507qPGv9oCK%2Fqqe9r%2FPYT9809HCGSSzZXWmWPqZKB1JqLYBJqekiu3XLir69HikGfBE0SUmq3LoyintSK9pkikyNj1a4SZaCFeS%2FRPkvU%2BHo&X-Amz-Signature=034fcf8eebdcebe05d30a8d58f99bfed290c38fb74c3a56c5a5ba3f706b2b5fe&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466652NOM4L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCICvAH1ZPPqjZerI2wSRlVQowSSa%2BK9sYFDvEO8HfQMjlAiEA5N%2BbLyY8c5NvlZU0NxxocLae64C04jE0z3YZ62d8SgcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOut9W7EEmTvQ0C7TSrcA6tVRTOYN9EkonpIFRYSGW4wSwT%2FjUBDyS9JCg8XuVsfdpV9sg6dF4P8fvhJstjmt24hbLi4UnxrJ4SQx2NW%2FM7%2Fnngyv7eteXdLoJKmLp4Bu5GmuWICfPh6ny3UybRwLTjTGFkgql8rqlT9GXG%2Bx3cFTNov9%2BJDyhnDoc0cL3Aoa5hz5ohsME6%2BXc2goRralJ8iftqtu5TlI7ot%2FrxabyLwgf2u9Mat0Xn9bqztCfm7hl77%2BxKpuReFecJWOJ4cHlK4oajV8i6boS6DwwWkTqKUJN3NbCkmMpIttORtmSsEW4yEw8MWfj%2FoCiUZAJL81ARDRSx9Dz%2BQc1ncHqk3RwclJwerMFIv4g%2BrHBg%2BJnQD7jEsmcs1VkzYbhnmoaMj39S1OllStQmNlH3oA6ehW2w2N6YMsRHCuo58mLCDXsksM2o0mZxIrMfeoG%2Bx2bnzeqls%2FHsWW0jiNuR46eA2LM%2FizPOOMUqGEg5tkdx5%2FvfF%2BbnSM%2Bo7VTjpOuNObwJO%2BlOKc1mZ9Lh%2BAm7WV3%2FKzkLx76QpgBJADUVnALgD%2B0t%2BNEtzRNNyAYUnyVvUjaZij7yeWKZYdDMUshT5iu8plnNosVEA1CmxZMQHT4zSCvwSEKRk4%2BW6jO8WMDPgMPPUm70GOqUBPmTqhyLKrZaNJwIcx4Pju%2FfcI4cOucuGgeBBUbhR4QX%2FXZNuKrW8ezmPWH7pMTXlRJ%2FhXD0O%2B5ao%2B66PSlgjjTWIMrjKwQAkjiD2z0wWZSlOWEhm507qPGv9oCK%2Fqqe9r%2FPYT9809HCGSSzZXWmWPqZKB1JqLYBJqekiu3XLir69HikGfBE0SUmq3LoyintSK9pkikyNj1a4SZaCFeS%2FRPkvU%2BHo&X-Amz-Signature=a6f8348c9ef2796a68b679ff303d4b2a223b77314cc3f4c5d9c1f8dfe3bf4541&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT4JVZEE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIGxr6dlKIikpDiOKIm1ZurfrDltqVHgitHWgRzoy0QtrAiEA3ej8MzYIgt24oWC1a1VrNso5teUUwfEynVLJ8tGVfJ0qiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNcPiyjT25gqoVvF7ircA6NzZHxVgkbI%2Biz0vvNz9vInvNG76EXYpNIN6y3JBtLHudCfuxVoYDpOCpH%2FujCnb1q8ArXpcPh%2BZEpsX%2BBWC1LOlKYGTOnU0etejLUgJgx4eed%2B6UVywuIceo%2BZankZt6Rd5vRFZaq22nLTEFWH474bolbY7bb6fcuGQY2hwvevV%2Bh%2BeY%2Bt4UzmZM7boGg0h8je6eocdhCzCcstoJSR6XJuywVjUX73hubltM1dO%2FXIPHmyrMfE3WoauBKGXURYczepawBFFOwpTrI766UWk3Wjsl4RtDau8G4%2FV5%2BDt%2BVvwiPJmP%2BWvss6F668q2AAYOEMUKAQdjGUCPObqOLzk7bcfi%2FBPPyEtO9wVmJUEzMbooYuLSVavcCI3ynVJe2S8KI4amH6DX2MIWBlev1RCDNdbr6VJVmsVhMuY4Vo7KS1P0Q72me%2BlJmJQIZhLC9cu6mAdY6rT8SLtSG0sD5hU27PXVzXG74Zx31i%2FCrkH3o%2FLBJbYvOTL3jA4fgbPPJ5%2BHhhzIvrtTpb8BzjpDkrXNj3nWA%2BOkLAH0E%2Bd53rF5qDpZ2KHI3XFRXytWCX6RZ80M5Eodl9R4gJSEQ3IERyPc1mu3brYOMFEeGNdsofCLj9gkWoqf0dV3kk8reEMMDUm70GOqUBYPLbXESqUUPPfRhRb5GKKA2N%2FbcuDKAjf3khqSFXxg4%2F9BJLzsEGJxtbPLWMTfb%2FvbvVTArR5Dlehj%2FaHnsy0%2Bw6sfsdMyqSjynga2jPe1qK9qX2P4nRChZlYOR5qen6a2m1oN6UI0ofnXIwfahnV2TomfY5EuqZ4xorCbQzY1Fc%2FA1HtAGrNFB3Aj9KCN3sC6Aqo8h5YFo8qZOVM%2BJrCbFAQjEg&X-Amz-Signature=6ef3287d00051476d44e0d94fe0ad1d6346ff7a08c6d5b769fc564fa4cd36e8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIATG2K%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIGw0t3Gmq6WrMeDCH%2FYXCW9OXfjnGjIzXJ50kwWtFFVtAiA3sMSktKSJIKGFKVb0Kg1VrmgTUEpaDYa0YEs83SokACqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgMCfb6ryIzkrrldiKtwDm%2Bmcn3XFTIlQdP972lIXerRV9do2K%2FLsL%2F%2F6X%2BOir8CSZrcnBrwHodDl4%2F5%2Btzm6CUj0T9donkEz3SMy1k%2BYRVi43MnAOwNieLiMOCvpREVvWoSej9XV0sS3ZJDcsxiyJs1exIwBvAFZEtI8UtljhOlNB7IniaaHQv2I2a7GFJO5FY6fBTQkqNQXaDKGLSXotlXOOsFBMJx%2BbRZGPvsv3%2BTfEQG%2B6h1lhdAU9h0yJ%2B83pYXT2JVX%2FUppO2HcVOPHvuwbTXeILdo0DHqKeHeDReWvVZhPk6BKPyMAX7FjL7%2FJ4NoxjXXf3eEAhtHehl3EfldAVCyahye3S47OUzxa408Y%2BAl1%2BvC5CvczyiaZKOmDUQFb1tC5txtSSMzqTpVwYt8srfdhVNTd%2FkPKaYEwWr8%2FF27sgxc9ZCfGIj8FM8Ug4ppvFF3cnXXVZGMJPZYITSlbKzr%2Fv72ZvBDGZHcTjJ2OskjocQnKZL3pe%2FaEwAsehxuWUkjNEuOMkSZCW0A4bm290sMvJbNBWkdpzVIfFYN0wqZmMg0or0eg59hQvZ86mlRZ8gkXVyj25p%2FSLA%2FkcgNup7ipZ3EngqF1f2hvWdq81u4yY%2BDoAHQr1xVGetvGNro5b4v4lTv3GrAwvtSbvQY6pgHNwYREKk%2Baz%2Be5m%2Bfua9aZmkkYtsWIeCQd5LHYWo%2BxbAyj3USMmnmVofwX2gyznXqI0lv%2BP6Obu5DNDt8X65TUUXv%2F1mpNrzXZ731LL%2FvBq3GeeL%2Fg%2Fn%2BddRYCoJsqkCPsoBAVAHOiS9nBpoWr1sKs0XP9HMJUVJp9DLYc%2BuKMgzbyT5TEnPRnwmCUvzvqPLLXPIyv7Y3wHfnYOoqp2IL%2FuqZHUzuM&X-Amz-Signature=f17ce5c1e80719935ddc26a26b33931ca42db160d75df8058f7a1cc92ee32118&X-Amz-SignedHeaders=host&x-id=GetObject)
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