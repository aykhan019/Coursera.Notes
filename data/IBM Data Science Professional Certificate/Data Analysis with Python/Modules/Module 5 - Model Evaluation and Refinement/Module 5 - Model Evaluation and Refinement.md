

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=c400dc97e5730be2d63e326d2cad317c1ba7091ebe029c76a6be5c124ead3f57&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=c9953fb58ea48afd706e9be3c3e7450596261c4f62099cd3b2c6ff839328a940&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=cd3da29cc3d7cd1c80a8e5645b52b48b90e406cf203295f980c9ba9ee492e2e2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=b050c69351e8de930b9e6f1131a66eccedebd70dd8ae32a3eefdbd598bd0c2c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=761d9688c8a0a807ae677d9d2d10c54f409841a8694f7586e77d8cd7a7292b84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=830deb8ef53e0af980aca6dc66bb10c61c1c1897037455c0b5614e345f9b2a82&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=048ac566aeb1591bbdb6a46313b85fabdb9947fe0305495d2c56c19c1e2de70d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=eaac5b2c62b0a4a377df38343cb1ab7cfd91b61bf270651e4b3da4f1d8c7af2b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=bca165b28da0a2dde6d58f4daa464da65432464a10eba33daff75935669a00c7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKNPKI3A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5o5DHTR0eEuKYVWnlUg%2FNRQV%2FlqP2%2BUXaJMwFJvkeuAiEA%2FscQ6EPvancFpjL5x0aSx4VrwM03NhCoRbKKXixVTwUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8QhVfEKBgR2HGPEyrcA56uWptf4eil5gHL8mGu7lVopIPfa986VL8hpQBmv5uPKpxZ2qrw4o1XpcnnK3dA39qac8%2BSgl0hDemVgo2WvzW8viU58wMkpp3HjfwOCNpKNgCzXVeKfovrskVRaJtweGR%2F29rpanqEqfLHpwUDNFb1sgNP%2BHJsO1%2BKn9xWP4mGg69mDAuXkQLxM3EUs17EYYx0aq9zVtokBChmNjXHngYjbgKaDxRYrHxUbGSYX%2B%2F41aMnluhTTU3etWVMsofMqIKa%2FqVTCgdiS75V0WImqKfWUHn3MuktPkfC4a%2BSc8qaHLAcr2CwTUqvTYBwo9PdZheEfi1JqTRtV9bKRkfksg2%2BEyUmx0BMENG8jZm8qFRU5L9QgmIWPJ71vfGNppkkTukXoZA0baOO8eBHndZBopA6f0xp9RLeJ%2BMoMfJyRcPfEEp6kuEufievPDAWqSFifJZR%2FCxgANMGIFBzewndkj2%2FAIcrHUNuj39AcuFph9jf0l0NUCiA9LAkn%2BBUCIVRwqLYZqY8w8dq5vorO2kR3OhBUaedGKwyRK78eKmvJswiJ9L4fGv3xunT353JYIWUddp3QJQD08uiaDqA9YfMynnpVcDITicHziUDTC%2BSnzAlOjNcjCLIRdJKz17XMNe9%2FbwGOqUBAVraBTHSzsLW6ZYCLxLGTSmJ%2FWazL%2FbXOCRtWWLWyo88OuHWdLmLEcD8hjNxMkcRMwPCw5ZZyX1M0hGJkzsQP9zbJNp2WinLPYWFMX176nv%2BkTbv%2FV%2FImHGbAGAFzfvDvXmOlE88kI1%2FXZ9ycGFoGQNiL3Q7m4cpl64oTPpJnEZ7v1IpUZKlu7CWYsZJzi8aEdTIrnnouiRKFqAPOG8CjRey4uMF&X-Amz-Signature=9947e9b704204c893d2ac752d746368323bde0541d1a497545e6eddef7168817&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKNPKI3A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5o5DHTR0eEuKYVWnlUg%2FNRQV%2FlqP2%2BUXaJMwFJvkeuAiEA%2FscQ6EPvancFpjL5x0aSx4VrwM03NhCoRbKKXixVTwUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8QhVfEKBgR2HGPEyrcA56uWptf4eil5gHL8mGu7lVopIPfa986VL8hpQBmv5uPKpxZ2qrw4o1XpcnnK3dA39qac8%2BSgl0hDemVgo2WvzW8viU58wMkpp3HjfwOCNpKNgCzXVeKfovrskVRaJtweGR%2F29rpanqEqfLHpwUDNFb1sgNP%2BHJsO1%2BKn9xWP4mGg69mDAuXkQLxM3EUs17EYYx0aq9zVtokBChmNjXHngYjbgKaDxRYrHxUbGSYX%2B%2F41aMnluhTTU3etWVMsofMqIKa%2FqVTCgdiS75V0WImqKfWUHn3MuktPkfC4a%2BSc8qaHLAcr2CwTUqvTYBwo9PdZheEfi1JqTRtV9bKRkfksg2%2BEyUmx0BMENG8jZm8qFRU5L9QgmIWPJ71vfGNppkkTukXoZA0baOO8eBHndZBopA6f0xp9RLeJ%2BMoMfJyRcPfEEp6kuEufievPDAWqSFifJZR%2FCxgANMGIFBzewndkj2%2FAIcrHUNuj39AcuFph9jf0l0NUCiA9LAkn%2BBUCIVRwqLYZqY8w8dq5vorO2kR3OhBUaedGKwyRK78eKmvJswiJ9L4fGv3xunT353JYIWUddp3QJQD08uiaDqA9YfMynnpVcDITicHziUDTC%2BSnzAlOjNcjCLIRdJKz17XMNe9%2FbwGOqUBAVraBTHSzsLW6ZYCLxLGTSmJ%2FWazL%2FbXOCRtWWLWyo88OuHWdLmLEcD8hjNxMkcRMwPCw5ZZyX1M0hGJkzsQP9zbJNp2WinLPYWFMX176nv%2BkTbv%2FV%2FImHGbAGAFzfvDvXmOlE88kI1%2FXZ9ycGFoGQNiL3Q7m4cpl64oTPpJnEZ7v1IpUZKlu7CWYsZJzi8aEdTIrnnouiRKFqAPOG8CjRey4uMF&X-Amz-Signature=3143887a415afb781e25fc384665c1d6545b1d36a1043b6a7626c72d2270507c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKNPKI3A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5o5DHTR0eEuKYVWnlUg%2FNRQV%2FlqP2%2BUXaJMwFJvkeuAiEA%2FscQ6EPvancFpjL5x0aSx4VrwM03NhCoRbKKXixVTwUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8QhVfEKBgR2HGPEyrcA56uWptf4eil5gHL8mGu7lVopIPfa986VL8hpQBmv5uPKpxZ2qrw4o1XpcnnK3dA39qac8%2BSgl0hDemVgo2WvzW8viU58wMkpp3HjfwOCNpKNgCzXVeKfovrskVRaJtweGR%2F29rpanqEqfLHpwUDNFb1sgNP%2BHJsO1%2BKn9xWP4mGg69mDAuXkQLxM3EUs17EYYx0aq9zVtokBChmNjXHngYjbgKaDxRYrHxUbGSYX%2B%2F41aMnluhTTU3etWVMsofMqIKa%2FqVTCgdiS75V0WImqKfWUHn3MuktPkfC4a%2BSc8qaHLAcr2CwTUqvTYBwo9PdZheEfi1JqTRtV9bKRkfksg2%2BEyUmx0BMENG8jZm8qFRU5L9QgmIWPJ71vfGNppkkTukXoZA0baOO8eBHndZBopA6f0xp9RLeJ%2BMoMfJyRcPfEEp6kuEufievPDAWqSFifJZR%2FCxgANMGIFBzewndkj2%2FAIcrHUNuj39AcuFph9jf0l0NUCiA9LAkn%2BBUCIVRwqLYZqY8w8dq5vorO2kR3OhBUaedGKwyRK78eKmvJswiJ9L4fGv3xunT353JYIWUddp3QJQD08uiaDqA9YfMynnpVcDITicHziUDTC%2BSnzAlOjNcjCLIRdJKz17XMNe9%2FbwGOqUBAVraBTHSzsLW6ZYCLxLGTSmJ%2FWazL%2FbXOCRtWWLWyo88OuHWdLmLEcD8hjNxMkcRMwPCw5ZZyX1M0hGJkzsQP9zbJNp2WinLPYWFMX176nv%2BkTbv%2FV%2FImHGbAGAFzfvDvXmOlE88kI1%2FXZ9ycGFoGQNiL3Q7m4cpl64oTPpJnEZ7v1IpUZKlu7CWYsZJzi8aEdTIrnnouiRKFqAPOG8CjRey4uMF&X-Amz-Signature=1b76e09b5677cff62307d4e8a01557b2699d966bbb333af6f41fef21ddcb77b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=c35c6a00ea61f5268f4b1811464806c77d942c99eafe494a1de7c5a344b00a47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=269c7d924e0b7a02c5a0bccb564d7d08fc31b2a7aeffb7e2fcca3a3b7e74373d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=c4463275da8195241f229ff4a3aff5430df1ce6c8ea9cfcbe7e10352b09884d5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=6319670d2a0f9e117d43ab133837305e1e69ff1e15c22e5915897ec01b735f67&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=bb619962c480c447f8e9bbc8e41a0fcd6ee3be9d980e2de6e10ab520ed854eab&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWRQKGV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVMs%2BKsI%2F1QObzxGO4QJ2mviaO8OJ1j0Aq51PJ0wHhcwIgdzycqL0yRRpp4QVjdXdKQA7EWdUDdrmkv4NE7t5WH5MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOOwI%2Fz1lUWEuBrgCrcA%2Bc9sfcdRt37kXiIqDnt4Lr3rYDGniIZZYTZggKBt%2BLGRzJHQ6WagpSJQM8oUZeWLm6%2BHETxv4tb8Mp63oKJdAa9UN9Wl3nBemONTJ3BGR6Sg9HMBzOlQ%2BaEL%2BUifaHbfq2GqoL%2BA9p5STZrGv2MwAl40X2UCFgcx078sera1vh1MNMYE%2F%2FFYLHOqD3iIuHyb5p7NBlMPG9cJKdHbZnBlM9wdu7sA2N16qJPKR2HYqzFlmBrEx%2BAINmuiHu9RbA4nO4gmgcXsJH9v9mhhcSJ%2B%2FNwMdoOzOE3%2FPpSOs%2F2Nxpe0YOQcH1wxb5%2B6rbbMbU3r3x0QyUJlk4J3lmgGX0TfcGlRIJMPhG70jsPU191hamu%2B%2BZUJniGCIDAAhPIp7UPuC0ayjiwOs773hIdLxPMGSxSfssTSAM5xUWF0G7xXhuSfaXryM%2BJyL9iiXwAVkO%2BdnaHkw3mQuVidzmypMPzUDljbW92vO%2Fj0JjvWOi%2B4b4pO6bD%2Fm%2B18KCkx2kasEp%2BjEbMOjZkblIYhsKaXNIcns6eJRI%2F4VCuZSNP0d7ODYKvhQtgT%2Bgh45bNw1Hb5ERmUUWKjfcbqKwDzAlClaqmRJbGzxmEHG56vJOCPaF2one%2F9lz2kNL4AQfXhY7yMIjC%2FbwGOqUBoWoHA7bFNSvz2vKbZit2LDjnLG%2BfplyPLY47Re7qzQYBZDBxx54m9MfrpdQAwdLfN%2Bb%2FkUm%2FX7mhjH9AM2%2Fcj8Ox3rhMWaIYlblUGXLutxGjUgc%2BkcQemMBboO6OAFhqvk0TsBI6bhOiBAoaPBNNH6MTPk0SSvqmGPu9P%2BCbmOPSz%2FSzcA06Z5dFBS8IObLWIGB59SWSI0%2BXQKEU2UTV30R3zFua&X-Amz-Signature=89813a45f6604ee35cf97108cfa5e11073c5f24792110dbf33fc8f44d5150560&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2S3Q4IA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9AkwtGTHWL3rEvH97pxC1igo06mRM3RbhkNqBNH0mfwIgClVNwpck6LXiXU0AFQ%2BRws7BTftjZdEMOUl0eBcwAUoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXGKtn3w2lK9mTl2ircA0lL0Om1UiqoGr46UBSMRSf3wp8Ak1sPtxPaQkL7jfG0WJlB52v%2BVlA%2FKY5crWY673RWnE8Z3xLJ3Yw%2FSp%2BbAQlO5XRtVTEPKNJ8yOo5VyQYhqagpOmz%2FLvWpHBDmJJWR%2F3PMRs55CcNQ2e9c8ThtVJUMPDI49tCb41ENR1n%2BP%2FHukyWJXicyDQIEkR8piFJetC%2FZWiIReNz3IGkgPPqdmWKiabJL2kczO1kyTY6mfR7rSVvIDqZc9kd%2FEoywlMA5TX7Ia20W4YWE56euZiNY2gjHEFQvaxz7DnTCpQyXxtLupuBGEoICAXIgONCZTA6fAexuNHkyI5sjl3uMbN4WwK4cEQgP9wwD4PoLtbS3Y0V1%2BK1IjHp7M5KN%2FoGzcjYYHyYAJQzMjoSstRec2bRNz93HFbuLjA%2Fdfi99WsiBjBrkw6Me8ulRcGaKrGNbUGhv%2BqbyOQjoefEQ%2FjtHp1jdsu2kXP1H1GoRykQuodEorWUSKVCsfIsUMNaAYKZcFKK46vLJbR7kMsYyj%2B5zSLe7fCKf0mM0TsEYQ%2BXxgqO6WjbP%2B0ZDSbZflxBA44clxWNTM67j7Eqs%2FWoeGXfgqezDbTbUXxy89w8hqw5gR9VFl3URCJRekAfS0K7f2pJMOe6%2FbwGOqUBLdUwEbagw8j9Sxc6m9tu510Rbw%2B7dzLmq8cUnNfc3yI1WKeqt9F6Cj5TMWbvl3hxZh7yhcqyyXr1bNhbbpaPRCn0Gm%2FA6Ru0W3LBiezG26NlGIfgCdw1G3%2FU5N5NCq50z7%2FR%2BXNcSwOcNWWcNdaZxns7cArc1PUnxwR7d51XtzsX11tQRb3fMYiLi4KlLZkKwUXLPMn16rBN5dXRWpyOJVSRNBAa&X-Amz-Signature=9f82610fa03bc5d698195b84b92c801428a9b8788ee7d3934e9dee74e65ee75e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2S3Q4IA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9AkwtGTHWL3rEvH97pxC1igo06mRM3RbhkNqBNH0mfwIgClVNwpck6LXiXU0AFQ%2BRws7BTftjZdEMOUl0eBcwAUoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXGKtn3w2lK9mTl2ircA0lL0Om1UiqoGr46UBSMRSf3wp8Ak1sPtxPaQkL7jfG0WJlB52v%2BVlA%2FKY5crWY673RWnE8Z3xLJ3Yw%2FSp%2BbAQlO5XRtVTEPKNJ8yOo5VyQYhqagpOmz%2FLvWpHBDmJJWR%2F3PMRs55CcNQ2e9c8ThtVJUMPDI49tCb41ENR1n%2BP%2FHukyWJXicyDQIEkR8piFJetC%2FZWiIReNz3IGkgPPqdmWKiabJL2kczO1kyTY6mfR7rSVvIDqZc9kd%2FEoywlMA5TX7Ia20W4YWE56euZiNY2gjHEFQvaxz7DnTCpQyXxtLupuBGEoICAXIgONCZTA6fAexuNHkyI5sjl3uMbN4WwK4cEQgP9wwD4PoLtbS3Y0V1%2BK1IjHp7M5KN%2FoGzcjYYHyYAJQzMjoSstRec2bRNz93HFbuLjA%2Fdfi99WsiBjBrkw6Me8ulRcGaKrGNbUGhv%2BqbyOQjoefEQ%2FjtHp1jdsu2kXP1H1GoRykQuodEorWUSKVCsfIsUMNaAYKZcFKK46vLJbR7kMsYyj%2B5zSLe7fCKf0mM0TsEYQ%2BXxgqO6WjbP%2B0ZDSbZflxBA44clxWNTM67j7Eqs%2FWoeGXfgqezDbTbUXxy89w8hqw5gR9VFl3URCJRekAfS0K7f2pJMOe6%2FbwGOqUBLdUwEbagw8j9Sxc6m9tu510Rbw%2B7dzLmq8cUnNfc3yI1WKeqt9F6Cj5TMWbvl3hxZh7yhcqyyXr1bNhbbpaPRCn0Gm%2FA6Ru0W3LBiezG26NlGIfgCdw1G3%2FU5N5NCq50z7%2FR%2BXNcSwOcNWWcNdaZxns7cArc1PUnxwR7d51XtzsX11tQRb3fMYiLi4KlLZkKwUXLPMn16rBN5dXRWpyOJVSRNBAa&X-Amz-Signature=6bd0bd55000a17a172fb9898e4367e9dc94726e16467c7bb21c8cd873f1dec80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVASKNX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVsDp8Ce5mySNtaeZCUNi3B7mEKeNyumAcoUMbSUnfDwIgfLQuTt9mxv37vZi5vLDIeh%2FLm%2BLTJE4SzFHdTixBRZUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQfF2xsB%2BhuNyAQFircAxwbHllgN2YLyk2%2BDhmJoV9%2B2%2BPKH%2Buc21lvgwvfZizkSjpNslWGT7Fj49kcB9epDpQiXv5FNefZPAgd5%2Beo%2BbXd%2FMMMyeEl390vRa9CsJRK1hoaDaz4ud3spq79Z7ehXF9WyTj74OXBp6ZJvZJpddLEXUtNmkmVEhKmjy1Xgf82IbpC60Zw5WFExXmDTb2yo01PX%2FecDH8jnR835VA6WkYruutzsb7VGwHquNYZkNG3rIrY9ZiKfrSp2AY7dgUgQZDRjBYDViKorI0AIpibWlNAFxhk50oqLm6pyQkg0NqzqICTW%2FcGaC2%2F1bgFyoe4%2BgVr7JiDogOHQSc%2B%2FWEdB9Z%2BDpEI4BU7atssGiE9QrxKE8gDj7pZMq%2Bj%2BabCP4hjLpC1GSZdclG%2BoGXG6Id1GLpuG%2F0Byd8cpy3rPUuoRWkKEWgcOhs8d6G7ueCnJnXaVrCZmUGD0yT96ZHLJkG8DRAPXtKdO63Mlal4sVzvWeItmoTnsrESORAkOljUjSEL4AX7yhtahiONO6gLkeeLpgjeq843AvRr6skJGT6e%2FbLubrU3iTbhFoWFv%2FCbQ9LK0A12suyTkcrP0brYeggC0e3St60B20xm%2BnWhXcmt85uWr%2BZ3xjPQFsz8e%2FvTMLG%2B%2FbwGOqUB6Idh9FlXA3ttu9mjp6vavzk%2FNJej2HE1xdpzTDMZk%2F3eqizE1Hc7D2%2FkVdWtruRY1iUfRgnPjX32VZ0TKQWLrZc%2B577kyYBl%2BUyZyMca4HXl8neNFDPGaTJURsj6UypQUhPcdxWRAu8pq2ADChMNI%2B9LA2RDU9H64gmv6F%2FR9htCe66hOUUySDTtgjsHPh%2F1fml0nD%2F8khlFx9UOWwJUGsrzBy7C&X-Amz-Signature=2c65613ba0b1073f94df2e971c6070b46de08b4c51e6167dda62e9d15ae59b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FRFSWTA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU1l7WlaG6w2EgXL3OmM5mRvYPJ8I%2FZpvXlP64cuSKsAiEAihwfUfR8Ghd%2Fk8VC7yjm2IppPt8nPa6%2FhtMVudXsDcoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObIqojGhz8xZu6HyyrcAxe4Sx%2BR4xwwlr%2BKg9%2BZ3Bmvvb2uiaAYps1eLhfXzyJGye21lFkjpLFmI1jgpK%2Bxzj3DYtU%2FkzLhWQC8ZmeNPMD7W3G0SjqvL2czPiWNQSY6bxxUG%2FGNoV5NCP0UJWPRykwzhzVlGMMS4vlsDY%2FXlezx6Rn7eMX8oqtiRaYkDAMVkWvwbWxD89ERKmDwNbuVifBDL28M37Mg8cpcP0PJVXUdS%2F4hzxQRWbg8aDYv%2BSZguJAKXQLW1EsCJFmCPt8coDrWWdK%2FI4mb6BqWwgzDUhcQuXzgz9CTdPtAaqNoWJC%2Bk8L911uRogOpfMUH00DbctSpQDzPG1Ftt59JMy7FHpa9UxJosSRkVo4kAfcYC%2FBLpG5TlvfTkMHYL2klo4ZQeiBdxS%2F5%2BlFdcidjk33zUaVSwusy7EK%2BKPUbX3Yxx0P9h4LQm%2BpcEmpoK0boUvO%2F3DpYI7rsQxCrSwCBBmr8m0PhPoQz45Y%2BE5PKhy6Q%2Fd1fOWDT26tkwfXn3HvnY96AMyf%2FnpTr6ECK%2FrBaqvs%2FCLmrhVuWhYUGjqMN9gPZUudRMVewXuZQY6hZIO2SEsKpGQYK1hGJDqrsxfpIzTfSKUbfmQaesRt7AyJIn4CA7ptZjezh7kYI2OdN94eoMNm4%2FbwGOqUBwqPu24BF42PQRgVUqxhXzPQJbuUymEhVh6KBuqajMrfRJSMbSpQiB1aZPsOXpooWWGBHSxBhBEdv1mkHsTb0AuhVvOzte2Bup5TVenWCphjDq0Inq2hlRF%2F2R3sTbsDt%2FpJmoN%2FY%2FMaC1xuaxDvEYa6WLlMocKhmXMKA9tUK9Ef5LgpZN%2FfTGOnUYAJmpCKEor2%2BgdOSPBfMs2z%2FKjzoRg4lGCuz&X-Amz-Signature=809d3237ec16e02b6f8005b6afe539125f5485d8c39b977c947b3c8efd3ad926&X-Amz-SignedHeaders=host&x-id=GetObject)
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