

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=a71bc04dbfcd27b838cb709c5b0f5de5dc2d0fced8d94e38a87dc2a429b46883&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=220e89814894fa9ebd6ce78679fec022cfc98b777d79a407c3f6e3dfa6600ff3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=36020139fca3eca83f6a72ae48444ee108353f10915c50f13e5b679d48e52e65&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=da9676a19fcc661dd02827017264491418ce454a03bbd98ee83eb10cadd2b5fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=9bdfc3dfc39a7afc4feecef9b30bfe72c52b67624c5cfab6042abd228a66ae06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=74450d90e0f6bb2df199c0afb94cb9392864c49337e980c12d8ee5133b4eab9c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=8e4b5a64fe966ed2664d794178255cdb2bce64933587fb3193774ba02ff1cc1b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=7f8fb6bdee005ce4e7bdf3454d2dce98849a8c02282828b687eb73cb49019971&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=b22cc535da762d8eee31752a9831ae7134883e516776ed5352315fec0c7c8751&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQVHS3CA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICy0PGvlI%2FD0AyPLkSx8tjJKDzuDdGPCpcF12HaYrYtpAiBDpz01jxHakT%2B9XIWH6SBfEm0hjrBkrEEc4U%2FPDb60Zyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMmQLfuERwX8BHiofMKtwDFpZJgVWAQFNLhbErSNX02c%2BfBGyGUUFxx9TWJmdYCVw3eYGTWalQRGil08xRBRbRf7NBmDisJQjeITWWpD%2FPEmoDa60hHRAAYaEY9KuHjbgUZuDhEDpTjoK5GCHk5dDo74Oe7GkkPD4pGMIgGnaglfilBWJQ5cxxZBL2zOz3yL9k%2BpyDFzxeURoBFQbBYKqIq2I1c8al6lGefLEEm3wTN4xNN9SJqV%2FjoixOqbAh0lP4DZX%2BHmtP62edQD0keBp5QCtPnerJJEO7nQlcaMMoCiba3ervXsMdgwvjZEWONrBfmllwjj3UNPH%2FXX3A%2BDzTVNrfgIqqo%2FVJ1kDhEpYlhKkjiYEGwE4MXtk1b20zuLG884H4MqTXtqM8JfYQXF2aMe7kzb6O%2FU%2Bq3XT8LI0RTv7HigdHq6OvW%2BHAlLpIikpLewUPaTnYumTwkuc0rWrKTvSwmn51us3hSHaPOLt%2FG5eP3agpsoyc7%2F5lmx4L3uu8x7C62rnedNB55Gtn3lA0bmlK2V6IZg32m1EbU8vcKEAWmsnN1fslDqpWtAJzvPUp0vg2haF%2Ftt9AK0qNUCdCW%2BscJIiniVnw7rBTCYs%2FU5MzVn7EVC56Bq%2BiNdierC6lTiXo0pHJZmaDkA0wm%2FqWvQY6pgHGuNMdb1PpG8EnFlBMU6zrqskgDq4UiRNRMu%2FbMRYCxr34%2Bv8bv0EYO7C0RJX25Tvkg5AUUUCJAw4gMYic3BxoZN1uf1o%2FydMyE1s6%2BrOpdVSbB143nmDWvh2BU%2FJyWglW0nJWEfpewPXkRJP3FkwJwyxRmED0H%2FsE8plT9oDh1TibegkUvzuPjWHjEYlrCj%2BGDy1WZi1iXMNFNmBWyfUoijOL4uZc&X-Amz-Signature=e148c06f4bc5a891e004a45fb239298839b95ffc726d35af48a12b0852bcee2b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQVHS3CA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICy0PGvlI%2FD0AyPLkSx8tjJKDzuDdGPCpcF12HaYrYtpAiBDpz01jxHakT%2B9XIWH6SBfEm0hjrBkrEEc4U%2FPDb60Zyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMmQLfuERwX8BHiofMKtwDFpZJgVWAQFNLhbErSNX02c%2BfBGyGUUFxx9TWJmdYCVw3eYGTWalQRGil08xRBRbRf7NBmDisJQjeITWWpD%2FPEmoDa60hHRAAYaEY9KuHjbgUZuDhEDpTjoK5GCHk5dDo74Oe7GkkPD4pGMIgGnaglfilBWJQ5cxxZBL2zOz3yL9k%2BpyDFzxeURoBFQbBYKqIq2I1c8al6lGefLEEm3wTN4xNN9SJqV%2FjoixOqbAh0lP4DZX%2BHmtP62edQD0keBp5QCtPnerJJEO7nQlcaMMoCiba3ervXsMdgwvjZEWONrBfmllwjj3UNPH%2FXX3A%2BDzTVNrfgIqqo%2FVJ1kDhEpYlhKkjiYEGwE4MXtk1b20zuLG884H4MqTXtqM8JfYQXF2aMe7kzb6O%2FU%2Bq3XT8LI0RTv7HigdHq6OvW%2BHAlLpIikpLewUPaTnYumTwkuc0rWrKTvSwmn51us3hSHaPOLt%2FG5eP3agpsoyc7%2F5lmx4L3uu8x7C62rnedNB55Gtn3lA0bmlK2V6IZg32m1EbU8vcKEAWmsnN1fslDqpWtAJzvPUp0vg2haF%2Ftt9AK0qNUCdCW%2BscJIiniVnw7rBTCYs%2FU5MzVn7EVC56Bq%2BiNdierC6lTiXo0pHJZmaDkA0wm%2FqWvQY6pgHGuNMdb1PpG8EnFlBMU6zrqskgDq4UiRNRMu%2FbMRYCxr34%2Bv8bv0EYO7C0RJX25Tvkg5AUUUCJAw4gMYic3BxoZN1uf1o%2FydMyE1s6%2BrOpdVSbB143nmDWvh2BU%2FJyWglW0nJWEfpewPXkRJP3FkwJwyxRmED0H%2FsE8plT9oDh1TibegkUvzuPjWHjEYlrCj%2BGDy1WZi1iXMNFNmBWyfUoijOL4uZc&X-Amz-Signature=665301d6d0610cb13acb2a4b5e5c85dd546d35b727990eb1502b827cdcb50c45&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQVHS3CA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICy0PGvlI%2FD0AyPLkSx8tjJKDzuDdGPCpcF12HaYrYtpAiBDpz01jxHakT%2B9XIWH6SBfEm0hjrBkrEEc4U%2FPDb60Zyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMmQLfuERwX8BHiofMKtwDFpZJgVWAQFNLhbErSNX02c%2BfBGyGUUFxx9TWJmdYCVw3eYGTWalQRGil08xRBRbRf7NBmDisJQjeITWWpD%2FPEmoDa60hHRAAYaEY9KuHjbgUZuDhEDpTjoK5GCHk5dDo74Oe7GkkPD4pGMIgGnaglfilBWJQ5cxxZBL2zOz3yL9k%2BpyDFzxeURoBFQbBYKqIq2I1c8al6lGefLEEm3wTN4xNN9SJqV%2FjoixOqbAh0lP4DZX%2BHmtP62edQD0keBp5QCtPnerJJEO7nQlcaMMoCiba3ervXsMdgwvjZEWONrBfmllwjj3UNPH%2FXX3A%2BDzTVNrfgIqqo%2FVJ1kDhEpYlhKkjiYEGwE4MXtk1b20zuLG884H4MqTXtqM8JfYQXF2aMe7kzb6O%2FU%2Bq3XT8LI0RTv7HigdHq6OvW%2BHAlLpIikpLewUPaTnYumTwkuc0rWrKTvSwmn51us3hSHaPOLt%2FG5eP3agpsoyc7%2F5lmx4L3uu8x7C62rnedNB55Gtn3lA0bmlK2V6IZg32m1EbU8vcKEAWmsnN1fslDqpWtAJzvPUp0vg2haF%2Ftt9AK0qNUCdCW%2BscJIiniVnw7rBTCYs%2FU5MzVn7EVC56Bq%2BiNdierC6lTiXo0pHJZmaDkA0wm%2FqWvQY6pgHGuNMdb1PpG8EnFlBMU6zrqskgDq4UiRNRMu%2FbMRYCxr34%2Bv8bv0EYO7C0RJX25Tvkg5AUUUCJAw4gMYic3BxoZN1uf1o%2FydMyE1s6%2BrOpdVSbB143nmDWvh2BU%2FJyWglW0nJWEfpewPXkRJP3FkwJwyxRmED0H%2FsE8plT9oDh1TibegkUvzuPjWHjEYlrCj%2BGDy1WZi1iXMNFNmBWyfUoijOL4uZc&X-Amz-Signature=2942846271dc1305ba2b2dfb7ce64095bce6f4e561aa7ab2211b43f008f30943&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=3f856c5071b574eb4f12c4db3af5d4f6e78846f015b92bf11ecaa98ded752c98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=77c9298e4aaa5495917bfe3851c7c4bc04cf4a984faea43ff1a03b2b9f4302ad&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=9e704c35bc8c0baa3257493311cdbd513af220e88dcdaf4693a56cabe4fece25&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=7718c4349f98d08a5df3da504018ff4f4c410cac08ada464a3e38219d910d7ba&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=9791e9d17008f32a70e0f0107fdae3eb3f640b05069b6abe24ae9f7417249adb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4M532EA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIF6sPIIPVan%2FXtaxwdf1QiCEJRJm3B0oBLLNO7wUvTajAiEAoJkhjh7Z3lT9FOn5hCQ%2Bd1C4sNlrWG7NGdvlG4rVBUcq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEA6fI%2FF9tMjRM%2FDeyrcAzcXXCCtLg%2Fb4wWEKdM4RiBrDPQYOVEQAzERjg80HszyTnS5Pv6wza6J9fHnxbarMwdHp4ChE1RUkQQDL8jTYcXIzNSmz1l1RleVQ29mwiL1qaRi5OO6DOunEtGsL%2B2xdU4k2GAXfXuWGiG14WLUzVBggGf2T3MJKtyhRRtgRo%2FyaEJuGY%2FOapnC7EP%2FVqBtJMkm3mOqPZH8gcTq5BqQRkb4gEcAZwkEiVyvGqXiYI1CkC4jjiEVnVyPwuzyCXlTp6JXDxi%2FanHO3VmF0UTp1ipNqqs7Xepx4otzzGsdRFLgcd66qmMGI4XRTRqJgwvrHvxqXCekfM%2BNyqX0sYmKiQIdeGwJWCMb5dq589kOkJEwniiuU7EGvT9RvXNIQ1o8JBu66%2BXDxBrTPyNuvHF%2BFlLF6zmGrwvrmiIipVbt%2BVCm6CIyEKsIFu7jz%2BR%2BNdrwn4OngVEte%2FKJ8IbrslO6NThFOsQ8BXwGxG4KEdhbNZtfRnsUUPWVTDIUbf%2B5zQjucCV%2BeKCl6zx1sO%2BfKH2oxllAW3rOxKSLO7WCsFKLlHIG22VN3m9bFHTFwj9uA0HoxppZ6k%2FAtqyzVXy5rnhGIfpdlaXiZvx4xml3IKUZZkJqCoRcvpSSWNNaIP6aMLv5lr0GOqUByw%2FrXaByAB2QpukyOmmCVB3fJb9S%2Ff1prkixLZUjC4sKwYXaQK85rnN5DH3c0HPVcmVw9pfri6VG84Ic1ar25F3Urehz%2F7Hueh9uC7BZHe1R4s9OZyVgK6SkGKXP4v6YvafZgY6EyP2hv0esdRwZ56j%2FXL2IaoOa8ZMkN44aGKRzUN1NfAxZcf9VDV9rVFIu6f%2FoUO0gLwwLtC8JVaCckdPg4bgd&X-Amz-Signature=5197ceb45c90ae7f6866fe50aaaa456fc8dd29829cc254390b18196a545a2a0e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHNBLS25%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIB5PR6Tl4DOUZNjsnvWcsXB7B1roJTXvO0tA9IvxMxyuAiEAuB6eU8vopb6Jw66Cpevxfa6OOUr9sOysRPVFOkFEBpIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLEDz8IMfgsah3AZdyrcA3UgSinj9U%2FKKzHC%2F%2FdRsKr2sTQL%2FaytGm%2Fsd32Vl9JajdETJUbPWnIR9THChVB5W7BzgOYIIFd0sBcihQx68HwhNrHvUnnzpd03EDx7O7au08kLJMVoYASDOFETkWlEE7jl%2BL4Yvp8ztyWrT29I%2BogSv8VFgq3ub8UvIl7o%2BmDFxUDYKTflGw5r2s%2FKF%2FxZ0TzdZwq%2FUxwbMI4CW5tpjOk%2B50F4vekqRVmIe7jsZeE%2F1%2Fr4JJ%2B5aO7jwGZnrZfhRHRn2S2FvINf55apkNTuuW3QWjtzulQzBzSI86axAdU9fDFhQab30a50fbxEwNafye1nF4vjjwM8bsrIDFkUmZ0r4mZEJmkyrB27f6Be%2BWqwGu2YwH6c5hXAPR4%2F9Ya7OLkmNB4S3gHfdTv9ywTTeuGg%2F79quuQE4WT3%2FfZ4%2Fs3FisbiiADiCu%2FxMw4IzJ6%2Bh%2B95Oh3N%2F85IdMiDZ76lYjspQZK0Vn0zCTHpqpdD6QOj3D%2FlehEq1yFEgSlbniUTgqYIXwaqmrCPFBHFq0y1VQaFGsSFnWr8PVpDuZ%2BXsMzwyQ8G7fdYr74rlPKp%2FfhwFF7kT9iN4pBeDHkYPtZ0OQXQC3HXTacQkx%2FLIGyIYW1gV5sQOXTLn6xKTYy2MIT6lr0GOqUBByap9aF7lwayRNOC9AfAn455JOZ4UtrJDIntCdFdKaDChf2pAUGYtCzyz1JEj%2BZx6TQN6C5L4vcBtCD89vjyR3OwFb5hLvwcE0Hf0AAiA8e%2BBfTJ5e6o5KVD%2FQoDRrtKbqQJuugjh5WrWXY7ucb0MANWPI0N%2FkFUbeviMFmYRZ2ECFBEOKnTETYIAf2agzM4W0KvzkOnO62QupNrSj2h9KMCTfp8&X-Amz-Signature=b834c8d574683012f4746cc8ef80b093836ae9ee8ff7d172715cd67dc5883386&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHNBLS25%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIB5PR6Tl4DOUZNjsnvWcsXB7B1roJTXvO0tA9IvxMxyuAiEAuB6eU8vopb6Jw66Cpevxfa6OOUr9sOysRPVFOkFEBpIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLEDz8IMfgsah3AZdyrcA3UgSinj9U%2FKKzHC%2F%2FdRsKr2sTQL%2FaytGm%2Fsd32Vl9JajdETJUbPWnIR9THChVB5W7BzgOYIIFd0sBcihQx68HwhNrHvUnnzpd03EDx7O7au08kLJMVoYASDOFETkWlEE7jl%2BL4Yvp8ztyWrT29I%2BogSv8VFgq3ub8UvIl7o%2BmDFxUDYKTflGw5r2s%2FKF%2FxZ0TzdZwq%2FUxwbMI4CW5tpjOk%2B50F4vekqRVmIe7jsZeE%2F1%2Fr4JJ%2B5aO7jwGZnrZfhRHRn2S2FvINf55apkNTuuW3QWjtzulQzBzSI86axAdU9fDFhQab30a50fbxEwNafye1nF4vjjwM8bsrIDFkUmZ0r4mZEJmkyrB27f6Be%2BWqwGu2YwH6c5hXAPR4%2F9Ya7OLkmNB4S3gHfdTv9ywTTeuGg%2F79quuQE4WT3%2FfZ4%2Fs3FisbiiADiCu%2FxMw4IzJ6%2Bh%2B95Oh3N%2F85IdMiDZ76lYjspQZK0Vn0zCTHpqpdD6QOj3D%2FlehEq1yFEgSlbniUTgqYIXwaqmrCPFBHFq0y1VQaFGsSFnWr8PVpDuZ%2BXsMzwyQ8G7fdYr74rlPKp%2FfhwFF7kT9iN4pBeDHkYPtZ0OQXQC3HXTacQkx%2FLIGyIYW1gV5sQOXTLn6xKTYy2MIT6lr0GOqUBByap9aF7lwayRNOC9AfAn455JOZ4UtrJDIntCdFdKaDChf2pAUGYtCzyz1JEj%2BZx6TQN6C5L4vcBtCD89vjyR3OwFb5hLvwcE0Hf0AAiA8e%2BBfTJ5e6o5KVD%2FQoDRrtKbqQJuugjh5WrWXY7ucb0MANWPI0N%2FkFUbeviMFmYRZ2ECFBEOKnTETYIAf2agzM4W0KvzkOnO62QupNrSj2h9KMCTfp8&X-Amz-Signature=86f963b767d9db614cfbc50adaba06ce0fe22f0402063feb4de6c3511ddb6aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625Q4Z5T2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICThSL0RlMbPt9TeGOOvWmBM3bXK4J7DyBqiacGNZmvVAiEAzqtmf%2FwC%2FdfkyeZMImqBeIhrA9BPae6DMn27ZpMP1%2FQq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNqBEUSnU1FEAlzxAyrcA3L06YZMmdJ3uXMuWqg1ZaXVaVTAyKburGJRs3KFYNT84efaRn20Vh1EwSZn%2BZRLl5zctH0R5WYp5nGc2XD%2Fytn%2FykkGkJhf%2BljjlZ3PEfdEY60EwD%2BwS%2BBxrCJa%2B6fNIsg%2FOSSRJ6z6TE7Ym5S8jsVQQhRfGF9n%2BWmGihxtrac72D730L4F5C41j2ZRTJoPKaoX1B23z3JPk86wSBgswAf%2FVJd1vX3eN9hk81OBq%2BJnIHCni5GzNdiKaTIZx1aN%2F2tWs3pY%2BEnufgwimYqiYkjN9y%2Bl449wvdDgbfAqLSxB8fNfdhKfTJJEvC6rbmfap4AYiYNBszLrecQh3PJfioec22%2FlI2%2FCBsgN6ENG8DSzd%2Ft%2FMfKqjvnO3im5cvnTzy71mYz8MnKq%2BSGdhNMB5aEFHVhXoOTnOwmUoE%2F2LvoQqms4iMKAojZRi%2Fe%2FYzY5ssxKPns%2FesIKEHpGx7se9lz5PuOU9W4qtJ2reHkbhOMlYw18BjhWf%2BSe%2FIdyoFMwQ%2BvRuWi7BwgP%2BPIRlorMv4yfCrgrkyInPXmZBIyA%2FgF8tgtYbQbpNtB9cxLBjxV%2FccAURBmlZyjFFezsqK5RWRzloppi9fYtuAU0%2BrpXljnYAwukoD%2F4TA%2FtFEDKMJH6lr0GOqUBwbjr%2BlYly61iJyhQx2tknfHERDLx1SXatcID4E0Xi%2FHkkEYrngwIC4j4uFvDPc%2BGGtWE1MsnfjN689pqym4ZGaXscYEs4Xs%2FpxtcusxFe2r1Nnl590%2FQJ6iXBIdOsYQw8QKU%2B9bKWarPZXCek%2B85m3BeDLvtcNcu%2BAuk%2BI9EYHSM%2FlgMnauekA%2BPy%2BTsPTu9iwjCQYULBLkYQT%2BEp8tfDEP6OsPb&X-Amz-Signature=7c877421e4029c00733ef57ff7c5563add0f8520889d8406e68620341c33206e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JEHN74M%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDE4kvj3zTjpuDD8rSXAGlAJ%2FW1ZohpcVuyYHUOPWiXbQIgW7rKqN6QWTPy3ZByvkwfUGm5tBsqSfnQu3MppTfvwiAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFyl6hygoFp9cmzm9SrcA%2FyS4xocPUZ7iyjcn%2FUPnuTRyuXfoE5Zl76P9%2BfmHbll5ZyMOyPfZxPu97iebpQkcTtnXhdhdpLvAvV1uhtyzPrrncqaQf3CgZyXeQw6Y9kr2f2vBw8B0qhQrlab3ouGDJGFmcQeRf%2Fgjp0dVm7Vgsnnjtbe37IDiCFWPHuD6mfylIz4BZzNpUXSzuU5LIs9TNO3ThzBHAQreOKE1SeRUpxWEi8RLtZR05pSemkonE8cfJolafeJEYKh%2BmACtjX5WeYLei81ug2euC3jk%2BDjpvxCZ57vzqW2MPeelUtk0b06qRBJ%2FptBwsY5p9cDWZ2aIVMCR3bD5csw1QX1p5WPckh1nWIC0JBE1DnysFQNH4UxldEiyG0CG3TH11%2BVXqvMZjTj6%2Fvq6U0GIh4I0znZz%2FJkZvLSONiQ65vxVXwO%2BBzdM46a8sCFMw%2BKs7fTt95tnRmK0rYBRoi9CDCt%2Bf0mMFLhTO3CoXjoPqZVVbvEm%2BHwwd4nOEzJ8pOvi88xrAxqoKeuT4a60sBqyKwU525ZFmAq9q66wKDdT3NcbhFrLpIyXXXvgfTtf%2F3En1qiLS2rd5Abp6lX3YdxVUTPBSbRa2S76QgDMbe8uylm2aqcH39ECag2nd09laXKsq9tMMv5lr0GOqUBF3gFLvXUauqKIBV%2BEkrN7juD10kq%2Bu8ZU3EoXF%2Bei1Y7XBazaAShvNstDXRQbu63OO8UaR3a%2BXT%2Fum8bcV1%2FvrQk5oSt6DDw8OXoA5MFdgOvqWRqTJtZEVlzoWn3jmM3WRcQawXtfxRS1ZN%2Ftbk%2F1%2BxBItQn7BGvdMEt7R8tf6CKFtA0ntoJ7xZLbMfcZLGKumagoWx5oMtXu0E3VEKrBxb1B1bt&X-Amz-Signature=30045faa1c7dcaa8a0d30267f31400ef8f23807bb73fbe21031fb836eeb005df&X-Amz-SignedHeaders=host&x-id=GetObject)
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