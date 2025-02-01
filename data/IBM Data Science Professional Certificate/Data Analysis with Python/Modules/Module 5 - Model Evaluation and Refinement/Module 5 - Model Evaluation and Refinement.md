

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=332faa944e4624e578a3c2e4ff6c41cbcd9bdeaa6630ff09fd488f7c0269160a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=c296d85788dbf35ecb6e930d09e820a2f63aa9ff4f21ae2b6aac32c101310e7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=131220d226216cf3975d20a83eca00eb632b28f26bb19db1128d53b84200e7be&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=9072b0fd7075eea7e55d6f1651aa995148fd61c1112e586aeeb40e2f227c3628&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=d8ae86fa6707d1a4bc3e2db1ff508d8c2c86af50bf4cdeb21657ceb5c8fe1152&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=507ed06a9391920285c3e2798aecf2f019d6ac43c654b20dc4f7c9d2a497dd5e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=57d14529473fa1f10c8eb820ea88117379e499136b06e6c45df27da05dbf2713&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=3b9a53d8d973d7dcd9897abf6bf8a8cfc0503ab998724254ebf9b74d6ae299c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=7868c93d5c9d20fe579c6d182855967c34dcef6474922f76736547129423afe7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRGRAKGW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe9cd1vbbdT3aWUtho3epqaphSaWIXKuqDMshcwrRrNAIhAIgOC5LoR4a5rb6r%2BCElfm0hrltmj034ywnpaHMA2qoLKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoJ2DWY938svuf2pIq3APH8gQVLBaXErv0qm%2BYFv2U6Tz58vkQ0iqLxVbX9fbAjmjJLVdCfv%2BnF%2Fzl7W2jykNx88o3l4JgNzkp86KnWqyvjBFK56c4zGlyC4AA11KR9fnnQJuDTC4mi%2BCg4OAoBvOhnmfcu08%2BqeyqF7rYxtKOf3TK5pjz%2F0Cou0Mr7ELBE2c4BkCr2muDpGYXUEen4ZC3noR4s4VHmNvM5hEA1ByF%2BtmBjINF7YQiiW%2FGbj7AtidduH1XCOLkQQKuiC05038OsmDBpSByA66dvYxpT%2BAYT0%2BhATXid6M7VX189xJEQXlYX67mANHO9uM2P6gKVNnb4UVqtmK%2Bzagd607e3M2AHSKmqokLGq7MVEciHIRVkwo2Wn2bZWlbc2i%2B3Lmn6tRQ3PiaOerLREUnNGSPG7x1gS1VlvKlrxMDG%2FwWPb8dZdDxP7nhIY5RJGAWio6gy3tZe39ZbIWL7C3z5FtBndsiR8fZJWVaGK%2FtqalFdmLzRyHxzROq2EB%2BrToMB1WELIAdV4j0WEX2oDowRZDofdxfjOHc5j2271JSyIY7XlkLRNqy3SWB8YzvmK9%2F8xTQtadXfqFE1AgG6uVWBXYvtNxcmikXb6050uLd%2FnqRNfxJeF6JQokbq4MwcYLykjD2k%2Fq8BjqkAZ3DTBK6MJpDNKtmM9e2mtvH8rRMZcPT9uvONgCVxEZzdPc5whLgap3YjSBlw3Nq%2FtgQ50O27ylyZUpIXzbA1IGMEM%2Buaf%2BN6GLQnTNNc9x6TfRHJkUpUCDT1Ig%2FHb1bArUN%2BrS7t3qlq51nqabbEyQjldgSVxovh%2F60cMEwHvk6uwAnqRXXUVdzpT1e257trIKzAj%2B8bqir0wqr09npo0bvHtwu&X-Amz-Signature=9267ac3165b7b3b747394f14a438e5dd9dff914aaa240f2b723479fba8f4e2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRGRAKGW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe9cd1vbbdT3aWUtho3epqaphSaWIXKuqDMshcwrRrNAIhAIgOC5LoR4a5rb6r%2BCElfm0hrltmj034ywnpaHMA2qoLKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoJ2DWY938svuf2pIq3APH8gQVLBaXErv0qm%2BYFv2U6Tz58vkQ0iqLxVbX9fbAjmjJLVdCfv%2BnF%2Fzl7W2jykNx88o3l4JgNzkp86KnWqyvjBFK56c4zGlyC4AA11KR9fnnQJuDTC4mi%2BCg4OAoBvOhnmfcu08%2BqeyqF7rYxtKOf3TK5pjz%2F0Cou0Mr7ELBE2c4BkCr2muDpGYXUEen4ZC3noR4s4VHmNvM5hEA1ByF%2BtmBjINF7YQiiW%2FGbj7AtidduH1XCOLkQQKuiC05038OsmDBpSByA66dvYxpT%2BAYT0%2BhATXid6M7VX189xJEQXlYX67mANHO9uM2P6gKVNnb4UVqtmK%2Bzagd607e3M2AHSKmqokLGq7MVEciHIRVkwo2Wn2bZWlbc2i%2B3Lmn6tRQ3PiaOerLREUnNGSPG7x1gS1VlvKlrxMDG%2FwWPb8dZdDxP7nhIY5RJGAWio6gy3tZe39ZbIWL7C3z5FtBndsiR8fZJWVaGK%2FtqalFdmLzRyHxzROq2EB%2BrToMB1WELIAdV4j0WEX2oDowRZDofdxfjOHc5j2271JSyIY7XlkLRNqy3SWB8YzvmK9%2F8xTQtadXfqFE1AgG6uVWBXYvtNxcmikXb6050uLd%2FnqRNfxJeF6JQokbq4MwcYLykjD2k%2Fq8BjqkAZ3DTBK6MJpDNKtmM9e2mtvH8rRMZcPT9uvONgCVxEZzdPc5whLgap3YjSBlw3Nq%2FtgQ50O27ylyZUpIXzbA1IGMEM%2Buaf%2BN6GLQnTNNc9x6TfRHJkUpUCDT1Ig%2FHb1bArUN%2BrS7t3qlq51nqabbEyQjldgSVxovh%2F60cMEwHvk6uwAnqRXXUVdzpT1e257trIKzAj%2B8bqir0wqr09npo0bvHtwu&X-Amz-Signature=05a53c0c1cb6fe4269e40188ef7036521dafacac27c5e43ad8dfa0b49d486156&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRGRAKGW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe9cd1vbbdT3aWUtho3epqaphSaWIXKuqDMshcwrRrNAIhAIgOC5LoR4a5rb6r%2BCElfm0hrltmj034ywnpaHMA2qoLKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoJ2DWY938svuf2pIq3APH8gQVLBaXErv0qm%2BYFv2U6Tz58vkQ0iqLxVbX9fbAjmjJLVdCfv%2BnF%2Fzl7W2jykNx88o3l4JgNzkp86KnWqyvjBFK56c4zGlyC4AA11KR9fnnQJuDTC4mi%2BCg4OAoBvOhnmfcu08%2BqeyqF7rYxtKOf3TK5pjz%2F0Cou0Mr7ELBE2c4BkCr2muDpGYXUEen4ZC3noR4s4VHmNvM5hEA1ByF%2BtmBjINF7YQiiW%2FGbj7AtidduH1XCOLkQQKuiC05038OsmDBpSByA66dvYxpT%2BAYT0%2BhATXid6M7VX189xJEQXlYX67mANHO9uM2P6gKVNnb4UVqtmK%2Bzagd607e3M2AHSKmqokLGq7MVEciHIRVkwo2Wn2bZWlbc2i%2B3Lmn6tRQ3PiaOerLREUnNGSPG7x1gS1VlvKlrxMDG%2FwWPb8dZdDxP7nhIY5RJGAWio6gy3tZe39ZbIWL7C3z5FtBndsiR8fZJWVaGK%2FtqalFdmLzRyHxzROq2EB%2BrToMB1WELIAdV4j0WEX2oDowRZDofdxfjOHc5j2271JSyIY7XlkLRNqy3SWB8YzvmK9%2F8xTQtadXfqFE1AgG6uVWBXYvtNxcmikXb6050uLd%2FnqRNfxJeF6JQokbq4MwcYLykjD2k%2Fq8BjqkAZ3DTBK6MJpDNKtmM9e2mtvH8rRMZcPT9uvONgCVxEZzdPc5whLgap3YjSBlw3Nq%2FtgQ50O27ylyZUpIXzbA1IGMEM%2Buaf%2BN6GLQnTNNc9x6TfRHJkUpUCDT1Ig%2FHb1bArUN%2BrS7t3qlq51nqabbEyQjldgSVxovh%2F60cMEwHvk6uwAnqRXXUVdzpT1e257trIKzAj%2B8bqir0wqr09npo0bvHtwu&X-Amz-Signature=6cb5fec92a629ec1c747c03e138e1e3a178dee9b6ab49a24a2c459d7080b7bd7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=e022913b7ec62ca234cfa7797d206cbfc80ffa7b351e562f4347c0fe1b8ace32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=bef9d1d9e93f4f0f4956b146912c40915343e52706069e9ba8fe5dea7e68a5a4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=fb699111feaaf22488ac03039fd4159ea0124def306b31096268ce98e3294d94&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=720648d56420c1844a1ff5405ea6fdc3c10df2e7955d9248c2656a43434f31ba&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=0dc07365c67ffb875bb99bcc9bd81f268d977480cfc01802bc27c09fbc54e485&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSBJPT2C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx1nYf0C9eTpXbCvviZn34MGXsFXPBzSspyICF5Hs79AIhAL%2BTIyH10%2FCDS0L%2BvkZVMF2awHjPuYoTPx4fRB2p3%2FbjKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwO4hZDaznUjMQVmjkq3AMydQb86jxSMzy1iC5gOzqt4ZfhiRPLA7O4N0ef6uHBeV4gAFuH00uB9XoNW1gyQ0XHn0qjC0nmRXNBre1Qmo2oSZiux96Gjva2gXtnZ78wbWV80bhgK2lFKw88VfKidw5JrpDwpdyQeqtNRUNtJFzeSK6wFARIOWz32KsDk6e4z9USS0uXL%2BcNhn%2BGrMClPbVJNBw5VVqp%2B7wdmQX1TXxnN5jast%2F3UdsF5pAjQ0aboDKeeSnqoGeAxEh7oNQl%2FAqljtLqr9KsbbRhbSjYM4YwTAhUOUxjoWk%2BPj%2BDqePlco23c%2FyNXlzDjMVEYQPuywJLmjdzCy3i4Nx1cO8%2Ffp61f3UPICJztHBDDO0mALeEy8f2Bn6fPxOW8maYf0mhcMRtKMRr38KSCSmDPKQMCZ%2FIbsQUDMm9zvVS%2F%2FMaipH2NC%2Ft1n56lWF08l7o2lYEE85qv9J5B87f2Qel1QP%2F%2B3ernRTyo2veLd%2FC8BtzZJLHlZm39n6i8oegBodISIzImx5wf7fT77C5DmoQZtyVgQq41WIPNz%2BZ5H63as1moR6rrX8%2BGmcF2aHHWKQnUpZQdEdjulZ7zGQchTFA%2BamQgz2rPNsTxL%2BQCXrLjGuYZXjBXYGlWWjTVTRCKvjwIDCtlPq8BjqkARBDsF7kBMgH6mWCiFf4kBjS07T1ypzuJkHn8u7asekF0VPKRI0Fr912C3PdQmIuPUA6s0XcOlLmpsy1g48yZYogv1kj12J%2BJX%2Bncms%2BFrs%2BfoAAowODSQhvtwXaOrhYNzW9qdwgCYfYQSZdmgzpnbgiipxE%2BwlPCQ6BjJlYhVLcUNsQ8RCrDbUzWIZBFUtgTsuctnFiSNwEIN%2BzKmgQp2DZbb0z&X-Amz-Signature=cfbd0fb35d39fe66a90ebc37db36424c2369bdc8e7dee6a4e4ea83cc7008c0f4&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YETV7VET%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1YTg7ydSuNR3a0ZlWxfDEaLjR7K7myDNJgsBow1678QIhAKnjAPZni9yc52ZfJGa0OdoiNTvx%2B9%2BRoXXHuF7Ct8myKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzp8nDgnfcupfNUWJ8q3AO%2FmK6NrycboUAPKSSxtUycosNNtoLTQMFIro7bRo%2BVwAYTG%2BAJ67m68hl8n3A0f6O6dWHbbxcQNAog1hYLBY4TAD%2BiB30l7F2fXv7%2FvbxbzmuTPY%2FkeOkDIodnWyLJ1298dRHUTL%2Bd%2FMZJNH0tvhmiyCD47MVrW5ZBzvX5FlMq7UogdSZp73UiyWHdfylN18bwXx5%2B2oQMDG13W3%2FcTce21aCBy5yjYasNrRDRBGHGB6IgCArBwMPIzrLeva2uiQZe4VwXnMQqDuQITCzlr8CnkOYXrp0GlgJekTQwujQu3RWNdweRd4dVPj5ARVcUzTn9fpvqrFX6o5GroY8kIV%2FMU3F3pEJfkoVdMPgyLXDPcpQgb%2BK7EPizyjLWhRGfbWLAdqhWGUlFONaBUihvYL479srwgxoYHTAM2mLPsXkDWEkISXt%2F0dWIM06JL7x5W8oWyAbjG5d3BQ01c%2FW3zHBAZNaBYqYN7SeHRQp0tejKUKLpg5flxqR2bFjePobnrZlytMBxWVS6KD8rS8XWXDKPrrRQZz5My7eTsUByKk5adckAnNBftLKhv5lAdGTHiOZgq78fIO7Dk3z1Xgof867I%2FVOyyussBVYvwtbmbJZYWllaGrrVXoENYnEQlzDik%2Fq8BjqkAaHkD1R0kWidtsoKM1X3XJztRvDmnta6IQOaP3TF2ijVq%2BSqYmEWQyG9c02gnssvp8d2o6mt%2BsGuMQTF565K5hXtHK3vNufCq8LeH3rmhuptj%2B7ZroQeI6OJBw5Ttxj2%2FjwhZmBAZfkZbIMKFcIbl6%2BOCZ2vJpeQTo1IIRDe1sTARiY31V1Tv2MnDyQf9v5lNiPM26W35ulTwji2NUsQAk0eR7VN&X-Amz-Signature=793ea1790ec9ae72eb7e5e01736ffa9e6370686b41e77d4b36fe2a6fcfe7f371&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YETV7VET%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1YTg7ydSuNR3a0ZlWxfDEaLjR7K7myDNJgsBow1678QIhAKnjAPZni9yc52ZfJGa0OdoiNTvx%2B9%2BRoXXHuF7Ct8myKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzp8nDgnfcupfNUWJ8q3AO%2FmK6NrycboUAPKSSxtUycosNNtoLTQMFIro7bRo%2BVwAYTG%2BAJ67m68hl8n3A0f6O6dWHbbxcQNAog1hYLBY4TAD%2BiB30l7F2fXv7%2FvbxbzmuTPY%2FkeOkDIodnWyLJ1298dRHUTL%2Bd%2FMZJNH0tvhmiyCD47MVrW5ZBzvX5FlMq7UogdSZp73UiyWHdfylN18bwXx5%2B2oQMDG13W3%2FcTce21aCBy5yjYasNrRDRBGHGB6IgCArBwMPIzrLeva2uiQZe4VwXnMQqDuQITCzlr8CnkOYXrp0GlgJekTQwujQu3RWNdweRd4dVPj5ARVcUzTn9fpvqrFX6o5GroY8kIV%2FMU3F3pEJfkoVdMPgyLXDPcpQgb%2BK7EPizyjLWhRGfbWLAdqhWGUlFONaBUihvYL479srwgxoYHTAM2mLPsXkDWEkISXt%2F0dWIM06JL7x5W8oWyAbjG5d3BQ01c%2FW3zHBAZNaBYqYN7SeHRQp0tejKUKLpg5flxqR2bFjePobnrZlytMBxWVS6KD8rS8XWXDKPrrRQZz5My7eTsUByKk5adckAnNBftLKhv5lAdGTHiOZgq78fIO7Dk3z1Xgof867I%2FVOyyussBVYvwtbmbJZYWllaGrrVXoENYnEQlzDik%2Fq8BjqkAaHkD1R0kWidtsoKM1X3XJztRvDmnta6IQOaP3TF2ijVq%2BSqYmEWQyG9c02gnssvp8d2o6mt%2BsGuMQTF565K5hXtHK3vNufCq8LeH3rmhuptj%2B7ZroQeI6OJBw5Ttxj2%2FjwhZmBAZfkZbIMKFcIbl6%2BOCZ2vJpeQTo1IIRDe1sTARiY31V1Tv2MnDyQf9v5lNiPM26W35ulTwji2NUsQAk0eR7VN&X-Amz-Signature=29e6fa95d72ee15a3c05647717c28c8912f4003f143a47ffc2ee8ae1c433e217&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB7B4A5O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8EKMzUsZL1UC9Kfco2Vcy%2FY2eBndybrluVNodPEswOAIgCFUZr7xEuNiTbamwW5vvxxgjJRrqxncZ23vlLfF2zHYqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJFSWNRULyF4z9eWircAwZl4kezjs0EvCAYAgOXABj3Fp04Hro6tY%2FhrQK8mWC5VJd6SjdY2WMeMXrsgpegzlMBoyNum03iFOEbxPXf2wRIS27SvFGbMZFd4uGo3%2BbJStIHicD0o3%2FVMUjlNNhJ9K%2F%2BYa1y3%2B1eKPFJtJi13bbHBh8%2FTEVSaxqP62GpP1CZebwfm6R21fLnaLe2JEx9n7XqB5h1BdXNDQBIl08acQggw7j4UkcvgJF2fA4CHlRWR4SlnugDouYMVrZEcURZmcQn%2Brp%2B6SXHIj2gHJZS2eappJZScqZtLGapT%2FRLmijlwLcnrbkQrV4YH523FR9rCxxkHDS7g20jQAsCbk%2BhCDT%2B5C%2BUWTxUZvU4xVzyg85pJDPd7XRhSzDn8OqKwI8YEbKQqJSolV%2BjUQ5Mt3TbmuFEWDUe3ssW8dkk25ov4KhYkak36yD4YqgjkGXPNourHUnBS88gqfbM1nAwOjdPQmhxj4X%2Fy9gLmpx%2FPmVezBsL6fNH8X%2FK7AZJcslSurOY0TXfq2piFtXl0ZnG9Ym%2FY3Awuoz2laaJqho%2FP8ef7%2F0mILSLTM5Vgi%2BThFxtbqLQcMp0SOwJZt%2F3kOQyPPSjPpFa1k5Libl%2BxE7aicwYFPT%2BORbZEUbfjBXT%2FBZKMM%2BT%2BrwGOqUBfpnzBxgSLpbiO1Nh5HqEWRDWSKU%2BNq6p8AoIBNA7ACHSHwelzYFva91IUSbTpWPb596bKBQgoN1Td7gFj47hCIVNxt001%2BDII86cgPqvjmPyjz7puSyEueAER1QIlqMbj9ppAWK9mLnwu2F%2BCb9XSfsXi2wPqrR5bv94tEWqB1HcBw8SYHpck%2FzwApd60fP8DkEKwy5l2M5GNLk96JMGeKqUW3Di&X-Amz-Signature=57b0a141f022216926a40390757c69dc4fda79c723c69eab47e3218a84db4ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2H2VF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD86TSn%2BWwSFV4nOlX0fViGWrOepIAgMRYLUsJY7q4L7wIgFHrV5BXPpMtGBP04OY2TkJO6%2FXC9g190lp2dvj8%2BYPkqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATi4EsPGqw%2FquHrqircA7QarRJv%2BftOBs6y0aHAFQREmIyzjq6f1kgiJHTFlHPS7V1XYqrrfemwAyGsD1I0Zw3ybThgKFzUPSQhbwh%2FDwPF6JfhTAw9pt91lA1X1QLb7Uboni08qYi3dT7KrHZg17SDoLkhQhJUwQShRxWRvXbLRMIRf4USH7AhJnnLFFt2xO%2FHNCSdPMNGXuZW11eVqTj0vnrnh%2BJ1g9Kpork8S7ZqjG82xz28AqPfe5i0E8q9hGy1mKXKUDimd%2FZWK%2FD6bkKQKp3TYCHGp7f3z9ykg9wnz76PQN%2FHDPgIQaFDrg0cFbeAWX3jR0wtWhXhIESz02Tc%2B0Xj23KfZ6Ckwb1DkOafvfafAuyQoQP5ajPUDBxve69e8%2B4bjglrdN31r6liIms2rKVgVOp1an63PN5VjAxlBWAMWDVer8bOsmJ0iYNHiyqUvy7oRBPeQrPK5OIugsEmb2niybDuo3%2B2ahihWTrAUdArLXxgdpcq2qx%2Fc7FhL1ohmMPGyK1kZmzdDt%2BiZ6bGcJhE%2FvI40%2FWZlCYDaZt8nm3QuIeFd56kPijv3P%2FGVgpe3baDeHBDfhmiaOwFuhuCBub1WbpX5LHwQvY14rmzLrgUCUaLNRBQRYawpoTLOrsmWaqZZkWIGKo%2BMPST%2BrwGOqUBF1TC7Bt5iCvoWG2T9cNl46IDIRtQOI5NbAUtCQsebxABZs4X0S3Qknegw9Qmyc2y6l2gPGgJyudircEI690daL0AGnden7u2cC8WeBh6BMrSQWY3L6AHo6OiaEGSqdQp6PzcNZM6hKsGHeB1Fp5FtzkQra3Slwp%2BdsJ1Z2KAKkGGeK9e7aPwQ5amW%2BPdXF0PD9yDsyU5g1jtz5KzBhaJjVqEfx6i&X-Amz-Signature=d79251cc85c8fa9bf7fc2e8195780d843fc96fcd95a6589170dc839f2e894acc&X-Amz-SignedHeaders=host&x-id=GetObject)
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