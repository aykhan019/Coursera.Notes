

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=4020722e45928b946ec789355f6c18a4f277a6dbc67ee090a30d2fe865f80786&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=a5a38597ede32502472930c94ce4fdaea731f4855657e65d9f407f38f00f3978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=f3f44e02f0503d9d6dde502558a6724fbf7c5c0d672c087949426118a6c36b73&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=91e293748abf7eec0647c08673dc6360b6c69bc3a50cf5e1ef980c7381bf87b0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=3b5c26b01fc39e184d51ea5a5e13da84002fce5f19660c4893a8a6669a8eca36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=ed82917885999c6f1a0f9e27def505a749602a159f0708a3c63d1ee478fb36c1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=f7b9a64b29c3fa2f0dc1cee6fc95766746b0031b66f9efbc0a8be8b68c423446&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=dea6789528876d80a51cc5d76dcd343073a7f68cb0f6dad35d9cbd133bb57540&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=006f04483d8c42ad5391808f544c58153c13d7951a885d54c615d54685027916&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ZUGSD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQhXJaIfTgEj4Cf1EIcafU0nZt3sX6yVaIsZi3LxUXkwIhAPTg2HeL%2BMnhRXbBEAXs%2B9Lxd4M%2BMqVyYMtNzxbGTsYYKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXPVw2xEFZpxWEu0Aq3AMRyGe5WBeBmDNfpoXtKGdYz7DtdjGgQBXBEtXo7YjTdTMStdSE2DtnLzzuGgEjPs%2BV1HKqmag4wgWL%2BnQsVqdofyLEU6o%2Bl3WhEkLn9tIbD7EfPSKb1i5lE%2F85Wguj%2B1xtBO6UWBiX4GXxIHFnsucBuxBZ%2FtDPiOfZXqYwVg1PERr4ujxE3CfMT%2Byn1%2FdX2BLVrNKHJDWbLr3qVq9Hh3rWu1SVEcn0P7ceIelUmWrpo5fGi9Jf4PRNT8YVnEC58FODx95JuWmkhQe5ZKoJevUw%2Ft64FyNY%2F%2BsqY1Ea0l8mMLkC%2FsrEs%2FSTkTR5wU%2BafV3kfpUCzj8EieCbJzVtQhAtvuWvvUvj2gPWHmZ9XOqYxxKpRIv7mzKKKkVAjY%2BeTI%2FQaaw6Sn1RFC5JIxV8EAumC7xzgFukJKw64zqRPsmVK4YGTAU0Yl42sOV0QTAm7FfHIhYmZI1ZDldUoqhqPBTh64kzxfMHVwg3A2PU7p3cyyUqKOmkq6kQJDXgL3qGIoGsaM%2F3t4jug81EbwyH9lwkgPiiAL1am9w%2BkqlCaCm1LOsB%2B4dtrSjlCBSpLhekVGG8P%2FwL0jAIyzlS1ELpdcZ5N%2FZTKjm8alT3um6ohcff%2BSHKQkNGxN6ejGidQzDS3v68BjqkAQmnpvTCHUAp5ek1oWe%2FkvcBh2DGoQGNsrI3dPpyWN4ZrfeGvk0hGboisMKW0hqfoJlfWc2b4zQzZxBWvoY0R2U8f78mS2tkYHEikNnspeIGdpyFkatSvn6SnFn7Q%2Ftj0AlRWFUBnDLHw5JRYPy2cOkh2OhT4RE%2FAqN40Ef1YnpQaY9pWDUnKa5Q5nh0Aa0nDrFzSQOSPTRIhIRY5uqxQUwVX60E&X-Amz-Signature=c1f21b11da039927ff177ad95bdc2dda7448dfacfd5e7852d6f54a73c8e111f9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ZUGSD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQhXJaIfTgEj4Cf1EIcafU0nZt3sX6yVaIsZi3LxUXkwIhAPTg2HeL%2BMnhRXbBEAXs%2B9Lxd4M%2BMqVyYMtNzxbGTsYYKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXPVw2xEFZpxWEu0Aq3AMRyGe5WBeBmDNfpoXtKGdYz7DtdjGgQBXBEtXo7YjTdTMStdSE2DtnLzzuGgEjPs%2BV1HKqmag4wgWL%2BnQsVqdofyLEU6o%2Bl3WhEkLn9tIbD7EfPSKb1i5lE%2F85Wguj%2B1xtBO6UWBiX4GXxIHFnsucBuxBZ%2FtDPiOfZXqYwVg1PERr4ujxE3CfMT%2Byn1%2FdX2BLVrNKHJDWbLr3qVq9Hh3rWu1SVEcn0P7ceIelUmWrpo5fGi9Jf4PRNT8YVnEC58FODx95JuWmkhQe5ZKoJevUw%2Ft64FyNY%2F%2BsqY1Ea0l8mMLkC%2FsrEs%2FSTkTR5wU%2BafV3kfpUCzj8EieCbJzVtQhAtvuWvvUvj2gPWHmZ9XOqYxxKpRIv7mzKKKkVAjY%2BeTI%2FQaaw6Sn1RFC5JIxV8EAumC7xzgFukJKw64zqRPsmVK4YGTAU0Yl42sOV0QTAm7FfHIhYmZI1ZDldUoqhqPBTh64kzxfMHVwg3A2PU7p3cyyUqKOmkq6kQJDXgL3qGIoGsaM%2F3t4jug81EbwyH9lwkgPiiAL1am9w%2BkqlCaCm1LOsB%2B4dtrSjlCBSpLhekVGG8P%2FwL0jAIyzlS1ELpdcZ5N%2FZTKjm8alT3um6ohcff%2BSHKQkNGxN6ejGidQzDS3v68BjqkAQmnpvTCHUAp5ek1oWe%2FkvcBh2DGoQGNsrI3dPpyWN4ZrfeGvk0hGboisMKW0hqfoJlfWc2b4zQzZxBWvoY0R2U8f78mS2tkYHEikNnspeIGdpyFkatSvn6SnFn7Q%2Ftj0AlRWFUBnDLHw5JRYPy2cOkh2OhT4RE%2FAqN40Ef1YnpQaY9pWDUnKa5Q5nh0Aa0nDrFzSQOSPTRIhIRY5uqxQUwVX60E&X-Amz-Signature=b4f2e907aa82d05f25c80cdd81f21ca5b2affd902b83180ba8488969db235f14&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ZUGSD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQhXJaIfTgEj4Cf1EIcafU0nZt3sX6yVaIsZi3LxUXkwIhAPTg2HeL%2BMnhRXbBEAXs%2B9Lxd4M%2BMqVyYMtNzxbGTsYYKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXPVw2xEFZpxWEu0Aq3AMRyGe5WBeBmDNfpoXtKGdYz7DtdjGgQBXBEtXo7YjTdTMStdSE2DtnLzzuGgEjPs%2BV1HKqmag4wgWL%2BnQsVqdofyLEU6o%2Bl3WhEkLn9tIbD7EfPSKb1i5lE%2F85Wguj%2B1xtBO6UWBiX4GXxIHFnsucBuxBZ%2FtDPiOfZXqYwVg1PERr4ujxE3CfMT%2Byn1%2FdX2BLVrNKHJDWbLr3qVq9Hh3rWu1SVEcn0P7ceIelUmWrpo5fGi9Jf4PRNT8YVnEC58FODx95JuWmkhQe5ZKoJevUw%2Ft64FyNY%2F%2BsqY1Ea0l8mMLkC%2FsrEs%2FSTkTR5wU%2BafV3kfpUCzj8EieCbJzVtQhAtvuWvvUvj2gPWHmZ9XOqYxxKpRIv7mzKKKkVAjY%2BeTI%2FQaaw6Sn1RFC5JIxV8EAumC7xzgFukJKw64zqRPsmVK4YGTAU0Yl42sOV0QTAm7FfHIhYmZI1ZDldUoqhqPBTh64kzxfMHVwg3A2PU7p3cyyUqKOmkq6kQJDXgL3qGIoGsaM%2F3t4jug81EbwyH9lwkgPiiAL1am9w%2BkqlCaCm1LOsB%2B4dtrSjlCBSpLhekVGG8P%2FwL0jAIyzlS1ELpdcZ5N%2FZTKjm8alT3um6ohcff%2BSHKQkNGxN6ejGidQzDS3v68BjqkAQmnpvTCHUAp5ek1oWe%2FkvcBh2DGoQGNsrI3dPpyWN4ZrfeGvk0hGboisMKW0hqfoJlfWc2b4zQzZxBWvoY0R2U8f78mS2tkYHEikNnspeIGdpyFkatSvn6SnFn7Q%2Ftj0AlRWFUBnDLHw5JRYPy2cOkh2OhT4RE%2FAqN40Ef1YnpQaY9pWDUnKa5Q5nh0Aa0nDrFzSQOSPTRIhIRY5uqxQUwVX60E&X-Amz-Signature=b9f6aa5ca7628e09898748e8a89cbf024ab497ada89d9ffb07cd3541cb80e849&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=ae62a0f9c90356895d185b6221e4e348d6c68bf35e0748f9434ff85c04835e3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=47fbaae25375ce5666ce8214b93ded183aa02e578051387f80fb501afea44ba0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=09d2ce3c9947cedce6fc0b07e79241eeb4345dd2040d1cc515df94830b3cc2bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=2f4fb6c387e99977f86f4374f3ebeca4baccb5e1960557ae87234293c6da1f52&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=38bc56a675bfc86da42a5f0e00023eaead725c33d944c3507d310308bc9ade57&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IL5OKR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbjTNNPt5YoCSiIWtBbk219tW86FPAnKNUP90%2BT9B9KQIgOghCrDhbYqHHO0Ar6Ysb4uFP0%2F9DI8ILn9Z5pDlPnssqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq8c0reZxrM3H9NVCrcA1%2B7m3hBjWxfNnQ2uhipiRw5CqaLUF%2Bj0MRNFrlimorIbNFF3%2FkYaPGhAqQfK2R4980N2W6BbGhQPB8QBpLibI%2BvDI6aPpCy81w6n%2FgQnR8EH33FiYe5iwNuz%2FM7rU6HQayHpKRjE6V2SSrNeYHfOYlxbkHloSkLtAkjYPGhZGXjXBO%2Fe6CQ1DZCYwel4pPWO8v6r7h8G5UNRfYCitSL9zUbF0L4cHW7%2Fj8tfauWc%2FYcyiaiB5jOTRUCE34%2BMX0G%2Fh%2BwtEOW6qFTmu1gjkC4Ed7QaV4FgsXBoOfoOdJYZYkY3frWJ7i5R%2FYH48N4eQ8fcX%2Bmg6sLMJmflhA89qB0NTPcBZ0hSHWdd9YKAOj0rB7aW%2BEqvKfgfBaIXVYeXQ1udH006RoQgAHZhy9LJWY%2F5kuN4hZJ2rBbCbkrfAMHj4TLhgG6rqLqMMT8NRxeAL6cEX%2BjMGI77ZYU5X64AByQjbp2PO9tuN0nSFxnw6q7dUBHs7CaIRrjVDDFIK3DT0hjpjasveQVtRZXrMTmevWfqargOoWrkxqTnUyqvra27%2BMBIJ%2F61BqU1MqD0E8uzSDFFY699mtuEFff9i9cfVRaBb94GaMCs2gjIGfW2DCxkpSGpXga6R%2BRUFve5GrEMODi%2FrwGOqUBTX4zINCLhDV%2FGWuYR69m1FRPDX%2Bdn67sBR4RtT1wwsKmgrAEwfkOUnv0wVEUrJM8tj%2FEqz0pAozzxNJ0ul2leOSfSggGeLc55NwT2fpYKhinViRaspYVHkxfECrPRdjgZZB%2BRNqQM50n6XCxqJ1v%2Fsq%2BZ%2FoULd1rXXfqsbUFKnyngANU8eCT%2FImJj2GbVlqoUORhnw0Ij5aCr4hsEnZrkXqkWMve&X-Amz-Signature=22da01974f92def3f7f39e4c46f7128de8bdd8d0a5e65d883f0ae92370f9ecba&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V6ES7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs5RwPjtanzCLiDmLTG4Kqq5ZJvk2tBBSkIIWsouxsmAIgJzDUFeNZexnp6XfqWs1NU3vZZ6200qeoth4%2FstSrzGUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLGDz9xAmswy2oXu3yrcA9Td%2B25pd2TnymVDtB2kDjkxJnGuvPGgHyg2qVWRdM0GPtHDoliVmFXquU7pn6mWbqyildrazzGU7GCJhc2qN855tLz5J2mc01GzvP1mZXctGld3vpZ8AsbGyMM6Vf%2BA4%2B0ba2euHkwvqyyOUOR7tXB3542IZwKbFCnjfW3dy6%2BRqYBs7uRcsqXy3lQMRcm03Q8AHhQSHzmYkNvGBB3JXDdOyiy0LqTEWL4VA3xgJY59JtUSKaAd4wZOOIs2bMiRmll6YHduiatWl%2BzwpKcPtej%2FKs6tJ95Rn7l2pC7ZUfUP1MhZDyb4slxSrPigGKWy6iU9eGPqbhsDVtupm0NxelEXGxuMlltMyL5POr7eeMQAOzZ4T5SQJp%2F918dJSpvu3zbdryaG7YwOfgTQNKIdHq4b2RaGl%2Fn1KV342yDERU0tm09hPtn1QiGkppKb%2B4c94%2B5MEqtEiXnXBtoZ%2BVsQESInBPok0hrZprwVCySde3%2FlTytOLghjCHB8cl54B3ixjGXB2VyzWMWrDu%2B3Xkz8aK8eqcpEUbdYKV8ht32A4AMEdpu3FCb4%2F%2FO91mcZDvSol6%2BAeaX2gOdeR43VWW9mfnyGDCFcIY7dMxu0eRyCQ00VdVGZmORVAFwTNpz5MJrb%2FrwGOqUBKmIYp0RN9lZ%2FG3%2BB4a%2Bv1ExxbVMvnlpYLtI4LVrrd8baU0lRNaKHZS8FMARowcy06WLlfNkN26G1YNaK3CYMLNYWl%2Ba1hVyQBTPp8Mva5BLOk3KsJHdKU5rA8L0h1d%2BwDuAhxDB0izhK3Wk3Cxy%2Bt5HAPVKjCWxiamRcWsGGGzHBWpT2Zp8qsc81h7QtmdRT5MS6Dwq%2B%2F7p%2Fp5HMuev37X9fSl%2FX&X-Amz-Signature=2328284fb656ede928d088cf1da4a93b4ff11717b07ac296ac88174e29072a69&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V6ES7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs5RwPjtanzCLiDmLTG4Kqq5ZJvk2tBBSkIIWsouxsmAIgJzDUFeNZexnp6XfqWs1NU3vZZ6200qeoth4%2FstSrzGUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLGDz9xAmswy2oXu3yrcA9Td%2B25pd2TnymVDtB2kDjkxJnGuvPGgHyg2qVWRdM0GPtHDoliVmFXquU7pn6mWbqyildrazzGU7GCJhc2qN855tLz5J2mc01GzvP1mZXctGld3vpZ8AsbGyMM6Vf%2BA4%2B0ba2euHkwvqyyOUOR7tXB3542IZwKbFCnjfW3dy6%2BRqYBs7uRcsqXy3lQMRcm03Q8AHhQSHzmYkNvGBB3JXDdOyiy0LqTEWL4VA3xgJY59JtUSKaAd4wZOOIs2bMiRmll6YHduiatWl%2BzwpKcPtej%2FKs6tJ95Rn7l2pC7ZUfUP1MhZDyb4slxSrPigGKWy6iU9eGPqbhsDVtupm0NxelEXGxuMlltMyL5POr7eeMQAOzZ4T5SQJp%2F918dJSpvu3zbdryaG7YwOfgTQNKIdHq4b2RaGl%2Fn1KV342yDERU0tm09hPtn1QiGkppKb%2B4c94%2B5MEqtEiXnXBtoZ%2BVsQESInBPok0hrZprwVCySde3%2FlTytOLghjCHB8cl54B3ixjGXB2VyzWMWrDu%2B3Xkz8aK8eqcpEUbdYKV8ht32A4AMEdpu3FCb4%2F%2FO91mcZDvSol6%2BAeaX2gOdeR43VWW9mfnyGDCFcIY7dMxu0eRyCQ00VdVGZmORVAFwTNpz5MJrb%2FrwGOqUBKmIYp0RN9lZ%2FG3%2BB4a%2Bv1ExxbVMvnlpYLtI4LVrrd8baU0lRNaKHZS8FMARowcy06WLlfNkN26G1YNaK3CYMLNYWl%2Ba1hVyQBTPp8Mva5BLOk3KsJHdKU5rA8L0h1d%2BwDuAhxDB0izhK3Wk3Cxy%2Bt5HAPVKjCWxiamRcWsGGGzHBWpT2Zp8qsc81h7QtmdRT5MS6Dwq%2B%2F7p%2Fp5HMuev37X9fSl%2FX&X-Amz-Signature=c6ed444b34d12862445f540cd7133a892893c8280b773ef531e6d3fb94892ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIS4ZYNN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHDqaqc3CEik8aLG8eARsWdoAB%2FNfnOCwvJcTk2FAd1QIhAJDMKMq7jecPVsu9K%2FGulG%2FS6nEj6QTagneN0gHsDqAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqUzY1YaCtfITic40q3AMMKF%2FTkFgV%2F4AxaxHls5iKxd7mJQXOFSjkzJaRxLc%2F1Hevdu31MFai3WZRya4xX6pX8h%2FG9huxeIqHI9GDWMU00xhKVFNPPozjitspE0TNphH7ueSxDuanf%2BMcd4jPp05qDOB4AcNNSiQcz8ZXJQlPuHmHM7MNG2UZ7MjcWoSFutglVqe0eNSMwgSQ0gcKwL81iyHYkDW7GA5HQtHreg%2FPgmpmEbOYpVuUQLK9R%2FsQaaetNJMDp22KBTNHgbBPN0FxXsApFrQWIytOmK%2BBYK%2Fx0XqWKyY9YsIWyk%2BWKooeRYJCwGYjkHpD986%2FA%2BYqc7%2FfWUYp4mq8hsEpZKVYn%2FFOWIxJUl9JwFjgccxQujG4r5ySzIXkuOpXqLs72okU7GdEls6RMFCqDTS%2F0byf0quWOera8W8NUquyluICNYVdMfbYDzqxUzZrJND5Uw7cMGZFI6ayzJKKVfecoFYJzXrFy1GXeb%2FWP6JOhqzF1Vk%2BM9kvPYqthsVvwBxMjg8jGC%2FTx%2BdbHpQCiM9JNCAif%2Bh%2FpDnnE1EK6rBMYsbwtAd9Nr%2FVX0j6CqUF9mtYtArc3D9nrv7knErLmRZ%2FPEKeb2DRl3shnqoP1odMfNS5NoUV1j%2BCUtLMYKjQqhocDzDi3v68BjqkAVve3%2FOLCotbpGbh%2BJ8ARwYuUX6RmYdmlRXclNvfPNjLrr4aqfdK5BUF08ff%2FIw6sJcxvNacJx7g4G6Y0dbuq6Yb6xNRstL9RvItNbHjDXIpPsdMNehMw%2Fmz%2FwN3jkrRIXK3TFlRPxtfgYiyIWtVgch7kMKZ2nzgWJ0W7oYkqt%2F4wgWvIsuiz5BSt%2FpW3Q8ZctzF%2BSkUQ0%2FOt0jMayhnD2jsc5%2Fx&X-Amz-Signature=daef9946ce27af603906832a6d74f7012399786c62276f7dcb410fa661129a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGWOPB3K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuspvL7cV9GpaRA%2Ba8GPZIvf3cMXN7IiWOgi7lXOd7AAIhALDVYxdcLM9syuRbdWrYmPJ5FNGMc6hxxYPMTCjGwwAaKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybqOXJTlq1h0%2Fjv7cq3AM4KALXcNEBYFE9RYUtpgtV57bV%2FkwKqeiSBCvZrbz01hqgtyYH4n0RPgBcehnLTWb8ykdIMzeLne1EaWy1kVaZytVj0u8RsWYEH5eh1pc68RXxddPnT7GDWU0THtxNvCov1I124wqPUlswlSR7ALQk3s9dvXVN6N3cDWNxCUCQsWf0Ir94YC5cqXIT4wnlwvnnQsKOttpKYMPjkE59i5TFiomUC17SKRougcprMqzZw7IIwMGRw17ugKvkvAiOaGQebemvs0IneGU7sWfgBvpj4MLF%2F4mOoqY4rCQsQMMgohjnrSPubjNIvZLzQDbDEhX%2F602CKWRjs8EeMBBdOsk4RKUHIAXki7HgritWA4m6HQT9xeR1TbUwcdu4FW437nXFgckqIx%2FnKld2Wmc0x3kmV8NIhawgyvhbi2rEbd8dGcsN2CMPukj6HEhy%2FP4NlDHbiw4wegU7IRa8ImWhlHjgtKidLRs%2BfuWXUpIgGCzODxvxCdhp15Zjqfk1YAhAcbItDS5nerCS8eL2ZB4GaB%2FjyZ%2BUnSF5I1pMxFT0ZxCG7h%2FB%2FJ1nNg6Pe7dYIWUOMjVdZKfo5gY%2FI57m%2FiIprg8%2Fr4l2g1U16eMn%2FTAHc4MSMv5SD%2FtZ0riyq8XnEjDT3f68BjqkAaQwBXitPDec%2ByCAetkD2ifAo%2FDw8zKKbdjz3SfWpkjos1FOItL3voDfy8J0PV9GJhjCySGIdYBtsweV1Myolzm1x8jgzhoj7e39lZr4BpxdcJEazr1HYFs8Do4omKPTHx0kMSar4jF5SiNY%2FfnwreqlOEznJj%2F5cwExD4EPhxjPhHmD048LQxIPJyJTdX0rElGedyc%2FGuJi6063%2FPylVDtMIkCi&X-Amz-Signature=e5c95c328ba565e195f24fadebf65e6ebb5c6c107c3870fd4c4f768d716826d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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