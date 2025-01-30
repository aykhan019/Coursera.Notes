

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=07d18ad4efe40199b20bdb259ec3bedaf62449c41f7bf88f3af8fe0abd9cdb4e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=120191be45d587c0a3ab3f668d10e10d35f1b889bea58e73178c05b8b10b837f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=ab58b4448a80241b211f9ae77c1151877d7a2bfc5b370838018b11f816c8987d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=09f9b810200fd59ecb03beff4d8dbb59f536ebc5eca6b9751eb981186c579202&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=ad65ea00eed808a22cc63e072cad2e024efc8e2fc4398de787d4ef7b0b9bacdf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=96a99983a3607adb40e5006b43c15b65ceea576b4d2c178a79dfc4f3280ae3ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=82c261a42021a7671b4ac6862424e0bfb976c3024b7569cb37f758beef37d902&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=88bdc45128d6fad2724652cf4fee14f92642aea19480e4b95efa8cab3c32b528&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=8f652d677cd0d55ad054c5af423ba58929b73016506a3fa606ee6b69d8d2b9de&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YI3KLYO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOcDfRotyBDNIfsanTKz5b8VTHgK77oNjYRszT7Ua9hQIgMh3UVsyT0x%2FIe9WPuJqP0mIegOMpLJ7MVjKKkgFfy4kqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4cOl8s1NCtHWyHYCrcAzbrY3aAM3Pedn7gPKC8K3lVygFoU9PgEfiowQo%2B5BKG%2Bbr3K%2BAxRT3WRiRHVI1P58kc2U74yFIi%2FFTuP1w7AH2OGLrDT%2F0X5sU2HIJIef3yazccCjwCIB8HrrNzpXjADQlIBdlyU3q8q%2FUMoVA%2Fzo%2BQM6ooXNbyFGwPXaxXn9KPCl65iluhDCs6NVTfjDan8TkF7p3757B41gGwQfVFqw5QhI4iI2WhhhKSQf7kpDkgyvgauQT968aqBm8PsNqOf5amUX1%2FkUHjgA99P%2F%2FjP4%2BJe8l%2Bn3AZ5snpKQ2Q%2B2kWBFpYs1CbCk7T7ZxaXYzXcsC41Bdg7ey3JilOuSMqoJUf%2FOZnUfhMGxXFIvlQnAcF9PmuodEZFBqgR2n%2F1tYIZxTL65V02HDVLdCoA2fIQpxiUVpr%2BfwnRYrkrJA6PDlDGW22KLaP4XRJkdveqW%2BWRItBBqMphFIOF1n%2Fe1niuRgU0Z%2FvH6a9OeWjuGqKWwVRYDFaZPYmztD8TJK%2B%2BeTuqBPHiN9m95sD7yC3jA9G6seashDFiXjrxPW1L%2Bkxd3lSYnBn5%2BedTVYmTasXQUDSBspJpDRrc1FJkPe5iup%2BgZb%2B9mbAHc5lU8E68s8mBGkTX5g16HxYA%2BnGhwAUMJ3F77wGOqUBsJ87yvzw%2BffazFeRwx9%2BQtoqy3%2B3eE7pIaW5SsFfekulCmuO8bLOMsSb1%2Fi6gqOuz5HwVgnOZ4lz7irAL2aARVBFuUyf6UWtr5%2BBiWAYQbTdcOEHXQukySmwDmU9AqA5G0nvzSgxUjFjqTXg1zOmPNUKMchrJHAXIPS1UOV411kJIS3pCIm0C%2BdTn5sM4PWezsJAnqegZgFAa0nghQZQCfx6xkdl&X-Amz-Signature=19bb36cf779bca6a54001d9c90ec960fca8ce28ea460d5567197887d902006d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YI3KLYO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOcDfRotyBDNIfsanTKz5b8VTHgK77oNjYRszT7Ua9hQIgMh3UVsyT0x%2FIe9WPuJqP0mIegOMpLJ7MVjKKkgFfy4kqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4cOl8s1NCtHWyHYCrcAzbrY3aAM3Pedn7gPKC8K3lVygFoU9PgEfiowQo%2B5BKG%2Bbr3K%2BAxRT3WRiRHVI1P58kc2U74yFIi%2FFTuP1w7AH2OGLrDT%2F0X5sU2HIJIef3yazccCjwCIB8HrrNzpXjADQlIBdlyU3q8q%2FUMoVA%2Fzo%2BQM6ooXNbyFGwPXaxXn9KPCl65iluhDCs6NVTfjDan8TkF7p3757B41gGwQfVFqw5QhI4iI2WhhhKSQf7kpDkgyvgauQT968aqBm8PsNqOf5amUX1%2FkUHjgA99P%2F%2FjP4%2BJe8l%2Bn3AZ5snpKQ2Q%2B2kWBFpYs1CbCk7T7ZxaXYzXcsC41Bdg7ey3JilOuSMqoJUf%2FOZnUfhMGxXFIvlQnAcF9PmuodEZFBqgR2n%2F1tYIZxTL65V02HDVLdCoA2fIQpxiUVpr%2BfwnRYrkrJA6PDlDGW22KLaP4XRJkdveqW%2BWRItBBqMphFIOF1n%2Fe1niuRgU0Z%2FvH6a9OeWjuGqKWwVRYDFaZPYmztD8TJK%2B%2BeTuqBPHiN9m95sD7yC3jA9G6seashDFiXjrxPW1L%2Bkxd3lSYnBn5%2BedTVYmTasXQUDSBspJpDRrc1FJkPe5iup%2BgZb%2B9mbAHc5lU8E68s8mBGkTX5g16HxYA%2BnGhwAUMJ3F77wGOqUBsJ87yvzw%2BffazFeRwx9%2BQtoqy3%2B3eE7pIaW5SsFfekulCmuO8bLOMsSb1%2Fi6gqOuz5HwVgnOZ4lz7irAL2aARVBFuUyf6UWtr5%2BBiWAYQbTdcOEHXQukySmwDmU9AqA5G0nvzSgxUjFjqTXg1zOmPNUKMchrJHAXIPS1UOV411kJIS3pCIm0C%2BdTn5sM4PWezsJAnqegZgFAa0nghQZQCfx6xkdl&X-Amz-Signature=e17ae2b475c37aabbb967190a57a48ba0fbf1a761129c722f5846445bd69355b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YI3KLYO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOcDfRotyBDNIfsanTKz5b8VTHgK77oNjYRszT7Ua9hQIgMh3UVsyT0x%2FIe9WPuJqP0mIegOMpLJ7MVjKKkgFfy4kqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4cOl8s1NCtHWyHYCrcAzbrY3aAM3Pedn7gPKC8K3lVygFoU9PgEfiowQo%2B5BKG%2Bbr3K%2BAxRT3WRiRHVI1P58kc2U74yFIi%2FFTuP1w7AH2OGLrDT%2F0X5sU2HIJIef3yazccCjwCIB8HrrNzpXjADQlIBdlyU3q8q%2FUMoVA%2Fzo%2BQM6ooXNbyFGwPXaxXn9KPCl65iluhDCs6NVTfjDan8TkF7p3757B41gGwQfVFqw5QhI4iI2WhhhKSQf7kpDkgyvgauQT968aqBm8PsNqOf5amUX1%2FkUHjgA99P%2F%2FjP4%2BJe8l%2Bn3AZ5snpKQ2Q%2B2kWBFpYs1CbCk7T7ZxaXYzXcsC41Bdg7ey3JilOuSMqoJUf%2FOZnUfhMGxXFIvlQnAcF9PmuodEZFBqgR2n%2F1tYIZxTL65V02HDVLdCoA2fIQpxiUVpr%2BfwnRYrkrJA6PDlDGW22KLaP4XRJkdveqW%2BWRItBBqMphFIOF1n%2Fe1niuRgU0Z%2FvH6a9OeWjuGqKWwVRYDFaZPYmztD8TJK%2B%2BeTuqBPHiN9m95sD7yC3jA9G6seashDFiXjrxPW1L%2Bkxd3lSYnBn5%2BedTVYmTasXQUDSBspJpDRrc1FJkPe5iup%2BgZb%2B9mbAHc5lU8E68s8mBGkTX5g16HxYA%2BnGhwAUMJ3F77wGOqUBsJ87yvzw%2BffazFeRwx9%2BQtoqy3%2B3eE7pIaW5SsFfekulCmuO8bLOMsSb1%2Fi6gqOuz5HwVgnOZ4lz7irAL2aARVBFuUyf6UWtr5%2BBiWAYQbTdcOEHXQukySmwDmU9AqA5G0nvzSgxUjFjqTXg1zOmPNUKMchrJHAXIPS1UOV411kJIS3pCIm0C%2BdTn5sM4PWezsJAnqegZgFAa0nghQZQCfx6xkdl&X-Amz-Signature=f17cdfa3f71a464ca839cc1d1ae6674340bc4573cecf60ac952eec3c75917e84&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=7cfb3aaeed9158d3383676d85a513daba2dd5d8e124488a8f057169978fb4426&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=36c898f2e3bdade02f406656d658e83e03d9ac22e3b48a2a08fa888334cc9a26&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=6020fdcaeb20f3947f911e943869f6635e5e819d59456e6d3ccf94ab20e228ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=ef00a2e944bc2503ca3bc20357c55a156f9878c996d752cc8c70c5b67680fee9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=ad0e243ba81500616d18a65166d75019236fba40f870655a2e6b3a1d7d20ca8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635L5AEI4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBYdcuzAhTm2vONRribqGVkoVGj3Kj%2FoaXdULc9B3MUGAiEA73ngN%2FlOaiuOFa8dWsE4%2FNh09R2MRsEbb4vgZwoccGsqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBV0SUDAgeK0wJKEBircA2WCMV%2Bv3fY24ysaPM9U8t8Ahn9KfVIYyfrLGgOO%2FYpAC1gEqfkDdBCIYkNrPc58ZcEMnNoLtdCdTiAMw1F0hX8qo196SWW5%2FNGXUWepzEdCJv2FAHeC2nO19FMomlFOycWPRbctHbcaa8e8s4jnfxCMUEKhX0Lw7btP8AyIUlpxVpPjtNn5PmEslpJmVbHY0ZtLOZnpfgNZ1UIN6P9IG27Vv0n00cmtZDZjhzZt6l6ws0JDpNJyaHE0jxK2sTURMMBRJb08CiGsK1evZ3BJ%2FHbTk%2BFBvTeWyM1IxIsK5oifUzIhz8mXyIIiUrKutZgDNvvW5ZhFjeN1vmSVBtt%2F%2BFfhTFFSd7KaCosHzC%2BPPYFulNxWzj%2BJulGgXlX3brg11j9SLTRC2ok5Q%2BrmctXFNERevPVS0vg2B5q1gnIGhAWYS6cYwfr6dHNzOUXeCGlSxvnGGn2lYBgXIJnkLPPN3zgZ08wbIPRZ6mv6XWA0ii0nS14O5%2FCR0BOvZcXLbxVfcliR1nsjjWME7tvB7ba3xpmPEanX1iMAy1IuFRTWM3%2FkO%2FjPTe%2BFf3HH1luMT3TOzYR9u7PhHRlONT%2BxOxXu7eU62rOub5Bnau2qHbNnib6tX7Lf7KlJXj%2FkXwSyMKbF77wGOqUBa3LjJaKhZe6F7pMGbmhecvXjEiasqPRE7qa%2BU8y1Je%2BjzM%2BmvTHcz8PulhxsIKWBddWfFH%2F8VbFsQTBq6ZHG0cAJdmQrGHS7LPmOkbLf1qSDebZ3aIHvwcD74FJUUJVIiasMqFGPIfBNQmA9QK1rmPv4kqgbaaMPikZ5QaqmmBKwY9NX%2FzMwtUjYdyFinWI2%2FUoziULt0OvBDfcZZQd%2BKROHRy3J&X-Amz-Signature=5875c870da31091771a4169efce00387f3719caa26b2591867a5c3f788ce6fc9&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKUJOWLQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyvoBWEQ5Y3FmUmZxBnugI7O4da28ZhxdgTgA7W6B7%2BgIhAMsS1ussTOHX8LQiuoRykYogiX46M%2BomMUlzc9qtnq12KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzH7HGYQG1rAL5pOAgq3ANwq%2FTy1dK%2BL9IlQjJUMY5KxL2bws02Lm4taTVU7NtnJoRgzF%2Bcfj2nvLoLYNx5%2Bu9NX%2FKZpQPiHZJC4DswGBt6Uo809A3mvRsejJ%2FtXZHsMJnvD5Lep5WYDsqP90i2Qw%2FT3qk9Lf2fPrpzd%2Bk%2FHzujoA5uhe%2BVLMdsymx%2FhFhcyEvE1%2FXb4qlAVznHlfuTQKd8jcq0aEW%2F56nRwbUH8DSfcsn4nEk%2B0tfTsyteYS53gKhyFTBiLGu7ftB1HmGC2kD4bRZ1krOMnFjzlFp7JhN%2BJXWXjdLBFLQ9BOPXNT%2Beo1Kvlbw6gUmTjhMJU9HgQ9QK7ygWYxxFTFzegjFYD%2FV5WTbYR6q7yH3%2Bq0n4K3nLJs%2BSH%2F5zuxtXKIn1r3w0%2B%2BTFWgNiugUrjg9Dw%2FK7RDRDLVhcIiqd352QqZxCTZ35qWnapwQlUR5N9xeW9lv8hMyfhuNt%2F78vm362MJwjhH1EEOhoZcInSzKwBlMy5%2B2XbWD5k6EeMyBk2Deft%2BQaWZ58vsk16ppNFnDHvTDeD3vYv2ai%2F0e2VkUZ6x3BMKP%2BiKtKOV5JvAaalKftGIlY0rhyeekC%2FXlTavsaTK2A4kWDuwDvjDPEX49Sy0M0yklEDPrtXZvjtsGCYvcb2zDVxe%2B8BjqkARjOLBoOJ4u35t3wPa%2B9fvogL19n5sgT1BWaju8qAwR5Mv4gR8FV1ZmQ0H1F5mHxDqU4xKRgYSgINfS7l9awQF%2Fes%2BD%2BoXGJD0Y7jMwIXJFdYhZj6fHr%2BD4zoUzBpTMQwDd%2FBxQplXNqWzNf3NOV%2B%2FjwLGgODjFrRKLPwcffkV%2BVnpcLC792bzQx%2Bi089Ycugp%2BMQ0q%2F%2FBR7JxJDzy2CSjVQHJ0A&X-Amz-Signature=72a43ccb785b2318bdbb0b0a3106ec9c9f1e6772e641e0ddfd52b90185debcd3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKUJOWLQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyvoBWEQ5Y3FmUmZxBnugI7O4da28ZhxdgTgA7W6B7%2BgIhAMsS1ussTOHX8LQiuoRykYogiX46M%2BomMUlzc9qtnq12KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzH7HGYQG1rAL5pOAgq3ANwq%2FTy1dK%2BL9IlQjJUMY5KxL2bws02Lm4taTVU7NtnJoRgzF%2Bcfj2nvLoLYNx5%2Bu9NX%2FKZpQPiHZJC4DswGBt6Uo809A3mvRsejJ%2FtXZHsMJnvD5Lep5WYDsqP90i2Qw%2FT3qk9Lf2fPrpzd%2Bk%2FHzujoA5uhe%2BVLMdsymx%2FhFhcyEvE1%2FXb4qlAVznHlfuTQKd8jcq0aEW%2F56nRwbUH8DSfcsn4nEk%2B0tfTsyteYS53gKhyFTBiLGu7ftB1HmGC2kD4bRZ1krOMnFjzlFp7JhN%2BJXWXjdLBFLQ9BOPXNT%2Beo1Kvlbw6gUmTjhMJU9HgQ9QK7ygWYxxFTFzegjFYD%2FV5WTbYR6q7yH3%2Bq0n4K3nLJs%2BSH%2F5zuxtXKIn1r3w0%2B%2BTFWgNiugUrjg9Dw%2FK7RDRDLVhcIiqd352QqZxCTZ35qWnapwQlUR5N9xeW9lv8hMyfhuNt%2F78vm362MJwjhH1EEOhoZcInSzKwBlMy5%2B2XbWD5k6EeMyBk2Deft%2BQaWZ58vsk16ppNFnDHvTDeD3vYv2ai%2F0e2VkUZ6x3BMKP%2BiKtKOV5JvAaalKftGIlY0rhyeekC%2FXlTavsaTK2A4kWDuwDvjDPEX49Sy0M0yklEDPrtXZvjtsGCYvcb2zDVxe%2B8BjqkARjOLBoOJ4u35t3wPa%2B9fvogL19n5sgT1BWaju8qAwR5Mv4gR8FV1ZmQ0H1F5mHxDqU4xKRgYSgINfS7l9awQF%2Fes%2BD%2BoXGJD0Y7jMwIXJFdYhZj6fHr%2BD4zoUzBpTMQwDd%2FBxQplXNqWzNf3NOV%2B%2FjwLGgODjFrRKLPwcffkV%2BVnpcLC792bzQx%2Bi089Ycugp%2BMQ0q%2F%2FBR7JxJDzy2CSjVQHJ0A&X-Amz-Signature=aa2ba5dc7aadd82af332342cf2cd398bcf6cb3afa9779d4ce602b5056f4fde66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HLQCFAH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBi6Kqozsil0NkCM%2FpJCHZfUz9vVFD%2FqOPWqOO4kjufvAiBw7TPesCL2IGX1fBsYTomwoWuLIEhT95%2FoIcqLtuFd0SqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEqH%2BtH%2FJhh9KWMj6KtwDO7JWutL5sXZ90H4RB6OqvNunEuOYWZPCWYHesSN9sUIlasWYAxj%2FKpNpCBKqTgKlwXUq5Yd%2Fa%2BP8s4T2rq%2Fa7BO%2B28YHLaUUMsDJCh8uPDCkEy2x%2Br%2FkWTyh3SvBBrIvCFrhxOhF1bNmudtALwoginJOmNy1jNfTs1sd9op3fHuBRDaPRqNsyq9x%2BEKdvztdEiTw2cuHqAzc4WUJR7FtFPBTdsdLu4ub8gN8HBaZ%2F2pFRGVFAO7wzG7FMsfpo2u%2BafKWLC9qlA6cfTK75LoyVhP4ykbnMB9ygwyTrsc1v2FiZEixBadeCqDom49dSqzHNDT5Hl1i9uPHBRZZLPVp0Ngv1ZC2gkWC0bpBPsbXNI6k%2Btexbxv5HaixcAV44VycTq0lfvSxcuuXZ9oJYCtspx8k76HVeMkdwI092MRHvBvayM4%2BI3k7PYlEAkt%2FsgQkIRo0hbqcceDHsiE32c0YhsnHGUZxUh9HCIzKwVKxk2zeoR6h2yZaMy7%2FjFh8cVNEstndvNiRTpP7nfz%2F%2FhtyCVlWpVPI7IgdLiYtZKLJh2XAjeiQUxTwz1Bnc9NOmpCnU5PX7u4fkWhW%2FSPbMAWSKoikya%2B2E6F%2FUuHXJJgJR3eaCER8G05GUMDMQLcwp8XvvAY6pgFme6uCVIwddt9iEU%2F5ob2jnn%2FpIyllJrmQ9t0SYcZrJCemQaWxaV2Nr7PBUTnhHuPd%2F9DUQNdFuvYmlBVZVkNpz9AnfKCv2XQ52YAzzQBC7anUl2JFhmrRhaZjgT95RuKql1bR%2FKfvcbmiTyUine8UpV9s2DImtiAcSvBvWtRsOr4FB28%2BddW7XvZZt5R1ZR5%2BctgkWZq3cs%2FWyLAdlwyXf9lKvoCA&X-Amz-Signature=eee985d580a831af723c53b7259658d6c957945762dc78aeea9f745b2ac024f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256DOOGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGESd2cGnXni3Kwiq1%2BL4HDFcafuftubrGXlPoXDF9I6AiEA%2BxQNiQNLRyeP4U3YPbZI5BSaaeqxR2QSH1ymfgBUlygqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3x5GjHedhdMM%2FkfyrcA0THop54ehDFaro3%2F%2Bm78OXymT7lV9nyfOwLkMqn108bbHj2NHTGGCvu5PEklh7xIaj6vhBarQO9rWW%2FxscbH5J9oDQlZ5ClXHBu2kH8XIqPeLJN8oGIhNal9gWaFSjVmTjgSxCtLsKnUOHkYfBTSxe4DrcSs2i%2F%2FCT1y2Hb4SDN4oEu6lOneD%2FQfrV0g7p8wh2s3HHaQKSn5Ky36f9%2B3G5kZk7h7Gh%2FtOZzxV2Lkd13gf%2Ba27H5TokAc4qaMJEmwVVinYqD%2Fz53HWN2wNJCDnjpGQ8aywuxFGYRhdEOJuWeQcxIadpPqTC%2BoY4DiGxA4FswELx94h%2Fgr4kmwUrDOb1ZaIicFBdvNcodj%2B2C1NjxueQNz93bFq480ttE%2FgHtUFqn%2BYNFElGcrZ2dh03HJjYy1rSwJjtVv2jpRH1rTYVRb9OKo2HsRs0KEQTS2u8fOo%2FD%2Bc%2FA11PKXMWIQuz78AGkapJIhzF9fV31Xg8JJZ6JZ4ubj01z3ZVM18zXzsVRzrhDb%2BiRC3%2BdhtgyLbiFuUva3u56HHOC1TMl0OE0Lc1Tv5Usdo5IYKa04EEVuwAfwzvIz0Ks4Oywurm6uktMiehzvojomo2RZB7vrzsE8qnIgbnUflkpWAosx%2FoKMKXF77wGOqUBdJ%2BaH8Wysyr5NAyvgs6vhci07TU2FDpMPy2K%2BJUG%2F%2B%2B6H58a8sC1GJEC6TKkzV58yFsINhq%2BKW37lbOsNqtkNfd6wOBClTbDwm4uBh4cBXOTkD1g9k6FkRyY5t7VjfFBfIJO%2BA3gQwSkcBRBKJbYFVvBYi7LDcWwy%2BcwEHPFvOQVsSvZemqjt6K%2BymIjt2f%2BedDhdZFVdG0N32H2Z2yaSMbtG3pD&X-Amz-Signature=0c4c5cdf4b6e9b3e8beda1acdc53f1c180f65fb29619b4044598cf816f56e444&X-Amz-SignedHeaders=host&x-id=GetObject)
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