

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=187ea19420d24f2178cb066de580a011c16f574c53d92afa2e55a2d11e816a9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=eecbef670f45ebfdbce11d45c605655ca01ddfe97cbf7bfe71f846445ff233f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=a00330e2f9a548792c99615f14a9a35c07f58365f6bc0045ddb371012a242570&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=ad76dd2da41e956c0fc7ccba7c4ab80d23a7c503ff0fc71a70ef67def6a695e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=26709ccc834d584e408ee1511ca1c9abca01c06ab9c0199283acebb4342507f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=57b746f5d3abf95d65648bf141cd7bc89d638293a3d193dc545edf274bd86fc5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=c9ff4cb394c11e726c1ae3d3783c98e21709e9742ecb7cf1979faecf13c90051&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=20b25671496de59c5462c2401a582ea6866163bd1b870fdffd4db686afb411e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=945947213029607bfb2257ebfc667b127d1f459c73619bc94d7e0ef7e664f26f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6EWW7G4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg5nRXQIfivC5I4UbA3%2BXPzVlulO4iYoP31xIsbumvHwIhALVPcUQL8dRG9nIewD2SxTAj7eVVBEfaf6n9aSUhnmsFKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVsDF%2BQhisz%2BhR%2BiMq3AM%2BmsCTRiA5HXw%2Bpd2sqYURtYJtpBBuyMsoMe0LRcQ%2BI1e9I3JkupgVHutKkLPhiD2BpPcRCkMR8gPCdQ91h4m0XtkptuWgRc1Yvk8eomJzJaI7RgrkoR7P1rvJlObgnBb293V3jEqe1caWjYGiwunT5o%2FNdPYoROA7rV586ZBSsivu8x7baZeKc8%2FqIf76VnCuR49j2DxPNU7PSiqzAVVd3T6TZCRxy%2BfrR7FYmn5LQVYc33%2F4UOGM1I3hwThoAge99YhW84BhYi5M2VjToTwYdRgrj3q6SvMk26WD93sT6z06cpwYgVL%2Brhm7AbkiSxQzXPJWeGNaEJVkD1lTxetM8fLcq03WgSkkeeqWgUBo8pG6znmY0fqSg4jCUh6KV0cPKmoCxTNsm48fMxJ1O%2BXa7%2BAEkWaaGNcL4WPMc1J1wFBAF%2FmNgTTwfdqHf5DhFk%2BDi0vEKp5t%2F%2BGFDTMQfjdxpijMGGot8Xruz9TFTGZlTQfE2irlXCKjpUN%2B8dpNahH%2Bmstf6NF7ioTLf%2FR5aSyv1liojw1rF6nrZYtk3Gnvp1yqSXZTqoG0oT92vV5His2M%2Fz9vGPtFW0cxSuVYxRmjLufNnWPoPkJI5W9h33Tk4YdulzEzaMN%2B%2Fsm1FjC43u28BjqkAeQp%2FQAkWRTEtWMLXY%2BC7IJHuvs7oWf6kOApV%2Fpp8XDN40GnRJmN8lG5NUtRNozQqovgHyR1vUh6lnWsoAh0orSbbgIlWNkBeujkCF5t6tXvSH3o9gZbbjVZfhWpRrz4DEm%2FgB5Dn9S0TG%2FYSMyMQT4ATVSd9kNVINJAUjgM6QErkxUAYYdJQD%2Fvc8010uu3mkp2P6Mee0I4zdZDTtEh3vwlZklB&X-Amz-Signature=d3b623eb305f912a0ba306746bb14ca575a96c95afe403ddfe4dd7bab6b44d1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6EWW7G4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg5nRXQIfivC5I4UbA3%2BXPzVlulO4iYoP31xIsbumvHwIhALVPcUQL8dRG9nIewD2SxTAj7eVVBEfaf6n9aSUhnmsFKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVsDF%2BQhisz%2BhR%2BiMq3AM%2BmsCTRiA5HXw%2Bpd2sqYURtYJtpBBuyMsoMe0LRcQ%2BI1e9I3JkupgVHutKkLPhiD2BpPcRCkMR8gPCdQ91h4m0XtkptuWgRc1Yvk8eomJzJaI7RgrkoR7P1rvJlObgnBb293V3jEqe1caWjYGiwunT5o%2FNdPYoROA7rV586ZBSsivu8x7baZeKc8%2FqIf76VnCuR49j2DxPNU7PSiqzAVVd3T6TZCRxy%2BfrR7FYmn5LQVYc33%2F4UOGM1I3hwThoAge99YhW84BhYi5M2VjToTwYdRgrj3q6SvMk26WD93sT6z06cpwYgVL%2Brhm7AbkiSxQzXPJWeGNaEJVkD1lTxetM8fLcq03WgSkkeeqWgUBo8pG6znmY0fqSg4jCUh6KV0cPKmoCxTNsm48fMxJ1O%2BXa7%2BAEkWaaGNcL4WPMc1J1wFBAF%2FmNgTTwfdqHf5DhFk%2BDi0vEKp5t%2F%2BGFDTMQfjdxpijMGGot8Xruz9TFTGZlTQfE2irlXCKjpUN%2B8dpNahH%2Bmstf6NF7ioTLf%2FR5aSyv1liojw1rF6nrZYtk3Gnvp1yqSXZTqoG0oT92vV5His2M%2Fz9vGPtFW0cxSuVYxRmjLufNnWPoPkJI5W9h33Tk4YdulzEzaMN%2B%2Fsm1FjC43u28BjqkAeQp%2FQAkWRTEtWMLXY%2BC7IJHuvs7oWf6kOApV%2Fpp8XDN40GnRJmN8lG5NUtRNozQqovgHyR1vUh6lnWsoAh0orSbbgIlWNkBeujkCF5t6tXvSH3o9gZbbjVZfhWpRrz4DEm%2FgB5Dn9S0TG%2FYSMyMQT4ATVSd9kNVINJAUjgM6QErkxUAYYdJQD%2Fvc8010uu3mkp2P6Mee0I4zdZDTtEh3vwlZklB&X-Amz-Signature=24c51fd13c4267572f14e9a4a648b679a8d73d1eda6d38a9a34639a027397d4a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6EWW7G4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg5nRXQIfivC5I4UbA3%2BXPzVlulO4iYoP31xIsbumvHwIhALVPcUQL8dRG9nIewD2SxTAj7eVVBEfaf6n9aSUhnmsFKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVsDF%2BQhisz%2BhR%2BiMq3AM%2BmsCTRiA5HXw%2Bpd2sqYURtYJtpBBuyMsoMe0LRcQ%2BI1e9I3JkupgVHutKkLPhiD2BpPcRCkMR8gPCdQ91h4m0XtkptuWgRc1Yvk8eomJzJaI7RgrkoR7P1rvJlObgnBb293V3jEqe1caWjYGiwunT5o%2FNdPYoROA7rV586ZBSsivu8x7baZeKc8%2FqIf76VnCuR49j2DxPNU7PSiqzAVVd3T6TZCRxy%2BfrR7FYmn5LQVYc33%2F4UOGM1I3hwThoAge99YhW84BhYi5M2VjToTwYdRgrj3q6SvMk26WD93sT6z06cpwYgVL%2Brhm7AbkiSxQzXPJWeGNaEJVkD1lTxetM8fLcq03WgSkkeeqWgUBo8pG6znmY0fqSg4jCUh6KV0cPKmoCxTNsm48fMxJ1O%2BXa7%2BAEkWaaGNcL4WPMc1J1wFBAF%2FmNgTTwfdqHf5DhFk%2BDi0vEKp5t%2F%2BGFDTMQfjdxpijMGGot8Xruz9TFTGZlTQfE2irlXCKjpUN%2B8dpNahH%2Bmstf6NF7ioTLf%2FR5aSyv1liojw1rF6nrZYtk3Gnvp1yqSXZTqoG0oT92vV5His2M%2Fz9vGPtFW0cxSuVYxRmjLufNnWPoPkJI5W9h33Tk4YdulzEzaMN%2B%2Fsm1FjC43u28BjqkAeQp%2FQAkWRTEtWMLXY%2BC7IJHuvs7oWf6kOApV%2Fpp8XDN40GnRJmN8lG5NUtRNozQqovgHyR1vUh6lnWsoAh0orSbbgIlWNkBeujkCF5t6tXvSH3o9gZbbjVZfhWpRrz4DEm%2FgB5Dn9S0TG%2FYSMyMQT4ATVSd9kNVINJAUjgM6QErkxUAYYdJQD%2Fvc8010uu3mkp2P6Mee0I4zdZDTtEh3vwlZklB&X-Amz-Signature=a2e6634e716eb2c2f19b75c2170f1e0d3a00a111e5c58430d6655d228e7755a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=c9c68a3d21c948921ecd225e9c331a8f9a2bebc4c639679a0612e4561744c528&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=4ae06322f975b3d18aa8210d0aa5271aebf7c8931212b6c496911be30ba4c0f6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=78d5e0923a0ea3bcfd83a66401ff6ae47e0fe13d40626714432cea36c6812446&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=95acc00af4cfddb23bfdb77395db93a81dfb4ad3e2667450dc596be38f69fa9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=3b5d60a0c3c0e14d6d22870847e41385b4ae18b6ba831241598f8050c057275b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CYUWDDP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2e56e43VyeR%2FqJB6ReK5SaDcet7VGOA0OpfBMmr%2BhVQIhAO%2B%2Btf4aXNEol%2FfpyCwIbynHFvZ0D%2BX8IwnZyshFTM1EKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTdxL0KNvOTMSDnUMq3AM6fVnVgl1kHjDRTMqQe4b368vKoDbnSET1p6Ce2OvNeLIk4bQtJhZN2%2FyyEWfzcGji%2B6r3bjqVHbwxkWCFsYjw%2FtKIOueT6MgI4HNtAXb%2FE7wEpC9WMMkOOS0QzEy0TlnX0jzs9W11rohAOUS1vVBKXJLtjSgSjlTxGaSyqW71%2Br7B6npawWr486ImSnjBqkS5ZjBh3ZXigGvB5OegBRXoi3S6sT5zcMpksb%2F3209unuAscAkH8h7roLoZPzhydP5jiJG%2Fffn3cuzbtY4KuI07Rkv5X2pNGkAdn7fD6Vf4UvOxghmqUj0cEqC5jYed%2FdgJbZW6LasEyOgqGD%2B53X1Dnf56nfCbpXO3TlcquAzkcFbYA8dU8Ko0xTClJwgsV8LdQ5Z6xdxYbioHeC%2BMbVAxSPkyJaYF%2FbzPNm%2FNy01sa5EMvCUwESeV9x4MHe5yCF7BnTc4n5DZK71P4q4iR1QQwxOQCFFrcCrI239O74Ot7T5dYzEGiszcFucjjH0bVXvFgS0Anzcelua08JCAO85eiG8%2FT60%2F2x7UAGKjfOFDeC7AE4E8U%2Bm7VFGI%2BDHPM0VB%2BwanII1TP3WaQHVTstz%2B6jh75NK9FOlZfFQxDwHablUXGVlM5wv0HWRaoTD33u28BjqkAS9PsZVQYA%2BCbtHcJXpoANIsjVkrYsVCGkXs4sNrLbuD6loxOWW4HjG0bxh3YjaGt0berqCdhXtvMjIlyvBjCCm%2F7CxpCbcZUoqUZ5D9Kj0XrzX7hNVbGS%2FJmulX90Ej0UeYYXnSQWuWwrdd5SntZeJvyiy5UYSPiTiY962FMGatCUmOiTGAzcqcooRUnsdnw%2Bp3%2BlHgaRARgBdNFkHULF1kZ%2FEm&X-Amz-Signature=4701331ed20a9a330aafd37da4d5d365f2bbaef5bf53a7ad24c044a736ac85e5&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SMHOJQM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgjPKdgLItZexOtB%2FNmIbyOLI8WOaFvu25ZZqs0rb%2FkgIgJluEzVjTYhoYWULueLuG84l%2FxRrth4ucY6jWacmWcEEqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLz98%2FK6Gu0L881bkCrcAwtHwRCA2akI%2BmIAgdQL0fpVH9Lb7cqXDitydjQZoERyNHZhsuCjDZopcrhXYQKN%2F5qjT9RG1xtnjKHYCNi513EpkGTq%2BLlCwOGF%2BK4dgsrQ%2BG8azJKfGfR%2BpS%2FhN5c3MsrdMT96bQ4HGqL%2BJZfot0ev%2BpUtKy0GMGJ8eE2ZdNT62%2BqsDIJWmLscT%2FiQGyFP%2FZ7dMerbh6OOZ77lFMScZ6YRFNY0qCKzemnkRwBXPQCALWKt2qEK0WYTuvzvoM10Jfa3dEr4rl0cohc%2FGCauaap9YfRq12tNwVatQnP%2F15sJUYHQY6BXcPQ4GF3n3VzJWC9SL9xLJPGvl5XiRh1jBoGTHkwkas1YUGTDRKX%2B7ucCKGzMhF3%2BgcnoM09dPAvvOhNsz04UO9pgLCCq%2FdJhX6nn%2FLpcdu7662HEea1eXDdKqeHOWo87vzycgzVdwImGI029sa6tynLe3pBTecn9RiXkiQZBvP%2BJGBwfDCtRvYbLSKJrY9LkKjQgOd15bRH3YqQXifSE%2FTBgJ20r0XKpjxgCHA70NpYsr3KzmT%2BTeqMr3glbq8YdgYIG1PuxZyY5zmav7IVdPyz%2BOba8i634zP8Wavi82AarHsRRCL6AcXpBB1%2BoqYmhJwKvCP8LMOze7bwGOqUBA7PK7Wc0AFVTX8P4Uvm1irlLcZXK7dOesbGfTRlu%2FUPy1wkNvplvr%2BPJXNIEG0wEEEODgxrF0kIWY6Q55If0V%2BtHIJkrzfPfP4e8Lf2aUK4uUq2B2YYbe8VErLMNV2d30DE1rhPq5N8fUEGhw1AufOGw%2FOiJVh2d%2Fgc2DHoC22NXM6uvAvPoADXVyZ%2Bi8JsMmoV9hjJn1XRNtorx1XkyvJ563wy9&X-Amz-Signature=cb3a9e1fd314addb1ee7332f88bd60c5858f219ea432ebbacf45c06280159a1d&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SMHOJQM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgjPKdgLItZexOtB%2FNmIbyOLI8WOaFvu25ZZqs0rb%2FkgIgJluEzVjTYhoYWULueLuG84l%2FxRrth4ucY6jWacmWcEEqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLz98%2FK6Gu0L881bkCrcAwtHwRCA2akI%2BmIAgdQL0fpVH9Lb7cqXDitydjQZoERyNHZhsuCjDZopcrhXYQKN%2F5qjT9RG1xtnjKHYCNi513EpkGTq%2BLlCwOGF%2BK4dgsrQ%2BG8azJKfGfR%2BpS%2FhN5c3MsrdMT96bQ4HGqL%2BJZfot0ev%2BpUtKy0GMGJ8eE2ZdNT62%2BqsDIJWmLscT%2FiQGyFP%2FZ7dMerbh6OOZ77lFMScZ6YRFNY0qCKzemnkRwBXPQCALWKt2qEK0WYTuvzvoM10Jfa3dEr4rl0cohc%2FGCauaap9YfRq12tNwVatQnP%2F15sJUYHQY6BXcPQ4GF3n3VzJWC9SL9xLJPGvl5XiRh1jBoGTHkwkas1YUGTDRKX%2B7ucCKGzMhF3%2BgcnoM09dPAvvOhNsz04UO9pgLCCq%2FdJhX6nn%2FLpcdu7662HEea1eXDdKqeHOWo87vzycgzVdwImGI029sa6tynLe3pBTecn9RiXkiQZBvP%2BJGBwfDCtRvYbLSKJrY9LkKjQgOd15bRH3YqQXifSE%2FTBgJ20r0XKpjxgCHA70NpYsr3KzmT%2BTeqMr3glbq8YdgYIG1PuxZyY5zmav7IVdPyz%2BOba8i634zP8Wavi82AarHsRRCL6AcXpBB1%2BoqYmhJwKvCP8LMOze7bwGOqUBA7PK7Wc0AFVTX8P4Uvm1irlLcZXK7dOesbGfTRlu%2FUPy1wkNvplvr%2BPJXNIEG0wEEEODgxrF0kIWY6Q55If0V%2BtHIJkrzfPfP4e8Lf2aUK4uUq2B2YYbe8VErLMNV2d30DE1rhPq5N8fUEGhw1AufOGw%2FOiJVh2d%2Fgc2DHoC22NXM6uvAvPoADXVyZ%2Bi8JsMmoV9hjJn1XRNtorx1XkyvJ563wy9&X-Amz-Signature=612d7e98270ff0f1d7d535e69583444e674623d49e26b14ffd9ccd479c451266&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTTH7L6M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxbw2jVm7SD8KNaABHPBtXiaH7RZhQjPtVq4Xw9QepogIgCxNAZQ0PXJWcMUw5vpprm1BwxlFBBt3SnV3tjetmHDgqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOI2oYBjb52UBW7PGircAxS6uH6QRJrNnTQ1sFttsHHu%2BmqIERPYIWeK8HWu55saavZoCDWG3X57C69KolzBGwBPSBY13gku1puL9yKiOF6WOMazEbhh0XZ13t%2FXR9gqhVJDNqQZJaV49u2SVC7rWjkvNFsAPGv3lNnZ%2FRdjjcDaq6llqSNIixdsgXwnLS1NNtA1aN01SRakFqvpm8HC9150HLyr13TrNbEVdZC2vsqTmugtULfaXvao0trKP0FJcz4Mso7kRoVumBWpbd76l4LLOWcds8jkE4iHDu2dEvkJxDgs6bm%2FuTBRGW8h8PsdHC1HdEziZgEj%2BdL%2FO3McOEpVVNDE6GpgVXzwxzj2McDvbnPj0tmL8cebC7zqlMJ%2FUfFrHZYOsbgARLfnrhcRJC%2BYTYgcYnDfvLer3ib1BPeuGZFLpw6hWmVYLDVd0kRtboROfnmYNyUZZvmT7%2FNWDt9PPR%2BTyrIgnUuZARi1fmnIv24sKyY4r9Dtf2gS6xs6Tt53%2BRFzZgkrucD%2Fesn73qQZ6S%2F87piLCIYz2dFz6SrMtWfxXm77tZwzT2yLNeQOKmPpOUNIVGBh1hOFayolhvXmFNYFsIM4Cv%2BK7waiM9w03WbzhCQfpn2iqPakXpv45VtsEOO%2Bt8mYQUzbMOHe7bwGOqUBxtLe3u42ccInR4ChEWSKurgUS%2FU66jPpJe8yGInY2ep4zogtcskg4U3BxT71t24FTRTNr2hgqNht6Go7AbGfklYfuafWeNw3l%2BIJJD6gpMhDBeBqj5IKS74NyDBIbyWbmuQq8yoQL7yGkPreCpAGQPU7fw8%2B%2BBlX8T%2BdRndiWbHzqiwDn5sKl1TQ7hw54jty1s7InEYgMyJjxpRoRcSyhfbeuVCT&X-Amz-Signature=c558fb2ca9b50f62c1784319b074691eb8de2ca2b3f796bacc052981f9529477&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TED6BV4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwBHqc75MPwUDR7U3aQaj3Cl6BrUZzjF%2FUTEEEU%2Bq3AgIhAIlCU9kSbyKPIQOjwqGNjJ1ra0Ve2KRYR8D78RhMSIAnKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySCdxU0oPohybn08Aq3AN3LqFyUe0I2A4oEl1xZzRAAVF34IeptcogNpwqCayRLljT%2BrSVHiFeEHraCIuBGcuIPznxvzSjDMj1okLFn3OC91QYldw9abvdNFw0LBMe4bNxR%2BtoANvzqaWtPiJM4GEU6uOjcguzMyysDo7j7H%2FbNCOolCaGte7peUG%2FVcK%2F58XinCfxQe794LuxjPb%2BC7ioiEyjLnCiuDDhdCnai1Ki2g4E4tNr3WB9pgeAOS1Rhv0tBXCpVzWKbM5e00KEHbUGe6BhdGpZpcsCSVKLX9ixk9OX6zsDpApv5Dy6xzInWaDSNtsvwkQDDxUCcvke3PzhL2ELijDu149Zwy8u0LkbJQcDWFskarm3lG%2FzNCdeWZLu1NTIss37dmQZIcDXnp4U5t2PuUTkCadwkCjltgxM1xtNukBB85Jw2QaHmybrpKNK26YbsuNLDhuwzecYvQoGuIsor%2B85eNN9EY5sID4BM%2BvOxBn0Fb0NxK33LlL2gCThKHtwmlO8FUIkkmHt8zW4D8xEKTuxNBZtUvI0JT6MYcDgtqCGNFeUVTkuUkvqIcJWU9SYt2wZ1Ojntego4NAJ6elxGt1gk7tBu5tO%2BYrexM09a6YXX5Je67Wslpp0ygTSeeP3vldUy5b7XDDs3u28BjqkAVAKMdhpjUxwxfVV7m40f%2BPtfM5Fs%2F%2BBGIzdgaK3f20KKNvct05SPvpmny7wxqssD4FwyqOQv5U7GJSorNygKjf5p44djtHD7%2FGN6C0icj28aTiARRTMXpq6YpLwTi7kaqZZw4j2%2BkfVXe4LJodOQrhC%2BTF9Qq3Wa%2FeBA4TJsr83d7CY8O%2BnGu5Kqjz69WqQP9SG3w96tm2lxXCxTCnJ69T5QEwN&X-Amz-Signature=1a5daddfe9dc0b4a5edbe4025e281159a3d0789c8808dca29edd969825d5f51b&X-Amz-SignedHeaders=host&x-id=GetObject)
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