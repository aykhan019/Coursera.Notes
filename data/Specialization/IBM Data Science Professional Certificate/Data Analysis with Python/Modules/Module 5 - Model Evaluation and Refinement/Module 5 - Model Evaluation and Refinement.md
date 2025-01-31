

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=8d10fec952a6d165cf105fc24bde2b3ee49da86b5cc3348267d4d641091b260d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=0bedc3ee0f560d110effbe8fde1137776a7758e23846ae37c2f828e249ed6421&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=772fb79b9a3382d6983bb86840622cd3351193bf531f80500586cc2549fbeecc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=4f81a4b95c63b7eb7780c46be4df0d38c07ad2f59965baf723520fd25f33c7be&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=b7216b58057a047b43d3f482f264d550732a0d9edea3ae7d3f0abf6f0c6a45ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=53f46b6e05d7bb3523721e957d9e24a5a1778fdb3e49fb98e697fad360b4e788&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=1d3be6a7d50676e2122f419c679b0db14f4e761628b22182cb457226d53126c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=b7eb4c5490d3263dfcdda6b650e0fe0d34aa26adc61719c84e39df8c21165570&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=007f7adc0071f271ae3a7fe05058cfb4f6d44dd610873d2f95858d532a4334c3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE347C3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Bl4o%2B8ruK%2F25%2FZBJ0q9GqtoClhBvBKfXesWeK5LG%2FlAiEA2QuWw%2BABNwp3MbrNZSC68oKNXXaeB3hbxLdcp1FnWS0qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGMLmfkHsdpM2rBcCrcAzcEpkjCJUxdo%2Bgv4yxRVQ%2BsylTs5rNIkw8OxAEhou9jK%2FaM0qq18JR%2BooVas0QhhCS7pbFJRaxUjvEhl578vKvHt0XwWzZEFLRjkv14FSnhjox169f%2BatSOs7rZ19lstCeC%2FIsPxH5KZDlSVhu%2FyxrGIqXAXGuXMFwXhePiBNsQXLRq3Nt1ZnTMCitfbVQElT3pG06yXuki0Btu9Sm1%2BSSfG8tEpCdSiKbfiic%2BHtuFcJlyCnzxkzFqhjd15WkfVnkMXRMaliLvq8T%2BE4FFLp2vOOvcrc6dxC%2BEG2EpiP0HkkqIJ3X53rMZAW0Z0F0a9n4EsJV1XZ%2BZlzT50ifn%2F3krgU1DLWu70DqxEU7gPPtArsZoiT%2B%2Fmls1n%2FuJ2AHCOJH1I8B%2F9M9GdOgsmS02TlPc2oTLRjIXmQidhf%2BCZnN47lkoacFS1qT0VW7BlAi66XO8Fd9Pbx5yfc%2BypaqEr%2FfbEGs5lPXoOl8HLYvkmfzaWhyFYWF57rdPif25vLx2Z6MS6RBMUiBgqtrry0xUsGLzvrEy0Yf0edKexzbaYb%2BT5mIXYoU3nduVA%2F1N8h%2F1zp56z7zfe1NXLJlXFxwgUMQyf476s487NbisJoMS0isvguIoVtWOE06XdNznMLjW8rwGOqUBO8oINOWo3JF1COOx%2B9FT5m%2B7V7ID6xcCkGBtUvuq1y7Es2xefIkR6qrLZW3irq9Pllu0b9R%2FlzE2TvrTqml1o6NNrP1Vtvzf3hBsSIq3GGUQPVu2xJkOuRIFc7xuOuIumH7TuP%2F%2F0f5aGJ2a1srK01wrFtVducAjmH5Tggvg3rCHvMAh0juSUWB79fYNbWKRKNXMANT3cefJDMnKCqMzKkHFrN%2Bz&X-Amz-Signature=448b516014450e03037db5189ebd7b23f53f6a91364ab8c546f5378d92f61aed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE347C3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Bl4o%2B8ruK%2F25%2FZBJ0q9GqtoClhBvBKfXesWeK5LG%2FlAiEA2QuWw%2BABNwp3MbrNZSC68oKNXXaeB3hbxLdcp1FnWS0qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGMLmfkHsdpM2rBcCrcAzcEpkjCJUxdo%2Bgv4yxRVQ%2BsylTs5rNIkw8OxAEhou9jK%2FaM0qq18JR%2BooVas0QhhCS7pbFJRaxUjvEhl578vKvHt0XwWzZEFLRjkv14FSnhjox169f%2BatSOs7rZ19lstCeC%2FIsPxH5KZDlSVhu%2FyxrGIqXAXGuXMFwXhePiBNsQXLRq3Nt1ZnTMCitfbVQElT3pG06yXuki0Btu9Sm1%2BSSfG8tEpCdSiKbfiic%2BHtuFcJlyCnzxkzFqhjd15WkfVnkMXRMaliLvq8T%2BE4FFLp2vOOvcrc6dxC%2BEG2EpiP0HkkqIJ3X53rMZAW0Z0F0a9n4EsJV1XZ%2BZlzT50ifn%2F3krgU1DLWu70DqxEU7gPPtArsZoiT%2B%2Fmls1n%2FuJ2AHCOJH1I8B%2F9M9GdOgsmS02TlPc2oTLRjIXmQidhf%2BCZnN47lkoacFS1qT0VW7BlAi66XO8Fd9Pbx5yfc%2BypaqEr%2FfbEGs5lPXoOl8HLYvkmfzaWhyFYWF57rdPif25vLx2Z6MS6RBMUiBgqtrry0xUsGLzvrEy0Yf0edKexzbaYb%2BT5mIXYoU3nduVA%2F1N8h%2F1zp56z7zfe1NXLJlXFxwgUMQyf476s487NbisJoMS0isvguIoVtWOE06XdNznMLjW8rwGOqUBO8oINOWo3JF1COOx%2B9FT5m%2B7V7ID6xcCkGBtUvuq1y7Es2xefIkR6qrLZW3irq9Pllu0b9R%2FlzE2TvrTqml1o6NNrP1Vtvzf3hBsSIq3GGUQPVu2xJkOuRIFc7xuOuIumH7TuP%2F%2F0f5aGJ2a1srK01wrFtVducAjmH5Tggvg3rCHvMAh0juSUWB79fYNbWKRKNXMANT3cefJDMnKCqMzKkHFrN%2Bz&X-Amz-Signature=681e4ad3f586bc93df55e3bbb0c39f7fb47c6583a2952777d2d8c01fe382126f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE347C3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Bl4o%2B8ruK%2F25%2FZBJ0q9GqtoClhBvBKfXesWeK5LG%2FlAiEA2QuWw%2BABNwp3MbrNZSC68oKNXXaeB3hbxLdcp1FnWS0qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGMLmfkHsdpM2rBcCrcAzcEpkjCJUxdo%2Bgv4yxRVQ%2BsylTs5rNIkw8OxAEhou9jK%2FaM0qq18JR%2BooVas0QhhCS7pbFJRaxUjvEhl578vKvHt0XwWzZEFLRjkv14FSnhjox169f%2BatSOs7rZ19lstCeC%2FIsPxH5KZDlSVhu%2FyxrGIqXAXGuXMFwXhePiBNsQXLRq3Nt1ZnTMCitfbVQElT3pG06yXuki0Btu9Sm1%2BSSfG8tEpCdSiKbfiic%2BHtuFcJlyCnzxkzFqhjd15WkfVnkMXRMaliLvq8T%2BE4FFLp2vOOvcrc6dxC%2BEG2EpiP0HkkqIJ3X53rMZAW0Z0F0a9n4EsJV1XZ%2BZlzT50ifn%2F3krgU1DLWu70DqxEU7gPPtArsZoiT%2B%2Fmls1n%2FuJ2AHCOJH1I8B%2F9M9GdOgsmS02TlPc2oTLRjIXmQidhf%2BCZnN47lkoacFS1qT0VW7BlAi66XO8Fd9Pbx5yfc%2BypaqEr%2FfbEGs5lPXoOl8HLYvkmfzaWhyFYWF57rdPif25vLx2Z6MS6RBMUiBgqtrry0xUsGLzvrEy0Yf0edKexzbaYb%2BT5mIXYoU3nduVA%2F1N8h%2F1zp56z7zfe1NXLJlXFxwgUMQyf476s487NbisJoMS0isvguIoVtWOE06XdNznMLjW8rwGOqUBO8oINOWo3JF1COOx%2B9FT5m%2B7V7ID6xcCkGBtUvuq1y7Es2xefIkR6qrLZW3irq9Pllu0b9R%2FlzE2TvrTqml1o6NNrP1Vtvzf3hBsSIq3GGUQPVu2xJkOuRIFc7xuOuIumH7TuP%2F%2F0f5aGJ2a1srK01wrFtVducAjmH5Tggvg3rCHvMAh0juSUWB79fYNbWKRKNXMANT3cefJDMnKCqMzKkHFrN%2Bz&X-Amz-Signature=5da00bbf892a7417c1b7f5d3b3b7fed781122220b367ac83e2ec5e870899bf4d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=aabd15b2382b2d03db2066cc70e5b3e3a5405b052e2ed4b78cb719581f9566ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=da802c9a713b4f6e70c758a8049184ee9b78565f5aefb3924c0c40fe85463592&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=2f62790d688c1fc50414929be770d21f8c5b912c573d104621419286c1614f67&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=97e03d9e752a4c33ee03a8220ba00c451347d212e6208709345060c9644944d9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=6d7f5d3f025e0c09c624278906a34745524ee51740afa8f282ff92a0e06b285e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEHGESOF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCG6A22jHILNyM9IHRkkCaIzCQxP%2FjTG1sGxdY2D5UBbgIgEA97OKc3yAYJ0%2BU9aK5ADfDnT%2FXHL4BNcwuPEJYedBEqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9m876nvMjshq%2F1ayrcA5VnxBq2VFw2wv47rhNAQpkBzui1Bbd174Y3MSQLmKFDylcvxNsUx9QgzTaEmDcvCfFNTPMPm4TidnnBAtYvT0W7LgQUogcuZv7B6xv8VH8hmEtU2%2FHBH99NDKZ6EpQcxvdxjKFQ9eXcFsEF75EuFJkhY9Oj0qfdMUttgYnol37Jt8zrAxlJUc%2Fxz7aYgay5B4XgYkFoTSOmOGl3dYCQsLmnQBS%2FXh69EpANtl8yriPRNPivdOt2kDc5%2BXmq%2FhvwWt2nIuiZzLb9jauYRHIhrSluanbX46yYTR460R%2BvurHKp%2BFpd2Mn7%2BMqeNpD2t3L92y%2FjD3l35vqSswG8JByziqpydUkpjtmoUkoovJMV%2FIy2ac95nyMabipHIpIKX7wZw%2FR5TNxsupTcMiMRk5sqVPwt850mQfskKtCFEt9me6aFp77UR2cb1RCRcUcWDsMFLuUlaHLESmZE3nghJeMt8ppWge6qF21UiZgQ%2FoSOTv0a3oyyGytWzra4%2FhKnpGn8lyL2QwmItzounRdJlaW0Boq%2BmWT2T0ygunsUIdD5%2BrciIxYhvNjbG3cIzPpE7%2BxQAP4LtOkoc7uEcj0YpeI5zy4mxeqd83c12RYFEEyoFzJpychcFsSRY5cp7mYMLbW8rwGOqUBj5QASipc%2FidSnsciPBTJ42tudnA294cOFM6Tmh7eaDRNKVtl4zppU2PRT7lA0q6ZaSUBFZW%2BzpKIEz31hGwaZEXiMxkGrpDx3IETmFVWSE5dhGgpyuVyEXW%2FNqk5JCLVXMN7odlcz3YoCaWhoQTpvfcfBKJKVN51yNRLJMihNb%2B%2FevRTTmM2JaOLRjpTT0IvCmts2FVtnTzfnrCVpcSg4NkpuHRz&X-Amz-Signature=bdcb650f895b1190603f03a306f2e23baf4aab592be8615a205122b43e9cb243&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UONUINWR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwNofLtpAC%2By5uruOZzWhi7wnpF%2BIowJk0REO2vgeE5AIhALdCs345YlEIkVgW5SIydr3aQ5SvIriH3LfBXs9tXsTdKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9hdGqJku08xWrIBQq3AO0LzSLDocchMCU6d7v6368bcI2nCEiZQN5yZnFwkYafvzdnf%2BuMHQLteoUXBW3nsehTr%2F%2BFDTOuf6SbA287QBkBUzDrc9NVN%2BcQYMvHneUoYIFg85z7QSBcQJ%2FSkzYhgRSq7%2Fqg1k7qznisnxZjd5g38m%2FzlX0Uax9%2BOEf2uSziACk65l1a3k4qTLcAWRQSVlCH4H5%2BQEG%2F1QAHlU3CwpcW%2F20N61dQggp1OYuFYE0YgUsrkJgd1wLdfnMMim%2FhAVfVatZ4u45ahrcWX2asCsvtY1bxsYIjLixDJ3HpJvAh6ds0oXow%2F%2FuG%2FuLz0hSagK7zRQBPQ%2B9nYOdpc7bkLz18eHBqiBD0XSenRNCGa1Dc5XT0nA3JR0Dcz3l3Ots5jZsPXd7ShG0YHJmOmWQKvOvja6CsYR73wtAgsX%2Bl5w67zYZ5dE8liQg%2FvtyHZstHDEiE15E8AYifknJtKDAUa9mhhji607MhS6HPm32eMlb8xg0gq2%2FdOvp%2FDMaxXM3MYRqQjcA9ACmFJTCJzSqhsieCh0QNqmvG8XwAFckDvdgnO2wR4Xsyr3poIZtN3mgLgS1tCDcnuGMoDjO9ga4gNjo9L0Hov%2BMiqXqLSNaaUOcSwMk4eKZNF60uJjwSzDk1vK8BjqkAc1pR48jLrVWqkEqh26gZfE8JEwlXFYfP%2BW19I1Bgbn7VQLjWyulpOfNvQjrqFRJfcCexuk1fUIlrw8LEM1XbKJ1uEZ5nDOrtYl%2F%2FNaKaGBahMDA0yoGZ0vRFiZ29EgWc0OjKhQ0t7j5y%2B3mEHdmQVO%2BD6mKc3aMADmLY%2FgFaJCsFFrsL9Dno%2BdVr21EtVcIbuVUhbE6jvnnsnmpswvewiTpYhlC&X-Amz-Signature=e18aa6744ad70cce800e36d9d3e65137d4d64a4651b8119abc43a586a8953d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UONUINWR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwNofLtpAC%2By5uruOZzWhi7wnpF%2BIowJk0REO2vgeE5AIhALdCs345YlEIkVgW5SIydr3aQ5SvIriH3LfBXs9tXsTdKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9hdGqJku08xWrIBQq3AO0LzSLDocchMCU6d7v6368bcI2nCEiZQN5yZnFwkYafvzdnf%2BuMHQLteoUXBW3nsehTr%2F%2BFDTOuf6SbA287QBkBUzDrc9NVN%2BcQYMvHneUoYIFg85z7QSBcQJ%2FSkzYhgRSq7%2Fqg1k7qznisnxZjd5g38m%2FzlX0Uax9%2BOEf2uSziACk65l1a3k4qTLcAWRQSVlCH4H5%2BQEG%2F1QAHlU3CwpcW%2F20N61dQggp1OYuFYE0YgUsrkJgd1wLdfnMMim%2FhAVfVatZ4u45ahrcWX2asCsvtY1bxsYIjLixDJ3HpJvAh6ds0oXow%2F%2FuG%2FuLz0hSagK7zRQBPQ%2B9nYOdpc7bkLz18eHBqiBD0XSenRNCGa1Dc5XT0nA3JR0Dcz3l3Ots5jZsPXd7ShG0YHJmOmWQKvOvja6CsYR73wtAgsX%2Bl5w67zYZ5dE8liQg%2FvtyHZstHDEiE15E8AYifknJtKDAUa9mhhji607MhS6HPm32eMlb8xg0gq2%2FdOvp%2FDMaxXM3MYRqQjcA9ACmFJTCJzSqhsieCh0QNqmvG8XwAFckDvdgnO2wR4Xsyr3poIZtN3mgLgS1tCDcnuGMoDjO9ga4gNjo9L0Hov%2BMiqXqLSNaaUOcSwMk4eKZNF60uJjwSzDk1vK8BjqkAc1pR48jLrVWqkEqh26gZfE8JEwlXFYfP%2BW19I1Bgbn7VQLjWyulpOfNvQjrqFRJfcCexuk1fUIlrw8LEM1XbKJ1uEZ5nDOrtYl%2F%2FNaKaGBahMDA0yoGZ0vRFiZ29EgWc0OjKhQ0t7j5y%2B3mEHdmQVO%2BD6mKc3aMADmLY%2FgFaJCsFFrsL9Dno%2BdVr21EtVcIbuVUhbE6jvnnsnmpswvewiTpYhlC&X-Amz-Signature=82f3372997a535972ec56903b25e38c127d8c736a6248148e698630ac9f7cdbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCXKRAAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAV5bU9NrMiTawTDb5ATeV8pq%2B%2FlJL%2BIuN0qjeu6rTaAiAoWsbeblArnjIcAhZwJzvNzjSa8JDWBB9Ix1Ogu22kLyqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcg04HRzyB6Yu07C2KtwDrWBv8k4vmylyYPPV11vleApOlqGQZVKBj%2F4LFIsIrR0xLder5LM2HxGvKQnfhAuI%2F1uddVNjzfOmiUbEyzPSRA6yblO%2Bww4U%2BX9m60SOg04pZ%2FcGBTNtVGhFuFB9B6aYN9a%2FKm%2FoSZli%2Fzt2IBM0Vsv5anfM9XbVi9z%2F3ujoYEVZqSAZjj6pucMT9GFbDAxalVpy5RaiZyQM51iPyHIJVva7BQD3uIUuF1vFM%2FlK4e3%2FljclRNuDuOB0GLmwjWAT4%2FWf6uA212P1wWuJ89gNwjhfUktB5IEinWmuOosTMgL6iEupoCcP02MQW5ff%2BVwo4AqoJsVGLYTVRTMSMgnU7h%2BGgvlw4tdltXSXkGxpTS3XezEpwQLPPpegMhMo54UhcO2%2FPyiZFdYukTJZbpJTHb3WhpH5tUCYIWUMiDFmBfFFIpryCdDJ7WF%2BfWQeviGwFSY1OphajQ9bQUIahbWpuaCm4a6ilDPXEBZO8X%2FCVzzjP9WUYxXz9voMZ3IK3uKMi0f%2BU2KhxvO8iAQdaoXTZbxojVkyKFshcyNEtKeAOPVMGQc2JiJotioMQVdPjld0RdM9DKFaAJ6Hvs8k2910q6mcsa%2F01OFntJ0bmMUjUaSVhDDaIDXgby7N2igw%2BdbyvAY6pgGO4rlB4ADKnCRtJXlUKpIdmbDBoWZuZW0yprl5R3veDbq4JlN5l4Ctt25NpuomsYYh0qgJD%2FREx16fony%2BeSfXtgRW2e%2Fj83QLd3iGi2Tsq93aSxUmn5IOd8WxhxG5scdmrsi40%2Bx%2FRQ8hXORRxaX9UA3bNSkHqoEDLkfd2UdY0HIVDRB8NR2Mqn%2BKy%2Bwr6FQJlv3P3jNZA9ttl8pHhjUF2lpJ8qP%2F&X-Amz-Signature=b88cd2ba6c10779f11bad7bc4445a0a9f968de36427e772fef3b24e1cc4e1cf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7U5JM5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdXfZIZTSevi7jYxXvN%2BIZuTbJkvzTz9G2WMDvBaTTuAiEA8RcQ2ooOXmvcRqpusAeJv%2F451IXddBiGjxXF87uqEBcqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhYSddib86enpnGYSrcA8UctB%2Bov%2B8CZxKcz0cTg6SQshFOKPXLqOaw539GK9AIw%2BeMQhwzcEvFKZ9OhvHiC%2BEdVGPNKMj%2FvGh5FjDAZTbyCjOyOiyDykKgdMpdKXeSdC8caOoV3q9bzs4nepc%2FIw3MLEEev0wxxfvymPyfUYqFGYjdA8RscWvcd3sK9YWSJhThk8g2vD8Q6Tp0aYQc7IY%2FovfHs%2BhM3hPjXMMRaOxmP3zH0eUn3AxVJF7MEaPwyl1L3m3lyjKjxVP2%2Fg2OUghr1ZvSwnRLqDpwh6SG%2FFdjUCGAp0NeFPWXU4HPNcJzEX3HCvpMEa175uF%2BabvvvDeUye3JiIRlkS25BRckibGrJBx57ugCLXLEuXmf0EXQllCrOeIR%2FzqK0DqfMcVJAqzp6aYLWGypwCplSwXiXeBHxaPTyTfPbqYHyH4KkysMfPg90g8HUhrj7QtHOliZjgtLUQr91pgbfz7Ag2IKE8bp%2FMQ7u4HvXZCorHxggxd5SMs4Hn92OpzqjFXjBSu5PUkmtV9mDa7JU5BPf5ZGD0gDY3uXSCqw3dW5rXUnmA6ib8bQJMEuWycBbk1FoXutV%2F15YoxKMI8FtU6ki2o9C7F3antcUFvGIGw%2FK04QnbytW%2FCj25pEcMD9KmslMO7W8rwGOqUB4DgEUIHZYNRjFsqDZ3681tz6%2BpUsTbxgrkGrCpshcXLW57dch6Q8fsbUdzc%2FrXOcXThEAxQjzR9neTvEWyqpQ1qjdYjZHjFaN16MWhIP52UaGj7v7KKZPxwGjCzDAXaWCVQ5j5KVwE0145YZJWRffqlFKRK0lOATYoTO%2BO4Gy0kpIk00RgIYYlwYvBymeRJgiJkJ4VJQiGMQ%2FjQptUoMhRyEGR2o&X-Amz-Signature=3bf61c793d4f5e6026d6377e908a62d48ec86d46329326ba7895cbabb1058acc&X-Amz-SignedHeaders=host&x-id=GetObject)
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