

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=05467c723ea148fb8188c6a7e85bc226341c9ad6d5f54a1f4ed239288962c614&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=ff344969afc341e07794cb26c80756e6115f53c6e3f8c53544b102952337bb98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=95c82536ea625650f201f755b4e01060b66178c9f1ccc3f36c390de7f91d2e8e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=4d0cea7050848b0b80b2146cd069feceb2b6518c638fe0e66e3cee1b19967737&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=e908f057a0164a46b726d0e83e04094e5811af3df86622ae28fd02a69505924b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=dc7bb79c9924fafb208ac7a879c135ea3cc59adafa9ce2b081b919bd25c38de8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=b1b80863386ff703ca54c91e61698062c1c2d5dc015a84f7475c5297e7ddce7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=fc9781a70e2eb7fbeb34a420093df3af98575aa09e5bffe0c976a2a2320f4ebf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=38405b718090d236ebff5ac7fc0d8f573399319f4dc6c66da28b37db39529fc9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPXUHOMX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCeX8sKara%2FPvtoir64j6IWgxrUphtsVauTfDiTEXBkxAIhALtROAnkPggwmVOxQTVIVxAUZed%2BNEoIwUDPgnWMYNQXKv8DCHwQABoMNjM3NDIzMTgzODA1IgwbQw7Cp8072MTw4PIq3ANhaJ3MN09G%2Bne3urUDBGhdJO9ZawjinU9UCkB2A0LFpQsgc2itJe1gQ5ejpmNCXjXOEVSskuizsuUCN9gr17F3nOhYSfPoZ0PgrQdB6RBwwcMUPK396KQ38cBlB9CiK8vv1GkW4%2FjpbZxotBhpF3xctljbdxUoVO1Ltb3dzsm6ShdX%2F1sJaT2X0%2BYVQp%2BRSf9G3%2B1p4PU1H2rWn75YqNk8FUK0Rn2YcqOQiO66jgzpaDlloT35edJuGPfz1h2jas4PrSmFPqxD%2BwUQhl5RZXDo1R5z%2Bxi8sDW5pBV1FOXdCIweTmkcUNe8KMrVmV930JpPXsKEuZe3wl%2Bv7Pqx8EGe0nzV4SZ3LKk4DGv%2F%2FRYpAQ4z6XJD%2BtD2n2czKsUv6%2Fxyrf9YlZlWCqZnJTpsigqwayQ0cXh9R5vtv4lCoaedhC7BsRa%2BgtQjEXDMH9TzjLVnSEMRvTDCCnH6rtB3zqg9RtGABG1%2F7%2BY0%2FZh99QbMiww%2BFOeD8X%2FEH8yE7OL2gvMysej5QpMIXmex7JgZGYgVbDPJ1SSoNbkB1eyo%2BvEB7P1MKEmmv0NCYcCCXmu2cwC1ddsYt0sHz3Md%2Bv%2BXyKPFfNfd6vOXJXSt0aLxK3Mbk%2FFChM9u4Qrl4Kz%2BhTDw3eS8BjqkASl4i1uKzORCjqo9UzP%2Boxo%2Fmo1p59CKQlw6kMTLvKLuG8cAQBRY67GMFgWGnMK7nKg6CWUgFLenAxQ%2F8PCp1HweWXG8uSlm6K36VqNDN9stlnIJce50FyQFpXSWK0V4FErh7mAVzB2m0Mtj0fIJ3RvCNu9lHJLJdAZFnehm7gIjaq9llfIZY%2FPXZSn2MYm6dKfgb%2ByGCk7EmbYewSsV%2BWSx%2BOYk&X-Amz-Signature=6eacb78b85fefd0107c4b256019301f3713a8bb3630be260501163f00f14a35b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPXUHOMX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCeX8sKara%2FPvtoir64j6IWgxrUphtsVauTfDiTEXBkxAIhALtROAnkPggwmVOxQTVIVxAUZed%2BNEoIwUDPgnWMYNQXKv8DCHwQABoMNjM3NDIzMTgzODA1IgwbQw7Cp8072MTw4PIq3ANhaJ3MN09G%2Bne3urUDBGhdJO9ZawjinU9UCkB2A0LFpQsgc2itJe1gQ5ejpmNCXjXOEVSskuizsuUCN9gr17F3nOhYSfPoZ0PgrQdB6RBwwcMUPK396KQ38cBlB9CiK8vv1GkW4%2FjpbZxotBhpF3xctljbdxUoVO1Ltb3dzsm6ShdX%2F1sJaT2X0%2BYVQp%2BRSf9G3%2B1p4PU1H2rWn75YqNk8FUK0Rn2YcqOQiO66jgzpaDlloT35edJuGPfz1h2jas4PrSmFPqxD%2BwUQhl5RZXDo1R5z%2Bxi8sDW5pBV1FOXdCIweTmkcUNe8KMrVmV930JpPXsKEuZe3wl%2Bv7Pqx8EGe0nzV4SZ3LKk4DGv%2F%2FRYpAQ4z6XJD%2BtD2n2czKsUv6%2Fxyrf9YlZlWCqZnJTpsigqwayQ0cXh9R5vtv4lCoaedhC7BsRa%2BgtQjEXDMH9TzjLVnSEMRvTDCCnH6rtB3zqg9RtGABG1%2F7%2BY0%2FZh99QbMiww%2BFOeD8X%2FEH8yE7OL2gvMysej5QpMIXmex7JgZGYgVbDPJ1SSoNbkB1eyo%2BvEB7P1MKEmmv0NCYcCCXmu2cwC1ddsYt0sHz3Md%2Bv%2BXyKPFfNfd6vOXJXSt0aLxK3Mbk%2FFChM9u4Qrl4Kz%2BhTDw3eS8BjqkASl4i1uKzORCjqo9UzP%2Boxo%2Fmo1p59CKQlw6kMTLvKLuG8cAQBRY67GMFgWGnMK7nKg6CWUgFLenAxQ%2F8PCp1HweWXG8uSlm6K36VqNDN9stlnIJce50FyQFpXSWK0V4FErh7mAVzB2m0Mtj0fIJ3RvCNu9lHJLJdAZFnehm7gIjaq9llfIZY%2FPXZSn2MYm6dKfgb%2ByGCk7EmbYewSsV%2BWSx%2BOYk&X-Amz-Signature=20d1d00a5d6c54d3718c38c5d6b7d143ca43a157905fd0418abc40b53dd12f5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPXUHOMX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCeX8sKara%2FPvtoir64j6IWgxrUphtsVauTfDiTEXBkxAIhALtROAnkPggwmVOxQTVIVxAUZed%2BNEoIwUDPgnWMYNQXKv8DCHwQABoMNjM3NDIzMTgzODA1IgwbQw7Cp8072MTw4PIq3ANhaJ3MN09G%2Bne3urUDBGhdJO9ZawjinU9UCkB2A0LFpQsgc2itJe1gQ5ejpmNCXjXOEVSskuizsuUCN9gr17F3nOhYSfPoZ0PgrQdB6RBwwcMUPK396KQ38cBlB9CiK8vv1GkW4%2FjpbZxotBhpF3xctljbdxUoVO1Ltb3dzsm6ShdX%2F1sJaT2X0%2BYVQp%2BRSf9G3%2B1p4PU1H2rWn75YqNk8FUK0Rn2YcqOQiO66jgzpaDlloT35edJuGPfz1h2jas4PrSmFPqxD%2BwUQhl5RZXDo1R5z%2Bxi8sDW5pBV1FOXdCIweTmkcUNe8KMrVmV930JpPXsKEuZe3wl%2Bv7Pqx8EGe0nzV4SZ3LKk4DGv%2F%2FRYpAQ4z6XJD%2BtD2n2czKsUv6%2Fxyrf9YlZlWCqZnJTpsigqwayQ0cXh9R5vtv4lCoaedhC7BsRa%2BgtQjEXDMH9TzjLVnSEMRvTDCCnH6rtB3zqg9RtGABG1%2F7%2BY0%2FZh99QbMiww%2BFOeD8X%2FEH8yE7OL2gvMysej5QpMIXmex7JgZGYgVbDPJ1SSoNbkB1eyo%2BvEB7P1MKEmmv0NCYcCCXmu2cwC1ddsYt0sHz3Md%2Bv%2BXyKPFfNfd6vOXJXSt0aLxK3Mbk%2FFChM9u4Qrl4Kz%2BhTDw3eS8BjqkASl4i1uKzORCjqo9UzP%2Boxo%2Fmo1p59CKQlw6kMTLvKLuG8cAQBRY67GMFgWGnMK7nKg6CWUgFLenAxQ%2F8PCp1HweWXG8uSlm6K36VqNDN9stlnIJce50FyQFpXSWK0V4FErh7mAVzB2m0Mtj0fIJ3RvCNu9lHJLJdAZFnehm7gIjaq9llfIZY%2FPXZSn2MYm6dKfgb%2ByGCk7EmbYewSsV%2BWSx%2BOYk&X-Amz-Signature=0733cd28a1271d32846e83e42b00a4ad2abaa90b111af83f61de9595bc1bad2b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=9eadd50e0f282943e87a0211061f2f2f7a2403025694c41de88af2d43d811074&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=39037bf33f8752add8299a038aeb819fa7001d9cee55217b9d9c6692a317d4b9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=8df4861e162bb2896ad47950cab5d922a0fc31941b3f880ca58df81f28168f64&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=544d83c5c94f1326670f5a2fe7e74c2fa4d3422d5e1deddfd1b9f92d49807228&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=956af307299ebb2f57ffb8347bd41c6c98e046eb7c4d4cf3624a619ed77ad4d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLULUAVP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFOaDKtGp0FSH2IKnENq62yLiuYpmvzCYc6Px5Ic%2FoFVAiAWKhwoPqLHeDfChrJ89LKaCHEt82%2FvAIWj16HvGAeKJir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMtux4%2Fx%2F2tgl6RS1kKtwDcy%2BDtr9aoruG9eFIe2GJQWH1X21siTe%2FE70fDy9B6Ogp77F3SuguJ2W76kYfZaD6REMQoycQ8uYVIAlHqS5XE4Q3gwTGoboLZ6NApYVraOvPoAioXAxRl1uVFVyQGuZZK5iEhI7k%2Bf9EU%2FHnT33wmIgVwuXQ6TxJ%2FwpTeW039A%2F%2BiBTe%2Bxx8PgTCUwGQ6cbtLW0LoOwOf4V3b%2FBy6N%2BG2q0qUXZmYlVHY18bHbKYk%2Bkm729dA9RbMBd%2BQPP5V%2FE6SSZ9KPw4yZuV1MnSM3VFL1%2BYQgMghKMq%2BfQxKMBHlfqM%2B3X%2BrrKJPVcrcA8ysakvMDRTKEkp2rQJ5tocW8Knsj%2FG5KQjXXLxd6yYBAjJt3hF6ZV7rxHHS52w9aHStK6F9KTaLeT9v6qIf5MYXE2J1Jzm4k9uIuOc1y48VnpX%2BaRHm3QuPNqWGuSB0rDGJdIcKJ5GLsTAnRhSNzC%2Ba%2FckkEzOWIaFBS7q4NtdSTNYE17bhQIbDGKpoSJ4mEj9gdMncgl1XGxyAGQv522jy6kzFwxgL2K5XJ%2BcTbdMKvPTRXXymIlan4gZQgcM%2FkH04JgP7fWDtzN6E81zDK27raGmW77u94XzFeyk6oBjQw7uzQjpHi0j74CC6e2ilBkwyd3kvAY6pgHIeObdEcYzzkljMLLii8BbMviDwEPu6uZrGhLnhc4LACZvZRmaHzBd9YWDPOS%2BLrGP91NwIp5U10axnpQICogOhHNyTG0KhrLA5RiwJJtY00AQARdXZrwza3w9ycA67l7p%2Fq3Db11BCavrhl2rHwEwSGDWCwUrLCd3tuuNTDe53WklOdf6jJkA%2F4iykINu3CVBa6T4nKBOM0Gqgk7D4osu8IXf3Dqv&X-Amz-Signature=447717de64a93ce9033ef0b55f32675f449a2da4daa5ec68569e3afd66b16e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG3KP6UH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHlYvE0cI2vTtvmeTeIwCOyZ%2FMQrV8hYB2uA3MZKfhUrAiAMu%2BMoFrYgOE9xPLsxodop1NP0NBkhh3xY9e5pAquHrCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMemSS%2BFcE4%2FzvK3S%2FKtwDUzdqi%2FG9OiLRFyNtVnXtdwFDLXiS2Inwuw8NWolz6mks%2FNNHEWQLfMokSusZV%2FoZsI%2FCyGAueegGGCbl10J0UEpEASVeXC2eynpKHh1j2Iqf%2BoXmJRcWIXkN8IIVKZBWtNZRFmT71oU0fAQ4ymSrA70%2BPqL2ACg3ujIXKcMt%2Bkyhgn1onEpsSVTuuP92VWk2amSVFiSCL3bVUqi3QWnVc%2FRK2YAVdNIu97XKzPr%2FD58KISrXe5iJZjs0GDcP4u08AwarYFs193DVh3%2FPbdb7X6w1yGTINyjm4oYFBlnegnQ5dZVjEKgoHN6O2f4PhPoSC3F1Vhm4QaYM%2F8sAEgmt8Aqra%2F%2FOp2mX%2FQ4U2clZwOyoSuKpNB1%2FeIC1VTCLLkeDZ1%2Bzn1EEQjoSbnuVG3YPy389Klwr0eRsvyLXzqkzUhBBDF2ZME0%2Bc1MN6A7hBcye%2BpTL7Yf%2BPGCTQ30KyX94Qj8pHjctm00PWHOQW75nKuoDafU63V1RvOqxPE7lgpNbdbAkijaikfYZCRA8eQMJMuv%2Bk%2BuQCW9klQnplZmFaH6UzC%2BieRp9Dyr8aUzZr49Vs5d8rS24EcxTaZMnbEM4tsYa6ikg6QAhJNmaB9keBYJiNY7D1DZvKkCSoVcw9uXkvAY6pgGOBg7KNrrHfWm5DHc3dzPDM9ZV8rulPRAAYIruHlK78dEN%2F5HcU7JQVcZCZyaAO5WRbT6ZBmS8j5ST%2BDO%2BcotZIGfmCFXYrRnY4D9fBvaVvn1A2Q1FiPX0z8u8wtvTp2fOnBthq%2FpMvo6cbTDGO1pnQRs3S6JJb8uQaQZdWGWdRiwVpV4o0MGio0OS%2Fhgiu%2FdFk3MWpyR7sODmxe4vdB%2FrJIK62lbT&X-Amz-Signature=81a6108add158e4bc491fcfdde62e19022b9408d59a397f1f5a16c0789a2c020&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG3KP6UH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHlYvE0cI2vTtvmeTeIwCOyZ%2FMQrV8hYB2uA3MZKfhUrAiAMu%2BMoFrYgOE9xPLsxodop1NP0NBkhh3xY9e5pAquHrCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMemSS%2BFcE4%2FzvK3S%2FKtwDUzdqi%2FG9OiLRFyNtVnXtdwFDLXiS2Inwuw8NWolz6mks%2FNNHEWQLfMokSusZV%2FoZsI%2FCyGAueegGGCbl10J0UEpEASVeXC2eynpKHh1j2Iqf%2BoXmJRcWIXkN8IIVKZBWtNZRFmT71oU0fAQ4ymSrA70%2BPqL2ACg3ujIXKcMt%2Bkyhgn1onEpsSVTuuP92VWk2amSVFiSCL3bVUqi3QWnVc%2FRK2YAVdNIu97XKzPr%2FD58KISrXe5iJZjs0GDcP4u08AwarYFs193DVh3%2FPbdb7X6w1yGTINyjm4oYFBlnegnQ5dZVjEKgoHN6O2f4PhPoSC3F1Vhm4QaYM%2F8sAEgmt8Aqra%2F%2FOp2mX%2FQ4U2clZwOyoSuKpNB1%2FeIC1VTCLLkeDZ1%2Bzn1EEQjoSbnuVG3YPy389Klwr0eRsvyLXzqkzUhBBDF2ZME0%2Bc1MN6A7hBcye%2BpTL7Yf%2BPGCTQ30KyX94Qj8pHjctm00PWHOQW75nKuoDafU63V1RvOqxPE7lgpNbdbAkijaikfYZCRA8eQMJMuv%2Bk%2BuQCW9klQnplZmFaH6UzC%2BieRp9Dyr8aUzZr49Vs5d8rS24EcxTaZMnbEM4tsYa6ikg6QAhJNmaB9keBYJiNY7D1DZvKkCSoVcw9uXkvAY6pgGOBg7KNrrHfWm5DHc3dzPDM9ZV8rulPRAAYIruHlK78dEN%2F5HcU7JQVcZCZyaAO5WRbT6ZBmS8j5ST%2BDO%2BcotZIGfmCFXYrRnY4D9fBvaVvn1A2Q1FiPX0z8u8wtvTp2fOnBthq%2FpMvo6cbTDGO1pnQRs3S6JJb8uQaQZdWGWdRiwVpV4o0MGio0OS%2Fhgiu%2FdFk3MWpyR7sODmxe4vdB%2FrJIK62lbT&X-Amz-Signature=5c8ef8eac5d63aab4c1705e04543282851082c17982791627ee2ba61a11060fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XI53YUV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDpoOfTMfAPQz1YiM%2FSBpVwgKOVANvz0igTZgVQUg%2B%2BOwIhAOIdGGtr9lZmbOnDS8leH0gQecdldEjOBOsImcEbuMaAKv8DCH0QABoMNjM3NDIzMTgzODA1IgzG2fIEpxP7GgFnU1oq3ANV08F0zFNJa7AI71bqCI8s%2Bb1y%2B7e0dbrGdx71BBt0pLTQA68UloIQjVPuvLFLhYnMGfZ35shzU80uuOsgRnHrGfH%2Bmc%2BCPYbGOmYV5jEjG4XVhkbI4UaclrsJVPMqd%2Bz4RoJ89j%2BKzM3zVMwfQA%2B3qB3sq%2FXE8gqLEsJ1wFGApph4%2FS1G6Gt1E78Gs15vn76%2FCVJ89UbrY%2BO5He8wMudnb7O9XSpSq6hW1CueVCIu5yJHBb1b6w43QF8Bgxc3ur2KfrcErpe%2Bih4%2BWYQb6t8zPn1In3BciKYAzRjJuEPo9gTww1F4Me3yEn0Dw9g37waaw7NyJSYwwh8lxpeoHGqy4iePOi%2FbSJHAz7bzwGhvfGZo4kxChpa0l31%2FPqcze4gVFznRPtJ4dF5ahCCPdV3mOzGESqE1PNWNLz7wUKbUJOGtpOoykeKUl%2BhqGFexVxDV%2BUJ34B1AgcnjXU54f1t7DKlGkjKiQCudPUaiSFW378LjXf%2FqnlGO1CETewxyGGQ%2FGmYZjKBRsPEAK54g6DsLqk5%2BcGcCN8CiUz9RKOSeDmCxTyk%2BR8jUApcuePE6b%2FxO%2BP8foxmRma20wTQiOU6t2GeKeX%2FliU%2BHjCmYuIQWoeCW1lRzN2kBBl41yDCH3uS8BjqkAdu5Fn15eoVL9a3QIctBUGYXZVawXkVs03Vo3%2Fz6tbJoEoHgjIxvjTUruGcWkqbGYSRYgpb%2BTYc5vRGr6BUJ8WlDFaFJ6I23gfW%2BKjfRDdi7beGt9GL3M94L1A1tZTk%2BYSufHlZt2iqG%2FqQeY7AfgES5%2BaN8v6JkI936p1MN3caAZD3KKfVP%2BlG0xtb9KRI8cXpNM%2FcHoLnL%2FxBfwT6r%2BrEHSUaD&X-Amz-Signature=e425c2940d6e90348646a747ae6fab22a8b8fdc17b38f7e5b87bcf46603bf2a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWK7ERP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBWA7VABOQ9WFoaRq%2B%2By4cOfvpPkUNUFdEXlm9a64KorAiAwbWxyebZmXDnV1kHQTuP8IexP35bD1H8KpF2rXoanvCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMPvP%2FgOnpOTf6stScKtwDj9x7h9uXQ4jlaEehT9IAadxuBcykRxQeNBzH5gs2Ax9F1Q3BhRtgGpUQ8KGJDLHojADgR2TxdUTCD24bCY2%2Bui9IULPsBF8groYXCHyw3Qw30i31YHRognjXLeCYCf48GgCyyq8%2FLc5%2BZdSQZSxCpq9NsxVUxwhA0L0dBtFfAoXPMPQ4ft1sAZUdgootpDmVh3kU27Ot9DaMCIuhZEuZ6WyWsV7ZPk1grnjR3TBTuXgl3KPtNhqc%2BOy%2F0aNQ0Om%2Bedl3s9wnT3riK12IKzYePqrSrU9CXunT4UU1yReuv4OK%2Fhawfr0QYCOzT3kQutG5GFUZrtgtpW9UmZ%2FC2lI3OhEPqxOswIQ7xX9%2F%2BtQc3Ro1AnZ2Y21uM7AeWRAdhF2ZbYR0f%2FARogpVjj%2FXWsnLRgR5FwWZ6N68e27ktFL3x0pAHqW5uHU14qWMzux%2FCDNwrT9f%2Bl1bDxPBkkguYevsnOBIo9VehCTS8bz3NAZFmMlmiboQFEuTTgnZQdbSAQDlN8%2FrDgNzRaR6rsl3hhV%2BPQmkBF2LWAQV%2BSP3Ubdvk4r0jUMyyOHfTXKSr85luFcTShLXpVd%2BQ515qUSioKf%2Fq0daWF0Tt%2FCjntyO8NRb9EPqkcWI9xJUiNVPo%2BEwnufkvAY6pgG%2B0vw5EhxXimUoWaZAT0Lz1r3B0eVLHagIzAOqoKl4RDwsTZdok9f4ri4k8C0Xpgul%2B4zlte7TYJl%2BTCUb8lKitWWn9%2B604xRSPsNNOcybogQJB9%2BanNpfrMde6ibxxEczNiYKvZxGGUJywe6f3%2B7xKZn%2BfVNWpGXDtF6BrC81CV8WgJpntoldDfcHe1aMrYUiinXI1Duyd%2FJLAhSai%2Fjy2o7RUU3m&X-Amz-Signature=085d81486325999298f87f3e1b6fbc322b5e91d5eefe5731251b22512166458f&X-Amz-SignedHeaders=host&x-id=GetObject)
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