

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=df1aeb1da4c6b6b7a6ee210112bf3847cd1d4d0d5a48d00b2dfe5d23303e1e80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=60b1bf3bcbad2597122ef6e2a9918208efbf57843c734925cf418082a2d6118a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=8a9d84260f8592e773ce17fca9c80482d4da0f1dbcbe868894d89cd15fb71f60&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=9f9996c148ff4a97cb27a19d4f8c661da50c7569f2ed58cad6e4c6387f529413&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=818419aeae83df47be8118c8e4f8ef4d5da3e64fb2f29730e48b21554aaf1696&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=e5a079ef4ce42255a1a87ed91af4708b4ecfe9af1ffbe44b11e63f12dbcddf68&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=f48b40ad0bff9f87a28f0ebb7fdab35c3a0b9d8a369f8cea367f3813e231b1b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=8094403dc5aa48481339b4f977d5705cc364b736b6944f2a1651d22e86395818&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=2a528cb4b83a85085e51a219bd58eb8ba3cd773e5040a7d434a47467e3666b7c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW3RHG4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHculYjxdUVWMSqdUGTZzuNSfYPwQfxkGB98%2FrGwfLEAIgavRYB4TNnOYIa4sF7ewNikOFFt33GANOsW0vddzuYTQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBghv3J6bqWPSRAUIyrcA%2FtlmO5%2B339LoWBSaYZQvY%2BfQI8vmzjEbt9KgZ7Idsa%2F6NU8AytH6IcmXqfdemkjvwg05XMm7%2FiFByWa%2FLu8wvfJdRkEgl7ZHTkvM59BO9wVW%2F3%2BXhpbx%2FluCMTlwhpUSmCptWf9GgMWx%2FtMmsRz53uEReuqdP%2BEAWM6W35BKbAdv0fLSy%2F6JBpu8%2FGhqMCe4mCZfkpZq4voK4Sqa6d%2BhZ4c753zoeD7iAU0sKO0s%2BOV4SAcaESfzIa76Ek7xxPpbdahQPLiLtIUAsgK3Pf1Tczq1PV3v%2FfhNnT8NC%2FbtD8ISnvIpkvsYxo%2FyYWC8P%2FJYlTagQnBYhCGRB9LbUfUDatDF0hNgTTdrV5m%2BJM114wKCzIhC1OTCshWXeFR6FCEe38KCE6GmPlVRC5J0kz0tTYQ%2BUjzASoOhxVhPn2v6ssf2HI4nSgAECBzjth4hcT9vRKR56%2B%2B086Sjx5U1GkfZyxkeeBSS14Df30HbS%2FnoJoX8n7RLr2w5o16HldqFdVtrX4VG2MvI4a7ggP9%2BPLjEA498k5wZENSB6sSnUH%2FARKZPcmjPBfJIt2Sg1KVfMRp1ax5WsL5YYrhFRWZ%2BuKCtlqBz35y2tzSjZ7la%2BcmymyT69hUQ2Uc0FceFAFoMITh%2B7wGOqUBc5lP2shbr7SPy9qM3tEp5EB8y2kt%2BM2gz7PCYDv7VJF6c%2FI89s3hJDjoESo%2FQCBnWjW0XmpR5U58cWtLM%2F4BuZzcIzdbwAYrHGLq1Zp%2B4UnCUtlOoyhCdrdo5RqON645UfbZkjk%2FN4TuFjcouYyriJbGDmmBE5OXdRiFmnvKyq6zdXqonrUeaxfbnasUIuJvbp1m1wcAWsNBwYdGmDUfrLaDeFER&X-Amz-Signature=47772a43eb750c9b9675228c351218e3761a91b02a571a172990b6d1f308f7e0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW3RHG4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHculYjxdUVWMSqdUGTZzuNSfYPwQfxkGB98%2FrGwfLEAIgavRYB4TNnOYIa4sF7ewNikOFFt33GANOsW0vddzuYTQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBghv3J6bqWPSRAUIyrcA%2FtlmO5%2B339LoWBSaYZQvY%2BfQI8vmzjEbt9KgZ7Idsa%2F6NU8AytH6IcmXqfdemkjvwg05XMm7%2FiFByWa%2FLu8wvfJdRkEgl7ZHTkvM59BO9wVW%2F3%2BXhpbx%2FluCMTlwhpUSmCptWf9GgMWx%2FtMmsRz53uEReuqdP%2BEAWM6W35BKbAdv0fLSy%2F6JBpu8%2FGhqMCe4mCZfkpZq4voK4Sqa6d%2BhZ4c753zoeD7iAU0sKO0s%2BOV4SAcaESfzIa76Ek7xxPpbdahQPLiLtIUAsgK3Pf1Tczq1PV3v%2FfhNnT8NC%2FbtD8ISnvIpkvsYxo%2FyYWC8P%2FJYlTagQnBYhCGRB9LbUfUDatDF0hNgTTdrV5m%2BJM114wKCzIhC1OTCshWXeFR6FCEe38KCE6GmPlVRC5J0kz0tTYQ%2BUjzASoOhxVhPn2v6ssf2HI4nSgAECBzjth4hcT9vRKR56%2B%2B086Sjx5U1GkfZyxkeeBSS14Df30HbS%2FnoJoX8n7RLr2w5o16HldqFdVtrX4VG2MvI4a7ggP9%2BPLjEA498k5wZENSB6sSnUH%2FARKZPcmjPBfJIt2Sg1KVfMRp1ax5WsL5YYrhFRWZ%2BuKCtlqBz35y2tzSjZ7la%2BcmymyT69hUQ2Uc0FceFAFoMITh%2B7wGOqUBc5lP2shbr7SPy9qM3tEp5EB8y2kt%2BM2gz7PCYDv7VJF6c%2FI89s3hJDjoESo%2FQCBnWjW0XmpR5U58cWtLM%2F4BuZzcIzdbwAYrHGLq1Zp%2B4UnCUtlOoyhCdrdo5RqON645UfbZkjk%2FN4TuFjcouYyriJbGDmmBE5OXdRiFmnvKyq6zdXqonrUeaxfbnasUIuJvbp1m1wcAWsNBwYdGmDUfrLaDeFER&X-Amz-Signature=99883ecc49e570ea5d531b1d70509dbce4a431dcb6932bd29305e28a6b39cee1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW3RHG4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHculYjxdUVWMSqdUGTZzuNSfYPwQfxkGB98%2FrGwfLEAIgavRYB4TNnOYIa4sF7ewNikOFFt33GANOsW0vddzuYTQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBghv3J6bqWPSRAUIyrcA%2FtlmO5%2B339LoWBSaYZQvY%2BfQI8vmzjEbt9KgZ7Idsa%2F6NU8AytH6IcmXqfdemkjvwg05XMm7%2FiFByWa%2FLu8wvfJdRkEgl7ZHTkvM59BO9wVW%2F3%2BXhpbx%2FluCMTlwhpUSmCptWf9GgMWx%2FtMmsRz53uEReuqdP%2BEAWM6W35BKbAdv0fLSy%2F6JBpu8%2FGhqMCe4mCZfkpZq4voK4Sqa6d%2BhZ4c753zoeD7iAU0sKO0s%2BOV4SAcaESfzIa76Ek7xxPpbdahQPLiLtIUAsgK3Pf1Tczq1PV3v%2FfhNnT8NC%2FbtD8ISnvIpkvsYxo%2FyYWC8P%2FJYlTagQnBYhCGRB9LbUfUDatDF0hNgTTdrV5m%2BJM114wKCzIhC1OTCshWXeFR6FCEe38KCE6GmPlVRC5J0kz0tTYQ%2BUjzASoOhxVhPn2v6ssf2HI4nSgAECBzjth4hcT9vRKR56%2B%2B086Sjx5U1GkfZyxkeeBSS14Df30HbS%2FnoJoX8n7RLr2w5o16HldqFdVtrX4VG2MvI4a7ggP9%2BPLjEA498k5wZENSB6sSnUH%2FARKZPcmjPBfJIt2Sg1KVfMRp1ax5WsL5YYrhFRWZ%2BuKCtlqBz35y2tzSjZ7la%2BcmymyT69hUQ2Uc0FceFAFoMITh%2B7wGOqUBc5lP2shbr7SPy9qM3tEp5EB8y2kt%2BM2gz7PCYDv7VJF6c%2FI89s3hJDjoESo%2FQCBnWjW0XmpR5U58cWtLM%2F4BuZzcIzdbwAYrHGLq1Zp%2B4UnCUtlOoyhCdrdo5RqON645UfbZkjk%2FN4TuFjcouYyriJbGDmmBE5OXdRiFmnvKyq6zdXqonrUeaxfbnasUIuJvbp1m1wcAWsNBwYdGmDUfrLaDeFER&X-Amz-Signature=ab492697af5d02b6bba51035e35908b0d0cbaefb3547b1d21c3fd6f5999dcde8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=195e3d6a7defa7cf3182ae17b2e2f93bdb68f56b28e1e581be1c8fd52f5a49b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=3cc33838646aac1d8892d92fbe5980fd1eaf6e2e716c91a9ca409068218612fc&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=5103e4942b6d7505f4acf9698b98ef896bba278575f4bfa62ffff6081924431b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=8d3880843f231e342257b56e7ae04e49c268c4d5ffaef9da747394da3fbc678e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=8cf1344bdcf511f551aec60dd22c51f55dca170feb4fc966d8593481e7ff5505&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KH3UVBA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdNhQWLLSUT6BhoVKvaKLMGQtxl%2B6TD9adA1zFb%2BhRQAIhAIR9WNVcjtsjxZh9z2opP0BBmLPwWylOWXoGxTHwujUDKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxSSxsxTtZGHIIZsEq3AOEUYWN8Q4cCKX4hAgWlN%2B18KyGomzmHUzocd%2BkJ5IUijoZVanNOfQAlYRNIvqRHyHyycK%2BW%2BYeCHZoSWPyndh65L5IjW51%2BPxxiuReMKa2iZ3TwDpPjsB6IxTMMrET1BYV6bv7%2BqfPFfKsJdBladtB7LRHaUVr6ZyJpvV5nqWZ8Zmim50oJOuc2ZGQ20aq7IgxhLQdxHEyX6ximQ%2FMzbrJMK19D10YGmD5iqn7hxsncRyieQ4eAPnD%2FJrl8JxOi7KVarQfOXsrs%2F5wmRsN4eCWtK4szTSOKmJkxv4M8Y%2Fwoodm6X1gtWc4IFLH34S4sVwg%2Ffpjimj39MlSVwWXc6u6M3JwxwVDgThPPqwzC3D%2Bvn9Ka3S2%2BZXQidoCpkJXxvzEakd4Z3PjqB%2B7xj9ZK497CVKrcTxoCZ2Y%2Bf9N5E25UWxdwOYL1WXB52tywA%2BBqhhN0pjWM%2FuaDN%2Bst%2FS66K0YYJEU43HORRYGDqpjE2B0gfvQNwAFR%2B74mbrnbGXy0jj8yT9zfEMtyczf6E1qw5KSKnDFPH7EQ2U1%2FYZdldiR4WAW7F%2BRw0GF32Z7TSGGkl3bZJy9YKymo37cHD39LJv1gozFFvU3xPo0orcClbi8GfP%2FYzLH%2BEh7VsApbDDgm%2Fy8BjqkAbj9uuln8fmATZ4ED34H3uzahR8VHuWWb3vATmhFYiE4mSmPn5HdJefQIDHCBHJ1Jw6kYB0Yfx%2F%2Brhi8bhFagzNXuM%2FXzVhly7H8S4fhi3gGnT1jflK%2FBZi4l4beJ9IIfOBeTRE5VwyMwuFiwdcQCzt%2F65QnSkXOYgyB2mVazt7Rv4ZYQLIa216ccqNDu%2FjRyH6sB3mOLPIOxd0wYflTRNO%2F2TG8&X-Amz-Signature=85ce72361de36d30c6e673081e5077fafe8d0ef584a8ea63e0cb1b95f95c6415&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YOZJXDU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzsYqET9Cx5xEdpIln9UdgOi9I9LGqtMrGkkKR4TiHcAIhAMO%2BX7PAsblQw2XIRNvEB8tu8D4O%2B9HnLHU796OO4%2FC%2FKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhBJy%2BUZhKUOjrjAoq3AOSSMDt79ke0GlYSp6g%2BFXar%2F9wYU0enl5CjG%2F8etZ6tSota0MMXisVVlLAIMCdHnp7VraME5aiPXo1M91JB15DbECzKSTzIgUdn80JBBcHTpUSc8xER8TcI9mECbjvJKyVY5w65oZNXBRsqVhk2HRIGKm3YqtY2YjzufgzeBomdIoqyuviAkOL7BTxpooZv2Ypi36rOqcDszVzs8kXIaoZcBY7h8sqlVHuT9CQGdpWS4Q%2F%2F2O3Z6XpU6agF7BCi%2BPhVcq4G9jwCpoZHnNlmmrHdDjrSamaLYZk53oUKdJjeqjFPczRCTRhU3pE2%2BfDqUKiTlRI5hkscUy5HRB8%2FCb3foNDn07wEpuhEAQuC9MoV%2FvPJNzHw4Re7geDS9mvSl3abr3ZWx5h3Odxr1i4YXxHlh8ae7TMQ4QacSISrbXePobA9ziPmmVm32QJ%2BZ9vjdQjJlSQ%2BOUN9qfW2tjGM8YVdeQ3ZS0MUmV830pRVOgHxATZ1YSE5lg6BsCb4iCBkexfO2bvmmGiFqlaJw65MmKuh1INJTkqtFFvbZRWOkZZRIaxC2YRm0TouOzcQhwhzgE8pfyMsQbcYfDIGVFyw3e1G1kZVxywLOQ1x%2F27Lgy0%2BJO176wiBvc1JSCnfjDam%2Fy8BjqkAXnzhz%2Fwhky4%2FjpfLffUoGuXlCcs78NVGl1HgkG6bMoreKeQ2aWOLSP8alkSX9Js4zVS5Dulbyw%2FH5zdYRBrHY1Zz%2BYxtYyiRsjnp19hEWnjCe%2BRiEe7f3iGwxw46pxH6gJ3F8I6wCM%2BJUCVa25i3twzSlf5Tiqj5DIdRRXMu3O79i7FJkqe00mBAlZkqqezCqR3TWyvzjoXnWqluxehyspgkzX7&X-Amz-Signature=e33e61809aa561102e4067630bdeb7c0b86d77e32816c8d8d1d8e87dae290b37&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YOZJXDU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzsYqET9Cx5xEdpIln9UdgOi9I9LGqtMrGkkKR4TiHcAIhAMO%2BX7PAsblQw2XIRNvEB8tu8D4O%2B9HnLHU796OO4%2FC%2FKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhBJy%2BUZhKUOjrjAoq3AOSSMDt79ke0GlYSp6g%2BFXar%2F9wYU0enl5CjG%2F8etZ6tSota0MMXisVVlLAIMCdHnp7VraME5aiPXo1M91JB15DbECzKSTzIgUdn80JBBcHTpUSc8xER8TcI9mECbjvJKyVY5w65oZNXBRsqVhk2HRIGKm3YqtY2YjzufgzeBomdIoqyuviAkOL7BTxpooZv2Ypi36rOqcDszVzs8kXIaoZcBY7h8sqlVHuT9CQGdpWS4Q%2F%2F2O3Z6XpU6agF7BCi%2BPhVcq4G9jwCpoZHnNlmmrHdDjrSamaLYZk53oUKdJjeqjFPczRCTRhU3pE2%2BfDqUKiTlRI5hkscUy5HRB8%2FCb3foNDn07wEpuhEAQuC9MoV%2FvPJNzHw4Re7geDS9mvSl3abr3ZWx5h3Odxr1i4YXxHlh8ae7TMQ4QacSISrbXePobA9ziPmmVm32QJ%2BZ9vjdQjJlSQ%2BOUN9qfW2tjGM8YVdeQ3ZS0MUmV830pRVOgHxATZ1YSE5lg6BsCb4iCBkexfO2bvmmGiFqlaJw65MmKuh1INJTkqtFFvbZRWOkZZRIaxC2YRm0TouOzcQhwhzgE8pfyMsQbcYfDIGVFyw3e1G1kZVxywLOQ1x%2F27Lgy0%2BJO176wiBvc1JSCnfjDam%2Fy8BjqkAXnzhz%2Fwhky4%2FjpfLffUoGuXlCcs78NVGl1HgkG6bMoreKeQ2aWOLSP8alkSX9Js4zVS5Dulbyw%2FH5zdYRBrHY1Zz%2BYxtYyiRsjnp19hEWnjCe%2BRiEe7f3iGwxw46pxH6gJ3F8I6wCM%2BJUCVa25i3twzSlf5Tiqj5DIdRRXMu3O79i7FJkqe00mBAlZkqqezCqR3TWyvzjoXnWqluxehyspgkzX7&X-Amz-Signature=0d4bae6a79c91b4bf054d7bf1986a1dd11dd6b9f179f012f8823686588eb3334&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5K4G4VM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpqgHlC6Ry06WTLXWO7HcPotd%2F9F5kDpuv87xE6TY3TAiA0wPIFB1zZHPEp1q7Heg9HEyzBO381onT0h7YMUZx0TCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3JiUH3gwjTHOyR1QKtwDh%2BsnqfC2GWJbZVAU88fpL9dvjIPQ6BYleeWO3PHUZhhWXR1gvO9wt9IQZwtIVlJBLvySd%2FrOMsY%2F%2BhxZXjPHNLetYt9zV1XAlFE%2F92XLOr9w8la1dCplFk1T9%2FCuPfHOPrlV%2BqB9GGo7YscP2F%2BNgllYaHfcnzMY2lfo1Jbqz0fo2sy7WmKPedxBR0s20kqwU%2F774XGRQ1byh0oTAgGmBdkBLnvHuUmCL%2FKj2V17xWriszzSZAd58tUW6vEAVd5%2Bi8G9DeHCmf8E7VQpmnCLdPCQF%2F3j3thOZBNWBhFj1SB05K%2BSmuiW9zSbNPI5q0S4s0XJ%2FWC1fU1BtrfQhE3dTCE8pOO%2B%2FX5SYEGVsy8mun%2FT2Zft2hyOFGOUt7GRVjbVP1rNKj4EDY7WQDiVF%2F1hqxicONJFHmrBIa6UmhT%2BKk7RkNGQ5AGlQySBrbWXNIhsRzf23XmVC5rfBSTL5c%2BNMAdxzEB77uCGKjbndBtD7Jz5HQ5uB53qnyRXZ%2B7WzuZO%2FugjOe7DUktaE4WhhIeyqAfcrphrQcIo4bHzU443I5ss2vIWPPuR4hmxmgtaDhUYXWn8SMAZ2M1RJoUyNWzHWKZL1yhNG9dcvdPb6C2WtpsDw8z47OMOHZrRsZYw25v8vAY6pgE18imUHQPFTGohzHvQQ4QncEBFATh66gGf2ZLX5YiP4l6rpGVtd1gCApohs9pVLKIbyl4WyZgvxwgE6pGfdetWMmt9nYCWVUm8D9%2BVUk6hwvxtX3Wj8Ywhcn3r3bqyO2mL3xY6IDDvf2TZSpmRiwUbAk%2BsxoApWTk59ZO658baGQc4rhECqtWiLbURAN90LTRfHrsVIxoQfWzDuozZ8svFrIJ9yOAx&X-Amz-Signature=f3d798b36d16704ac779d09d6ea26a9b383ebecc14f81c3dd965fa8005417182&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJWO4EY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoGLQH%2BFIXszC%2BCo%2F0lEZnDybSqp%2BdTyL5dAP8xcheLwIhANA3hk%2Bu7pjPrE8F1RcLDNF25Vs1L9dkWBuNN2at57pcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyehz1VdTLP6fa7cxwq3ANTp14Y2PxJoCmtk1gA4uBfqhqWDgMCtd%2FBlOzIQXhauwe2SktcRX9v2X99gZDbP2I9HBxV1MhMqWP14YMFQV1t6hQo8b6ffuaoGICK906c%2B%2BAFxSKLj%2FqwBoZ3lGWRy2PFPtu9ndEDvweROieTJkqw22Dctsn%2Bh1g4QwSxq6sRiCcqw2D35z3oDkglghRgfJmVO9dZD3Wl%2F4Rdn3FUNAoqU%2FLzHWgIRQlPWuheUEAOLydRsii%2FOF5o1qA6vGj14fpdWgTFjUxjb85nLJ9MkA5%2F8n9HrdrXTuB3hGeewvrD8qbpHeLS60BCcMJC31pqNB%2BA1xjXTA4G6TRHHfn%2BIJMxfagn9LTqFCWpdAT3jexGFiGejxUPjXR5wneHSyZMRosvB9l5642ZDT78dU6RfgOkRu2O%2FYZmeai5P0v%2BxUlaAIf3dVQgZ82Kv5ju6Y1O5HJjy6cbzLdvZve02GQ9MTKAtPQFXFNcLLug0cj3L3alBNfjRRKlvEEQtc4Yl4vm2cdEVNAfCAcM6gXf2hSrjnMNfZv6%2BjE9kgE%2Flw7qe3ke0guPD2vKlx9mgFgxILxrQCMX8Xh46EHHVaNiFvlPc1Xp5Minpe0XnNqbXFxOYPm0%2B69wU1nYPQ6ba5iiITD4m%2Fy8BjqkAQ6O%2FF3FfxyCqmkwed4Kp7aN2qf7li%2FN%2F8VmF3ITqGI6Soa%2FNBR91UVquHO4Zj6rSL16dv3FQXY9XpsG4OBg2BRSJMeaHl7UG0eR%2F0bFh202p4fSGeBMbkChAuk8M2KuSCAQeaSIh05iiq4Nxgby%2FqYC%2FEkAzh%2Fgo%2B5T9tmOFRESctDnS7KFQlJRGO7adTm4UUYozRCArC7Kng%2FNg4jIOYAeZ2ZU&X-Amz-Signature=a2417e952046b4c71cc67ee6f5aa0d012340988e55f517419701b0e132878a64&X-Amz-SignedHeaders=host&x-id=GetObject)
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