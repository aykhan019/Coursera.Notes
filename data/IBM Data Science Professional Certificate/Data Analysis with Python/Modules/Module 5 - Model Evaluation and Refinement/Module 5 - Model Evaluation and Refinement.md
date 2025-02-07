

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=eae5ae39e4758697b35767136c2c0d2cce245d5b96e754a50bc41949279124a0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=cbfabbae2233e500ac9f2c331c1eccfb1425fccad3a72dd58e0a24995998d197&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=c2a609a2a4d314a45b9fe7d7dbe9f60675ee10e6f7201f59886d60c7f2a56b6b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=500a964a0be6b732b6289232f362bbd3bf5d9761bbb458bdea7b42a3c00a9def&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=69fd63afd163986497e8eec77d03ed9459f745055926a4133a5968ef378dca2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=203727a31093f4410891c42469b5614cba94cfd21ff252bdbe17492c11d942a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=a083348a9dae2910fdad8c974e07e29f5a6c519f314c2dad61aad56930e45303&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=26d9983e3b4df81621d49c3731fa2dc32984edb94938109b8cc41b0072113b65&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=4711dacfad820e54d65bb62af4e7ba39ad9e1e7e3063e76b6c63e7f9cd2c25e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DB6AWZR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDShgjTczZZXXuSKcScSMSnRB9lX%2BDz%2BsFoDLzRQvLNRQIgQkG5pBDhecTAq5ujk1e86zyjyROnDjzd6XdzwoEx67cq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDFd2N5LPor6d2nYc4SrcA42RGBOzNcEmWDKHSgOrTbAH6N0HC5Ie1AMyNuKweGeUpQd%2BIfhTfe7gzJ914xBbmQFjMSJPVnV2mENvKEL3G5VvqyH8FhyNEpnFkgqGEMtL03vtogTHAx%2BslFzVd4Vko3EUkXbT2DhqEB%2BkpZmhdQcsPaeRA%2F4iydxVndQ0vH7UvaOwzt5PfuPSI4ZV3KieK2wosUkvs94BIX%2Buh%2BmxztOiav7eY9BlhoiZeAfBg%2BQbwP8RbZhVIdukxtgkbE%2BeXuX7zRWWRzCKnnuaqD5XlxqAZ3TDuWyM80XfI%2FAoTE%2BS8%2FCPckW%2F2e3%2BzoQbZBFSE6iy3yGB1%2BlJFRzwIsAMmjlbXImXYZy9NEHSULXxi8R0Y6zZbp1waJQ2Kd9dOmjM%2Bs510dvwkLNDjTMEr4jBw%2FyosqcrAPb%2FBswBLPGn5mpRfahmbWPS7PUkMc4D0H5yqZwtWNNmrVfjkm9wA1gRX0HozQlsIKuh%2BOJvWyFSI3x45tkBWQ3lykrSG%2BunK%2Bs0f%2BCtlVf7EttDz%2Fsvvy85KUHYDJ9KChRs3WTQyioeecfPZqv9MOvuRMPd8jifWPrxZHbfX5xS%2Beo%2Bq90ZqKeicXjeWd11fMfjOb%2BojbZWBJzqp3uZKQHrIb8ZxvF3MODclr0GOqUBpa7SKsy6zqSKoUnPxqyQv5Y9upG0XLOccl1eBbXeEaWvCG479E%2BqJUzMwcb9VVVUjSbmeoBMzSZ6mzWgZOJBBoXsmg65z3XmMrgam4azyugXbjVAvYdJtz4braYGj8%2BKmJGOIzPMI8%2BUpIvszpOCAAjggqWpbtAjnMvBIVttgBLikvSH5JrSEHIoACGk%2Fc45h4im%2BUb5cH%2B7zrvAL30sFzUd%2Bk5J&X-Amz-Signature=141d5c3248e531769978992525ecda804b1e27361c8fe828e29bf42bf4c99de3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DB6AWZR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDShgjTczZZXXuSKcScSMSnRB9lX%2BDz%2BsFoDLzRQvLNRQIgQkG5pBDhecTAq5ujk1e86zyjyROnDjzd6XdzwoEx67cq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDFd2N5LPor6d2nYc4SrcA42RGBOzNcEmWDKHSgOrTbAH6N0HC5Ie1AMyNuKweGeUpQd%2BIfhTfe7gzJ914xBbmQFjMSJPVnV2mENvKEL3G5VvqyH8FhyNEpnFkgqGEMtL03vtogTHAx%2BslFzVd4Vko3EUkXbT2DhqEB%2BkpZmhdQcsPaeRA%2F4iydxVndQ0vH7UvaOwzt5PfuPSI4ZV3KieK2wosUkvs94BIX%2Buh%2BmxztOiav7eY9BlhoiZeAfBg%2BQbwP8RbZhVIdukxtgkbE%2BeXuX7zRWWRzCKnnuaqD5XlxqAZ3TDuWyM80XfI%2FAoTE%2BS8%2FCPckW%2F2e3%2BzoQbZBFSE6iy3yGB1%2BlJFRzwIsAMmjlbXImXYZy9NEHSULXxi8R0Y6zZbp1waJQ2Kd9dOmjM%2Bs510dvwkLNDjTMEr4jBw%2FyosqcrAPb%2FBswBLPGn5mpRfahmbWPS7PUkMc4D0H5yqZwtWNNmrVfjkm9wA1gRX0HozQlsIKuh%2BOJvWyFSI3x45tkBWQ3lykrSG%2BunK%2Bs0f%2BCtlVf7EttDz%2Fsvvy85KUHYDJ9KChRs3WTQyioeecfPZqv9MOvuRMPd8jifWPrxZHbfX5xS%2Beo%2Bq90ZqKeicXjeWd11fMfjOb%2BojbZWBJzqp3uZKQHrIb8ZxvF3MODclr0GOqUBpa7SKsy6zqSKoUnPxqyQv5Y9upG0XLOccl1eBbXeEaWvCG479E%2BqJUzMwcb9VVVUjSbmeoBMzSZ6mzWgZOJBBoXsmg65z3XmMrgam4azyugXbjVAvYdJtz4braYGj8%2BKmJGOIzPMI8%2BUpIvszpOCAAjggqWpbtAjnMvBIVttgBLikvSH5JrSEHIoACGk%2Fc45h4im%2BUb5cH%2B7zrvAL30sFzUd%2Bk5J&X-Amz-Signature=cec6107bae0c4592b018d566d21f021eda480fad67f3b9328b03f8846923c34a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DB6AWZR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDShgjTczZZXXuSKcScSMSnRB9lX%2BDz%2BsFoDLzRQvLNRQIgQkG5pBDhecTAq5ujk1e86zyjyROnDjzd6XdzwoEx67cq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDFd2N5LPor6d2nYc4SrcA42RGBOzNcEmWDKHSgOrTbAH6N0HC5Ie1AMyNuKweGeUpQd%2BIfhTfe7gzJ914xBbmQFjMSJPVnV2mENvKEL3G5VvqyH8FhyNEpnFkgqGEMtL03vtogTHAx%2BslFzVd4Vko3EUkXbT2DhqEB%2BkpZmhdQcsPaeRA%2F4iydxVndQ0vH7UvaOwzt5PfuPSI4ZV3KieK2wosUkvs94BIX%2Buh%2BmxztOiav7eY9BlhoiZeAfBg%2BQbwP8RbZhVIdukxtgkbE%2BeXuX7zRWWRzCKnnuaqD5XlxqAZ3TDuWyM80XfI%2FAoTE%2BS8%2FCPckW%2F2e3%2BzoQbZBFSE6iy3yGB1%2BlJFRzwIsAMmjlbXImXYZy9NEHSULXxi8R0Y6zZbp1waJQ2Kd9dOmjM%2Bs510dvwkLNDjTMEr4jBw%2FyosqcrAPb%2FBswBLPGn5mpRfahmbWPS7PUkMc4D0H5yqZwtWNNmrVfjkm9wA1gRX0HozQlsIKuh%2BOJvWyFSI3x45tkBWQ3lykrSG%2BunK%2Bs0f%2BCtlVf7EttDz%2Fsvvy85KUHYDJ9KChRs3WTQyioeecfPZqv9MOvuRMPd8jifWPrxZHbfX5xS%2Beo%2Bq90ZqKeicXjeWd11fMfjOb%2BojbZWBJzqp3uZKQHrIb8ZxvF3MODclr0GOqUBpa7SKsy6zqSKoUnPxqyQv5Y9upG0XLOccl1eBbXeEaWvCG479E%2BqJUzMwcb9VVVUjSbmeoBMzSZ6mzWgZOJBBoXsmg65z3XmMrgam4azyugXbjVAvYdJtz4braYGj8%2BKmJGOIzPMI8%2BUpIvszpOCAAjggqWpbtAjnMvBIVttgBLikvSH5JrSEHIoACGk%2Fc45h4im%2BUb5cH%2B7zrvAL30sFzUd%2Bk5J&X-Amz-Signature=24a8fae5fd2739a70e344ccea0b907075c1bf385533396b25a53abacfa4f8a07&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=4b587c5e873ae8f945c331b299dbda4f34ad1341befc3a7f92c8ab943d894086&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=0da8ae2c68f0ae84c26233041e9df7f136335690ae375b047c832a3a7f063273&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=379c0cdc8b758ca3e344957e2b2cfb6cab72b76f06389254f74195a48a715299&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=251bd5812def34128ce807a4ec1d08bc31a8eaa5ea7f8f33229d137384f497cc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=1db2e1b18d7d167812481bd52b74652cb81b4d490c51c1c6905f873801f7d967&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGCEZLPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCHye9NsKDtIndKuZ7honccn1o6wXSitikxC6EyxA04VECIQDRz76mHVc3fw4MMjzKNZrisQfYXpPofhgxE0H8QBHv2Cr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMUuA8gIaAjqbz1L66KtwDZUAGwQZkUhRP%2BQ%2FiqAuV7%2F4P9UScfOl5aw69XuwwGjf1QeZC9omqGdNERNaiV2elUbvaG9eAJEM7Go5lXMQkPJWeWs7pNDW0Ez5c%2BgTCEJ4yJ8Mx6moaGrDMzB6z5vMNrmAmY7lWCymik71Whm2jvL0r1h%2BZA7qLJmpJ4whyCdwwbcTBa8xNyK84qA29FWpwWP67Ji4mAn3Bw6aK7DGw0yc1ecCuDbpDwF7bIWiagCBVjD7Ie2mHmahN7xFYdmzjZYyE5FFKtfrJvxiwF1mkwFW6tMcAKmCsSaQPeT2%2BxE%2FKxMLQ0zAajUWh4psEUlG%2FSKg5hs%2BIkIygZoHcuAsQfXxypMVRsBFPOxzPmBHXXQWApQLmXwYjwG3cmH3uFUgsDyQ1ST6I0oLz7wLjqqUx51akKxkr0wbYPADthyMc8fSnd6QxhFAfgUvA%2BM2sV%2FZuzq96hsu2AYgiJ3Xu0IRjS7vAkQuWYdGfML3iyda%2FjdtJAOEv4zfOFsDhaBDQdhMPY0sj4atUMZa%2Fa9Cnl5otG%2FzQ0%2Bg8wRsv9BtnOwPqj6iHYeruKcabU%2FO3ypwH%2BrORtOiN3VXdy%2BMKAZzWsVLuQfVbtJg%2B9k%2F6tdWFWOHtnk1aC4ycZKKCmdftoMAw9d2WvQY6pgHclpR9Ye%2Boflc7Lz2RiNxgupqnWbjyhSN723F%2BahDf3KBLTI1EZkEXpy7bIxMOxQEYHd0Ffrq3IC%2ByR9iQNBFqXDNd2nFNBxu4MVzzoS3so0Imnh5gm0ruFGcGv3wsmhSIOQM%2FjT95vDpuregACXYyCuI6C9rGo2uV2wGdbOLM4wutlL1l23cPmTX75QZWvH%2Fa8CJsj7gVWzZiOzjYMnBB%2BvlsKwMN&X-Amz-Signature=7c52b72792efcd9ee5a22102403bd413ae4fccf1b53d000a6ae7ce91ec2b0d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI2KTJIB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIG8O9F%2B3ZR5ieth5MLae63BdOiBm8AoB0J3bfS5uhwiyAiEAipoS%2FxN70dtwmZCcZ2McMd%2FcXawAXV4ejSomAE7n7fsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDPLvl%2F1IfWEqGmc9pircA5LJmw3vfzcMB4iS%2BE0AM70PAxBcDJ%2F2NMb8606rOT0X0WpTEjNV8PKN1d4%2FTBaRlNc6x2cBaWi3C2ilTT5%2BH54FFLJQiYmqT5KSOZm96lLxQS%2BrtMANGCx2rKh4yhxlEJrEDRZMiKZKwCJ8jW%2F05JiYGvCno4%2FGtMrVtObr6cOLKuksDQ6JvjAhHGrjUeR7lvH6SB%2B86K9GMLI5o5ulAfmRoBdn8jUjkh3R32Dtqw98QbqW4FduKESNcoztcdIZcjkcrGbjegmK2gRE%2B0YCgtM0DpAyyx4PTjOsBARUPofMbI2mzlma2cG5LdPVL7f%2FqUePlwtv3o4EoQqndq8tCsfYldK%2Fghg42kQdDmNTHgZLiFZXHfmpnfMlU7rj2KdTQFwUvlbFUJCGHLzncAWaHn6HyM2Iv3Og32aqUBqFxcN4uz7UayBNagBy5aQpXhdCGMreTqWZ0zuonxbtGL%2BTRWi7bO3Zk15EjkK5aYZX8RK3SVr78yhTdkrRYONk6k3DAAsYJCAp4nPGn7cUogt0TLpynkXDap3v%2BgOByYbKNxuKpsan5P7Uv88bXkCaoVjiIjN7a8RrftXSg6B3prmaMjclUVDVk%2F%2F%2BP%2F4e5HSzOANIPnpC8EQXCZFo37rjMJTdlr0GOqUBi3D%2Fpa9WcDjzjmz6fB8wYUaecbmqQP3WYzbdcMcqz4CTgogxZ1FWYngpnTCXuWb0WBiBddHzr35bx3YcSmRbgxPSsUWwD2pPKOx34odzcOA87T7CYuqotp5aQoXC3FQD9NBcpjRJXhWGtNwwmHhUtGngkPGv3FR34SJG8xw5oa%2ByY1NDtXyiJLGMoSNceE78xaGxt0slHW1PONqwVg1Pyh32tQFg&X-Amz-Signature=3408f353ea9a1d5fa75a5fad378e7b9f9d90cb6d231ffb99915d1b2a9b29d096&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI2KTJIB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIG8O9F%2B3ZR5ieth5MLae63BdOiBm8AoB0J3bfS5uhwiyAiEAipoS%2FxN70dtwmZCcZ2McMd%2FcXawAXV4ejSomAE7n7fsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDPLvl%2F1IfWEqGmc9pircA5LJmw3vfzcMB4iS%2BE0AM70PAxBcDJ%2F2NMb8606rOT0X0WpTEjNV8PKN1d4%2FTBaRlNc6x2cBaWi3C2ilTT5%2BH54FFLJQiYmqT5KSOZm96lLxQS%2BrtMANGCx2rKh4yhxlEJrEDRZMiKZKwCJ8jW%2F05JiYGvCno4%2FGtMrVtObr6cOLKuksDQ6JvjAhHGrjUeR7lvH6SB%2B86K9GMLI5o5ulAfmRoBdn8jUjkh3R32Dtqw98QbqW4FduKESNcoztcdIZcjkcrGbjegmK2gRE%2B0YCgtM0DpAyyx4PTjOsBARUPofMbI2mzlma2cG5LdPVL7f%2FqUePlwtv3o4EoQqndq8tCsfYldK%2Fghg42kQdDmNTHgZLiFZXHfmpnfMlU7rj2KdTQFwUvlbFUJCGHLzncAWaHn6HyM2Iv3Og32aqUBqFxcN4uz7UayBNagBy5aQpXhdCGMreTqWZ0zuonxbtGL%2BTRWi7bO3Zk15EjkK5aYZX8RK3SVr78yhTdkrRYONk6k3DAAsYJCAp4nPGn7cUogt0TLpynkXDap3v%2BgOByYbKNxuKpsan5P7Uv88bXkCaoVjiIjN7a8RrftXSg6B3prmaMjclUVDVk%2F%2F%2BP%2F4e5HSzOANIPnpC8EQXCZFo37rjMJTdlr0GOqUBi3D%2Fpa9WcDjzjmz6fB8wYUaecbmqQP3WYzbdcMcqz4CTgogxZ1FWYngpnTCXuWb0WBiBddHzr35bx3YcSmRbgxPSsUWwD2pPKOx34odzcOA87T7CYuqotp5aQoXC3FQD9NBcpjRJXhWGtNwwmHhUtGngkPGv3FR34SJG8xw5oa%2ByY1NDtXyiJLGMoSNceE78xaGxt0slHW1PONqwVg1Pyh32tQFg&X-Amz-Signature=a3517ccd55f45a96942eb6ab01854d840655b0355d253ae205ef90570dcc24af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB7QWGBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIGk9RyA%2FjHk2QNcbaNtTzjhxXLmDv8DDVVQve9xAJs3HAiBzpujDayh3rTqhfJcoEDQF7%2Br8DQBQ4uxrxwHAtvZc0yr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMToywVoVtcqmv4VxbKtwDDlhv4hKbEeU2uwgveRTVdeImWU2qzr8PtLoqCFDu8u8Hop2FN3c3vNQa8dC2MFvmGbKylZVeZ6fhRd4QSugOweQnPNhcGAcZMSiV6k466qA2rR6l3p8mhM9T8CfBTWC5j1AU3EbebgFYWgLCBTf8GuUELXuse49VbBh0WT%2BT%2F3N0vEhlJFZT6VcH8RhU%2Fnijbnh3UIIDKzmoyQzqYoLHUyS49Nq%2FWHOsZ7pGj2L9IgLUsJ497JTcHnTujvDBByoYyHl9NWwyueAV40StJrINiyNOpxt2rK4xj4BEyq4rOSWB13l72QzcHr%2BEchx4jmFUwtKH9QMyvPqqYNckGv%2FsGY5Wy4JCDIxrQiWfJIfTHpaR%2B4vNYy3ykRRQ1Th1mpsSCQ%2BcqqjBx3hguy2kFItJkXoTUn6fpZ0wHL5vJH7TgSD0jkr2C%2FzlQEIPWTvoX4e%2FVnLesSCaTpRMLGIErod0MGXb0IpjBWywhrPwrRej%2Fm012g%2BEyVPtCjnNCZEMLjbswqocOPuVMEwv9nNlASmKNXp17f%2FDd7b%2F0in%2FIvgpR55F9NqRpWWKolki%2Beim5Qi509KIZyvKaJSFPKXDbe8PngW05dL0s1rAHJ%2BrbDWUJYvXPRWaSu3aKSSi4Dcw%2FNyWvQY6pgFjWkJ7Fqqb3GL01xDgpNxnIq%2BxBdC3%2FNzkpLDdj%2FfeJLxUXUh5HBsFEx8Ar956GISFfNO%2BXcX8TNwf97Uew%2BbMjiHSgdMH2vpAWBxwZ5EPq6CNivKPCRLTuAeRAuLVc%2B3nbJaPnfdtZCdP5LI4zVnfAmc9EBruE2bLDuZM8HsWVZQhdoaIBWIISMSctLE9Gl3xo%2FHax%2F67m%2FOvBy0tra6Qo5eY2qqP&X-Amz-Signature=f420bf4fd746f55cefd83d478b10e9a710a2ff696cb231c7f5a048dcf9d01a4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIPWLJJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIAbXFqgQjeS%2FDF0YZmXTTdJkxq0bH%2FnRzrFscJ2%2BaYVCAiEAlzXiARrXPHK5OlRf9o0tnMYSjjPCIVJYAsiSsFqwuwAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ%2FRJEAGQ3rfGFzjECrcA08kAiCTWWFUC%2BB24KBWCugPBccD1fme55O4%2F0cfWmBA8DbAImYuZwuf8BbPQOv78T64aH87ATnLvYiugi6nz3puft%2BDnRd4XSyRhpmr1M%2FsL%2Bh8tvdi0QxrnYpV20gvJQ%2BTK84frASH7wfZlMNOMajvef2JFwl7LnKdjTg7U21pvO5dFDS4XbniKEb7bu2rf%2FJqpEllFGr6TSd%2FIN4dqqZUue%2BM0fycXbefVQRyvgzquP732JR8U6CIP%2F8SbPZqeIRa9ijWWQoom0mMj78EmODVTOxkUGEmDdPhXTSi%2BQCrioXX7JnRvfjCg5WYGyP0cwflg75lOORKeqWVlV5GC%2BFdVftNVOsCy6L1d1jotB2EOoWKDMB30pHrXElW1DhScB9%2BpsU6qaqaq5NqYfCJwlgW45YvTMBaiT7rcZohp%2F4FQRtgvNbr3iKEZyjJstxjEFDBbwZ5116WSNo7wkIsuN9fkAV1mTJV1HzcQoCmOw1AaajBliH%2BdDt88N0QhyK%2FNMC3BUoAdrz94iOjTwqU86cVPEkPnlsTHkE1YZV%2FDFL%2FkYx%2FayaDiN9ZKrR3EGVZyBDD8V25JKDvr4hOuBBxBkJR%2FN0%2BHuh%2B8%2B%2BrHLA6SZJtOHi5rMVlawzbKWl6MK3dlr0GOqUBZOreytDZLGF1Ie6yl%2F449dH7Y%2Bn%2BmpbcfbQINzXQtPWE%2BJF1m4tz1%2FlILQ%2FizhKHjTy2a6AY6n68ySsO0A7qJxZU04J9oV060WOJdDQonkxEZF5DZqripOfNVu0j0zcI6Tb3W0qrKqsn3EEZVNBIwas3yCWxZWVYRKCm%2BJqoyP%2B%2FiU8pkDkrFaDCVKarpM8vKOUytaRTWh798ubZYce58eDI6X%2B2&X-Amz-Signature=77e3f4f7f64937641bcd554cf7dbac88b1bc30244689b57fd3365948ad7486e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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