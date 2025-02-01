

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=15c10409ae441edfbf71ed82da2d9b257a560a8c570cc565c2591510c3c65831&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=a7fd97ac438ee57750c5b82d7d1db36ee79a97e0f3f32b096d500069dacaa407&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=d8773aca230f26a364db0d5f600f88a7a18fbc3c32a01287b8388b7835bac6a7&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=f257dc8e8fb58e4c3e1be224a058af4e2c790936f8295fe13521a1597b2ae89f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=69b6fd30013e6357b22f1f4ad6d2d31f4ee83a396a1a965d6f9ad573a7ed68b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=3a291ff1000a06e9f6b16009442ad14ba791def08ba6b6d534fd5625ec62b512&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=cf3a4cb3585d606bc5bddcf21b1f1d99cc12c1102d15b4678b687e0de1dcdb76&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=2413510959ce177c061c1adbd246c6a3e5bc377e3ce77336b53912382584523a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=d516091282b59753ba8795357d195d36bce837333dfc3fdf96eceb7c8fc2ca86&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LHJDMVY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNRno07RqtcTVpWpw9uxSzmVOiulPTmaEjBJjk2v3c7wIhAJhlcpoeIIxDQGEFAZdQZnKvF5ScG1yLKJSSfNm9bumpKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV55MmW2P84yXBvW4q3APg8LhblhwkXLKfHUwOCxJ5WDaQkdBnAZzbFOxF3MPmulwVR37Op2WpMGHQvf%2Fn4vWMcvbRPKkmNxbVxW4YuUF66uGof1ItUH0o%2FZqi7HBb%2B3WJ1EZnSKubfNsnR6uNjnEObXxQN7BsNxVLVsai8iMXGG5WFl69ml7HFXen%2Bi4NfbtBS9lX2P1Md%2BmaxWUP0zm40rNY23OczJVgoxbVkCaqE%2B1r9CO0pgQ%2FqdroMay4bWMD58SNfKwA9m4GfO3o%2FxZH7GGVxgPhXzwNnsqWJaaVX5t0RCmfNC7h6%2B7UQ3xeHquArb%2B7OQouvBkNBGNrRwKLN9DW%2BrJPHdMIsLHrCDfWlVLGe4oF3szIqt0KQXeSjdTR%2BIH1wThA%2FvA7mL7DZpV5Vn6yd7WovBtFLd%2B4QJzPawBTwojG4wi5%2BkAXS8r6XzoKFwyEXpwbvEnbrnjx0NjJ9cHY%2Fz73cHwGY1wn%2B1wFv5sPEA7v2FvVosC9qemyo%2FHQoJSE8jFtqffpICKHQnmHnlNvcJV%2BYn%2FpnnEW17JxRq2q4Ohb0pwMuFJwCjp8RXqNv%2FuHxfnlkrIu0LCARiyrIlP9wuLHYbi2E%2FCG%2FrI83JGKigNPfY3omkdSreaVIydT5fZBGt3EkNlukDDtsfq8BjqkAQlDjDtKkPo%2BnlRAKlN047UQqXfj8oPPupOgPv%2FdcFQOwSemdtWX44fqAAfKNuWTzXq3qz4%2F34z9M73kQ66qQ6VsA1Py5vdFDi9YLAm7m0njO10PKdOX8OIP4iQLUDcrM5SB9pOxaqCyGTzVMRLi4k5rYGko0mAUizblnR3ZD1WPVCBHMUmWR2FojncRp3CY9nuDDJRJG6%2B21liobrBV17TnMZ1d&X-Amz-Signature=16f2cb81424ef0205f0f9f3fc71facf0198ecb41acd93579c1e71a039e8a2b07&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LHJDMVY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNRno07RqtcTVpWpw9uxSzmVOiulPTmaEjBJjk2v3c7wIhAJhlcpoeIIxDQGEFAZdQZnKvF5ScG1yLKJSSfNm9bumpKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV55MmW2P84yXBvW4q3APg8LhblhwkXLKfHUwOCxJ5WDaQkdBnAZzbFOxF3MPmulwVR37Op2WpMGHQvf%2Fn4vWMcvbRPKkmNxbVxW4YuUF66uGof1ItUH0o%2FZqi7HBb%2B3WJ1EZnSKubfNsnR6uNjnEObXxQN7BsNxVLVsai8iMXGG5WFl69ml7HFXen%2Bi4NfbtBS9lX2P1Md%2BmaxWUP0zm40rNY23OczJVgoxbVkCaqE%2B1r9CO0pgQ%2FqdroMay4bWMD58SNfKwA9m4GfO3o%2FxZH7GGVxgPhXzwNnsqWJaaVX5t0RCmfNC7h6%2B7UQ3xeHquArb%2B7OQouvBkNBGNrRwKLN9DW%2BrJPHdMIsLHrCDfWlVLGe4oF3szIqt0KQXeSjdTR%2BIH1wThA%2FvA7mL7DZpV5Vn6yd7WovBtFLd%2B4QJzPawBTwojG4wi5%2BkAXS8r6XzoKFwyEXpwbvEnbrnjx0NjJ9cHY%2Fz73cHwGY1wn%2B1wFv5sPEA7v2FvVosC9qemyo%2FHQoJSE8jFtqffpICKHQnmHnlNvcJV%2BYn%2FpnnEW17JxRq2q4Ohb0pwMuFJwCjp8RXqNv%2FuHxfnlkrIu0LCARiyrIlP9wuLHYbi2E%2FCG%2FrI83JGKigNPfY3omkdSreaVIydT5fZBGt3EkNlukDDtsfq8BjqkAQlDjDtKkPo%2BnlRAKlN047UQqXfj8oPPupOgPv%2FdcFQOwSemdtWX44fqAAfKNuWTzXq3qz4%2F34z9M73kQ66qQ6VsA1Py5vdFDi9YLAm7m0njO10PKdOX8OIP4iQLUDcrM5SB9pOxaqCyGTzVMRLi4k5rYGko0mAUizblnR3ZD1WPVCBHMUmWR2FojncRp3CY9nuDDJRJG6%2B21liobrBV17TnMZ1d&X-Amz-Signature=c963e60f6152d870ab55b9223b531f25a46b911c0e890de26e5f4d1f321c5140&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LHJDMVY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNRno07RqtcTVpWpw9uxSzmVOiulPTmaEjBJjk2v3c7wIhAJhlcpoeIIxDQGEFAZdQZnKvF5ScG1yLKJSSfNm9bumpKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV55MmW2P84yXBvW4q3APg8LhblhwkXLKfHUwOCxJ5WDaQkdBnAZzbFOxF3MPmulwVR37Op2WpMGHQvf%2Fn4vWMcvbRPKkmNxbVxW4YuUF66uGof1ItUH0o%2FZqi7HBb%2B3WJ1EZnSKubfNsnR6uNjnEObXxQN7BsNxVLVsai8iMXGG5WFl69ml7HFXen%2Bi4NfbtBS9lX2P1Md%2BmaxWUP0zm40rNY23OczJVgoxbVkCaqE%2B1r9CO0pgQ%2FqdroMay4bWMD58SNfKwA9m4GfO3o%2FxZH7GGVxgPhXzwNnsqWJaaVX5t0RCmfNC7h6%2B7UQ3xeHquArb%2B7OQouvBkNBGNrRwKLN9DW%2BrJPHdMIsLHrCDfWlVLGe4oF3szIqt0KQXeSjdTR%2BIH1wThA%2FvA7mL7DZpV5Vn6yd7WovBtFLd%2B4QJzPawBTwojG4wi5%2BkAXS8r6XzoKFwyEXpwbvEnbrnjx0NjJ9cHY%2Fz73cHwGY1wn%2B1wFv5sPEA7v2FvVosC9qemyo%2FHQoJSE8jFtqffpICKHQnmHnlNvcJV%2BYn%2FpnnEW17JxRq2q4Ohb0pwMuFJwCjp8RXqNv%2FuHxfnlkrIu0LCARiyrIlP9wuLHYbi2E%2FCG%2FrI83JGKigNPfY3omkdSreaVIydT5fZBGt3EkNlukDDtsfq8BjqkAQlDjDtKkPo%2BnlRAKlN047UQqXfj8oPPupOgPv%2FdcFQOwSemdtWX44fqAAfKNuWTzXq3qz4%2F34z9M73kQ66qQ6VsA1Py5vdFDi9YLAm7m0njO10PKdOX8OIP4iQLUDcrM5SB9pOxaqCyGTzVMRLi4k5rYGko0mAUizblnR3ZD1WPVCBHMUmWR2FojncRp3CY9nuDDJRJG6%2B21liobrBV17TnMZ1d&X-Amz-Signature=7df97249972990d96994acc914d5e1c58357640eb2b68fc54faaf18ff1d1c455&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=d7e15ac0bfdc82d953683f564928fbdb4a51363ba29e6aa9f1992e219cda5b63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=edafc213d3926633688463507ff163f72a548a1e39260fb5e245f4b084ad3a1f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=23f5cc40b4e3668437886f0881ddf6d149550c7caa4ad62bc8857d048cd31708&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=64ecb881b48ad08229853d3a4aa461c6e7bf63bc7441ac182033c67533bd70af&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=ed11bd04ae0e11ac0d67e5857f7bb0a540eaa54d41a4ac854dddd8621fb9260f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAMWCFUD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClNfsjTBMa8bjz9xwro%2Bugwhifszfk%2FjwuKWBLiQnlrgIgI%2Bg2sULL3MVn32QUpYRifSuu9%2FJnQv4LH9kPnZVmPh4qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9BFXGftRgUt46GmircA%2FXVeVvJV%2FWJIWR5GRhul08f9Y7KX3z0Owg45Q8pIF9VMEP1wERSVFRpf%2Fd7BeOKEsZzQZzkRWqhwg8qoDGJvpZ0K7%2BsqsgCeO7qPMqJAg7yNgWkiCTpDQ9237scp5ZeQIX%2BRLBu1ZfK1v5ofGF%2F0phVZIfnPgfzr5nBXC1%2F3UDadf8Hts2MG91GPDKN5oSW3mQqmATJFENJQyiJasT1NoI46O38joMZiomumblwCsu41voqLkRyAwqCQgh%2BoM4rWcDP%2Bf3pO6qNmXYm2cvOoB%2FhixCJ6EpP9AYNylUmxdL11nb1g0R3i5vGy6CmnyxuS0xbC7x7oFrMUaOPagk%2B4o82asM4dKjBulzETBD52sd%2FrI8oXYY0kevdNzMVZij%2BlkcxzWz%2F7UjkosObfT04FcGcbAdi8unYElJDK%2F%2BHR4SVvur8sVnE%2B7rxWW9p83v8qCn%2F7Ixj1%2FzSJBXNgdbZf%2Fk7tR6iXHY5H1ZKUAXP3Upq8HkadcIwaMRksHSBRL4DD3uGGY2gQyBjr9G65Tq2NxjycmvKe56jJBx0eXvkBiyZbeMYtPOgebUmbPQmc21ujekY1SXpaaj9JunOcOEQ8e%2FPY6nHEXmBfo5ApJdFHs%2ByS2HoIbsF1A6mWWSZMPWw%2BrwGOqUBpXvwG0stDLbhDuVtCVeF%2Bg1qFlIbb792%2Fa1g7rMiSfn5wSb9m3UdQZs2d3XOC%2BGXFOKQvIyu%2BgwAVEtAxEn%2FEUNacBzdTqaaUsjEK1Tf6rfitTK18v0Pz7MN2zbpR2Q4bqXuTrr88XHoMWSjlCOPE47Nzax4jHz4xKjBlecpYAbMMOYfU0ILL63TNup8UpBJBhKvRjHWx6%2BXCV6411Jc%2FysGztS1&X-Amz-Signature=06a792bb8031bcc1f87b7add90b15eadbc9b6535b11d90db7981a491a262c91c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKXKAH4V%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk3aeySZcB60dfuxUiNnX1aNRKkj%2Bj8RPe8XkaQlhmxwIgLYTEElvQTImggviGmIFt3Ba0ToOLejfBjKgMqanOcjEqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGZupjUv0P9%2FpY2FyrcA2QxVfXjfittcMCQerOsb%2B4oMSUfw%2Bv9SZ6e4tEH%2B2omESGxP6npmfkd6OptxzucSJzYriAUV%2FAJjeOjlZOlJgyVwR%2FVNuzc%2FHjp3TXFdGhKEBzoraV6L3oXIRMX4w39naqKidp97NmJJKgZYOJCl4Fz2LLtGWCXJrYvqOvbHLENaoJHsPc0o8%2Bx4ni9BRVN8ovCANij9lULlx6rvO%2Bg3YdkGock5ZNeuZwQwlppsoypeEZ67S6Cbk9pv%2F1vIWo%2FupRgYbxqHHKgh9nnFf4m6s2mF%2Bf1CnDYMigqsjPbTWjyUNqv%2B%2Bm20Aaa53VEJ1IdkPABq%2BBeAb0bAwmpUeHdqC8rMoTlEwFYt2xUU9ZlkAvfB3fIu%2BNsyABDrpEc5JtlFJy6VxO4wQmoLEt8HOYTzyXro0zHCzFWbS21pFPkkBxH0416bvFnJgd23zemr72XWA1kWfK1%2FA%2F5jCOwx7AfS1YvUzq90YsbomTlZPI1k84NjKQgsuOp2oBkMxmkF8s%2F9wxPdsWyFEFzplo6iWtDWlFGEJlUWexNPDkFtWFvG5%2Fx2DCK%2F3SlS%2FoGTTWQ7JWz7Y%2FdAxcw0xIbYVl0IhacwBlLiRxAZdsLEenJLJw7AZoN4j6nAGlhcq%2FhNM%2FoMICx%2BrwGOqUB7QbJw%2BAWhKqY0XJqeWjS9UeVlhhm01JOyoFEAwk7wZbqKKoTocQ91YcyPXMWOi6LwTuVLlsXo62If5qCokuRcRBFhKEnd6JqjKFfqTV%2BKRJn2Nrv5Pvpd9ptAfb1P6XxHXniDlwYXYsWmksFBQmtcGdK5%2Bz74KB%2F%2FpvVBaqWtPnyzJbdpXIvPEjA7gKmzC5aGNXsWlSPPWL75xru8gZRZnZWoyDL&X-Amz-Signature=78c8ad633b58678c806110909ed3444f71cf0a04ab2926bbacf5f150b0a2218f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKXKAH4V%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk3aeySZcB60dfuxUiNnX1aNRKkj%2Bj8RPe8XkaQlhmxwIgLYTEElvQTImggviGmIFt3Ba0ToOLejfBjKgMqanOcjEqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGZupjUv0P9%2FpY2FyrcA2QxVfXjfittcMCQerOsb%2B4oMSUfw%2Bv9SZ6e4tEH%2B2omESGxP6npmfkd6OptxzucSJzYriAUV%2FAJjeOjlZOlJgyVwR%2FVNuzc%2FHjp3TXFdGhKEBzoraV6L3oXIRMX4w39naqKidp97NmJJKgZYOJCl4Fz2LLtGWCXJrYvqOvbHLENaoJHsPc0o8%2Bx4ni9BRVN8ovCANij9lULlx6rvO%2Bg3YdkGock5ZNeuZwQwlppsoypeEZ67S6Cbk9pv%2F1vIWo%2FupRgYbxqHHKgh9nnFf4m6s2mF%2Bf1CnDYMigqsjPbTWjyUNqv%2B%2Bm20Aaa53VEJ1IdkPABq%2BBeAb0bAwmpUeHdqC8rMoTlEwFYt2xUU9ZlkAvfB3fIu%2BNsyABDrpEc5JtlFJy6VxO4wQmoLEt8HOYTzyXro0zHCzFWbS21pFPkkBxH0416bvFnJgd23zemr72XWA1kWfK1%2FA%2F5jCOwx7AfS1YvUzq90YsbomTlZPI1k84NjKQgsuOp2oBkMxmkF8s%2F9wxPdsWyFEFzplo6iWtDWlFGEJlUWexNPDkFtWFvG5%2Fx2DCK%2F3SlS%2FoGTTWQ7JWz7Y%2FdAxcw0xIbYVl0IhacwBlLiRxAZdsLEenJLJw7AZoN4j6nAGlhcq%2FhNM%2FoMICx%2BrwGOqUB7QbJw%2BAWhKqY0XJqeWjS9UeVlhhm01JOyoFEAwk7wZbqKKoTocQ91YcyPXMWOi6LwTuVLlsXo62If5qCokuRcRBFhKEnd6JqjKFfqTV%2BKRJn2Nrv5Pvpd9ptAfb1P6XxHXniDlwYXYsWmksFBQmtcGdK5%2Bz74KB%2F%2FpvVBaqWtPnyzJbdpXIvPEjA7gKmzC5aGNXsWlSPPWL75xru8gZRZnZWoyDL&X-Amz-Signature=84175d02372136ba6406df01e0d900bbe26a7789c674ce5b057e723b07210c5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=f50ca81ebfc9cea83bd62517b6a7baf2c941fb1cc9a9c73af06d7460a54edc72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB7AFOFR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqmEMvA2twYTOEve0IsA0JCHrhonKgXpNhyf%2FXPvBk9AIhALcb%2BUyz0vd1HU15jn%2BVEY1T8zfYOXl61WGLULVNenFDKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFphwoo8CB%2BsZVH5Mq3AMGQoaHJTt4tXNju0m%2FfsDdyXTNLAW1mNFd3gW5p56aQ5szL3ykaCWeSd1i76zwNEQCXHNy75m%2FHX5FD2PxYLym1rJz7C6K3bJH8he%2BfI8wgTrpUa7FhMW%2B%2BttyhGQP6DwyZBop3AWgXHh5pcRD%2F6EOcs9tcqWaPIVkKc2s8423lNIv9t4rmVRmxpRAjw2TActs2L71iq6uFp7tCnJkW71Hg1%2BPSB8a4NOefpjg8HEQxpuupdybbxJxLciJmWfDDEo1B2vWHYYO6cEhRCvyGnERuN3BiEN2XI3WG3TEM%2Bs9ny0tOlDp5kYmelyeCj4dk6IzAAw3O5t56REiWPeyYWUyWSqbr0vqRGh8yY5w4qdNfj5irWBoWEH4zZy2h5NKkE3sMf3BZsdUcB6E2HeMLr3ncd%2FDtabKqwHa0TTR6jDgYkz4k5KioeCLRvcKd7%2BZKnE%2BxuZW1fKTiWgEsNbpa0B%2Br1%2BBFpbfnbO5FByXCB3jyrJ%2BgYzUXrZeekFYmDE%2BQcb5PUSudc5y%2B470iP4LIWJ9%2FVnRvNjjqCwRDBxm3oNslRw2DuZshIXKFE6P3GauWf27PMrKcdQ1UUP985xoc%2FIvTMGjKqS69%2B9feIaHhrYvPnA3gA2zNv%2BeE0mkzDDvsPq8BjqkAX2E%2FMwOEqnv929IUEpcOHEdiMIpaNvTHu1%2BYqbjMA24AMiJPmQqTDGVXBmEz1XVDKFji7av%2B0IJTDqhHS3aokocOXgTwLvkeZCsJS6nUVsORTM4SaL6x3e2BkM8mVLiQk14pbAt7WDqhFnwvKxNvNdp%2FXb3GoUhNcS6LP%2Fb0ZjwpwHDqw%2F6eySJnj%2BY8vmSNnrBxIapRrsJeZeAQL4JTOeuKcXe&X-Amz-Signature=b8e361dfdca94d49d264bf8674fa0eba73048027995e958730c40724f1008842&X-Amz-SignedHeaders=host&x-id=GetObject)
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