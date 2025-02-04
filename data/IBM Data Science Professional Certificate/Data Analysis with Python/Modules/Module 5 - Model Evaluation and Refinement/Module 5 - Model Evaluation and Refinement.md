

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=55cad2a61385eed51756c591a98591766e61037db342bd37b7a1170e03ae7cf8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=d8cae9178dbc45c9b7b79bdf78b1eefa878a8df0e3b50dc46e155aafbf2e35b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=af6a3944453f6e3cae10fc67ef7139e5ce48c7b5d838c304680ccdb6ee4f4b31&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=9df0927222c20c1bf17005ce903aed289429a65e98794c035e1ef10a3fa4a3e0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=e8a418db7cf55dfbcfbc662813482e386d12d33ffe9caaa2eaffc6aadbe8c0bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=d40977380a9baaacf1db95bf9850b4aaa900d08b0a1110cd3c9a1dce423ac1bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=f3c5b6961f0637921d102a9de58dcd9416e61c37e666c60fbd81b412eae6cce3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=6e916a0460fc57e9430affa79f8610635e57bfe67ddcb85d257be825ac732a72&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=a296aee24388e776cb8f5e8539ce1107f139c4f297096480dbf9dc2995420d51&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTHVRQE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIBoYqv%2BzHI7TU7Z5H9WGMBBKRMlEqIiQfYFtPAQ2HZN0AiEA6Z%2BIeiX3LDhAaOP9DXEXNhviVeAiFkez8GIFAog8EKoq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDEgtbxSi1vAfzZU8DyrcA1N6EVH1B3EE%2B%2Fjd%2BLXO2pDlnYeMrBZkkkxUsRPOx1SY%2Bh9LzCzerZ1YQQxCLS%2BPp9P6fN2OOiDPsCpwL8WeSgtSEO54jiWXYVBcdUqiUNRfPTYSVusyVBHN48dpI%2FXJ077pVrqC4GqLPlCgEVMbH1NMIH8jNovhVOkpLnrWZ%2BCu%2BkH6dR6puY6JV3EoCdwqS6cKLb8%2BHGssm9j5Zd9e%2F7BsJuPIXbcjuS7jvhr7qbBQjg%2Ba7RCcqX1ZN9ccHGSw12mWcFkL1IcCN3gBWGN9ylOSZgvKIN2qdLqU7dkOHQikRXC9lIsI8GYjc8PpbYYgmuFKo%2BYddPOyR7cMoeIvFOV5Day6KEZIoYa59CH9HoGZ2%2Fq6jEhF1e%2BQ2e%2Fejvqq%2FfVPZ0%2BYD8TUrOS0XHrVRAfsC%2B71qvmRPPuVWtjJldvcbYZgVSuRP0%2BgTg8s5kr3WZi%2FwoQRr4dkpvQk%2FVh3rD%2B49SbMV7pIJlYTybQm7ct2AcUnbh14%2Bi0nKZe5XilipxZ%2BYSR0tL62OfLCf8hYaoqVHwcM85ERtVE%2F6QvWpWx3bsYKc%2FiAgGvks9cv5RvK3UELxl%2F9Zw%2Bn82JYJv7HBZ7lP2hixakxzCiUoPxnYwxNT0RUKhfpCO1wZ404MOD8ib0GOqUBetgb%2B2yuvU5BkSeapl7RmSpHJ6dPw52iFVvVT7VqRlrB5E%2FVqGIMVfpXM3ctKO1EINE5E4Fci2rpi6cZtvhOtvVOmUdarsNd8GOeZZlhZaflKtcvSLK98FFehH%2Bqj1D2VG%2BY5YLaTir0ibVtItFen7teXNJAdcR3i0Y3KJANLR3mp%2FjyYKjmFAlzpDVQZMvp60wuOx6wcG6Z95G8L4vVq4riFCg9&X-Amz-Signature=af360d0de4f0fbfb9e10e5624726c6fa4dee74f4eb3d1c25e9b1785a528a4f83&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTHVRQE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIBoYqv%2BzHI7TU7Z5H9WGMBBKRMlEqIiQfYFtPAQ2HZN0AiEA6Z%2BIeiX3LDhAaOP9DXEXNhviVeAiFkez8GIFAog8EKoq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDEgtbxSi1vAfzZU8DyrcA1N6EVH1B3EE%2B%2Fjd%2BLXO2pDlnYeMrBZkkkxUsRPOx1SY%2Bh9LzCzerZ1YQQxCLS%2BPp9P6fN2OOiDPsCpwL8WeSgtSEO54jiWXYVBcdUqiUNRfPTYSVusyVBHN48dpI%2FXJ077pVrqC4GqLPlCgEVMbH1NMIH8jNovhVOkpLnrWZ%2BCu%2BkH6dR6puY6JV3EoCdwqS6cKLb8%2BHGssm9j5Zd9e%2F7BsJuPIXbcjuS7jvhr7qbBQjg%2Ba7RCcqX1ZN9ccHGSw12mWcFkL1IcCN3gBWGN9ylOSZgvKIN2qdLqU7dkOHQikRXC9lIsI8GYjc8PpbYYgmuFKo%2BYddPOyR7cMoeIvFOV5Day6KEZIoYa59CH9HoGZ2%2Fq6jEhF1e%2BQ2e%2Fejvqq%2FfVPZ0%2BYD8TUrOS0XHrVRAfsC%2B71qvmRPPuVWtjJldvcbYZgVSuRP0%2BgTg8s5kr3WZi%2FwoQRr4dkpvQk%2FVh3rD%2B49SbMV7pIJlYTybQm7ct2AcUnbh14%2Bi0nKZe5XilipxZ%2BYSR0tL62OfLCf8hYaoqVHwcM85ERtVE%2F6QvWpWx3bsYKc%2FiAgGvks9cv5RvK3UELxl%2F9Zw%2Bn82JYJv7HBZ7lP2hixakxzCiUoPxnYwxNT0RUKhfpCO1wZ404MOD8ib0GOqUBetgb%2B2yuvU5BkSeapl7RmSpHJ6dPw52iFVvVT7VqRlrB5E%2FVqGIMVfpXM3ctKO1EINE5E4Fci2rpi6cZtvhOtvVOmUdarsNd8GOeZZlhZaflKtcvSLK98FFehH%2Bqj1D2VG%2BY5YLaTir0ibVtItFen7teXNJAdcR3i0Y3KJANLR3mp%2FjyYKjmFAlzpDVQZMvp60wuOx6wcG6Z95G8L4vVq4riFCg9&X-Amz-Signature=1ea94bdc751b50921499c5ad447999ec8d9410e0d96155ff68fc87f32889652b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTHVRQE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIBoYqv%2BzHI7TU7Z5H9WGMBBKRMlEqIiQfYFtPAQ2HZN0AiEA6Z%2BIeiX3LDhAaOP9DXEXNhviVeAiFkez8GIFAog8EKoq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDEgtbxSi1vAfzZU8DyrcA1N6EVH1B3EE%2B%2Fjd%2BLXO2pDlnYeMrBZkkkxUsRPOx1SY%2Bh9LzCzerZ1YQQxCLS%2BPp9P6fN2OOiDPsCpwL8WeSgtSEO54jiWXYVBcdUqiUNRfPTYSVusyVBHN48dpI%2FXJ077pVrqC4GqLPlCgEVMbH1NMIH8jNovhVOkpLnrWZ%2BCu%2BkH6dR6puY6JV3EoCdwqS6cKLb8%2BHGssm9j5Zd9e%2F7BsJuPIXbcjuS7jvhr7qbBQjg%2Ba7RCcqX1ZN9ccHGSw12mWcFkL1IcCN3gBWGN9ylOSZgvKIN2qdLqU7dkOHQikRXC9lIsI8GYjc8PpbYYgmuFKo%2BYddPOyR7cMoeIvFOV5Day6KEZIoYa59CH9HoGZ2%2Fq6jEhF1e%2BQ2e%2Fejvqq%2FfVPZ0%2BYD8TUrOS0XHrVRAfsC%2B71qvmRPPuVWtjJldvcbYZgVSuRP0%2BgTg8s5kr3WZi%2FwoQRr4dkpvQk%2FVh3rD%2B49SbMV7pIJlYTybQm7ct2AcUnbh14%2Bi0nKZe5XilipxZ%2BYSR0tL62OfLCf8hYaoqVHwcM85ERtVE%2F6QvWpWx3bsYKc%2FiAgGvks9cv5RvK3UELxl%2F9Zw%2Bn82JYJv7HBZ7lP2hixakxzCiUoPxnYwxNT0RUKhfpCO1wZ404MOD8ib0GOqUBetgb%2B2yuvU5BkSeapl7RmSpHJ6dPw52iFVvVT7VqRlrB5E%2FVqGIMVfpXM3ctKO1EINE5E4Fci2rpi6cZtvhOtvVOmUdarsNd8GOeZZlhZaflKtcvSLK98FFehH%2Bqj1D2VG%2BY5YLaTir0ibVtItFen7teXNJAdcR3i0Y3KJANLR3mp%2FjyYKjmFAlzpDVQZMvp60wuOx6wcG6Z95G8L4vVq4riFCg9&X-Amz-Signature=2489be0786724645d023a1e53d56b468894f7c6c85d1f3f004373bf7b214f36f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=f5405664e13c9988e3c0d54f841eebd8d774b1f025809322a65a5789fdad6cd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=bf5f14d87fe7faf98ec2a9c4e4d48b8c56ae60446ba7d5617844e73975d59df3&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=cad2f43346f53cb951913458a89778eb921945a3585da1b0088e17efcab9132d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=7db82c7f26c782fd982724ef5cd1cd495fc32418c7c80a42b9d56deeb906bd55&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=e8cff4b815b63b1fe451aefa7866daa854f0793d4c7e28459e8fc5f02824a543&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGLZLUXL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIC2zyvI7A9pWoqg6xwrPFI%2Fwbow7CnurvA7m%2BXyUL8HyAiASlfArMCEjc8%2FN4B2htet5QKNdjCs2fQHjMQNoJQ9Egir%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMN484SV9zbKKG6MAFKtwD5Yq59XQMg9MzV6K1NDIwIB3HsbIimKwAybvnr7nTrGUQiM%2BiAzrb8F709HGuH6kiBsrhDLsQrEsM4OTDRsd62FJLnXQKjBtNV1le4nN%2Bqng7AM7gf4%2FgiXqf5asC0K7f2TjA3e5pVeosTAN8xeZ3FSF1sMmza1Y0tzvciYhy%2BuIKYR8Nyvt5IqPktYEF0pl9J3%2FQGNsP8NVe6QvgxtKpVF1%2BD1uyJr8PHx6ZSlNllFpyQKGWoTwKaj%2Bpm0MmGGX3uOdenmQlI9XW%2B68rGZZ1chpX5zmy7c8AaPTC0zliq502Q8R8GTYi7ULRNthvdKzf7PXyY%2Fq3IHgmxpoK70E6GyTxBG3vHib63GmKL7iAvpJeJ0g78Aw5TRKfUUCaPVDZyQI0sQkumY6UM86aPPwH2p1JsRn%2B6%2Bn2SbHrWU4u32uVdp3nVlpqowvzNy%2BspJfB%2FnqWiqzoKaESvhWrJjtYIREwkp26W4%2BiarQ9QAc3BEKZWXRcOdwIcermw1PSlbPyG6X1ksTM5Z%2FaG14%2Fl8oJMDXnCpcuYDhSEESAvOiJRJfx3eUmvc1VRkQE5DmWJna6vBqu8sCPfNZz4vc2B5pg3EhioytrQBdg%2B%2FcCf18vSXeNfv1sLv2nAR2PiEgwgv2JvQY6pgG4NrJbuZ7YywpCIlr4Z3RUhBEg9nnGzIjAJon7IvCPleVRoKVfh9fKqgRXfuGpkGYcXcvQMn3dZVxogtPJGOeaW4fuI5hGe%2FdGDy%2F3Q0AIsfKX8sLJMG82ra5rmMdcqYBKx43Gc9RXk9%2B3rww6OW8SYhBqXni4kYgKjiMkAoLDN92axJAknSXcH7zq63%2BzrrIl%2FMgTfJSYDuA%2F2EVIEBGAhvljPiBa&X-Amz-Signature=709bc795d76c08ae2ecd44e91e851c7d4489069adb7bda0392f4557467487f93&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV3A2JVX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIB3pIlbgGlnZVQ1qat8pwzEgDWkrk0sZZmqrRNR75JNVAiEAvq09ZZbP8RzWeRl0sPtCxSugGdGXdBemzvnGL%2Fxiu0Uq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDF7m9%2FEVwqdjwbrfFSrcA%2BTYNLFlnbPBOVl75bXuAXafZu9qOFTDVTiS2RwIuQsQcoC5aD0UiebhA7q98wvor5xb%2Becyaq6OoOR675p1ku%2BKNOCKrDrYWFZOmMj2CutD317Ii%2BNYKHkY5TDffRvx40c4yOrSwtzNFzAwYr8UmjWVRHLUJWs7ozxYg1%2BdrmMc1Vfu8hNEqjVutENT7PM%2BFv7W6hThL492G17C0uryAmcFv7ezFkMeq4kJfagzTPpQdby1HReVOKCbn%2BbjLSgwQpiu1DiVTVeuUPoeg2Blh%2FhMZhAO%2FADt62C6s200kzr%2BULY90RcOhx8skkbiWANLbgqQkWqiUp0TDY%2Fo3lH7bWwBe8Xz8yGxftnUONLoVBqxpKeyXcNDmQcKWvG5HwyBDjYz%2BkW71XHAQm7hEv6xA6965q4z1lHbKvzVvOjx77feEKvXrNhd%2F%2FHvl8ItRcCWv9osXMx8kBoHPHmGXPzsZRs7MUMW0faaIU2nhEpl28w5n0c8Lqy40ZwkvS%2BctL%2BlJSoJqKrCoCyfYgKKSs4bLEJ9%2FPPGDpJn1EHzbXQEfCrBp05HchhEEPC2lY4mxRR2gmCEAgsFqOw1dwd5aDhv%2BrUfH0Zh%2F2IkDtxM%2B7XfvVoMRmxmweQYV5umRaBfMNP8ib0GOqUBajFX5K%2BoCsAFf7M44TZaGNBTHsTmARycimFcezYLZzAIJ8xE06czYhXX6MTiEJ3gVQQoiTJxFwf%2B6YBuPBuewpr7OzhQegHA9F6uTV8czKwtXcoBEAwpup6zJrp6IQa3Gug4yAzyhXYV%2FPY93Wx93ugbsz%2B%2FWdCBiOYSvmogz46jzAD%2F4nB2MnOzqndH2QkXuK5ZSdntFzK0Q%2B%2B6Xj2VO2FQJl%2BS&X-Amz-Signature=40a593ea265b0784b785896037468455cc5bb22e3de155b37eb05931904cf862&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV3A2JVX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIB3pIlbgGlnZVQ1qat8pwzEgDWkrk0sZZmqrRNR75JNVAiEAvq09ZZbP8RzWeRl0sPtCxSugGdGXdBemzvnGL%2Fxiu0Uq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDF7m9%2FEVwqdjwbrfFSrcA%2BTYNLFlnbPBOVl75bXuAXafZu9qOFTDVTiS2RwIuQsQcoC5aD0UiebhA7q98wvor5xb%2Becyaq6OoOR675p1ku%2BKNOCKrDrYWFZOmMj2CutD317Ii%2BNYKHkY5TDffRvx40c4yOrSwtzNFzAwYr8UmjWVRHLUJWs7ozxYg1%2BdrmMc1Vfu8hNEqjVutENT7PM%2BFv7W6hThL492G17C0uryAmcFv7ezFkMeq4kJfagzTPpQdby1HReVOKCbn%2BbjLSgwQpiu1DiVTVeuUPoeg2Blh%2FhMZhAO%2FADt62C6s200kzr%2BULY90RcOhx8skkbiWANLbgqQkWqiUp0TDY%2Fo3lH7bWwBe8Xz8yGxftnUONLoVBqxpKeyXcNDmQcKWvG5HwyBDjYz%2BkW71XHAQm7hEv6xA6965q4z1lHbKvzVvOjx77feEKvXrNhd%2F%2FHvl8ItRcCWv9osXMx8kBoHPHmGXPzsZRs7MUMW0faaIU2nhEpl28w5n0c8Lqy40ZwkvS%2BctL%2BlJSoJqKrCoCyfYgKKSs4bLEJ9%2FPPGDpJn1EHzbXQEfCrBp05HchhEEPC2lY4mxRR2gmCEAgsFqOw1dwd5aDhv%2BrUfH0Zh%2F2IkDtxM%2B7XfvVoMRmxmweQYV5umRaBfMNP8ib0GOqUBajFX5K%2BoCsAFf7M44TZaGNBTHsTmARycimFcezYLZzAIJ8xE06czYhXX6MTiEJ3gVQQoiTJxFwf%2B6YBuPBuewpr7OzhQegHA9F6uTV8czKwtXcoBEAwpup6zJrp6IQa3Gug4yAzyhXYV%2FPY93Wx93ugbsz%2B%2FWdCBiOYSvmogz46jzAD%2F4nB2MnOzqndH2QkXuK5ZSdntFzK0Q%2B%2B6Xj2VO2FQJl%2BS&X-Amz-Signature=360a7cbab087defac442ad461693b3bb9bafadcfb8856541a56820560681482f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWSHRASF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQDm3%2BsLGTWzbDvnSXvwkgjwgHCK8WSHfRfOZhREIxlKTAIgTv2ErpdOPB37F3p0kYRkei9vuy4wVO0qAGJ9zY65BZwq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDF1fzn3esGSwPBWMvSrcA4%2BBKCzfPhh14u%2B97SmtgkSO6zlm2eE%2F%2F5mJ0JgOKb%2BJfnjwsuLYxKMq0xql0M9UyJcpVxV9WuRAOGwnsxVO41Vj%2BqwaYXSFUmTG4ioJLQwduFFQau5lPQ%2F3BISM45xeb6WmcUY4wcOmWJEcB29wWpQ2NNSw3zjqyIThXh2lM8WZ4vG6n8q7htmzlfQe3Z%2BQIoCQW%2FGej4RCLCZgHMeiXEf7s74zabpWT7wrv4JY6SlAaLEmFpUWQiKkxZ7iyJX%2BxTuHXqa97RksMm3oNb0YGuYFtskGrRQ1zAb2CMq9sib8785G7FVAx3eIAppY%2Bsq5u2dURon2CoVlSrYk8BK40PZ1CbxP0NyZcWAXpWzimf69g%2FqIqjLr1%2Fh6%2FCvvUXtJJPLdEL%2BuIfWwF3VAYgdc7LSEr98l6edizD0TwjjRw%2BJUBB87ibUc71D1JHKscdMrM%2Fde%2Fp%2B4OeF%2FY81cuRW8%2FouPXeNRbfXKJj3PDqnOOR9jtwVTzwSjZDnMGmohV22H2RWMI5nKMNLX4%2Ba357JNbeOK2H4v5ZmxTLc6urY%2BEpMLYpjFD2T0dNmrA54lb%2B2%2FGTcCBbJB6pEhunu8vlDaYxgzrk%2FPdTooWUn%2F9SVafUFTw5%2BwJRKF2q5v1xdnMMv8ib0GOqUBOtxoIeUyvxzmQCGFT5l7ZK2fwfk88Wj4HMIXfcIJLVTNYmM3G9GYQANhiHmhoodiHOoxB50lYhF%2F6z0rVi4id2XDo43zi4iHnpgnim26HQ9N8kPq%2FkMyGPAhueQU5tY5us9iULL7NTbDDxWknbV3tYKaDSdaKmsqM1AqGIePYsKrfGkd%2FwBUYRWjrpaAvVQTtjaO1yPeO5Art6R0DC9NbYfeQcgS&X-Amz-Signature=7fb96781dbb3fa28076bf798a6481607a536d8b37b521a7a0f11faa45ffcb685&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LHZXQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCuY3ZjT0aS%2Baw%2BEIe3L%2BABS%2FTw1qMy%2BfAZLBqXq%2FD1CgIhAMLjz15Q%2BWf8hB97Xu7IplTf%2FQzdExDXWcUsjRMYvfd8Kv8DCDYQABoMNjM3NDIzMTgzODA1Igxlk0gfCWFok5kLbLQq3AOS4UCJTn1F21xvH8igEotvWt3FX0qeS9g63i758OT%2BGpVCT8BoORFdYWKDHsFjoKO1McHz%2FmTS1XmMI8X8PYm1k29O0eXV8aS1sab9ED%2FPY5A%2Fk3LQr4U49JfiVcAUGErm4iysUz%2BIoc3j0qvJ%2Fd9cB2vyxOSp2vk%2B8%2Fe1Hhh4RveF%2Bu0wrcrUPqCs3oW8l8%2Bw081T4HBx1%2FlbK%2BNLSTLXK9MWfLMikXw3ygwZ02eRmG7fdWtL3758YoRz3YiEjInPhFfGmGEt0zOExE9LSzWGVNp7DP1bldmQYWY5xsRz%2BP03tq9QrTLbBpTiwazjODAhyxCylr7dipVOf04tfR%2Fg2eqp1kri%2FxejJh2qX7LQmdu4eDl7RXw%2BgC7Be%2F1MfFd5G9NI7pAeRE8mb0GDEA8MoA3asfd9OdEwAt58scJm6efXtwX5lMCwp4gibm%2BtxAxH%2F7DrupfIOfvPLrJB%2Bw4PgaAvHrdG4%2FO4e3zQ4OchQNYq4LMzGhGN1ZXL%2B5k83ohKE0XdlLIgIVnJ1QBGBtEgFTs1%2BHWWLsN9FjETWMMfuDwMPV%2B6z4beBmm8TVOOBQAlKUy8kUgqX94tgSam2Nntojg41MZLcTROozVSg8HvEqTqa7K96QO5S2gypzDO%2FIm9BjqkATKr%2BOPm9W6jwN4lTwHq3LevnJS8Uxw9ToQ91DJCplVUxg83pJwys0XXyFiHMYWb%2FLC5MHdefMlW%2FF56pif%2BDfuSqfaPgAJDJT3nh8wAIEXAa7rvtiiU0FK5eYfGRn0VWyeHS3XSV7TxrDC%2FzJbNUMJibXDhppGr5fBcmLQ%2FCHAv8paI%2BxmudNOmOWf7mnBgnugIfJrYRkYIAMqnMEKORMVkKzcb&X-Amz-Signature=029b4d562e25f2f8edc03cc0b54b2c77f8231e6eff3ce9b029b900d997993da5&X-Amz-SignedHeaders=host&x-id=GetObject)
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