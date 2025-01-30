

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=f253c2aa52fea27336a20a381fd2bc85446d18792f81912d62bfb09ce0b5c210&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=27cfe962d42d396259dc3404e341f381686e98cfe7551c0f145ea8bfe61c8c3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=c67b8718552ccd00ce5748e5c6781baaaa583b74e0aabe09c21dd4aef49cf775&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=c75b939dd427f371801f78d4246bb4cf54a29224d354f24158bcf87f3581601c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=e4bd8bf96785c1f6dcb3d797e56b82717e9907d7ac2cf9f0a9bd846a1c0fbef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=ce219a38a800e26fd71e11d8c13a6d59f1c87a46f8af63ee1141b30131f245d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=5072b3698d0494f067e0bcd61cb51b1fd3f4e983fcd54cf0ed3b162c09851aef&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=76004ec58dc86d0337d721fc0f46c4eac4d8961be7ee324b8a0700cfe74a9340&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=1ff26c7aabe605acd04cb37d7512ec362a35ec3c35e3f17f866ff76b6fc96f47&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GFIGEZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICtaJ8cSF0DUELbCoupdgyVExEqEMy7lELIHy6D%2FibTEAiBXL0%2BYct9KObKYsP%2Bjhkg4phCZGtn89aBLdxpHUrPeeCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMB1NS6sgwo0SLI4kKtwDp8W6W2tliioTSWPjQHJPlD2Mv9E5kDBtn%2BY5ncfHHE%2BH5%2BBcfnJd7DmFh7Xr10Pw3MmcfIcFx985gAh4fzelu%2FyAIa4%2BFobiFSK8W27yd9cC%2FN66uJgNtkBhJykLHAWmcWL5UcwsKMNsC3lmOd1AHEVybACpU2%2BQ8CLseSWn4l2v9avcKmmRU2TAWZYEiyiStXwmRs8Cz5yner1zyabEvuaI%2FIdgVpnTpbp3wMdDDH9EK8V%2B7tOJ9%2BV1d%2B2hb3NytrvzgYgOcSgB7Fp1bn1mh4B1Q%2Fm9CXUYjWG20Phhqqiw9dvBonJYJqGpVD3sHVVCrlJWSAopCizSbvWbJqdCfk86%2FgdwP2AIYMSeQfi6rlrxe3IoYycLTAmN9Y8KuHymyLhaIuHGaGmy1tbwHreDf%2BeqmMdRt4DtO%2B6Y2Hqz5tqJomsFlYVUIy4B%2BXoqQBN9OXI8KRWCNsDqAZSHU%2BlZHbiDuy0fcFxCWann82%2F9zFBBLHR7%2Fxn2uR%2FF1zm9bL3u1ZUtJIoWfB62Ro5SpQz5gnR7I39pZHx95jOZ%2FHrGhjLzKNxccfCdoXxw1AjUaRX8Pa%2F9%2FbnUDdRj2jwRFtsyBQBCCWEIG0hfnxJdx%2FQGC4jE8shzj%2BveQ%2BU28SwwoqPsvAY6pgGz0SN12yYacqlg%2Fh2yc0ZMsg7qQyKQtViDrjhZOxO0uRQ8YOA2hsTWbDNjOPy%2F6KufjEnyYHXmTSyFD4BdgajrXJVpeEQ06soxojjZ6NjOcxoU9aK2ucvup5VAcp2F5KzTFnUgT7rIhcDmtfDm0XqEatPW5Kqtt%2FKxcmOier5IMajUH%2F6SjDRuPPe13ZS%2FOX1hVz0Zyy5upL6HgRI0KPsFq0jZx7oO&X-Amz-Signature=c2d8c529c9d63cf2e0704a6ef1367d2b29f12d0ba548433c9af73578b486b7d1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GFIGEZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICtaJ8cSF0DUELbCoupdgyVExEqEMy7lELIHy6D%2FibTEAiBXL0%2BYct9KObKYsP%2Bjhkg4phCZGtn89aBLdxpHUrPeeCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMB1NS6sgwo0SLI4kKtwDp8W6W2tliioTSWPjQHJPlD2Mv9E5kDBtn%2BY5ncfHHE%2BH5%2BBcfnJd7DmFh7Xr10Pw3MmcfIcFx985gAh4fzelu%2FyAIa4%2BFobiFSK8W27yd9cC%2FN66uJgNtkBhJykLHAWmcWL5UcwsKMNsC3lmOd1AHEVybACpU2%2BQ8CLseSWn4l2v9avcKmmRU2TAWZYEiyiStXwmRs8Cz5yner1zyabEvuaI%2FIdgVpnTpbp3wMdDDH9EK8V%2B7tOJ9%2BV1d%2B2hb3NytrvzgYgOcSgB7Fp1bn1mh4B1Q%2Fm9CXUYjWG20Phhqqiw9dvBonJYJqGpVD3sHVVCrlJWSAopCizSbvWbJqdCfk86%2FgdwP2AIYMSeQfi6rlrxe3IoYycLTAmN9Y8KuHymyLhaIuHGaGmy1tbwHreDf%2BeqmMdRt4DtO%2B6Y2Hqz5tqJomsFlYVUIy4B%2BXoqQBN9OXI8KRWCNsDqAZSHU%2BlZHbiDuy0fcFxCWann82%2F9zFBBLHR7%2Fxn2uR%2FF1zm9bL3u1ZUtJIoWfB62Ro5SpQz5gnR7I39pZHx95jOZ%2FHrGhjLzKNxccfCdoXxw1AjUaRX8Pa%2F9%2FbnUDdRj2jwRFtsyBQBCCWEIG0hfnxJdx%2FQGC4jE8shzj%2BveQ%2BU28SwwoqPsvAY6pgGz0SN12yYacqlg%2Fh2yc0ZMsg7qQyKQtViDrjhZOxO0uRQ8YOA2hsTWbDNjOPy%2F6KufjEnyYHXmTSyFD4BdgajrXJVpeEQ06soxojjZ6NjOcxoU9aK2ucvup5VAcp2F5KzTFnUgT7rIhcDmtfDm0XqEatPW5Kqtt%2FKxcmOier5IMajUH%2F6SjDRuPPe13ZS%2FOX1hVz0Zyy5upL6HgRI0KPsFq0jZx7oO&X-Amz-Signature=798209f15524bc195f820a21514cac63dfb33379c130fb3585b7dfac1e8150bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GFIGEZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICtaJ8cSF0DUELbCoupdgyVExEqEMy7lELIHy6D%2FibTEAiBXL0%2BYct9KObKYsP%2Bjhkg4phCZGtn89aBLdxpHUrPeeCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMB1NS6sgwo0SLI4kKtwDp8W6W2tliioTSWPjQHJPlD2Mv9E5kDBtn%2BY5ncfHHE%2BH5%2BBcfnJd7DmFh7Xr10Pw3MmcfIcFx985gAh4fzelu%2FyAIa4%2BFobiFSK8W27yd9cC%2FN66uJgNtkBhJykLHAWmcWL5UcwsKMNsC3lmOd1AHEVybACpU2%2BQ8CLseSWn4l2v9avcKmmRU2TAWZYEiyiStXwmRs8Cz5yner1zyabEvuaI%2FIdgVpnTpbp3wMdDDH9EK8V%2B7tOJ9%2BV1d%2B2hb3NytrvzgYgOcSgB7Fp1bn1mh4B1Q%2Fm9CXUYjWG20Phhqqiw9dvBonJYJqGpVD3sHVVCrlJWSAopCizSbvWbJqdCfk86%2FgdwP2AIYMSeQfi6rlrxe3IoYycLTAmN9Y8KuHymyLhaIuHGaGmy1tbwHreDf%2BeqmMdRt4DtO%2B6Y2Hqz5tqJomsFlYVUIy4B%2BXoqQBN9OXI8KRWCNsDqAZSHU%2BlZHbiDuy0fcFxCWann82%2F9zFBBLHR7%2Fxn2uR%2FF1zm9bL3u1ZUtJIoWfB62Ro5SpQz5gnR7I39pZHx95jOZ%2FHrGhjLzKNxccfCdoXxw1AjUaRX8Pa%2F9%2FbnUDdRj2jwRFtsyBQBCCWEIG0hfnxJdx%2FQGC4jE8shzj%2BveQ%2BU28SwwoqPsvAY6pgGz0SN12yYacqlg%2Fh2yc0ZMsg7qQyKQtViDrjhZOxO0uRQ8YOA2hsTWbDNjOPy%2F6KufjEnyYHXmTSyFD4BdgajrXJVpeEQ06soxojjZ6NjOcxoU9aK2ucvup5VAcp2F5KzTFnUgT7rIhcDmtfDm0XqEatPW5Kqtt%2FKxcmOier5IMajUH%2F6SjDRuPPe13ZS%2FOX1hVz0Zyy5upL6HgRI0KPsFq0jZx7oO&X-Amz-Signature=41ed48a7fd703f715b510c3b0abc2224ad543b5943f967b8abac4e63de3df524&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=683f4255c3f83941a3a268708d3850317a36129907ac3cb156a25a5625fdb5db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=cffa7ef2cbbe7aba9cd2b4da97706070f125a321052490e0ae22796d59cb61a3&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=10387beb496ce9c532cebf04522db7836088ca239e18d5dcbf6874fcc0640072&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=c97ae8d53cca75f62561ea5ac7b54af8b36e0ddb6577a5c16b3b0ea72d820b76&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=873c1d37d4a0cc6d870efa02bc26e1320fc9b06e78ebd85295311fb6efcbe727&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z55IADJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHU2MxCNCR5CsiavRlxDvTdQ33JdE26%2BYiOPKR6qL3UAAiA82R6z1KXF1X3fuVemjh9dgZWend5EOnqsNfk0V6P93CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdguL83YcQpF%2FNE6QKtwDetDJ2AF5uN6jNfcIt0l0eRJOeuJYjFj0PQk%2BXnt%2FPFPfqaowcc%2Bn9w3NPPEx2q8hBGRmV%2B9bZy3FWWk8w15SHdGeYw4AV2CYTHYtreF4UoTp%2Fp%2Bv6sEAnSkLb3TDA03o0VakoG6GuM0yKp9ZOyuWDXZ1mCQ8XCzie5aiJU%2BNJDG8fZuDKjNHPY7%2BOzCZgzOV%2BIW%2FrNwtt1EbMAr%2FmbnVo%2Fn5TPrnx2lL45smRgF0364mOhp%2Fw00mhRAgQ787o%2BBF%2FLLbQrJ803LV1651yX267QWPru4u1wlGCKvTDqm%2FbCHxbcL9aeGYf8AaygLpvCVOEzyp%2FcOb5FArel2klJmrZIxqlYagbgvSYaoqiRjGoVnQiIfBmS0PwilVLC9fJpu5%2Flp0wFvkBn5S1SnoYva6%2BcWhy6oDU7XbOwK%2F2f1R0UEWXcsjRO5328v0%2FHUzOrQsWOQesU%2B%2FtAC7ZKiA%2FRd6yHdiFYwVsTvXE%2FVEMDWwyVYfX5oTu3Yb78vCGgwGUO3RPtHQ7HN6YMz6VTRy2VfKad0%2BuaxGVwsZZMPTETmoqaaHazwvg199gZWLQ60b%2B%2Bo2HOjIfTrp%2B64zgQ%2BVPchel%2BfB1cptojweafE8nfi%2FEVkNLweCVtKFTKwdZA4w96LsvAY6pgEKpS7nkvcw7g6xgpr3FzMkdswamEP8VTtaoKCt0fOrHsxgtt9S7VZET%2BvnkJugvHkMt7koDcBQ0Z7EJBFjkahxbdt9PXaN4Hm3Ho6NJ7zNe1NGDtWDWvwLo4bDiAytLjLDyrLMIExJD8wglQ81KO6epRhQU%2FU5TZ3q6cGZbcVyR4O8HKo5IqSPYxkQcjIR51ZY34INrNS8phlomy6TKiNwfIBAbi5o&X-Amz-Signature=b22177d907e721ad1e46cf6a74d630db05196e61ba8c185de7d638fdedbb35f3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZAK4TFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICe6bmPsjiKii0TAOG%2FZWWMArA1ON3dz9FavMzwh58M1AiEA3Tjnqu3MF7yVbtAZ8hnpWZ7MCeMgzVwN6vKlY8%2BT3EgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8KMpJU8O%2FoX1BieSrcAxgaDuVnKuxsASAWL5wrqfe82ZECN819i04iMNDCceRdInUd%2BlfjRRI%2BgCfpcKTcQfM%2FC2yQZc1AYeiI%2B408jqoFLzrt%2FA5eDuNpnofZN%2Fl%2Fr%2FLAZ2bF2TDAwruEpltKT3FMqpio5uZXVo8e3un3z6X37Gucleu4ROHMuuz%2F9fKQkfUCx%2FGK6kTz91rTI3%2FL5vpWYo71wpqqLJeMmZHA6QFJbyzEiWghyOxmeTU9GrjU6zzjT5xWmJbQv%2FGYWOkaxQIaPI5QPspl2dtnC8SXsTDMbVenudL2%2FM%2BC8bkqJfc%2FDNvAfcQaLx9IAPSr5U%2BeGL3iDZOJFDvDkR1Pbqkn50jv2kW35tCT0CqwXQfE2GGeNW6Z3CZ1LDO45dV5J%2Be9jaujOdnBcmD%2Bej4bFBHG%2FO9vADJKeqFBSq74vPTtUeCHtyjEHyYli85tgafJyMFTQ6LL9s692nbujwaLA5MBwbDhtMjJ4Aj3luEPKYetN25G2hPjEk46b6miruMzerqxPd3qRmohAcuBwm8hS6uxQn4fNfikbqCT7%2FxClG78rKilk3wZu1fub%2FbLEd%2BtTSN4zqBn3irL923aU1SgSjpNcGbA2wV3Ulej9g7GX4PUcms%2BtxQw37xVwE%2BL%2FBLkMPii7LwGOqUB8mOBkZPoceeHZ2n3YjCC%2B10GY3Np%2FSs8nTYqqvatfLxVdtcUzyXl4Z0U7AiqlQpNtNJ7Q%2FKUSVSKb3xbLL8TBQTtutCnJJJMOEV9R%2F0EZLM5%2B4CTZ%2BKQ6KvElA3687Dsi1XXHpWwmm3RPV3BzFfsZEf0v%2BS5IiOFuVqZauovL0VnwJkdSi94UZJo%2F%2F7QC7EpVfOT8%2Fi995nkmeLyQNpSeT2bz2Ys&X-Amz-Signature=b359eeb5037488245dbfab70b81a1cd5362aa0f22c6509d83ed128a0b0c6de89&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZAK4TFJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICe6bmPsjiKii0TAOG%2FZWWMArA1ON3dz9FavMzwh58M1AiEA3Tjnqu3MF7yVbtAZ8hnpWZ7MCeMgzVwN6vKlY8%2BT3EgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8KMpJU8O%2FoX1BieSrcAxgaDuVnKuxsASAWL5wrqfe82ZECN819i04iMNDCceRdInUd%2BlfjRRI%2BgCfpcKTcQfM%2FC2yQZc1AYeiI%2B408jqoFLzrt%2FA5eDuNpnofZN%2Fl%2Fr%2FLAZ2bF2TDAwruEpltKT3FMqpio5uZXVo8e3un3z6X37Gucleu4ROHMuuz%2F9fKQkfUCx%2FGK6kTz91rTI3%2FL5vpWYo71wpqqLJeMmZHA6QFJbyzEiWghyOxmeTU9GrjU6zzjT5xWmJbQv%2FGYWOkaxQIaPI5QPspl2dtnC8SXsTDMbVenudL2%2FM%2BC8bkqJfc%2FDNvAfcQaLx9IAPSr5U%2BeGL3iDZOJFDvDkR1Pbqkn50jv2kW35tCT0CqwXQfE2GGeNW6Z3CZ1LDO45dV5J%2Be9jaujOdnBcmD%2Bej4bFBHG%2FO9vADJKeqFBSq74vPTtUeCHtyjEHyYli85tgafJyMFTQ6LL9s692nbujwaLA5MBwbDhtMjJ4Aj3luEPKYetN25G2hPjEk46b6miruMzerqxPd3qRmohAcuBwm8hS6uxQn4fNfikbqCT7%2FxClG78rKilk3wZu1fub%2FbLEd%2BtTSN4zqBn3irL923aU1SgSjpNcGbA2wV3Ulej9g7GX4PUcms%2BtxQw37xVwE%2BL%2FBLkMPii7LwGOqUB8mOBkZPoceeHZ2n3YjCC%2B10GY3Np%2FSs8nTYqqvatfLxVdtcUzyXl4Z0U7AiqlQpNtNJ7Q%2FKUSVSKb3xbLL8TBQTtutCnJJJMOEV9R%2F0EZLM5%2B4CTZ%2BKQ6KvElA3687Dsi1XXHpWwmm3RPV3BzFfsZEf0v%2BS5IiOFuVqZauovL0VnwJkdSi94UZJo%2F%2F7QC7EpVfOT8%2Fi995nkmeLyQNpSeT2bz2Ys&X-Amz-Signature=d6ea6f9ede56127c3bdd27149612e5a5bad86162ab1760b92607f4f102001a0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NUSJXQR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0Kc2bi0CHi%2Fffv0ij6g94Mw2ft3XewUjtPPs%2BPZjeHwIgcmaT7xmxtQe5%2BAXEKPuKQbVv7rYs%2FeM%2BSWDwKgft3KwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOgLSG%2F6l1YDZ3l2yrcA5LAOsaN%2BUkAN02IwbMXAm%2BdFeHusy93tQ3NBavLME6tscW%2BWVnHc9T9j0y%2ByTM%2BAFbv5V0kygLz3xgRV8cvmF25XWAVmmS1pgRoGCsR5dnPYKIwhsM7ySeKQkcD20WwCB%2FwP2V%2F0RmCVwrFG2WaNersnDb6TVBkRSBmr3JUicWZQhbVxsSV0BOoGjcp4cmcH8%2BBx%2Bd2XEt7zjntB3TINd72pVHrNXwWnqo4fPnON8zamOf1FR9WAAhl%2BOWber1TUPJDvjtN7Qwp2K%2BdyeLyBaiTc63ZvlmofGFG%2FvEZLnsX6OBoSQNJbcHAMO%2FMmokmtC6NUPqfVabTS71kbzRpkLcIr%2BXoXIXOQvqNLSmmiNPUf3%2BPM0QsxCyjkrZVsFOu7qKXra8VMVwPVoyrsvlL6Jio41ngYbQfC%2BOqxHZs1BoamqFrgxhNHqyChMBRREMU%2B7mxcmNFoep4CunG6XANgwf1jKJDOzSdpSmp0uos1BxxSmSFCKDPu%2FFNxRamUMtRncTutCsaxwI4vG5gcFA73xr%2FMX32RN0i6TNubDNS6Zrv2yM4UY2MB%2BXl7G2DQV5BMo94rfYgTOZHakYAg2hGfjU75mrTB1%2B9WvUWtBUbHYMTYtmlr7KnC5N1pza8MMei7LwGOqUBdJ6GQM8RsGUseitOKAfDJkeg7A8a3hqIEebZ2yDvZt0QhHK6qnWDkDKv7rHiM4pnkwHxiYqN40VRNVtiPVs2gSw3Jav5wcRDqBooOJvegMIg9%2FE8riBikddTGjoEUbbGd7fbaVtlQYtjxdyuUMUvVISVDPXVzzWuzUxIlIdyeIDi89FXTwQXx%2B54ZiXiAZKPm75A7BTEHa%2BlN3TdvPMOyi%2Fkm%2BEZ&X-Amz-Signature=51970c3e485fafe19fc08734e5dbde1b92cd94c0a7dc9bb15ef850d8c016bb8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TNKFH2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLHCsFC%2FJ72koH0uAiRQgrSdaTJkOPz9F%2Fu3tun6ZlXwIgFDDep%2FNQKkR5ERirb2NYH%2FT0yOSKL7EEuvG2OOoUc1kqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY3FvVWurmQMIc6QyrcA7ItrbhVeNalFDtH%2Bc0VcRNXkBdqyHQuXpa%2BjRlINGGCIS%2FeKpxTGXglITSwbigQt3xBwIC7ebokSYgrKnxjO7AQULpiGZygVhiGc24s4rpwjZD9NjHKypOPCd5PORGby2pESqEYQrY6HqS90JaCMm5ZqvrJKNLTBKY%2Bk5qu56iDvfx0wlAxjI9xGcGelY3lnFLxbRkd2tx7yYqMoOAsnqKO9Q5YqI0k04aNAWbA54jdZ7GI3BNFfNf3bNTPFwbY4aeRWwFzn7Y1IefnO1X2x7b3FSFN8qrxXLLuL%2BPVvPYIAZ0TU2KSwdR8AnAu%2FLERJYMwg9FaLJqmBEotjuqmCG5pgcrj0ABztWT604tvqXwGEgof%2FOKANPyyJW9oRVlEeNi%2Bu1RIWxrS8CsQQbcGuKmr%2BkwXdYMcl7%2FPkMa6qlmi%2Byq%2Fv2k3dgJAOyvJMMNGHbYEsujL%2FeRRXCUO2%2BGfNP90SmAd2NyQ8eP%2BxiOcRwYaCSD1Jonl1oRrr64TfLHYl2IweKkhj9TbmvnEKsun7ap0vCSMPvX8yAsZf0FmO0O0C6F9A93OdsI5UfoEoDdmIahrqjwT4kvccTFArAYSYs%2FMk7VA2qbuN6obLXeOgfYE3%2B6VDJv%2F82c8TjFUMJyj7LwGOqUBeJRvxHzr32cBLoWBY1OO18wTGpbiSI9Vso3vGWEgoD2cqhNmho9Eqy0jdtZ69Jq%2BLiuinF6ihersQhT%2Fac%2FnT0tolP0WHhu6aF0YvOy8p53FvqX85BqeDx9cwj9kfNZyEHkTi7Iuz3Tkam1ALOBtQcLJXOTUKRoDLwK6Sh2X1C4ef2ev8x21R6fsM%2BPP83O5rBzeZ3cSKiRvyy%2FnDFM0deLH8Rz4&X-Amz-Signature=adff559bb9dbca225a00e7f85eea474619f06045213735d522d9597126fcf6cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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