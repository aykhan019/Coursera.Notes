

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=39e4b7ac91674d5b85f2a72a65332bacddd37a602e13e16cee7124fe1f03ca10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=cc1c681992808472c2485aa7e25ddc093f7d8680d8ae96ee1cdcc96b22338261&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=30159410dbd62e434359cdceec8747c0b94520d2175763a52250931a6ecaf949&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=680c659a4a726f8ba858fdba979bc5213938b35747d31a70a51d635004d40393&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=4844a6ec6c3239b5ec0d3c623e712be1b22b6fb3012cd26c5be980d147d90fee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=2bdbdf4e95c7e774b10cca0fc7c26d696f2de69860154ce642949b0a66be0611&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=7c6301e6340508a34ad0d79c08d3e8321eb9827899a09cb589b9ee1a13e4c31a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=705c0fc91b4a4913b3c112c34e6e3e5c0facc998f6153231f5cd6722b64fdf9f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=1289214ea1e1a7ee9f41047e2e89c3edde9f103ef4087ee713b1a4d00fa96357&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZXW45X%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIF9L%2FdhsqZ0EVFqZmmAwTfymI04AoCKNpytWqIu3HqozAiAhmgSIqxBtcIS0T%2Fku6d6WIZ9XHBgzpypuRpNuFJm1JCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIM2XnSo7s0y3cU1dQNKtwDrc1XsJ2DjUaqdVOGhQCZ%2Fd6Y1a0KfLnuYQ2ePGILtoECJRzvVzTCIOpENcjezed6ROA%2BEPe8EkeSw768hfpdtxYmmum8cu0Fibg6iv5pJrYsfzL5wJKhuvCuKGsVDQqMINTwjQ7Iza6b%2BPDS%2F9DL5EOQbYCRYg3tbXJ9266XJYhtxeU2hDVRTTq32RKPudCSrUwUNZJ45uEL4vIVuA0%2B50nxayD1epePDQsj60oLF09bk0%2BhHw0PbGOApMlV0QYMA4Xj%2BRmKSh2ycu5WEBEOD9s2P3rO1BpqplvnQOd5AO%2BXTYTiFSAMxMWJVC8JSPFO9OfBucruEcxCJSwGSkd52v3t%2BQBbsW0SuJ6mvZdJsr%2BSD7q%2F57bKuJ5Atv8ZdBLm3lMEyskhDSuC6W1jFOAjKemKpcPkI63t%2FgDDTPnGr7mCua90eyfbmwvWSHLawpI0rXhLZnbt0bR0OBJOtHiPOLJnRVyk1%2BgTwA9Oa1oul5Jwfyv89ocsd1h6jircBeH3Vnt77qxMj%2FdcnqA0nbH14prEGX0U2xK0epna904Tkv69%2FX1h5dj5tlkPiAnG0rbh0gFjZ9RsT4xhYznVB7kM%2BLloo1THgK4kNVtRxp%2FgxtG%2BvDF3HTzhVZ1FXNIw%2FvaEvQY6pgFlkbjodAhYVz1QZA1GgdSIRfeagvmu03gxukRFtbvuq9AtxcDkPiLxTUN%2FsnNq%2F5rHjcOZhLDfQEXb0jgUeUQpmH0VepAbAtKSjDfUj0aSTTUtpVM5PIe%2FEc%2Bs3hC2%2FYLFWtWi45EayqfmoTTPxXUGJ8uyceGdGjzp5ni8mfBvKib8%2FSp5MEtx3tibiadnyAbUQqCkpgM5JNqkpxOlhN2JzEeDl7m%2B&X-Amz-Signature=5f41f7e42d80d904e914c581ef6651300de89c6d91299de29fd803c0d683c09d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZXW45X%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIF9L%2FdhsqZ0EVFqZmmAwTfymI04AoCKNpytWqIu3HqozAiAhmgSIqxBtcIS0T%2Fku6d6WIZ9XHBgzpypuRpNuFJm1JCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIM2XnSo7s0y3cU1dQNKtwDrc1XsJ2DjUaqdVOGhQCZ%2Fd6Y1a0KfLnuYQ2ePGILtoECJRzvVzTCIOpENcjezed6ROA%2BEPe8EkeSw768hfpdtxYmmum8cu0Fibg6iv5pJrYsfzL5wJKhuvCuKGsVDQqMINTwjQ7Iza6b%2BPDS%2F9DL5EOQbYCRYg3tbXJ9266XJYhtxeU2hDVRTTq32RKPudCSrUwUNZJ45uEL4vIVuA0%2B50nxayD1epePDQsj60oLF09bk0%2BhHw0PbGOApMlV0QYMA4Xj%2BRmKSh2ycu5WEBEOD9s2P3rO1BpqplvnQOd5AO%2BXTYTiFSAMxMWJVC8JSPFO9OfBucruEcxCJSwGSkd52v3t%2BQBbsW0SuJ6mvZdJsr%2BSD7q%2F57bKuJ5Atv8ZdBLm3lMEyskhDSuC6W1jFOAjKemKpcPkI63t%2FgDDTPnGr7mCua90eyfbmwvWSHLawpI0rXhLZnbt0bR0OBJOtHiPOLJnRVyk1%2BgTwA9Oa1oul5Jwfyv89ocsd1h6jircBeH3Vnt77qxMj%2FdcnqA0nbH14prEGX0U2xK0epna904Tkv69%2FX1h5dj5tlkPiAnG0rbh0gFjZ9RsT4xhYznVB7kM%2BLloo1THgK4kNVtRxp%2FgxtG%2BvDF3HTzhVZ1FXNIw%2FvaEvQY6pgFlkbjodAhYVz1QZA1GgdSIRfeagvmu03gxukRFtbvuq9AtxcDkPiLxTUN%2FsnNq%2F5rHjcOZhLDfQEXb0jgUeUQpmH0VepAbAtKSjDfUj0aSTTUtpVM5PIe%2FEc%2Bs3hC2%2FYLFWtWi45EayqfmoTTPxXUGJ8uyceGdGjzp5ni8mfBvKib8%2FSp5MEtx3tibiadnyAbUQqCkpgM5JNqkpxOlhN2JzEeDl7m%2B&X-Amz-Signature=61afccb8b29f6e6add7d1c3f0879bb6f9c06296806e1e1c00af8089efb3caf96&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZXW45X%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIF9L%2FdhsqZ0EVFqZmmAwTfymI04AoCKNpytWqIu3HqozAiAhmgSIqxBtcIS0T%2Fku6d6WIZ9XHBgzpypuRpNuFJm1JCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIM2XnSo7s0y3cU1dQNKtwDrc1XsJ2DjUaqdVOGhQCZ%2Fd6Y1a0KfLnuYQ2ePGILtoECJRzvVzTCIOpENcjezed6ROA%2BEPe8EkeSw768hfpdtxYmmum8cu0Fibg6iv5pJrYsfzL5wJKhuvCuKGsVDQqMINTwjQ7Iza6b%2BPDS%2F9DL5EOQbYCRYg3tbXJ9266XJYhtxeU2hDVRTTq32RKPudCSrUwUNZJ45uEL4vIVuA0%2B50nxayD1epePDQsj60oLF09bk0%2BhHw0PbGOApMlV0QYMA4Xj%2BRmKSh2ycu5WEBEOD9s2P3rO1BpqplvnQOd5AO%2BXTYTiFSAMxMWJVC8JSPFO9OfBucruEcxCJSwGSkd52v3t%2BQBbsW0SuJ6mvZdJsr%2BSD7q%2F57bKuJ5Atv8ZdBLm3lMEyskhDSuC6W1jFOAjKemKpcPkI63t%2FgDDTPnGr7mCua90eyfbmwvWSHLawpI0rXhLZnbt0bR0OBJOtHiPOLJnRVyk1%2BgTwA9Oa1oul5Jwfyv89ocsd1h6jircBeH3Vnt77qxMj%2FdcnqA0nbH14prEGX0U2xK0epna904Tkv69%2FX1h5dj5tlkPiAnG0rbh0gFjZ9RsT4xhYznVB7kM%2BLloo1THgK4kNVtRxp%2FgxtG%2BvDF3HTzhVZ1FXNIw%2FvaEvQY6pgFlkbjodAhYVz1QZA1GgdSIRfeagvmu03gxukRFtbvuq9AtxcDkPiLxTUN%2FsnNq%2F5rHjcOZhLDfQEXb0jgUeUQpmH0VepAbAtKSjDfUj0aSTTUtpVM5PIe%2FEc%2Bs3hC2%2FYLFWtWi45EayqfmoTTPxXUGJ8uyceGdGjzp5ni8mfBvKib8%2FSp5MEtx3tibiadnyAbUQqCkpgM5JNqkpxOlhN2JzEeDl7m%2B&X-Amz-Signature=947b96c155b50639d6ae69a7376a2a8c45ac8730df78712f36e919795de885f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=eb52c678370e919915c0da4fe2e69538faefc3da8d2500f78a0ae3180ec618c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=a0c8ab76f764e2de49179f7bca99a9e96efa6d4d4b6624a55b993b08917dc3ef&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=d681c155aec9a252776687aadd3937e3c1b82c52c163e6653710cc9195121b0e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=3b88e7c3aceec844785268b2de8180a0f7f9132aeb006d006e6f2dc235135d6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=4f5337c24caae9c4e696397a3fc0d452eeea7c85a9591c93af43ab769ae48922&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FO4CN3I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC9m2SVKEJMOLcS8zO%2BV73eXQmsjysPfny9J2%2BZrj7YDwIgdtwOXEYuCB9QIfQIU%2F%2BdVfSMgT2M9rrRJzsZ61kJHW8q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDE4YWN9WUAJtxRSAeircA2hnBhytKM6moq1Ri09Lcu0bWwKMVZeo%2Bhn8ewDnzX0DXShlVZcwgzMiRilshQkXn%2F7Eo4hwXzFw786%2FWXYV0sEemdkeWn6bi7nAWCcS87AqAbuAL9VcXlciltFiF7ywNpGBYg3rSCTdnbUXAzuDVQvxt3WMCSzVnnwf2qc6YgyO9Yn1hCh%2FyyU3P8Hm9hFrErf%2FGm1Zv7In9WomGUPypQc%2BWnGnltLuabl9LvgT5bG6%2B2eVOUsjegvqGVGQYb5K%2BcVZXiNyvLEUV9MzsW9veyAOh3OqhAL3EXg%2BLw2dqRdPzvn5Cajd9r9zkP8WbNY4DK%2B%2BH3DaQTJ0M8Zp%2BgmTAQsMEaFX7OMz3eFXazcYBLRnjDq258bmSp7gg7brkRLBvMYyUVfCOfM2tOos1hEX8SrUpZztRP9TKm3p1f1ZWzfxh0FXyhkOLBcWHi%2F541VNIQPzndYpvc%2FP%2F6U%2F0pDf80DRVfiGbFAiGcPZomM8W%2B8BMvmDpMdJsPlo%2FrJIPnFd5tGW4FXHu37rsBUV4segMWHGqyNXwJDYuk8qNRQBfCsRyhBoe6KVaPNjet8ISxhrn%2BmwPrFMp9xfrnIaNCzzxHrFKTajEuFEPy8lpB0RFcCRiGY3plHGJDFLnkCvMJH3hL0GOqUBqPcKw8c95yTqminY5L72VMRziDy2BbphNGIDkZo5oKKT5LvSBvixbxiaxBNk4Ui9BXXYV8BRfUE5%2Fhf2OtaZUJ%2FBy%2BmwiUEFixvc8jJo8%2B7PCfhAP6O20qTasdywmyU8sRrZtqKARnD6ROtSKhpvXH7fZlPtGwOhqo3qXcuuySbHHRnb5w%2FQtPVjUSA44wGPecGdMu5LhL7B97trve8VsloNb9tu&X-Amz-Signature=97371d2bb1773a6543e11d2881881c311fc673ea84f6cb48c4e5dc637e0bcb7c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMMQMGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIEpv5l1jcTnbhGcbUe2TkFbQ86DSIxs67pOezLKhOI%2F8AiB1sAsI10eknjLQ0yFRrp22JxNenyHcsmAS7AQKRHN%2FCSr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMaYBa1B8dCMOZbRpHKtwDtbzT%2B0MJe5%2B2o8GEQ9UtYvTC2vq3Ah0dZSRZNnPTOsAd09X5ZiZ%2FmHoEFstP4CBt88%2FpVDD%2FtWq67igAeoUdthh4GYKNtAObz3HGl2reQ954eIWPjywjTZJFfXrNdc%2BC71he%2FBbmOQDbyQiQuqKQ7hxoiawoyLs5wTw3GTzTTbeJk9bF3VsVmu1dK8POwO9Big6XqS%2FaX01ODUtuxrx%2F5%2BF1Q1g4hAHHm3fF95oeMkRYy7T1PGgxKH26eaUvdQwJhjYiSR%2BmIVDc3sSJO2SZJ%2FFBPiGfFh1VjiOa9Lj30O0Kk9RKSc1kesSD%2BeB5q8cxzBobMkh0qnaz0pxgbUhSTs7g07WcoU6XDfIw%2FqGMZcKAUIIbhoUX9khj8HkyNhUloCS0bWzXBVNfPxUoFWQkVZv6Uz4whO8tatRncKzCUpM1ixPg6x63Ir8ZRgGVUsVq%2BDEEQhKv4aAKsIFjclloPuo4nkceHEzutQyPEyfpi6ELjVoPGsJNpN27a3JBvZef3n4q8KExZ%2FOerRHKSUoqSTofMbVuMeMW%2FpgdSyJ4Z5VOBQ9ASwqH4xpd%2FEtGlbVMIdoSqEXKw9EEGgFXN9dLlXt0RF2aajx4z3KR9oRi%2BV2kKw4JlBrmjpNyF1UwpveEvQY6pgE%2BRA8oNUK2c6kEZCpTSWYonSGn19TbX2Yxbbyo8moG7m2xxNRtam%2BxDMdxwOkjy7SqB3ZHbt4%2FQ5nl4SdNXaHGYlnP%2BKy79XFNxIbi2f39peQEj7dnPwlNAFL4bIJz%2BP7TZGrM5CqjGAdXpEq4QUv6gvYGVZjo6lEZX0R8hc215VAAaHOjf8hDMj8iCqdc2KF1JSBdCVDYORofissgKrp4B7nEGFkT&X-Amz-Signature=fb08c28f1d52180be16c0e5f3aca2b51ca6fc3b2bf3029bf54c1993f726ce183&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMMQMGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIEpv5l1jcTnbhGcbUe2TkFbQ86DSIxs67pOezLKhOI%2F8AiB1sAsI10eknjLQ0yFRrp22JxNenyHcsmAS7AQKRHN%2FCSr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMaYBa1B8dCMOZbRpHKtwDtbzT%2B0MJe5%2B2o8GEQ9UtYvTC2vq3Ah0dZSRZNnPTOsAd09X5ZiZ%2FmHoEFstP4CBt88%2FpVDD%2FtWq67igAeoUdthh4GYKNtAObz3HGl2reQ954eIWPjywjTZJFfXrNdc%2BC71he%2FBbmOQDbyQiQuqKQ7hxoiawoyLs5wTw3GTzTTbeJk9bF3VsVmu1dK8POwO9Big6XqS%2FaX01ODUtuxrx%2F5%2BF1Q1g4hAHHm3fF95oeMkRYy7T1PGgxKH26eaUvdQwJhjYiSR%2BmIVDc3sSJO2SZJ%2FFBPiGfFh1VjiOa9Lj30O0Kk9RKSc1kesSD%2BeB5q8cxzBobMkh0qnaz0pxgbUhSTs7g07WcoU6XDfIw%2FqGMZcKAUIIbhoUX9khj8HkyNhUloCS0bWzXBVNfPxUoFWQkVZv6Uz4whO8tatRncKzCUpM1ixPg6x63Ir8ZRgGVUsVq%2BDEEQhKv4aAKsIFjclloPuo4nkceHEzutQyPEyfpi6ELjVoPGsJNpN27a3JBvZef3n4q8KExZ%2FOerRHKSUoqSTofMbVuMeMW%2FpgdSyJ4Z5VOBQ9ASwqH4xpd%2FEtGlbVMIdoSqEXKw9EEGgFXN9dLlXt0RF2aajx4z3KR9oRi%2BV2kKw4JlBrmjpNyF1UwpveEvQY6pgE%2BRA8oNUK2c6kEZCpTSWYonSGn19TbX2Yxbbyo8moG7m2xxNRtam%2BxDMdxwOkjy7SqB3ZHbt4%2FQ5nl4SdNXaHGYlnP%2BKy79XFNxIbi2f39peQEj7dnPwlNAFL4bIJz%2BP7TZGrM5CqjGAdXpEq4QUv6gvYGVZjo6lEZX0R8hc215VAAaHOjf8hDMj8iCqdc2KF1JSBdCVDYORofissgKrp4B7nEGFkT&X-Amz-Signature=8a56cbf154b8945013d27395ade63c269a7ed8fab20e92f64842b0ce905ebf91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP5KXP5X%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIGwI2R58RCSB4p%2BLrTaDfmfaLPzFEZc8C3vaweBaIY5OAiEA%2F9a2t3FyAyuPkw2BoCRZHpssoITCRVATMu6xStEIKjkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDMr8f6G0OOiM7fKOpCrcA3shPivIoSa1Q8SOkiLHQXxfm%2F%2FsLo1cgum8Pw8E3AC5cv3UbLQjvOyIfay6ccxrtQEUEv9iwBKN8hSIzHa9TY9BajulPjZsS5ek9p5%2FyOpIBf3Dial58uyqgiuEB%2Bwn%2F3tmwNkH6X%2BnK6w%2BcL9mRpCZZYRiX%2BHg1QdF1VTnMi85vTQss6EAZr4glfSlJoz6BhAu7brb%2B8kH9dSkXxfx3x9MbmxA648VzQB0TI3xNJ1nZZvOiXrdo1st2F7IR1Eo1oycIkh6ffHZlmxZSuh9BOuRGx354%2FiXBa%2FWrxkzkj6VwfJunkPzuZEdnVTQ7bZOdbcM99Jmzp4tArgZjB7PUCZUH9hVt5My1TJYkkvIDbYdCn6FeqetB6lDXpAK7Q2aB3OIMY%2BTOKoL%2FxF3mdFiCXM3N2I605aWVwX6IlBR7P2WAwnry450VsDuAa%2BHpaHilYp%2BnjDMMVcAEKA3K2fgUhET8ZsasRBh6H54qh4CK9%2FT5K19bu%2FljawJpAfsFf0iLagO7i7UQvZVVMfEptWPIzKxcd%2BVvIgPb5nbq5AHzApeuVX%2Fnh2u6tKRpny%2FgRVKjmkuXIO%2FP7IZETN02ha1EJZN%2BWdzRWF%2Bk2Hb7fP3R2DQbGzr1X9vYk1wF%2B9mMJH3hL0GOqUBegkI56fcCA%2BYt01k0YDPviS8%2BPjiCKpLjBD1EGxE67avoioWzhcyEM8IobzLIojx1yBh46lFMkn9dtaj1TvpjbD%2Bij%2BlD5fRmzkb3s2qxMqXqWxjTtxYoe%2BPTpgaimWUXecxjPje%2BlhKGALZ7SyfBB13cp%2BeO4UIiP3JILo20PMlnr1M16%2BAlNN9VmZGSKzXhAC4%2F1nUYCKrFe830oTJNttjc0dV&X-Amz-Signature=7f67493464c3bea1ae7b90c9923a5bc364ecf354edcf2ec8124b29efb6fcf629&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFU3FWJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCSb1Rcbfg8V8flbl5vqiDT%2BM2ISUuV1tqvkYbAmK7eeQIhAOqiwOTIqUA2%2F6ugrtbs1oUZ%2BS1jSAdcs%2F7eq4pz5uZEKv8DCB8QABoMNjM3NDIzMTgzODA1Igzq8BW%2BzzXvFOA6wLAq3APXtgXXBIwL6O9zEOsYiAcjp%2BwFNCY8gDfoWDbK6o2LBnx1%2BZBPs6vPd6WOdefnQtmCYJmZnznRxeGwfP%2FJtIpdcCl3wf9ZJtrESDsIZH2Osn3E9i%2Fb0w7YyZyXOLGSYqyfT0thsKa5bwHm4d5TAJIBCfLCnAsW0oYBgf2xny9AkD9th2o5vC9Gfwy1ULAk7270zwHUjCaQTQtF93CgWAZLM2YcaYHIqebUF%2FYM8CjO27QWvXrWEkxnXnEnVuCTpAJy8TibY9Z3qDqua0wcCii7fo6xDUTpdlE7dJ%2BDiAiN%2FVTXMg4ejhWbv3ej4NPSU%2BgL%2FtrUj2jhENmsAXrNq6ZhGs%2BXteWzkIlNRVkmF3Ob9zNtDWOG%2BgHBNsGUAGtyeslF5j6Nyfw2FwlO289qJReavAFLVtNyEvnKFl7cjJToW9ll6DW4B7ZGTbCr3Yjw1TUxno%2FGZ%2FqLyP59ZnpxgCrzKHlMCZSdbJHWT%2FT4kEM79L%2FjZToGvTQPXbXxsGJtXWHmFjqGWDnUFNyfKx7Jc8hlJOjXHWHUL59zxAqgrUsBxxj8L9hMcHnVp4UOORnMiKCFWxVO%2F%2BnNmP9d48UVAe5EyoP3l6712krowdHXH2kHTp7ELgPyECX2wPYn3zCI94S9BjqkAV%2BxcT2UzToXfIzkahPKBxf%2Bj8WCr6CKnOj0%2BEAHn38ZySXgjt1Y1qzYMMtK%2B%2FskZkRbIx7lVXR9yexnoKmrnNyUI3GXDNd7tAttunhp6ndiPEpkiPaUz4%2F2tcxRNFt92i9PRS5Ujv11Bxx8XjnNeiHY8S1vT9eFkDLO9Xvm5GMQLJQ54BdfWeFz9%2BI8UyBZWUiL4kC0Br57mGPffyioel%2F2Paqs&X-Amz-Signature=5ced7c544468419a3ec307de67b64f77447eaf4813b8064e6975b8463c173920&X-Amz-SignedHeaders=host&x-id=GetObject)
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