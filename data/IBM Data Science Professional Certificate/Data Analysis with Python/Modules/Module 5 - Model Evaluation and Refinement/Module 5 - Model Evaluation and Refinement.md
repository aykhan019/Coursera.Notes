

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=483c5c903a3a3ca830dc7f165375b84101e5b58334a2a8ff0107dd960092db3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=ea90d9fab11f8f406bf3b10bc77123a6c87ca6e8188a6ac3a362a5bd126bdb6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=c019dafb05bd32b35bc2b74e40888fdec64c3be1a76588c85c8326d02becd172&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=7067923935f5115bdc8121f768126915f0a4f2e85eca5a33761b8b3bba8b2dc1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=b5d746cb4ffd1a2296add3e14d46fdef0c8ab37340c787382a2937b0f046906b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=29aa5962601d420641c2fcb0ae00008dc7bce907479bb6b9b05d089c4caeaa5b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=e32f06527c825fe431444e75d2144de13bf23a5e95979c60a4390e316e3da294&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=c9fe3476c32ff2c243e610fe5fbf6b61ce501f64e751b0358f715baed13f6cc5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=e3e0564d7bd3675fa75a020eaf628b273b21a4272051bf067806d696304e6e2b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA66EV4A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH0XlUaSOYq2h3CCY0Nhc0y13mki4cxdYDo5CaInddNWAiBD%2BXVhPVmEEp15lpi%2FTkCEu1rLIZIrBbX0GAqKEJs7xir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMR5XsxB6mURGgDp4aKtwD9IMp%2FELJvnA72CEMh5beKZGCuQvJHT8AM%2BmaiN3MMWAfDdeh2Ndeuvz7l64j3GHadaImZ1khHpTTtLDZYqPD977ZflXChmRwvSjAxpxXv2OE%2FJCrRfm4KAhhAjft3nHlcd6tSYS1K1j5b7WRwjOWr9nuOXZfSKfotKU8WMr0UzDCCG2q7VKnOV%2BmXoHPeWWoePN2kAFAlFvuBZxnAM%2B0kLtQAYyQYoDsteeWzhh2JYA4hX2J9NVgBby7rhJjYGfBjg2L0bvTWvlckM5K8mwrmcgESOJGwO7S6%2FC%2FSX9CBepJ6Q2v59JWIheVkxcp40%2BrmPunTG9rfrHRvZ18XM6B%2Fe8KjEZ6iMMetJCPTVVqnAgoR44rPX4fD101z7h59W5Bohqvslikj%2F%2BU5AITXyq4iqDvgjGKIcuPo5JCGDc1g1ZoXJzBSg%2Flwj%2BAgPE6jzPTA53Y9hexSqe9AWZaU39VOFn9jDdtUJQJ81qFufkRUFrjrBnFK2YbZoAYjdEQYJvi3Gg9lCcmFXvytRo2rSM8VBnpslfCE0Xh2v343dXAAiksq1vkMwTqzfGT%2BN29Ay9iMKRV2GwxHd36RiEqcCRO%2FvPa9GMkybQB8CG1aOOagtwmamyK9DPr%2BxET7YMwsfOBvQY6pgH059IEkYqXXrcd13V%2BqG%2B5znfpeNsPBxyGdruEMdXJR%2BdaJC%2FbWuZI71mh8QFuvKJ7Sa1CB9fL5hNWwobvnbP9SscCttJ5ge1Id5jjoulofbnpntRFfn4dKv2Rrp6zN90W3gBb9Ir5IOx2plECWeAmiL%2B7wmJ%2Fjr9vKOSKvTWjYPfDP%2BNf2RCMzeTcV9YtIVcX9CzU3tBt0YHNJA3eGetK4AGW%2B7%2BI&X-Amz-Signature=dd872d5525be8591d10030021eeb0ad02c43bf99770b740340e9243cc557ed44&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA66EV4A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH0XlUaSOYq2h3CCY0Nhc0y13mki4cxdYDo5CaInddNWAiBD%2BXVhPVmEEp15lpi%2FTkCEu1rLIZIrBbX0GAqKEJs7xir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMR5XsxB6mURGgDp4aKtwD9IMp%2FELJvnA72CEMh5beKZGCuQvJHT8AM%2BmaiN3MMWAfDdeh2Ndeuvz7l64j3GHadaImZ1khHpTTtLDZYqPD977ZflXChmRwvSjAxpxXv2OE%2FJCrRfm4KAhhAjft3nHlcd6tSYS1K1j5b7WRwjOWr9nuOXZfSKfotKU8WMr0UzDCCG2q7VKnOV%2BmXoHPeWWoePN2kAFAlFvuBZxnAM%2B0kLtQAYyQYoDsteeWzhh2JYA4hX2J9NVgBby7rhJjYGfBjg2L0bvTWvlckM5K8mwrmcgESOJGwO7S6%2FC%2FSX9CBepJ6Q2v59JWIheVkxcp40%2BrmPunTG9rfrHRvZ18XM6B%2Fe8KjEZ6iMMetJCPTVVqnAgoR44rPX4fD101z7h59W5Bohqvslikj%2F%2BU5AITXyq4iqDvgjGKIcuPo5JCGDc1g1ZoXJzBSg%2Flwj%2BAgPE6jzPTA53Y9hexSqe9AWZaU39VOFn9jDdtUJQJ81qFufkRUFrjrBnFK2YbZoAYjdEQYJvi3Gg9lCcmFXvytRo2rSM8VBnpslfCE0Xh2v343dXAAiksq1vkMwTqzfGT%2BN29Ay9iMKRV2GwxHd36RiEqcCRO%2FvPa9GMkybQB8CG1aOOagtwmamyK9DPr%2BxET7YMwsfOBvQY6pgH059IEkYqXXrcd13V%2BqG%2B5znfpeNsPBxyGdruEMdXJR%2BdaJC%2FbWuZI71mh8QFuvKJ7Sa1CB9fL5hNWwobvnbP9SscCttJ5ge1Id5jjoulofbnpntRFfn4dKv2Rrp6zN90W3gBb9Ir5IOx2plECWeAmiL%2B7wmJ%2Fjr9vKOSKvTWjYPfDP%2BNf2RCMzeTcV9YtIVcX9CzU3tBt0YHNJA3eGetK4AGW%2B7%2BI&X-Amz-Signature=124d6add7db9e0a7e17a0f05a1046c3d6f95391595e8b8e6470026c40a8dca1b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA66EV4A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH0XlUaSOYq2h3CCY0Nhc0y13mki4cxdYDo5CaInddNWAiBD%2BXVhPVmEEp15lpi%2FTkCEu1rLIZIrBbX0GAqKEJs7xir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMR5XsxB6mURGgDp4aKtwD9IMp%2FELJvnA72CEMh5beKZGCuQvJHT8AM%2BmaiN3MMWAfDdeh2Ndeuvz7l64j3GHadaImZ1khHpTTtLDZYqPD977ZflXChmRwvSjAxpxXv2OE%2FJCrRfm4KAhhAjft3nHlcd6tSYS1K1j5b7WRwjOWr9nuOXZfSKfotKU8WMr0UzDCCG2q7VKnOV%2BmXoHPeWWoePN2kAFAlFvuBZxnAM%2B0kLtQAYyQYoDsteeWzhh2JYA4hX2J9NVgBby7rhJjYGfBjg2L0bvTWvlckM5K8mwrmcgESOJGwO7S6%2FC%2FSX9CBepJ6Q2v59JWIheVkxcp40%2BrmPunTG9rfrHRvZ18XM6B%2Fe8KjEZ6iMMetJCPTVVqnAgoR44rPX4fD101z7h59W5Bohqvslikj%2F%2BU5AITXyq4iqDvgjGKIcuPo5JCGDc1g1ZoXJzBSg%2Flwj%2BAgPE6jzPTA53Y9hexSqe9AWZaU39VOFn9jDdtUJQJ81qFufkRUFrjrBnFK2YbZoAYjdEQYJvi3Gg9lCcmFXvytRo2rSM8VBnpslfCE0Xh2v343dXAAiksq1vkMwTqzfGT%2BN29Ay9iMKRV2GwxHd36RiEqcCRO%2FvPa9GMkybQB8CG1aOOagtwmamyK9DPr%2BxET7YMwsfOBvQY6pgH059IEkYqXXrcd13V%2BqG%2B5znfpeNsPBxyGdruEMdXJR%2BdaJC%2FbWuZI71mh8QFuvKJ7Sa1CB9fL5hNWwobvnbP9SscCttJ5ge1Id5jjoulofbnpntRFfn4dKv2Rrp6zN90W3gBb9Ir5IOx2plECWeAmiL%2B7wmJ%2Fjr9vKOSKvTWjYPfDP%2BNf2RCMzeTcV9YtIVcX9CzU3tBt0YHNJA3eGetK4AGW%2B7%2BI&X-Amz-Signature=f4f44aa7a660ff7b929940441f84b2d9b37f18fedba06c0880dee022b7edf676&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=22f17bcc1a7b67d15e5712f869ecb2440d12bd584a3313a9a27b43b384857889&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=6f1fd50031a7e00022bda9b35d04284da42597137492f4140d72c771d9c7c60d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=1cfac1014e3934a45ed73196e5d139d7bb56295659667dbf906e1f243249de09&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=ef55dcfb75b294c73b42cc9cfcdebbaa9ffd14abb4f6fa2112a7ef0408a84f05&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=a01dc2c2fc211628e5bf50d42d20f3ccbb608348f4cdd735feac4d6337149e34&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HKUV57B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvzI6zHvNqVSuZbmieKBfHfCi4CshXkBhEFS29EGY7twIgLk0nfxxoabsActAXnufywMPt3yi7NO5fQizF08BihIIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJWHP9NOSHLzp5NgpyrcAyOcfL80V0sue95FpOK79h4j9Aq66YE2pxxfbd7FAVYGFGH1%2BB8Zqu%2FpLBjQvBQ1XGUZD%2F3DzbGhcXwIt7%2B72IjAqDOwuTW7Ia2XeMRE5bfCTxLQRDkLJgtIeAW6XSkIbCXI35y2w90tAofIcCPpmVjczesDgEuC%2FTKlMBOlU9rGE6NM8%2BwwuDHM1b8BTKIfGJ4tQjpEDRseYmAwifRWKDz5%2BH0HEWdt%2F4Qydcm%2FXfHh8k%2BkCBKQbTnoZ6SCMFbYevm5NNtcdRh7pysFetM%2FR%2B%2FOALC%2FcpFtFocFJA7n8gImp7UG3gk6uHcaqYfE8TyF8fWSWXO6RJmXT82pobPSlv%2BWSmXvDIDm59NN8J1VAeaYPSvigBgjECgKQIKG4V9i5hyuTWhH7OX2%2FFi6B5cTsN3%2BtQBPTmdxUSHqsTi3m3z2CQjng1PAJ4SsJwxVjw4d5Sr34rTSaTe8%2BijQ9NCdzcs%2BQF34CBk%2Fvll3EACqPSj9ucBmJhmkGHyoRo8%2FVZS%2FTjkEgSe%2BDE3oxNrMALgGIvHxw1c8oaVpjgaz1g8uhtFYEadqNIsfppYbob7IVQxSsHUjgCVM8um3lGpdtznaO6Duy48%2FeTFZS6%2ByJRBSKG6x3v9O5%2Fey2MMX65xqMKTzgb0GOqUB9wHD%2F2iKsW41H7GhqaNne5xADOKCziHJZx7%2FdCim2wet%2BXHjCxhV%2BPjBVe1o3DD8sfAfVZRgQCC6sFAaDcuDHWoAQRqy7QuAPK%2B%2BYtkhsRMN%2Fjws2uWYvT2IcUtBHnVq%2FgaiKsLQEnEEjNwgAW1LphbmAUQgg8gUuUpDkkpLrSFBdPsZLLM0FAIj1y1FLoYM%2F9fojdKEg3jygYBPycBDEqPVPT%2Fw&X-Amz-Signature=bd808ea4ab96e0cac3534a7a4e6dc2881bc7c92a020ce2183af181358b24e9b8&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTDPDBC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBf7HulamWltupKjKzbSu0D6noM%2BCpYPIqi9jpnkFFMAIgFGdKG17wAs3Ab47n%2BS9IxR31CBiOEZSvfqujkR2YaCgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHGmOULyODRlZ8xwLircA8ozr3SDXm%2FDC7FQLTJ18oNYuhqp8KyTjRm2FCVto6UI1SMXwZYeDb2wAM3mGMlg%2FrCKnuT%2FWuaL9FbkBOanGITC9AWxMWVXjvbheRaY3kFO1X0U%2BnDT5YIIr%2B2ElVdP39bXOGHpptAKGkRtAguNsqDzEom%2F%2BlfHUfbv0OZkVHMQ07f41z70lrBU5cqiICZkRNWbbOvgKD6%2BOTLY%2FlZxL60VdJVEAw4CeWz1mKcKrO0IeN5j5cr7OjLkuBjBUc8oT7BJWNaxFD36hS%2FSchDU73fjZ1KEoorAZZUFd7wmZhMw9vlmJVJzGwjL5K4mh%2FlNDKPI4J%2FYwS8jnGQNWiGZXeS%2B3Zggvvw5bjpt4Q1ExZ9kyGB4BN%2F%2FYibNrO%2BGVao2njFtx5Ptbw96BJfle1TWAmJyaxImAWaSuWiR5jFvx3R%2B6nhtVQikGRetdYI%2FdOnBzfc6erzX6PzPZDXavj0jHoLDr4bSTrgMIUMF6TTYI6j8oBhtuU9yN9tyo6su8nO7MYllXgFaJzQjmPN29dwobHqwdC7nvjE%2FlQbFjot4HGCynplsaDm8TuvTpyBHO5kgqPu%2B2GgfsRAfJrcuV1Ze3SDql5OvMXqXo%2FB7KX%2FWDFZYIqhP8rOCshVvLHgHMLTzgb0GOqUB2nbKKXLjBOB4r4gQC3UT%2BMcXNWn0xrZH1s%2BQ%2BQN9%2FNQChw6dSuX%2FigHctqEG3HbNgAu1tnq%2BD8Kv9EIKre4ycaxbiUzJu%2BoM2iGarT0au%2BvXkqiHe%2BHC8VHyiQf2hgOcOugAmnOQSGNYSkFqcoSMnsfoYLv%2FE1b0lfcqJq%2FxPG84tFp5BoD05AfJ%2FWX%2FVVZK%2FdoC2J6vMhmMdJkln6vQiK12yYKs&X-Amz-Signature=d4de2722f414a3274d8e4fcf5c5135f75d28d171b29387b2d6638c4b5fd20bf4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTDPDBC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBf7HulamWltupKjKzbSu0D6noM%2BCpYPIqi9jpnkFFMAIgFGdKG17wAs3Ab47n%2BS9IxR31CBiOEZSvfqujkR2YaCgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHGmOULyODRlZ8xwLircA8ozr3SDXm%2FDC7FQLTJ18oNYuhqp8KyTjRm2FCVto6UI1SMXwZYeDb2wAM3mGMlg%2FrCKnuT%2FWuaL9FbkBOanGITC9AWxMWVXjvbheRaY3kFO1X0U%2BnDT5YIIr%2B2ElVdP39bXOGHpptAKGkRtAguNsqDzEom%2F%2BlfHUfbv0OZkVHMQ07f41z70lrBU5cqiICZkRNWbbOvgKD6%2BOTLY%2FlZxL60VdJVEAw4CeWz1mKcKrO0IeN5j5cr7OjLkuBjBUc8oT7BJWNaxFD36hS%2FSchDU73fjZ1KEoorAZZUFd7wmZhMw9vlmJVJzGwjL5K4mh%2FlNDKPI4J%2FYwS8jnGQNWiGZXeS%2B3Zggvvw5bjpt4Q1ExZ9kyGB4BN%2F%2FYibNrO%2BGVao2njFtx5Ptbw96BJfle1TWAmJyaxImAWaSuWiR5jFvx3R%2B6nhtVQikGRetdYI%2FdOnBzfc6erzX6PzPZDXavj0jHoLDr4bSTrgMIUMF6TTYI6j8oBhtuU9yN9tyo6su8nO7MYllXgFaJzQjmPN29dwobHqwdC7nvjE%2FlQbFjot4HGCynplsaDm8TuvTpyBHO5kgqPu%2B2GgfsRAfJrcuV1Ze3SDql5OvMXqXo%2FB7KX%2FWDFZYIqhP8rOCshVvLHgHMLTzgb0GOqUB2nbKKXLjBOB4r4gQC3UT%2BMcXNWn0xrZH1s%2BQ%2BQN9%2FNQChw6dSuX%2FigHctqEG3HbNgAu1tnq%2BD8Kv9EIKre4ycaxbiUzJu%2BoM2iGarT0au%2BvXkqiHe%2BHC8VHyiQf2hgOcOugAmnOQSGNYSkFqcoSMnsfoYLv%2FE1b0lfcqJq%2FxPG84tFp5BoD05AfJ%2FWX%2FVVZK%2FdoC2J6vMhmMdJkln6vQiK12yYKs&X-Amz-Signature=37e29abd142ddab74b040de5d59e73511d60a7e253cd9e3d9abe5d7553fb1d8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUZMVSRN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVePeJ4o%2Bn5gvZLOpG1amJ7fCAggkva0Km5S4TH3JsnwIhAPCuCS9VVzHBZ1E%2BG9siLVVB%2FgCVBXDLVY9WbHj7R51fKv8DCBEQABoMNjM3NDIzMTgzODA1IgypDx6%2Fk8s%2FjjoMsgYq3APtOuDxlyfQAAHwxp%2Fq1m%2BUpC%2BkNSGJjMzL%2FOzgisvnbh5qIiSoBsQYkKNGxyNpm%2Bv%2FZnh6bR3wiImSUfnfti1XTpHlLsWc2T%2F19sv6s7A%2BbJKNq1X9l1y3%2FiRS%2BYkaOOw6J1NlwiqpX9zfpHjzxS49%2BAGR0ZWcmrxa82NaYOLqYq1F%2B8EPTKDiv1piAhnP35a0mXCiCsj2Ka8RCARpweUxIVdbxoJM35eVpttg2cbrSBPhF8eoD2wwQm2jI0IKUVPom6eswAAcjDp03X1zSCTJsNqdXUd%2FdQ%2BoAeNUkadyHT3Ty%2BQQO3AVRhK1tfoBy%2Fpr2SUS%2FI8PWxpZzLSTlcib7mizyMCB7krFkjUOrfm%2FnXSACCNC0y07Xr9WMz0nUUaLyBV4OY%2BnbNNCgrgTpFcwnNwysK0sub3%2BuYIv7bG0kuCMBR8MelS1%2BmkO5Buh1ndkSjJqgnyJ%2Bwswt%2FcCs6IH8V5AQqYUDhrQTwgAsIXYxAiyGxllRcJ%2BZZt%2FZD%2F4on3KLkAckdCVcAxJBd%2BZFDcaNiwInAkJSof1gQ2w9ch2JLZhoL%2FfkKQmVPgWSCm%2FEYsyHXcx8omdepoAhL3SB7TNkVYIOSJrCKhaeUxX5g3F5xskEChJlRP21JWnATC384G9BjqkASBv0dAl6ng5ux6XUQfBKWl9VrKfRqczzK5PfiZ7tJHbDJi%2BNHAfiUqL6JLSL6o90sKd5KoI3dVv0rzfyyvyaEZNXD9jrS667iqNUWIeFaBqey7xbVxUuI1pCwym7DajRpZp%2FgTkDrTALTAlOoY4aozueagMB1GdnsbLb4JJGBA4xsUAwA8PHNu88CoA8idiD2rsq81c9kLmg2okDK6HjCg4CPAn&X-Amz-Signature=cf721094c2affc39f7517eda8536fcba1ecc8882080aa11fa046af5e47bbb545&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VJFYUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHNstsCJHUt0jE91ds15Nwt5kzMcO61dCY92PRM6grVgIgeRmzFokDGbVwuLANMOpozGF4JjRv4vqmv1vRmhbU4ioq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBLmbVcuQWE8MVBnHSrcA3TJMr4i0op1sunkZewz7PDjEoLOmxAd1nsWfAYNw4LJKSCN1RBJ561De6Sf4YLIBMAnnstDyF69YolAw2WvaaIzfz1hCG3r3T5Vv81AbvMOmXtT4LdWLMQ%2FlmcBnrIvr5meEoQHWWfV7QSpvEMBnJJy4DpZMBPEfrRNo8J%2FKnLev6hWyqc4RO1wqfk%2BE8%2B%2B5ePvJ2RSX7SkmDu8%2FGINrd3757GnfKKV1y4nYUdjAQLGH75tKk2mENzg8lQeGjJf5Y9MISrgpIS5H678iOGBzwVI0dJPL6bHL6J%2BVY8mpwLwOp9ehoLU%2Fkb%2B5KfB8C01fNhC%2Bk%2F7CNlUXwsO0mTmds4QfymbgUSwwNjCRp%2FsuJqtjnyvCyAghZSUMM81L%2B60uQhWCvtfXF5uCdwfKMHyRtXc8GkvQtwzHyaw9lLNglvnDrmZuGdNz%2BaD7LFOhSqpNtlNVnEusKLlxjgos57m6PFywYfKwOf7bHSQqwFazHLGb6DgcieGXXdFFuXepFEJxK%2Fc%2FO5kIpaN3xUxJJ1yK3yuqnsqVdDxwNTtjijTdLcIA657SwG7xKxfZoV61vuZaArh%2FLcV3ntyuWa0QFhaGOxDQF8R9tEtmh2lAhW1P2qkk1Fg38fUOa%2B%2BXmqaMJDzgb0GOqUBB5mTZ3gr8qreQhZbjTmXYUQa0AeEd1LTdDYrF9wMKfC96OJdvuVFD2AesnjWfMpU%2BT07DbxWTl3D1OALbcX56%2B5yjh6UWpIAYhsZZLDgquysxkyh58XwdipJW44Clrzd2QTqieSTZRBKvTwiF9DGkKvee6TEqsP6UhDHmZHmEBEJjY7uPKTmsjhJaCf%2FF7sOAsBjqv2zXZWcwqFbfWmeKKXga4Fk&X-Amz-Signature=024e26be966f2e236cf7a0ddfde6f63020f75ac72de04ede068e0c3ea8d8dd22&X-Amz-SignedHeaders=host&x-id=GetObject)
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