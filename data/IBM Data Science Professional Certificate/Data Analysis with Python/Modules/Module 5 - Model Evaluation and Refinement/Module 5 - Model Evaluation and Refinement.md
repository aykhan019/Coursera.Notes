

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=abb938c407a5f1fee301397c903be06e84401a9c18b2484adda0a0287461a1cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=0955e74c669ef46d5ff8982c37326ccaf7fe6884d84b4c8d3be0d1b4e9f28177&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=8926ac6063bbdcdd99cb6e9f2e1f4f4f8e2cbfcc8078b17756333139839dde38&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=ed5e7b19017340fe83ea334f8ac754c9e88588959ce4b29130c146c583ec909d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=5e43f661554eee04eb959bd80c314fa2e21297536ff3f6b6f22df11d5c491b43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=328830312665f90392b90a7ec52b0fa34ca205ca9e5600a9bf59a28739aeb46b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=1a49a83f5f0ee4b34594e9dd23c50170801f74325fd8198a9e099ffbc3902d60&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=1544032a0c5a8f14046c8d5944d97e5e1de9110df2b91991f27a4711b47d95bf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=21a851d3a1a86c222b85e193b742f3cc271e434aa104e41d93f49c60c169d336&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNUTA2X3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIDd2MjAXjpPjJZqJvr63kJ1BDwdvSoYuisl79IxyhqTKAiEAnFGMo40kIeABhpiuEDV%2FclqlEn31pgEiFKIPyyeclFcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPdgB%2FmNVuQbkGD3%2FSrcA9O9i6bjKqqO1Wt6HO4V%2F74sHsMlhrK1VzRg465pSKzuPNgMTT04kHlMYFs9yTGnyXP8mi83UinQoUmOQyqG65XlxEs0DlmdlkH7Hd0fAKWD8LeDMbFTbqWod%2Bx4TAf8rfbf0rc4SKFn7kdF4c93r6zTjd9pAr10BDMqAfxnykG6DKLSVhn6T3O3lHPZI3z83cEIwjHGdNXFHZPWmPGCTtfM5Tfm4nJ6mC8zkkLN25CdShVAXAndIsD4ytvAK%2BvESJHToLkewUeduAE5d2dRH4kQDmNCpnRyOn%2BUxlstvHru2M2bKI5V%2Bie%2FDlvn8luk%2FlGVQ5M1ia3C85RO5f77nMJqz3J0Z0KsQ86htRRPYd5cs5%2BNM3%2BdAbcvWNhvl8Lh4POjJjPDI1s%2FsAr0jdZKs16OfWJhtse%2FqWUZmKf3iXaQCWMuyP92YgRPuM%2BzwwfSmMSWwiiPDZOfW3b8jCSXQlUK9nYPVgUvIbATPC5HO4Pk8dv0DLKFp8auTFjPQe4qYicWI5PKaQxVv7tpWwEnlnvjF2Z0Sw6kSGjvNuzqs7wPzOtOFdm5hqkJe8f2Ph%2FIziuDsf6syztKMCLH9o7RNlYY8O6JKnFHHhTWfaxpF8tOeOIapiiDibVBvpSqMLjNhb0GOqUBjOpcFL6oAuIwaBx28IXUrM1izS3UcCmYwfdVhEXcTby8UOQsdU08xUdemZLqyzQMx%2BrSRJQE2d8XJ1KwM24cyQJhrWs7T3YarUnGkCUiBswJ6sSfbI2QGdJkIqaF4ZIUriN0hWlefbvRqw6a2Qd5mWVcOtoAxdDfVoTr6UQpGA0kJpgtUrFy%2FXaHE52v7TVj7E5WePy3YQH5oblClQaQ31qLGAZO&X-Amz-Signature=3c54d5805ca14b564b437c2ac074cba0b5419309afc3ccceb2598248204f11fe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNUTA2X3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIDd2MjAXjpPjJZqJvr63kJ1BDwdvSoYuisl79IxyhqTKAiEAnFGMo40kIeABhpiuEDV%2FclqlEn31pgEiFKIPyyeclFcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPdgB%2FmNVuQbkGD3%2FSrcA9O9i6bjKqqO1Wt6HO4V%2F74sHsMlhrK1VzRg465pSKzuPNgMTT04kHlMYFs9yTGnyXP8mi83UinQoUmOQyqG65XlxEs0DlmdlkH7Hd0fAKWD8LeDMbFTbqWod%2Bx4TAf8rfbf0rc4SKFn7kdF4c93r6zTjd9pAr10BDMqAfxnykG6DKLSVhn6T3O3lHPZI3z83cEIwjHGdNXFHZPWmPGCTtfM5Tfm4nJ6mC8zkkLN25CdShVAXAndIsD4ytvAK%2BvESJHToLkewUeduAE5d2dRH4kQDmNCpnRyOn%2BUxlstvHru2M2bKI5V%2Bie%2FDlvn8luk%2FlGVQ5M1ia3C85RO5f77nMJqz3J0Z0KsQ86htRRPYd5cs5%2BNM3%2BdAbcvWNhvl8Lh4POjJjPDI1s%2FsAr0jdZKs16OfWJhtse%2FqWUZmKf3iXaQCWMuyP92YgRPuM%2BzwwfSmMSWwiiPDZOfW3b8jCSXQlUK9nYPVgUvIbATPC5HO4Pk8dv0DLKFp8auTFjPQe4qYicWI5PKaQxVv7tpWwEnlnvjF2Z0Sw6kSGjvNuzqs7wPzOtOFdm5hqkJe8f2Ph%2FIziuDsf6syztKMCLH9o7RNlYY8O6JKnFHHhTWfaxpF8tOeOIapiiDibVBvpSqMLjNhb0GOqUBjOpcFL6oAuIwaBx28IXUrM1izS3UcCmYwfdVhEXcTby8UOQsdU08xUdemZLqyzQMx%2BrSRJQE2d8XJ1KwM24cyQJhrWs7T3YarUnGkCUiBswJ6sSfbI2QGdJkIqaF4ZIUriN0hWlefbvRqw6a2Qd5mWVcOtoAxdDfVoTr6UQpGA0kJpgtUrFy%2FXaHE52v7TVj7E5WePy3YQH5oblClQaQ31qLGAZO&X-Amz-Signature=5447381ba834844f5cb1c40b0d93a3ffa112c0ab8d0dbd4522d58e83fcb79921&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNUTA2X3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIDd2MjAXjpPjJZqJvr63kJ1BDwdvSoYuisl79IxyhqTKAiEAnFGMo40kIeABhpiuEDV%2FclqlEn31pgEiFKIPyyeclFcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPdgB%2FmNVuQbkGD3%2FSrcA9O9i6bjKqqO1Wt6HO4V%2F74sHsMlhrK1VzRg465pSKzuPNgMTT04kHlMYFs9yTGnyXP8mi83UinQoUmOQyqG65XlxEs0DlmdlkH7Hd0fAKWD8LeDMbFTbqWod%2Bx4TAf8rfbf0rc4SKFn7kdF4c93r6zTjd9pAr10BDMqAfxnykG6DKLSVhn6T3O3lHPZI3z83cEIwjHGdNXFHZPWmPGCTtfM5Tfm4nJ6mC8zkkLN25CdShVAXAndIsD4ytvAK%2BvESJHToLkewUeduAE5d2dRH4kQDmNCpnRyOn%2BUxlstvHru2M2bKI5V%2Bie%2FDlvn8luk%2FlGVQ5M1ia3C85RO5f77nMJqz3J0Z0KsQ86htRRPYd5cs5%2BNM3%2BdAbcvWNhvl8Lh4POjJjPDI1s%2FsAr0jdZKs16OfWJhtse%2FqWUZmKf3iXaQCWMuyP92YgRPuM%2BzwwfSmMSWwiiPDZOfW3b8jCSXQlUK9nYPVgUvIbATPC5HO4Pk8dv0DLKFp8auTFjPQe4qYicWI5PKaQxVv7tpWwEnlnvjF2Z0Sw6kSGjvNuzqs7wPzOtOFdm5hqkJe8f2Ph%2FIziuDsf6syztKMCLH9o7RNlYY8O6JKnFHHhTWfaxpF8tOeOIapiiDibVBvpSqMLjNhb0GOqUBjOpcFL6oAuIwaBx28IXUrM1izS3UcCmYwfdVhEXcTby8UOQsdU08xUdemZLqyzQMx%2BrSRJQE2d8XJ1KwM24cyQJhrWs7T3YarUnGkCUiBswJ6sSfbI2QGdJkIqaF4ZIUriN0hWlefbvRqw6a2Qd5mWVcOtoAxdDfVoTr6UQpGA0kJpgtUrFy%2FXaHE52v7TVj7E5WePy3YQH5oblClQaQ31qLGAZO&X-Amz-Signature=438b34acda998e35254124ef6268a03c4159ed73ecda31a59cfecb82a991e332&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=34f3db7e51fe49ef3072070e137ef56dafd7331b31d4e1ab658180ade0f44a03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=8ed6b32a9e52786ee8f2a20203f029b821f9f122464d7c778c7191280a113151&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=645638025be46d789e01365067f47eefef6f1f30c43f3fa0f6de8c41532f8b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=04e8d60c3df75892117332a627cb09b7d50ef46f30cd3fc80ae25c4fe1f5eac6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=153aa6a3ad9b7639512fa19c65f9542e822f172496711b0e476b52bc246eec94&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEXIXNR7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDhdYSxYkYVvl2z3zLA%2FXi0jPwfFESWxuy%2B8BsJLmoDlAIhAMg9uIfSTGVIpxNPphmmW69WzKGc%2B6iTLBGXUY6RoyRTKv8DCCIQABoMNjM3NDIzMTgzODA1IgzBcOivR6pJmLlWL6Uq3AOwFOtCnPLeP6fmYPudwPAEmOoDahOc0d3CLccLVn2NsW%2B6HgIL5WFoIWHt2JoHaeOovhjFax2FhS9VPBxOmyZFa3HI5pv1XuKpvOw6pFGpozdrDHLqbpjSevwVd7NHP7QMyJJT%2FPGp6HTQeDnBanmRiEjjdkSXFCPFHLtNwdmqTwEDFCnHoQSfuYhVTVFMA%2FSrmf5o010iXhgXbhPsDTVpjWUZYcWz2NUkp665bHQS2F8Ksck7TtKzV5veQYUEvHAj6kJBuD%2BNm%2F6yXwkF8IKHC7NJ9MQFJ%2BukPQIvMxnLrFvjXGEdIjkpxgoVW7S3WXyFZulXTYSDYWdlnv0bfAJyQ4FoTNU54xk4ORb6vt0MbxPxGXYR%2F%2B5U75Vgsf7eFm4NLF%2BM9W86x3cYqqQUQJIm67bgDYXzu02VZQQ8axrHmcNOO5AO8GBxO2uIp9lByPXxz%2Fq8LBJgqBrstZ4gn46B3tgOaaQNJSq34N%2BVmytk3x0o9fuoUGkkIHOi8jc7dT5DhwHUlibrb1nM7WXqmdVR4E06LhRZC5BY3FvQK17OvE8G8fXXkkv2mNJC9X3I%2Bc1ZwjtCsyyhLLa9PxWmzI6eW9koIImBEfNrlbBWRvGKTcL7T1SYSh2JjFA3SjDGzIW9BjqkAb4F4PsRz0910J%2F1wWV1zd%2Fe6T7SbA3TNtB8TXFCUGM%2FbFqjV5osLqy0rTIXzKJoyBtD8EBDX%2BUIVLR6VoF5XPFVwvhw9a0KlFWXqCr2geQvpRIJ1IfwPzKXL%2BCZx9rHIsFcwPx3XrtYq3cz7R%2BZ3so5Vnxr5XIEBadLxaqSFOZlrIuxiF7bHk%2FtPPfZnEOVLpQ%2FxEk7Wr%2BzzpYM6O%2BPqtiQuZcG&X-Amz-Signature=8f41994f546d9c065d003f28ab92467d6297cf584d7e341a7359e41c088becab&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663UEUELS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIE5N7HkXsUw2gROgH4J8aS%2B9CEYz3yDEESzLVLPAdrDGAiAC4U2K1Eq2H7vsHPJhWpkoQuEjKHn1p9WTlG6NrhmN0Cr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMZBYCH0AVJcC%2FOU23KtwDtsqXpV9A9i0HTKwVpCKh3QlIYAYUJWxUKvEGbB2c1lJu%2FOkWYU3%2BrZosWaRTNrmM7aDyEM6MZXiNc0gYyXwu7rTLqdc7K4ctqxPALQDQL4LSGbs%2FZmAhVhvXsJtBTs8TavJ7PwxYdZ4DSU83I%2FhaKnuZi01Rb30SL3kXnYiVfqgsON2%2FvQNSm3Z81l4swrHMFh4ZxQhDvHTp4OiHZfMt5E7iHvfjOTo4nJoMZJ%2FST1JOmt53CKq1fr7t8wMh7CQVGcMFY8VZjKeMa%2BCoaN1xOeL8WKr5maavxq5hVHSktxstHK%2FO1mrwf8DZiRHNGO1IAoBLM9%2BUNG2CKNdCMMf364dAl01VJ2KZNKmaroRKkd%2Fj183gbevHStGsTNDqw6xf5HvjqlRD3roLTfNi59dBmkKwobNT%2F4BmHsoPJx%2Bp4hE4qFSQSVzMMhGE6VH4plGS1NdXLhfDf%2FfXLcgtiwkRVRyvhImuI5RB9%2BmV8t3aRR8P%2BCEb03nzO6JLeKP8xRNsJz2qRsLmNBY9cDfKd42t7waVldgBLcKaoKKxQFtcc%2BlpSbt%2F3JZWK5uJCr4Bh8SgoIavTjaQf6uPVQdKS0DHyQ%2FLG2D7oi9DdfhsUgozsEIRn7rCfNZsGCUg%2FcEwxsyFvQY6pgE8wjENAZBlweiLfRJdN9S4eKb3sLNnspgLoKcgh7ZI9%2BhfehBxnELqXDAQr8D9%2B%2BPc%2Bk%2F00pz4GBYOZOLTyXtX53e01a2T9BsAFxkh7lRKXZ9N04tIAAJL2FHc0i98ej1OZn6spjulFGrTibPeKkQGKuVSXLv%2FYE4tw1fX54A95Q6mJ4G9FDXz5AkJzxUJRVoJDKdeand4xpCOC8X%2Bzl1cmq37o9MV&X-Amz-Signature=0c6ce11dea6aeca50769f7b0303cee8b0492a84057527ca91338cd42d4c4bb4a&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663UEUELS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIE5N7HkXsUw2gROgH4J8aS%2B9CEYz3yDEESzLVLPAdrDGAiAC4U2K1Eq2H7vsHPJhWpkoQuEjKHn1p9WTlG6NrhmN0Cr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMZBYCH0AVJcC%2FOU23KtwDtsqXpV9A9i0HTKwVpCKh3QlIYAYUJWxUKvEGbB2c1lJu%2FOkWYU3%2BrZosWaRTNrmM7aDyEM6MZXiNc0gYyXwu7rTLqdc7K4ctqxPALQDQL4LSGbs%2FZmAhVhvXsJtBTs8TavJ7PwxYdZ4DSU83I%2FhaKnuZi01Rb30SL3kXnYiVfqgsON2%2FvQNSm3Z81l4swrHMFh4ZxQhDvHTp4OiHZfMt5E7iHvfjOTo4nJoMZJ%2FST1JOmt53CKq1fr7t8wMh7CQVGcMFY8VZjKeMa%2BCoaN1xOeL8WKr5maavxq5hVHSktxstHK%2FO1mrwf8DZiRHNGO1IAoBLM9%2BUNG2CKNdCMMf364dAl01VJ2KZNKmaroRKkd%2Fj183gbevHStGsTNDqw6xf5HvjqlRD3roLTfNi59dBmkKwobNT%2F4BmHsoPJx%2Bp4hE4qFSQSVzMMhGE6VH4plGS1NdXLhfDf%2FfXLcgtiwkRVRyvhImuI5RB9%2BmV8t3aRR8P%2BCEb03nzO6JLeKP8xRNsJz2qRsLmNBY9cDfKd42t7waVldgBLcKaoKKxQFtcc%2BlpSbt%2F3JZWK5uJCr4Bh8SgoIavTjaQf6uPVQdKS0DHyQ%2FLG2D7oi9DdfhsUgozsEIRn7rCfNZsGCUg%2FcEwxsyFvQY6pgE8wjENAZBlweiLfRJdN9S4eKb3sLNnspgLoKcgh7ZI9%2BhfehBxnELqXDAQr8D9%2B%2BPc%2Bk%2F00pz4GBYOZOLTyXtX53e01a2T9BsAFxkh7lRKXZ9N04tIAAJL2FHc0i98ej1OZn6spjulFGrTibPeKkQGKuVSXLv%2FYE4tw1fX54A95Q6mJ4G9FDXz5AkJzxUJRVoJDKdeand4xpCOC8X%2Bzl1cmq37o9MV&X-Amz-Signature=7aec249d9c6e0f331be6d0eddc46c13fe7cdd655382a8f869372657b3e0c0cae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LYD56P2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIAoDxSrk4JygNiFsf5cIPBFa9f27%2BhpMCuS12ShvbIFdAiEA%2BHA%2BRng%2BOZ%2FO1MfDoI06K9baSNL6R3MZFSiRbbn8V7Iq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDJuKqqnRRxaxGQ8lKSrcA2ptHdU0z01iBx52h%2BMDnbr%2FOxEaP3d7IWDv7iAnl8%2B6gxU842KoYHKRC%2F91plmrYSAaDoz59cDT7du7OHDuPrNwWfKySZx4RFhhUtJ4cIRRrrWkLDZAvj%2BPTPRC4sfmsrqef%2FrMXURZJ8QSxLQdhD61UNMxNyl%2Fxpl39VN8keHzDXDnq1i%2BFGEBjDRg8f3QfCvvMNjQ3sbNoijtXUVKWhKrUtghzopP5jQd8g7v%2Fr%2BA0iHdZL%2BowFE%2BxnR3Tgy62ODBVibC13qeWvelE6BI6UOwWMyuyTnuqm%2BfWhtMXFwO0dzoCUzdiTIAWNUsBjp7zpPvMJoxbo%2BuAAGdohNvLeM3FfV0kn7U%2B5NNx%2FEHL18JJ87FmuHn%2BnrydXmysV5IMMhlUbr0ZNV9n7hAieYzWPTg7C3q%2FxRwRQPO87TDO6owy5U7SGx%2FvCCmemMCo%2FZ2iGBixbkCkljmX7AIoINNC6CptYMcyKJ3NrQtUQODVpRGwrHoRTNNbuPPm4rJtExackY4cHfpTn3Vq4AueQBvf8q1usNtnXdNKpwEPXsYco3kNctUo%2BhgEKVKnd5TZvZQE6vVFL9%2BSpQEShk0olId%2B1hFwvV5ukmVkuBS2fRcI5nqA8pP9JEdp%2Fm6sqVRMPvMhb0GOqUBjygX03QADmfPSR%2F6MMbvtzJXmaAiwC%2FN6c2ENMeyuqxYaK4453aZEWqcAOZfJLUsjPO3RZQ7U14zQbtQxxtshD53zlGqZCX8bCv9g2PtDF%2FWN5IXXRTTC7etw7tpf1YgAoN5aM6K%2BRN2XVf74%2F68JLBLUbly%2F5ZcDuGYLIC%2FXNrRHTr43%2FXeVMVFe%2FS41DeJCq%2FIadMCm4mt6q5nPdqkDbwDnkWY&X-Amz-Signature=2711a479acabf26c67214eb2fc91798c883ceaed45dc261f7fe969a1abfd015e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSA6VEQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCzdoG49V%2B2OwDRPD3twll2Kxr%2BzjrJU6BceBAINmZwZwIhAL4dPQ1yUxMIarNxdvBSBdnMDp%2BXqW2sETYNUpu2kUvjKv8DCCIQABoMNjM3NDIzMTgzODA1IgyGtVrpD8RdC%2FJsdw8q3APXPKco%2BJd6jTZJ1NLE7Yx4legnFWpneAkTewHibPOiInH8jL%2FkC6rB75yM87bVZD%2FhxdSrLtn5%2BGLT43MBOMxE79lFlkhud5aakHL2L4Ogm1Aao9EGDtvMlHkH5x1zRBNx5Ipfv4NpXIj8t9Y1WQjnnWoQ1bEP95qXHETq6BDy%2Fyv%2F1WvgrzIk9fUaJ9aQ28%2Bwmt63aY9M0844KVQ%2B%2B30Laohl6XuJwsTJMA5S8VkoO4ADI2aVu1goTc9xLGsj2RBpmSUnQem58AZX729XES8mexwgRLvLC8kukIwK9bfQ7N2YdpSPeYxXnhoE0vjCYhVPAt0my8l70BERlWjVBWFhB2zmUXmlvCOn%2FCDAPMvOo9%2FTICTOqC%2BSzA3ft1AMLPQm8mn%2BrKNGEGAp8s0rlD72D2ffoV2KnvGCcyBj4ag02cPH7w%2FbCVyrEMByncAtf3aQ%2FPNwmzUwP7zg2qf5%2BwdhWcN9r%2F888BVd5HTAF%2Bx7Lmu2MwEQt2ByuTSo%2F67Ex6dpN2sSnGwL%2FOkwSZijdjiV1pT1H3lttalw4ugjHrwDXndO5MoHYMLKOCeUtgEj5N8Toku4lUXrOV2tqreHVCEXRxD6bKAkLfhUVmhJuWQ0SGGJGubzbCr%2Bwba%2FnTCQzYW9BjqkAfDf9cT7IzirLHi7vwP69Ms2VhXqqyPEpUqYYGTnVF4oOt8vbqtNBt07q%2B5zzZ2JUCYoS1sNerg8bz%2BGVKEJFXR9b9Ea%2FUC%2BaHE5roVTBRuzSU9JLEiEZ9UJ6YfmCOU6pEhZ3%2B0SsgSzJD9IOvCKhRAVpN%2F%2BhO14TcPMD20ECe2ky4v9mvYd9LtV4ij9SDfD6RpqK%2FL8V69CEr%2BPtv%2F3su83Kd9k&X-Amz-Signature=48b39f519e3091768f954ed5f0869aa6493adc20d3f62ea93b63d16398faa081&X-Amz-SignedHeaders=host&x-id=GetObject)
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