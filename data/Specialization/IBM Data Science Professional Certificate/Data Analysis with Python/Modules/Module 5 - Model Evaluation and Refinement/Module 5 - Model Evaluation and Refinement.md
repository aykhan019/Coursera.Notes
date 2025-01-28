

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=61798fa2ac4e5234deb8b131ac6d0cd845ec7d70ddc9c7b77da2cac72d9c7e88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=e7cbd38e3247e6817c3d75bad99f56ab5b53d89b156ea6af3a6e5c70c9eb1466&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=d5336f2d2b2ddba4089aaac1d34d9d734cc4540de5233d86eed97acbe9906561&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=0a716e0f1db53078ea99cabc34fe492897c5a43844c9e38f14904eabeb0c5360&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=f87db1b6a625a81cb759e647b7910f8218416f6d607519aef4f4cfdf4e38afa0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=16c0971ae26da26aa5668cb4d5e7804b4510c3e1c7fcf4c91587d63403337918&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=7bc84b5a34cf38bc78f4b99ee2b5881b48eb1272f516a5ea8ca124f1f7f679bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=ebf6ab11b76b351045dcbbf9858ac056263ffe4bf94e6abf6ce965f2f2043905&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=06ae73c11851a5ae4b7c1b48af5c11611de1b8509cb7305cb0de8cd7aabc60b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5CCAPPN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIAvEgPDZmL0yYzEXwKWyPLiogSBxR4DCHUe88BOCP3EqAiBVxZ66d56YyPLRXgxetEocIlRedtq6aYoEXAOT1vKGaSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMaC987sniJbMC8BDJKtwDyXBPE%2BFMb%2BhGkp4%2BxurVwVSmbsnyTCwVj%2BYOLVOpc5nUhUwilsMvIlyWFNLJp3nXNyB8cSwyQW78%2FhUdiow%2BsRRqn4X6rD%2FhZgv6bF7eu3PuysNQ6nTbnKKJMK9sVBqpAkIKB2T%2FvtylgOEYg2qhZyLNGwStnu36aNSXtjawfk6cx90bNy88L8ZsVIH4O8bLrRPdPBrkXFUM3nKBKL18%2FRGyfUI7Ks%2BuYb9X6ApsVLc6Ws4R80cvFO89l8nFsx189Oa6DYv2%2BTdDfna8xYBVOrrcGn%2FSBUQPGsVhdju3mxk4eFFhJPfYZmct3yCVirZmyJC9mj5SvK3wQ71gRODaoGQ%2B%2BSN52EgnuKtfifT1aC3wfr6PAbpXZ%2BtMDPtHj%2FcBJlOZMHpOz8kiJvq6Zp0gv48JRUU6EPsq%2FUers2kc9XMnXVJn9zNseUZluN7c8kIBssTWYBnVH0cNdIJZo75u4AGMyXiMKF6eP81dXgUcPD8FtUVktmyG4cKsb4o9n4FzyzUVbji%2BUWy6UJVisS4f5UZM5JYXNKopHCKIyZBchjeP5CvlWFRqaDTqkWJaB4tmjEO7b1GxiOwu2tnXA2lJoicHAMUNkLk28%2Fc7wEDMFIa4n1F9HCqZxW2yi5Qw7JTlvAY6pgHGqQ%2FHYFyRaSgcIRpF1YbcaaSip120CMtg8nMoBVJFcz%2FOLp9dRuvmKhgpTU55QO1vTsk7NSi%2BGTfgw1kP7YDjRj2NtwfERzTAGl%2F%2BXnnbwu5qVwxybVWs5Dg26GjcwV9iikdU3lUYNOr4xaui3V2VrkG6F1SZ171l4uy3XIAQQ2CPblAhxfSKs66AMY4LIFOGQ2YVsvjTSO3aX0mwt2oJZXjkyhp6&X-Amz-Signature=c6d9273858d64b302b9ec742c5f55e9cddaf11a481d13cf26309c087eef03815&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5CCAPPN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIAvEgPDZmL0yYzEXwKWyPLiogSBxR4DCHUe88BOCP3EqAiBVxZ66d56YyPLRXgxetEocIlRedtq6aYoEXAOT1vKGaSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMaC987sniJbMC8BDJKtwDyXBPE%2BFMb%2BhGkp4%2BxurVwVSmbsnyTCwVj%2BYOLVOpc5nUhUwilsMvIlyWFNLJp3nXNyB8cSwyQW78%2FhUdiow%2BsRRqn4X6rD%2FhZgv6bF7eu3PuysNQ6nTbnKKJMK9sVBqpAkIKB2T%2FvtylgOEYg2qhZyLNGwStnu36aNSXtjawfk6cx90bNy88L8ZsVIH4O8bLrRPdPBrkXFUM3nKBKL18%2FRGyfUI7Ks%2BuYb9X6ApsVLc6Ws4R80cvFO89l8nFsx189Oa6DYv2%2BTdDfna8xYBVOrrcGn%2FSBUQPGsVhdju3mxk4eFFhJPfYZmct3yCVirZmyJC9mj5SvK3wQ71gRODaoGQ%2B%2BSN52EgnuKtfifT1aC3wfr6PAbpXZ%2BtMDPtHj%2FcBJlOZMHpOz8kiJvq6Zp0gv48JRUU6EPsq%2FUers2kc9XMnXVJn9zNseUZluN7c8kIBssTWYBnVH0cNdIJZo75u4AGMyXiMKF6eP81dXgUcPD8FtUVktmyG4cKsb4o9n4FzyzUVbji%2BUWy6UJVisS4f5UZM5JYXNKopHCKIyZBchjeP5CvlWFRqaDTqkWJaB4tmjEO7b1GxiOwu2tnXA2lJoicHAMUNkLk28%2Fc7wEDMFIa4n1F9HCqZxW2yi5Qw7JTlvAY6pgHGqQ%2FHYFyRaSgcIRpF1YbcaaSip120CMtg8nMoBVJFcz%2FOLp9dRuvmKhgpTU55QO1vTsk7NSi%2BGTfgw1kP7YDjRj2NtwfERzTAGl%2F%2BXnnbwu5qVwxybVWs5Dg26GjcwV9iikdU3lUYNOr4xaui3V2VrkG6F1SZ171l4uy3XIAQQ2CPblAhxfSKs66AMY4LIFOGQ2YVsvjTSO3aX0mwt2oJZXjkyhp6&X-Amz-Signature=b1fb22a63fbe7a7bfdb1bfeff4b2a83d0885608a30f2d58ad243086b971bb4d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5CCAPPN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIAvEgPDZmL0yYzEXwKWyPLiogSBxR4DCHUe88BOCP3EqAiBVxZ66d56YyPLRXgxetEocIlRedtq6aYoEXAOT1vKGaSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMaC987sniJbMC8BDJKtwDyXBPE%2BFMb%2BhGkp4%2BxurVwVSmbsnyTCwVj%2BYOLVOpc5nUhUwilsMvIlyWFNLJp3nXNyB8cSwyQW78%2FhUdiow%2BsRRqn4X6rD%2FhZgv6bF7eu3PuysNQ6nTbnKKJMK9sVBqpAkIKB2T%2FvtylgOEYg2qhZyLNGwStnu36aNSXtjawfk6cx90bNy88L8ZsVIH4O8bLrRPdPBrkXFUM3nKBKL18%2FRGyfUI7Ks%2BuYb9X6ApsVLc6Ws4R80cvFO89l8nFsx189Oa6DYv2%2BTdDfna8xYBVOrrcGn%2FSBUQPGsVhdju3mxk4eFFhJPfYZmct3yCVirZmyJC9mj5SvK3wQ71gRODaoGQ%2B%2BSN52EgnuKtfifT1aC3wfr6PAbpXZ%2BtMDPtHj%2FcBJlOZMHpOz8kiJvq6Zp0gv48JRUU6EPsq%2FUers2kc9XMnXVJn9zNseUZluN7c8kIBssTWYBnVH0cNdIJZo75u4AGMyXiMKF6eP81dXgUcPD8FtUVktmyG4cKsb4o9n4FzyzUVbji%2BUWy6UJVisS4f5UZM5JYXNKopHCKIyZBchjeP5CvlWFRqaDTqkWJaB4tmjEO7b1GxiOwu2tnXA2lJoicHAMUNkLk28%2Fc7wEDMFIa4n1F9HCqZxW2yi5Qw7JTlvAY6pgHGqQ%2FHYFyRaSgcIRpF1YbcaaSip120CMtg8nMoBVJFcz%2FOLp9dRuvmKhgpTU55QO1vTsk7NSi%2BGTfgw1kP7YDjRj2NtwfERzTAGl%2F%2BXnnbwu5qVwxybVWs5Dg26GjcwV9iikdU3lUYNOr4xaui3V2VrkG6F1SZ171l4uy3XIAQQ2CPblAhxfSKs66AMY4LIFOGQ2YVsvjTSO3aX0mwt2oJZXjkyhp6&X-Amz-Signature=a57417e573da2f146017c06cb091b7eaeac7591fe071b4b0eae265362aa2dba8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=14a22337d6098d37bf9f4d2c858816c69b9ca14835ad92bf2dfa40088d3d1fed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=8570a7ef8174c9a2b5d438493053584ea71ebba2c79dbfa2c431c9de0b4aa94a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=7a31b81c773e3a7a38260b3883998deff36c000074e9604f222d24c0142104e8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=e099d3fe374cca8b42dcd17d06af2b878e5d6ed3ec2af8079aa8c0a5912ebc49&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=7a91872ef78bb9fc791bc85e86d4ffdb3f0e807710cae85f53ed7a9532acc778&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TXAD3FX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIFUhVCgXjQfntd3IUcl9Mgv5otTd6qz1vzvXiqYM3kc3AiEAma6m8Nq5L7EvEvIXlhL8A7gFF%2FFx0kxX93%2BjFSGm5NUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEWb9AhxEK1FedxCoyrcAyrKPZ%2FRGzCvQeaZotGYoHAeqKY60bqDtkON13Q8BrHqWF0SCpqrZvgyjpzQWPFtnlGqT9VlDmm%2FjjuW8z5wa8ChXrKkhcB7%2Fmy5NEpXbJ99ybaGNFTad1dGfmGtnGPV%2BE8X%2FfPL%2FI7%2Bv%2BOElJhgWKCbd2NP84xF0t3tJqL3XgL8hx5m5V3DqMrxFdkBOuN37RZAVfA1xZDDVxCsO9Rv8uOx2eVDBoqgM1VHKXDkmC8MmLHinQfEGgHBdiOwTnLl3VdOJ0EQd9KoTlAQpCe5wcDcTo5lZDHPFWRO8USxWa6fHiYCPjw8Vsckdg9qKaimE3B5frMq9EVF4UDaB%2F156%2FvGtIk8CmWTQqlTJv4inBqrsmoPT2pUcd7W4ysPVFbBjDpr%2F2ztWxUHkZ5%2B2FHwMa%2B%2BbJ8YhqgbhLGLfYxZSYUiwZr7qPgbX%2F4lKk1C3EF%2BWbFzBGQDuUsghM6942%2F5omTYvdDcLFl0frPVsVmj08UJz%2BBAxz1pEUSaAnlCscNp4T9IRLvUoDgP1sMkrDfHD8woMyw0CUt0g%2FmQ3wtiXz3sH5V%2FwajH52%2FQDbwiQwVVyTthVhkYpltELv1DWqPiYDtmDFlRPWoA%2Fr0VaUq%2B7c79O6aTyPDDOMxxHONtML2U5bwGOqUBTW%2B8mO4XHP61eLMQGUOMmLjeUgoMn7MEVTNPr9U2GObOxk6Vr8KMHWzPFUbV5mi0HgObCkovWrZ3Mbe85XbbGzWhl3GbaEaVfGqvIJndcjLzubsvzZmghWVoRMziClgOs9QlUJ5OFYQgJgbqIzFh4Q05VbN9quitHpqSI7U9LzCZpa7geHItZIDWG92MRqWa%2BbbXyIzuZZTzU6KBzFYd7m%2FvV54j&X-Amz-Signature=b596d4f15927db977cc0a2b8736e16001504fa94248c3ab3d85a8a61f70c2915&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XREKE44N%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDRBxrn5mXp1ulvS05VG2Lkan%2BlxG%2F%2Bv6n%2F%2Bm%2F0gQvawAIhALk7XeJMyOcE7rw%2FahQvEwgazGemV0ocTdFpX1Wp2C82Kv8DCH4QABoMNjM3NDIzMTgzODA1IgyOTqJAcvWoR%2B7kGD4q3AOd6hsLefk%2BipIvvt1hJr9GA2KSDF0quzlfRmaVQcxnYb7aYeBjNYSw%2BMQ0iCBKsipG7gudZyiuHukVlot7uwck3demUmjHxXAaMWQoA%2B%2ByVI60eJiQvddLmcmESpV%2FL%2FzJ2W8KJpo8Eu9STPYXRTR5yIRqWjlXLA5ZekeWt%2BcDLU18vqG3eLIFPL6TxRvqKXrUrCVHI670lkjjsXkdFNuedg%2Bsuki%2BC0HdteXHSXfkKLbH9oNbPCSzSgiK9hYXGVUjl5zsz3VwpDoRRnEceh7MS6w5noX%2FylV8o2HKa0boU2bdH%2FCOd5Qw4LrC0DBRqGYA9hM9IWNDY99fc4IEl30KidH2La7WkZVZbWgIrA%2F7raINnIwm3Xa5Cm2%2BaflHh2ntWC%2Bx4NWPLH%2FjaOsqmbf5%2F5ybx17pQvWn8ouvRIIX1QLsSYf0qnY%2BdzrENXjRQvjFD7usjRx%2BxWXp4EsejBtePMXgcA29yaBfFD2UY2sDj79XWp5xRN3Lx1WBNiLXOS%2FK5GJ5mYxsZD83WYM31HXOjQGOrrMF1Ss%2FbNm05m%2BjBBvwwr%2F8hz8cLgAoFiJWd6dm0%2Bmt0qV0B013ccRGgm5ulYdu5gIbhHQo3LG1ItU5ZDcUzPzY8GrURWfsjzDWlOW8BjqkATRBFBBtp0CzmIo8kj%2FP34d2GgNd4DFF%2F680SWyB0wKAJJkCYQM1wWE43KYJLAt86vJYrLIjvNE8xlPycDgbGKm7xcHhhpqLjJnWxqvpN2er7g48bwk8JbTKRXR8W%2FCPjaL%2BFkf2yz4G4WRnQnlJtVku1jdthf12YiQDGT4xq50B67ZQdEaajP7UuZUuyqVlkMVuZF0MH469p15fYS4Cf6Tj2%2FIN&X-Amz-Signature=2189c923df5683fe701cb347072e7ee277f464bf01353ae0991054bb30d592b0&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XREKE44N%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDRBxrn5mXp1ulvS05VG2Lkan%2BlxG%2F%2Bv6n%2F%2Bm%2F0gQvawAIhALk7XeJMyOcE7rw%2FahQvEwgazGemV0ocTdFpX1Wp2C82Kv8DCH4QABoMNjM3NDIzMTgzODA1IgyOTqJAcvWoR%2B7kGD4q3AOd6hsLefk%2BipIvvt1hJr9GA2KSDF0quzlfRmaVQcxnYb7aYeBjNYSw%2BMQ0iCBKsipG7gudZyiuHukVlot7uwck3demUmjHxXAaMWQoA%2B%2ByVI60eJiQvddLmcmESpV%2FL%2FzJ2W8KJpo8Eu9STPYXRTR5yIRqWjlXLA5ZekeWt%2BcDLU18vqG3eLIFPL6TxRvqKXrUrCVHI670lkjjsXkdFNuedg%2Bsuki%2BC0HdteXHSXfkKLbH9oNbPCSzSgiK9hYXGVUjl5zsz3VwpDoRRnEceh7MS6w5noX%2FylV8o2HKa0boU2bdH%2FCOd5Qw4LrC0DBRqGYA9hM9IWNDY99fc4IEl30KidH2La7WkZVZbWgIrA%2F7raINnIwm3Xa5Cm2%2BaflHh2ntWC%2Bx4NWPLH%2FjaOsqmbf5%2F5ybx17pQvWn8ouvRIIX1QLsSYf0qnY%2BdzrENXjRQvjFD7usjRx%2BxWXp4EsejBtePMXgcA29yaBfFD2UY2sDj79XWp5xRN3Lx1WBNiLXOS%2FK5GJ5mYxsZD83WYM31HXOjQGOrrMF1Ss%2FbNm05m%2BjBBvwwr%2F8hz8cLgAoFiJWd6dm0%2Bmt0qV0B013ccRGgm5ulYdu5gIbhHQo3LG1ItU5ZDcUzPzY8GrURWfsjzDWlOW8BjqkATRBFBBtp0CzmIo8kj%2FP34d2GgNd4DFF%2F680SWyB0wKAJJkCYQM1wWE43KYJLAt86vJYrLIjvNE8xlPycDgbGKm7xcHhhpqLjJnWxqvpN2er7g48bwk8JbTKRXR8W%2FCPjaL%2BFkf2yz4G4WRnQnlJtVku1jdthf12YiQDGT4xq50B67ZQdEaajP7UuZUuyqVlkMVuZF0MH469p15fYS4Cf6Tj2%2FIN&X-Amz-Signature=a7f41dba6402a93f8e847b8f7457fee66de5fa90464976b285afa07edd0e1915&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBCCKVBS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDxo%2Bnx5IoYD0KxIJYT%2FbyFihJXcVgB4pX3SXz1MTaE2gIhAKALjd9icmmPsPvGhkpKPyug84QZ6XwVeyRS8czto1KwKv8DCH4QABoMNjM3NDIzMTgzODA1IgzHeZoszvsdWa2Jb2Uq3AO211tjGEblU6Jeia2tpeigfulPJt5C1ZHishK9ruab%2B7yCmj7C2riAO0ugM7zzK72jHenUtELvTH8ykeHXtxM5JdYLy1EQbWzUAPsDo%2Fqgs63HrT8%2F50sL8LzpuI18RQF1ky8I9LIB8Hs1jV%2BU2pbJH0zFVpJcgnVav7cDzY%2BUKl8oFcFzq5TOG4nXCKT0VVUAvVQ8UbVzAE8RrliyXqAwK5vCaCMG4KBherWSureBrzEdHb7eABcm3UfGNEC6wGVXuemsCpi4yFbeYGzOo0dFG%2BvnBTFnVe3YjscnJXV4a8jrUd%2FAj28YV%2BDi3UZc5Qf7OJYzJEVKaPTZdUAmzGG%2F3tagnpk7X80h40QDA2Jm4K%2B%2FYwz5wNx9j4znJMOBfzqBFzcF4zGxuDWEvh36%2FOZXb1ojBJ%2B%2FpLzjcSJw4pyZ6tF%2BYscbeAK3czgXjFCTuuWGEbEuIxLirz56oEmQhFulJfgd3UGs4AcOAflOMA6stspewTuTlzOwdJcu9X93aZxy3r7SkO3z01%2FmPb3ehW3D0c%2BqxHUXgTrWtRun6kR8YoqcOys2dIIMlXq8cstHzg3uqLMqwUgJLRWvlooN1b%2F8POzWa1st3%2BLxZmZ%2FzqteotcPQZCBMzIVkr7GxzDFlOW8BjqkAVGpc8heI2MQQ%2Fh5rouYyDCUC%2B%2B%2FsukTYj%2B7rW8LJ3EK1LDDNcI4zmD1ILSBh3wCItJVVHRIBDQaJGHFNiclj3LQjFqeRpjE9y%2Fq2kHnoC28TU1VNz8jfEuqVf%2B5AI2d3QR0fmjLQh%2Fw%2FWPySj230Ot5xUuH%2F8n4jJ0ouuaJ9m4Jyd%2B7kEFg5Z1xHZY1eNw0lVDs6RofZ4Bbt4kbX%2B6UzQpjAOcp&X-Amz-Signature=eed4a7a7e31d63ee77121a3412b6efdec394bf3251676df4a521c46f26416057&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R5CJ4TM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEN8I7GXnNz%2FvrFo9lIoz4tWNPPCtBK9r5aKa3uKqxvBAiEAxjaccecV%2FAwSPKfT9IXyxtTmEsC2lfVPm9EVZc8ALHYq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDM6tzQcVAzB9DbilqCrcA2%2FyCZiUXQ%2Fn9LnzB6MgfEV%2BvBVG7wLAq4L9s66xOW0gVmfnec8a6zFbGNzk0b1a0sKVpi8V0A9TJGzjtRbVF4JBO7cDhkZutihXd1sTABR5RiMs6iPvDJXWPye1B1qpI8%2BywP0WQJ0BXOkoR2i%2B9dLF6VLjTjg2Xz3J6ywzVn3JeTG42NWmLRfTdBBOqYycBYIQMFMz7gBD7xKRxX569%2Bm9BRqo%2BesdeGlWceMbDISoIna9ZGVkaOZYg0Ned7Mh9YdI8BkCAV8PFGlssO7X6qU3goo8t%2BSbZFgz4TN6RJlYxrzccZ6siwauuCGoq%2B4XsiUfZaHfjGcbwbTqfoRJkbb2PyUjmZbyKanh2gnnZhSxbX1aGGNboIl3sjHXpPCaZy%2BJHXvupn8X91SDKsJOtr5m7%2BwnKNX%2BO5i8mVoVqVPuQOnujECGTygmPaiVW5mKzF1jV%2F%2FjgQaZ3E4qd%2B2jkBF5rrovJUkKl0xjtaz1DkWHalHU7gFTvMYnfawk645oTA2sQ2ZrmlF38G0TRlJ%2FrzNoKlSUGmGUnD0%2BBPDVOpL0Ap9a33ACLpxreNggAjbS0UZq4GAfHl6d1yhvlE0XlgaMGRLhaIqJ7w8CE19X7cTSkxwpyzeWeQ4e3QStMNOU5bwGOqUBPKQ0na4D31x6IshAKubSe3H0r%2FOSKwjxVx9PJtoV29D7vjgkyYSeBx1NNRVctnFXxqQkWaJ1pAExJ0%2BG6Yev2IVI0PA59ARFvHtWAAUm6VO2oYuuxO044JBsSQ%2Fdg9dA8N4qO56DPUZXcRuJhNyZMzouhn%2F4RBDgTF%2BGKePgaDj7x61ibBg51bHg4nReUoMK%2ByAxmDvmaY%2Blk6quTpP4CfJoaNJT&X-Amz-Signature=58c0860f13a31fc0dd32567a30c6bc2477c6f08e92861321f1488fe4715e7e27&X-Amz-SignedHeaders=host&x-id=GetObject)
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