

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=328aa7e6c6dda854a87e9aed0809c80f25938c83e5daab5a2047a27949d8fbb5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=baf8e49dd69bbc852485b38dca8adea3c4e0b8d8e5c31f4d9ef1a91a45aba1fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=5dbb0a6d25b94df641c714b9710ce257d57d665507c24b2245c6f47f72ab10d4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=f59bede8befaab4b2d34290b49b10a88611e01b5801c62183c0428e2af678129&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=3618645cd614f63e71170726133930422e06ca4ace48e70098a8401e9701268c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=dbbb92a3bd1f37159bebd300c73c46ade00dbde2fa209f9410dbda821e522877&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=39ee0a60c85c0e645b60a1f7434fd0dedf1ca315a136cd2afc405fa78a940f51&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=c7f876cf031e5bfb2f67c7ee3aec702d1ac104a822607a5352886f8751c8de62&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=b96f07cd68895160a5f781540ddec7106af5a4d47a031369b761c4d1cdc12f3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XD4TY4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKXgBwvybnXLbydmdwFTNJhW9SkAjK2%2B%2FLBb09OXhVKAIgE%2BTHzkJ%2FijaZrc4o6t9g55r6X5pG9TeXKQGTccclEecqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5Kpqt8bgBRY5XHvCrcA93WwSLP7WzUCJkoJRYVyONNJBqHPbYKuSFnm7PfRllbImaY9g6QreH4oM8j%2BW8gXoyDIc83daLV3XKvxZhTvcLsowXtr8KcE9vIVEQEpXblwQYQJI%2FrS%2BihASV0V%2Bc07%2FSBlj7qtnYSsDi2JJaoHhswmQnlca2gcpSQ8aCBWt8T5sVKbPVheqOLC3YynekQj9IhOy4Vfhvg0nEUKmgqIqCjM9D7ZPOMVfOD6JlQRMHIZxV4x0ijUSRkwu8AgoLR2PNs8cYl80oZon2DZKeWPYPUV4KrZYBGg9gVqOqlp2ndTGPrq%2Baagy7s2y2q4tLDYLBHMEthNfnKS5sGwkSYgO1NgB88sOJiqG9pXSFUACm7nYivNDFUUXY1Ov4cy%2FVcSAjQxnv4tyGEBa0DmJADqKNYMYupXiwypJq53Etru3XCbxpoVs%2FvS59rCmDZ5LyFZnGa7XmqfMOqkeu1osOEw7D%2FweD2qv5ynVACPqxugibWrxO56daXXA6J6BcMReDXFb1vkSgL0aThR%2B7F9Hgusi6CuNy6TbAaHfPMy963JX3BcNseQ0UIiU9Z29zSPpBW99raC4G%2FdQ0jOJTL6V%2FquDke40yvHY4r2QHRC1NatZ0D5%2FI%2Bc4yUCxMTUIIkMO%2BT%2FrwGOqUBrs5iogpwhC%2FBE%2BadQ19TVqYTX%2BkUd60fi%2F46solrPweki7HHlnp1y4w2B2MkAaN7Wmq8M%2Bc%2BozE%2FUq%2BpPFzfBLUtagON6RaDBWjW1KJzOTVu6fED94TZoYK9aJRzLM4AY5%2FWv9Gp3ELqItJXJP9thGHqyqkL1RDDH8C7fz%2FPiv04NHgqYP31qaFw%2Fyjyr6tdbuTvULRQOdy1shzkhQT2Rzbj4Tl8&X-Amz-Signature=9e987b77e963901bee6820420368a45bab03759cc4fe1210607d2357e80cadb4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XD4TY4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKXgBwvybnXLbydmdwFTNJhW9SkAjK2%2B%2FLBb09OXhVKAIgE%2BTHzkJ%2FijaZrc4o6t9g55r6X5pG9TeXKQGTccclEecqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5Kpqt8bgBRY5XHvCrcA93WwSLP7WzUCJkoJRYVyONNJBqHPbYKuSFnm7PfRllbImaY9g6QreH4oM8j%2BW8gXoyDIc83daLV3XKvxZhTvcLsowXtr8KcE9vIVEQEpXblwQYQJI%2FrS%2BihASV0V%2Bc07%2FSBlj7qtnYSsDi2JJaoHhswmQnlca2gcpSQ8aCBWt8T5sVKbPVheqOLC3YynekQj9IhOy4Vfhvg0nEUKmgqIqCjM9D7ZPOMVfOD6JlQRMHIZxV4x0ijUSRkwu8AgoLR2PNs8cYl80oZon2DZKeWPYPUV4KrZYBGg9gVqOqlp2ndTGPrq%2Baagy7s2y2q4tLDYLBHMEthNfnKS5sGwkSYgO1NgB88sOJiqG9pXSFUACm7nYivNDFUUXY1Ov4cy%2FVcSAjQxnv4tyGEBa0DmJADqKNYMYupXiwypJq53Etru3XCbxpoVs%2FvS59rCmDZ5LyFZnGa7XmqfMOqkeu1osOEw7D%2FweD2qv5ynVACPqxugibWrxO56daXXA6J6BcMReDXFb1vkSgL0aThR%2B7F9Hgusi6CuNy6TbAaHfPMy963JX3BcNseQ0UIiU9Z29zSPpBW99raC4G%2FdQ0jOJTL6V%2FquDke40yvHY4r2QHRC1NatZ0D5%2FI%2Bc4yUCxMTUIIkMO%2BT%2FrwGOqUBrs5iogpwhC%2FBE%2BadQ19TVqYTX%2BkUd60fi%2F46solrPweki7HHlnp1y4w2B2MkAaN7Wmq8M%2Bc%2BozE%2FUq%2BpPFzfBLUtagON6RaDBWjW1KJzOTVu6fED94TZoYK9aJRzLM4AY5%2FWv9Gp3ELqItJXJP9thGHqyqkL1RDDH8C7fz%2FPiv04NHgqYP31qaFw%2Fyjyr6tdbuTvULRQOdy1shzkhQT2Rzbj4Tl8&X-Amz-Signature=66214d6f56d1058280f8e8febd9dcde7dae4b35f504a94e0003832df71ded0b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XD4TY4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKXgBwvybnXLbydmdwFTNJhW9SkAjK2%2B%2FLBb09OXhVKAIgE%2BTHzkJ%2FijaZrc4o6t9g55r6X5pG9TeXKQGTccclEecqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5Kpqt8bgBRY5XHvCrcA93WwSLP7WzUCJkoJRYVyONNJBqHPbYKuSFnm7PfRllbImaY9g6QreH4oM8j%2BW8gXoyDIc83daLV3XKvxZhTvcLsowXtr8KcE9vIVEQEpXblwQYQJI%2FrS%2BihASV0V%2Bc07%2FSBlj7qtnYSsDi2JJaoHhswmQnlca2gcpSQ8aCBWt8T5sVKbPVheqOLC3YynekQj9IhOy4Vfhvg0nEUKmgqIqCjM9D7ZPOMVfOD6JlQRMHIZxV4x0ijUSRkwu8AgoLR2PNs8cYl80oZon2DZKeWPYPUV4KrZYBGg9gVqOqlp2ndTGPrq%2Baagy7s2y2q4tLDYLBHMEthNfnKS5sGwkSYgO1NgB88sOJiqG9pXSFUACm7nYivNDFUUXY1Ov4cy%2FVcSAjQxnv4tyGEBa0DmJADqKNYMYupXiwypJq53Etru3XCbxpoVs%2FvS59rCmDZ5LyFZnGa7XmqfMOqkeu1osOEw7D%2FweD2qv5ynVACPqxugibWrxO56daXXA6J6BcMReDXFb1vkSgL0aThR%2B7F9Hgusi6CuNy6TbAaHfPMy963JX3BcNseQ0UIiU9Z29zSPpBW99raC4G%2FdQ0jOJTL6V%2FquDke40yvHY4r2QHRC1NatZ0D5%2FI%2Bc4yUCxMTUIIkMO%2BT%2FrwGOqUBrs5iogpwhC%2FBE%2BadQ19TVqYTX%2BkUd60fi%2F46solrPweki7HHlnp1y4w2B2MkAaN7Wmq8M%2Bc%2BozE%2FUq%2BpPFzfBLUtagON6RaDBWjW1KJzOTVu6fED94TZoYK9aJRzLM4AY5%2FWv9Gp3ELqItJXJP9thGHqyqkL1RDDH8C7fz%2FPiv04NHgqYP31qaFw%2Fyjyr6tdbuTvULRQOdy1shzkhQT2Rzbj4Tl8&X-Amz-Signature=0e7aed8c676891c2639a8753b9a0c39c87d461fa9587682881ef32dcc7484251&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=54359dbcd27c3537c1a09140e09b6019e062739af169ee1cd63800d85207a7fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=913ed7f2f307b981c2174532f792c9606470bba31bf004dbe86fe07dc96d3fce&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=55881b110dafad948e6870e8fa23733f16b109cbd92c849183894a3251f8bed4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=172b7ad902aed730cf7b93f5516f1f94b427a9e4ca71af1f4ed68bd694b0a2ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=8a6a227bbd5c77748b2c36775def828fa9921a8e0724a068576bd8b677e80d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=4e03d67dc6db84230d8e3787d7cd377482c280d97c4a0cc23052f94e21c49396&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XD4TY4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKXgBwvybnXLbydmdwFTNJhW9SkAjK2%2B%2FLBb09OXhVKAIgE%2BTHzkJ%2FijaZrc4o6t9g55r6X5pG9TeXKQGTccclEecqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5Kpqt8bgBRY5XHvCrcA93WwSLP7WzUCJkoJRYVyONNJBqHPbYKuSFnm7PfRllbImaY9g6QreH4oM8j%2BW8gXoyDIc83daLV3XKvxZhTvcLsowXtr8KcE9vIVEQEpXblwQYQJI%2FrS%2BihASV0V%2Bc07%2FSBlj7qtnYSsDi2JJaoHhswmQnlca2gcpSQ8aCBWt8T5sVKbPVheqOLC3YynekQj9IhOy4Vfhvg0nEUKmgqIqCjM9D7ZPOMVfOD6JlQRMHIZxV4x0ijUSRkwu8AgoLR2PNs8cYl80oZon2DZKeWPYPUV4KrZYBGg9gVqOqlp2ndTGPrq%2Baagy7s2y2q4tLDYLBHMEthNfnKS5sGwkSYgO1NgB88sOJiqG9pXSFUACm7nYivNDFUUXY1Ov4cy%2FVcSAjQxnv4tyGEBa0DmJADqKNYMYupXiwypJq53Etru3XCbxpoVs%2FvS59rCmDZ5LyFZnGa7XmqfMOqkeu1osOEw7D%2FweD2qv5ynVACPqxugibWrxO56daXXA6J6BcMReDXFb1vkSgL0aThR%2B7F9Hgusi6CuNy6TbAaHfPMy963JX3BcNseQ0UIiU9Z29zSPpBW99raC4G%2FdQ0jOJTL6V%2FquDke40yvHY4r2QHRC1NatZ0D5%2FI%2Bc4yUCxMTUIIkMO%2BT%2FrwGOqUBrs5iogpwhC%2FBE%2BadQ19TVqYTX%2BkUd60fi%2F46solrPweki7HHlnp1y4w2B2MkAaN7Wmq8M%2Bc%2BozE%2FUq%2BpPFzfBLUtagON6RaDBWjW1KJzOTVu6fED94TZoYK9aJRzLM4AY5%2FWv9Gp3ELqItJXJP9thGHqyqkL1RDDH8C7fz%2FPiv04NHgqYP31qaFw%2Fyjyr6tdbuTvULRQOdy1shzkhQT2Rzbj4Tl8&X-Amz-Signature=7ab5746914a1f37bd294c7721b8d536944a3d963bc4df9f8944e0d81b427044f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XD4TY4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKXgBwvybnXLbydmdwFTNJhW9SkAjK2%2B%2FLBb09OXhVKAIgE%2BTHzkJ%2FijaZrc4o6t9g55r6X5pG9TeXKQGTccclEecqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5Kpqt8bgBRY5XHvCrcA93WwSLP7WzUCJkoJRYVyONNJBqHPbYKuSFnm7PfRllbImaY9g6QreH4oM8j%2BW8gXoyDIc83daLV3XKvxZhTvcLsowXtr8KcE9vIVEQEpXblwQYQJI%2FrS%2BihASV0V%2Bc07%2FSBlj7qtnYSsDi2JJaoHhswmQnlca2gcpSQ8aCBWt8T5sVKbPVheqOLC3YynekQj9IhOy4Vfhvg0nEUKmgqIqCjM9D7ZPOMVfOD6JlQRMHIZxV4x0ijUSRkwu8AgoLR2PNs8cYl80oZon2DZKeWPYPUV4KrZYBGg9gVqOqlp2ndTGPrq%2Baagy7s2y2q4tLDYLBHMEthNfnKS5sGwkSYgO1NgB88sOJiqG9pXSFUACm7nYivNDFUUXY1Ov4cy%2FVcSAjQxnv4tyGEBa0DmJADqKNYMYupXiwypJq53Etru3XCbxpoVs%2FvS59rCmDZ5LyFZnGa7XmqfMOqkeu1osOEw7D%2FweD2qv5ynVACPqxugibWrxO56daXXA6J6BcMReDXFb1vkSgL0aThR%2B7F9Hgusi6CuNy6TbAaHfPMy963JX3BcNseQ0UIiU9Z29zSPpBW99raC4G%2FdQ0jOJTL6V%2FquDke40yvHY4r2QHRC1NatZ0D5%2FI%2Bc4yUCxMTUIIkMO%2BT%2FrwGOqUBrs5iogpwhC%2FBE%2BadQ19TVqYTX%2BkUd60fi%2F46solrPweki7HHlnp1y4w2B2MkAaN7Wmq8M%2Bc%2BozE%2FUq%2BpPFzfBLUtagON6RaDBWjW1KJzOTVu6fED94TZoYK9aJRzLM4AY5%2FWv9Gp3ELqItJXJP9thGHqyqkL1RDDH8C7fz%2FPiv04NHgqYP31qaFw%2Fyjyr6tdbuTvULRQOdy1shzkhQT2Rzbj4Tl8&X-Amz-Signature=6553299d78a1013c97bf79b574542ac0e3006f0c93bb0760a60a11d57361b1f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PR7FRUW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDF8BN%2BMEPUUP0hWrTvFbhRvuqpNtpBfFi%2FN2QzJAqLtAiBemwZ34JMYXrwQWHLkLNSC6oKbILvvmKGEu5p5XZdHzyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKFQoUMQSLu%2B6HbiXKtwDutsoCU6AwToUPwsgMGBDEQg0vnVMrxTESiBOz01sVXwIoU4jJ54%2F3PskAR1vvbVW1r75YsObtlOTBmuTk5C2nrlO%2BN3HsgR9fRxz9BcMGpM89IYOkBJL13F5IOekqZKb4knx5wMp2%2FDEc51tc9GyPo%2Fu8Pem9eWBx4WC1hsry4Kt4GDOpgw97KbC7ijWEh5B%2BuT7x06o0%2FR8gua%2Fg4oJDfwZ%2Fy%2B%2FXLjfqC4RW5ZJyYqZJPmlvKQqRkVsWfk%2FuvdohqRVQG39i0vYfEjUPOqGd7gM147s2DCAnX3F1ztHWErcsZfVLXUCqI3BRFOVKQvig%2BA8PphDHzbPSgQlSRAet%2BiIM9aRkj2WY8qalDcj1RtF4vzEcxr%2BzXw0bxPycok9A5L1SSTRrE%2FhxCPlfSxZ5%2BBrSVrl4eqwMkKnpuE6FXVcv8mb8tYhN8Syv%2BDr8OeZDvCz%2BqrE88KwhL47d4CnbGLVnEmhza5YRDXo9Yxf0x0yQr54gA1NfZ7zhRu12Ek9RDYlC9UtIVQbdO69JtOdZGOSiI7ZRfKfslFnbqPedTWCbBC8VHG2jjaoiKuyknOcz%2FuiZOmQrmJSav7KJwWgMVJJglMq9o6uO%2B%2FtvzXLBLZO9423tfYyMiWpEosw37T9vAY6pgFL2wMfQM2vP93wNQptQIPw4PpAyPNnnGdRAZ8JHpSUswr%2FN5UcHtqbbiu9Se0%2BpqjPq6%2FdCkyFJTa%2FK5n%2B%2FKZznCoUF%2BuJNpG1UBEpf2pr2y0jnMHTYbRCktWkB9BY0K2UGwT2jb9%2FXeKUIOqk7syhYrEA6NiWkTFWYI1jencMbZ9zLrKWZmBvJVfezm1OT%2FN8i1tbH4aNsUslvYxfxBLYrN72pAty&X-Amz-Signature=51ea5d4b6de375fd9402e862ffaff4193b17eea11e5498fd043e7978d044459b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773ZCROS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtX2qDq0AyE3cu6lwcRXHEra%2Flz5D84eM39Gsc7KuybQIgB5fFIJt9PiA1FEsW%2BKHhG0b6Q9tA9rJ0DndRhJp%2BESQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHh4YgSgffqYqRSgmSrcAyD749G4rWio5Fdv%2FB%2B%2F5KHulcCD87svSV6%2FV65fVBuwaWiLyvrwDKkwtzxWka9xQ14mJhPKIozdmbVgxFi78dI3UHLC0r63A0gC%2BNpbLpmmiEjsMKpfw3ihE5aLmyHxxqn%2B0I3aiL%2FNNbhynQ6dhprC00Hh9d0IxPRsnHgMe1WfPL1pJYzUWmkHJI6tt%2B2e%2BLRnlDhaj3%2F7CZBgxoFIEMV7PnJiMdTcdz%2BLvDtaTVhp8g8pUXTozXD8WqUdjwTHV865CT46yHyUHdOmLr0qe%2F2qZ1UM31q7z5l4EwKtVlLv%2BI1TSvomHnat2kZZmPgkYG%2F6QAKGZt9tDiPHbB1utCbFS7mhfKEIQwChL0pNsuR6VEWok06v5P6xJtIaeEutOp0QAYZ%2FDucfO4Pqpkj9P79ezf2xv83ahW0bRJWrbc9bq23D4x4xaApjRVNlkOCYdN1ozpQ4oUii67NF9%2Fh09P78yErL%2Fu6XESG%2FSYaQnjcPqnsuyzm75iHA5DCkxc9jeAkkXLsrrgaCbJNdLMh24ToMNYceL8dmF%2B8tc0K%2BBxf36Kc7k9X%2BdA%2Fh1kzvZo%2BPU7UWJEaHlPILNwAKbv6jIc2zDPyvo6mDNJvBA6N94yIGjBSmC5yZwDeZiJfoMOTB%2FbwGOqUBSSay4pK6qySbsysGXVkDE8HZRSqiNHeuAywh4L%2FBeJONeul1qqRegfrXBdisgiD25mjq%2FBAI5s0%2FlkU5VHBKHm5UGYKL4hcytjUwG3JXwq04Cn1hBeaAUStmhHOlF8u89ellFTGdD4VeCBvIEBfDiGG6xqDW%2BCOMILVWf%2Fa6eKbuMZBfOvGW%2BgI7vd8gTzBDB4RpRG3WUmePb2Y1XsnicAOseRuC&X-Amz-Signature=0e8760394e6b5798225cac961f8717fe3250fc90511da397da876df6230212f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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