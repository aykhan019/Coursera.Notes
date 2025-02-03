

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=b6f1feeaa05f81375fb72a79f2db831627eaa59b23a01fd4cc836a8a74b16b78&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=24917a66553c1fe60b12ce35915514cffe885f20594c21d41c422fcbf2ff92bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=318df7d89a2a9069365e136fda2130158ed9b82d356790dc0c64e1cfd37a8904&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=48f5948813e23c27846a5449bd9c4346247b85136cfdb617e118b8bb5e41ad9e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=365f462c2829e88d62ac38b50bd79bfa47444a5343f57d678886553dc93027bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=25f32e3437711beca7c69e0aff0280c67fbb06f4b1eb43a5c17d62731680cff7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=5fd4dd797a9228b1e9d1bf0513bb0d08ce7b45f48f578f2393fd24898e38e960&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=10bc5965786a6fd35419faa530f754c02482861d4d82aea9f710492b80046eda&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=4d9ed83422abff39a6f78317e7d8072dc6b62c4a5c1d3a24f5e5a5dd9ba2f4e6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OFKHJKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIErzE1EZVfhShueu1iepBQODzCuaBTr2OtLwyzGuZc9zAiAZ57Wf%2FIegnmu1KeOAmnceyWCnNShtD1VsscRZB6aToir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMfmuAJI9t4JMshHPdKtwD4jSzPP4S4yQGa6EOnivyxbpW%2BzwbGokTF9tSU07pOGHGTr0n%2Byi%2FKuI2Aune9IUQwF07TG9sYPg8XYsezjheK%2FHRgvqQwvjt9iMolcPZmKe59ytVZzf1M0YnZPts%2BnWqj6TRwKkhjdnDpcWd0xy1btfcJN%2FPGip7ceqlw2TZCGwWBtwyT896MI8yHy5DU39zL8yUvOkf3e5JIzS%2Fcd04JsN1boEFjjdKZyinmT5wYt4yXlqSchW%2BE7XcKEvuxUz9bczbgVJIP4ykq%2Frpzb7ypIMb%2BZx%2F%2FUwI4lEpx3O%2B4PzJ9ZOeSjfdGXQC%2FUUNtQFeVuPQ2fQwTWAVTKijZOQpbVLDIcExC29Ct2h2XTnJFzWYtXC%2FQyYQZQNjcLDizOz1RY1Qt1LSeTSiJXETihxbh0qPOYCUBAJkudEEZmc%2FHzB0VKlsAaE%2Fo7zTKRMV8eTAOphOlA5VNdNHK7o1GHfN5KHZWUDcUNCecBQyM8bproR50kgaYDSU4zMzVHqLuRWd49DDleVYjc4UEhX7rYxWe8QrdcMxeMxBtYx3UGw6Eg%2BNVf73LCuj8Sq44leOkDHUa0xraaeRuzqMjTJyImWsNdncCiYTRL0fWvmqJ2JxYQRHxfgMGn2991ddrC0wqvOBvQY6pgHAChC44i7FS6fCPid3AU6RxWJLjSnmjDtYVhS96qtNwlXCRONTidctb1Ro2sHukdvAEIfD9q9UoOwdVyDtZZbD3HlpUFnerBgFOI9w2w8wT7nrzqrkTi9xNnqKbWCY05PzFQwry6NcKszU1ZSkAKAPvxJeTS4Jz7ayZZ2dRRdf43DsGTePrcBaGom5MyFb%2FivWMVenT6%2BKWOmv5Dd61gtNy%2BbsOF1r&X-Amz-Signature=d8eb6156a1397fd0feedd453407fc5cfa963c93d185b5b11c7b03f2369bb365a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OFKHJKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIErzE1EZVfhShueu1iepBQODzCuaBTr2OtLwyzGuZc9zAiAZ57Wf%2FIegnmu1KeOAmnceyWCnNShtD1VsscRZB6aToir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMfmuAJI9t4JMshHPdKtwD4jSzPP4S4yQGa6EOnivyxbpW%2BzwbGokTF9tSU07pOGHGTr0n%2Byi%2FKuI2Aune9IUQwF07TG9sYPg8XYsezjheK%2FHRgvqQwvjt9iMolcPZmKe59ytVZzf1M0YnZPts%2BnWqj6TRwKkhjdnDpcWd0xy1btfcJN%2FPGip7ceqlw2TZCGwWBtwyT896MI8yHy5DU39zL8yUvOkf3e5JIzS%2Fcd04JsN1boEFjjdKZyinmT5wYt4yXlqSchW%2BE7XcKEvuxUz9bczbgVJIP4ykq%2Frpzb7ypIMb%2BZx%2F%2FUwI4lEpx3O%2B4PzJ9ZOeSjfdGXQC%2FUUNtQFeVuPQ2fQwTWAVTKijZOQpbVLDIcExC29Ct2h2XTnJFzWYtXC%2FQyYQZQNjcLDizOz1RY1Qt1LSeTSiJXETihxbh0qPOYCUBAJkudEEZmc%2FHzB0VKlsAaE%2Fo7zTKRMV8eTAOphOlA5VNdNHK7o1GHfN5KHZWUDcUNCecBQyM8bproR50kgaYDSU4zMzVHqLuRWd49DDleVYjc4UEhX7rYxWe8QrdcMxeMxBtYx3UGw6Eg%2BNVf73LCuj8Sq44leOkDHUa0xraaeRuzqMjTJyImWsNdncCiYTRL0fWvmqJ2JxYQRHxfgMGn2991ddrC0wqvOBvQY6pgHAChC44i7FS6fCPid3AU6RxWJLjSnmjDtYVhS96qtNwlXCRONTidctb1Ro2sHukdvAEIfD9q9UoOwdVyDtZZbD3HlpUFnerBgFOI9w2w8wT7nrzqrkTi9xNnqKbWCY05PzFQwry6NcKszU1ZSkAKAPvxJeTS4Jz7ayZZ2dRRdf43DsGTePrcBaGom5MyFb%2FivWMVenT6%2BKWOmv5Dd61gtNy%2BbsOF1r&X-Amz-Signature=0d744db3cbb75613ce10457520720de7ae3c35816dd4b965c2359151261b1037&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OFKHJKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIErzE1EZVfhShueu1iepBQODzCuaBTr2OtLwyzGuZc9zAiAZ57Wf%2FIegnmu1KeOAmnceyWCnNShtD1VsscRZB6aToir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMfmuAJI9t4JMshHPdKtwD4jSzPP4S4yQGa6EOnivyxbpW%2BzwbGokTF9tSU07pOGHGTr0n%2Byi%2FKuI2Aune9IUQwF07TG9sYPg8XYsezjheK%2FHRgvqQwvjt9iMolcPZmKe59ytVZzf1M0YnZPts%2BnWqj6TRwKkhjdnDpcWd0xy1btfcJN%2FPGip7ceqlw2TZCGwWBtwyT896MI8yHy5DU39zL8yUvOkf3e5JIzS%2Fcd04JsN1boEFjjdKZyinmT5wYt4yXlqSchW%2BE7XcKEvuxUz9bczbgVJIP4ykq%2Frpzb7ypIMb%2BZx%2F%2FUwI4lEpx3O%2B4PzJ9ZOeSjfdGXQC%2FUUNtQFeVuPQ2fQwTWAVTKijZOQpbVLDIcExC29Ct2h2XTnJFzWYtXC%2FQyYQZQNjcLDizOz1RY1Qt1LSeTSiJXETihxbh0qPOYCUBAJkudEEZmc%2FHzB0VKlsAaE%2Fo7zTKRMV8eTAOphOlA5VNdNHK7o1GHfN5KHZWUDcUNCecBQyM8bproR50kgaYDSU4zMzVHqLuRWd49DDleVYjc4UEhX7rYxWe8QrdcMxeMxBtYx3UGw6Eg%2BNVf73LCuj8Sq44leOkDHUa0xraaeRuzqMjTJyImWsNdncCiYTRL0fWvmqJ2JxYQRHxfgMGn2991ddrC0wqvOBvQY6pgHAChC44i7FS6fCPid3AU6RxWJLjSnmjDtYVhS96qtNwlXCRONTidctb1Ro2sHukdvAEIfD9q9UoOwdVyDtZZbD3HlpUFnerBgFOI9w2w8wT7nrzqrkTi9xNnqKbWCY05PzFQwry6NcKszU1ZSkAKAPvxJeTS4Jz7ayZZ2dRRdf43DsGTePrcBaGom5MyFb%2FivWMVenT6%2BKWOmv5Dd61gtNy%2BbsOF1r&X-Amz-Signature=8c966d775b7f981f1e335638f6f117481569917732911711317e184a6f2cc5e9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=462361df8540495d775c20fcfacb0c51cbd427a89914a39e8f05ff747b4f7e3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=4c553e822299f9e868d6e162361ca43b5b17165e9e6b87444b5083f45e08d022&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=99f6bfb1c72432128b44206d07cc6863e4d7af8e8768a2d51c79a135a3bb446e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=843db38d57064ad6f41697982e3a10f25b326ca51e51903200090ee1634c63cc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=a813ca9673d5cea53bf2ed05774516ea012b654ae087f4018f4d170c3cc50dc5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WN24WHJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqncDgEJDzaoZC%2FvikRGl84%2BCDYtheHJlsiDNdXGmIqAiAlERcrnPCFTXzAv3uQTAqEH5xHkx7CGuVjyWdqLZzSeir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMTYM14jBjpDGnhVzMKtwDikQBwpsumCMQep4%2BDMK1%2BlvE%2F8ZuZR1X4VA3x1DSoYfavkGvNsyVIBYYMntJo%2F0HpCksGznnpvkXfdsdV5qM0g0pSQeAAwZzOnGHrgFwcdHq%2F1JQPkZTW3ESjl8c5vBiM9452W0E%2FlTSxUr%2FPk%2Fhxeu1i9H%2FYspKGZPcm%2B6WVS%2F%2BKB1fjL4XWpQHYw7BnhjBM3DSV1UTggd9yPZBk54De%2BDtGI9d91psB3f53JVsjX01P5PSJ4XytPNCZDU%2B0LtFEMMjZLbtp6wc23VNoX7JRocQrK6kNX%2F5AxwpJPekCour2xsgk1mRjSU2iqCfRUoRkBVNLC4lz46LUl%2BmPIoILxSBw1RnaA7sJcu4LKmspmsTemJY6733kG5oLZYkYzdtyWela5Hkyry0AeTZeb6HzB1U6PrUvLF0E%2BtBITv5HjYsmmQOjLrY%2FXge5mX9Igg30sAIsTI7Ut9ZXxy39jBQCzW7c5CfphidKqEq263HHp0p2hbD5Bt81%2BqsqA4njpzRpHW8a9NDChoQsada74AeZUCJVxf7hwtuuGi9Liaj6RIWUuD8HNIckGjPltGo%2BnfQbMInUYPgQ9H5z7Lc1sQet0q1eGzz5O7d9idHGDdP4uODe15rk4wVlrFvwiowtvOBvQY6pgFxyo%2B8UW%2FlksIn2TLUntGj00JAMEl5%2F2NUaXGG%2Fz1oCqIs3JLiAbkooFQqYiu0P5u3T4KdKm4ixVe6Rby1LgH63z30%2BfzOaRuDytmNbp6TXGs6f5WkrDNb4lX7h1oeTnAyM9LvjSsy7yoqu%2F8Wfym6VVF0WoTzaxpJrWUIxpXQzDGgduy3AqZasoCG5IeI%2Bp%2B4qIaxIbyFdcaTcGYAsB10HboFolbL&X-Amz-Signature=915146f96cb03dc88e9c8c7e53fe81b69822eeb2b592e6d6d35fdb9085d8cd31&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PTM6ABX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJDy4UbClFTLpFEFWrD2GoOTpDHCq8dpdLFHhzEeXhvAiAPdEC9Uc9R%2F9l%2BczjW9sSgmOWc102EXVlcA%2Fg0HKPlsCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM3e3137AQ8Trk5UxXKtwDVeUhtFL%2FAYJxLNXN5vn7BJYPmRAkn4SK6BS96EhMyHYDPGjL%2BDzOzLhWRjSA9MG6raprscNp%2BW234VIOzy4BazEq9n%2BWngtpblqRyjEheNBIHhFVjodAyqb%2BPyNt22ohEAzVxodX%2B811TaY3GNoTkHZOjvH1AD%2FVUWW61pJBm0%2B1ePXqmzKMdm9QXq2sqjx7BzbdrXiJMXrH5Pa%2BySZ8xTr2VesqgeoddUYNEEPJ52JTgSkZ9YlkFXyunqgdTIzF0flUK6JMyaMabnGSwT3HqHupw7TyF5apP3xg%2B3%2Bc6bMDLQQ7XkrlaSstvZWzTcKM%2BEq2xjzlnlxekpLQB9caf92y4iKyXho4jn2%2FjpJm4ebmmfYQoHbDGovZs%2BivHIXU0SO%2B2Td3boA3yZ%2B12BCJg3U2Zsjbhysh5WAbyO0NqzN6zNq1X39O1arZcnQ3Gh4260YOOCTyZFNaVo%2F4b%2BAuZphd4aEPjGJesbSbij3sfj5slndzNVIJ2S0UEgQ8hZRECy%2F0nw%2B0%2F%2BEZCSL%2BdrhsCZtc4Wz9xY%2FP1q6%2Fa0J0nMiBQShO7Tb4cWFM18CJpfHKuk2gFP7SDp27Zm%2BgVIPJ6fNddb2aWWq8CbJaLTwzsGuXCH7vY7zKxERBboMw2vOBvQY6pgEHteKr694XbAVlVbuoyXGGeNrht4YZxHFGrA8d0UvVWT5L%2F0K8C%2F148Nmi8pN8NUGVP7zfxz%2B5%2B7i0ZpvKDtMH9ZOBw%2F8NDEmEQB72%2B%2BqmDfwDcJBd5vjWrzSAKkf7mb0Ojd3C2HeHKd46zVGbmGY03HMiINP%2FGluFkzaVvRQ8efUYleNyRKDzkdcwhMIE91Vh4uGKRnoVMAz3yZtm00ZZP3THNNnh&X-Amz-Signature=61250f7d57d125ccc4cc2d507a5aee0aeccc88c8046563768f1af97c2076da4c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PTM6ABX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJDy4UbClFTLpFEFWrD2GoOTpDHCq8dpdLFHhzEeXhvAiAPdEC9Uc9R%2F9l%2BczjW9sSgmOWc102EXVlcA%2Fg0HKPlsCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM3e3137AQ8Trk5UxXKtwDVeUhtFL%2FAYJxLNXN5vn7BJYPmRAkn4SK6BS96EhMyHYDPGjL%2BDzOzLhWRjSA9MG6raprscNp%2BW234VIOzy4BazEq9n%2BWngtpblqRyjEheNBIHhFVjodAyqb%2BPyNt22ohEAzVxodX%2B811TaY3GNoTkHZOjvH1AD%2FVUWW61pJBm0%2B1ePXqmzKMdm9QXq2sqjx7BzbdrXiJMXrH5Pa%2BySZ8xTr2VesqgeoddUYNEEPJ52JTgSkZ9YlkFXyunqgdTIzF0flUK6JMyaMabnGSwT3HqHupw7TyF5apP3xg%2B3%2Bc6bMDLQQ7XkrlaSstvZWzTcKM%2BEq2xjzlnlxekpLQB9caf92y4iKyXho4jn2%2FjpJm4ebmmfYQoHbDGovZs%2BivHIXU0SO%2B2Td3boA3yZ%2B12BCJg3U2Zsjbhysh5WAbyO0NqzN6zNq1X39O1arZcnQ3Gh4260YOOCTyZFNaVo%2F4b%2BAuZphd4aEPjGJesbSbij3sfj5slndzNVIJ2S0UEgQ8hZRECy%2F0nw%2B0%2F%2BEZCSL%2BdrhsCZtc4Wz9xY%2FP1q6%2Fa0J0nMiBQShO7Tb4cWFM18CJpfHKuk2gFP7SDp27Zm%2BgVIPJ6fNddb2aWWq8CbJaLTwzsGuXCH7vY7zKxERBboMw2vOBvQY6pgEHteKr694XbAVlVbuoyXGGeNrht4YZxHFGrA8d0UvVWT5L%2F0K8C%2F148Nmi8pN8NUGVP7zfxz%2B5%2B7i0ZpvKDtMH9ZOBw%2F8NDEmEQB72%2B%2BqmDfwDcJBd5vjWrzSAKkf7mb0Ojd3C2HeHKd46zVGbmGY03HMiINP%2FGluFkzaVvRQ8efUYleNyRKDzkdcwhMIE91Vh4uGKRnoVMAz3yZtm00ZZP3THNNnh&X-Amz-Signature=6ed9a7f960ea192d53b207466b0be973b43e4ca697a75a66691444854ad4a0eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEH4NC2P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgYYS6nnty24IpaIlM21ueBYFjvFWIgDLLS%2Bt3tVR5JwIgGUlRO1dZIw1gLYj7YCOYrxGOzxw7vY5Z0UgNPt5whtoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDNJWWtLb%2F92dSj01iCrcAz8yyOtUQg74EOfZiViLtoJmil8XFHcph5%2F%2Bz0bKaJQBdKeuZeyqNcevDwNVykUbLUdH6p69mjAT3WZvEToU5KvHxtLlGIbb%2B%2BAuUBUalbAnxzML2vS4It7KkmZ%2FEygohou6sjhVMlZDrHW%2Bj26vpGFdeV44W%2BO%2FGR3ylEcfYrMAMTe9fpP5PnL27azJ7x8EvXXqrc61Hd368YgImMtmH1%2B%2Fo3OVn3pfp9FVKm0NMURuRcg01%2BxTnCTajoYyx88dBxxgZqYxwGzVS05Z%2FFM7jc7vkbry2Y4nq2L772zohlhc6sbgiFgLZSr9gJPsZKIRuRobXKiTM7c85n8JFIj%2FRN1L9v%2BFKPwD%2BZnMGToTtEijI6%2FG9r3nSV4TDeJs9I9ydBAmEMLeUgoN28ZXlWlEX6uj5%2FGDiwbFJp6HB8Se2ocfAcjNe7F0UN4ri3uEm5LY4iBvk4ToT6sLHAVZ5G3tCdhmOs4EE4HnP%2FO59fF5plr82RXZZD7dOp52Nc2aFmz%2Bcvbk%2FWzHzxIActu%2FJ%2F%2BU3VSKFgEYw6B81EFdKFPDJ1dGyMkqml3bL7uq5CCfZl9aXd71iBzAWlL8Qz9m5SzAzjbPm9iJbRZdbxrq7Rs79x%2BgamwugUZ2FMx0GeyIMJn0gb0GOqUBi71Xs6ps0fe980W51EBQYI4ulKb%2F8k2DaDUvuE1j4jPPWJgst2kxujs8U3eUo6coRz68wpEJOZe9XGL8Y0xpMgs%2BOJK%2BB%2B%2FxhJc5Qk7e%2Fqy2%2F27pjeTz9ose%2FBfu5EbrPZmYcyIc1%2BVq0OVuAKp2Mmu%2F9tL59wPWcYMyheXxqlEUVj3qBHKcmbMymKaKNkhpxEVoTczX3MqKZYGBGX562Hiol0We&X-Amz-Signature=035198ed9299e98d33ce03295cc7424cd23f2795b46894c2c1018e7596c5e58a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642APEOAC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFItIQ7t9%2FUIyLLg7vfahGhavgqVbcO6589asbDNtQEfAiEA0mZk8xohN1816XpcHKNn5r9KNiof2F6aoLKvbKmfJIcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEdrEOtfhfVTUC32RyrcA0HN4%2BxsAdP11RjXPl71alAg2Wz%2FQxUrbrX5N3dbkM6HcsgI5auvhVKfDuC46TjHLWu8RHUgSppezhic6sLPLNirVY3d4qG0oJVigiAQSaoqwzUyu3ffcaI3k%2BqEbxifHNpYpID1f5twinrp8FM7zefElUSOLvKnl6bSnL%2BIOpLVWCYWIJeU6XqhhwtS0Y9jcL4PJ0bRnl2ErRhlF6FF9oNNb3VNFuntsnj2MzTz4qpHGm4byqTsg2EGwSaqxpLYXpAjtkW3MbFclv0wW0CFgLi589drLJMLdl7pRJtFsY332f1O1sAMHZgne35bAcPLm4mD8%2BKgWuEiy5dpVoigceS1GB4G%2B7g1bzm2XWGSbxxOSXntyx8eWhbaQz7Hojz65IHAmiwf2TLype7CzOlBNihVPHrY5NYkDe3C28u%2Be6rAy4Gt8gx9F4DiSyLfwwZapyIkbu5cN3XGgpZQaXjUu211RppMyViP6SiIsPnAl6ifiH3qbWG02anxawA4f5zYLGKTK8Yd09p8TWs13ZTG290MRHjE8gy0TkVR%2B1nZMGTFB8D9jfGr4MiVr1VDL%2FMhv89DYziucIJnmgpCEgpOsbN7YiLFmbX3PpCHtiWwbqYCwTb7etdnsUWcqw8xMIr0gb0GOqUBeZbyGSk0Z6AKD%2BsVGIcKkxxknQvNOFdE4DTXU8oUH5p0RS3jnffGE%2BZS4VCOrHsv6mqftJmeNdC2EHiyettKCXFzHyQRv4VDMfXw7rsBCp21%2B4FtyzMUMB%2Fci1ScP6qtWJOlioTlyZo23EneG6gwC9WObuS9VkkkcX1a%2B3su%2B3tW6gLguR5AMxQj3T6%2BgcEdb0%2FPGy3Iu8P3X4vbudNWuZ8UJZdq&X-Amz-Signature=8bbe7e243db6fbc264deb7d0531fb811e024b7fa4639446ac7661988d8ba5e5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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