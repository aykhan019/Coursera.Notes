

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=36720b3fb531f1c7e5fedadf6735e314031121d5334976bd6512cf6980e0bb75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=dd22816601a797ebabaa44ddaf538c5bccdcda1e65c5164a7a03f4749aee8f91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=403a59b66cd0489c907ba7d59a0813b8b52f53aa2d3cdc00a872b02561ff6cc9&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=321e3634bd9e6cb718bed2e14649b6c5291cd19582943a72eb65443699f0757b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=28c3523f1dcbbe379d69c74f19b3a296686d56eebc4f4a09a0372eb0831e8c61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=32e67e26773030bfdc0a41737242c4b3bac57a52ce14e5bf368ec4a07d48219c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=e4f4b880fc78f7bcacc30a0266d72b20461e0cb1a5d135a4f5782db7f7ce1eb4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=1e86565a850fe69659c7490fa1c6c74c281f52eefe748f0d305b0ff1fd5e6baa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=41a9f86de644fdcfcaedb75863a22a024386e98940a2186edeb3d5a7cc7b8c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667354M2P4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeOraqLarSxXfsu6EejMa7MVjObv0n2f7VORiDBJF%2BMwIgK8iKHGsbPwTX3t5BkvyauzOUBgZ0oEeZOw1Ojhr568UqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO78I8BemZ2vqO2u0CrcAxwkwuf8RDhSNm8U4P9ZWaWcmVaf5fXx2wJ3o%2FDrzWHrJXEyOiuZjXplt35ArNxKtE%2FakMX3bNGAGwHGvE%2BE29eAk%2Fo0Vu9bNkFicQOFbXAge1Bl%2F8Hg4YXkDlVhxQUTjgEGc%2B416sVpOjE1l2%2BZEhjC1Lt0RCxT7z0uzkMjt9q5DYOW78SHHGeUJN5HKuSxowWcpS0MuBi8kNFaJUOxFPtSQPyfzibCEXrUW91Tpj2bISsM7%2FI0jS6Pp0%2FmXuKvVZRP7WxnX%2FojGYKGBXb%2FDbzqnd8W9ur%2FUvek8Jo5EVwmkODVfgAUV2p3FNqgQOrhzQWobGHPH%2FspECYCZ0ZuE8UIBm1LQ39WED1Px32%2Fsff33UesDnKOBuDeJagIMUnPJMJeGpnPbg6bLrHQ%2BgdY2C8a0QSftSkcmQwT7RSt8Qv6DCvo9JqS4qMFg6rw8RMiuL7VLYdSZZS4NJ%2BxsRBZagvp5IiefdJ1h8nDJhcg0U31GK1t2tbxdxiCSCmboBx8qlUG3wnnKhzd5Njbwijegx8UNgBDKUWPFZi1yduuJqu75Mgmvo4N2aub9cX4sBays2GTxwqgea3OiaBbbFfMMQlaZrVBjEyMnnk%2BvUGYazC6%2FBLz0F0F7g7hnUddMM7h8bwGOqUBlEmFGr%2FbMYQ4cB5N1Cr5eTnRz8m5hZ819QMJxyBLeYvs8oYJr79x5OvO2rxDEc2aRikCUJABIbuR3RtbDNX4ur%2FBlWBW1U5fEX8GTwiUUYHrJ0Vxeqg5VrSS%2Fqbyg48wMEpGzptYOwuInYgXSoiLX48F0fNdSUSahuSF84kGzbtgsCRHxBMgWzArLwImwhmiU84nbAxYsqdWy0iZLXeb9QpymukZ&X-Amz-Signature=b8bc6ac718c4d555836f1fc2f4dd18504ec61065f65b4cbe73bfde57e6a3c417&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667354M2P4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeOraqLarSxXfsu6EejMa7MVjObv0n2f7VORiDBJF%2BMwIgK8iKHGsbPwTX3t5BkvyauzOUBgZ0oEeZOw1Ojhr568UqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO78I8BemZ2vqO2u0CrcAxwkwuf8RDhSNm8U4P9ZWaWcmVaf5fXx2wJ3o%2FDrzWHrJXEyOiuZjXplt35ArNxKtE%2FakMX3bNGAGwHGvE%2BE29eAk%2Fo0Vu9bNkFicQOFbXAge1Bl%2F8Hg4YXkDlVhxQUTjgEGc%2B416sVpOjE1l2%2BZEhjC1Lt0RCxT7z0uzkMjt9q5DYOW78SHHGeUJN5HKuSxowWcpS0MuBi8kNFaJUOxFPtSQPyfzibCEXrUW91Tpj2bISsM7%2FI0jS6Pp0%2FmXuKvVZRP7WxnX%2FojGYKGBXb%2FDbzqnd8W9ur%2FUvek8Jo5EVwmkODVfgAUV2p3FNqgQOrhzQWobGHPH%2FspECYCZ0ZuE8UIBm1LQ39WED1Px32%2Fsff33UesDnKOBuDeJagIMUnPJMJeGpnPbg6bLrHQ%2BgdY2C8a0QSftSkcmQwT7RSt8Qv6DCvo9JqS4qMFg6rw8RMiuL7VLYdSZZS4NJ%2BxsRBZagvp5IiefdJ1h8nDJhcg0U31GK1t2tbxdxiCSCmboBx8qlUG3wnnKhzd5Njbwijegx8UNgBDKUWPFZi1yduuJqu75Mgmvo4N2aub9cX4sBays2GTxwqgea3OiaBbbFfMMQlaZrVBjEyMnnk%2BvUGYazC6%2FBLz0F0F7g7hnUddMM7h8bwGOqUBlEmFGr%2FbMYQ4cB5N1Cr5eTnRz8m5hZ819QMJxyBLeYvs8oYJr79x5OvO2rxDEc2aRikCUJABIbuR3RtbDNX4ur%2FBlWBW1U5fEX8GTwiUUYHrJ0Vxeqg5VrSS%2Fqbyg48wMEpGzptYOwuInYgXSoiLX48F0fNdSUSahuSF84kGzbtgsCRHxBMgWzArLwImwhmiU84nbAxYsqdWy0iZLXeb9QpymukZ&X-Amz-Signature=ec80adc892997f7bd36656bc67ded54d88aba32514fc23e83ef471afbdd31160&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667354M2P4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeOraqLarSxXfsu6EejMa7MVjObv0n2f7VORiDBJF%2BMwIgK8iKHGsbPwTX3t5BkvyauzOUBgZ0oEeZOw1Ojhr568UqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO78I8BemZ2vqO2u0CrcAxwkwuf8RDhSNm8U4P9ZWaWcmVaf5fXx2wJ3o%2FDrzWHrJXEyOiuZjXplt35ArNxKtE%2FakMX3bNGAGwHGvE%2BE29eAk%2Fo0Vu9bNkFicQOFbXAge1Bl%2F8Hg4YXkDlVhxQUTjgEGc%2B416sVpOjE1l2%2BZEhjC1Lt0RCxT7z0uzkMjt9q5DYOW78SHHGeUJN5HKuSxowWcpS0MuBi8kNFaJUOxFPtSQPyfzibCEXrUW91Tpj2bISsM7%2FI0jS6Pp0%2FmXuKvVZRP7WxnX%2FojGYKGBXb%2FDbzqnd8W9ur%2FUvek8Jo5EVwmkODVfgAUV2p3FNqgQOrhzQWobGHPH%2FspECYCZ0ZuE8UIBm1LQ39WED1Px32%2Fsff33UesDnKOBuDeJagIMUnPJMJeGpnPbg6bLrHQ%2BgdY2C8a0QSftSkcmQwT7RSt8Qv6DCvo9JqS4qMFg6rw8RMiuL7VLYdSZZS4NJ%2BxsRBZagvp5IiefdJ1h8nDJhcg0U31GK1t2tbxdxiCSCmboBx8qlUG3wnnKhzd5Njbwijegx8UNgBDKUWPFZi1yduuJqu75Mgmvo4N2aub9cX4sBays2GTxwqgea3OiaBbbFfMMQlaZrVBjEyMnnk%2BvUGYazC6%2FBLz0F0F7g7hnUddMM7h8bwGOqUBlEmFGr%2FbMYQ4cB5N1Cr5eTnRz8m5hZ819QMJxyBLeYvs8oYJr79x5OvO2rxDEc2aRikCUJABIbuR3RtbDNX4ur%2FBlWBW1U5fEX8GTwiUUYHrJ0Vxeqg5VrSS%2Fqbyg48wMEpGzptYOwuInYgXSoiLX48F0fNdSUSahuSF84kGzbtgsCRHxBMgWzArLwImwhmiU84nbAxYsqdWy0iZLXeb9QpymukZ&X-Amz-Signature=954628423e09ac7894ed047e4d232bb3e8d5f765b4e911fbaa4f67b87ec7ed0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=9de2db1f1584a85e3dd87c23510b0e5f2b3941345e7d1c5aab87aa7641892bd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=c58a8e8e16fff561ed58b376d7dddb7087c2c5ca390f563408b7347db74b077e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=6883886797431eeeba6baaf0071107247d8e5f07be20937f3aa133978dadfc5a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=0ee29176cc20aa90f5306b2c0eb29bfb400c71e34892cd4527a3dd561f923253&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=3960ee0c331bf5b6df4fac34519f3c96abdfa91204b4c8979a6c8ab0c9641d0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJQLO76U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZSnlMfyOJFyUe0EwxF80pbdwXNLWA6mvTmUAA%2FgwDqgIgC0vUg%2F1WTXUoplvxjCiVjhje9nWEwnWi6fDK3%2FEyLMcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCByz8CpVNH%2FVBOgkCrcA9sIbX79hbz1qurscigg43H1npAVw5%2BEmY7uasoYE2AjSAEiI%2BIMtzNGAfMACIPT6yK8CSmPEvs35alFAJ5%2BT3vsElcF%2BUtlHGnHfloj2%2FdV%2Bu7hJcJnV0lNmGZ9AFrdBjNHMIq5N9P5ziG19xnYIphXUhdy1W9ho29EnJs%2Fw2HwqlIOk7tUv%2Fz%2BFXqpOkP09duD3ERQLf8eV7wVXgFRvXIpwm7Uxzq5hB4mLSpcVNHpBLCm6Bkkwn3T5ON%2B42MD3NqwjO4z9PQFun%2Fh6zo6%2BzesaeKwdomgEcWD7dd9FLi43B1U2qgL5uPHRf2MTvrnbqFuRG13IZiafwSUr1l92FsRu5LU8w4f2iVzi7vHIkbUj3FzpT4PDZis%2BdbwuMxqtMlzURMoQXLfOBFkXgiz4ABuNfsGPxJdK7z3QuKtu5kspLCcfQja5zF2CLRlL08H6iqQZvnm80nuCuluRD7wvgBVMjlos2a5UYWjr73otaaNRi51qOeVLg1MR4GeuaXxMvC0qa9uDxV%2FU9231eKOSlpgUbjXSJErx98hIvew%2FHZH85qEtgowxn5z3modSDGJUavpMR5rQ5%2BUz7dfMquWPVb%2F1m3HshF05%2BaTetPYIhovXee3N6GJPpfVG9%2FwMIzi8bwGOqUBgB%2FkTmijkgpBtic%2B0Nmz2ih2Yc0qPJB2ePorBpUjmS%2Bt7PQofyg470hGjtGrySc42fib%2FZoM3L6INZaF%2Bsyv0lvm%2BMebqQUudYmb1GloeEJQ2uFbOrPj%2F0HoKtQNTMJuqEfiX%2FK3PD5EfKe87qhHhTYvBtSXkjRHxas2D6ZFDEHMLVA6B7YR8BieEgKC2HWwq%2BIpNEp9koW0wCCosBzwxOIabckC&X-Amz-Signature=4c4c4d9d0dfc82d3725d4276c9bace0f97fef9c07e180676fd8686eea494c44e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKDOFX7P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLD2Z7yCcajNC9904SNluKVhBZLcI0MGcHlskN7hZPQIhAPfv471Wz3IeEBk3G8v5RATROzWfjRjcbsuRAl6iAS%2F9KogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwURGjqFgLQNj6NvwYq3AMbc%2Fp%2BIw%2FLgUC%2F1nEdPudnROVx1OclX9bkC3ykY36ay9%2BmT3cf%2BkiTnpd8emMxTcawRKYIqKQad7lq9QzXa7pUu7e1sNwnHuNwGqNNxmWdcZ55N042OwweJGTfgYLAU6wIdRscM6E0mlodncxttfXvifeemXhNyyFwcMNwUiRVRQjligNLwzfABsi33Hcy%2BSy0J4y329Ww0aKJ1t18mzu5JUDK5%2BFzH2l%2BN%2FE4Kh6UW3K2wmko0kGmdc8elA%2BApP2s2yor%2FKmNdcR1arKUEWcZEYUacOJiHsV%2BM5ZuXvaCeAyDK%2BIedBdIleNbyFxRRqNXDBaF1qlhE%2BluCns3ZxRd64TngSh1t0grjJeFmckLFgU82jTC3lqyRvBsqMmhqPvp0JjmTqLUMVY3%2FcQ3xxUQg32EHE6YiMuiUb0C5%2BHG1c8XxTagniX5roPVkl6mbtEu7GnmH6W6qvgk1Cwngp41uU%2BKCpciGXYVzvxLGMaoaRlwAOwRkAX8Ii7hq8Koo0QXD6vX8zvrqnw8dqP6XHz9M99DQTbcI5312jsHLfMaIx%2FLDGmEaa9kKzgw2MHVqzCvGSfH7ULrp9j9XYiVPSooRxAA6%2Fp4POXF2%2F67tzULGGXeBDvSyclmm%2FhGgDD14fG8BjqkAZ0L4Xqn0pXknq%2BdBSCNO0E8Co%2BuYYC9yRtlAuSsWNqt2BY2y%2BNW67oP2yqS3AsUBA02qZKxdR62RyZLhaDBKHt%2FMueZroedoesCNVAFi1NM%2FhhZ%2B7S0o96EOUVpXJBb739anMYGL0hSWcFaEie7SvVfY4vYpGsXiXDYD33u9q5V0YW7yh7GqJNU%2FiSxBVkhUnnM7DsPukbH4%2BoTaYV1LtUmrvJw&X-Amz-Signature=6854de9b0cbcf27c33321fa65c0c43cdbda260add4fe34125082df5870d938e5&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKDOFX7P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLD2Z7yCcajNC9904SNluKVhBZLcI0MGcHlskN7hZPQIhAPfv471Wz3IeEBk3G8v5RATROzWfjRjcbsuRAl6iAS%2F9KogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwURGjqFgLQNj6NvwYq3AMbc%2Fp%2BIw%2FLgUC%2F1nEdPudnROVx1OclX9bkC3ykY36ay9%2BmT3cf%2BkiTnpd8emMxTcawRKYIqKQad7lq9QzXa7pUu7e1sNwnHuNwGqNNxmWdcZ55N042OwweJGTfgYLAU6wIdRscM6E0mlodncxttfXvifeemXhNyyFwcMNwUiRVRQjligNLwzfABsi33Hcy%2BSy0J4y329Ww0aKJ1t18mzu5JUDK5%2BFzH2l%2BN%2FE4Kh6UW3K2wmko0kGmdc8elA%2BApP2s2yor%2FKmNdcR1arKUEWcZEYUacOJiHsV%2BM5ZuXvaCeAyDK%2BIedBdIleNbyFxRRqNXDBaF1qlhE%2BluCns3ZxRd64TngSh1t0grjJeFmckLFgU82jTC3lqyRvBsqMmhqPvp0JjmTqLUMVY3%2FcQ3xxUQg32EHE6YiMuiUb0C5%2BHG1c8XxTagniX5roPVkl6mbtEu7GnmH6W6qvgk1Cwngp41uU%2BKCpciGXYVzvxLGMaoaRlwAOwRkAX8Ii7hq8Koo0QXD6vX8zvrqnw8dqP6XHz9M99DQTbcI5312jsHLfMaIx%2FLDGmEaa9kKzgw2MHVqzCvGSfH7ULrp9j9XYiVPSooRxAA6%2Fp4POXF2%2F67tzULGGXeBDvSyclmm%2FhGgDD14fG8BjqkAZ0L4Xqn0pXknq%2BdBSCNO0E8Co%2BuYYC9yRtlAuSsWNqt2BY2y%2BNW67oP2yqS3AsUBA02qZKxdR62RyZLhaDBKHt%2FMueZroedoesCNVAFi1NM%2FhhZ%2B7S0o96EOUVpXJBb739anMYGL0hSWcFaEie7SvVfY4vYpGsXiXDYD33u9q5V0YW7yh7GqJNU%2FiSxBVkhUnnM7DsPukbH4%2BoTaYV1LtUmrvJw&X-Amz-Signature=e3ba34ad02f74a3b257e3b865b3e88e74347e084347bb1f00c757e46a3edb6a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OJB6QHI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf8QPhPsaIWtUspn%2B5cEokINZ8n%2BKj6W8Wu0G%2FbGVC6AiEAs4xUkpcyx9q1ERKJ9hmp3ivMA4C9cwCjqVB5rg71010qiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHqfZmhn3SOvqtDgaCrcA5vGARKwdAiIvekmBv3lMH%2FbtuAeVzehtXc4ljzYt26ZssbaUgGoSQcjPdj2D%2BZLokQfATeJaBHjZsJDPuWJqKA3ePeceS%2F8QbgTRVEeF6tybzS56b%2BSR0pQNNk29vD7qwOzw3W5N1q8JC1YiBc3LzevqofoODZl0MFwW3eJ6SzNegsPSqrmGaZRmQl%2FYHdvqbuUaAEkf7arm5SDWUAcBzvyrNl9WhwQNamF4ez0rIboGkCqr%2FrFP5IGZcaGkxxoN1eE6o1z%2FCzUgFdLYxa6utdVTYS02fN8cdLZ7ZBXT%2FsbIcnQUs%2FaTlJ2%2BpmiGKcvcS%2FcZPjy%2BUzGl3Ph%2F7RXFymZxIHWxx5mzZevo1DQ6DAk7eNAGu35RAIs4DQ%2Bl6%2BWtxviXtwzDfXfbnEjnTrQZM9cZpzGmn1eThfYVs%2BvQQSOSpnyT4WsDyLE4GqTBuFH0vMm0ZfBsKEhRXtbEXjRs4bJnBDhfHuXMn4OmD0njwbuY%2Fe9%2B5K6t4IupUJ4G9HMC%2BbTrSLgDllemfQ5hKIZIz4uJTunVJoC9dw7jeYM5FyJ%2B%2FPxI%2F6kUx2B37gZCw3aTj0Bl2zEJ5RFesE1cYjm8zGZvNQy4tsNwAnB6fcX%2BE0SL4ZxojBYYNm28joCMILi8bwGOqUBtyyU3VYQyzij43gIM7vCp4pZjh%2BneZMHRhKde9wplU%2Fvby4wPbZX5grBHQdguad8JzUkewb7gzCPAVI%2FDtngLhJTRbZH2TZz0eEwVqiiJiBtzGsvMgiGDRKVm%2BiNdd8Ue0nvOp5YcSQP6MOcz7j5KCvX4vIytVKk9lh4DyfO6Y27dBD7Tjr74mIeTIZcKxworbY%2FqUh9uX1hmdE1giJXdSvtEI5a&X-Amz-Signature=d891000ec3ae65d93793731af63aa5eb1dc0c8891b4ebb1ce27b237a00591df6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSRZF45W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDskMAHE%2FdJAzK1g1Zl66U884FLZ6FI83NGv2kfqUgSQIhAIy4zoBg6Le0QVIzujlKyVEs1yrQ295dNPgMrX9%2BTFMVKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMUS0xDXWkmoH85EIq3AOZugNJizH5LwWXhLY9c6ZeAipdjXGWbCwhByjpsTLrwgPngkxv712MOBOOjIzU%2FZfAOxQvED%2BVixGitzvHyrohbiBr432XxNdNPfehTYkrHzMg70rkkWSyj2DNA03qpjcGlpMtBQ3LMiNj0KFPSY7JreS7af2LwRCUIliyganj5UqjB7s5yMuQkq3NPCdO77XGcrj1ZleDfbeYR41A3N%2FQdoNozx5YQR4b14BmG4ktKLGTq%2B0WCCmMsotICaIJm6OtOAZYOi7E8jdMYybT5%2FA4Co%2FfKvvFmm8hoVktd9GRY9HjWyEUjJ40LzMVyBnha%2B5g28djJQ7FZ1qoJtf4I5UA%2Bt6KfjRLjp9AoeXypRctRCHVEJesH%2FqAmURZuXheWNYdQvGMZoWflphBeh99bfSGuSylbsR%2B773m%2BIUYlzjrqY4qhRH2%2BJR1Bnx6xUiR1PR5jybkDHFbTt2o8%2BCJzW79IZ5ZC4QJweBqya9c%2FGyry4ZHkBhQS4o5Jg8ed%2FsRMiEXV6Xl11G%2Fucy8Pzn6DtRdwTEtmI%2BZFewyRQrkLZXppU99kgTHL13NcFpigjwln3lFDwKXtD%2BSk8pvmp7ET132SfjAzVM7eWP%2B7K%2Fa%2FUJk9BP9okzpbeCkka8ZBDDv4vG8BjqkAZBjSsjYy%2BSps4SBUa%2Fmko7CdkcMHy6GvTNdEah9NAzA2qlbPxXiys5SCTnHa5gEyUoS5s1hDtUAfrF02cpLGgbS4sn6wCgRjHZxfrGctctiW%2Bg%2BGOIR5FVgeP0JBhSQ5fIG2fcFGyU4j1wmucsxUjU9COca13jfjUXnhKhg3xbWo9aj5i%2FDrhC%2FRXO%2BFW0%2F%2BFqszmUNa93Nh7tPxR2LwPunmh7b&X-Amz-Signature=e35fa822773af409025b66244ef821129877c19ff53bd3f5e4fc2fbd0adc4a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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