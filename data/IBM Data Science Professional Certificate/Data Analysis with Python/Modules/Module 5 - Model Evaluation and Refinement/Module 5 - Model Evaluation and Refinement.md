

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=527ac494a8c77f8e713cfec4824eb8dc183a9d4efc1adb6345618e2390000751&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=ca414ff71829313b51d787a73b9f209ac8853d2bea8e7654ffda5f89d7e7eb9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=67de0bdd3824e3ade6b9e5e4ca52d86b684255c8c0a0a0d6c44e12efe37ce24d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=f307f794a1f195b9d3b3109596b495884c94acad7d36f671904dc2b0bdd04509&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=af371e635a572ab55009dc5e61749b6e09e0494e6347e8c1167584493de1a7fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=7ac9c769bde5c3625630e730fe8a18654a178e901eaf1f28b3e3ba7ff90eaa51&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=8ed95e8c3eabfc86577298ae3dd51d436518fb0d5318ec9a9db11ad851de2fc1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=6147b208a4d46af82fef9206ceba268d26d99119a019f72050fc486d79ac9160&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=1aab7a7b8b244d7da6cebe8ab571df322e708a73dec614273a7462c44e2a03a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XBV7VMX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi%2FjPFUPcz5NhLN3WHwBEc3kWRB9IXnrrmLZnT4z%2FIGQIgLwD86532jFeC%2BrQ%2B9SPWgxziCQs03rmD9w1bNheEmxUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG9W5OYh1UtYTLkosSrcA%2FB3o6OiA7AS1fNFmlcZZHXX%2FsVnL0i4Ik7M3767yJXkEaRMaKiDl%2FZloobBn3nRGhxWxlN6NyRKCW%2FWyCM%2F7%2F%2B1bm9R4L039dRcBjxS4VXsV7dVAKIlIh36V%2B%2FbOjJzzlft8LElYUqUpCu6WoXYGU9Oyzti8sJw7OrlHnvOn1hIaPrLWkYweH2WC2ysuoQX6Bvs%2FS01oXC3Jnsh8zMmlJ0ELx5cBcF3w1i3HhrE7LsztVqlIDXO1RbPw8CFoulyzg%2BArnMYhiHvJ7wN8Ui4rOQYg7lEkgEfGiaUHmeqp9z7BlfZIdHdAJ9X2vvzffPv9vMP8b%2FYI62QlGoFbE4YX13Y4YZhNVguNuFelN4GuttdbT7xU6EqX2iaZ7BPFebTjfndNuVXDDDYdcglJxoFoT%2BhO%2FNEbEybYzpoeurVkSmA5ckex%2FkIIRkHIDaCgvj1i7ZYHGRyQQiG40VzDXpdim4H%2FD1cBCiqff0lS1usenZRY%2BYtFnnLtxb%2FE9U9Og8XLvL18%2BR%2F1bzhJ0c9Bu8y6aSW9lJMK0laVQOtiTSiAedg5B%2BU62ATebtTGG2K49I0NTNsZox%2BXT8yNCQ2Qb9YFluExETRRos5MHEhrdfP4MyaKx6HtNZZYy42x8IaMN2k97wGOqUB9aIm81VY5oTvpLlUtTJZMdAnC1UzNXsbD6dAS%2FwJSpbrjuZ9LWwQhFOHvvlvlgm%2F0%2BIyAp2APQi1z8f2xK8GWDc2XlU30gnnJrpuENxhgYe6ZAZe2DHoDMCApd0NQw1Hc7S6rZ0HN0Mz0yJQEs1UopMOg2hWxhR2KkWDZryD3nYCoNfMHn2tsf6cwypHWxquLrn6gUkbJQ3%2B3Lz9jzcXgo4xltbz&X-Amz-Signature=67c93ddf3bbfc94551ff8ab7f98444b4bd6ad7982e18f9b2df38322ccfbf494a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XBV7VMX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi%2FjPFUPcz5NhLN3WHwBEc3kWRB9IXnrrmLZnT4z%2FIGQIgLwD86532jFeC%2BrQ%2B9SPWgxziCQs03rmD9w1bNheEmxUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG9W5OYh1UtYTLkosSrcA%2FB3o6OiA7AS1fNFmlcZZHXX%2FsVnL0i4Ik7M3767yJXkEaRMaKiDl%2FZloobBn3nRGhxWxlN6NyRKCW%2FWyCM%2F7%2F%2B1bm9R4L039dRcBjxS4VXsV7dVAKIlIh36V%2B%2FbOjJzzlft8LElYUqUpCu6WoXYGU9Oyzti8sJw7OrlHnvOn1hIaPrLWkYweH2WC2ysuoQX6Bvs%2FS01oXC3Jnsh8zMmlJ0ELx5cBcF3w1i3HhrE7LsztVqlIDXO1RbPw8CFoulyzg%2BArnMYhiHvJ7wN8Ui4rOQYg7lEkgEfGiaUHmeqp9z7BlfZIdHdAJ9X2vvzffPv9vMP8b%2FYI62QlGoFbE4YX13Y4YZhNVguNuFelN4GuttdbT7xU6EqX2iaZ7BPFebTjfndNuVXDDDYdcglJxoFoT%2BhO%2FNEbEybYzpoeurVkSmA5ckex%2FkIIRkHIDaCgvj1i7ZYHGRyQQiG40VzDXpdim4H%2FD1cBCiqff0lS1usenZRY%2BYtFnnLtxb%2FE9U9Og8XLvL18%2BR%2F1bzhJ0c9Bu8y6aSW9lJMK0laVQOtiTSiAedg5B%2BU62ATebtTGG2K49I0NTNsZox%2BXT8yNCQ2Qb9YFluExETRRos5MHEhrdfP4MyaKx6HtNZZYy42x8IaMN2k97wGOqUB9aIm81VY5oTvpLlUtTJZMdAnC1UzNXsbD6dAS%2FwJSpbrjuZ9LWwQhFOHvvlvlgm%2F0%2BIyAp2APQi1z8f2xK8GWDc2XlU30gnnJrpuENxhgYe6ZAZe2DHoDMCApd0NQw1Hc7S6rZ0HN0Mz0yJQEs1UopMOg2hWxhR2KkWDZryD3nYCoNfMHn2tsf6cwypHWxquLrn6gUkbJQ3%2B3Lz9jzcXgo4xltbz&X-Amz-Signature=152d7338c4ee6e3308df85b42b9cf2857590ab677a9efb5680f9b6b39575bbaa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XBV7VMX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi%2FjPFUPcz5NhLN3WHwBEc3kWRB9IXnrrmLZnT4z%2FIGQIgLwD86532jFeC%2BrQ%2B9SPWgxziCQs03rmD9w1bNheEmxUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG9W5OYh1UtYTLkosSrcA%2FB3o6OiA7AS1fNFmlcZZHXX%2FsVnL0i4Ik7M3767yJXkEaRMaKiDl%2FZloobBn3nRGhxWxlN6NyRKCW%2FWyCM%2F7%2F%2B1bm9R4L039dRcBjxS4VXsV7dVAKIlIh36V%2B%2FbOjJzzlft8LElYUqUpCu6WoXYGU9Oyzti8sJw7OrlHnvOn1hIaPrLWkYweH2WC2ysuoQX6Bvs%2FS01oXC3Jnsh8zMmlJ0ELx5cBcF3w1i3HhrE7LsztVqlIDXO1RbPw8CFoulyzg%2BArnMYhiHvJ7wN8Ui4rOQYg7lEkgEfGiaUHmeqp9z7BlfZIdHdAJ9X2vvzffPv9vMP8b%2FYI62QlGoFbE4YX13Y4YZhNVguNuFelN4GuttdbT7xU6EqX2iaZ7BPFebTjfndNuVXDDDYdcglJxoFoT%2BhO%2FNEbEybYzpoeurVkSmA5ckex%2FkIIRkHIDaCgvj1i7ZYHGRyQQiG40VzDXpdim4H%2FD1cBCiqff0lS1usenZRY%2BYtFnnLtxb%2FE9U9Og8XLvL18%2BR%2F1bzhJ0c9Bu8y6aSW9lJMK0laVQOtiTSiAedg5B%2BU62ATebtTGG2K49I0NTNsZox%2BXT8yNCQ2Qb9YFluExETRRos5MHEhrdfP4MyaKx6HtNZZYy42x8IaMN2k97wGOqUB9aIm81VY5oTvpLlUtTJZMdAnC1UzNXsbD6dAS%2FwJSpbrjuZ9LWwQhFOHvvlvlgm%2F0%2BIyAp2APQi1z8f2xK8GWDc2XlU30gnnJrpuENxhgYe6ZAZe2DHoDMCApd0NQw1Hc7S6rZ0HN0Mz0yJQEs1UopMOg2hWxhR2KkWDZryD3nYCoNfMHn2tsf6cwypHWxquLrn6gUkbJQ3%2B3Lz9jzcXgo4xltbz&X-Amz-Signature=b68bc9cd8ba10bdc12852faab102e79c155533e4273dd3d7d77123f81a0132f6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=8a29c820cf772926b711ca8a69f67e3a3fce61dbcb9f0ead61061bb122413d30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=edec751c90f72ec91c13486c0a12612782ee59bc1888e11edffad6683dce04c6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=67bbaf70894374313c10a661a7c5bb819ee468b20a098931672eabaacd65b17b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=669de17a64d44c4f71773faec7cb6c6c835dfb986984a5623db21f065bc423ff&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=4039d125c8846733305aaa2a12b593f48c8a7a60ee470684605328c6312cce3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGKJBXJA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCH%2ByrUZ0OuvtgRCuyCz4U5UUDHbxFL%2BYCFmc%2BAkYTrXQIhALl2Qw16xoXAGDa%2F0tGUPqdr4zYaxJLk7TolHn8Q%2Bmz6KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVIHuaLGznamwj0bsq3AMZXH0OLwEux%2B81sCi77FgzXld6keVdf21XEzOYe%2Fz%2F8nyhXDtu%2FY6hWB6%2BNZ2G7GW%2FIiTTOs7bbi3WIRtfcm89dbhAwsd36SouqosNihyAoob%2BMGwfcWqWhEV6ZdklT%2Fc1zFhwOfKWpgKhXAjFgAyU1QsB51fn6%2FhNUCtzHUuZi%2B6GBvOOk6teWp7QiEirY2T30TUjq5QbpZuk3zeF8S75rmeliMiv7iiLkbJmdZEpHPIjFjvQKjyz2gY1esU81hysx%2FeM047guYaOu%2BHKHISOqEphd65q8PoDJ0rj8L%2FGoY%2BbhVOgrnzd%2F3O1GFfiX5L5M6u5nLAPgJm8NZfjYITaBjSGAQYpEYd9xkcqrYwyFDzYbZ4RQ9Amp0UtrkgcsMVYPEkPkbks%2FFXxF2RKjuBVK8ZeT%2FS%2B6pFzgZRKk9ba6qJljNCP13Tu73yFaVz97vV4NqOimZtxmsBOVIdQUW2ULXO%2Fw70UXhVOJSdZDiKnV7kNfeFZa0Y3uT5Ovomtn3Kg7D3zkpJUS0DgBH2M9T87pzLwKH1EPz1qcTAtZTRXBgxAW4blakcijETtCgwtwEAKFxvyh27IX9w2j1zx8WPhjh6l1tv2Fww0cbs6iMp1ppF693seRRnNKfZTITDBpPe8BjqkAUaT33G0qe4Ew3%2F91sqVKBJW5bIafa3yDBo%2F2jYWK6btx39tPfGdof6UwgV8gJ6jRkP3xW5K4M3Y8p%2Fis0l8sc%2FAAHw92FefE3JTVCq7CNOxRX9CLwi%2B2mj39bpM6hsYaxkvR2fo5YLtLYkz%2BeiXnWT8sgouv09XqSFV3%2BVlc%2BTFTl8kktlSKUV6a5qn6WTGL49nUunYF9X4rapAEkbpS9stFviV&X-Amz-Signature=78de576a1d4b2a36833d305b178c11b8b45104468afdb67a518f2156cf97e32e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUALWLI3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQx%2BDp3t%2BD6%2Bvd5RI%2B5rZTyUbMyTnxQjh2HeNOI26LaAIhAO9Swj3jzZuaDSF%2FgcCYaAoivKGe5v8v2qUNfE0656bPKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2Kqgcs6Lv6GvnQloq3AP%2FrBAe6%2FFake%2F5GDhp%2FcQrs04bxdL6nG%2B4KwPt48GgqLGOfWDqrSHkLd9D1bObHzcbaDPhfQnwNcgETceJrYHdYxShqJldQy6wSzUiwxpzGX1SB03jZSWn6049FHVvh5sNOgZcPpiee962k%2FLYhgIeIs9sa1FhMs1LUF%2Fp7hXGeg2ac%2BB2a%2Bb5%2BrpaoR7%2FSGpmtMNHWpC58l2hrWlJeCmHfAEOSAyGzwBYYCOepXyUfoomMsWWMd2%2FTs67lMo1rwGM%2FoWdLEDcV4dbFIi2qUhm9wHi%2Fnerv5%2BrzWZJsdD8XSo5qJ87Klz7uh%2FOnFvLax7XM9OPE323qn%2BUSX4a66FwzPB2hWFtgNLOA1QnFDKh5k0Ro5VI1K%2FpS%2FvC3Zfbhd87zoGRqUlEAf0ZUPu2biv1pAjD5pQ3PHxYB3m9ZgEhZ%2Fz8FRgNbV0m3F5TZf2qlz6xUfkE%2BWTONeX7HH7Z5s%2FJ6uXIwb95fbStA%2Bpu90tAubOMleAldIQ52ZlpsNd%2FCgSHhqT%2FhfZMiZph%2B4TuCoPJQwXpGaBmGcRabTa55JGagss%2B0F9DGEqzwR3qL%2BhmHXj3N5XbrFZwupJCgYkhDb9k%2BSOY6j1%2BOcFfDNPglS1jm7c%2BPXgb2Ex5ZokfhTDmpPe8BjqkAcZX25x865ovt3Uhq8HeZzqBMWCoOMX4zEUWW4Qv9iiIBhPdagUyQqNLoySGAlmrPDht6RfdUYYsx3jJM%2F7u7bXxim8RipJNLjGL%2BW7VpgPbR8m2wRCIbk5nkdq2Ua8YeqBOjUnulYr9lLtA4XAlxdh0OdKlb2KGkbmmJf8jRoLD4FnL7O22Crxgnmw0npa1lbHl20Rxdg%2F3kbdej5bso6pr7rX%2F&X-Amz-Signature=ed03de345e22702bdc8d654e846dcc1e4b73251e33cb3deb9d1379d1b15d1f3f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUALWLI3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQx%2BDp3t%2BD6%2Bvd5RI%2B5rZTyUbMyTnxQjh2HeNOI26LaAIhAO9Swj3jzZuaDSF%2FgcCYaAoivKGe5v8v2qUNfE0656bPKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2Kqgcs6Lv6GvnQloq3AP%2FrBAe6%2FFake%2F5GDhp%2FcQrs04bxdL6nG%2B4KwPt48GgqLGOfWDqrSHkLd9D1bObHzcbaDPhfQnwNcgETceJrYHdYxShqJldQy6wSzUiwxpzGX1SB03jZSWn6049FHVvh5sNOgZcPpiee962k%2FLYhgIeIs9sa1FhMs1LUF%2Fp7hXGeg2ac%2BB2a%2Bb5%2BrpaoR7%2FSGpmtMNHWpC58l2hrWlJeCmHfAEOSAyGzwBYYCOepXyUfoomMsWWMd2%2FTs67lMo1rwGM%2FoWdLEDcV4dbFIi2qUhm9wHi%2Fnerv5%2BrzWZJsdD8XSo5qJ87Klz7uh%2FOnFvLax7XM9OPE323qn%2BUSX4a66FwzPB2hWFtgNLOA1QnFDKh5k0Ro5VI1K%2FpS%2FvC3Zfbhd87zoGRqUlEAf0ZUPu2biv1pAjD5pQ3PHxYB3m9ZgEhZ%2Fz8FRgNbV0m3F5TZf2qlz6xUfkE%2BWTONeX7HH7Z5s%2FJ6uXIwb95fbStA%2Bpu90tAubOMleAldIQ52ZlpsNd%2FCgSHhqT%2FhfZMiZph%2B4TuCoPJQwXpGaBmGcRabTa55JGagss%2B0F9DGEqzwR3qL%2BhmHXj3N5XbrFZwupJCgYkhDb9k%2BSOY6j1%2BOcFfDNPglS1jm7c%2BPXgb2Ex5ZokfhTDmpPe8BjqkAcZX25x865ovt3Uhq8HeZzqBMWCoOMX4zEUWW4Qv9iiIBhPdagUyQqNLoySGAlmrPDht6RfdUYYsx3jJM%2F7u7bXxim8RipJNLjGL%2BW7VpgPbR8m2wRCIbk5nkdq2Ua8YeqBOjUnulYr9lLtA4XAlxdh0OdKlb2KGkbmmJf8jRoLD4FnL7O22Crxgnmw0npa1lbHl20Rxdg%2F3kbdej5bso6pr7rX%2F&X-Amz-Signature=f4ef36c262360daa6cafc702e3cc29cff6998b506fc3602867ae4670c5598721&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667NL2GCY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdo%2BNoUxrEH9L8mNwnW3rFyl2Az%2F0bHgrNSnnchIIGSgIgKXRgBIDsc%2BuWiv5VX3Ee4rhhPBWvQak2OKkT61ugDbQqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH85pTjdaOdnZPtyiCrcAzfkLjUGG2y181hKFO5b2XynunzQeRPEZ9oHJq3ajvDR%2Flkvk%2FtlksGhkL7B0eFgDE7FpCesztfGOsdV5PDoFnd%2FbXVU5OywG4dYtE1XxV6Hb9uKMovitLMItZii59gB0xBel1erbBldxKjAzJ%2F3gpZeaM7bE4PpLP2UAkEwXN5E2mIdwUPO6l7EMGqom3UASCjaTky8bey13DY2UzThvlal%2F7HAzR8efN3ZP1BtWMLrDA6yyHLoHD8FkAXz4gsKTTQsYCarpfr5Z3ZZHnLHpdtVDXJv5Px76hWaBaGEA3hEwdBoL%2FrMH0fxLkxHE82OlMY%2F%2FbV6bTE7bJQV%2FN17%2Fab8tUvr5zDI6HPEloTjVNLl6RyXpY%2FD6E%2FyH9CKEgDfQ2Ze0tY2gBLIPo1wS8UkLKm5nVCnrl4VMmjoDrHaxhu3NOGkcHlcqyUTSeETA0E%2FiiXTXwVVJld13hA3XtO33AW55zVFM5F3gH20XjabgNECUQktSzfwh0u5oQhg5be3e8MPfycCW7VrTkbXR2Xi6ZMfbt6eCctCBo%2F3BH8MERZmaYEGFhmoOKlPC91fOgW6oiHrsS1g%2Fto%2FLo64DqGOU9i2PFojYZDsgRsVErn9BodUSTkE8KkbmlqeQhMAMLOk97wGOqUBWiXtYHMVUWQOwvPTCoXvMwmpxloR%2FdfKNBvZESTfC3G%2B5%2FdfjUbLyT7rG8OaBW6cNJuhjeoP4FgfxRkpefdruDTT3KoBn2rthLPmIGCVTBYGUp5LHRlbDWXCgxjpoF4EwOIDi9K7g4343n%2FICCcPUdeXttRcgKV6AO9G7aMPJ5ZVETexDZLz57o0vENsh6UATKA%2FUnGdrcQy18KPniMtg6DGL90c&X-Amz-Signature=21769227c37baa4d70f32aaada51c8159652ffd9b5fdea37f543fd67181b0bc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34ALNKF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Py3HhTD2BU09i8g7oxd1OsZHtm5DjivSptuQSMs8FAiB2YhLzXBRxrQJsYRo6Svqp3skgvWRCij98EepVpknYlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUf9E9HzqaGxFDUkKtwDUlf0fIXxen09Wd4PHYlb1RPaRnV7VGno%2F0vGPt6zRHUp5TsBDMeAUdp5HuUTdqCMABzbM6mmtsGveDwMNwwU7amVPok93aQuAZUrxvnQLIffHrSI8SrGXZ6Y92dKjIe3GpD%2BsipD37lbff5ntQOYdraPZ%2BRwrAuhx3OKFHSQrGtyGoNnbApY7eGDCzc4iJYYdQ7PDrrsfJf4y%2F5Hob502gg6a9vdsoE1f7m1cShB2s6bQjE1AXRFHs9wRmrTs8stnMwbYPIB%2BBDuW7%2BHbJbf4DsE6Y2pKjxigsPgE8ykST4t9UKQWOw9uWhaM0QD6H8lW8BrBhqBW4qArWgo1%2FBwIaeCjMy3UEiMvOJUvkB%2BAuHIeU1PiMWysOfqWUgfgV05FibkPvR34IQrSMzVEsKgY1J7ngOj4Kjxflqr55k180ratJrfonJ3SNC0Ya06iqD7XJkh7mhvCnghJxYDsojCfb6VP8dafWUzs8Lf3Y%2B%2BXcExwnj8sft7pAObeluh436cL5QZuvS14v6XwaKxLw67C5tEroCfJsFR%2By3fsL0tUmong8pNq1O422w5OoIjAXshUulqfhILG9iwn52APeDeNRUTEg51MWZLDXtMznHtHJ7Yp94HjME5sCXmTFIw3aT3vAY6pgHqmFY67rBJqobpbizHvNNXW0xX2Nzi3Md2dewQjnSrsoEMRivc6YHbrU5wLpxiszJMg2rApfwxtmB77MizWkvL8xMzWiw1VAjWYgcV25njwbWYYYnKFGQbJssJ3HO9jvzLxRHInq5pHIrRZRz4fWiqb%2FigCykBQYM8boJLzThVqzbIRcrKZe8ByVuv0nxj0%2BQyOzDCXlfP5tOCNamTZaMDxgvec7Sb&X-Amz-Signature=ba27aab0b62e045bc49b83a8f6cfc6e4c158e81860f5300df74e4193c620b5e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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