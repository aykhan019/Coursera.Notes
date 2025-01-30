

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=553426709b19d1c4c0e341f65dd71b5e2f7e6571d243a68a7d819bb53a0bcab9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=bd27565f234d98dfadc57c1438c6c8aef9818689015e3d0309e96b85280755a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=d8d0a12f149ce8021a7e0482b1eef162155d1953b3ad707adbc6749d0f33c6b8&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=72a29b0a1e63507740fb64a02f17af91f65fb681219deeff8104a6ba4a99a6a5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=ad62eb84bffb2caf8eacc70f6b617693dcdf727e0c3b7cf5638a4fa313fe94cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=81664baf899bed8fa580cdfcb5627bd0954f57ef50d54798cf8027f671c0d14c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=35474422ed5f956a4aa3536d9321d8d4b893019bb06613f9489d32c97347e835&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=80eea0094bc40021efa6e4d7b6ca70b2f502bc548ae70031b48e56594a4ae93f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=ba06f0746b000488f901210aa632b9c326e3e79a545b293225f92cd548d15d3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2N24RY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLz8bhXYecSC7n2rbIr7edZ6NndZ08oceegqYahB%2BT%2BwIhAPNLkICy%2BNMyvoFVsL7bjLyoVX90fsr0rp4ALJKZ3yuTKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWfpys3i7mcjWCgyoq3AO0ZFRPRfXEUn1zHmbMMMbTQ2BblQ3KkbJqSv9KwEtmtedRNsqBhe7gQMa2mvdkijw1e7rJdPgO3t8lJ38JLGrrc%2B%2FOnPc44gpuP1XCVzWdFz2SXJy4CJFHNRAgnKNvLcySI993mrzt4QFl9hd3X7ZIDMj%2BljU4TCYp8iLXy8mYF9msHOW0xTDar8gy1xFi2NHnpJC8UaJKnsgXIgamiY6HQaeqXDhslR28hLv53ymdUuefz9IG51S77oixl%2FEJZur3fq8SoBXS2ElHfc2mj4QuuVrHxt1aTwGlZaeUy35tdG1Ir3uyPMwsx9%2BJK1m3koU7L26JI3hjdAImG61dRVTO1MVzfpICTF3STWTtjYIQdPCM8XnPY4KOE60sc7nT8NPHK2wPC2W1vXQk05zHpfwlEBgxhgl2hKovPpq7qwgHNLlccF1hBdVegEDuJ9sCOjKxbv3mhNotEcYFPdwNDqvWMMQqpY8ClUb%2Fe%2FZroTE4ZPiceuklOdACKJ9Dff%2F3GD41bsjeJ4nA89l%2FgF1U9aR1nt0EohG608rHWw09Ya2fcXaE7snoh%2F9srUDD62O2Km%2FMGjxE8A9MwmRZWZvsfvsH5zN5lncbRT4MUnUTknFQFE%2Blva8nhuJVBPp4ODDb8u68BjqkAYiUVCDbYPwVbCst4tXl54g3Zt4gayp7nWEyB%2BVSyr2FHDAwWWUq9gTbYy1RP146ISBK3xnzDtbEv5ol1xtPEMKXc4lQHiSc7x0UZJBxzEAfeyCW8YKSYja88MfG8mzwTbpudlDxPIl0ESkdtIO3nQET8MagwCacMu9NHVFQq8%2F4cjfE9716e4juoqKX6IvDHvv1oxumc2w7B2pA%2Fmf%2FqrkxO4EH&X-Amz-Signature=5df3381fbc2529af85a68e5b4d27e1ff87dac500bbd46c32239b4d208c27de42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2N24RY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLz8bhXYecSC7n2rbIr7edZ6NndZ08oceegqYahB%2BT%2BwIhAPNLkICy%2BNMyvoFVsL7bjLyoVX90fsr0rp4ALJKZ3yuTKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWfpys3i7mcjWCgyoq3AO0ZFRPRfXEUn1zHmbMMMbTQ2BblQ3KkbJqSv9KwEtmtedRNsqBhe7gQMa2mvdkijw1e7rJdPgO3t8lJ38JLGrrc%2B%2FOnPc44gpuP1XCVzWdFz2SXJy4CJFHNRAgnKNvLcySI993mrzt4QFl9hd3X7ZIDMj%2BljU4TCYp8iLXy8mYF9msHOW0xTDar8gy1xFi2NHnpJC8UaJKnsgXIgamiY6HQaeqXDhslR28hLv53ymdUuefz9IG51S77oixl%2FEJZur3fq8SoBXS2ElHfc2mj4QuuVrHxt1aTwGlZaeUy35tdG1Ir3uyPMwsx9%2BJK1m3koU7L26JI3hjdAImG61dRVTO1MVzfpICTF3STWTtjYIQdPCM8XnPY4KOE60sc7nT8NPHK2wPC2W1vXQk05zHpfwlEBgxhgl2hKovPpq7qwgHNLlccF1hBdVegEDuJ9sCOjKxbv3mhNotEcYFPdwNDqvWMMQqpY8ClUb%2Fe%2FZroTE4ZPiceuklOdACKJ9Dff%2F3GD41bsjeJ4nA89l%2FgF1U9aR1nt0EohG608rHWw09Ya2fcXaE7snoh%2F9srUDD62O2Km%2FMGjxE8A9MwmRZWZvsfvsH5zN5lncbRT4MUnUTknFQFE%2Blva8nhuJVBPp4ODDb8u68BjqkAYiUVCDbYPwVbCst4tXl54g3Zt4gayp7nWEyB%2BVSyr2FHDAwWWUq9gTbYy1RP146ISBK3xnzDtbEv5ol1xtPEMKXc4lQHiSc7x0UZJBxzEAfeyCW8YKSYja88MfG8mzwTbpudlDxPIl0ESkdtIO3nQET8MagwCacMu9NHVFQq8%2F4cjfE9716e4juoqKX6IvDHvv1oxumc2w7B2pA%2Fmf%2FqrkxO4EH&X-Amz-Signature=c904e2f856c6a9019b759c05f3d6862c89a2095c9348c7d6f6024895997fa27e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2N24RY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLz8bhXYecSC7n2rbIr7edZ6NndZ08oceegqYahB%2BT%2BwIhAPNLkICy%2BNMyvoFVsL7bjLyoVX90fsr0rp4ALJKZ3yuTKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWfpys3i7mcjWCgyoq3AO0ZFRPRfXEUn1zHmbMMMbTQ2BblQ3KkbJqSv9KwEtmtedRNsqBhe7gQMa2mvdkijw1e7rJdPgO3t8lJ38JLGrrc%2B%2FOnPc44gpuP1XCVzWdFz2SXJy4CJFHNRAgnKNvLcySI993mrzt4QFl9hd3X7ZIDMj%2BljU4TCYp8iLXy8mYF9msHOW0xTDar8gy1xFi2NHnpJC8UaJKnsgXIgamiY6HQaeqXDhslR28hLv53ymdUuefz9IG51S77oixl%2FEJZur3fq8SoBXS2ElHfc2mj4QuuVrHxt1aTwGlZaeUy35tdG1Ir3uyPMwsx9%2BJK1m3koU7L26JI3hjdAImG61dRVTO1MVzfpICTF3STWTtjYIQdPCM8XnPY4KOE60sc7nT8NPHK2wPC2W1vXQk05zHpfwlEBgxhgl2hKovPpq7qwgHNLlccF1hBdVegEDuJ9sCOjKxbv3mhNotEcYFPdwNDqvWMMQqpY8ClUb%2Fe%2FZroTE4ZPiceuklOdACKJ9Dff%2F3GD41bsjeJ4nA89l%2FgF1U9aR1nt0EohG608rHWw09Ya2fcXaE7snoh%2F9srUDD62O2Km%2FMGjxE8A9MwmRZWZvsfvsH5zN5lncbRT4MUnUTknFQFE%2Blva8nhuJVBPp4ODDb8u68BjqkAYiUVCDbYPwVbCst4tXl54g3Zt4gayp7nWEyB%2BVSyr2FHDAwWWUq9gTbYy1RP146ISBK3xnzDtbEv5ol1xtPEMKXc4lQHiSc7x0UZJBxzEAfeyCW8YKSYja88MfG8mzwTbpudlDxPIl0ESkdtIO3nQET8MagwCacMu9NHVFQq8%2F4cjfE9716e4juoqKX6IvDHvv1oxumc2w7B2pA%2Fmf%2FqrkxO4EH&X-Amz-Signature=3331df59dccf95376099379777aea9936948d9012ed489a04a9d32cd731f50ec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=0f36d6410f7e0a4da7eade8b75381fbbdfd9c8f586ad467b765149b10eb9810b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=a873f6b36a30bf5c132fc6bdf3781aedf0d51f081b891d6493d54c29fee3aa5e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=91b6a076eedbb51f3157b11e545dff18ad37a70ce5195976d6d4f05eb59c003e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=1d50b5f332946279c250006ba0c6385a13f6b1c5032fa24c787620817e285ce2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=5c52932b1386c8a3cbbd41bca29da066cf477fd27f5b2a79f02a403846c090df&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOUGCNG2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3hD6vNw97RbFynzLW1GRSQ3S%2BQAt%2F7KGAwvQYIg1EfAiBndTHNfrj%2BnLHH%2FC%2Ff0UvjZt9KKLyDwTDVPRxqMzP4zSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgOzmiQCv1vrM5%2Bi5KtwDP39v0te6CF5i%2BCPHiI6zdvNg7KQ%2FyCgXVawCih5G2RNZDNj%2F9LxwB3Ijh03gPseRVT5Biue2%2FyCufktVqcsq7rS8j6%2B1UJ891CnFOwz79yFa3rRZ4kVDSsL3Ur8KuizkLYjSOOiNBHrK4NzkOThMQ4wtqJQ4YTulVZLhNgPJ5FOKzUcuXUXbSK3qaTgfGBtFsvfbkminjq89bguo%2BgQ9eo6JGsS8ErohfZFEbMxZ7cVuz1oT48qt1kO0HEd9Y%2FC%2BdkV0xuzKgvmp%2FAS2Jmv%2BNHVd6lh34%2Butt89tDAcCtt8W8WZDb2hCgY3Fe9pSBk05LWfeYUEyQBYkh30hJgCnEBuly%2FchjTFSGWmeUSoCP0zZkpBFHo6noB6SYBBqjRRb8RxhCYXXjnU9Ksi1UfRSdPyA1cUf5ecoWjIIf709M1EphmMT3h7YYt2GdPIU38%2B0802RVqrinUhLx%2B%2Bmv3faosHMbfC1thEfMTR4JHLw6DDkXy%2BhtpeXx5Ofw%2FMdaYj6dtwXG%2F%2FYixuXqYRBY0xTwuD4kSinA9UWtcnC7QyIB8M8rBGFJtXPD3j9o0XM9h5EPnZgfOe8SPo6CrnxzE4hDAlJKZFiChd%2BquTbWIq8nqXAt3wXM%2FJ1fN8%2FqvAwtvLuvAY6pgFSZONpqeklQzydSP%2FTIXopsNqa44h%2FjO4kqq7rfPuJJcxUMDB%2BryxDUW5%2BRl5IYDj2eX%2B445pzxZBOhy2CWjuJZPmCE%2Fah49fP33%2ByKlEhrZCqDWz%2BEyrBEF%2FZ0KuCSG%2FMfrg4TKvaknT3evREUi3O6FEZ%2Fa2ccC876x1QVZpDXWBwakQRbaTSLJNVKHTaQ8u9n76e31G5wVupdMCP7eRWr6HuKHp%2F&X-Amz-Signature=051f9e565fc55b5a30e951f96fbec3f49324be259844887e404010b800cd7c49&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDJRURLJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB4gFhPaU6ZlvbIjEqmgTS6JI5MV%2Fs3KcauOkysosvPWAiBy2WcqoGjkXlLw7qqpdIYG%2B2hSmRc8375347lWTCOkIyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtvJYwT2btBlnoV7iKtwDOLjRmJGfYmEtkaDjaz%2FkoO9iPy8dvTbrnKert65mGo1wpxE%2FqppRTKOPHQIeSsH%2Bu5fpxqGRst5t2T%2BDKQknXddecZmexqFFHrGdgbkVfHmwijPVkq03wlSsDcpRNOdb222LD3fi5fEhxYN%2FsvhfHkol2X4GV1ptNcGsHtlUeDpKl1MbsC7BZ2wu1y4ee%2FgrBk7EWXHIO0ZhlCvQIYnpyz%2BR479iTn47cwSxfvOpCxLhovpQHlgYK0iG4ynORUJTcAYPoLSlxp0P1eU8By4BtMkAi8eCmoghODN8ARIN3B1JC5b5c657Td%2FqxkhNmy4rJTy7w1peL93qQuBJfTOh5I0vvCBK0BNNEHpQHHyiGjkakcX1YvTP1OoDroiKPGGp48WAcbcM7LPFflOU7dwpSJV8lr7iZfzCMBERy4ELnu9pXN7hRZW%2Bd7UY82rsTxH4i9wMcmpVZkkuVQ%2BFLVfreTsNFCZyfyA%2BvMvRwOAZD7P1hjmZKAeeLuROK68BROKwyqdc28jcC0H%2BxKe%2B0KzjGlDjuVc5fI39X9FgJgC%2BgVaPi9IcJUFdQxOXzNLsBZ3DVzVZnDHgu%2Fk%2BtsnJaOH1OyvE2SjSEjIalEsklinAXA89VFBU9MSm4kLqqiAwn%2FLuvAY6pgFzoqu7o4DROBO3RStdpaq6XkIhygl1q3IDGZOpnCB%2BgIlE9jhXuGpH7r%2BRQZ4XITI%2B555lsLROKhZ6LRHMgw%2Fo9XwbfD3nVUGUoc4OH%2Fqa0e%2FqFSdG6hCldp9cSkh07VNd9GhqLFuRS1%2BtLbMQbTugrWE22wbkuQj5XO8GEBBgikXVRUX07S4xw%2BB0X2dC10Gh5xypW6BYU87X%2B5SFi74b%2BfuGNDYr&X-Amz-Signature=26dc2ec954598217a8e70a1502c550e1f8e66b2f8429aa69cb6a593688b74d9c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDJRURLJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB4gFhPaU6ZlvbIjEqmgTS6JI5MV%2Fs3KcauOkysosvPWAiBy2WcqoGjkXlLw7qqpdIYG%2B2hSmRc8375347lWTCOkIyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtvJYwT2btBlnoV7iKtwDOLjRmJGfYmEtkaDjaz%2FkoO9iPy8dvTbrnKert65mGo1wpxE%2FqppRTKOPHQIeSsH%2Bu5fpxqGRst5t2T%2BDKQknXddecZmexqFFHrGdgbkVfHmwijPVkq03wlSsDcpRNOdb222LD3fi5fEhxYN%2FsvhfHkol2X4GV1ptNcGsHtlUeDpKl1MbsC7BZ2wu1y4ee%2FgrBk7EWXHIO0ZhlCvQIYnpyz%2BR479iTn47cwSxfvOpCxLhovpQHlgYK0iG4ynORUJTcAYPoLSlxp0P1eU8By4BtMkAi8eCmoghODN8ARIN3B1JC5b5c657Td%2FqxkhNmy4rJTy7w1peL93qQuBJfTOh5I0vvCBK0BNNEHpQHHyiGjkakcX1YvTP1OoDroiKPGGp48WAcbcM7LPFflOU7dwpSJV8lr7iZfzCMBERy4ELnu9pXN7hRZW%2Bd7UY82rsTxH4i9wMcmpVZkkuVQ%2BFLVfreTsNFCZyfyA%2BvMvRwOAZD7P1hjmZKAeeLuROK68BROKwyqdc28jcC0H%2BxKe%2B0KzjGlDjuVc5fI39X9FgJgC%2BgVaPi9IcJUFdQxOXzNLsBZ3DVzVZnDHgu%2Fk%2BtsnJaOH1OyvE2SjSEjIalEsklinAXA89VFBU9MSm4kLqqiAwn%2FLuvAY6pgFzoqu7o4DROBO3RStdpaq6XkIhygl1q3IDGZOpnCB%2BgIlE9jhXuGpH7r%2BRQZ4XITI%2B555lsLROKhZ6LRHMgw%2Fo9XwbfD3nVUGUoc4OH%2Fqa0e%2FqFSdG6hCldp9cSkh07VNd9GhqLFuRS1%2BtLbMQbTugrWE22wbkuQj5XO8GEBBgikXVRUX07S4xw%2BB0X2dC10Gh5xypW6BYU87X%2B5SFi74b%2BfuGNDYr&X-Amz-Signature=db8c8ec4074a4cd34013620489f809f10737202411cd852301a42d368c22b6aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJE5XDZ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrhUvij0zvGwZ1VkWuZnA3QJVJr2pJvnqJnWLrLOfh0AiBNZWrIThQ8APE%2BIx62f%2FFio6%2FJf1mxkRhOJdTGU%2Bd0fyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVZ6iksrqq9TXTA%2B6KtwDq6llZJ9u%2FttBxJ7TVezu8BBfHGNK4%2FvQ8nw8CT9QFpY5GvgpAE9m4U7tX6T3txSynrRPe3WAqJ%2Bv8xXQaA8L7KI9eykQHVNpTEZleg5Fx81Pd8%2FTxiLoVkdgsOwnrDxvJjlc12MRmE%2Bq%2BAZ67Ru0PbBiZj9g%2FCzIWoZ%2FutOs3EVg%2FN0U0qnakxbPe3jidiqj0Q4OgZdB%2BjFMXh300VNaf9cJo7Qy5Jp2dTwGIHmJy9MCEpQmeUH90uoPsGy0v719fzKr2asbAtpLQFTxTSVMPUYcubot4DmzpD4hu4hBhRxyyUC%2Fsutbm162Z%2FxTT3ZZxt947nyCrBbjA8v279UdCKF3VHJGuE%2FJXRhhdX6zwxCkMzofdFncNfjQO64Wsf5PwXkk32pS13Fvw83%2FhhvoTjcHRrWJiAsaaKvdNcp445u8KJ%2Fs6UNBRsL5XQ9xWnZKm5yHE%2Bax8cK1lpzkHIB64n3sQYxxyNA6u90v6Btq9AWiQjjNccq8sBb8tgk5tLcPSBDd0k6CvhRSnttlFYU5ZPxZrf5tHyNGpGTUQ9lEYMRIncLrGBXvImvUOP8inA7pibjl6683J2nyrx%2FY19WWAigV%2F7AEqo2rBi%2BgFc0%2BOz62uQPQWzlQEe73Up4w%2BfLuvAY6pgGEuJMr8Shct%2B1gg3f2%2Fxlo6GvqRCRySTmJVj6HX3LDi3sg3IzoxQcLTD6KXnnPej9UpaP8TJ48t3xcQ1%2BY602CkhCZHuGhhjjiEOsYErKjZuQJYhnElHFbfY6VaB6HUcfRdH%2BtGYD%2F0nJILno5kHz65BSadm%2BcfpBDko7K31OLZnlVDNt7rH92lFjoEvAqh7k0Maxe4Xy22pRol6KgF58JLAm%2Fr%2BlL&X-Amz-Signature=26e4c896875c9edaf0f6068a081ef2f1392ffd828dd354f0d05e3d40dcd1a180&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCWWMDG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCExeJ6VG4fiVEVjUMvuubh9yOqVcnZoHQPSdlA3FKRKwIgYhUAQH9qgG6yAFyAX98jYn%2BkB2pS17OdElQKT1eufCkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIF9b1qgx5BbF2T8SrcAwDVoQ8L7aqy6jgmZ4o4Ea6CvE5Ge1yyTRXNPWQt9zBLV3g0f01p%2Fdyzybz%2F0uBojVgDEqk3NWleMSso9Gxr9BB0zNFjWfW4RsPv9uD7GZzNzTMYBdbc23D%2FneJ1yzbBandetqV9j3R8NGMIouaxl6jjcVWqjaJT0Ajrvtw9cGRZg2hAh%2BkKY5EUYHhyISxenCXaKAjbqvDCaMV1Rbm%2BEd5Sa8R%2BTrUntUnBmfQEGnCXilljXg14rAMEdkLZJ%2BTGJ0KT0I8u%2BfnNCT%2FPFs8rK6mCloejfBQPpyRprTj2D9InnIf4U%2BHG7qWHWUDb1XXNCIHBbcbQIgWi2%2BTOpRMOG3m2HyEHYyem4lCiBJX14WIMEYsBAxCR9o0MfXIDNWrEcny2LzlX%2FDwbP7Rxy5bx780lksj9FDgoD85EZlihVMMrxV2S%2FTb5rq5lpzffmILzOh7z2EAT%2Fuu3rnjWaYGc1QwLMQHlA61ztx%2FGshzJsjd1Vfw22DpYQjhy080ay2DDEacRAB0rqxGs8hcsc5B%2FkcqgTyaNI%2B0xf0OjsACzEvwrxEm%2BnyfYrhog9Q%2BK0Eo36TbLYKG3W6HV4EHTeYiRxuyK%2BrbTJgEYfBXwCJthDGSuboRHoFtELxd90vdHMK3y7rwGOqUB6WlGhCg5q6dfHSH0CicZuOIVPW348dR1cfXqnb9fuyzALznMZXmICccaUAx7xb1cJyXb%2B%2Bn9yzQV974klqFYOpv%2FDULXj6oL6KibFgaubZYk043LVR1H8fnW9QiFhs3400ZZJiqmI5tpV9an%2BdocWEcjmJ0%2BUjIraR3yEutV%2Fer9%2BbQ72K3sg5KiCGTaR3TgxKX1t%2FVa8XqxYFk0IFbrYEOgxwVA&X-Amz-Signature=03d9052974367a5c81b42efbd8494e6cf9aecfe23fdb6b5ff17a66ce49ef58b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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