

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=fc4e93db1ce2e95ecbcceb44e04ace73e790a7920246a4722c3efb0452157cf5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=bcf04c19aa8eb52dc96dd215c308482d0f365c358204a612ddec5e58c26c7835&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=73ef719acc1c1229d41857910f241202219d5a61437878273a057a244fc4ebdd&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=2345b56d9142f29686f4b9556c541f28e022a6d2f9f83b2854777e71f4fe66cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=e9f960bef2a5201885b59b5ce3012d8b0682b2257abf4f1c4bf557f5a3982f71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=8c005ebcd2849f2047f1c4e74a148eb411b6af3853b00126e218f1c1608882d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=2bd6bec1b6f6b5c8f4f595dfa8f78ba39c51158305775f65111e1ff4247ac4b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=17ddbf966f76c520505587400613b0c5f2ab228b80f448c09f963326aa97181e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=edabb8d3ed3589c208701c3bdb65f4a3c53b6cd1a99d15d9b9f9f7c8c64d579d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BQ6NSS7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDPlB094UNl8Ln3DX0ClVq27%2BOJhaPx7dN%2Fxp7lf3T3uAIhAKSZTvIKMiUKFaF%2B6civTM%2FCyJt6OJd0but0OGCrU%2F4gKv8DCBwQABoMNjM3NDIzMTgzODA1IgxiCxzBVpTvKkfBEsEq3ANLHjYiQ7DlB2jmyPx0OvtDXIREtYIo4YEuGF00W%2B7kVncmeETo1oXp55c5aqR7KUB0P2pyAobD%2Fzj2t0L8qLDyAE8NQcqI0nzcmLbxtV3dlwjf7imoiDJ6x04hATFsUZOXIKm3poEDp7X0iGN1efrVlVP6rOryLU%2Fh3hseixVUp%2FF82Lc%2BRsOviC6XeD2U3A3PQ8wepIjI%2FJTTRt6Z%2BX6DOuu6O2iBpnLplhNXhSt693gx2eYv%2FCWTEHaCtf5UbTXtBTLk5C23ZWhR6FCxPHpGN105w1xg%2BrYUwzE0g8786WCYf1qOOVXPwuP8JHo3AXAryyz6k9vt2sYv3FG6ZpbE2ZHeECHZ1NXjP%2BV75UJAaMHNupcLUhyD7izCq9UD5TYFAi5QWFHUUegnW4KxJj04Iltdyypj86mcO33FTq8NIdszfyohm5NkJ5p7eyW4uHiDmDTuLJ6HGatxp6Htq%2F75E7ovISEDEKV2W%2FeGeLCdI%2Bk%2BNVIsa0XL%2FrrxIFNdxA4OfbzjZRrESDuW%2BNh3Irad5Rr7JsnFyOQlM7CLIJ4jX3y5hWcUAid0Hmic%2FjLti5jWIqjM0LrgDX%2FO9%2BDBUsowlJGxxxu0cTZXn%2Fth%2B%2F2DbSQRFsrIyeQDY5w16TD8oIS9BjqkARWG4I%2Fc84FYlHBrI75IZKdMzhQCdV8UQAkGoY84%2BEzLVwj%2FfpIzJhxkRUmrJ1PcQdIGpYmlYuMRrLNoFKhYL0CozpgMMBZpMG8ilRQ%2F%2F8%2FTSjLJoubtDSCkPUKqrhuq%2Bpm5kbZHCdpTJanC0blvdwFJ68FzZWmeu1KeviT3MSniCTIHAjdfcbdzhjI7qIZz0lgUqpoZuWBsjefxQfpQn5ZFd23H&X-Amz-Signature=f0dbe69374575490ced638983356e77ec6d52ca25be186d92d57b4c5d4ff5170&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BQ6NSS7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDPlB094UNl8Ln3DX0ClVq27%2BOJhaPx7dN%2Fxp7lf3T3uAIhAKSZTvIKMiUKFaF%2B6civTM%2FCyJt6OJd0but0OGCrU%2F4gKv8DCBwQABoMNjM3NDIzMTgzODA1IgxiCxzBVpTvKkfBEsEq3ANLHjYiQ7DlB2jmyPx0OvtDXIREtYIo4YEuGF00W%2B7kVncmeETo1oXp55c5aqR7KUB0P2pyAobD%2Fzj2t0L8qLDyAE8NQcqI0nzcmLbxtV3dlwjf7imoiDJ6x04hATFsUZOXIKm3poEDp7X0iGN1efrVlVP6rOryLU%2Fh3hseixVUp%2FF82Lc%2BRsOviC6XeD2U3A3PQ8wepIjI%2FJTTRt6Z%2BX6DOuu6O2iBpnLplhNXhSt693gx2eYv%2FCWTEHaCtf5UbTXtBTLk5C23ZWhR6FCxPHpGN105w1xg%2BrYUwzE0g8786WCYf1qOOVXPwuP8JHo3AXAryyz6k9vt2sYv3FG6ZpbE2ZHeECHZ1NXjP%2BV75UJAaMHNupcLUhyD7izCq9UD5TYFAi5QWFHUUegnW4KxJj04Iltdyypj86mcO33FTq8NIdszfyohm5NkJ5p7eyW4uHiDmDTuLJ6HGatxp6Htq%2F75E7ovISEDEKV2W%2FeGeLCdI%2Bk%2BNVIsa0XL%2FrrxIFNdxA4OfbzjZRrESDuW%2BNh3Irad5Rr7JsnFyOQlM7CLIJ4jX3y5hWcUAid0Hmic%2FjLti5jWIqjM0LrgDX%2FO9%2BDBUsowlJGxxxu0cTZXn%2Fth%2B%2F2DbSQRFsrIyeQDY5w16TD8oIS9BjqkARWG4I%2Fc84FYlHBrI75IZKdMzhQCdV8UQAkGoY84%2BEzLVwj%2FfpIzJhxkRUmrJ1PcQdIGpYmlYuMRrLNoFKhYL0CozpgMMBZpMG8ilRQ%2F%2F8%2FTSjLJoubtDSCkPUKqrhuq%2Bpm5kbZHCdpTJanC0blvdwFJ68FzZWmeu1KeviT3MSniCTIHAjdfcbdzhjI7qIZz0lgUqpoZuWBsjefxQfpQn5ZFd23H&X-Amz-Signature=d82a0a3fa77f806ce737a9cf091b964ba970b8544638fa903ad0a90daa375157&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BQ6NSS7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDPlB094UNl8Ln3DX0ClVq27%2BOJhaPx7dN%2Fxp7lf3T3uAIhAKSZTvIKMiUKFaF%2B6civTM%2FCyJt6OJd0but0OGCrU%2F4gKv8DCBwQABoMNjM3NDIzMTgzODA1IgxiCxzBVpTvKkfBEsEq3ANLHjYiQ7DlB2jmyPx0OvtDXIREtYIo4YEuGF00W%2B7kVncmeETo1oXp55c5aqR7KUB0P2pyAobD%2Fzj2t0L8qLDyAE8NQcqI0nzcmLbxtV3dlwjf7imoiDJ6x04hATFsUZOXIKm3poEDp7X0iGN1efrVlVP6rOryLU%2Fh3hseixVUp%2FF82Lc%2BRsOviC6XeD2U3A3PQ8wepIjI%2FJTTRt6Z%2BX6DOuu6O2iBpnLplhNXhSt693gx2eYv%2FCWTEHaCtf5UbTXtBTLk5C23ZWhR6FCxPHpGN105w1xg%2BrYUwzE0g8786WCYf1qOOVXPwuP8JHo3AXAryyz6k9vt2sYv3FG6ZpbE2ZHeECHZ1NXjP%2BV75UJAaMHNupcLUhyD7izCq9UD5TYFAi5QWFHUUegnW4KxJj04Iltdyypj86mcO33FTq8NIdszfyohm5NkJ5p7eyW4uHiDmDTuLJ6HGatxp6Htq%2F75E7ovISEDEKV2W%2FeGeLCdI%2Bk%2BNVIsa0XL%2FrrxIFNdxA4OfbzjZRrESDuW%2BNh3Irad5Rr7JsnFyOQlM7CLIJ4jX3y5hWcUAid0Hmic%2FjLti5jWIqjM0LrgDX%2FO9%2BDBUsowlJGxxxu0cTZXn%2Fth%2B%2F2DbSQRFsrIyeQDY5w16TD8oIS9BjqkARWG4I%2Fc84FYlHBrI75IZKdMzhQCdV8UQAkGoY84%2BEzLVwj%2FfpIzJhxkRUmrJ1PcQdIGpYmlYuMRrLNoFKhYL0CozpgMMBZpMG8ilRQ%2F%2F8%2FTSjLJoubtDSCkPUKqrhuq%2Bpm5kbZHCdpTJanC0blvdwFJ68FzZWmeu1KeviT3MSniCTIHAjdfcbdzhjI7qIZz0lgUqpoZuWBsjefxQfpQn5ZFd23H&X-Amz-Signature=589b57b709d169c7a84a8c55dac4963d03725e188891a2683bf837b1d94ec7cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=41c9f048fb5a841bad5520dd7ed48dcbe0a478d3c74843f20db981ef234f69da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=2bffb72a138b3cc82f083cfb01aeec15427bf318a064f606e64bbe3ada311976&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=2819ec0558f5cd2c8c591438c2e67a42e70c6533ce007f52d88222d17bdd7b49&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=5a890f8507e211298bd95fb693582275819e73353cd7c43eec037f5c440413df&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=28f13674148210a1cccfcbccc0d16eda97e03840f919d2e3622bb6738588fc05&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHDJCVN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIF90TBnkDDNE9xqiIGkmp%2FKor6rIt09BdoprtN9mlCg3AiBTYfRDPaHpCXMvNBiWXo1I4Imu1pH%2B%2FYjupAtTuzeDgyr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMT2y96d2StemY7WLkKtwDcO8HIP%2BrYMW4TA3HHbyOdylKDRHEJHWYqXLViVFVLLbUAFRJSjnw%2FpwIQ8kp%2B8A6%2FRuTK%2FLRM0ZeTU4X94eK04e0DTpsxWSzYhCOpCPucd%2BDswASnN5yTF7%2BLrR6%2FoCW4vVErdV5v1HdVdK7Z3iGq6RPTPHrbDyBSq1vrE7P3W9z7HJK6EWrCAt35iqPkV7dVMyYKHPgJEGaJD3%2FE%2BFqkixfQZqMpXRAxX7lxTrTrHzIT497RzkHfwMHJmcebENwv7%2BObbuPbOi2WJmHUpgp%2F1a8fIJzw5Si2LgxgrWAVWVjs0%2FdLWMn01XSZeB%2FO5TwbDDURhiwBmCICo79GuClDYg%2FOX9LyXEEq%2FpfrFF6RbJXN6OPNx8zeZWCPoHunFFK8QwZCj1Ox2enHO2Z38P0SnzBLg6lJUH%2Ftr4YkIM%2F1%2Fkr3P6thQoDxeyARQhCGUSNbND3w7wLz5KTnhvTJNychBQsp9y6td%2FnEC9BQfBwc5jT%2Bx2JnbUaq7lHnDLsmWwbFEndwp78JGmMygG67lWGp549OBqHcSD9pNQgXWjsjojnpY9IvG15E6GJ9BlnllW%2Bh9she1bBJ5e2aD3yO0P7jcw23H7%2FZdJNgQceAtwgqIlToNb49EVRd7qU8sQwoaKEvQY6pgEE4hyb9zUri29cUswPAgFx9juaz5%2FzYgv007Dff4nbT5q5nw6TWSp6qjE3lrZ6beq8H0TUr%2BkA5D1qLjIOQKdWNBof7%2Ftj9qnXhPTVDR7qCFS2UydXY0hLX0w6PXB0aY8LufZzW66o9RbYuiqWmy6q1Bls2CMCfLP434qsyOXHH0xC3UpfLQxoI3vRY1fcFgaDWkaVhHnITko4p6m1WF%2B89Gh6mmG7&X-Amz-Signature=83184c2c76389920b1817f1982d9782dc7a2864a1e49551bec2a86b1e4a860eb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKEPDAT2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE2qboIdPaUnCcaK1N9gprAU%2FwyWzhkHozdWwJnlIqAfAiBv7pqllwzFZ0NfuMwtRsE0ocJNn%2F%2FyZWyz%2Bpi7hLmbWSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMbWrD%2Biyr7QUHnnlsKtwDG28vnbjjUZLlN0%2Bcb38u45T3%2BB%2B%2BIzeKLN2QkVrh6Q%2BEzYf3EoTS1wD4hofzog3EkHWsTQz%2B2ciiebjuQnetthzzI38Q1JBmFz4lyd13S%2FdKvLNDlvJSx0Unq%2Fa11y%2F%2FltanPNbf3%2B6b46xjP7wKtodysEE9AMDczhsyhAHLjHQ02auXyt5QgJ%2FtjlPyKOdKS5XIfQFVgJw%2Bnd0DQwRkNUla46GLWW3szOxq6tuB7l46CUrSMA%2BJEDP74bsK4WuzjNYXxZhOnBl3%2BDHhBQ5tV4IKEvUVXeeAtw2YzH7DdnlVjmhvYYGAW7j3BrK%2BvX4vePMjRldYGnTVD5C0TcxgedwiH5Bplt%2FmyOA6KIKIlY4p48tMOfTmJFUrY1viW%2BqGYTzjdH9lqoOhnrqxi3Tvb7tWrO9sHQZxZs%2BInY95gPt%2F%2FbVkg3bSe8QsdTVL%2Ft7hQA4GjC47LJ4TVFur27Kt6HFzpn9Np7ndmi7VN3zPD91hc%2BM8%2BDqlEZp69U8QS46sB8k7Jgma8vpsUKUxc68jUd1yswZvR6wcUkx6MoR9eeImYnfl7ivcjCvfMEnM1FQBLLijnoQFNTuSaaMy%2Bp9qYNEP5vY1msGEOrctnC6JTKKBYqa8COumEneGvWEwzKCEvQY6pgG9QYI2Uh%2BVLHmrwW%2FJc7zIafJaSvEtdbv1SjnRwFx1sxnXmzD6%2FwAfwWua%2FKdk9mTwuzf3pyl9Z9l8ZbZ%2B6qE4Eh4VKsDDlUxPIjM%2BZ%2FK5cwM8%2FKpy2TtKU6W76NxVXdvGVw25bY6V%2BLzQTqn2a3VjvU4%2BUBSxuFhhI5F7m%2B0hAiq1iCr3k%2FByu4Tq7MBdUlXgemNn4rSfGxYeavYvjF7eKLOoGiHY&X-Amz-Signature=156f676787f8e185b17f663b8bc73f98dd3b008fc917690f79eb60ceac08dc79&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKEPDAT2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE2qboIdPaUnCcaK1N9gprAU%2FwyWzhkHozdWwJnlIqAfAiBv7pqllwzFZ0NfuMwtRsE0ocJNn%2F%2FyZWyz%2Bpi7hLmbWSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMbWrD%2Biyr7QUHnnlsKtwDG28vnbjjUZLlN0%2Bcb38u45T3%2BB%2B%2BIzeKLN2QkVrh6Q%2BEzYf3EoTS1wD4hofzog3EkHWsTQz%2B2ciiebjuQnetthzzI38Q1JBmFz4lyd13S%2FdKvLNDlvJSx0Unq%2Fa11y%2F%2FltanPNbf3%2B6b46xjP7wKtodysEE9AMDczhsyhAHLjHQ02auXyt5QgJ%2FtjlPyKOdKS5XIfQFVgJw%2Bnd0DQwRkNUla46GLWW3szOxq6tuB7l46CUrSMA%2BJEDP74bsK4WuzjNYXxZhOnBl3%2BDHhBQ5tV4IKEvUVXeeAtw2YzH7DdnlVjmhvYYGAW7j3BrK%2BvX4vePMjRldYGnTVD5C0TcxgedwiH5Bplt%2FmyOA6KIKIlY4p48tMOfTmJFUrY1viW%2BqGYTzjdH9lqoOhnrqxi3Tvb7tWrO9sHQZxZs%2BInY95gPt%2F%2FbVkg3bSe8QsdTVL%2Ft7hQA4GjC47LJ4TVFur27Kt6HFzpn9Np7ndmi7VN3zPD91hc%2BM8%2BDqlEZp69U8QS46sB8k7Jgma8vpsUKUxc68jUd1yswZvR6wcUkx6MoR9eeImYnfl7ivcjCvfMEnM1FQBLLijnoQFNTuSaaMy%2Bp9qYNEP5vY1msGEOrctnC6JTKKBYqa8COumEneGvWEwzKCEvQY6pgG9QYI2Uh%2BVLHmrwW%2FJc7zIafJaSvEtdbv1SjnRwFx1sxnXmzD6%2FwAfwWua%2FKdk9mTwuzf3pyl9Z9l8ZbZ%2B6qE4Eh4VKsDDlUxPIjM%2BZ%2FK5cwM8%2FKpy2TtKU6W76NxVXdvGVw25bY6V%2BLzQTqn2a3VjvU4%2BUBSxuFhhI5F7m%2B0hAiq1iCr3k%2FByu4Tq7MBdUlXgemNn4rSfGxYeavYvjF7eKLOoGiHY&X-Amz-Signature=b17bd315c6af2200d5556a83410095c7e0d9a3b5a0c95f943c5091d2416da23d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDH3F4ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDeu1d8r9dyOtFiR%2FOjYknmZpsEdS0ny9wufBQvDnpIKQIhAMtn8ncNfkQ5MHYAiiebDp9P8aqnQu7sBDlML5irTmQeKv8DCBwQABoMNjM3NDIzMTgzODA1Igy6QdEuh%2BBjT6b9Q14q3AN84eBy1%2FVe%2BVTQpw3sWyrZhed5gFfrhCJ9T8Zz8Y9ce7Dm9nsZ6MKxBmL48KjLgzz4%2BLlfRN6oW2vxURv3YotRRVlE92SiPRyMZV2jUBgImiOgZQ9yfHudhXAYEaO5I1sidCqMV3VwaUWOu31Ob41XpSDdswOJ4HGXLFuce6zpZvzz8qYNytZZOZFR16n9gyEe%2FRF2tu%2FM3L5ETWZ%2FZldWOuI7AmSexynLOTdk%2B2nruJ1e3Ha1t2UZzwyRwSvYjpTbUzpOILb%2FKbW7sSWjKQr5GzomPzcewTej16rg8SI65I8a9uwwWm4Hh%2BAeHPND0c10yCtmuWFwPs27Z4EP7tMO9DICMrdK0B34iFfCQGPaW%2BOX2qg53UpNY1zENT00I2X1bSeeyRFX3fclNlwNKP%2BgTMn2N3TW80%2BDRfPLGzuAIiFI1JnHOlMLBqLmyUeURFoRmZnHDdGRk1%2F4%2BXRHyz1Dw8Bp7357SqZVLoxErmGnVtInczeo43IBgpFysTzcDCzfhPFDEEBClsu87EgHgnhDOqpwDGzDThA%2BXLNoWrRNx%2B06gfkr%2FyDiUfNSIvagEzVLtFKQQRcYg04EdyYhPfl8LsjIQkKgUk6qntDOOHP7jckJYk6Q5nWBlN0xQDDPoIS9BjqkAVgHNZ%2FOp9qhX%2BOUt0Gqz7x5lKcx7OQOsEwdfC7LNatBe%2FUtLE0%2FpxJWczbP4ruvrj33ywZO%2FxnGRn%2BiD44NzP2pCLAZkhXu92KdhC4rNYqnO8jHCIEBGCJvNhunTvkR14Q64HydRymaZ%2F%2BCqX4vxGj%2FJa%2F0F%2FZFqOIR7jIt4Eozsfh%2BBNggvnX7sXJH4LVTOnuA4a5lw8Q%2F%2BJdYfR7D6VJuc4PV&X-Amz-Signature=5799667f9ec00501cb496ccf27bd7e7076c8efb13029dd231f694b2814ebbdd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVYHYBR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDXJlqfmvn6SzkX8QVzbW2dfv2LrOyfEo0W6bjQrCQlAgIhAKhH%2FHzw4n4oEVJDLCCCH%2BIG8SXM5ZjHz9bAtbCYsRmPKv8DCBwQABoMNjM3NDIzMTgzODA1IgxlJ%2BD1bsXET0kdilkq3AP7A6iRl7isLrgPPfsxzDUwhmfUckqndgZ2eis8XO%2BiBklK0vt%2BqOJNp9RBSnJGVpBJlJBww0hv%2FmggrotSTeAs8sh%2BgD1L8GH5n6LBhSxmQ5%2BOX5VNBLax1OEknaI1gUlaT73IYSu2GaMiUazf1rQxSQ1%2FYhEvCY1aCV6uwW8uxii%2FolenPSQxr%2Bag6pV8THg9CpaFwDkCViSpBmvPmW%2FoCJ2f%2FK0FR%2FYGI%2FlxeIOdl5ZYeGA%2F8r9aajhy%2BYJjZmmBxLtioojmgsjT%2FGXizqleg8X8hPjrEShOMd%2FBxX0R%2BGtdS1M%2FcBasTecs0fOQ8XA%2FTMyi4UXFFbBdGKnP5t4agH0R6%2BZ92BjSuPbe9J3GxHd7Btc6BxUhAog1GgqnCMzvfGTupXpduAinbVPXkqc9%2FRpNE4%2Fsfr9Ym8KRBjQHzOvbFyPyzDfpxQSmH%2BjdlW2%2FJDv%2BVblx9MwvLfQ9UfJ%2FJx6WiPyCiRV%2BtP4Bn0360Sh4phZD%2B9mcbS2Sw96TAgQMfzG%2FkZkCtHklQ%2FO1kbl6CRT0OSQ5x8uqjPW9AZYn1Y8lcJgvBbRSxHi37v8b%2B%2BCZ%2BmoNV2ql03jcGw8ZXJqa8LCu8KfLg3pr%2BEa1ud0za4CVVTNhgy7BMx69wjDMoIS9BjqkAZCLb6uJ9CN5ySfGGuYSU5jJ9%2BJeOV0hyqLy6elF0dSSDFkdeAVryC0QVKtem8uayEDFpw4nWJbI3k52mFcgCL6AKVqIBJyir%2BlrBQV6Fq79osS%2FJmrggUzxB2H9T%2BifBABXSgulnFNLoIz4ISM4t81lNsnmmv%2FlflqUgsFbudS7HThfGqIInb74wYk%2FCbsrZ6xUTh7QUNhKszKLH7ll%2FolUcLNB&X-Amz-Signature=9e1bfb7e7c101e381eba857cebdb00f2174bbf19da7e1347a7b21ea0da6f21b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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