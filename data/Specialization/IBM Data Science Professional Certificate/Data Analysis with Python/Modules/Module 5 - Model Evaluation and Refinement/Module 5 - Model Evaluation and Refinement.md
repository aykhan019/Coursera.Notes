

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=5da9c45f5acf9cf70cc304ba0fd3fdf4c23229682d552efd6492878c914b6831&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=b3c81476603673143d9f6329937230ea491cbd887885c9561729bf49d12b61cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=b00ac12e118da0fbb5366bed5c8bef8f73a787ee5258fda366f0e457911cd06c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=a27c5a73e777504888df2b5d85a0eb09eb996d052604d5496d96e38e416173c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=c2e35594199dff378eb454fb0794f4325af00ec2c96acd5dba02e9621f422892&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=0045f810331698c565c3800db2308d0131c3d99365c10d899e460a46b58f40d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=ea57f30830ab7f86bd25353473768fe89f565f5a19591a308da0e117b5779591&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=fb197726c0940b1ed11c1fb7c4ee96c5928bc6aede637ebb8a8763f63e4e9c0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=0e05c1e979df4f2e3b8a91ca44b51ff3351c17d3c17858af55a5637b7fad0fca&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAFOHCD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcIees8TC6I7kEcoEY18p13OqIHwOvnv2QsZ%2F%2B9j8sFAiASSexV2E92nS6rNVwCk%2BhoqQ3TZqONEGLmeth3wGG50SqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv1nrw3KofyiRBmEjKtwDKCfGWyCO2fRyFjSO%2FSjstTj%2Ba22ZoC7CnBS7ud%2FxxZ20iRgXG3BysMi6eQvtCDsnkKgQaUW7AkLzLEBW4lRtx3WHld3UUaJRbZ8ID4r7UZ88GwStYKQQAbcAF0j43YNnbz%2FrGFj%2FCsPlfZZLgBQ9Dm7VY4xwca2Xrs23U7uGI%2FaTxSc5LPF7EBNKffCLrPnHmNpIfrD93bT8UXL3mxvHTnD2DE%2BdPJybi9f7OaAzlIpoa5Seiq6uTr8LqTfQ3EshY8ZojSDOcbH%2FwQXwEVaRtMc2phzrrnkXFa%2FfGNgbkbewwgN5JM6WtF58DMof4a8LgP1wqBVJj8O9zMtwx6sltqTdAktjhXhHRZnLcct69Hw76QVxTAh52KEl3MFgU2gOZQSfmEWrWmnJ6pQEkkSoqQPnckKACYldSgOimSRKgxvjOS8aMPUis9wx%2BtWPq5A9jE1nzXBXmVAAZckTsPjmQ5iIj5K3IDGZ12kAxq9mfNF3YlwlNLj6W29fZBhLxT89PmcWp789JnuSIDM8SS9WCL%2BlCmQhcUKxlyQUGrEtzM6QEMaDibS83WjmMGd3kow4eon%2FW62wlvIf%2FSjPnT2nlaQHM7jpNLb%2B3M2LjhKwQHPg3RY2j2B4RgA7nOow47vpvAY6pgHOKu%2FCV6d5VXjtE3alsludgaXCl6ZQNHYrYM9sYHmoobY2FpwCnWrmZPCfoTkG7HYPv%2FukN3iw%2Fm0FfTAjSak0znppQdmoeddAXcz1zDIY%2BBLV2EOPDIOAwDohhJSLyTzIokooV4A6peyw0pnNqS1Rfdk6OHkPzpJMOqFVGkZoN3SqJ4Hdl01YD1L5OU7i5PdcEXfjzwbh2zNCGeEXKWYiExL4VYWy&X-Amz-Signature=4959b869354019b21544b5be4d29b47724d89c6f42c2bc3a3f6b6c014eeecb51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAFOHCD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcIees8TC6I7kEcoEY18p13OqIHwOvnv2QsZ%2F%2B9j8sFAiASSexV2E92nS6rNVwCk%2BhoqQ3TZqONEGLmeth3wGG50SqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv1nrw3KofyiRBmEjKtwDKCfGWyCO2fRyFjSO%2FSjstTj%2Ba22ZoC7CnBS7ud%2FxxZ20iRgXG3BysMi6eQvtCDsnkKgQaUW7AkLzLEBW4lRtx3WHld3UUaJRbZ8ID4r7UZ88GwStYKQQAbcAF0j43YNnbz%2FrGFj%2FCsPlfZZLgBQ9Dm7VY4xwca2Xrs23U7uGI%2FaTxSc5LPF7EBNKffCLrPnHmNpIfrD93bT8UXL3mxvHTnD2DE%2BdPJybi9f7OaAzlIpoa5Seiq6uTr8LqTfQ3EshY8ZojSDOcbH%2FwQXwEVaRtMc2phzrrnkXFa%2FfGNgbkbewwgN5JM6WtF58DMof4a8LgP1wqBVJj8O9zMtwx6sltqTdAktjhXhHRZnLcct69Hw76QVxTAh52KEl3MFgU2gOZQSfmEWrWmnJ6pQEkkSoqQPnckKACYldSgOimSRKgxvjOS8aMPUis9wx%2BtWPq5A9jE1nzXBXmVAAZckTsPjmQ5iIj5K3IDGZ12kAxq9mfNF3YlwlNLj6W29fZBhLxT89PmcWp789JnuSIDM8SS9WCL%2BlCmQhcUKxlyQUGrEtzM6QEMaDibS83WjmMGd3kow4eon%2FW62wlvIf%2FSjPnT2nlaQHM7jpNLb%2B3M2LjhKwQHPg3RY2j2B4RgA7nOow47vpvAY6pgHOKu%2FCV6d5VXjtE3alsludgaXCl6ZQNHYrYM9sYHmoobY2FpwCnWrmZPCfoTkG7HYPv%2FukN3iw%2Fm0FfTAjSak0znppQdmoeddAXcz1zDIY%2BBLV2EOPDIOAwDohhJSLyTzIokooV4A6peyw0pnNqS1Rfdk6OHkPzpJMOqFVGkZoN3SqJ4Hdl01YD1L5OU7i5PdcEXfjzwbh2zNCGeEXKWYiExL4VYWy&X-Amz-Signature=3867b49d590e7519d69589ffaf66870017c21fa098bb99e74b57e824d4bd9dd5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAFOHCD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcIees8TC6I7kEcoEY18p13OqIHwOvnv2QsZ%2F%2B9j8sFAiASSexV2E92nS6rNVwCk%2BhoqQ3TZqONEGLmeth3wGG50SqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv1nrw3KofyiRBmEjKtwDKCfGWyCO2fRyFjSO%2FSjstTj%2Ba22ZoC7CnBS7ud%2FxxZ20iRgXG3BysMi6eQvtCDsnkKgQaUW7AkLzLEBW4lRtx3WHld3UUaJRbZ8ID4r7UZ88GwStYKQQAbcAF0j43YNnbz%2FrGFj%2FCsPlfZZLgBQ9Dm7VY4xwca2Xrs23U7uGI%2FaTxSc5LPF7EBNKffCLrPnHmNpIfrD93bT8UXL3mxvHTnD2DE%2BdPJybi9f7OaAzlIpoa5Seiq6uTr8LqTfQ3EshY8ZojSDOcbH%2FwQXwEVaRtMc2phzrrnkXFa%2FfGNgbkbewwgN5JM6WtF58DMof4a8LgP1wqBVJj8O9zMtwx6sltqTdAktjhXhHRZnLcct69Hw76QVxTAh52KEl3MFgU2gOZQSfmEWrWmnJ6pQEkkSoqQPnckKACYldSgOimSRKgxvjOS8aMPUis9wx%2BtWPq5A9jE1nzXBXmVAAZckTsPjmQ5iIj5K3IDGZ12kAxq9mfNF3YlwlNLj6W29fZBhLxT89PmcWp789JnuSIDM8SS9WCL%2BlCmQhcUKxlyQUGrEtzM6QEMaDibS83WjmMGd3kow4eon%2FW62wlvIf%2FSjPnT2nlaQHM7jpNLb%2B3M2LjhKwQHPg3RY2j2B4RgA7nOow47vpvAY6pgHOKu%2FCV6d5VXjtE3alsludgaXCl6ZQNHYrYM9sYHmoobY2FpwCnWrmZPCfoTkG7HYPv%2FukN3iw%2Fm0FfTAjSak0znppQdmoeddAXcz1zDIY%2BBLV2EOPDIOAwDohhJSLyTzIokooV4A6peyw0pnNqS1Rfdk6OHkPzpJMOqFVGkZoN3SqJ4Hdl01YD1L5OU7i5PdcEXfjzwbh2zNCGeEXKWYiExL4VYWy&X-Amz-Signature=feb1d509893cb7bb17d2fb3a39a7147fa76dbf0c3d7e33429ad158f8360ea1a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=430a1ba0b14c944f791cd96e1b41c89192ebdd603b2108473fc9feae6227a602&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=245bcf9097f8d0f07384f064be663de239d97ca9924e3f3e92d3ecf70960cd09&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=e91db16aef49b376905fc9d325ec794a41b201d224599f9b057e7c7d88690859&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=74529b80ca99251a3bab01f030d2f6ecd7d61d47f37085e22cc1ffd6225c6d08&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=8742869f4cc07ba5a898fea77b1d92ad09435ebcff939746c4a32ce97ba75863&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647XJG54Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCA7MbP1SPhwyfWfhx5kvc3ncdIlbkH1aDBs5tOa5QEcwIhAI2xUN9bXtGbQVNc8%2BnpdVmGTKqyQQOIMZSHhMyA3K1oKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytgquiaeIpjCBMOYkq3AODgUQFsxadxjFJu%2F0L8ARZ3A%2F%2BNVfe%2B2jaYitOVmffYRaQQ%2BDRlRpPDDxqUpg77li%2BYwGOvFaQ5LYwbYTcqQgEWMFwz4sAcLMg6geraDERq3OXDIuWrA7VXF0Sqjih3WWdUFVgnkBvJxSpetQrRyGoJNLePrPIibYqRHoanNpRZ2rlDmjvEFc7xpWZh0wkt02CuxBWhkBsORV6b2BzE504jrJWoCCVIfU15CBclejnzAC6jTYA9nWcF6QnSZDPKkvU3EcUfLftluGEtTwXIwK%2FSREZb02qRmDCp4RJA8eoLyPDDzdS3gO4XLHXoEmygBRW1D%2FfjLRp%2BiuObLf0Uw0%2F8x575tD8tDfIfOXqeSLUC9xD2C%2F2f3LNVZDmif4gZRcJEmcG2ycm3Cqd5hjofuyhoUlO7UvRN1mCXjYIr2QUZOJrXaZbGj4kpk%2BQqdxOAMIswoLLX9tBHzAtySnMrykNjyQuvEiQNWXxTCAIZKDQYeK44%2F93XR%2FfdSVhaIfJG3XeOU7UmnihOuSJsZIQaiWds8iXi0T5DL5g1jx%2B46VjbQH3DbnCbidVTFkVmoIIAh89X9uSkGVrSiGKKyaYnrtM4NGagM67eWgdZxFnxf6nxr9YGMeEkmOCffmzEzDLu%2Bm8BjqkAVZfDwaBhQFK4fx6Cwca4ztiMk%2Frms6fLlI%2Fin2tC8xfwfJ8h2oLdujG%2BzH4GnJoL81E%2FIfu462h0AprZVAIQMxVytmp0iEV8%2Baa%2F26PjjV3wFDnvFQmFjTb7Hki3SuLLEldCwhWykDPbyd28y%2BVIMh6G87%2FfUS3%2FL5LXUnVVQBeTZ2KkMwvEC7zNGlQdtboMlAlExRXNasAT5jaGMEPNui1NlcG&X-Amz-Signature=aeed2ddac7baf3ae2c21dd7a917f3870b311da27ab024e5ded802862e286017c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJY4UJRL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGWS6mlpFvT6ChCrlmbRZ4tWHLyQJS06kmFrwZwNq8dEAiEA9W1Qg264%2BTuVO7U%2BUoPs%2FQtgQiddDmX65fvTvt5nhOUqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDffPJbKEWm8AS5RqSrcA05G53K%2Febtn6UVcFELHGaKg4KD0tA5iY9lpbMIivkE3BzWj8Qh%2FLQAorn6dQ1DHH9OzpebI%2Fff4BK1LnBOqpoztVVLq62hviDX9vJBUQoSFb9Acwj6FX7hR7GRzGZ1RNGw%2B0I7iytqsa%2FLtDftuiyDAuK0GvtcLtfRAyEc09PAS7ckwKBhAYNhgT6MY%2FcyeIz4MAoMvpWhNmY8Kwxrv2ghncXo9mJbS9WwuNzFq1C3m8IcUH5%2BD8y31LmUAkw9NkJ6lMb8lErdtCqGyA8IGX7TPLuGiZ%2B9fAAA3Z1NeM6rxUBl7RHRPsC6neI1koAeu9eO5AHeKLxFI1Q9aQeL%2F5KeDo3QCOZbymopVojfX9ONuQlTY%2BNSiKIADbuEmPn0uofNOO2ElZZpuVonq5BLjjCkstTRw5kE%2Fukzyl9tbmdAWX1o0PEP8CVe2sF%2FDfAjFaXlvXkQHsBYAZKcWZZOarV1DjXipjWsB8g1M6Wwl4qLLLJfWu%2BKzJID8FckosuGFbN6MNiz5VSIdxJsfTeQ%2FUxE%2F9X3jp2BwDs0TD8JRcYwbNWzj7J0ul0il3Od8czuMBzcqnLXsKLvMemVD7LQ6r4y6EZRtuQwzBxk9gNRMu%2FFPB0VJQjoXNtlIgePWMOO76bwGOqUBxU%2BYaCJNgrMTBImp6t%2FKpF%2B68VfV8MlJawCa%2F8qwTOu3W0vTmPbn8aHGga7vVxxnejiXo%2B8jI2BloSasBcOv0b3oTisli2mh0zakzlLJ5msRe9LQ2St37kAqhsC6QB56oxd5x9TvM%2FKbkfOGc%2F52QNpq5cWGJmuJmspFB3SUrkgWm3N%2BVHL13g%2FQNcAliGEcjS97wkdg7Lb6s5ql8M7SCRs%2FLg4S&X-Amz-Signature=1c62bb5b52cb4a2f73f7ce966079fcfc961181f5aebc9b2c3fd613bb6b86c74b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJY4UJRL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGWS6mlpFvT6ChCrlmbRZ4tWHLyQJS06kmFrwZwNq8dEAiEA9W1Qg264%2BTuVO7U%2BUoPs%2FQtgQiddDmX65fvTvt5nhOUqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDffPJbKEWm8AS5RqSrcA05G53K%2Febtn6UVcFELHGaKg4KD0tA5iY9lpbMIivkE3BzWj8Qh%2FLQAorn6dQ1DHH9OzpebI%2Fff4BK1LnBOqpoztVVLq62hviDX9vJBUQoSFb9Acwj6FX7hR7GRzGZ1RNGw%2B0I7iytqsa%2FLtDftuiyDAuK0GvtcLtfRAyEc09PAS7ckwKBhAYNhgT6MY%2FcyeIz4MAoMvpWhNmY8Kwxrv2ghncXo9mJbS9WwuNzFq1C3m8IcUH5%2BD8y31LmUAkw9NkJ6lMb8lErdtCqGyA8IGX7TPLuGiZ%2B9fAAA3Z1NeM6rxUBl7RHRPsC6neI1koAeu9eO5AHeKLxFI1Q9aQeL%2F5KeDo3QCOZbymopVojfX9ONuQlTY%2BNSiKIADbuEmPn0uofNOO2ElZZpuVonq5BLjjCkstTRw5kE%2Fukzyl9tbmdAWX1o0PEP8CVe2sF%2FDfAjFaXlvXkQHsBYAZKcWZZOarV1DjXipjWsB8g1M6Wwl4qLLLJfWu%2BKzJID8FckosuGFbN6MNiz5VSIdxJsfTeQ%2FUxE%2F9X3jp2BwDs0TD8JRcYwbNWzj7J0ul0il3Od8czuMBzcqnLXsKLvMemVD7LQ6r4y6EZRtuQwzBxk9gNRMu%2FFPB0VJQjoXNtlIgePWMOO76bwGOqUBxU%2BYaCJNgrMTBImp6t%2FKpF%2B68VfV8MlJawCa%2F8qwTOu3W0vTmPbn8aHGga7vVxxnejiXo%2B8jI2BloSasBcOv0b3oTisli2mh0zakzlLJ5msRe9LQ2St37kAqhsC6QB56oxd5x9TvM%2FKbkfOGc%2F52QNpq5cWGJmuJmspFB3SUrkgWm3N%2BVHL13g%2FQNcAliGEcjS97wkdg7Lb6s5ql8M7SCRs%2FLg4S&X-Amz-Signature=8cb0d7bf0f499d42f8a75eeb3ec0323365dd40cd7fb1bbaa88eb2363aa911a51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4XKHKF2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkBnc43ZygOCK4BuiMKlLFz1nHyPvxuvZsDxvAcriDgwIgA1AWU7eTF4XNgyAwHAtOgwr06dDs6tmXUpFUykUXSDAqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5h8Y9%2B4qqudV3tfCrcA2dppD8Lrmd40qC4Je7p%2BUSu5NmGTXxL%2F06rZtuGkPWhSZmwx30kGDtB%2FZHWHOEYO5nLXkX%2FloGcfcUcL5g0ofEL7elCmKR92CHZ5k9mnQuFJRZtS8UwmEPOKWz3EL8FbIFOalQfuJu3G95Tyazihs3Ab8sHOYCFJjWKYlI3mVsZ64qEnBI3mKz4D8OiQhw8vawws%2BKIdzh2DzbjGxpNvp85TCunfeli911nWBuXh8ypgSGd8dSlBbvuUb7tr6QXPO%2BTMRMGRGXlCpspxKpuRaBcaEY%2FG9q87fdRQXaj0ftis7ta73FR3J5XvAA29Cc0DQFInZpkyB1oHcQDHcfSZVD15JPiYMadZWYGfyCM30fBfZqmDsEy4Kpcnt2KsVTP3mnCkJ0m3Q2CKyuKrF2lpyjYIhuPQ5UFhY2ocm1V2enWHynObAiYJiN%2BTzTjaSch99P35izndRiGvU2EBEVz0b6sGDFVwhiqYxgHaBexpCeYCWb1%2BnyuxIVwhoBGrnVsbdwcz0VCYzlxsHn1MdlJSExcEw%2FHbmvVPwOxyQdjNuHvdLFx%2BhZQ4cReP6ToaGvwgmYi5vBdBYXl2%2FUNDawE6KEgNUcnhzX7vGSLHDAb8ZkrT6D%2Fkz12ef5eTOjRMPm76bwGOqUBMtgGCJrPwBerMYCkAnYUe6eZfUPhJkhIrqXru5q0z0QTaEu6SPLqbBoi62I1FUVCoFIX1r2TKClI%2BfAiCg6nrjp81RMFP88VgZWWpul3Kj3uOFIj%2Bcp6U84dOuAGZ3kTS0YnidI4YN4exem9L5CZGlFtgwCT7a8DjkpouE32Ze8jSLHrhZkRxsAMbaaQgmhQjjRgSl68zEldYF1g%2FaxHyOZp1gha&X-Amz-Signature=a55a366a2dc664c5feda250a5affa3cefc7014b7221a72506dabc761a9ca87bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=c54ce0da15515910079ceae633d15ec7f8dd9abcd173fa6febb5181cb318823f&X-Amz-SignedHeaders=host&x-id=GetObject)
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