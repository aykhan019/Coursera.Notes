

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=1ed6c8c441ee78a14da1588f3151021c3c386de70fbdbe465162aa46b2d9c282&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=24a1108fa2382892812f6c1fa523598387b0a5b11478d21fe8ac5194c473d4b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=a231c0c26635c08a5b40fa45168e78da1474889dcdb4d47bdbb7b429a90e375d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=4d5acb5c5dd981faa65e2df138cba22ac0efdbc5fb31979a9ecc5ea245454de1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=9f28d20589a933ddb1cfbfa2343b4933abba7c181a5f978b1411f87c5b15276f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=38f7bd46fe6133a9fea2b1b98ab405cdd2aabd65fa72dd1863aacbf9675f4af2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=6838c2d83b5d24a81d94e462eca80dbb2612ea1ec1d801a626c03091782bbfeb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=daf9bb06914a262c2528164a77b04d9f12b42a61387f65ad7c877a330de34fd7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=6ad6f2b40b016fec9b2952eff4a317c2d1dac6ba0f2ddb840110d9706756e0f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC54MLZV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIGJkLhd8adC4LecJEDc0x1laAS9u2Fy3oP3pGfTWNhCVAiAvmPbCMfL6893ExLIBDRv5Ja%2B%2BKv4fZ3nkSq0bQSmP3Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM7OkGtRRa28onVMRzKtwDt2Eickft5zuAS6JjA6JGKwESEv2rjY3NB%2Bu%2Fh%2BVZlgVC5YczaxoMcWeBkR2WFQylhNtmEy4z5idsHCYCy6EDofBkXRFYzfsggoa1l5vkm49MkhmHnr0lmn5CBvLA3LhfZl4ofUjHTRjw4u0zbq%2F5lFk2TvVpSEnXrq2nMVIaIoQk5PhhfYCY6KaN8ZkkWsVfQQbqe6IL%2B5G0LtuBcxi9Bi%2FQJtgRRygJ%2FjhJ%2FRp3bo8YYWLhMFsRWD9l5z1TNZ69w6%2FGNko%2FK6%2FzZUh%2BMM8Vnkg4LRqkGs1dibp9h3PH%2FWR7wlWX2bVvlcEm%2FqMeWDcumgSYWTgG%2FOqIMGMbjfyH9EZWlwxlUJsPkB%2BM3YvTjXmCSOP5oN0%2FObAttd9WIBqAHLJXnsij9G7lPOKK3ox%2BSdecO8QveRbezhi%2FJVG2sxsKPPfMz90H0chuunQNIv2L9qlt1%2BjbWHJxZB8CyS3%2FrQmpARH4r3yDkvL77Je7ek8eJdeE2Eoohlz37aVyEtswWu1xQaOBaTmJidJETxhtJ3pTEU%2BG8OXFWC%2Fq%2B7hTMjJK2KTIaC7rvjOaXWekSErGPlq0TBpO6J%2B%2BBfN%2BfI0dARMpzIEuOWzNl%2BY%2FMFBmzBSTA5go%2F3ibsZVi6Uow0%2FmLvQY6pgFfkz0VrJSvs5H91BFszIpNns26yG20zzFeiq4sxrX1s8ss4cuGk%2BrpJwnlAL%2BiTFx9hLFDUs9KYh8KrkoWPGkgrkkOQjel2oN4Dk6m6P75Nie1ISx79WcSRR1Qwajd%2FvlyHs%2B1xtHEBWh%2B%2FYNFactGLEZghov0kk0lMr3uWKTZKZXLerByIWzxc%2BDii4%2FQeFHAValzpl1edb%2B8IUfJAI53A05b2Qkx&X-Amz-Signature=9594e1c1396def879f31047af13c3f708702fd5534333ba55f4bb3a4224b5b7a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC54MLZV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIGJkLhd8adC4LecJEDc0x1laAS9u2Fy3oP3pGfTWNhCVAiAvmPbCMfL6893ExLIBDRv5Ja%2B%2BKv4fZ3nkSq0bQSmP3Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM7OkGtRRa28onVMRzKtwDt2Eickft5zuAS6JjA6JGKwESEv2rjY3NB%2Bu%2Fh%2BVZlgVC5YczaxoMcWeBkR2WFQylhNtmEy4z5idsHCYCy6EDofBkXRFYzfsggoa1l5vkm49MkhmHnr0lmn5CBvLA3LhfZl4ofUjHTRjw4u0zbq%2F5lFk2TvVpSEnXrq2nMVIaIoQk5PhhfYCY6KaN8ZkkWsVfQQbqe6IL%2B5G0LtuBcxi9Bi%2FQJtgRRygJ%2FjhJ%2FRp3bo8YYWLhMFsRWD9l5z1TNZ69w6%2FGNko%2FK6%2FzZUh%2BMM8Vnkg4LRqkGs1dibp9h3PH%2FWR7wlWX2bVvlcEm%2FqMeWDcumgSYWTgG%2FOqIMGMbjfyH9EZWlwxlUJsPkB%2BM3YvTjXmCSOP5oN0%2FObAttd9WIBqAHLJXnsij9G7lPOKK3ox%2BSdecO8QveRbezhi%2FJVG2sxsKPPfMz90H0chuunQNIv2L9qlt1%2BjbWHJxZB8CyS3%2FrQmpARH4r3yDkvL77Je7ek8eJdeE2Eoohlz37aVyEtswWu1xQaOBaTmJidJETxhtJ3pTEU%2BG8OXFWC%2Fq%2B7hTMjJK2KTIaC7rvjOaXWekSErGPlq0TBpO6J%2B%2BBfN%2BfI0dARMpzIEuOWzNl%2BY%2FMFBmzBSTA5go%2F3ibsZVi6Uow0%2FmLvQY6pgFfkz0VrJSvs5H91BFszIpNns26yG20zzFeiq4sxrX1s8ss4cuGk%2BrpJwnlAL%2BiTFx9hLFDUs9KYh8KrkoWPGkgrkkOQjel2oN4Dk6m6P75Nie1ISx79WcSRR1Qwajd%2FvlyHs%2B1xtHEBWh%2B%2FYNFactGLEZghov0kk0lMr3uWKTZKZXLerByIWzxc%2BDii4%2FQeFHAValzpl1edb%2B8IUfJAI53A05b2Qkx&X-Amz-Signature=f7e89a850c7fba0d16ae0cbad1c1b91ee6d3f65532194b08281e19d42de4d799&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC54MLZV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIGJkLhd8adC4LecJEDc0x1laAS9u2Fy3oP3pGfTWNhCVAiAvmPbCMfL6893ExLIBDRv5Ja%2B%2BKv4fZ3nkSq0bQSmP3Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIM7OkGtRRa28onVMRzKtwDt2Eickft5zuAS6JjA6JGKwESEv2rjY3NB%2Bu%2Fh%2BVZlgVC5YczaxoMcWeBkR2WFQylhNtmEy4z5idsHCYCy6EDofBkXRFYzfsggoa1l5vkm49MkhmHnr0lmn5CBvLA3LhfZl4ofUjHTRjw4u0zbq%2F5lFk2TvVpSEnXrq2nMVIaIoQk5PhhfYCY6KaN8ZkkWsVfQQbqe6IL%2B5G0LtuBcxi9Bi%2FQJtgRRygJ%2FjhJ%2FRp3bo8YYWLhMFsRWD9l5z1TNZ69w6%2FGNko%2FK6%2FzZUh%2BMM8Vnkg4LRqkGs1dibp9h3PH%2FWR7wlWX2bVvlcEm%2FqMeWDcumgSYWTgG%2FOqIMGMbjfyH9EZWlwxlUJsPkB%2BM3YvTjXmCSOP5oN0%2FObAttd9WIBqAHLJXnsij9G7lPOKK3ox%2BSdecO8QveRbezhi%2FJVG2sxsKPPfMz90H0chuunQNIv2L9qlt1%2BjbWHJxZB8CyS3%2FrQmpARH4r3yDkvL77Je7ek8eJdeE2Eoohlz37aVyEtswWu1xQaOBaTmJidJETxhtJ3pTEU%2BG8OXFWC%2Fq%2B7hTMjJK2KTIaC7rvjOaXWekSErGPlq0TBpO6J%2B%2BBfN%2BfI0dARMpzIEuOWzNl%2BY%2FMFBmzBSTA5go%2F3ibsZVi6Uow0%2FmLvQY6pgFfkz0VrJSvs5H91BFszIpNns26yG20zzFeiq4sxrX1s8ss4cuGk%2BrpJwnlAL%2BiTFx9hLFDUs9KYh8KrkoWPGkgrkkOQjel2oN4Dk6m6P75Nie1ISx79WcSRR1Qwajd%2FvlyHs%2B1xtHEBWh%2B%2FYNFactGLEZghov0kk0lMr3uWKTZKZXLerByIWzxc%2BDii4%2FQeFHAValzpl1edb%2B8IUfJAI53A05b2Qkx&X-Amz-Signature=b33a1c852ed01f09ec614604e2672f169b5c996d7611bc83ef3f3f0df0d04318&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=52a7a9a473699a354dc8dec880655f624648a625c46992b62c15191670e88950&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=a164315668379ab5c61c35eadf38e090e7d6a0c36a28cefafaa1c3891a619348&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=4fff964745c8c567bf930e40f76793d55a831f3f830abf381d59c5f8089ad616&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=092a5dd4f1936225a6ba47e561de9e50a36af4703dc7fcf7560ed02e08724f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=6212f72b775b78ce32a5cd7a818b4baeb4a7264a9b197ef4e3c0fa3e4edbd43c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5PC6YKU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDt%2Buy5KdX9L%2BFjXi6etKVePUWTL2YM%2Fbsxl3YXSiuzogIgNGJu%2BlWJpzz%2B1kEYIDU7iXnti3odCUXNp0ABB0dmbeAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDAZ8D9odIEVOrrQVYircA53hHukljN4cBHwUe2FijQd8%2F8%2B6WmiPy9vF38xzkTD6HzdXOJFQC9i6Z6DAXm%2BjMsrI9egEfNo2awCZDWCVc4yyP9%2FOU7uZXFI3B%2FlNGod9AiuO2LaJclEPz3JqZd9WoAKgovmQtkBqkgQSytBNLNcqsJKlDh2JRlxm5XZ6O%2FsZWkOH6Y7z3Sbgymd%2BUuA088fEsDA4AmxxNPXotgXMUrIJCpc06UMZsP6l6hDZT%2FPjn5ID31KlhF4CS9ZJVO9XrlMLY5yAJSmoKrCUOh%2BRUZJ%2BFFQswaxLTjGJamw8QkHOeykqNf0El3exSuc0XA1SGrnyS64x9UIK%2F%2FFnU%2BrU6XwY3LFpUsIVbItyFV4tZd%2F1twxXZOXV4hDHAeJRugXW2iAVvMjgDmqBHcUS4QZd8KL5HkBnctMKhFh67A70T4eg%2F%2FROYwI%2BQnT43ALpExroLvuRkz6%2B4UIPYMTcw00G%2Fu9PaS4zJGUxIzqyKSt%2BDFkgmGX%2BrAI%2F0qk9k4eFfFuasqRvR8fm0bDWdBrKEE2ADed1MDAj%2BaKww358fpM%2BqjSFDu6i3GvM0QtHYG9Tr%2FgM7wI%2FNccRgaF7u8dAZkve04lE5mUdGxnELRSUiewh7bEh%2B4FBEF8WufXtA7gzMLX5i70GOqUB7PRI7ZVtyE4q1jDXOKgSarZGyBl502iBw8%2BDe5kaHV0JscnMT8gkq2cmxTA2cQYf8PE4UvHE3%2Br%2FtufUep6fJbq0JwJ3XYa4044RcznyuhtLdsBsqk%2B%2FAOWzOtyJBqVu6gC1XlQDawyihj7VsitB8yAXO%2FDMUCtDH6a0XKBHAj4gXtQZvI9re6PekkkNilXUiFZi0lXX%2Ftj3uzEOKGM5JQOee9C%2F&X-Amz-Signature=79118b11daa454d8b2519e362cc9c8271fdc409e4a045cfc5dc56c4171bcd00e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UG2UJJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFAPpG6BduIKxKcdDQuGZGDS%2BXJtKO2mqgbEmrkGXRuFAiEAosPJ99Mnqr0g6m87JTdyacjKSNN4gD5kjmc7T%2BXTVNsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDM3Kac3eZ1NmzarpUSrcA7RaZ8N5qf64FZWTn8io7oY5PsFVYwUsazgv4%2BCMEKcnHltt%2FiG2q%2Fn0sSQRDKWY6hN1u96hUrPdlKOqXx6yXRcH9pV393rDTY3Hn%2F2pdSpFK8NuH6x%2B4OcIbx5ERtS3Kujy1NgaZufRn2x2Oz0nnUlyQmiODKG85kLEvAxq%2FrSxlAGOTrqOvNt5HBWq4wfA8rcUrNV2CYSXj3dkgK4R2y%2BapfPyHhHkO3ackKssgZg4so3ewouk8IohJBrvt1tL0SKDfcdoUT9x%2FUXciw1tQjuXmDMMAEE4txSSjefekTSV3R%2B1rOxhmM2gALR%2FXNSaLGf%2BU3LgF%2FaUkZQOmw8mYD9JMiOOht1y%2BE82flU%2FyAZzk%2Bnak84nCs5OOc29ONJ1UKx%2FAWWtoLR%2FoJuqX5wMIgKbAEOcymuq1qOYHzushpd8VxGF%2FHXam%2B9TdsKgVlVqP11N1D3fEXWKFIombZSz7hpeIO%2F9ar1uD8D8gRd4il7J%2FNaDJRZ7U4b6UATVE%2BR%2BjBI0RdzA6hgpCyiWDTJ9dCAIBhA4DUYd2kMgVMgaNVpMJtIFSgbe2qbKvJM3C%2Fp1nS3i4WCiEcxPWe1rIx5QdhrJ1pVCqWEcFSsdyw7NI3NMu1vbDcS%2BVsYAJjswMIb6i70GOqUBKUt39yr7p1prEWWV82bXUsfH6BvAhu1oost%2Fjhawjgt%2BvI%2BcWlTuvlNMbzfzQH43lqNDNJliWySrpKVKFVc8%2B7d665Ft5hNj2nX8jEPJssb2QhjEzoE9ak1OmnGiDs78VZQSXK%2FXookfeZqmgTQoMcrOKclNAo0ARCwJo%2F8gLMAAYsylR31Toz4uMmGciBQTvpMyVFhL9e1RLzuEUpr0wve4rp71&X-Amz-Signature=9f32fe03d59efd8e03e6630841866ea6e62f3453974f556eaeb5c391952f5a03&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UG2UJJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFAPpG6BduIKxKcdDQuGZGDS%2BXJtKO2mqgbEmrkGXRuFAiEAosPJ99Mnqr0g6m87JTdyacjKSNN4gD5kjmc7T%2BXTVNsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDM3Kac3eZ1NmzarpUSrcA7RaZ8N5qf64FZWTn8io7oY5PsFVYwUsazgv4%2BCMEKcnHltt%2FiG2q%2Fn0sSQRDKWY6hN1u96hUrPdlKOqXx6yXRcH9pV393rDTY3Hn%2F2pdSpFK8NuH6x%2B4OcIbx5ERtS3Kujy1NgaZufRn2x2Oz0nnUlyQmiODKG85kLEvAxq%2FrSxlAGOTrqOvNt5HBWq4wfA8rcUrNV2CYSXj3dkgK4R2y%2BapfPyHhHkO3ackKssgZg4so3ewouk8IohJBrvt1tL0SKDfcdoUT9x%2FUXciw1tQjuXmDMMAEE4txSSjefekTSV3R%2B1rOxhmM2gALR%2FXNSaLGf%2BU3LgF%2FaUkZQOmw8mYD9JMiOOht1y%2BE82flU%2FyAZzk%2Bnak84nCs5OOc29ONJ1UKx%2FAWWtoLR%2FoJuqX5wMIgKbAEOcymuq1qOYHzushpd8VxGF%2FHXam%2B9TdsKgVlVqP11N1D3fEXWKFIombZSz7hpeIO%2F9ar1uD8D8gRd4il7J%2FNaDJRZ7U4b6UATVE%2BR%2BjBI0RdzA6hgpCyiWDTJ9dCAIBhA4DUYd2kMgVMgaNVpMJtIFSgbe2qbKvJM3C%2Fp1nS3i4WCiEcxPWe1rIx5QdhrJ1pVCqWEcFSsdyw7NI3NMu1vbDcS%2BVsYAJjswMIb6i70GOqUBKUt39yr7p1prEWWV82bXUsfH6BvAhu1oost%2Fjhawjgt%2BvI%2BcWlTuvlNMbzfzQH43lqNDNJliWySrpKVKFVc8%2B7d665Ft5hNj2nX8jEPJssb2QhjEzoE9ak1OmnGiDs78VZQSXK%2FXookfeZqmgTQoMcrOKclNAo0ARCwJo%2F8gLMAAYsylR31Toz4uMmGciBQTvpMyVFhL9e1RLzuEUpr0wve4rp71&X-Amz-Signature=a592d1f8269f9d52cfb7b8ab5094dd45d67b3a10b2be266257eece18636cdff1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTTH5RSQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCbDlCDhnr6gbfLxHMz5RqPRqlgn8f8IF3hqNZrA60jPAIgLRgbCRNb7R5Z7o%2Ficf349%2Bn0lzk5tvNNqQb2i3NMbwMq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBTZyUj4dmV21LGPLyrcA%2Fj5BnXVgjG7NUyEi0vbddbd6WpwMqRZMsc4jv01AvSYfqk8txlFIBdJ%2BVFSTSh1jj4ILE8IRhqgpRLHUG%2FszvIaE5VFbeJdVVK9YJ9vkm1b5j0AO51gbQ08cy1cQEMxffWAz2fOv%2B5vga8UV%2BulSXQyGY8ydxElDCM8k9Gi24e07rgWgoejikaAJOT5NLmo4TSy0ta1QeW56h3YLn%2FWTlJHf3W5YXFM4%2FKoCzb1PkPRlLu%2BiwxZUpDvOTyohmB99j13xqXffzhZpsPwnQ2IuzmLQUSIvv0woocw2eu1pZOJILhhYDPqkYhfSOfA8g%2B1oDNudkmvzaxaw8%2BCcJh4xQ2DbNMbbNjcNUmsDcFyyWjhDSqQcbR9esrIM828X0Dnuc0S0AFKDiiywto350vdyW4aa0qf6vz8v6CdMeq4%2BEnNjN7sARptwpKJQVwU0V%2Fa9cVIz7XyyzZ6RKiy1ANdJ21GoDjzgNVEHU8yhfBwGFdvLjkLSM9ANQ9zdmR9etvd4mvCZo4dr8qM56%2BQXlZ3IuRdzCKPgbJHoayTA7L%2FYuwEQgwoUIq7rwaW1Bzudz53DceacIs%2Fd4UpFDc0qSwC807P%2B92hzkcqeblapxpv2n2f3z2N5Hq1zvUwbN6GMIb6i70GOqUBKbRLQ9o0zwPKdtMxFjDAvi9FywWfwfEQ8lCe0EdxdcQlVmwc8Wdvmm%2FvUVQYcfHjNbOi1JWYMVV68V9OXUwVs1IV9fjxFK0YQhplCJ9QggretZ2W7zcrDart5JCybuLSefroC4xifdsXNK8h8Sv5mRtkkkiqtyx%2FU4XOuUpvS2keXXzOb3fmy5D%2BCkDxu6LVh33j0V48odUefnsUrRNnrFrwD7Hw&X-Amz-Signature=9cd31e2601673d1d93853116f42d14f41fd53de037adb21533ebc70fcf17e5b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2DP4B7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCTktn%2BQH3dBL6UMdWl587WqQaeQTrwYvew9PifWxmV6QIgAt%2BUVa589ev0u4adPh%2FANrQhRTpZKfpwgchZZ9eqTRsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMd07EE8M6NaD%2BI8aircA%2B%2BIFp3buegP3yYctI8T%2BS4CfoJtHor4JeK02pWT9MjAQuEKoQYbjt33fAQbtGkUL%2FLvRIelQRktitKN8TSYhmojCGx8MhgyzstudslyPmPOF%2FV1AO3z1b5oUd%2FhQKjc7h%2Fipc3cuzlBXveGJnvaSsMFVmnZpEdJyeUm97skJDorDAFY4RdkmZ9Y9SitLxnVJs6yCRKiBqu9UvdiRQnNsj3bwGEepu3oiPm%2Bg77ULa0Wq5bEkqW6AGH45TItzmIW5vJ943%2FpnrVVvt4syNKkjo4cvU35b6nOKcBbZDfFaMLOU6WAqV9nSUjiJo0%2FygjS6uh8KpE0aLY2N9Xy01tZvbVENMuxYr%2FczblOY6xL%2FRVL7MwPXSn6tqYKYIGJboC%2BgRW5eL2rWaJP5NphRSD%2BsGuaUEWQrfwyBclZeXGNx%2BSUrB%2BR52cIodvldr28Z0FI%2BWrdkAM9Xfs%2FUMdiuNTZbTrQwojEu%2FZ0I9GJQDdETgV4zvDBqCKgcVIQ8VPj9LF%2F5YSFppT0ledZZzt1YmxnNCX4UzJVF%2FJBAvbCpKZPI9VlNwJgf5KLjUKPPSMv7zjfSErrc%2BqK%2F9CALczRx%2FDNXj%2BdbYXUCFXYxBS1C1%2FD21QuwqPSdqZtXuzYVRBCMKr5i70GOqUBN%2FL9AMQZvYe8R1K1ALM80k33Va1WW08xIC%2FDHrxmm502JmOWWuWDeGyVLXDSJCOCZdES%2BpI%2BjYupcih%2F43glMOUMJt2RMwLTi0jKkYwGj8jh4hDCofzeV8NvUG4fWKbxnXIP3SblpTmvwZZW%2BCgO59WYRmK17ztr36ysXPBAxldHFhdzzLvWnTi4%2B5JF4Orwu89gY2xgNHnGlSg9e15g3Vjp3ZKp&X-Amz-Signature=4e86d53c4c020906ea0f025a2c8291335be3d5986b95b35ec3029112653cc683&X-Amz-SignedHeaders=host&x-id=GetObject)
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