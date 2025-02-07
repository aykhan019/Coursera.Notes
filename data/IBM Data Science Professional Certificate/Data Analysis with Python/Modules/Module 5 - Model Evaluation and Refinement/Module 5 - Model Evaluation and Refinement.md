

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=1170b99d0638ba7928762d2abce8d74da33799d78ffa3cc049b0491d5efa1468&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=373f9e374fb9f2b44c42d0aa4107dbbdc2ec3bb83c170fc228cf17628777cd9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=27046cbd4bd0e893f26af8ad024062b18fd91048cc88f288e0e9abc867af0c18&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=b734a14b5b54b7b18829ffca60a93f1775595d3688540e38505aaa1569c00dce&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=8a414828c838962d263bf3f1c6541c78c0f2dc22ab45ca6e7f440c04cec40d36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=18c3fa8ffab6d69645c05f4be34936d9edc45c6d057c9f0aee53dd05fe003d2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=c78c76197d9f4f1cccb92ed7d5f537e8c6054afbcee3b7bacf1a240f6948d25c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=b0e002cb6c62cc790e5c8f8ddbce814c257fc24162c72a86be1b591c3584520f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=abb5dd2b3914eb044705f715633632817d97841bad4343220c5ec7c9e5b79850&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BB5BII2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIH5M68nsaDZo7kr5TXDSRLCLC3y2KaaijGM1jNAbrML2AiEAu6GaWzMVNBUXxQc0afgEPxg7nWKIuBSCjTdHkI253kAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDA%2F8hpK1mxBlpOOr%2BSrcAwB0BEoaY3hvX%2FrfeQVDkJQpzE3jthFNaHpcYVuOrOdwAgrv9sAx%2FzVhtG6AhdAFGrHJlqT5qK8qOFGn9JiZ5HEWfo9pmWPLQi5VusxqbwABJCuyNPaeVbMjS6JVaEwm%2Fzrra6nchcIYvAiE%2BLh5%2F6dZQ0308E9%2Bq%2F5IpeHHJaSmY0CkbTCmRbICs%2FhTcmA6I5YPov5F4LEhtjHBhS8NCMbJ55z2rcHAWVb26Vd%2BdJvGikkP1RWU8qs6DnI3vamQ3J5gpCQ32Oi1yuME02zyIataZXDB%2FOW99geV2u8ut5Ude90dmSuVca2CE8wF7ZHAWxuUpbSc%2Bihr%2BQobQqcgLwBzFW5h4rON8Q7sES7GDInUIThyTeQzdFMTDhzsExD%2FviB0ndFWm%2FWGIQB4S3KgVIQxAuq0TEZkPSlWYa1gFkOpty2TjW9UedGt3DQWoPm9j42%2BRCdln%2BasH2KL4XVMhcnTbOOUGPuVS9zSGxCUyokDzOfvZjkFb6jDN%2FAePrqlEuEc3SXVEdnJiN03hOqN2vyNLWD6OU8JIde7C4nUEgKwlbBpiDHr2g8UdHgb9CPytBCKZE2elDp12jl740HsSjJSkJ4pTili0L7dieLvuGsCqbWNyRV8rVmdGlciMLfSmb0GOqUBIvyMeZPCOnijwkaYBbGmZt6Uv2PLht1cciaHEWYSaLNxrrISau996199GylCxXkAe6nteF%2BgyipstqDxWj%2FyFFRwWjYf29JX1tHF3rUXF7lqMUyOcEPCFVKcHWAyJdg%2FK8kQF2c4%2BbzO1NkGwDCdT%2FhyQdwrCCpx6TA2O4dUPQzvDFnDz2eycMe4LFcmaVukXWri%2Bn0pJYe%2F3fbgBYVRG5zxT%2FHd&X-Amz-Signature=7a08f0f6e1ed4850fbd1837baa5a05c3bea457677c0f94b71324176d941f72f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BB5BII2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIH5M68nsaDZo7kr5TXDSRLCLC3y2KaaijGM1jNAbrML2AiEAu6GaWzMVNBUXxQc0afgEPxg7nWKIuBSCjTdHkI253kAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDA%2F8hpK1mxBlpOOr%2BSrcAwB0BEoaY3hvX%2FrfeQVDkJQpzE3jthFNaHpcYVuOrOdwAgrv9sAx%2FzVhtG6AhdAFGrHJlqT5qK8qOFGn9JiZ5HEWfo9pmWPLQi5VusxqbwABJCuyNPaeVbMjS6JVaEwm%2Fzrra6nchcIYvAiE%2BLh5%2F6dZQ0308E9%2Bq%2F5IpeHHJaSmY0CkbTCmRbICs%2FhTcmA6I5YPov5F4LEhtjHBhS8NCMbJ55z2rcHAWVb26Vd%2BdJvGikkP1RWU8qs6DnI3vamQ3J5gpCQ32Oi1yuME02zyIataZXDB%2FOW99geV2u8ut5Ude90dmSuVca2CE8wF7ZHAWxuUpbSc%2Bihr%2BQobQqcgLwBzFW5h4rON8Q7sES7GDInUIThyTeQzdFMTDhzsExD%2FviB0ndFWm%2FWGIQB4S3KgVIQxAuq0TEZkPSlWYa1gFkOpty2TjW9UedGt3DQWoPm9j42%2BRCdln%2BasH2KL4XVMhcnTbOOUGPuVS9zSGxCUyokDzOfvZjkFb6jDN%2FAePrqlEuEc3SXVEdnJiN03hOqN2vyNLWD6OU8JIde7C4nUEgKwlbBpiDHr2g8UdHgb9CPytBCKZE2elDp12jl740HsSjJSkJ4pTili0L7dieLvuGsCqbWNyRV8rVmdGlciMLfSmb0GOqUBIvyMeZPCOnijwkaYBbGmZt6Uv2PLht1cciaHEWYSaLNxrrISau996199GylCxXkAe6nteF%2BgyipstqDxWj%2FyFFRwWjYf29JX1tHF3rUXF7lqMUyOcEPCFVKcHWAyJdg%2FK8kQF2c4%2BbzO1NkGwDCdT%2FhyQdwrCCpx6TA2O4dUPQzvDFnDz2eycMe4LFcmaVukXWri%2Bn0pJYe%2F3fbgBYVRG5zxT%2FHd&X-Amz-Signature=73ccea600ea0fd041f8fffc3d278ba7b62309f2e51cc84f3fc9a72f1eb29e825&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BB5BII2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIH5M68nsaDZo7kr5TXDSRLCLC3y2KaaijGM1jNAbrML2AiEAu6GaWzMVNBUXxQc0afgEPxg7nWKIuBSCjTdHkI253kAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDA%2F8hpK1mxBlpOOr%2BSrcAwB0BEoaY3hvX%2FrfeQVDkJQpzE3jthFNaHpcYVuOrOdwAgrv9sAx%2FzVhtG6AhdAFGrHJlqT5qK8qOFGn9JiZ5HEWfo9pmWPLQi5VusxqbwABJCuyNPaeVbMjS6JVaEwm%2Fzrra6nchcIYvAiE%2BLh5%2F6dZQ0308E9%2Bq%2F5IpeHHJaSmY0CkbTCmRbICs%2FhTcmA6I5YPov5F4LEhtjHBhS8NCMbJ55z2rcHAWVb26Vd%2BdJvGikkP1RWU8qs6DnI3vamQ3J5gpCQ32Oi1yuME02zyIataZXDB%2FOW99geV2u8ut5Ude90dmSuVca2CE8wF7ZHAWxuUpbSc%2Bihr%2BQobQqcgLwBzFW5h4rON8Q7sES7GDInUIThyTeQzdFMTDhzsExD%2FviB0ndFWm%2FWGIQB4S3KgVIQxAuq0TEZkPSlWYa1gFkOpty2TjW9UedGt3DQWoPm9j42%2BRCdln%2BasH2KL4XVMhcnTbOOUGPuVS9zSGxCUyokDzOfvZjkFb6jDN%2FAePrqlEuEc3SXVEdnJiN03hOqN2vyNLWD6OU8JIde7C4nUEgKwlbBpiDHr2g8UdHgb9CPytBCKZE2elDp12jl740HsSjJSkJ4pTili0L7dieLvuGsCqbWNyRV8rVmdGlciMLfSmb0GOqUBIvyMeZPCOnijwkaYBbGmZt6Uv2PLht1cciaHEWYSaLNxrrISau996199GylCxXkAe6nteF%2BgyipstqDxWj%2FyFFRwWjYf29JX1tHF3rUXF7lqMUyOcEPCFVKcHWAyJdg%2FK8kQF2c4%2BbzO1NkGwDCdT%2FhyQdwrCCpx6TA2O4dUPQzvDFnDz2eycMe4LFcmaVukXWri%2Bn0pJYe%2F3fbgBYVRG5zxT%2FHd&X-Amz-Signature=1d28e67ef52500a2e925d976a2a27bfed51a3d5bae580e9fbff20240b48ea673&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=226b2914c93344dbfeb68ec379562bc0d540bc7352d3c966c38657d9bbd34a50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=4560b66c79d13bedca190cdb5e7409fbf1231487083a77c8306de98eb9b9e7c8&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=4816cce17db325c6b48739562e2a5095c8eaed8b973eecc585594961c164bf01&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=cedada37ea724adaaae5984c3a477813ee6fd9ebdcda7796f2934ef2f96f0811&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=c904621f5f4b1a9a20f3a67bdf377c39a87b79fc90e24ae831f49913a6b53d32&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QRDXK4O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCbRWnDLumdF64vIPcIg2itgQPcCK8BQKeIWWWMmKH5VAIgYmLmPB%2Frougnsyl78UB7OYKUOUfvQzcp5q0iltX5LmAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDL%2FxTf8v%2Ft8jxAL9ZyrcA5k%2BFJgI2E55IGGJ23pIHV0ViL1h7r7D55gG5cSO8svojUIb0Fdmph8nbU5oj%2F9EnV26NYaLXyg9fiweXUWUnODDBhWWZqr3gXhGRPeBgEyimsOeP9mSYyOjgIGxsf3GQ%2FocnWVLNLKdpEE9qvjPncXiiVzZPalLXDj6hbKyKltpnm46ZbDldtC2FFga7qFM2EsOrE4CRmSlq%2B2IXvMEnSDi9b5jA6fhdpPuCoLMV3HXnEPrQMa3jkEsxfBmwyDJDEcTPFgz%2FLpwueyWRYvbeBMdirINkR9tOjVNSRYy57Re4%2FecuRngwy3mDiANVHNrkL9qeJanbBLpeOSLlsAaslji0J2wrjt%2B1I1JK5XL%2BlD382SUpNCh%2FtUtjZP86ZunCVN%2BGuaQQPcR42hi9C7EuSaNG5p1%2Bsb%2BL0jNuVqXv3YG8KS%2FL1csqnu7Dnk%2B5okOD5qWbpACODNJifKlzr23k4GWfUU0FHl1Sku3m3BfSJQ%2FCaqSMXVmALYJnFq8a5LEYhl1ovmtQeWBeqNy1uBeT8p7wQPFdkiNefA%2FxOSYYrrmAPPD%2Fpr0jAWICV878O%2BhcKiNxj3kSReOwNyIuHyB%2BN9dQAfWr6xg7w%2FEtFsJVfEstneHsYwgG3dIQcPmMIjTmb0GOqUBcoqpeJa67uNyMUftijRFYNdftToneTIztrdbJg7WKkhGBRbj%2FkZXSLu0Re%2BBK%2BTTJSH8hHO3CUQLFvnz9EEF9aJK1ChD6RSjF3sRyZt6QNcQsM7Q43Gtw7di023W2v9%2FzBFRP3ANp64ro%2FY3NM%2Fx77VhqS0%2FXdoHeKlbAbdFYimMquJdPFrb2e45HeIF1ERydm1WXj1rqH2Z8FtI7QZRGovnbn7H&X-Amz-Signature=fa8af612870c4ba98f36e711f3af2eb2e63a0a6b17286947e8bf77927af29b97&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJXICPLG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD1wn0t8Nw1W0pdtM3wkEJ1oIq17E%2FxJjyeEkSvWeRiJQIgStpjLybalXEpn8lyB3c3Da9Q4OO4ISUHK%2BRryH9mqOYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNzVARY3UBJwefDFTyrcA9sdqEp0aq79cqmKx1fcWInMo7TeU3HpHrc2LgRbedMqfex3fPma87WdmkMlu1RAJ%2BmG6E%2FaykyHHyQ0AwgD0d%2FdEkx6fRNNWPt6DRN5YABMR5TqQxsSg8cFIyXgaVbEctglt8UjLnqbK399RSgO0u9UjM4Gm035wGM%2BqzmZfLl017MuTdMZLOzY2jAva3ybFCtDkFX%2B9M55kbCRWYK7QZw4Ki%2FZaVozGebkK4GFQ05R6ia%2BjYjGu3VbIxuFCp8OLPtY43WLQDk3kh2nEAY6Ci4B9%2BT%2Fb%2FDRU2%2FPly3vM2yso7svuKUWS0sG6f6UQn57nk31C4%2BatmiVIFZJZCiELDwbv6C6AvS8Je%2BDMUBlBakaq9qKVdvlyAoOnKUqceVveEkXx2S%2Bnpef0N8XFw60kfg8LERNmZfokViopCwFR6UOQH75ZU1xg9tio2OlQF37ioE4v7MXE9HZuRXVa18Z5tIhFLdH34LNaIL3%2BGbKJqZZ6%2FJUwuUZaga%2Bs%2BLf6QON7EoUsmOqcduYGPcZPsR1L794Yx1Poi8A4fX3ZVqTt25IG0DUuyX73Z05gVIBOQgFF0z6MH5QwPY%2B7hwRDDzr%2BLiEorc5GCOJ9gJWOKLzikwW77mbWHztBqSpSU2cMPjSmb0GOqUBbwDRwgsR8y%2BGxYYpMgPigX2vd426dpI8RZP6edmD96NCvSo7XxknkjYAvPn1%2BOuMYWPAGccZL5Mqr2NXEB0IVFXnw1pM2ZCWQgP5K95uQE6UKF5VY7azCXuLOqxQWmtZpulJasMOV0Kmllw9rBBy%2BTCsFS4SjmSHB%2BkzzwDA8PzIDLb4IBaKPLfRnqwT841JdN7P%2F9G%2FIZvSlyfAHgWTwCNXloZu&X-Amz-Signature=7a6215cddb66126739b106902cea5ec4774f273f426c3e70a6837a6ed2ad43e7&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJXICPLG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD1wn0t8Nw1W0pdtM3wkEJ1oIq17E%2FxJjyeEkSvWeRiJQIgStpjLybalXEpn8lyB3c3Da9Q4OO4ISUHK%2BRryH9mqOYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNzVARY3UBJwefDFTyrcA9sdqEp0aq79cqmKx1fcWInMo7TeU3HpHrc2LgRbedMqfex3fPma87WdmkMlu1RAJ%2BmG6E%2FaykyHHyQ0AwgD0d%2FdEkx6fRNNWPt6DRN5YABMR5TqQxsSg8cFIyXgaVbEctglt8UjLnqbK399RSgO0u9UjM4Gm035wGM%2BqzmZfLl017MuTdMZLOzY2jAva3ybFCtDkFX%2B9M55kbCRWYK7QZw4Ki%2FZaVozGebkK4GFQ05R6ia%2BjYjGu3VbIxuFCp8OLPtY43WLQDk3kh2nEAY6Ci4B9%2BT%2Fb%2FDRU2%2FPly3vM2yso7svuKUWS0sG6f6UQn57nk31C4%2BatmiVIFZJZCiELDwbv6C6AvS8Je%2BDMUBlBakaq9qKVdvlyAoOnKUqceVveEkXx2S%2Bnpef0N8XFw60kfg8LERNmZfokViopCwFR6UOQH75ZU1xg9tio2OlQF37ioE4v7MXE9HZuRXVa18Z5tIhFLdH34LNaIL3%2BGbKJqZZ6%2FJUwuUZaga%2Bs%2BLf6QON7EoUsmOqcduYGPcZPsR1L794Yx1Poi8A4fX3ZVqTt25IG0DUuyX73Z05gVIBOQgFF0z6MH5QwPY%2B7hwRDDzr%2BLiEorc5GCOJ9gJWOKLzikwW77mbWHztBqSpSU2cMPjSmb0GOqUBbwDRwgsR8y%2BGxYYpMgPigX2vd426dpI8RZP6edmD96NCvSo7XxknkjYAvPn1%2BOuMYWPAGccZL5Mqr2NXEB0IVFXnw1pM2ZCWQgP5K95uQE6UKF5VY7azCXuLOqxQWmtZpulJasMOV0Kmllw9rBBy%2BTCsFS4SjmSHB%2BkzzwDA8PzIDLb4IBaKPLfRnqwT841JdN7P%2F9G%2FIZvSlyfAHgWTwCNXloZu&X-Amz-Signature=575970fff024ca2f9844c9bcd60c011240f3d0a00ae1a6cbcf2a5cb2f8ccae43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7HMVCKT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIA9iLZHJR0ibmdndgkr03DfLdcYBOizmmFPBzLkHnX%2FyAiBZu4GHmbHTUD1YiYkgIv9gB%2FPDtp9Aj2aDXpwRwoXTaSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMy3e%2F6bIueWP%2Bv1GmKtwDfXCN3ctdsYhpEGjU%2Fj84ZpstbelukdS92wx%2FrLmLMwdCJYry%2Fm9X4xqM%2BbE0WvYlUUJKvPVdJGYCg3l6PwrWoL5if6KYQxIHBI8RXG3gQVf1i2v8i6lvTdVMtUZ3CYdBYEmNohNPebqg7V4fFLPLSK7J4a8OlPvy8Bucg%2FJf3Oufq73R81YngnIejHh1ntqpfMz5kX0OoSMQBLimWOEQBJ%2BUNcUl%2FtBSMgfglEp33Bdhynn%2FpzVPTHckcCKIU%2BTHUHZm6VlhLTtO9oGuX8Ec4QhnsFDrT7GbGQtTrweZk%2B2%2FSXKuQ%2BuOwjdSIlFKYpSUeQ34niFq3qON5OBbTt54o5Leh7eHf9aniUrvN6SfMBMB4drTCwtVExdWwfsaFkiLy1Q%2B0KKSqiRmhiRcsBn5rCQ5v5o%2Fx8R74uF5kiYLGVwe8mfxkmpnet85%2FquOnyM8Jsb2eShCauq6NvNxYn8p%2BRfKRCZLQrlOO7qweQ5TGR27%2FIqPFm28VhIEww%2BUirXToREJXb%2BM0qB2p5GZRag7WR4iuWUEoqRIWSnaB2jIfejmzGb%2FwBAn7gdaWX0c6AT4VDTdOKX9i26eOSvMhGERAWc54wD91flx4hQDYHXBv5rr54imYuti6IroUT0wpdKZvQY6pgEuQCR5p3oDOFsTr%2FZHts%2Fr5Fh1xAbQ%2FNtyzi4GaPMUI76sgY2331GxuXAX9HPw0quHzNBFx04Br5dbcfl%2FgKK485VEG6t7aYAiy2HlFzB4CqOVBxCbURyxmHNgE8nOKrYCTnodWLYms84w5h%2FeWw8AT%2F65ZdUpSlcYcp8hI%2BmYzDHffMz4CiyVPCQtBTknRZB5gPrhy9C1CDUkICSjaHeqr%2B5S%2F1PD&X-Amz-Signature=883521a110dd731f407b10f2c7cdbd9bed4b99975b311f10e0963184f76d1210&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWQ45W3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBThjng%2BbGfoJFAIhXp83wavLGdvd%2BpuqDkrHRusSuKaAiBdd9TZgvtxUR%2FKyMvQ8rqGH0O1syJ3sfkVZHdRXF6aECr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMt8aVIewnFrKgRBJbKtwDVB4Jk9%2FmV9CwiSWta0S8wOJFJFhUSJBaI9FgUfaOI3jihLyWqSPPVSORS9wDS%2F2illiuP3LiyHmvnCmSc57nw742oiHLF3BN3gT8g9JvQgi80bB6eD9PjdDZhk3PJuoIO39U4%2BVcEbIJ2RuU5edK1lWcX2Y8q4yU%2B8uCcWiebwlNpyrNye4wdIki0J4Z2WkhEvF3Wl5DlldHwflOiQTp8Ur1gF4xTMTBk%2Fkwis%2Fu8LqijEc9GG9Ygr8nXV8v0CVzTBtob1m8zTBYnvKyFug9Lub7ot2YIF806mIvDiJTsYPTqn4%2F60r5SbMtdmjWmhYb3ofrCM7f5QYXrH2jb5E4tDeNtjHoBMWzFZORyRvtKO1wxkD2yFh7Z0q7o0JS7qhcY5fCS7peE9FK1beeg9zXETJ97EWfPz8qGfMISzWyFGTPniVU%2BjzdqQOnZJz8bEpz1FAoHChAmEY%2B9LL7%2Fslf7TIGvGb%2Bp4t4Hg8KToEXXU9RcGiccqtAFVBUAG4VNLNd288%2BRyzR5LPMpdNstVChrylmAkQKInew8r1s2YleED0oUXGY2JS0AxS5KplDQ1ba5BikjJ6w49eQozF6e2HPjVhmAcsgT%2BE7Q64%2B8IRAuRY06QzfFqrVbZ%2Br1sswg9OZvQY6pgHQ%2Bs3GBrFxzqoGnPY6I%2F02zAMR8gF65wb9Y4tqLNiQdvkmY521bxgOdJW6n1%2FOSGKXYrq7yrORmpLtZL%2BrB5mFPetgkzzXYdd2kwDaETBfPTPTGpQvSZ70QxjXo%2FGCILVFpmjeIM0Sbvv1aR%2BDeFUNCPGHdjVRS6AKKt79pBvhOW716gt5rZelRLnKY5Oz2ajRZSyCovYpNcJXlNTqb2GYsaW2Fyt%2B&X-Amz-Signature=72dc55f13e424a747d84f444d06d16ba9caa46ef24149b2be50c79b6a3af6106&X-Amz-SignedHeaders=host&x-id=GetObject)
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