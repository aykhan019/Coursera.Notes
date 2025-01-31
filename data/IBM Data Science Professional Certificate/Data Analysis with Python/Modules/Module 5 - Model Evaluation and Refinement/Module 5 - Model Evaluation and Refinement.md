

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=e7715250bb7d864ff6a8c1a4a526200604786be121e2bb26e523fb3a632e8c23&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=1db7278fe136cd6bc55f17458471b48c2793f514163818efacde8b74f5a6468e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=c66cfcd3d5fb4133c0c88f2b5868630e8d14ec1a8dd554a536b8555cc9e12ff4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=c243fc3022745c12d7d9d18dc41c6e449a5495424567b527d89dda3f08e66b97&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=c2527cd733eefa97a80044dfce3cb7822b09fb382885bd59ea7802d5f903d149&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=05db74de5b3f567e072ef35a38279cf6338bf110903c04d241f508b4ed7ea3a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=841b8571c4e77da405e3a753d03929f05e75af5cfaafe3bd826ec9083accea5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=86a0aa1688abc50bbf2d69f7ac665084b992c64924417ccd6eb25a46c72f0196&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=d9ec11756d61db7b9c5bc711f239b39780b2c6b71432bfd1fa1aa00ddda12db1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE7MRSMZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Adz1pNyeSZgretN4x6%2BAnv8KlyM40yaR1A9Zx6l4dQIhAO1JL5nKoeKjfYNj5FoMxTjc61U7edTxqm3cMf3NYrJjKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQg%2BhMpyfIieJk9XEq3APQJItbfYXhFFhFNCJRD2ze68cRHqZBdeC5kGlsy%2Fxkg3mTuY2ZKjoGGBrRlKJEnsA%2BPWRDmlbzEkZgD3nI6By6dEDtCEc%2FpruQHn2nXXmWsxSYyIKQKSpX7%2BQ%2BWeeB4h8lepuaECWR4MOzPoBhg7R1wIpzhkXU4UmLmtZFBfGlUIXOOdxFB%2Fh9CkMLl7anIzFUDoUzqLD%2B%2BjpibnhTfxDvHi2NSeq23YQjM1b7z7527GTrmlIISuX3z4Gx2%2FZUATLvrhTGENvI%2FGEHp%2FyFqMgZXB5YJ6UEWslSoZ2YGR2Q%2BKpcPp0Rqp691uBNON1ZJQyrUeFszlN7pYm3xpfhVFtWGAJGkPbAUMYuWAJzABn%2Fcm6SjdYPqafaJ1knJEniLofspPpIxTyoUgbrMcq2SXGekKmubVhydXvq%2BIZ%2Bl3qz6csh%2FNRbd%2FkSI32j90I0XTr2G2ZbAGeax17KNp2gVL4dVGK8BDqZYjIVbol37tDGPthvwy9Z4f3tNd8iihqMlkETZlL4PdCqjm5L7Xk0B%2BTH7Vcku%2FHCLag2eb%2BEnirb4DPX8gLXIgoIt7z1PHrx4JG6QaWl4BjzRFzLP5sWNLALOYKrBuOhBnyTGbN%2BwZofTRXPCH3bWmws7qOxqzDLyPO8BjqkAZTYY2Cbx%2BvV5KaYWlBccTxOeAqid64TyzV87ykqlRqW22knOQWajsPgB%2FY8RJtfyphtW7J63n1cQHzA%2B6Y7wZ9PoYYBQZMvo1lUDwh7i6fDpSaC0CRtAM3VCxF1aDCWWfl3zet3uY62torZE1YnpSmtdJ4eS1fDt9zFA6xeucMEQjakFiML5LyHZlP223w3T1YcgpZ%2FitEvy3XIrgexqh38wQRa&X-Amz-Signature=76fe754466f97c273e4e542ccee925a378117b19d469dd70598c8f85ca2c05d7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE7MRSMZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Adz1pNyeSZgretN4x6%2BAnv8KlyM40yaR1A9Zx6l4dQIhAO1JL5nKoeKjfYNj5FoMxTjc61U7edTxqm3cMf3NYrJjKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQg%2BhMpyfIieJk9XEq3APQJItbfYXhFFhFNCJRD2ze68cRHqZBdeC5kGlsy%2Fxkg3mTuY2ZKjoGGBrRlKJEnsA%2BPWRDmlbzEkZgD3nI6By6dEDtCEc%2FpruQHn2nXXmWsxSYyIKQKSpX7%2BQ%2BWeeB4h8lepuaECWR4MOzPoBhg7R1wIpzhkXU4UmLmtZFBfGlUIXOOdxFB%2Fh9CkMLl7anIzFUDoUzqLD%2B%2BjpibnhTfxDvHi2NSeq23YQjM1b7z7527GTrmlIISuX3z4Gx2%2FZUATLvrhTGENvI%2FGEHp%2FyFqMgZXB5YJ6UEWslSoZ2YGR2Q%2BKpcPp0Rqp691uBNON1ZJQyrUeFszlN7pYm3xpfhVFtWGAJGkPbAUMYuWAJzABn%2Fcm6SjdYPqafaJ1knJEniLofspPpIxTyoUgbrMcq2SXGekKmubVhydXvq%2BIZ%2Bl3qz6csh%2FNRbd%2FkSI32j90I0XTr2G2ZbAGeax17KNp2gVL4dVGK8BDqZYjIVbol37tDGPthvwy9Z4f3tNd8iihqMlkETZlL4PdCqjm5L7Xk0B%2BTH7Vcku%2FHCLag2eb%2BEnirb4DPX8gLXIgoIt7z1PHrx4JG6QaWl4BjzRFzLP5sWNLALOYKrBuOhBnyTGbN%2BwZofTRXPCH3bWmws7qOxqzDLyPO8BjqkAZTYY2Cbx%2BvV5KaYWlBccTxOeAqid64TyzV87ykqlRqW22knOQWajsPgB%2FY8RJtfyphtW7J63n1cQHzA%2B6Y7wZ9PoYYBQZMvo1lUDwh7i6fDpSaC0CRtAM3VCxF1aDCWWfl3zet3uY62torZE1YnpSmtdJ4eS1fDt9zFA6xeucMEQjakFiML5LyHZlP223w3T1YcgpZ%2FitEvy3XIrgexqh38wQRa&X-Amz-Signature=9065bf370d3d0088c955b0a837e86628ec64d3e0a59e32eaf89e2d148b7459e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE7MRSMZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Adz1pNyeSZgretN4x6%2BAnv8KlyM40yaR1A9Zx6l4dQIhAO1JL5nKoeKjfYNj5FoMxTjc61U7edTxqm3cMf3NYrJjKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQg%2BhMpyfIieJk9XEq3APQJItbfYXhFFhFNCJRD2ze68cRHqZBdeC5kGlsy%2Fxkg3mTuY2ZKjoGGBrRlKJEnsA%2BPWRDmlbzEkZgD3nI6By6dEDtCEc%2FpruQHn2nXXmWsxSYyIKQKSpX7%2BQ%2BWeeB4h8lepuaECWR4MOzPoBhg7R1wIpzhkXU4UmLmtZFBfGlUIXOOdxFB%2Fh9CkMLl7anIzFUDoUzqLD%2B%2BjpibnhTfxDvHi2NSeq23YQjM1b7z7527GTrmlIISuX3z4Gx2%2FZUATLvrhTGENvI%2FGEHp%2FyFqMgZXB5YJ6UEWslSoZ2YGR2Q%2BKpcPp0Rqp691uBNON1ZJQyrUeFszlN7pYm3xpfhVFtWGAJGkPbAUMYuWAJzABn%2Fcm6SjdYPqafaJ1knJEniLofspPpIxTyoUgbrMcq2SXGekKmubVhydXvq%2BIZ%2Bl3qz6csh%2FNRbd%2FkSI32j90I0XTr2G2ZbAGeax17KNp2gVL4dVGK8BDqZYjIVbol37tDGPthvwy9Z4f3tNd8iihqMlkETZlL4PdCqjm5L7Xk0B%2BTH7Vcku%2FHCLag2eb%2BEnirb4DPX8gLXIgoIt7z1PHrx4JG6QaWl4BjzRFzLP5sWNLALOYKrBuOhBnyTGbN%2BwZofTRXPCH3bWmws7qOxqzDLyPO8BjqkAZTYY2Cbx%2BvV5KaYWlBccTxOeAqid64TyzV87ykqlRqW22knOQWajsPgB%2FY8RJtfyphtW7J63n1cQHzA%2B6Y7wZ9PoYYBQZMvo1lUDwh7i6fDpSaC0CRtAM3VCxF1aDCWWfl3zet3uY62torZE1YnpSmtdJ4eS1fDt9zFA6xeucMEQjakFiML5LyHZlP223w3T1YcgpZ%2FitEvy3XIrgexqh38wQRa&X-Amz-Signature=f517175de2a74b8de0d8e6d254dce935387434450a6151a29baf292e86949a74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=26da8884a6807d73cafbd2ba53954eee9b37ecd0c62d769c5df63599b24d20c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=2a1a319ccd5b7b66b1f35c1dfaca6c5029c6799f16c8eb26d94a4021d6e5b882&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=0bbdb34fb828623c5c67b60e4604fb2fef7b70c1e96b75e634e716c66fb65cb6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=5b2fc68d1d8189ac980874b544fe6d892997fe87b4b240ee03961d28613a0013&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=5b95cf8b7282e5b6ddceb1be6957d0897510e78665b5536a47915a262ef6a5f8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GUWPU2C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRGEJ5Ve8ahCYw2%2BeaDuEC64oN64pxeDHei%2BClPm5TYwIhAL%2BpsoSMTmmrtKR3b88lM6In4he3COiPDZ429Ek4fFOVKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyU4tBlqod4FJ02bjEq3ANMMtQwQ0mKwqFqMtCJBwIF9Ors5GNJ5Z4WzLfT39aplM%2FX9lLhtVMCIw7ATGaNRQ8q6Z27b4dj5bIB5J4x8%2B93yNEHCspJBsaNC9q1KE%2Ft5ZYy1toKOEM8yPWXLIAMkO2q4cRl6WzCCBqmiQsSdHwhtqomx9HQyyUhaiTHY%2Bvu%2BfgZ0K%2FoPBpjA26%2BNOAycwOq6AubB6yIxVuNpWMWNdlwTXxe2IwHHtIqTthp4j32zOBAI6Ubr2SYoHa1sN9AhmF32LkKI1qYuPhEng3EsPWcyNfDnGLUVqb95vuAXLW4Nz3bSVmq%2BGHDXMryeAqPBRU1Dc9KWOtm%2FDdr3IyKMQznuZS%2FPIf59Acx7DmSu%2FfzNgw9cotUTmY9uwASJ5oJkHK8y2Qp5dB0ySzm8MUjG2RmCveGltUujNV%2BXPv9BbYhTQUsfjPnt7MbIzwPddsiKpW0t6%2Ba%2FCfGg2UAsfRadmR2ZvfULJiss2Ub9D5Bntnp41I9Fk0vdNAXhDkr00Pqy8I49IjHGOylGjob55XTuCTXxQBZIk8DRvyk%2BM%2BGGFq7g5Xzy6HMG2C19ElXzzFShcbpl8QxeFAk61uu6pVR4eR6IZF7u%2Bo9EmAroODxWIIf2jG6j9OXbvwAMP%2BzeDC7yPO8BjqkAT%2B2pLEtdM4BK%2FxJq4V1wcr4vS0i6WHtz2TSjD8TtcwD17z5FYAu%2FJPJucx08bxt3O80nmswxhju32DcSLHD8qPwIV%2B5I6rDNSLKeEmZLznII%2BZ1fG9drnr3Bi29IKj6kiQFApTtlMXZtLRDyGy8Y1eKVAEBPvSMd2Pk8ySt%2BY3lfPV5GzJWsoebShz6GkKiKMAJfOXVW6HvZBeA6rQzNMeVRinJ&X-Amz-Signature=b9db7479baa8b176b06ae04352341dde6836903ca29c541463d65e650991a70e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U43ZWYQM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNGKfKfL4suVrxLTFqp%2FqN6mXKhMouVA5JVV0JtIeUHQIhAPPVT0B4%2FnByF8B3gq24zsbD8WE1m0RLRXaxwO6c51b9KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwAcOp2lxO5cnp23Qq3AOe7M3Zrg7n4u4yYR%2BNgel2S2MOi2CU18Rc%2BzEofabnQLtgJw8kYrg2ZRcAWV%2FnRvTdhBfFM3a1lFx%2FK9rX1S8PJo9hUf6ZaQ5fWCkrJLQlocMH2PHiyXdafcEP8el%2BjaQxNcRN1QCYLLd8dBB2OVTk8pBt25AIifMVqsxSO1SePGjNHwuQLXmxKuzBfNHKOcRbzQtebukhI%2F1mwN0aSUJ5Sv2iGFp5JjAUEj99ePKFkDR%2BBrRWNzTtjQjWvOWEwuzBJ7vC4WTWvjx0VE3oCKD6oWMu91%2BVCfBy8cQ%2Fpo%2BygGzz%2FvbmnGNuv3q9%2BOJi1TuchlB7lhQDF8UG0xF7ErynvQlBi%2FxnUF8vJstXh%2BttfhNrOFcHbPWbql3d06TqkuMSy0J8UpMXhGaIJ1XqKByFQcroASBunOc16iUwoeC9wd9kUT6WviFtrHro%2BxdBYE2aXLFcz7vv5KxQC%2FpHdpQ2r8%2B0gyVV55%2FUhQcvFs%2BSRpt%2BxXmTOciSssnXh%2BLZo8jCr8GPssXbZV7JxRot0s7iwjv34sNWz6DWfF8a7qNw0jBNUtziies2qs7RYQCGddkc%2BY7Z6lJJU3DX2YxxpTg9XyXoCRk89I29by8B2wi7B9zeircZuULAfM29djDXyPO8BjqkAZRCNvLccHtHYoQnXs1dzNYmJj%2FVmPvCjD85AiVx0i%2F7TDw5gD%2B%2FxZo0KBTJq4FaRrFeRuF3v6tDTF9E68VMZFMtPjg29NEApki7iDf%2Fad0mEOAK30NyXa%2FuSLhdNTwsAZ%2FL5zuX%2BdWub6qsN3CWC41Irkgd9lr%2BEGqZATlz0UBl9YB5K2r8xa7aIZJh31Y6XvQ5f1yR%2FaKCDuNDgTxaWsKm6Pah&X-Amz-Signature=0a8f7b6aaa77a8b0cb3b3a3a92438577845de9e4f6b7dfbb89e06ac3c485d389&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U43ZWYQM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNGKfKfL4suVrxLTFqp%2FqN6mXKhMouVA5JVV0JtIeUHQIhAPPVT0B4%2FnByF8B3gq24zsbD8WE1m0RLRXaxwO6c51b9KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwAcOp2lxO5cnp23Qq3AOe7M3Zrg7n4u4yYR%2BNgel2S2MOi2CU18Rc%2BzEofabnQLtgJw8kYrg2ZRcAWV%2FnRvTdhBfFM3a1lFx%2FK9rX1S8PJo9hUf6ZaQ5fWCkrJLQlocMH2PHiyXdafcEP8el%2BjaQxNcRN1QCYLLd8dBB2OVTk8pBt25AIifMVqsxSO1SePGjNHwuQLXmxKuzBfNHKOcRbzQtebukhI%2F1mwN0aSUJ5Sv2iGFp5JjAUEj99ePKFkDR%2BBrRWNzTtjQjWvOWEwuzBJ7vC4WTWvjx0VE3oCKD6oWMu91%2BVCfBy8cQ%2Fpo%2BygGzz%2FvbmnGNuv3q9%2BOJi1TuchlB7lhQDF8UG0xF7ErynvQlBi%2FxnUF8vJstXh%2BttfhNrOFcHbPWbql3d06TqkuMSy0J8UpMXhGaIJ1XqKByFQcroASBunOc16iUwoeC9wd9kUT6WviFtrHro%2BxdBYE2aXLFcz7vv5KxQC%2FpHdpQ2r8%2B0gyVV55%2FUhQcvFs%2BSRpt%2BxXmTOciSssnXh%2BLZo8jCr8GPssXbZV7JxRot0s7iwjv34sNWz6DWfF8a7qNw0jBNUtziies2qs7RYQCGddkc%2BY7Z6lJJU3DX2YxxpTg9XyXoCRk89I29by8B2wi7B9zeircZuULAfM29djDXyPO8BjqkAZRCNvLccHtHYoQnXs1dzNYmJj%2FVmPvCjD85AiVx0i%2F7TDw5gD%2B%2FxZo0KBTJq4FaRrFeRuF3v6tDTF9E68VMZFMtPjg29NEApki7iDf%2Fad0mEOAK30NyXa%2FuSLhdNTwsAZ%2FL5zuX%2BdWub6qsN3CWC41Irkgd9lr%2BEGqZATlz0UBl9YB5K2r8xa7aIZJh31Y6XvQ5f1yR%2FaKCDuNDgTxaWsKm6Pah&X-Amz-Signature=ae9353be47cf194501817c7337dbf917840c9994c12b91429d74db682b71297f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PXCKM3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeiJcm5Zo4guQ7uH4iqXdTDc90mN755%2FeeNrZjxm0bRgIhAKOPE9M2Lqhc0mM0gu%2BtAGsOre2t2WVJjLlb3sw9rFOcKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCM0gE8iVIAdh8Fwsq3AOvK4jQREP5xAOxuHritKGggUfPnweOcnxiwuq%2BlW%2BwCjklj8lJHW70e8tC8bsslzatSVczh%2BXiVddkPinFcJbWtt55iPrvO3Y%2F7buApdXH1ExQc8GEgePI641C7NIUBtGOaqLL4vtErusdvCNq07M95xZrmpq74XRH5MZYvI9Q8%2BijMp6BvphMS8TzVF%2FtTCk6PaMn8AfdhMv%2BZ%2FfhsRQ%2B%2BUMH4JDyKEa8zCcbUgXhOLhXlWEa%2FpxvoXKanHHPzLEvdgWQSlh52J5I2fw8%2BEBhnqP1Pjn38NJHow0HKpWDQiZXVjB1S1cTstnADDFQvnhLZVqeTRdeBMyyOIxJaOPM0uI7rVLYoNytau8nEkNj6aRcdip8hUoScfKTQBcCu0nJRh6WjKAYNyM5n18NwOuQXTV%2FA2WFT0y9lnBkMyXrSUxAT4K5vrDbVsijWCudl3E%2BndHPt6AqxIKp3XZx3BwBo1iQJjGTA1zA43IPSHffURApaedLvrfqvHrlr7B3%2B19WKMhN3%2BcvAkanj4izmHewd2QGJVuEekVWAyrmkruax5e0SAvZ9%2Ffcdgd6lteKAjoVgYZxDrgJQuZnQFzTYzTJ5F6trJsRV%2BmeCxkge9T%2BFgqP77NKtjnx3OLP%2FzDJyPO8BjqkASwbj2nh0wcuXssYwKEVJyeiheojR0bvkyLXbEylXR95le3wnd6ZYsAtrGG4tyvJuobJOqvVbCvCtPGkDnU9xw4OH0gy61LFm2%2BikwbBrihbcfz2FfqAjAgHUShV8IdW9yp6iQ3wBMbtszh50Tkhqzstiu9YXVXC6V6oIJwt%2FoVHAC%2FUbVmpz3aWP0j0IAd2qJSJPXcZcPEu4mDa2itvLTMf1M%2BL&X-Amz-Signature=14afcbd1f710a413d7f33e68d0ccb08506de8335deb60fcf9d4393bc1232d5a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJSUBUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsPX60P6p7wcraf2UmUoX6vxEvqmzNNACKDeHuq%2FXiHAIhAO6AZitEursFQQZrjg3KI3nvKFwAX17ys7lNsGQ8Jn8kKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhGFbEMScoM9GCyxgq3AO7ZpZWq6P3bBIeKx1hcwqFx3h%2Bci6RcZP5gq2wCDBq%2FOTL%2FJ0EBCob06QtHDHjQm2Utj3q6Ds494kAR0HRI3XXpjGjba9bD9fVFok%2F%2BzntPAchsJDeqe%2B92B15HLuldwOGXiE%2Brc%2BPEOS5VFq1n8yP5e%2FiPtkks8cW1A67AJz8W%2Fjs1st%2F6%2FHbiuR%2BBmyhz7CkOIYf7kiCCv1zT14Rgxw2Pxe1MziCgfVBiQgMQglFRFnQ2cvnvGGB27Hjt81jO4OqwMAqLeSqaVePAO09cOu34WtmSeL%2F%2Fm4E62jugBBzVfut%2Brf7J1zew%2FHqJH9ZYc%2Bj98nyfER3q2kixQtknv%2FpSgeTDmQlaO%2FF9pR6WgSos87Wm8KPWeKYWfT469K3hOJf6nZC8VjMlJBCQMgAI4s3c4If5zBd3CSKJvwZEq1S5qzckyjnwQ1%2FM2mfBezaBdKzaqE6SSCfouolNet19GXBmA2tMtgSOSclgLn9Y2g6e58yoP3xB761JFU8wtsIaFrJNX6ypi6yc%2F2Xe%2FaYAQGs0syqB09NH5eIFgnMBZENDzcojgWyPILm8rr9BhgkA0P1YjaU1E7ZguUYOqYBWOZPPrwIIIIVMZtLp53tQLzNL6N62Jvoav%2B%2BmxB%2B%2BjDAyPO8BjqkAXzCZVHvGkT9euSk6N6sU8KbY604ZDJOME%2B4o7ADfyWra%2BVw1R1yr0vPA7DFu6G62yB2%2BGRpzIB0qvSSdnalyJ8FfieQmiD8obJjIJVuEOWzf5uMncD0XcISifIbF8nlfnVkJrX7kKIsAZIBJcd46SwXRIx2%2FcOEkx4YcZNLEv%2FeMif%2Bss3aS2aAkOrQeQmOfDtQW0ljJthreSsMKH19QSywU7bF&X-Amz-Signature=a5a303eda9c5b5b21a73cd3cbe7edc4216a227742f9997a426e20eacf7a8e026&X-Amz-SignedHeaders=host&x-id=GetObject)
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