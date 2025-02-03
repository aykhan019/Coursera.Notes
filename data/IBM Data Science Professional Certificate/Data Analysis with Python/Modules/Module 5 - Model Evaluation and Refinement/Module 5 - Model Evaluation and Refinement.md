

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=e4558220d92bc5eae4b719beee444c5323e7f487a546faf6087d14fbc718cb27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=bc8055ca5bb951b111e572fa7917a8791f4271fdc94325dab20a6ecb0b2ef00a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=760cb8d7a221ac8648b44ea4779962ea0adc2259fabc8d62c06ffd94bf0958fd&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=bc96b3836abeef636f1282aeb1667f559457b4ba14e61ec008f7f6b3d18d0d47&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=52e9a0db91c9ec36b22e33f7b93e2e28f9e4ef84f555a0dad8b283d6c087f7ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=818a0efb4c18e834b89cf9723b1b81bb89a1c636dd8031069fa64fd5ff0ac564&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=637bd9d15a762b62756e616580e03e9b24bcaf17ea15f13c4fd1a62ffad6b6b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=a56cb58d232f571dbd15632bf972602f8e9e77625acb6a23c8760e3b0e5848b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=dd6cf18e45e73c7a05af0f206575505b51f664c475bcc410d38c7b8645cad17a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHFZ2Y2L%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOIKFyhpXmt0FsTaO%2FxubEm4zqzgr7DcigVCPN5PCmewIgNu10fjRwi2bU8%2FrLk47MREEa2Av%2FR9lIVJdvXgrPFVYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDAko5sQ9EDLehSjvJyrcA4FCRqvKBZC%2BhUApLQ0uENrVR8%2Fv7me1Vzt465%2B8EkKwcz6iZksTTrebeXAizCbnHvOs4EI2xWwLtHdr5xJ0XYR0OfvcDh5CqQN%2F%2FmPL4mZ83MeNuhxbtlx%2B3c6BC0%2F3KolW1InsIuh3Fq8r7KedDdv4pflHfz7dRHetCGoGj%2B7LzPhz2nVxGjPiwCCEziA%2F0u9i1B2W5%2F5YcPEMt3%2F5JWMmHsUDqP8wYRnJrbfF3l1svzfcIvrkcX65qdGJiEZx%2B38xUm3LRaq%2FPovfY8HtgGxWeWqOPou7fLTfgYW%2BlQHKbLOhJ23N%2FDO4yqF2q449sIpwrXSYjxxxjfIjqQQG5KVnCCx0jeyguRy9w4eJqpzoiEiRLzy6xQ7vbJchUZlP8sS9rUqcl3urffQNdPazfAeiQ2klTWyhP%2BboJJieV%2FGHlrNWpoy0zjowbR%2FHuQTi6LZKb9ILM5Jc8ZDtwgGFzyo%2B350e9ebtdkz3MtbOwwu6gwl2mOMCoRjcJ7dE2ieVa%2FSFKJz8%2BbnJqkhKHSitSmxD2kOcy8dtxFfryDuQmoI4b%2FTEJLsgdNp4ibWFc111DuBGidUl8DGhFlmoNqEEUuAscwwZ%2B3yaDJ%2BBGh65kfeb%2B1LWk%2ByFsepuiwl4MNy0gr0GOqUBpx59kLHSi7N3g7e2tElC7NYqUhpQzToEnETLmh7TlLn1BIOyfrxin7gOJq969DaCvY7qNfjjPH0W0sRHESsyJFy5Wd%2F6i8s4XImVy2yO5ZNFZqWux%2Ba%2FuP1ygtMJFAb17LKIBVngqpUZRWPiG9oFf8OE60AznjBHlmSwPzuloeGtaa5l6m27xMAcb%2B975AmEQqnUezkGgYTPILRybJ2%2FWFG%2BEhzM&X-Amz-Signature=0e7df45d921ebbee07b1e42db94967f341ddd384e5388ab8c496ed78bc2b3106&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHFZ2Y2L%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOIKFyhpXmt0FsTaO%2FxubEm4zqzgr7DcigVCPN5PCmewIgNu10fjRwi2bU8%2FrLk47MREEa2Av%2FR9lIVJdvXgrPFVYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDAko5sQ9EDLehSjvJyrcA4FCRqvKBZC%2BhUApLQ0uENrVR8%2Fv7me1Vzt465%2B8EkKwcz6iZksTTrebeXAizCbnHvOs4EI2xWwLtHdr5xJ0XYR0OfvcDh5CqQN%2F%2FmPL4mZ83MeNuhxbtlx%2B3c6BC0%2F3KolW1InsIuh3Fq8r7KedDdv4pflHfz7dRHetCGoGj%2B7LzPhz2nVxGjPiwCCEziA%2F0u9i1B2W5%2F5YcPEMt3%2F5JWMmHsUDqP8wYRnJrbfF3l1svzfcIvrkcX65qdGJiEZx%2B38xUm3LRaq%2FPovfY8HtgGxWeWqOPou7fLTfgYW%2BlQHKbLOhJ23N%2FDO4yqF2q449sIpwrXSYjxxxjfIjqQQG5KVnCCx0jeyguRy9w4eJqpzoiEiRLzy6xQ7vbJchUZlP8sS9rUqcl3urffQNdPazfAeiQ2klTWyhP%2BboJJieV%2FGHlrNWpoy0zjowbR%2FHuQTi6LZKb9ILM5Jc8ZDtwgGFzyo%2B350e9ebtdkz3MtbOwwu6gwl2mOMCoRjcJ7dE2ieVa%2FSFKJz8%2BbnJqkhKHSitSmxD2kOcy8dtxFfryDuQmoI4b%2FTEJLsgdNp4ibWFc111DuBGidUl8DGhFlmoNqEEUuAscwwZ%2B3yaDJ%2BBGh65kfeb%2B1LWk%2ByFsepuiwl4MNy0gr0GOqUBpx59kLHSi7N3g7e2tElC7NYqUhpQzToEnETLmh7TlLn1BIOyfrxin7gOJq969DaCvY7qNfjjPH0W0sRHESsyJFy5Wd%2F6i8s4XImVy2yO5ZNFZqWux%2Ba%2FuP1ygtMJFAb17LKIBVngqpUZRWPiG9oFf8OE60AznjBHlmSwPzuloeGtaa5l6m27xMAcb%2B975AmEQqnUezkGgYTPILRybJ2%2FWFG%2BEhzM&X-Amz-Signature=aec60c90d56ab9ef7594098aea813bd03ca57cadbebdcbc5bac856d54d9c6044&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHFZ2Y2L%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOIKFyhpXmt0FsTaO%2FxubEm4zqzgr7DcigVCPN5PCmewIgNu10fjRwi2bU8%2FrLk47MREEa2Av%2FR9lIVJdvXgrPFVYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDAko5sQ9EDLehSjvJyrcA4FCRqvKBZC%2BhUApLQ0uENrVR8%2Fv7me1Vzt465%2B8EkKwcz6iZksTTrebeXAizCbnHvOs4EI2xWwLtHdr5xJ0XYR0OfvcDh5CqQN%2F%2FmPL4mZ83MeNuhxbtlx%2B3c6BC0%2F3KolW1InsIuh3Fq8r7KedDdv4pflHfz7dRHetCGoGj%2B7LzPhz2nVxGjPiwCCEziA%2F0u9i1B2W5%2F5YcPEMt3%2F5JWMmHsUDqP8wYRnJrbfF3l1svzfcIvrkcX65qdGJiEZx%2B38xUm3LRaq%2FPovfY8HtgGxWeWqOPou7fLTfgYW%2BlQHKbLOhJ23N%2FDO4yqF2q449sIpwrXSYjxxxjfIjqQQG5KVnCCx0jeyguRy9w4eJqpzoiEiRLzy6xQ7vbJchUZlP8sS9rUqcl3urffQNdPazfAeiQ2klTWyhP%2BboJJieV%2FGHlrNWpoy0zjowbR%2FHuQTi6LZKb9ILM5Jc8ZDtwgGFzyo%2B350e9ebtdkz3MtbOwwu6gwl2mOMCoRjcJ7dE2ieVa%2FSFKJz8%2BbnJqkhKHSitSmxD2kOcy8dtxFfryDuQmoI4b%2FTEJLsgdNp4ibWFc111DuBGidUl8DGhFlmoNqEEUuAscwwZ%2B3yaDJ%2BBGh65kfeb%2B1LWk%2ByFsepuiwl4MNy0gr0GOqUBpx59kLHSi7N3g7e2tElC7NYqUhpQzToEnETLmh7TlLn1BIOyfrxin7gOJq969DaCvY7qNfjjPH0W0sRHESsyJFy5Wd%2F6i8s4XImVy2yO5ZNFZqWux%2Ba%2FuP1ygtMJFAb17LKIBVngqpUZRWPiG9oFf8OE60AznjBHlmSwPzuloeGtaa5l6m27xMAcb%2B975AmEQqnUezkGgYTPILRybJ2%2FWFG%2BEhzM&X-Amz-Signature=1d5c370796b330fe709c4abc10dc88fc1ca16f7dc6ddfc507f9f2a876bf2b077&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=5a1578fce7750fb5469b96d19e9fb3786368ffad3a757a4fd8e7a765fec305c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=8ef6c867864a3a8b7a8babf11f3046c94d7b5dbd8cdf33cf025da4fd52064c50&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=780175458684381c996ff95c4bded8979c649e355445f14fafe9f70d29208237&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=f8e53b0a310ef5452ee4103bb140ef4a0603a8f1f6bdca2b20e3ad697af9fb0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=fe11725ead01aa79e6162230fa5fef971d8d27db22df6b79afdb0d9b8060cbfe&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VETL4Q3J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZyiLGo3sAzWURGcSONSSDg4Kor%2Bn%2FDfvI2a%2FthSLynAiBSdxWuWiKUseIOhoNXz%2F092qn3YhctU3mzv14AnxYvvCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMMeUWSa4YRYLr59NmKtwDd%2FGHTv%2F0HTUKdb%2F8HHcFBUcTurYF%2BWMcF%2F2fMxMrsTUFQGzkEuntL31rOLgWKVyCAswv1cTLOB%2FOr2lTbZ%2BkQE1OpmySznd2gGRsIzUbg3En2QAT39LuMv6EcnDZGihVE9fFa02wC5nY376EBR4VJz12fSEqSWlrUeI1yaz9gN9hLgA7w7wFCMgBDvLXKEo82scrfX5EQqVltwUJAjsU0JUCwXGRUoh4rNVA%2FHqJlY8NqFoIbyF3OnEfp6Fyre%2FnBmoDg0kumtTVV2yBo%2B9lSNqzxrJROVqp9brsDyLvwkT%2BiW4qq8NeDJStWzHnQNKZeIFcE9nxa%2FH%2FvZifMnl55BN3vs0hmq%2F6V2tTq6%2BAbwyeRc803uRhadkFWAKVHQvSqColZ6cEbvQlpwetn2AVmFl8WHKEeHI6pRgLKLO7siU2g8DA02QAG1rzO6S47Ql5dVFz9XT9xQWgaY0znRV0DT3u2%2BoxI2OoMUUp3EdDbefLLROJlz0CL3dVhe%2BYQiPpIrM7Z18lsXig%2BQSdQjCRn16qqeMgUbm7bmlDbM0C692VfDU%2FrdhS7TxXchta4jB0ltdiqSfH%2FnOjPKvu78loll%2Fy9fXu4jL0LKLhSso%2FjWpJYbVaBaNug%2B%2Bu6WAw2LSCvQY6pgE2dwDi8eTHDWrJYCAoXBs%2F1nTC8ENwmz1mf0Oriaj5IowAVuMmUsacPhEuDWYkhMTt%2Bvl2n6inmS%2BWsGm6A2IW8dPN%2BczwHHAGV%2FBvqufvwwTjp4Rl1lAq9uZS1%2FF100Fol1x6WUk0ML7u7MOBfjlFmFUbwbmP4x1nN7xn5ck8vw1fbVkJ%2BIKFZkHFVxuo32oEDug7%2FuWGxXN6IGzfiYdHuwkqQY7C&X-Amz-Signature=7302eebaf955a40983c3f1759ad32adbea8030cd48e6cb6f6767edb9be643c4c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVG7ZIHA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeez%2BeoOTUsBgrYwtc%2FFcMQzBo0BjD5p0AXh1fUaOADwIhAIDw16mmWzybSI7on349YTJYCO3X%2BZn9FbjjTI2AatDZKv8DCBQQABoMNjM3NDIzMTgzODA1IgzWYg3MgUB5rPtHQ6sq3AMUTp7s4R0s0Y3hwl33bTrXOYwZlcokD8VcWqy3of59hrXreTl5%2FK5U49nMt8lYa5R%2FxmNMMjgZ9rvucm99JlPtn4ypZlH%2Fz4pCr5aIe8y0GkPHcoKwwGRjHjgMzYcHinMcIJ7T39Rmiw6FDxB4yDIv6440NAE8xYFpMS8hQzNYC2rcieK3fcYJ60Oa6SIgfufHXAHcfj4qKKMldQz0%2FLdcV28Lb%2FQln5V0MHru80nMTmVysTiVqdkVIAXd1wPOtFPQw4VvrTHbfoiu5CCg4AqAocPbp3o4zSuZsXsNbr1IVYKpjRyM83S%2F%2BSms0fEjs5ek4SSL5g8WBTmMlIeSBMPVxpLjT4JIpmYYSo2BiH0csAxFkH3ZYwhzP%2BiaxeV3FtL079W50C%2BXGw6xwlsShNt6MiBH23Nf5HFcouVESR7HYv4Tkx6yObF9ru%2Fz73qZILV1Jj11UyqwUhgl9ubctXRSFosxH7j1Xt2JVBObsd%2F8moAJ%2BQla6SjehqCv479sooPlRwPIGJda9l%2BzzYymhBC85aWFO0XFdFjvQYfNhTnsRjwrgWXDQDfRqKx6MvG51rIHDa1m8jNrNSOxTlJfdh7Xjpjo9w9QgkCg6uscigz9mQv3BfPCNJ3uFJ9%2BhzCVtYK9BjqkAakfF0yh2pj0hmxLSOUSZPVkljXYvtol%2F%2F6VkL1Z6n%2Bp%2Byf8vFq%2BRYjj1IiZoqm1iOtSAtbQf6Ly84XCElSyaqSElZwldv6l2t0ShjXYkK4bXbf2o16xxxQeL0hidT3TrDGnjR3Ag%2Fxs%2B4U8bAYQV0HGYqWuOCC9Bpg0uOFDdXoKFetv4E7gsu6zT6TtPsbSROjNN%2FVp%2BdxRmNyKV9J9NFVZGiML&X-Amz-Signature=b3d779d2b2960428bf0d955f5c48b7bc969f91ca7e94a8acdaaefe6b336616c0&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVG7ZIHA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeez%2BeoOTUsBgrYwtc%2FFcMQzBo0BjD5p0AXh1fUaOADwIhAIDw16mmWzybSI7on349YTJYCO3X%2BZn9FbjjTI2AatDZKv8DCBQQABoMNjM3NDIzMTgzODA1IgzWYg3MgUB5rPtHQ6sq3AMUTp7s4R0s0Y3hwl33bTrXOYwZlcokD8VcWqy3of59hrXreTl5%2FK5U49nMt8lYa5R%2FxmNMMjgZ9rvucm99JlPtn4ypZlH%2Fz4pCr5aIe8y0GkPHcoKwwGRjHjgMzYcHinMcIJ7T39Rmiw6FDxB4yDIv6440NAE8xYFpMS8hQzNYC2rcieK3fcYJ60Oa6SIgfufHXAHcfj4qKKMldQz0%2FLdcV28Lb%2FQln5V0MHru80nMTmVysTiVqdkVIAXd1wPOtFPQw4VvrTHbfoiu5CCg4AqAocPbp3o4zSuZsXsNbr1IVYKpjRyM83S%2F%2BSms0fEjs5ek4SSL5g8WBTmMlIeSBMPVxpLjT4JIpmYYSo2BiH0csAxFkH3ZYwhzP%2BiaxeV3FtL079W50C%2BXGw6xwlsShNt6MiBH23Nf5HFcouVESR7HYv4Tkx6yObF9ru%2Fz73qZILV1Jj11UyqwUhgl9ubctXRSFosxH7j1Xt2JVBObsd%2F8moAJ%2BQla6SjehqCv479sooPlRwPIGJda9l%2BzzYymhBC85aWFO0XFdFjvQYfNhTnsRjwrgWXDQDfRqKx6MvG51rIHDa1m8jNrNSOxTlJfdh7Xjpjo9w9QgkCg6uscigz9mQv3BfPCNJ3uFJ9%2BhzCVtYK9BjqkAakfF0yh2pj0hmxLSOUSZPVkljXYvtol%2F%2F6VkL1Z6n%2Bp%2Byf8vFq%2BRYjj1IiZoqm1iOtSAtbQf6Ly84XCElSyaqSElZwldv6l2t0ShjXYkK4bXbf2o16xxxQeL0hidT3TrDGnjR3Ag%2Fxs%2B4U8bAYQV0HGYqWuOCC9Bpg0uOFDdXoKFetv4E7gsu6zT6TtPsbSROjNN%2FVp%2BdxRmNyKV9J9NFVZGiML&X-Amz-Signature=c9a3bf7cdd5bb6934adafc834c2788f17264fcd50881467d8afd77485b0c8a44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEIEC2M5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCPSTvpoJ9loyNXeebMPnefy0wEp7PB6CMeAsVViEmmAIgWalivnXCy0kABZHLOYjkhbE9WoR2Ti4QE2Ma9C7qXrwq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDOY%2BrDxGvOMTOkEPrCrcA691MmiOzpR%2BLgD20NF%2FipXw4JSAhp9LN8Z7prOAIOS6maBASf%2B2LRhT6qdmvqyTn7BSgptewbO%2FRMYv3bSBW6tK%2BC85ruhDx2yV%2BvEQox5lh5fNaZnopZFAtwONtc0aayOWb%2FBZUOZgF1jJzmuxU4%2FCudRk1EDzjFlKNg6l135Ux13sIIhvvpwPoeLcpJPR76Q2tlvLNLaQ8tVoSkB8YN0lPfRlrKTF4cCeAVJZmh8XW6Uvi3kqB4A%2BdFfpR%2BA8rDyhFM40a4yJzyrc2CSfdoWS8nnAAbDKwrco%2B8UmZCBYjdIvMXCT9RYh9lj8QOtdDduCLQUKlPF34qOHuC1knk2aZ4%2FApamiSHSLeFVEh0xuHjQ%2FXYQZ%2FjeUU6EP3Gd%2F4luwz4oD%2BrwgWmHlwj6Ow1xQ18JBKRmkUUNc3C6bQ2mb3%2BQkENWzse2Me%2BHmQkp5aNBoztYROFQABPXBfzprf9cmhpW8urYkNKU3mJbQ8UEUkUSSbrK66AhrXOvByN8hBLZpGi8Ve9zGpjH7xqSbUsyK8YhbfFP%2FSuk6ojbNQ0YJkwHXwCo3kvzr0oluRK2b0s0IH71JQ2E7PAjBkRYyaKx3PIfqpLxaDkoRaByMMyW%2FNK0vD%2F1IiiR9Z3j0MMG1gr0GOqUBUv1WaaZ1SGJ2FUoYvbkp6eFTD8NcUVK2%2BHuZODdFU7JRhdKamH26DcfcXUIs%2Fz1Ikp%2BYBEuNkwR2Jy%2FmlgFQ9FWZBiFoCNoVhyF4vXFNje3rsAxTuD9ylX7MSLVt1dSxDg4yfP3jPXqKu9HlX9MTRxYE38jOzzyAhVjLOmCVB5kyxfgdSfywLx%2BvMLJtU5idNoJTVZBIR%2BZNRPahl25nwDqplBC8&X-Amz-Signature=76d9494af58c8a744fa6d8ce9c1d4eee2f14fb7f314adfa98c5c2381bac1fcc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BBNYYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA2MLUBDexFvf2T0ei3NaL6t7iyztPV8EHpD4LKyLxHGAiAY0Csr2%2BiMcNNxWjdANpCnzZkE98QKa%2FsU6TM9ltlLayr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMCkYRrBSIbWI9royKKtwDxJhNhQnYCN%2BXQmstduMX27UCaGQACnWirRB8rWMvchKu1Z19FnBnh%2Fl2sCetT1L%2FP92uucPUb%2FrNQErBxVYTDDlw23uB7ZMZVV0DGil8HaL5v3gmfYi9tbUjWt8F6uw6DA7wxF4hXllGcfmXHNTUfwsZxDOehLTzrivkVG4ylq2WxQCP9C29pWPXD098SXfbSaEL%2BgsYcoayNaUsbuFVuWuUy08PIpTQc0CkWICmgXNvh9bHiq90GllUSSynOvyZu0IIyeMErWsqA%2FyrCwfz%2Fjp2GR66YA4K2IwSeuw8tq3nlCvFRqKhx8ia%2BIi3pJQWZXlGtUgEFmmkM62MpR%2BMeH1hPWCTHVkbqUsf1jMZtcGkVCPt4uUQ%2BPCW5ACcL0mj30DfDRx7M4eBB6PMjPXq%2FIvqJLZiKN3mBeRamkpBQn%2B%2Fze%2B53wyK6pKHQmPBfEXaFvJK7489jjvpEJoTir%2BC8vF6X%2FPJPBnVFBk5wHb9pOI2d5mS54F5Tm0G9HTMQVrppFvisvMb6Y%2BAKAw1O%2FZ5j4n3hEBOm2CA8Wt2hdk45WZ2uPxq08bOXBTOTSDXJ4adswTaAcl%2FFn6tUG9oqt48RH0YlLl6KqSRUR8%2Bds86fpiOxn1XgIPFEURdeKgwp7WCvQY6pgHPQJE7kvH2PmBYYwsA7CPCethrFNp4DYNCtjfNLXgHALi4jI%2BJekBAPQOwvQAZ5uR7wQ7acpFtugSRNcZWNIiYh6YMZ%2F4jZNFPS4kpy0RfAoFA1XTSTwBoS%2FbEANA9wgQjeDWg9kzYGXES9Z6ISDFl5YdATp8AXW2FrDVxiu9BHMv%2FM6OsFi8h8ZP9c%2FTdcIKVtrcMyQNx9uzT6U29c7ramo1HvvPo&X-Amz-Signature=640ade45d7735dad3777bd3e7c2ac82c2a4a71b7d9d6a4befc0e7a0c8087f920&X-Amz-SignedHeaders=host&x-id=GetObject)
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