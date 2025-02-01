

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=bdb79747549ee3278f281f2c5758b779c0f849d68fa6a0e023dfeedf94468e19&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=9ae1dd37149f0cb6680dc3b53d4e95bdf002165ebe63e23a44f8e376942ab208&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=dc10126e13d8ab49d102123bf630037a17f329bd8a8e311c5d9261b153de73c6&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=e5c5aa2e7738e8b6a2ca54f88f5be97429658dd4f02c36b0743f5804121844a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=97ab5fb63149ccb9f611461fb3269d6ec1d95cbc8e114614c52785a62a97e17a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=ec542b203dac4ef8e188f5da1235b1c087bedb825f1d93b41e3f197985c4a3d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=2811c50090f30427412294be6a8eb00964c1c249daae6a612cba9ce5560e4c76&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=c1a2877a2568f1c63c981fcefc6a64eb74e3a41eb9b1097da2697e4ab3e6df5f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=b848fd39ee68a9ffb5f20730a6a89d9d63ac6b5e82f4f78fea0cbad84cc6ff74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP4BED63%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDd%2FzbSKfo0rCsnErz0bK1MfYVfcokABSkuumeGMgmqAiEAlCsPSHnnKr4P3w0yAQreggPzxqG3jI%2BE%2BPtU3NNsvM0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJq44RU4Vwx5BbNCnCrcA1eb9zjE3K5RHvaKpCV%2B6a3yTUqVxnSZojqHjr%2Fs0%2BR7UnlSWz7KYfsCjCO6FNNHOtikZemCWUxUsETNHTg1FB8XHcw6bmVcBm2HCnOp18hSXfB%2B8gpvopRhSNjb4HvD03UOb%2Fnahn2Gles9YOzxTnUoIqTl6E8YunP%2FZMHSJpRv2jW95UDN9g5XRTZYWo%2B2niUYRsaOJyipx%2FanXw%2FyQ1uYlBYvcxu4oR6BqfY6tGig0NXneGFlno00XTYYYF%2Fk4aQhbxs%2F82ISM5vHoKwaEHVPMfeE9MQ2Pdax3LuWUsaE2NYu4VCLB16rSndHIPm3aSL2OPHYx4RGFiEO7H1o1XwbsLv82JUlOuFj71vxCZrYpUjSJl95s4Mu5uDZzqvJjbUzCrh9fzYw9MA48z3MdLIYW2B47Lng29tYlGMdOAIgiVwuPltmvY%2BHyEDZ%2BM8Xco%2FlB2iK%2FgMRQvnSqGgAyZW7MbjfM3cFQ8Krb5BxuAXdbq6KSIkekwie8bUarRL1bGia660w74QC5fBr4W7Xzjusa787YJJtru%2FF5BDhBFVLcPjkXpECA7Vj5TIodYrLrswJ5tx5E%2BrkANKuVaVXQJLL1ZB%2B5pS2A%2FO0iZRPwDdpZ8I43wgOcKAQmTcrMPrK%2BLwGOqUB0Uz3hjmKoa4D4tfSU7QVusBanLG12eSOtIkol5cFgcrrvbGuVlr8l8oNarvWkUM5o8qi7Jm6150YqhzUwGOti%2BMWsxm9%2B509wQTWFGhrF%2FmQllG0ua0%2BQQ9YXOjZaq%2BFQt7KuRTFNGSjyqxVCoq4qILYJ5NdJu1HkKhQURxnId8MboITr%2FyfU2bZ9ARLlWsf4kesdA%2BBGUpmcndLPZF5LAOi7MI4&X-Amz-Signature=a00acdfc34eb75f8524dd98e4cadafe92c8b3fc400d748dceb1578c1fe19e548&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP4BED63%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDd%2FzbSKfo0rCsnErz0bK1MfYVfcokABSkuumeGMgmqAiEAlCsPSHnnKr4P3w0yAQreggPzxqG3jI%2BE%2BPtU3NNsvM0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJq44RU4Vwx5BbNCnCrcA1eb9zjE3K5RHvaKpCV%2B6a3yTUqVxnSZojqHjr%2Fs0%2BR7UnlSWz7KYfsCjCO6FNNHOtikZemCWUxUsETNHTg1FB8XHcw6bmVcBm2HCnOp18hSXfB%2B8gpvopRhSNjb4HvD03UOb%2Fnahn2Gles9YOzxTnUoIqTl6E8YunP%2FZMHSJpRv2jW95UDN9g5XRTZYWo%2B2niUYRsaOJyipx%2FanXw%2FyQ1uYlBYvcxu4oR6BqfY6tGig0NXneGFlno00XTYYYF%2Fk4aQhbxs%2F82ISM5vHoKwaEHVPMfeE9MQ2Pdax3LuWUsaE2NYu4VCLB16rSndHIPm3aSL2OPHYx4RGFiEO7H1o1XwbsLv82JUlOuFj71vxCZrYpUjSJl95s4Mu5uDZzqvJjbUzCrh9fzYw9MA48z3MdLIYW2B47Lng29tYlGMdOAIgiVwuPltmvY%2BHyEDZ%2BM8Xco%2FlB2iK%2FgMRQvnSqGgAyZW7MbjfM3cFQ8Krb5BxuAXdbq6KSIkekwie8bUarRL1bGia660w74QC5fBr4W7Xzjusa787YJJtru%2FF5BDhBFVLcPjkXpECA7Vj5TIodYrLrswJ5tx5E%2BrkANKuVaVXQJLL1ZB%2B5pS2A%2FO0iZRPwDdpZ8I43wgOcKAQmTcrMPrK%2BLwGOqUB0Uz3hjmKoa4D4tfSU7QVusBanLG12eSOtIkol5cFgcrrvbGuVlr8l8oNarvWkUM5o8qi7Jm6150YqhzUwGOti%2BMWsxm9%2B509wQTWFGhrF%2FmQllG0ua0%2BQQ9YXOjZaq%2BFQt7KuRTFNGSjyqxVCoq4qILYJ5NdJu1HkKhQURxnId8MboITr%2FyfU2bZ9ARLlWsf4kesdA%2BBGUpmcndLPZF5LAOi7MI4&X-Amz-Signature=97f66ae78d8990c0ff718ea512efa5852ea2d4319b7a4ec5f3eb4fe7c17fbcac&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP4BED63%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDd%2FzbSKfo0rCsnErz0bK1MfYVfcokABSkuumeGMgmqAiEAlCsPSHnnKr4P3w0yAQreggPzxqG3jI%2BE%2BPtU3NNsvM0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJq44RU4Vwx5BbNCnCrcA1eb9zjE3K5RHvaKpCV%2B6a3yTUqVxnSZojqHjr%2Fs0%2BR7UnlSWz7KYfsCjCO6FNNHOtikZemCWUxUsETNHTg1FB8XHcw6bmVcBm2HCnOp18hSXfB%2B8gpvopRhSNjb4HvD03UOb%2Fnahn2Gles9YOzxTnUoIqTl6E8YunP%2FZMHSJpRv2jW95UDN9g5XRTZYWo%2B2niUYRsaOJyipx%2FanXw%2FyQ1uYlBYvcxu4oR6BqfY6tGig0NXneGFlno00XTYYYF%2Fk4aQhbxs%2F82ISM5vHoKwaEHVPMfeE9MQ2Pdax3LuWUsaE2NYu4VCLB16rSndHIPm3aSL2OPHYx4RGFiEO7H1o1XwbsLv82JUlOuFj71vxCZrYpUjSJl95s4Mu5uDZzqvJjbUzCrh9fzYw9MA48z3MdLIYW2B47Lng29tYlGMdOAIgiVwuPltmvY%2BHyEDZ%2BM8Xco%2FlB2iK%2FgMRQvnSqGgAyZW7MbjfM3cFQ8Krb5BxuAXdbq6KSIkekwie8bUarRL1bGia660w74QC5fBr4W7Xzjusa787YJJtru%2FF5BDhBFVLcPjkXpECA7Vj5TIodYrLrswJ5tx5E%2BrkANKuVaVXQJLL1ZB%2B5pS2A%2FO0iZRPwDdpZ8I43wgOcKAQmTcrMPrK%2BLwGOqUB0Uz3hjmKoa4D4tfSU7QVusBanLG12eSOtIkol5cFgcrrvbGuVlr8l8oNarvWkUM5o8qi7Jm6150YqhzUwGOti%2BMWsxm9%2B509wQTWFGhrF%2FmQllG0ua0%2BQQ9YXOjZaq%2BFQt7KuRTFNGSjyqxVCoq4qILYJ5NdJu1HkKhQURxnId8MboITr%2FyfU2bZ9ARLlWsf4kesdA%2BBGUpmcndLPZF5LAOi7MI4&X-Amz-Signature=a0a64d90dcbd97684da812362e6e74e0414d45292efd355f5091ab807099e57b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=2c7a13a11671718cd5d119cb5aacd225e236b7492978b0c15ad63e0791fc0265&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=a8454019cd798ab34c0dd25842d6a824db9c892cc6a839b1f463b24d9b181550&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=37422a2438cf184863a28aab4c3f16ba59c2e50f8c7512d56bcab0054e248c6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=e819ecb6c5e5e191a83e7a06bf3169af7980aeea765f68bd4e65a905dbfc7f92&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=e9735c089a74be21d7acb347ccd9643cd47d6bcd707cfd50ed1accc884279220&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIC62F2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTTd8Sdvx6qCQCGafmz%2F6Ka2%2BNA4g501JP%2Bmhs7pXtbwIgIyf2vzPuZuSR%2BiWbZOcDkiVhjdx%2Bvz3LCJTi7xcQE1oqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIx0akAp7Kf%2FHx5XvSrcA2r%2F3VHb8UF%2B2gQWjAJa4kJ%2F%2Bmhkv%2FeFbVsUa5nXZMxih98PTNz7hWMo7IWu50HYlwFZzyn3KOyaohyQ0Epsy0AmmWpd2eYdkKOQaodqAU18pOyawWoIjMMPIp0jG161C2SPB0Z3PNLCD854PuMtacfIWSnD%2BRFlVOS%2Fnv0%2FzpuwaYkxNcU%2BSwFfDnAcB86tR232wcnNcNr5amjqwLUiufwCY8GHJ8Zl%2F46f54LxyZDL1mAZL2Ay7gt1xrlUjtSVUbuarA4KXL8Vow7Eq%2B%2FLZWR4GIT0DaaWxDx8qTM%2F40dIULU5h7DHvoKj5PIee83YkPopNPIN2qQBODXkKWcEVpCTbbd%2FqRiTAZep%2Fw%2FJHii%2F283fkzUeHgeHmshbfV%2FnlbpQNTBIeI7L7Ma2KHMvBe44fnMXO%2BMHLzgrdtTUFlwLyf6xbJdS3mVf0WyS9PiLHRqYNm9EgOJOGiXXzcFT7cTvOkvDfKGarQmSTvTUVQ1TF2gfYCM%2FglvP1HQ0hf%2B9qzuNuGCAP0ySIZgrHfVYQUHhmXp9yB0CYzVnQVqMmYw%2FXkHSeTkfMHQF4jDVWhqufxFLFrwc6B90Pnf5xBMGXWM8MHtz7%2FDCywptfTsXLAeX4HxrgA8FT8w11B21MJzC%2BLwGOqUByTIZsshAt1P99U%2FkIL0kxI42F44WwanxamovYvf5gdiff25fEqzrVaG6k0x5QSAfyOHJykazyEehgd%2BKhXc20vYBGFRV43ozU9rtCBq9KQxW0SD3zMn8OgqD2L8M7gHc1QL73G85b7%2BxwegKm6RJH3fKlqky0%2FhQj3nBWp5MWreR%2FrOwKviARHPJA2gNCPJ%2BVQ%2BM870H44i2%2B74Tsji6LW6Y1URo&X-Amz-Signature=f385feb5123e8f7f4b8deb5f6c28a006ea8daf4fe92b607a5ebaa9348d7267b6&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KM7MT36%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnsvdP4d%2BwCwfqU7FzHZjpW9VOET6Pb6wU8czYTgdlJAiApw5CWHMEXfJ1qi%2FPMi7uAUzQaB4J1WWyHdDPT4Lik1yqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT2YJ0HyQLfA3yQT1KtwD9lRy34Dl%2BlsVn0hKNuiRZX22qNWswiDu76ua9EKXEn4%2BdJws%2FoYiTpj3JG60dORy5DA7%2BlY6CvvIivC2n1j8q1HboCRF4A3MHVUD22s85W6%2FvhERv%2BlubglcVP1kKMdQpNtV3XE77cN8G0nhP%2FxZu%2BrI0EEaNpBKZ64RHVbyhC6dd8iY6gkDO9kKu%2Bq6%2F7vLNWndf1kTuxRS8F4OfQeebBm2yuaLiJ33rAWGHf3ByY9PQQrbf2HZVLn%2BvbXvMVEgF6ie7G4JuWYS6m6VBEXbo4jONvxfEkva421C5mIBHqHbXxpyH6G8IcleXAITJutzPD4W%2B4uhoK9LE9cP4OEPrDd9MuZBWQFz9QXnzVbycplE11u9izzFplo7Jfa%2BBEXrujOlaIPf%2FOMbB2MGqwQ8743YdKBUHt7SH%2B9VTiV4aY7xHKQ7YmB9fs6yc0JKoNhuBLOhxFcChh6uBm%2FRCrZRn%2FyMxrGajYU%2FB6hQl97Xjd0xBtLpHDt%2Fg2lI1aLqDRfpUV%2BURKYoKK5EkqNd7uSpvZAYOFwkjRr0mmMvCscXIdNh169kV14E%2FCqts7FqiZLKM7%2FUePVrmS%2FIpk5F3Y0FjjlELuwefaHUJrUGDwoQf%2BnJDyQ%2B7uXkjw2G23wwtcr4vAY6pgGktlxY5XwGQ9sy6UB%2FyUtw1%2Bx17MWhnZmXP%2BLbCfJVthOenCBVmevF6uEuCUobbfk36TOx%2BM7jzpmkzGPFEwgNcIDM2Jf9Az5z4AmGyod4tCgNUNJNZ7mFdpvzrRkCbS8Vs3z0LKoiHvuK39Ke8t9vNvNYI2n87cZjRe5rrBfnyqmj7LMs08o3LQ2yX%2FzqS81UPa6Ma%2Bg%2BHw0mXI1CKDyGzczAqPpG&X-Amz-Signature=bc88f99952bdaa0220dac037d754e95800c23928a419f2ec7a3d22488e5b32b4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KM7MT36%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnsvdP4d%2BwCwfqU7FzHZjpW9VOET6Pb6wU8czYTgdlJAiApw5CWHMEXfJ1qi%2FPMi7uAUzQaB4J1WWyHdDPT4Lik1yqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT2YJ0HyQLfA3yQT1KtwD9lRy34Dl%2BlsVn0hKNuiRZX22qNWswiDu76ua9EKXEn4%2BdJws%2FoYiTpj3JG60dORy5DA7%2BlY6CvvIivC2n1j8q1HboCRF4A3MHVUD22s85W6%2FvhERv%2BlubglcVP1kKMdQpNtV3XE77cN8G0nhP%2FxZu%2BrI0EEaNpBKZ64RHVbyhC6dd8iY6gkDO9kKu%2Bq6%2F7vLNWndf1kTuxRS8F4OfQeebBm2yuaLiJ33rAWGHf3ByY9PQQrbf2HZVLn%2BvbXvMVEgF6ie7G4JuWYS6m6VBEXbo4jONvxfEkva421C5mIBHqHbXxpyH6G8IcleXAITJutzPD4W%2B4uhoK9LE9cP4OEPrDd9MuZBWQFz9QXnzVbycplE11u9izzFplo7Jfa%2BBEXrujOlaIPf%2FOMbB2MGqwQ8743YdKBUHt7SH%2B9VTiV4aY7xHKQ7YmB9fs6yc0JKoNhuBLOhxFcChh6uBm%2FRCrZRn%2FyMxrGajYU%2FB6hQl97Xjd0xBtLpHDt%2Fg2lI1aLqDRfpUV%2BURKYoKK5EkqNd7uSpvZAYOFwkjRr0mmMvCscXIdNh169kV14E%2FCqts7FqiZLKM7%2FUePVrmS%2FIpk5F3Y0FjjlELuwefaHUJrUGDwoQf%2BnJDyQ%2B7uXkjw2G23wwtcr4vAY6pgGktlxY5XwGQ9sy6UB%2FyUtw1%2Bx17MWhnZmXP%2BLbCfJVthOenCBVmevF6uEuCUobbfk36TOx%2BM7jzpmkzGPFEwgNcIDM2Jf9Az5z4AmGyod4tCgNUNJNZ7mFdpvzrRkCbS8Vs3z0LKoiHvuK39Ke8t9vNvNYI2n87cZjRe5rrBfnyqmj7LMs08o3LQ2yX%2FzqS81UPa6Ma%2Bg%2BHw0mXI1CKDyGzczAqPpG&X-Amz-Signature=1f08d0b90d70bca71c67c06aa7293cfd7e385b53ac822add266656e0eb853c51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZ56EQK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEE9XfOuK32%2BH8RzE3Y8FxiOhH%2FUHet0qKhSHb2H3meLAiBHRvpVuJAgOYhvXr3Eh8MksdZi8lWTE0%2BYNUOasTgyZCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYK6c7NfRzFqqFmGMKtwDs%2FlG1dsBj64kisZJlRsvgxHY0MRY6KCeQMmas4RpWrCKQdRBzWbUJFWwnOBeLZ%2Bwdl4yt1K33dKNq%2Fc7Au5r%2BJQ7z%2Fx5iPCKIqWHe82UTAqinNH5at8eecLLmJTVb9wCKTKdMIk4domQRk0%2BkxexmSy8mUII0n1FnfqUXBQCOwXpLdHMljr%2FloeMVRPh8aFEMKcS29wnZ1kNApy4kXcydW1tE4UCeDu0WNQ0BZ%2F1GtIzOyoAVNPNI09Np5FghudreHzFowLRdJO9wuXHmhJII7URsBbUNKGVwiU6SqKZH%2B7kLhYPogWwTSDlcCzYhMjdyAFXSuuNQ5UVHV%2Bf6HspWTl%2FJeZ%2BUcfaQiAmg5Ahl0aMO2oz78tY%2Fwo3YxO0b%2B1Qv5AaxGgXNBLW02uweUkjczuriEI69Ym8TjYkrfsn4nxeOBPAkvzTT1ku6WgCoCwbc9CvSIwSZbb6AJNMh%2BLyOH49ta1hez%2FSorx9uuqV9mUTuB3Vf8YFyPu6AuyZRVt8BWvabIED4x%2BCtRpXS9JXs361GuGoSb5EL2TW4lp24xFVxZp4f%2BrTt%2FVjyF6Bc%2BLGtq8FiB2mgyjxpTX4Mf827fhW24rMjbIutOgkjP1clFW1eI5S49UOPTWio34w0sr4vAY6pgGE3AKkaOAVkdli1WMh%2BqWDUyn3d%2F8t6L14bIl3jFaepxFrwpkh67zr6KfUq5h078N2nxeH%2FQCcKV91O1yjqscuMpa%2FinKrTbCTsr4sxXnouGTEzEZp%2Btj2KXlgvMCnE%2BQlyZ6Ma4AhXrnszWUdYnlki2jVgkjn8LDS%2BeBvjNpfV9x%2FTyut%2B9fqvNoPLjdtHfDmoHewjGmjJYw2uzqGlGaQNbsmH%2BQb&X-Amz-Signature=2e9142c2b03bc27a9a8bd70cc2f86ab4de4fac55fd072c36029cbc9f0a57b378&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFHPY7T3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3tqp%2BVoam2SAEeETGccvKSc11oMK264CiuL9yvm7i7AiEAxsOaSUgxdHrfk0V%2Fp8lld%2FGdxjssgP%2Fa0h44zKGVXE4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcGaZ6LvaIV5N%2Bv2ircAyRdqD%2B5tqvGvZND%2B4MvDJVnjA5vasHw0yW3H5SbML4sPsrwoVW4hG81xJ1WHqjpuJST6kAOn5mu2GfvIiSn6ajENen8rmCbyg31fd16qQmB74gUuXWc46GwKD3R1CFDHVY%2B%2Bn1cA8mdmbCG8hYIWyeGhfsyTkW8duKHyINVGlcDl0Aj3sDakCJRAJY0O6euSV36NtOv4vXdMlLI6w%2BzydBNew3P2om4AgfnFyevjnf%2F4dWsFTPhQWrT3aPb%2F172ExwkECTVtn%2BaId%2FizIkvyBOnRQE2Z5bKrCPviDYQMb5qkwtwIB5jvtLXILsFsU0cZtbO%2BvbQcAMTvXq%2Fm%2BPT607nnd0%2BtCST5JeoRuPfCBZf6Dued6%2FtOi10XgVtsjOzwVUUeB3jInmS7tPtqiJJBjkuk98LUmKkx4j8HyHKbaiXhCL%2B3ZTx1wbtyPFE3Ow0ct2Zej2oN73MYtVG92uED25NgF1YxncIIdnEcTruStzKR%2FVHOewjPb%2Fc4O3ybZd7Wq6SrMl%2FP7hSmThfohaTo3EQPF4Ya2Byyfs3leYO1xig6BVO4r2zyKKBR3R7kGu7rROf0pHUiLGJzAxEU01rt9dAOd8PeMC3PYc0QB5KkxPi87dXAGLq5t81UAkJMILD%2BLwGOqUBeZVFCTeHUTmau2nm9dCztyWUrmmZ1sW%2Bv%2BO8GV7hdvCLIYavLLlJCNMuRyyBvziWyrmNMu%2BzUsy%2F7NMMmTqDUx42sNuzZVareN04QDF7K4YkJIhzECiAyKJlqPJLYKmkoRltF2FWh8XfF%2FXdGKa%2BnrkRPeJH9QdFSKl%2BLjBDvbYcTsROCbxLoyFVnUDpDHbt19p3yHWMvrSBPH%2B1fu9VGa3NhTbS&X-Amz-Signature=44cd14c838a5f1ae3d525dbc4009e14c81802b2f7e77465f15055af371ef151b&X-Amz-SignedHeaders=host&x-id=GetObject)
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