

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=c97a9f715c09a0fee8f8d4c5e37610d221a2988c813dc124bacfde8b8f06757a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=788ac0be6564315471ec2d24967f7acc379974dd36c66f16692780381e25f8c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=99dc6a32d629e7cc8581303fb688be2e833e989b201f6395f954ecf5c0e38a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=ae8a3c1f06055eab84faeb94ad55d1e1de768e3dedac986e7244eca63b78e591&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=4faf918d670fec0b8602393c2763d65f74c16e3e290ef06c5103a52629a5c780&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=4eac44086c2621d5dd53417f16788ba3c08e9e8c4bcfce8d710f2344c06b39d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=e3065968ba141ec0c0b93caa48c711d47ac72f2b05a97c20ac55c72fdfcada72&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=2494a31ebbeba4bff7458de56f9e848f6fe4fe0406f421566e2dfbc04f280e03&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=804666b53ca1e18032454562e92250c8f1b932cb97ee28513e363e7904bbb94a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BFU6BUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvhK%2FEJnqyqXypDIzDs3OJ7mqXLJEDfeAS9f0XFFW9awIhAIAVimVXbtK0jtyJSmQU6BX79xHbZaj0cA3o304NlVY4KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BLt29PsTu4apKmAq3AO6p6lUgAIWDZt1u2Bce20xWmzb0AnXldXMF215lSnWqhOWotJWsUq5xEggZ5MJWplHTvzKjqOC3xRVjraQdS2p6VzhTwWke%2Bxd5xZCXqOXv%2FsliiqFUlE3VcpUm%2FJz7upiAhoJVkJe7vuc45skpYwUOmsRSnQwpEpkvw6K4iTW%2B4ZGay0HuWGfDRlETsBzyuxluvpRxszHJ9nCcGEQcuplaf4iyWG%2F5zDg4uw%2BF12Ejilwqv68U6wVEwBPfA29YJCGilug5QWbAvSGSrIIvdO3pCb%2BM1RxPsXGh%2F7GEOzOO%2Bx8%2FoqAXEcem39kSsgv2tGBF9FtdZmXBx%2FA1pp6WlI6Ono0YCE5N%2BZyJppzGNshrE0UySkQV2o37Bxm8RBjCmss4MuE0805mf06VNZ%2BuTxbCPI6qeLmFj406Wbw46OQ9M%2F04jBAFDGAOR6MEjDNsl7yNNisYZcH%2F%2Fy7x4FOXt8CJ%2FOXZXzXJBppUKELYtz%2BwjT7Upz5GxodZuFk1oTqnWQ8RQUNaH%2FY6oSl2B5g3HvIi81zLEdbqjP9bAon9UvBGlZhNwJ2tgIEuwOYBSq1D4rqZCKR9mbnEcNs%2FgB1ohOrYOAHn8D%2BLM8G0REfrdc6FJ8Xkf5%2BvnhkB32McTDl8fq8BjqkAVPo7REFeDNg3xengxDsxVkuh2seFzHkj%2FXSwAW%2F1eB4NQA3Zs4OjJS%2BMaDSN8XUAeljPOHCM3aVlTmFrRKNXop8wVXjiRCPImP2lCchvlKTQKkTAL12S0HXCA2kGM%2B69dOp52UntEcVgMdu8GnO15S7%2FOLEArHmwu%2FMzW0hyno0QPtJEbmReKATI%2FsaMqlVtNQL3tcBhc6cprmLiuXhUsGtQEJG&X-Amz-Signature=76d7e7f03de1b47dfea7012b6d780fda274cd9c4f1817d193eef4114d1a9e38f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BFU6BUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvhK%2FEJnqyqXypDIzDs3OJ7mqXLJEDfeAS9f0XFFW9awIhAIAVimVXbtK0jtyJSmQU6BX79xHbZaj0cA3o304NlVY4KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BLt29PsTu4apKmAq3AO6p6lUgAIWDZt1u2Bce20xWmzb0AnXldXMF215lSnWqhOWotJWsUq5xEggZ5MJWplHTvzKjqOC3xRVjraQdS2p6VzhTwWke%2Bxd5xZCXqOXv%2FsliiqFUlE3VcpUm%2FJz7upiAhoJVkJe7vuc45skpYwUOmsRSnQwpEpkvw6K4iTW%2B4ZGay0HuWGfDRlETsBzyuxluvpRxszHJ9nCcGEQcuplaf4iyWG%2F5zDg4uw%2BF12Ejilwqv68U6wVEwBPfA29YJCGilug5QWbAvSGSrIIvdO3pCb%2BM1RxPsXGh%2F7GEOzOO%2Bx8%2FoqAXEcem39kSsgv2tGBF9FtdZmXBx%2FA1pp6WlI6Ono0YCE5N%2BZyJppzGNshrE0UySkQV2o37Bxm8RBjCmss4MuE0805mf06VNZ%2BuTxbCPI6qeLmFj406Wbw46OQ9M%2F04jBAFDGAOR6MEjDNsl7yNNisYZcH%2F%2Fy7x4FOXt8CJ%2FOXZXzXJBppUKELYtz%2BwjT7Upz5GxodZuFk1oTqnWQ8RQUNaH%2FY6oSl2B5g3HvIi81zLEdbqjP9bAon9UvBGlZhNwJ2tgIEuwOYBSq1D4rqZCKR9mbnEcNs%2FgB1ohOrYOAHn8D%2BLM8G0REfrdc6FJ8Xkf5%2BvnhkB32McTDl8fq8BjqkAVPo7REFeDNg3xengxDsxVkuh2seFzHkj%2FXSwAW%2F1eB4NQA3Zs4OjJS%2BMaDSN8XUAeljPOHCM3aVlTmFrRKNXop8wVXjiRCPImP2lCchvlKTQKkTAL12S0HXCA2kGM%2B69dOp52UntEcVgMdu8GnO15S7%2FOLEArHmwu%2FMzW0hyno0QPtJEbmReKATI%2FsaMqlVtNQL3tcBhc6cprmLiuXhUsGtQEJG&X-Amz-Signature=218f110b0355ebaea9413119fd6e33c3e24b64e560f029a4beeafa3fbabc8be0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BFU6BUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvhK%2FEJnqyqXypDIzDs3OJ7mqXLJEDfeAS9f0XFFW9awIhAIAVimVXbtK0jtyJSmQU6BX79xHbZaj0cA3o304NlVY4KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BLt29PsTu4apKmAq3AO6p6lUgAIWDZt1u2Bce20xWmzb0AnXldXMF215lSnWqhOWotJWsUq5xEggZ5MJWplHTvzKjqOC3xRVjraQdS2p6VzhTwWke%2Bxd5xZCXqOXv%2FsliiqFUlE3VcpUm%2FJz7upiAhoJVkJe7vuc45skpYwUOmsRSnQwpEpkvw6K4iTW%2B4ZGay0HuWGfDRlETsBzyuxluvpRxszHJ9nCcGEQcuplaf4iyWG%2F5zDg4uw%2BF12Ejilwqv68U6wVEwBPfA29YJCGilug5QWbAvSGSrIIvdO3pCb%2BM1RxPsXGh%2F7GEOzOO%2Bx8%2FoqAXEcem39kSsgv2tGBF9FtdZmXBx%2FA1pp6WlI6Ono0YCE5N%2BZyJppzGNshrE0UySkQV2o37Bxm8RBjCmss4MuE0805mf06VNZ%2BuTxbCPI6qeLmFj406Wbw46OQ9M%2F04jBAFDGAOR6MEjDNsl7yNNisYZcH%2F%2Fy7x4FOXt8CJ%2FOXZXzXJBppUKELYtz%2BwjT7Upz5GxodZuFk1oTqnWQ8RQUNaH%2FY6oSl2B5g3HvIi81zLEdbqjP9bAon9UvBGlZhNwJ2tgIEuwOYBSq1D4rqZCKR9mbnEcNs%2FgB1ohOrYOAHn8D%2BLM8G0REfrdc6FJ8Xkf5%2BvnhkB32McTDl8fq8BjqkAVPo7REFeDNg3xengxDsxVkuh2seFzHkj%2FXSwAW%2F1eB4NQA3Zs4OjJS%2BMaDSN8XUAeljPOHCM3aVlTmFrRKNXop8wVXjiRCPImP2lCchvlKTQKkTAL12S0HXCA2kGM%2B69dOp52UntEcVgMdu8GnO15S7%2FOLEArHmwu%2FMzW0hyno0QPtJEbmReKATI%2FsaMqlVtNQL3tcBhc6cprmLiuXhUsGtQEJG&X-Amz-Signature=4163aa30fb1c3b71de4269ca32a32a01d43aa9c60550e3c718a7fd67f5aa42f6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=503bdeae263427582079115f069f4b110fefc94fbf2d71cf3c8abf1237f63169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=fc3ef9bb92a85c942c9c842b5134bf76fc5bcb53ba5f8951d1152153f7df7fba&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=522f1c78826ac626bc1ebf9a7d2ab2c67baab309693f83088012892e7817bf86&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=3825ce67e5e4d0e150efc1b4f1c73318efc90d86b7eb9a5522d8d17e5e184ed9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=1ffa62a9ef44d6058ab150658a629563a82b7b9466c636add23b1d941934d354&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RJ6DUVW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE5OCeZvhg68q2QPtxDt6M2YvnacujXQ2QZxR8JDFYBOAiEAk24pedhDqIrMk%2BrGIDeQm1N%2FuZG17bXywR%2FU52T68JoqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFMEJ%2FImPIVxZjwc4SrcA2YhZ3wAX0Pg4X5FS%2BQpoiAE6W%2BfI3wf%2FPc7pdLZQ9s7dxw17E%2BEeFJrUisMnUaaon7hjXJQHdB3IrQQbuLvL586%2BCC2NVMeQCMtlt%2FluXBQxJBVCNFJP9ZDK6Ix%2FDk6WtXkwKw%2B0aoexagXbnntBeqQSKMEd0Ooxg6BiFZAgSuzjNcIMyictaqS4ouwbn8mBkZuTNF6Xxfmq1sBy1ZtIreMInhavCY45oBX2NFo8XhFCTzDgaFP1%2FxG9d7u4LqZuML6YDvPQFTMgFxg7Xx19Y0HIV0Ye8VGR%2BvWs%2FU%2B3iJnxyQrCHH0XYR5E32qAaPsHwEL0fxZ8fL%2FIEpHd1JM3Pw3XxQusmM9MXw1XNDhO5qIGAmGa7TszUlDfuOEMlvRSbxs7WqPcoDfwPIV3xZZY62FGG9mIaMBmx4hiGj%2Fd%2FcwRySUyo5pMojAOpB2ZLpq7RIkouSnZ4V3cAxezI10a9tKMB9p6Z7ZBRGlPLhPQbIVSlXgjrOgdCD0R4zpi2F72JJz92tbIfNZgiJC3Phy3IcgqSgw7IWgQF4RB096GbTul4mb7ShGXcKFrPwYQOMUA9JDMK%2FWNkNif%2BD9OS%2F2qSvZqOAW1q5VQFvaoQ22bBeL34JtFrOrdvXfQDKgMLnx%2BrwGOqUBnVMvgf9rFDw2vcoD%2B6260YU3aM5Nd0NAuvYWHfktcQE7M84xBBgJM8nvUg5qQ6f5aqM9d%2BNuouWJZquV2VuwE8rQtpieScVRSW0E8hYeYqgASFHM1RPwSFpCeR5SG32evjUmAAwWTgP1GgDauQrOZC7PhNXYpWIECaW2kRupqq0KIZOacgFERkH%2FyKM%2FGzVy3QPaLN5YQkrhxEizkd%2FQKmEy1WfO&X-Amz-Signature=e4e11e83cd7319742ef3086152e2c3b230161245ec5d9e37f4a485a9cfdb11e3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EGOWHOI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2B2djKeWAcqvazASCbCLl7StnqBqUOxOTW4DfD87KkrAiBWHpwS3kdFEFS2L36LrieGksHEyf4PJagx%2B1PU70V66SqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQpGl0CxoBRUe6qssKtwDvbsztDtjP3m0yeX8UtCbsOmtKXX4iTE9XWZtJC%2FQh7zwstk9AvM67IXjav1daGTAzljx4lzhM04ObEh8x%2FlQQcW3z0cECjA20rn%2FhXoe45Q%2F6LDTvmSXQzgUM27CHTSY%2Fm8hEmf4jY4iFYxgPk3NC9sw1oMrj7oofM1fsve%2B1BNrZTGsh4qD5OyOf9gufu65DXvdQBSBH8TaTkGLeQ7mOzc2%2BFTZxxKem7Vg9lU4MRPJ%2BETFAXCdqUHdK9NmUIesasA85HaoFuUgmQ34fjSxwY2S9DmYS%2BYr4mk5He7NCtDCq1dDdh5pTiXSSOS8fDp%2FDAcTWjW1Kq09ssJTugq0nT7AHs6lxHxIQwaMeONZEq0XWG5u58fqbS4BbVy3oGEOEJXElWxH71wYSsrbauJPKFURzunKPYqmEA0SHr%2FpZeSMdZBrfFg%2Fp6GMIC1V9M7qmxkTc1CFsPTf%2FMPKqR2BTgn60OidwUziJzG6VD44uCZagU5q6tf%2FxAaBYlusWJQ44Z94efJUFG8vB%2F93ZCUoOJ0Skh0fxDVEFsDBmDtP1UCy3NKyVUQgfxXDZLh2YxBJiezK86cu45ae4dbDAgulg7ZdXjPIURnNb8%2BXWchpews2QB%2FftDGMDr9iZ4ww2vH6vAY6pgE2RtWn7uAjkYRvsvIKDRuCNMKfXauVXM7irXXD%2BbBluZSDzVGxbAktJoPcVT0twrFf9PwzOQ6iSGHs0RPzlsnN1852nI9VSmA2rns3ohk92Q%2Fk804NNWM8BzHaGeGiR0zk9hJn2Evz%2B0UHs36HnKa%2BXsisosZrG3USRajk1hp%2BGmPs0eSlF9WPjbEs8ql3FpYtgoGyd6QTywPgkqJvcMA11gZaCpL5&X-Amz-Signature=a1ebfcccb09117479c00d6ecf28711c4026af99a31cd6db57d57003ae704b5a8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EGOWHOI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2B2djKeWAcqvazASCbCLl7StnqBqUOxOTW4DfD87KkrAiBWHpwS3kdFEFS2L36LrieGksHEyf4PJagx%2B1PU70V66SqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQpGl0CxoBRUe6qssKtwDvbsztDtjP3m0yeX8UtCbsOmtKXX4iTE9XWZtJC%2FQh7zwstk9AvM67IXjav1daGTAzljx4lzhM04ObEh8x%2FlQQcW3z0cECjA20rn%2FhXoe45Q%2F6LDTvmSXQzgUM27CHTSY%2Fm8hEmf4jY4iFYxgPk3NC9sw1oMrj7oofM1fsve%2B1BNrZTGsh4qD5OyOf9gufu65DXvdQBSBH8TaTkGLeQ7mOzc2%2BFTZxxKem7Vg9lU4MRPJ%2BETFAXCdqUHdK9NmUIesasA85HaoFuUgmQ34fjSxwY2S9DmYS%2BYr4mk5He7NCtDCq1dDdh5pTiXSSOS8fDp%2FDAcTWjW1Kq09ssJTugq0nT7AHs6lxHxIQwaMeONZEq0XWG5u58fqbS4BbVy3oGEOEJXElWxH71wYSsrbauJPKFURzunKPYqmEA0SHr%2FpZeSMdZBrfFg%2Fp6GMIC1V9M7qmxkTc1CFsPTf%2FMPKqR2BTgn60OidwUziJzG6VD44uCZagU5q6tf%2FxAaBYlusWJQ44Z94efJUFG8vB%2F93ZCUoOJ0Skh0fxDVEFsDBmDtP1UCy3NKyVUQgfxXDZLh2YxBJiezK86cu45ae4dbDAgulg7ZdXjPIURnNb8%2BXWchpews2QB%2FftDGMDr9iZ4ww2vH6vAY6pgE2RtWn7uAjkYRvsvIKDRuCNMKfXauVXM7irXXD%2BbBluZSDzVGxbAktJoPcVT0twrFf9PwzOQ6iSGHs0RPzlsnN1852nI9VSmA2rns3ohk92Q%2Fk804NNWM8BzHaGeGiR0zk9hJn2Evz%2B0UHs36HnKa%2BXsisosZrG3USRajk1hp%2BGmPs0eSlF9WPjbEs8ql3FpYtgoGyd6QTywPgkqJvcMA11gZaCpL5&X-Amz-Signature=02f994a35d53e1b8c9018e07614c612d42e79aeaecf39471987541dd6c06b254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VMS4XY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDK3%2BUJ3bZR6glgFgy8BjPhPeBCqaVzD7md2gF%2BNFqQ2AiATjz2KFACHyUbkDU5Eo7qKPI7HzyV9vOdv2SCwd0N%2FDiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcI%2Fx3KtnLdaK%2B1BFKtwDFapignCvy9uCCAf4GczUZb6tfCVD%2F2AnEGi6FGVq%2BEhf6FVFeQScyrteZIZp1E9Ov9uptM%2F0MtFVtsbXCzW7nQDf%2FGd9wKJqiCX7AsiZAqlRF0lCIUWxEdBsFxfgK31G4NvkyV%2F%2BrhpxcgjkcC%2Fq2NrLRaNT6fhKL4rESe5I7q%2B5%2BOc2Cfb6AOSSvlT0kiimjOBEQsbtqFJTfHvQ6avuJ9tk8QXDl3ufIS%2Buv%2FVGspTqaliGfbcUAtNQHraUmt%2F22GV5U%2BpD7i2XyUhs6Pb58uGauwc61D0H0NoAjzELVksHJQd9xJlaUI9zlGJws6jNUgTXn1wHksvNE3kZcvxGkcVvNauQSNy4urEcCvhLg0n9KTu2a5Ox7f4QxL%2BzJU5Y5VQQbKAAlhaYllDgKkVGFLVzseeIFt8vq2EPcD7xUHL92A9L2a2jhecWIfrErmvW8z%2BSFjHU3ci43pn%2Fjf4EyoxU%2FD4INrTE6KUhqUfm3SJwX%2BHPIEoHHkyOM0J%2FVy8vWIj0wQxshf9%2BhxELMWIv%2BAyXwdLrBsISsMwIR9Cza9ffk6PaD4ZS1mMmHz%2Bj3HoSFn318%2FoNxyIDX%2F4NawhVWc2NPW6xprPt4CaCLFGmNKEi7FGML9mQiLeJm0cwlPL6vAY6pgEgVexR0heyyzr6B9dAwQH7yf3IWvs5SpghVjbNvIC%2FzYuVoltHgFwnSkp5vD9HXL%2FpQcp7x7JMBYNLeDM9rkc27ZOh442efJYsHvZTCSi6e8fJ57cOl2bAnqrNMpfqtV2OSbGx9FYq0iN553WRO319s8RU9vSw0bVYs8kp27duwFdtFLQSE%2F8v%2F6LMVuP2LPBRFWsUyurHdskTt85ifinEZGPCrV2o&X-Amz-Signature=a864601ebe0bedf0c425fc2b10f5b13974f24687abfe2d72d291fbd646ce1e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KJ2JZZY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc786lsp9k0tpv6PEZGaccRDaxf8qhgvbIMAZ%2Bc5AG%2BwIhAITi5aFrVLmL5qjtcAbNJFUd8ps2tvkTi0YgcBquYIsmKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz9FkgUzBkskTB2MUq3AOHM1yJwh1%2Bfamf8jslAFKhlab6IO6fgdDEi%2BTNwRFNfF0Z5mJ94da4%2BlhLBNBN9tX1ZbmuwQGxnD%2FVQCbDJirutnhLH5b0e2AR1%2FLIcvn7MlW0ZewD9zEyWDp2M3eggA3rNXPin8E%2FeeygE6l7kyUnCAyGxu4mHlxuv0xx5Wl5Uk%2FG62pKJ5Sg5%2FpCqr0cBf2dubtzVUlUHbfgw75lXQPPdTOKUVDO1RMtEQgM3IFb49X%2FajSb91DkmIWTru5DBSBKLbK%2BwRrgm0gmsRjdMVmkokgeCG3hSDCyXJ52t0aCshjsxrcKWzlffyrqsvWTnrf53iBv8uULr1HVD5b99jF%2FKUiIl8WWPVXSltdJxQ7J58SZjQBaGG1onRDmjH9o01IK4UuyYeCXgGe9kb9zrKzh6NFlmIowTVGOg%2Bf2f2mI0YScVgzEEpZVuDppVfly7mRl1RxJqCvJETPpOFNdY4ewH2Lm02MduKDKkyGrq0hOsalZFhxDfPMQ5K52pL01%2FPN3wR34RYAxt6AJIUjV9wLDx27J257GV%2B82EDYTT8j3eM9yXkAcH3r%2FOTsCpsuSamow2UfIBZbrThXsQyxmwvHCpQg2pVoRSCCCjQP21ZpoTpob3CKdLJ%2BcVu%2Bw1jDO8fq8BjqkARnfJHkFiowY1aQPvUN4gBI4WpQ9pgx%2Fh023GA5biWk4vAXDrlPrYTKgo8nesRryL45eTAvGP071Jc0PqRokajw4RWA23CerCaBpEXlwFGO3qeAa5HENgJ7x9%2Bznq5%2FkNLVdf9vzamfsb1k5%2BE8VTkIqmdZJADUei%2FAsCZB8OtmM63rWmYVwIhrxdP6JqpfLKvQslIuvXEsEab27Mnr0Os0q8Hdv&X-Amz-Signature=329f7b7988907d94d2a57a37a3e067527e4dba8f5d6a761ea1d01d183ace9a9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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