

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=7539d50dde98a71780bc917bdd4f259267ab611db11802eaed5a959fad2bdaa1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=1bc87a3f50682cff4ec82e7fd59615a5d6f8c6c355ab738d8759cffc828855f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=2e34920a693368230e8f3f5364a84c17ce35c2cdaaf2fd26897662111868bc27&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=6153453a2e5ecb92f7a3842af5770d9da55bf1405e190ad1ac54d0a04bbc1402&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=e501462f65b7c61a798122bbd21e6f572387fc2a3a01d5eee5c78fa8bc4dc4ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=8abb1b9c6d88a212dfe86bebfd023549440ef6dc3660732556bd2b4dfc415269&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=7dfee2c21cfa28fe2ce323232324f5289b42c21740ac364d0dd68fa8b9e54958&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=674cd9a7b615badef3240271ecaca2aa4d352cada8f7039108fd89310d855d13&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=e89f30cb6adb58f3484dab4bb143f4869943ee2c28d2bd1a7a7f2b0fe87f80bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF7IOSAR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICoSQfkTbgIOE2hEv806KjMy9NZOdJSyMjVNRX2CeanXAiEArPZfqUi%2FLB2SlNAAUvdFyqbMagDyBn87C4jkx533YDwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBMb6bUrN%2B4AORl13CrcAz4qsx4Tle%2B%2Fl%2BlxULmwheQXc5fIaTA9GVYnCpfnWrfaeo6yTOp3dNEV6WSBQEMsebrSockk15Fh%2BBSmW5e3sre8skrTt6%2B5TEp3%2BAQxeZf1v1G4PwYeZOxQvls1bmn1MBeALSPeyqKPnb0e9Cw6lrtcZQ1W6FFDZW4KSgp%2BagEa4aKbBlg2cDtkvy24iX1cH1xlwB8fhP%2B3MAl2JDJn7wVqngLbRFIhLpfbgVA%2FviJhtzImV8pbxtLN0Q1lerTHT9hn8qTcbqv9m9fBvK9HLMYH2w7N8CM0zjIylkqpP%2B0MYwJ%2FCsHjvgx4LmAPl6QFs0isSLejYjh4hpXTyNKcs74%2B0PDvcbxrSyriNGlsPEAdbg6pdCZe3JcQpI%2Ffl2dPWTDSWcP3EBCuEF%2B%2FImHk1w2khvSn2rh5km2HQ073UxgaqOFDxPsPTl17i1ivkT8WWeRH4RoIBDZJq8i8kh2Rs9LVsN1By1%2F9BTTigyZ15UXvzNGeS6szkBX5bK9C1EvbLAi4W9F%2BkgbLlmUMhAvWQVf87UTA1c5K4BT%2Bk11wMvbD%2BUVKqZ1SeShPqqY%2FHW7geXdhEVdy0q5WQbjdJM8HaGyCKF5evAXRN2vsBP6scW6egjlMMS3H%2FUenRv8eMMHh%2B7wGOqUBDyOEgazIBgGpowtw45R8%2BcKNxMuLCJUI7XO5eKhYZ8Y5gnldS5Nt2RL4F%2FKMgIzlUdE%2BOKUtvglgbTiQYJrAgvQ4x4AgUPycyOiRT1DLUvt2JSe9S3TAcXsjJlu5lK1lHmua8%2FhKN%2B8pMPSJHfVYPFPqQnn1PcNtYDQ4Npur2uAzfKKqfL6kV00FJsUHPjUmUe0tqoTGBXdcX%2FBNBoyyl%2FQb82vV&X-Amz-Signature=4842f305f9c6f733cb040799cff23b98eb5017ea7062ac5fd7f3aad76ffa4e85&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF7IOSAR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICoSQfkTbgIOE2hEv806KjMy9NZOdJSyMjVNRX2CeanXAiEArPZfqUi%2FLB2SlNAAUvdFyqbMagDyBn87C4jkx533YDwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBMb6bUrN%2B4AORl13CrcAz4qsx4Tle%2B%2Fl%2BlxULmwheQXc5fIaTA9GVYnCpfnWrfaeo6yTOp3dNEV6WSBQEMsebrSockk15Fh%2BBSmW5e3sre8skrTt6%2B5TEp3%2BAQxeZf1v1G4PwYeZOxQvls1bmn1MBeALSPeyqKPnb0e9Cw6lrtcZQ1W6FFDZW4KSgp%2BagEa4aKbBlg2cDtkvy24iX1cH1xlwB8fhP%2B3MAl2JDJn7wVqngLbRFIhLpfbgVA%2FviJhtzImV8pbxtLN0Q1lerTHT9hn8qTcbqv9m9fBvK9HLMYH2w7N8CM0zjIylkqpP%2B0MYwJ%2FCsHjvgx4LmAPl6QFs0isSLejYjh4hpXTyNKcs74%2B0PDvcbxrSyriNGlsPEAdbg6pdCZe3JcQpI%2Ffl2dPWTDSWcP3EBCuEF%2B%2FImHk1w2khvSn2rh5km2HQ073UxgaqOFDxPsPTl17i1ivkT8WWeRH4RoIBDZJq8i8kh2Rs9LVsN1By1%2F9BTTigyZ15UXvzNGeS6szkBX5bK9C1EvbLAi4W9F%2BkgbLlmUMhAvWQVf87UTA1c5K4BT%2Bk11wMvbD%2BUVKqZ1SeShPqqY%2FHW7geXdhEVdy0q5WQbjdJM8HaGyCKF5evAXRN2vsBP6scW6egjlMMS3H%2FUenRv8eMMHh%2B7wGOqUBDyOEgazIBgGpowtw45R8%2BcKNxMuLCJUI7XO5eKhYZ8Y5gnldS5Nt2RL4F%2FKMgIzlUdE%2BOKUtvglgbTiQYJrAgvQ4x4AgUPycyOiRT1DLUvt2JSe9S3TAcXsjJlu5lK1lHmua8%2FhKN%2B8pMPSJHfVYPFPqQnn1PcNtYDQ4Npur2uAzfKKqfL6kV00FJsUHPjUmUe0tqoTGBXdcX%2FBNBoyyl%2FQb82vV&X-Amz-Signature=4cf831ae44aacaaa2f23e5502cf59e415df312e2688c9729afa1d9e575bef7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF7IOSAR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICoSQfkTbgIOE2hEv806KjMy9NZOdJSyMjVNRX2CeanXAiEArPZfqUi%2FLB2SlNAAUvdFyqbMagDyBn87C4jkx533YDwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBMb6bUrN%2B4AORl13CrcAz4qsx4Tle%2B%2Fl%2BlxULmwheQXc5fIaTA9GVYnCpfnWrfaeo6yTOp3dNEV6WSBQEMsebrSockk15Fh%2BBSmW5e3sre8skrTt6%2B5TEp3%2BAQxeZf1v1G4PwYeZOxQvls1bmn1MBeALSPeyqKPnb0e9Cw6lrtcZQ1W6FFDZW4KSgp%2BagEa4aKbBlg2cDtkvy24iX1cH1xlwB8fhP%2B3MAl2JDJn7wVqngLbRFIhLpfbgVA%2FviJhtzImV8pbxtLN0Q1lerTHT9hn8qTcbqv9m9fBvK9HLMYH2w7N8CM0zjIylkqpP%2B0MYwJ%2FCsHjvgx4LmAPl6QFs0isSLejYjh4hpXTyNKcs74%2B0PDvcbxrSyriNGlsPEAdbg6pdCZe3JcQpI%2Ffl2dPWTDSWcP3EBCuEF%2B%2FImHk1w2khvSn2rh5km2HQ073UxgaqOFDxPsPTl17i1ivkT8WWeRH4RoIBDZJq8i8kh2Rs9LVsN1By1%2F9BTTigyZ15UXvzNGeS6szkBX5bK9C1EvbLAi4W9F%2BkgbLlmUMhAvWQVf87UTA1c5K4BT%2Bk11wMvbD%2BUVKqZ1SeShPqqY%2FHW7geXdhEVdy0q5WQbjdJM8HaGyCKF5evAXRN2vsBP6scW6egjlMMS3H%2FUenRv8eMMHh%2B7wGOqUBDyOEgazIBgGpowtw45R8%2BcKNxMuLCJUI7XO5eKhYZ8Y5gnldS5Nt2RL4F%2FKMgIzlUdE%2BOKUtvglgbTiQYJrAgvQ4x4AgUPycyOiRT1DLUvt2JSe9S3TAcXsjJlu5lK1lHmua8%2FhKN%2B8pMPSJHfVYPFPqQnn1PcNtYDQ4Npur2uAzfKKqfL6kV00FJsUHPjUmUe0tqoTGBXdcX%2FBNBoyyl%2FQb82vV&X-Amz-Signature=863f85514d3fd9be09845225bfe95cd7a9e12b6d826af5e00df3cd2fe7e02f11&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=5fb741cc964a32869b479a4fd6c5c456c86adca2b07fcbac1c9e15bd40fe5b30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=fa9906235ec31b10585399806edd2b4e9cca20a67753f6bedfd40dbcd7918bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=d90049b6f5438efd784886e8a9de27b4c0dd610e7f900faeb73a66fc2f99e847&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=9440d7ecc6b73bcd60d176979a7cced5270bf91015f31d0a45b3ef68a061a49e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=75418231f634182077755b45a6907c6031bdb78a3225b9155486d0f00284d276&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q5YWOVX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEPxMoV%2FiMkAPtIntdMSG4DeFVM2BPJk6FalglW5y7bMAiEAib3ozItKFn2ZPn5%2BqwX70r7TNV2W4gOlYHFu%2FzBFeywqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGb0Fv0mvRGgFJVyyrcA5XTCq663faj%2BsCpIQXxKqy1qVU13o8i27uJ3wa%2Fvxe80R32mcPAvksgUaU%2BV7IELdj6ucKxil%2Br0dPSGXn8GeQKElTK8WyHMGe6zwj0HgBNbDO2Jq0e6HdW1yv%2FL5jM0FMSohm8eHz784CjQcU3gJTS40d2vraRDwcYLF%2FM1tuxumUduKSjV7cVNuQNB7azBV8a872V97nZ1ca05N2Kuw4FVkI4tMQWr85aLBPcNss2KUSKhw2LZWizpPDhLq9dXTL1eyn7NLsA3HqmHABp5dWCEqRQeV9hdpDyfSXJ3ng2r6O3AtVHS%2B%2Fww97k3bhMZvBXvoY52MP5vWnq0TQwcrRDYO%2B%2F2LEGtVW5bLrsKI%2F47fNfBDU%2FjFBQK3WbpSotelMwvY8telVM64TsvlVXeJRf86D8btchqT1zbdGaeNSy4zkTuZKzAFVx%2FslV4Mi0MSg0sZfTEsOV5KhnHt2Vcr0cyEO99valRWn%2FOS2NMR8mtMk8FkbhCSO5ODNd2z6HAtAGQrLvqYKWY69D%2BN0VTGZCgtTv0RlNHPRJ0UJmJxu1FsL1XHmqvmdH1u0RTKbxk1BD4oGbxA1yjB%2FEFT4W3hhyYhPaPZAw5hmU6IqrCRiqa5CIzdu7fZe234eKMNDh%2B7wGOqUB2lMBAtkxdrCed9os1NS7pttopEUhKcOAd522wZGjnLOdlQNsDG7NkWXqnS4uRt3UZZKBMSeJnHBmBFq8ko6Z4VnnA1jZLtHQeodDc0HF2fDxdDZ6lQJSgybYL2BJjpTP7hill8SNWPnh7CfaRo%2BfRVnVdICORSXpqF3hDnEVjFGYNo8%2FxX8%2F9Q7RhXl2DRVyVmznFBW9jX3ORd5XdeMMRana6D%2BO&X-Amz-Signature=be7cbb6002ea3127e64702874ebb7da7a97d8da6f2e99047488bced87104d08a&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FMRALOL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoUn6EXvEIJR%2FSdw%2B43D0B6F%2BVVTX94lYN8kHSdOPCOwIhAPjdjZZeLtd8B4CzyZITC0XUmaxo20ZAlKAyWsI5d07KKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYMjUpHwqiJPyeGicq3AMRCKcoQSlqh6Rb5ihD40Jy%2FYhLaEpEaI%2FnUQQJTNg%2FbY6pyQ5xcrY5MdCdFwuQhzhLBh41Tz4VQmWQ5gYxz%2BzSX%2BiXmO60s3Jx5nBwj%2BKgF%2BKpudaAee5w0D6TyvPROQR%2Bpo3tfrMxKZpDBIdp1weCcS034jtQrT8ajmOkv1fqlb0g24G0O2W5TLRI8JbwEWyt6yFZ%2BzxJX8n6Tf%2FpnMMnOdesT9ivlbUsXcM0KSsWVcugSbOQiLwJYWf9PgSNCpwrPin8li4HEYEeEi2DfWjd0ia45Ks94CayaZ8SNqqoa6kEhCNqHO7qYGArptyW%2Fn4a8kGH3xPkFGS1A0fDJBLfiFpHr9b89tOxFwPROPCmW2pkIgdXRjUqyeRYQCg0uVadHFPIlCq%2FGwCDYkIlRMGasi4n2OBadmUJnZ5ZKXGhGSFvde%2FyGO1N1TP6dtP206o8lNUqgDbLidM8o2MBFUbOHuuUaLFw8gd4Z9%2BCT%2BHpHR0oTD45NVxpl6uKWOOeW4qciya4pClzhzbA36zz5J%2BP0CQ4pv4qNS7lU9U49Bj1xN1bU%2BMgw4A12ZGwo8e3EEEgUsr0AOoegaF1enqZJOM2yfbOQ58kFq0ytTSKj9%2BdjBT3qbiF6h17MTcavjDO4fu8BjqkAc2fISQOHXNutCH2B44%2FbvFOdc404ouqjslCkX%2FyPzlL3MGBGREz6kmeFoy7LKR2e4Vn3vzs%2BkqyPWwo2owZbCKpal43BjCMt1Pw8QBYnF3tguZ4baa54nkWV1RnjcAQr%2BFbmnQ33hVjU%2ByqKflaxQpGslO3B9IH472GvObDevgmsmdVrE1Y%2BMKspaXIYxjklouIl0UQZSKQE395fwaZrdoiAffy&X-Amz-Signature=6dc1d44bed9ae322564cafd30b7cf4c6d950a6033d9cf87ad7a788ca24c86436&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FMRALOL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoUn6EXvEIJR%2FSdw%2B43D0B6F%2BVVTX94lYN8kHSdOPCOwIhAPjdjZZeLtd8B4CzyZITC0XUmaxo20ZAlKAyWsI5d07KKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYMjUpHwqiJPyeGicq3AMRCKcoQSlqh6Rb5ihD40Jy%2FYhLaEpEaI%2FnUQQJTNg%2FbY6pyQ5xcrY5MdCdFwuQhzhLBh41Tz4VQmWQ5gYxz%2BzSX%2BiXmO60s3Jx5nBwj%2BKgF%2BKpudaAee5w0D6TyvPROQR%2Bpo3tfrMxKZpDBIdp1weCcS034jtQrT8ajmOkv1fqlb0g24G0O2W5TLRI8JbwEWyt6yFZ%2BzxJX8n6Tf%2FpnMMnOdesT9ivlbUsXcM0KSsWVcugSbOQiLwJYWf9PgSNCpwrPin8li4HEYEeEi2DfWjd0ia45Ks94CayaZ8SNqqoa6kEhCNqHO7qYGArptyW%2Fn4a8kGH3xPkFGS1A0fDJBLfiFpHr9b89tOxFwPROPCmW2pkIgdXRjUqyeRYQCg0uVadHFPIlCq%2FGwCDYkIlRMGasi4n2OBadmUJnZ5ZKXGhGSFvde%2FyGO1N1TP6dtP206o8lNUqgDbLidM8o2MBFUbOHuuUaLFw8gd4Z9%2BCT%2BHpHR0oTD45NVxpl6uKWOOeW4qciya4pClzhzbA36zz5J%2BP0CQ4pv4qNS7lU9U49Bj1xN1bU%2BMgw4A12ZGwo8e3EEEgUsr0AOoegaF1enqZJOM2yfbOQ58kFq0ytTSKj9%2BdjBT3qbiF6h17MTcavjDO4fu8BjqkAc2fISQOHXNutCH2B44%2FbvFOdc404ouqjslCkX%2FyPzlL3MGBGREz6kmeFoy7LKR2e4Vn3vzs%2BkqyPWwo2owZbCKpal43BjCMt1Pw8QBYnF3tguZ4baa54nkWV1RnjcAQr%2BFbmnQ33hVjU%2ByqKflaxQpGslO3B9IH472GvObDevgmsmdVrE1Y%2BMKspaXIYxjklouIl0UQZSKQE395fwaZrdoiAffy&X-Amz-Signature=232fd3d1cc9b00fc5960a1e1a155a4031d2dcac00e0c31fb31c4ea5a5a31357d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WCZCGWA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHUQEANKs1gDGN0eHEKWIWNqQtKNwzpZ9hfEZI1sBHtAiEA3CoKaxnpvCdKRtaS7%2Bb0cmefLrbOzO3z1tYRRPK9uVwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9sX6J7s6AThGcpLCrcA5ltO57U%2B9LuvXBI3IjQyI0N7staLTlm%2FG2gH6hHMLDB2sAcwyPRLyUmI9JxM9B9v4QmhhnpE1y1mmcKt54bYzIM9radE8moso4cBXW8l0pnnRwVgK0h5z1tlUDJrx8I2xrekzzm7xEJbt0j2DwPs9GEAn4gt5cjBVSHotmWa2TSkkdko853b%2FlAvJqDpcsPa1QVNfB%2FbJk7g%2FQSrMNjCUw%2FH7jzUdQmyHMAT0LwNuV5NxyOv98IHnwHEOymm%2BNKwh4FBErBWqVFI%2FPTY7XWN8nv4jXBS5OQi3K3uvzBDL8F1jBTko%2B5yG9FNnsOfz%2BLhEqjcOOQ85EkpyalpmBTbn%2FL4Z5EJXgMoBpbcUpD32ZBPbHN%2FKaCnXxEyMwdG1NvzRubEVYfdia2UHFHaZZz1kH7khKsThPMK33mmM3GvlLo0PBASfYUP12dDvnt%2BT1DwAPuaE5JGu85suzF6drHdr8MvFjGP3tqn7zDq4z2aD%2B2Ck1t%2BUvpvrOba%2FBvQBBGfKgP4TmSYYTVnWrwJj1YXDqO5K9ZoL2MtSzbPbjm5CR5PC5Y6%2FbJfWLtGh1hCh64zWOU29CHpDeNyQaQ%2B%2FLjnT7hU2Fh8xDbJn4q1aAVwiYh0MVC1jgOM9Q%2BsTqxMIHh%2B7wGOqUBZNIVhMl1ATblCe0Rremdn44h6pFXUrSuod4pj08tGrSlhC1wu3GvGMTjgmvdf%2FLYppjXIV97ujy7wG1Rr8E5c5rcFgIbkh%2BbDx%2B7kuer8iTKfiY3Hb346uPuTU1akM0j36%2BSycbLSnKVgPCLs%2Fkgbwq5ZdD4Lh0kKo9NyVbLjby1x4pb5OPDHZiusDZdhxQ5rKch09LaXiGwRl0soueQV6T%2BzkP9&X-Amz-Signature=77a08020ff8612b71499b790a855fc3602651b83a7d9f0b4b076b26794f555db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP5U6QSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFJTrN0iZfw7veaUaVFF78SkKvnFolAVxnb4lbIuUDgIgAQmNe5klkeNvhIGheOdvTSMpz1aXQHbubCZ5FVq17f4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3BZMgNicA5ufmyDCrcA970koX4ZyYWfN1kGe%2B5Li5umYrfBPI%2BJ54HGcN8y1Iha7k7iUEl89duB0oUBj6eVCSdswd7Ql0sS3xDGvjLixWLy0pUl994RC31O6GMbS9XILyADtyHT4noDu%2BR3du%2FMFDfxZ7X89hMUIQqOhxGAXe1MHaqrJiosK12%2FNXNYqWYX6FGn0lyuXklwQV0sZVTHgkoKnom0hzm4CuXhYCV%2FHEPUT1KherXBdtBxirGqN4AZ%2BO%2FWRuwklt81R5WVq%2Fo998%2B3sOx22bmm0E8qGrLrNQS79jvv6MOW9DTvNVlCWopT1GGdjQJkroV6I81VRInSA8F0Pb%2BruFcmB%2BIFh5fSqeclwIPydFmn%2BQwUDyjlMr7Nrv%2Fz2DSwiwEgRn9jAyrr7f%2F9UyEtRwo5IjWyxfBHlEUSa2ReKNS38%2BtDirWPbzyNPiatXYhZrla%2FtsZdQ8lYytp8zLj4FMPt8959AfDS88d3XjcWRE%2BwnF0JVEB5bYIzLsQYzgZtkLCynr2Pu0WWZoMVhkBOx3coRGWAFSL4Dq0JJyne1BKChU%2F%2BxHTDCgsoJyasaD53dVii0gK95H6nKufRCkl1M9IOR8X7Y%2FcfNtRqc4CaBpztLSAZGOVIrTao7uanpEIpbfxNtGHMJfh%2B7wGOqUBqKAJedjRAj1hLRNyUY4RIA8NFPasGj%2Fdj5zw1woOJuuAtDmTB2lNgzeHDEleKNuO2jVPMbmsOyJS78%2FfYZly%2BxjNq65Svf4Vg4i2VVmz1MQwL4XPxxOrLSn4aIlVl3d4luigLj%2BHUFhdnT62U259Ngu4OE0nLzaTU14SoE29ly5NSVU056eArA743yAMZlqizDRhGyEyR9BLdfYPk%2FrXscZO%2BI%2Fp&X-Amz-Signature=fcfb4b4f9d70650562b6120b01870b928de4a71edfb7f66cb1e8f7d66fdae0f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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