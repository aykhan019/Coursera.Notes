

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=827d07c141cd5c6fe1810f93648d1a7c13ea6e8e295f766560a5b539acdd44e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=71efa01bd1f25b4c287ec88ecd0af9de8170b1ab9676162ca2ef58b075bf152e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=e7dfacb0caec5d5aaddb1985e87a526d237b6aeeed252807afd5b2cdd0689ed0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=c906a580eb72e3210726e0893ba938c7172ebfd97eba8324554d7f97f7f59404&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=5c0a8082076466a693611abc32297ea425c0ee4dd9cf6cbd8832f741407794a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=a954e9ca7748baebc68479c33953b57aa820716a2e66df8db40673e783fad832&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=6b337623091fb86d8f13bc16abb671b212a53130080550a48cfa189bc2a6121b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=a4bda982c5053dd875b22819b9f7042213b45f452af01ad3933147487ec9664c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=06f4a007938406b250f63eaa5e3c83542a0a92abf8e5d7b914df60e146afa629&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTZ23I2M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAbiqVdkPQmIHKMYTaSGz41DlaYXpgssR9T2d7KqhjDwIhAO8JqsM2kfipZsHnDyXxaeE6CgqNH%2BtJLmf8JgF9fSx%2BKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIBSPGy3clBcT2qC8q3ANJTcXvVsqdx3wCt2uf72FAoGp3HT8GIxu7SG%2FWac9n5GF9A5dhMOjkqQEAmcmeJgfoRGiqRPp%2FxwF%2FnITV9FrN7vLnEz6Pwk%2FAAnCGa8PQv1tepdvlaXpE9grKkmdURxatQD4YJ5kB7C8ganIfWSiIvhMdGHUf3CsFQEb1SaSPsh2jKJflf%2FQ6RcDtfLXEWOi5eCr2Ni05KqPonWPJvXivvKoXv5ID6Cbl7q2kJdtvxFoYH8MOe0u5hYKDwNpkuVZJcFkFwflc6MTPc1nIKGt9C4Dl5lddX3Ueq5I87SmC%2FOFL8uAwGUOCyraNvbzUBXPtMKhRhqSFoaOmaHfl3mURYPYenzA0LGLX%2BXKRjafJNdDD1NFZ05FHXKwJzmmG5t%2FF6iSKI39wVKAoWc2ezLyyRuJKesipGtC1zLMQZkN4EXDUXuQe5Cx3uwmi3snc3B3GIwN%2FQVbSrNtoc8g0NnSl%2FhbQb7FnGP7hw30SsF34D1%2FacP%2FMdPCv0jqPccVP9brYW%2BleS7ZNAkidcWYwgwHG%2B4Z996S9vXOAS9eVFcsr8KL%2FAKs%2FzpqPFYE26Av1qMt1TQHnuwDRGiMP%2FS1mcGZeq23eiUNk5oV3RqpgNB%2BBO%2BjEym1BV%2F5mHZaUXjDt%2Bfa8BjqkARGvsmvJWqgrRgcQonIuYm9DFvQm%2Byn9SnIEyx7SZXuJrdCqnzxNafpvE8KpMCZwsLxoNs3XMVkzUeckXBuxiG5LxF%2Bi8LXXwDgU4oGbaMDYIHQzRhqLlp7T4hhUaF%2Fsm75GA0JCbSxRwtH%2FCP7L8RWgddjQYVEIipYjmnD9vTiPOTesC74xUqN7gsidv%2FLwLRsD8m5CILBamNRiSO6GLuT%2Fl3OJ&X-Amz-Signature=4caa1ed6ac2a567f822df963d0ca32ffc23da583966fc6907275c05f48df22c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTZ23I2M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAbiqVdkPQmIHKMYTaSGz41DlaYXpgssR9T2d7KqhjDwIhAO8JqsM2kfipZsHnDyXxaeE6CgqNH%2BtJLmf8JgF9fSx%2BKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIBSPGy3clBcT2qC8q3ANJTcXvVsqdx3wCt2uf72FAoGp3HT8GIxu7SG%2FWac9n5GF9A5dhMOjkqQEAmcmeJgfoRGiqRPp%2FxwF%2FnITV9FrN7vLnEz6Pwk%2FAAnCGa8PQv1tepdvlaXpE9grKkmdURxatQD4YJ5kB7C8ganIfWSiIvhMdGHUf3CsFQEb1SaSPsh2jKJflf%2FQ6RcDtfLXEWOi5eCr2Ni05KqPonWPJvXivvKoXv5ID6Cbl7q2kJdtvxFoYH8MOe0u5hYKDwNpkuVZJcFkFwflc6MTPc1nIKGt9C4Dl5lddX3Ueq5I87SmC%2FOFL8uAwGUOCyraNvbzUBXPtMKhRhqSFoaOmaHfl3mURYPYenzA0LGLX%2BXKRjafJNdDD1NFZ05FHXKwJzmmG5t%2FF6iSKI39wVKAoWc2ezLyyRuJKesipGtC1zLMQZkN4EXDUXuQe5Cx3uwmi3snc3B3GIwN%2FQVbSrNtoc8g0NnSl%2FhbQb7FnGP7hw30SsF34D1%2FacP%2FMdPCv0jqPccVP9brYW%2BleS7ZNAkidcWYwgwHG%2B4Z996S9vXOAS9eVFcsr8KL%2FAKs%2FzpqPFYE26Av1qMt1TQHnuwDRGiMP%2FS1mcGZeq23eiUNk5oV3RqpgNB%2BBO%2BjEym1BV%2F5mHZaUXjDt%2Bfa8BjqkARGvsmvJWqgrRgcQonIuYm9DFvQm%2Byn9SnIEyx7SZXuJrdCqnzxNafpvE8KpMCZwsLxoNs3XMVkzUeckXBuxiG5LxF%2Bi8LXXwDgU4oGbaMDYIHQzRhqLlp7T4hhUaF%2Fsm75GA0JCbSxRwtH%2FCP7L8RWgddjQYVEIipYjmnD9vTiPOTesC74xUqN7gsidv%2FLwLRsD8m5CILBamNRiSO6GLuT%2Fl3OJ&X-Amz-Signature=8ebfcf0627aaebe7b1c84b8b1209c6a6a6becf496a43f4e6963502148d16ae63&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTZ23I2M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAbiqVdkPQmIHKMYTaSGz41DlaYXpgssR9T2d7KqhjDwIhAO8JqsM2kfipZsHnDyXxaeE6CgqNH%2BtJLmf8JgF9fSx%2BKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIBSPGy3clBcT2qC8q3ANJTcXvVsqdx3wCt2uf72FAoGp3HT8GIxu7SG%2FWac9n5GF9A5dhMOjkqQEAmcmeJgfoRGiqRPp%2FxwF%2FnITV9FrN7vLnEz6Pwk%2FAAnCGa8PQv1tepdvlaXpE9grKkmdURxatQD4YJ5kB7C8ganIfWSiIvhMdGHUf3CsFQEb1SaSPsh2jKJflf%2FQ6RcDtfLXEWOi5eCr2Ni05KqPonWPJvXivvKoXv5ID6Cbl7q2kJdtvxFoYH8MOe0u5hYKDwNpkuVZJcFkFwflc6MTPc1nIKGt9C4Dl5lddX3Ueq5I87SmC%2FOFL8uAwGUOCyraNvbzUBXPtMKhRhqSFoaOmaHfl3mURYPYenzA0LGLX%2BXKRjafJNdDD1NFZ05FHXKwJzmmG5t%2FF6iSKI39wVKAoWc2ezLyyRuJKesipGtC1zLMQZkN4EXDUXuQe5Cx3uwmi3snc3B3GIwN%2FQVbSrNtoc8g0NnSl%2FhbQb7FnGP7hw30SsF34D1%2FacP%2FMdPCv0jqPccVP9brYW%2BleS7ZNAkidcWYwgwHG%2B4Z996S9vXOAS9eVFcsr8KL%2FAKs%2FzpqPFYE26Av1qMt1TQHnuwDRGiMP%2FS1mcGZeq23eiUNk5oV3RqpgNB%2BBO%2BjEym1BV%2F5mHZaUXjDt%2Bfa8BjqkARGvsmvJWqgrRgcQonIuYm9DFvQm%2Byn9SnIEyx7SZXuJrdCqnzxNafpvE8KpMCZwsLxoNs3XMVkzUeckXBuxiG5LxF%2Bi8LXXwDgU4oGbaMDYIHQzRhqLlp7T4hhUaF%2Fsm75GA0JCbSxRwtH%2FCP7L8RWgddjQYVEIipYjmnD9vTiPOTesC74xUqN7gsidv%2FLwLRsD8m5CILBamNRiSO6GLuT%2Fl3OJ&X-Amz-Signature=29ca2b9c2ad8014befbae274324a4435b5a00c260d5cf91b186284c2ff6d414f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=ac170451513ba1d15fd8ffb9bba5104f62bb4bf6e4bf2ea5ec2983cfcd5a5344&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=0b42fe9e417fcd2ac967f76d90df486ef8b1b52007915a17e581678f91d2e69c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=dcc56937d7332555b3fb9dd60b4e38c23ebb1f11238a2d63bb56342b89afa1da&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=6c6e85cdf5e9f1ef64e771f5138ce9849cfb2d8cc4ad8971c0884c466e41dc7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=2baa4642228c4bbcfa021c91d280fe3fa1d81f8e2ca53ee4e528af92519e5932&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT65YZ7K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCp7JvWkwkPDaMhNOOsPyRbgJ%2FPPsm%2FIoJaFPjr5HHjnwIhAJA9cpjlZge0dHrd9hlJ%2Bbjrx%2Fzxo4aoWUwNTcAzCo7qKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSEj6DWuuUA93FxfUq3AO6h3z16xhfdQOFgSvud7w4izx7CW17Gb7kgs%2FFHlIyOseMBBtuJOjvbu%2FYKFgUxz7GKBuZDceUddg6QLXDZiBM8JKuKJMbFgyCUQWc6%2BrjGNtU89n3y%2BLVWhtVmcj6%2B6hsDK3ihW2%2FhiDB89bsMUi9M3xUcuxvXZP05iXF%2FG2%2FRR3viVMbH8n0cnJpx9M6xK%2FNyM5jd4Yz%2Fv33wDC2kYB3%2BJf3XkvPHKF8gEwUh%2BYPHKtuC6KYiMMecXc%2BZwbybEEQdQLxhYY4ARY3yZuhfazmLYbdplsOAmF6NWqggppRMN60KTz5ePlYjjz5NMsoUgc01rMjbbPoqCBhQjJtfMmm1qZDU5nmw1gCeuWLgBGuARSuNEQXlMss%2BLHb%2BmAnusKQsj0NrnsCZZEt15sOFlGExUfXo6f2TI%2BzK8K8MHfwN9Y0gg%2FhD1ZsNyG8RFMsADIMN9qHp9Ycxgog2nNZ6Mc%2BG2KTHP1M%2FhbGmb8Qq4wntDvrEx0yEmM6zcq2drkuLyOVZpNu0%2F7YdzoYfQ%2BPerM7dhKNZuE2AVTrt3pD7oci9YrWgCn2LXrpUahVxiRH0wp7ASeNZkoL5gYxsNuttDjCZIx%2FzwnjZSwxZ5pP%2BW7q37511c62i4GyevgOyDDg%2Bfa8BjqkAZleQ4j2rcGGcqYcxa5UQEegEKtEgzsCBWm2z4GPVDHitT%2FQhaBwFAummLESjJxAAv6TLLU8h1udyTDBMLyvvNHmnUYvBuENt1qoG2zCsodA876K3JIFVmy%2Fkxo68Lr%2BiK1oIdxpYJ0HagumGkEzBt9ReIHEKasY1AV7K3PXlqQNIy5NZx%2Bl4hxzYuOQNp%2B%2Fph3%2FICtBILQmzIqTa0b9o0y4Hb5k&X-Amz-Signature=8a68d1ab64515c476e01d64d827ba0546f972af126f2114cba6ad4d2e43df2bb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST7RKG7Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFps7fU6Pcw9xnUT%2BAm0KL9ogiXsv1rylWtOnwU8TnJNAiAccbg7wWr8L4O4Wsupv3zzAHdhX57APbt9AfEZEET7QSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLG9LLvol7EBtgXxOKtwDBzkXYG6q4%2B8PoYpYaA6ikTzfEhQNOZ%2B9uZo3Jn%2BIYeEko1lJNQ07BgaojaTGLWCZC65dDqaB9JBA9deJDd5SaBOUC%2F5zgL1QWnz%2Bjzf3aOWw7SbalZG0%2BJViBA0sB8S0c74DDYPBlNa%2BScplVrz%2BhfwncxxC%2FkCn%2BV1GSZJZokVCaHymVMYgU1agw74bBPdaOpeNd38yu5JtMoqmXijohRf43xs7cBbezPCdNouBqaM4StNNfQzQpz0Yq3%2FjWCWne42NiEDqoIgIQXLNAIPWV0hyB9kx09ouH8kN5qrBSyA711NhJR87OraEh7BH9zCqMhhTUaTJwGdaGg1HlfwkE52qiWLzPaRneNNQ8oOZa3cSqHn0zk91oT8zHP%2F4ChHXUD67lo5zzGrwP%2Fhnw0tAHM24A3WJXW6gzL8R5BeMse3y04x3uQ2G8l3KKERlyOuG%2FHO63VzQ6FXFbPm3qDxadJuF77rlojPU0%2B2XtRwOG4wMTlsklAPX22Lf%2Fb%2BvPIikCJDsTQteu%2FbopLsOZZC4GytUh9xGw0Y3HKrlfDqHXnOmhSpb3q1yjXb2LVpgPlRd1zUYH7ke8BlcEVDl9jp%2FcQdKbreD%2B5ddN%2FK8HuYCVx1nyZf79a9N3VUonnwwn%2Fr2vAY6pgEFYjgWis3LiskypFj3dDrji1VG58b4%2B3JWN5kpyJC4uslHTnu%2BsE2%2FiMNrekComKk18ufDI6%2Fg2254u6J9jMFj4ECWv59oveYssiYut5C8XYV%2FKnS0sSYwAt%2BW%2Fq%2FvUn62BSoR0zrXt9Ho0WUbRLmVhfzy1gt58%2FXc8G%2FJnd82c%2FRYyF3X6mfUDnKKxSEo9GV29rwXar7CQsCtca7XZzv33n6JHXTm&X-Amz-Signature=c28ad19268c78c39b5490a9495e0c70f081b0694bebf90aa473b61f053137d56&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST7RKG7Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFps7fU6Pcw9xnUT%2BAm0KL9ogiXsv1rylWtOnwU8TnJNAiAccbg7wWr8L4O4Wsupv3zzAHdhX57APbt9AfEZEET7QSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLG9LLvol7EBtgXxOKtwDBzkXYG6q4%2B8PoYpYaA6ikTzfEhQNOZ%2B9uZo3Jn%2BIYeEko1lJNQ07BgaojaTGLWCZC65dDqaB9JBA9deJDd5SaBOUC%2F5zgL1QWnz%2Bjzf3aOWw7SbalZG0%2BJViBA0sB8S0c74DDYPBlNa%2BScplVrz%2BhfwncxxC%2FkCn%2BV1GSZJZokVCaHymVMYgU1agw74bBPdaOpeNd38yu5JtMoqmXijohRf43xs7cBbezPCdNouBqaM4StNNfQzQpz0Yq3%2FjWCWne42NiEDqoIgIQXLNAIPWV0hyB9kx09ouH8kN5qrBSyA711NhJR87OraEh7BH9zCqMhhTUaTJwGdaGg1HlfwkE52qiWLzPaRneNNQ8oOZa3cSqHn0zk91oT8zHP%2F4ChHXUD67lo5zzGrwP%2Fhnw0tAHM24A3WJXW6gzL8R5BeMse3y04x3uQ2G8l3KKERlyOuG%2FHO63VzQ6FXFbPm3qDxadJuF77rlojPU0%2B2XtRwOG4wMTlsklAPX22Lf%2Fb%2BvPIikCJDsTQteu%2FbopLsOZZC4GytUh9xGw0Y3HKrlfDqHXnOmhSpb3q1yjXb2LVpgPlRd1zUYH7ke8BlcEVDl9jp%2FcQdKbreD%2B5ddN%2FK8HuYCVx1nyZf79a9N3VUonnwwn%2Fr2vAY6pgEFYjgWis3LiskypFj3dDrji1VG58b4%2B3JWN5kpyJC4uslHTnu%2BsE2%2FiMNrekComKk18ufDI6%2Fg2254u6J9jMFj4ECWv59oveYssiYut5C8XYV%2FKnS0sSYwAt%2BW%2Fq%2FvUn62BSoR0zrXt9Ho0WUbRLmVhfzy1gt58%2FXc8G%2FJnd82c%2FRYyF3X6mfUDnKKxSEo9GV29rwXar7CQsCtca7XZzv33n6JHXTm&X-Amz-Signature=89fabf681b7b9d2bc1e4358a894c8768ae1bced522dcd27c3f571c31b3e293d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHNF3BNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC1M3VPReV8%2Bx8yNrhQism61dTBTpsgtcEfmhumo1UXgIhAPd1Pad%2B0G7cxYyh8X3CaxOMvATp8t4jPD7i%2BlqNqX5WKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEyDczKRXqCxmimx0q3APcL3NcKt%2FLgkk%2FHCfrXnzdVq%2B9WASGvkouc7j4lXRyEu4aE2tHcFwrewdIEmgWd0swddlaXhhiu69iNil4tbI3TgJOoB3bYF707LRISb3v92eWfDiL25C7%2FJChQaUvPfhqezZwxJz%2Fd0XVhgZDFyn%2By0iyGk7e9Aqto66XDq5b3rGGaK6bCx4m3YcvJs2Ix%2BPuGuzUNoJXbXEGvj1yrQv2ptJ00yLtsWjHGEPzYEnE7xi2h5VGF7MLf8am1KUQXezOssGsIIlsvKeGMFn2Ro%2BESigtWKcxIqAaIAYPIYvvL1pRfhxlwY3lkoKSFPTrE3NBiHX63wl35cFQ7QzvBWxCu9HaYmrROJP4v0%2FI%2B%2FYkt1ql6vehZ%2Fd7NNGYdHhNnp%2FIVr1IqLq%2FbciRmEO1uzkNIAHFawFvtgkk6lFvUwMm4eUdjoHEaTnYUw2AgBAvs5zhVLo%2BYwBvy6kvfM1pbrNyDqPMlptEt2%2Bzv4sxj6tNisRXs%2BOCCbNVHPSDlnk%2FX0FCRxUaRGZgRlIWqbwarE94StqIj0p1K8I7%2FWVGFLRb2c4pfySA%2FsVqsOdY7kulACN%2FJF4bONh%2FuAdoa8OsWc%2B35KSBqtkCd2iWMcD0g94fTDpJi2A97DxeY%2Fe6TzDV%2Bfa8BjqkAYpD8j05%2B%2BZgrHyev18WW1p4IMNsLzEbQYPN%2Fm%2F%2BsvzvPHQuJcZH00zGEGJgsCLsBiZlBgaMVFroKBhE1%2BAofKdV1EvVfVYkFDC6gOEgC3LDo%2Fm7b6jFVlCTc8hfHYRZRW1J1m7EjjDP3G%2B3Dl%2FzzufHHJHo66M6jlKk7kySAbtRB2BwXIODPLeTpInQbyWGUsqcv9DQgsjTAGKFDkRPdW%2BMj0Io&X-Amz-Signature=d4619728f3acefe8504e7073a15515d4d0fc6241210e6baeeb30cab7e036aa6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPJDAC3G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSif6OoblxIfofBlrOqNUSOdq0wHJqCSpGa8ttU9zmVQIhAI1LlSfZzRI5FpNFoNLYMGccaXbYeIy9De9IUNKAvsqoKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BiQsRBOv6ztvAuiEq3ANziHwmSCG2aqphK35Zji8iu59HSxMxqBxuZ%2BnrSx5udYrQ424UU8PlHPNc%2FzaYGJWCF6sZ6ZmsWIf4pBnLcJYtgVQ%2BaZSxJ9MN5nsN27Wri%2BURKI6uIRJSfA14eEKGGtyZWWh7VJDi6PiZqvhMOkqlo0DEYCysO1Hn3yCkjRRZMLrZFABT3VDZetWOmMbMmKGO9MP%2BJgkXraZrBzqtp%2FlnRxJ5uWQ5H3G%2BoSThYKE2ysnRRGR8ZoBqIWX9Yibw3pKwv3DN6VbPZSEzaAueB2DzYGh2tRaRdwKagIebMHuxea5u7hVQ0znfr%2BNSJ6jjw1BXygvtOkz9sa30BTMqeZy0MaI8kNGgHGrv083tNDVS2W%2BqChdmcv3XGVRk3anxJ0fnR9NuMmjUBQqbLDCX0Wm2Ckn9xGs2FopH1kpaFZryBCb3IW%2FmOgsk8ME8ESHdc0QjQWiyjVMk3EVhNoDNMo4cfk6u4E5757ONLf93Sz%2FWUrJZZJKEeFU27sy0vjrMqj%2BBZ19fKyLZyMAlT3oGl5GZgoylQgpICkZkSD%2FkLt1Ot32eOKW1BMARCfMp%2BerV6Nhh0mGCbEtf%2F7VX3Mm4h5VTGgHQjEl3tZuOWrnXxUUKz1tk43ywtZpUwpd3gzDHgPe8BjqkAU7vwD0BrV3tLvvDFwiOY8Cc0u%2BdLBf%2BQc6JO2z4KK0z7pXObPs7mwgdL4HnOb4Y%2B3f06QMNI4fB2Jivd5QHrJWFBnAXQnzy22UJhHr9Y4DZANdRPnY6Ecmy3VdBfgWwrEYHbCZ%2BEdjxoAwPb8ji%2FTdrQX8HADnf2PktoByEvfJzKiMn2zyPC70LMvQjy3gnvYCAzGo7VX9t4FTSln%2FO1tYL%2BfS7&X-Amz-Signature=4764da646def82e303e66860a44fb4984788b58ed69fbce64fcb698d1c864d17&X-Amz-SignedHeaders=host&x-id=GetObject)
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