

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=ef11323f6a45bc501db9d4733f3d3b2e29d7aa2d2a69d9f2f23ba6093e5aafc3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=636350ed935ccd8b869caa3f526e96d6aaac7d766c64328ac8b4adb444672127&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=6fdc3ce763f1264607d0b179a68e172b4fe1cac1d5a0c511e3efc804d33a8cc0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=ee90f387dd2fca64850afe56132ebbbcf4c8608239a8339137a742c979f6156e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=3383d2b9c3d8970854fabe3acaac458491b41a20cd53342045a6e1df44de3938&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=e31887ef8878bcbb1a67d7fbf3dbb753495859a110e7677f189f621a384ab90a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=6f5dd841b28abb0c16d93a9f6befafa1cda243d8de3714d8557ac35eadf18846&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=dd56caa41794b18f044db035ba80825544deb034764fa2d5e4f05c596cc7fe6a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=bb271ac78f0964a9902e70d129d860cf03c4e324506bc65d7015f94bdd757f6b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ7E37WP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDW4xjQqNGydB0bFzzX4vvvBc4UOYoBSDsoWV6%2BtmKp2AiBmRFU9rnMMz84nTO0KxDdcyoYTL1qLt8eAjCL8sG%2B32yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIM1ty1Zc2GJbFK8d9iKtwDhXOUq%2Bn8ENdDldqzf1haq4fC3a5CqfeopiDiNkLEBHDbACqInlVq8%2BYjS4BYemUDU75iJda1s1Ujdp3ORaMit19oeZe3Li7wul0KNDcy%2FpJIvhu9z8zmHirHQtl1t5H%2B%2F81BqJvilvR8Lg3piR6vTuO4vCuMdsNtt99GFkFkF%2FQRPr%2FrFzzU0pgD5M9OBxjp4uNmUmZCcioepA%2FZB4GH%2B%2FhD6zuzTXI5qcK%2BcJrKgBvAKb3UMJMEEGUwbtLaEqliAcT0z8eiDInAV4H68jIbmM6A445ethtF4b78Oj4inS8stkuBkeUUAvDVThaXQCuu%2FbgizryrbpBgzISEF4fHTSK2Mn6AdpJlSuy3T3%2BRfX4L1xgt4U6P%2F0crdDZf%2FVqsYGCRsZ7T7ZPZv2k%2By1wRATPMfDP97G12d5IB0nENeAPtMjZiOfolCNUp7c93FP8eLmLbhOhi9CqKaWZ9mDLBaCaf7tSmo2NWjHxM9VEGk6TthLLqZgTmK3pibSyJ3TuDe1DwKoqtZLjwtvJOOHDu0WaIb1p6XbjRRX%2FvfwduLIfQbbZgs3inaqR9kjP8R%2FgvubwnB9Tgo97mhANtw8EE3B1uYk%2Bl%2B2BPCjJuD%2B4cks0TFYQ0YH2WXYGOMD8w%2FO6MvQY6pgE1X2lciihAl41tg76ecfugdkMqitjl4uty6Z%2FirMkTnRG7Ze2ryizj6Yzj6UUDebzqn2BKamKXLCjxomAI2orOTNiZ0VA9yX7YyiQdrgst1Rg9dcyc529eyKmPD94%2FjRuwPW7cP8JWK9GyZbjRt81jO8yIbjkwepSTGJ5IAZCzfGsD3IQMjd4Rtearpez7CaxH1t3mNbzGOWtlO9Q2BH94P1fNlLwY&X-Amz-Signature=c382bae09fb56e48c0c3e0602cba40f8925f78e97761d4f3228bd9e9fcb52ccb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ7E37WP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDW4xjQqNGydB0bFzzX4vvvBc4UOYoBSDsoWV6%2BtmKp2AiBmRFU9rnMMz84nTO0KxDdcyoYTL1qLt8eAjCL8sG%2B32yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIM1ty1Zc2GJbFK8d9iKtwDhXOUq%2Bn8ENdDldqzf1haq4fC3a5CqfeopiDiNkLEBHDbACqInlVq8%2BYjS4BYemUDU75iJda1s1Ujdp3ORaMit19oeZe3Li7wul0KNDcy%2FpJIvhu9z8zmHirHQtl1t5H%2B%2F81BqJvilvR8Lg3piR6vTuO4vCuMdsNtt99GFkFkF%2FQRPr%2FrFzzU0pgD5M9OBxjp4uNmUmZCcioepA%2FZB4GH%2B%2FhD6zuzTXI5qcK%2BcJrKgBvAKb3UMJMEEGUwbtLaEqliAcT0z8eiDInAV4H68jIbmM6A445ethtF4b78Oj4inS8stkuBkeUUAvDVThaXQCuu%2FbgizryrbpBgzISEF4fHTSK2Mn6AdpJlSuy3T3%2BRfX4L1xgt4U6P%2F0crdDZf%2FVqsYGCRsZ7T7ZPZv2k%2By1wRATPMfDP97G12d5IB0nENeAPtMjZiOfolCNUp7c93FP8eLmLbhOhi9CqKaWZ9mDLBaCaf7tSmo2NWjHxM9VEGk6TthLLqZgTmK3pibSyJ3TuDe1DwKoqtZLjwtvJOOHDu0WaIb1p6XbjRRX%2FvfwduLIfQbbZgs3inaqR9kjP8R%2FgvubwnB9Tgo97mhANtw8EE3B1uYk%2Bl%2B2BPCjJuD%2B4cks0TFYQ0YH2WXYGOMD8w%2FO6MvQY6pgE1X2lciihAl41tg76ecfugdkMqitjl4uty6Z%2FirMkTnRG7Ze2ryizj6Yzj6UUDebzqn2BKamKXLCjxomAI2orOTNiZ0VA9yX7YyiQdrgst1Rg9dcyc529eyKmPD94%2FjRuwPW7cP8JWK9GyZbjRt81jO8yIbjkwepSTGJ5IAZCzfGsD3IQMjd4Rtearpez7CaxH1t3mNbzGOWtlO9Q2BH94P1fNlLwY&X-Amz-Signature=968b819fad698e8b9a759e8ff3a16a33a52ac1123ea950c7f4c473d7c619e09a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ7E37WP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDW4xjQqNGydB0bFzzX4vvvBc4UOYoBSDsoWV6%2BtmKp2AiBmRFU9rnMMz84nTO0KxDdcyoYTL1qLt8eAjCL8sG%2B32yr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIM1ty1Zc2GJbFK8d9iKtwDhXOUq%2Bn8ENdDldqzf1haq4fC3a5CqfeopiDiNkLEBHDbACqInlVq8%2BYjS4BYemUDU75iJda1s1Ujdp3ORaMit19oeZe3Li7wul0KNDcy%2FpJIvhu9z8zmHirHQtl1t5H%2B%2F81BqJvilvR8Lg3piR6vTuO4vCuMdsNtt99GFkFkF%2FQRPr%2FrFzzU0pgD5M9OBxjp4uNmUmZCcioepA%2FZB4GH%2B%2FhD6zuzTXI5qcK%2BcJrKgBvAKb3UMJMEEGUwbtLaEqliAcT0z8eiDInAV4H68jIbmM6A445ethtF4b78Oj4inS8stkuBkeUUAvDVThaXQCuu%2FbgizryrbpBgzISEF4fHTSK2Mn6AdpJlSuy3T3%2BRfX4L1xgt4U6P%2F0crdDZf%2FVqsYGCRsZ7T7ZPZv2k%2By1wRATPMfDP97G12d5IB0nENeAPtMjZiOfolCNUp7c93FP8eLmLbhOhi9CqKaWZ9mDLBaCaf7tSmo2NWjHxM9VEGk6TthLLqZgTmK3pibSyJ3TuDe1DwKoqtZLjwtvJOOHDu0WaIb1p6XbjRRX%2FvfwduLIfQbbZgs3inaqR9kjP8R%2FgvubwnB9Tgo97mhANtw8EE3B1uYk%2Bl%2B2BPCjJuD%2B4cks0TFYQ0YH2WXYGOMD8w%2FO6MvQY6pgE1X2lciihAl41tg76ecfugdkMqitjl4uty6Z%2FirMkTnRG7Ze2ryizj6Yzj6UUDebzqn2BKamKXLCjxomAI2orOTNiZ0VA9yX7YyiQdrgst1Rg9dcyc529eyKmPD94%2FjRuwPW7cP8JWK9GyZbjRt81jO8yIbjkwepSTGJ5IAZCzfGsD3IQMjd4Rtearpez7CaxH1t3mNbzGOWtlO9Q2BH94P1fNlLwY&X-Amz-Signature=2733d3b840517ea1092dd73a559940e7efd663545791f71b830f5e6c36c8ebac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=5a6097f1d3e1f20c397321d22e55354f8096f8e188c75275e0428ef734fc5a61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=9daf0e5f732b1bccd5523b6db78bf2c28d57f7ab949cb86295344bee6d9a7a99&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=4abd2300cd5f07cd9063924bb6a4570ce6348d95bc2c3c73e225130777022aec&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=0d7394cf1b4f367fedf7948265460796d8fb89b33b4a1bae57775c178287a3e4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=ad357eb922d6af382763dd752f40e1d5f0aa4713c2099d139057c3b2ea5b9988&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWN5VSUN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDcO1yJ0jZS9myuXEbPJmzJSWhrtq6c0IvlKMEBcX%2FUTgIgJdBwhxn2nVYik8nHV%2Fr8n7g5ObTXtjTYmhbhmULwmFwq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJkhIaYvovvwWYFlNCrcA0xkLwTNPlnv5PQTGTqYVx4YTpu9QhXagTqAYFQn7B1TKl%2FXxpu7ObmbOCcj2KcP9Sj002SB7Kvoh8B2anx6my8WxaVvAQbzr5vtgVZIVdTXpxvdNJZsFnQfrtxJeCQ3t6q26Ih26GiqsNWD8e4q2yPevh42wQdZARCqyJwS%2FnGM5YisDHQoNnhKkUmdTChkcjDwG7ZkLNCdVbNRvlwt8vxDnT7XFyBW7FsdlKFtTUMdZLDZGl%2BHhIh8XfgMvM9AQv9M6pUbDX32ZQP%2FzmyGq7YRqlaxTqGarQYkJJyYGeIM%2Bhx5qcBmcWOubM0vahsX2ex34Wc4W22wDvIIxK4IDqNDttiE9KWyEagQs9kpw3m%2Ffpt1vhp1KP5aX4%2B%2F7YN%2FIhX403o3ZKxEb%2FFvl9QF3veyti4zV%2FUae71o0Pca%2Fg%2Fed9VxIgh6A%2BYln3KZb526gHRobYNv4MA05awy2xAj175cGoYX0wxiMswU1UYZzF%2FcuzEpHTcMGhWWyS%2FOQ1ug%2FUYbvLRchgy0kn6ql8ftc1%2Fs1gs%2BQDTkuXHG0GE3v0OyddLur7y0sRIGqPKnB29ORiD4eEpcvbkv0ZOt%2FRJiPxLluGNRrQIj8WRXp%2BNW0ga91I8n%2FGIu%2BzWCbwGMMKHvjL0GOqUBlePw3SjQtAejf9IM%2FRmU95nBhabMlRQxCwl67y%2BYNdsfQ%2F24QlwHllseSCmQbkBTdrTh12dKwksvgUX4p8q43XmzhUGa6W998LTzwNDsWB%2FrlJJjRaCmlgWPvxVdxyUP7W4HUuYEKqZsC9YFXSTI3p11rP6HcWIcAfTEcoYH7d1mGLdS4RzjZcOy1pfsOT0BW0L7Kv7TnA1Kpbw65PTkyicjWjBe&X-Amz-Signature=77ec436447fa52eb38b7482b56210b6fe770753ead5ca15ba5596473eb719d95&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LAFUM66%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHYto27Vct88pco6bCyvNFVcJ%2FkbNPWlTrs8GsHsu9rkAiB7V6vnPldjymEKYfAzVIjCNWx70o5x7zMB74SZ8WFw%2FSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMP6MPnjt4w4mpvZBSKtwD%2Fbwbk%2FZkLJmyW5fERzhHkob1ukJRNq3WX8vUozsDbyryFRSCXo0ucoW2acK%2BEg%2BeeyTWdT1Xn0nUwGnmhYnK36iKAQPoDKg367OLruD3l9D2pYAxs3Nmqy%2FXhHYmbKTKIEQQadIBsl0Dg5gaj0U%2BOhxbk2tHgZyRjxbF91%2F%2BnNMKY4IjrXeiR7YcfgQo8y8o1xTFOYl9QTN9%2FoNkRTrDrwtNVu2MbxEqgdfENfV3tkp1P2eiVTYudn%2F2RELvG5PK8ohbXmnm%2F11bhWkntgk6QceDgxpmPLzDqriyv1PGhecYQ8ckDLD%2BRJAsNaV9xlmsRdZ2%2FxtdhSbyGfAFZ3%2FHEpCnwQdxm2J6Nk2Qg3CpKfLLXfGm08brgrpKSAQH9Ontl9C5UHtwPB0cAll8cHKnZlcAYi60LEsmlTRbrRH6oDbHZlRZNm6V%2BFhZ%2BvEuvm2cfcfCbjff6VE9MEYF5Eglt48eIPlV09w9Hp38p1I3Rl%2Bt%2BEp27JUvWWcH0G0h9S7Jdn9oem2OR2VweSyqcwwq%2BF3f6hrrJ6Je6ihWi%2FuFIFAT3%2BD4O2V1KBpPBqge5koC%2FWgWvUDQD5NNKqjjP%2Bw9EQJoQX8t7HDAfuIpvnF4fLQ0u2czxvk1xPahTTUwj%2B%2BMvQY6pgGcRyRlSnL69v%2BYml78NaNT4VHp26u5wCgwNCEg6kkkv3atuAR0XEDRyqOoRzoYi6%2BOmJQpKXl2sMSMflY%2F0ZedMsYXkRK%2FB0i2ZOtjsL8WCWgJK4LQHPz05dwHf2jnkLG6VnmmwVtjPKpcINwBYvREg5%2BiI%2FoCBPPwE1HmXBbL%2BV9GGlr9s7tP%2BDbgA8t%2FfOn1qcn8%2B13A4nDMSnliXEUuAGx1DThz&X-Amz-Signature=02ab5eff46eb2a3dee11480c56729503b4764c08f4b813e490a2ed34690dcab8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LAFUM66%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHYto27Vct88pco6bCyvNFVcJ%2FkbNPWlTrs8GsHsu9rkAiB7V6vnPldjymEKYfAzVIjCNWx70o5x7zMB74SZ8WFw%2FSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMP6MPnjt4w4mpvZBSKtwD%2Fbwbk%2FZkLJmyW5fERzhHkob1ukJRNq3WX8vUozsDbyryFRSCXo0ucoW2acK%2BEg%2BeeyTWdT1Xn0nUwGnmhYnK36iKAQPoDKg367OLruD3l9D2pYAxs3Nmqy%2FXhHYmbKTKIEQQadIBsl0Dg5gaj0U%2BOhxbk2tHgZyRjxbF91%2F%2BnNMKY4IjrXeiR7YcfgQo8y8o1xTFOYl9QTN9%2FoNkRTrDrwtNVu2MbxEqgdfENfV3tkp1P2eiVTYudn%2F2RELvG5PK8ohbXmnm%2F11bhWkntgk6QceDgxpmPLzDqriyv1PGhecYQ8ckDLD%2BRJAsNaV9xlmsRdZ2%2FxtdhSbyGfAFZ3%2FHEpCnwQdxm2J6Nk2Qg3CpKfLLXfGm08brgrpKSAQH9Ontl9C5UHtwPB0cAll8cHKnZlcAYi60LEsmlTRbrRH6oDbHZlRZNm6V%2BFhZ%2BvEuvm2cfcfCbjff6VE9MEYF5Eglt48eIPlV09w9Hp38p1I3Rl%2Bt%2BEp27JUvWWcH0G0h9S7Jdn9oem2OR2VweSyqcwwq%2BF3f6hrrJ6Je6ihWi%2FuFIFAT3%2BD4O2V1KBpPBqge5koC%2FWgWvUDQD5NNKqjjP%2Bw9EQJoQX8t7HDAfuIpvnF4fLQ0u2czxvk1xPahTTUwj%2B%2BMvQY6pgGcRyRlSnL69v%2BYml78NaNT4VHp26u5wCgwNCEg6kkkv3atuAR0XEDRyqOoRzoYi6%2BOmJQpKXl2sMSMflY%2F0ZedMsYXkRK%2FB0i2ZOtjsL8WCWgJK4LQHPz05dwHf2jnkLG6VnmmwVtjPKpcINwBYvREg5%2BiI%2FoCBPPwE1HmXBbL%2BV9GGlr9s7tP%2BDbgA8t%2FfOn1qcn8%2B13A4nDMSnliXEUuAGx1DThz&X-Amz-Signature=337ced2d09d074b45329c0e3a1edaefd675546a060b88402221e55a7a557bb45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCJHCKCL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIE8Jlyrr0kiMAYc9%2FU5%2FrzxDfRkeyyUFkhR5X1RvrxNiAiEAk9aIiuQUwK0r%2BlaNko%2BtrsZTsGfJ7Ml6uCKqTLi2Dqgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDG2vwZpi6MND5mrYVSrcAw2aDEUcvBPDbonniCiIRojVE%2B8%2F2ftop7zDNkak9IKi%2BcvmG%2FJjVESJvWlO%2BneaZj7saOgfJpSg4A6WYkv3%2FbFMSBwwOTID07ynVN51c8%2F20joAXlwwUdapl2pxHGHV5CkmmKCtkzU556aq1YZZSJHBY5VCRYtLdJxUkmCvy1RUnvaPy6fTwyrPjHCYYj%2BhW%2BxxyDzgqb3LAwGL1tdh3Zmhe408yIlhQnpLJ5dVOMClqWE27I2VuzjFN%2FREtetw%2BwsQS4X7rYdIJ7FRvPECKGSbcNyHljL3Ud2r0a8lpA6yCzhGteA7QIxbsOtjgifryV1QVaxKCTWBDxQwrZgo9bZ1xltxaZ%2Bm8L8qpa7%2F514FdJjL8WMhTun75klZnTfXUogN9ciz5EdJxYPh2cotTrs%2BefSTaAx3cUVGkFtzXgE%2Fwit0D3p8AN5cNTLNSA0fwnDU1yPQAPkxhKxn8olz%2FumPFYsyJIC8DogmQXpw3VSjZdvHz%2B0T4kYLM4G8fZDBvao5Lxti5MAQiIj0dlZxm5rc4m0CDUOC%2BdafnJ6Cbs%2B78G71nTMA1ijwlOa3np00KeL2x7O7g60jR1rHpzEE5BBtUQRCcV0WgZhd8Ljv4JK%2FxIB93N8MxaUwV9hRMJDvjL0GOqUBuyz5g4byoVTZ28pm%2B%2FyM7PhtqPtbZ0g0ga6gTp%2BZ1JhlQ%2B6id7yWzvfdjQxO848OPc%2Fbm4Z%2FtY3vKp4ihBE%2BwpF1T0RQs856SHG4b6dXko22KMdlzvAXWykM2btv63Y8eILcBf8Okpr5TCmF1hkxba%2BFuS%2BdeEnXKzIgadJH%2BnDl6o6zIVXqpjWuUMFwGGf3k9MXwphh2c2kjFGgyMQU9o0vNbU%2F&X-Amz-Signature=0a3770959cb75b8d47dc5b025d15be1da6249c2463b86d11a2e05ee29facabc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBDI75A5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBTzZLmBIxKY1DvZa%2B5C4lgFwIb8GKnBZSOG42VZ15aFAiEAt%2FxGPyt%2B8VDTx7r1T5UvbST54%2FWSPA57E%2FJZjKYey28q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDOPHPASprpwbNAUflircA9zdVA7QFUnNQUb0nVUaZno7lffRI38ARCZMfDvkJCXLfTepNjpsd4NYLNKFtanuS8RrGctVk676%2BmIFEIpgue98AZ8Xe19s83BoC651igGUkFgrSZNc9STcFipSqhPIjcm37ASIMyCr%2BXJMnU%2FcjBRZQ3o51Di3ECSOw1ilr63Q2MUzSzarIeS6VMYhNlpfX8DuU4q65EjSqk2hjphQyFGch%2FPrIdjuzKqmIHzJF39%2F24OweRio%2FfJz0rwDZ61Qznl5g%2B%2BU3Ic%2BtdlFCn2BD9y1L4jGEM0LPgmuV8lhgPqM8vGKrO08C1JwxTgQCYsNUyuCLiLxlPuvguxNuqSwE0wyXwdLPtnPKXNUnel8eplxjsB7i2XgrNS%2BDeL6g5N34OYei387wuORkBBihM1mE6DRHff6va3cPuxfXU15GjIoB%2Bf80UR2%2BTnKYrSc4YICyAbUfJ1rBnxFeVLFRC59C65Vw1SkGAvwHUp3JJofsiB%2Bp6aO9jZjRt57C8wQVX87iFE2Knxy9dXCMAsCrq%2Bn8Njypht8TpiawdoeSORRaNYmS%2B2dQq2ejcPHPF8IQFqntu4%2BBAj2Wt6Ftf5ko7lsjZvsAwLWTOENXz0qHWE1Fy30GtcqqZ8iBgMHwsMrMIzwjL0GOqUBhez99qgS1fTM1g1lZHTOTMTKbWiZ5AnCXre8WgBSw6bSqszt6FdTVe%2BdpUhiCY81NJnykr3A%2BRmrEtCDHzOozy0gaZbdEzuV5fvZmwiTy6h%2B4Z6X4WQ5OwgKMYIKjMqStu0sm%2F1iuFklSWOL4v8jYiPDWAlCumD%2FFTLTV2%2BVa2Uo5c4aCmaT%2BKcVgqeBRfVdMiNdabVNTN2AS4cJ66YerNuJe36P&X-Amz-Signature=ddcf58896d993a90f47efe9a3820f3282df0a9ad8d5dc074f975508ccd197729&X-Amz-SignedHeaders=host&x-id=GetObject)
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