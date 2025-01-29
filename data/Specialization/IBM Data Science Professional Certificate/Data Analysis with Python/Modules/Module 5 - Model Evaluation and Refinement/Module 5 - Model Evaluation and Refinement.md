

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=1279803e998ec9168c8cadc35a4f31994769c64e4f12906439623b1f4b511f00&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=b567b08236a3644ac41b0f29c847c3f1d56b24bb84d99d4011cf726eef0b38ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=d8abe026251641501f8faa258c66d77c9af61ca98fcdd7bb23725dc4fbe6fdad&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=f531acb0e968845829b61961621eb242d15e4d7b29a97ebe0e87a77742b9b9e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=6509a9efeef461f529df1ac5322041a9defe402ff3c699214ce30cf3684640dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=caf44c917d24d23482a81024bccc2c494ae77f38e3a1e4be005e684eaea333d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=d80a97de37abfe26d81476c5351a90ddfe24d6db08c430caf20742655bc3ea25&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=7cf972cde82e8cb4d8c591cc5b036f2b315fcd412f547490546e7146ecde2d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=408d0b8bfba9f620e087c391a26e503d25a3f948c8ac0c0e5409f1de645b5ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIAILI4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnmkNYiBEkMjAc6zzuJADzXi3giF%2B5ox3DG24EPE7RdAIhALbHWHEe%2BRm7yelXXyR%2BKdJfHdsddL9dD3e2wAewf9oqKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1NBjrKguBJwkfaFsq3AMYspDbuxARm3HoouVAT1gupgFOTRCyzgSyJ%2ByZLfVYJLexz6849ng7I5pLiOf4i4VxtZV7kJ9TtHTlCyWM2mGqbhrlQEMSMAVhlpLBayGZ4Pz%2Fr6IPN4MZhUEeLA1xVTYGCwzgtVLshmhMM%2F7mUwZC0q60Ht8vEIcmrqrPdny9R3UJ0urmKKsgUk5htcB3SnczL01dKVcOO%2BwmbN%2BM47hs0F0S5tZqcUohmbQiZ0cUskO5kDY6DwDA94%2BFMbDlZXJ70xlR%2FopCEqFdI3p1SaEl6q%2FaU6R8rXy3eiSgAdKCpHpoOdTdpImneZnFE6KH64Ax3awkxhzH31jg%2FqM4DNr9403cLLcY5S3I1%2FuHcftmSc75rR8OmHsPghtHsz8OfjDFOOfW8G0LVAGPEiv0ssKqt66hGI6D%2FR%2B8ffmOoxKJ%2BEQn%2BWol%2BeKXy8kSa2OwMOFqY7byFwCuOfRw2OCL5Pf8qa6h2AnJfjPoHDPoN%2FwPunj9aqb8nGvoea8M3nZkXQvFSG5LXLiIHUPXoapllZyMekOWkXf%2FDsXCqDvT3inlgPpEv5Y6XtVHMgB72lGqMO96tyfaWmZEBnNycqJlHdKSRGr4zHiM5hlTPQWicYnRjm%2B69nsbp7plM6z3cDDVu%2Ba8BjqkAStNW2SwqvJYtJo6yw9SyYL47BNN7znON1L46kdHiLmp3DIvKejWSih3OLsA%2B6RFbxWPrYjgBi415KjBfQMNHm88iOOe0OsYGYSThng2HN2d9vIjtwTPJZuIfiAqTqsmWHJslQFSpnD8rt6GsKpvmq%2Bj%2BNH1rvcOJP1sS8Grnfzbn6qma4bY4oDsWhEX03t%2BRBeNRMkEuPr6OLV8KWidLPY4O6gg&X-Amz-Signature=4e44b6dbd6cee35a053455cdd090443427c908266c06d471c500e58ffd9d3b15&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIAILI4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnmkNYiBEkMjAc6zzuJADzXi3giF%2B5ox3DG24EPE7RdAIhALbHWHEe%2BRm7yelXXyR%2BKdJfHdsddL9dD3e2wAewf9oqKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1NBjrKguBJwkfaFsq3AMYspDbuxARm3HoouVAT1gupgFOTRCyzgSyJ%2ByZLfVYJLexz6849ng7I5pLiOf4i4VxtZV7kJ9TtHTlCyWM2mGqbhrlQEMSMAVhlpLBayGZ4Pz%2Fr6IPN4MZhUEeLA1xVTYGCwzgtVLshmhMM%2F7mUwZC0q60Ht8vEIcmrqrPdny9R3UJ0urmKKsgUk5htcB3SnczL01dKVcOO%2BwmbN%2BM47hs0F0S5tZqcUohmbQiZ0cUskO5kDY6DwDA94%2BFMbDlZXJ70xlR%2FopCEqFdI3p1SaEl6q%2FaU6R8rXy3eiSgAdKCpHpoOdTdpImneZnFE6KH64Ax3awkxhzH31jg%2FqM4DNr9403cLLcY5S3I1%2FuHcftmSc75rR8OmHsPghtHsz8OfjDFOOfW8G0LVAGPEiv0ssKqt66hGI6D%2FR%2B8ffmOoxKJ%2BEQn%2BWol%2BeKXy8kSa2OwMOFqY7byFwCuOfRw2OCL5Pf8qa6h2AnJfjPoHDPoN%2FwPunj9aqb8nGvoea8M3nZkXQvFSG5LXLiIHUPXoapllZyMekOWkXf%2FDsXCqDvT3inlgPpEv5Y6XtVHMgB72lGqMO96tyfaWmZEBnNycqJlHdKSRGr4zHiM5hlTPQWicYnRjm%2B69nsbp7plM6z3cDDVu%2Ba8BjqkAStNW2SwqvJYtJo6yw9SyYL47BNN7znON1L46kdHiLmp3DIvKejWSih3OLsA%2B6RFbxWPrYjgBi415KjBfQMNHm88iOOe0OsYGYSThng2HN2d9vIjtwTPJZuIfiAqTqsmWHJslQFSpnD8rt6GsKpvmq%2Bj%2BNH1rvcOJP1sS8Grnfzbn6qma4bY4oDsWhEX03t%2BRBeNRMkEuPr6OLV8KWidLPY4O6gg&X-Amz-Signature=8b8bf7f4df048cee3c048d2665debff864521d473af9bdbb5f5c83468a3b08b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIAILI4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnmkNYiBEkMjAc6zzuJADzXi3giF%2B5ox3DG24EPE7RdAIhALbHWHEe%2BRm7yelXXyR%2BKdJfHdsddL9dD3e2wAewf9oqKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1NBjrKguBJwkfaFsq3AMYspDbuxARm3HoouVAT1gupgFOTRCyzgSyJ%2ByZLfVYJLexz6849ng7I5pLiOf4i4VxtZV7kJ9TtHTlCyWM2mGqbhrlQEMSMAVhlpLBayGZ4Pz%2Fr6IPN4MZhUEeLA1xVTYGCwzgtVLshmhMM%2F7mUwZC0q60Ht8vEIcmrqrPdny9R3UJ0urmKKsgUk5htcB3SnczL01dKVcOO%2BwmbN%2BM47hs0F0S5tZqcUohmbQiZ0cUskO5kDY6DwDA94%2BFMbDlZXJ70xlR%2FopCEqFdI3p1SaEl6q%2FaU6R8rXy3eiSgAdKCpHpoOdTdpImneZnFE6KH64Ax3awkxhzH31jg%2FqM4DNr9403cLLcY5S3I1%2FuHcftmSc75rR8OmHsPghtHsz8OfjDFOOfW8G0LVAGPEiv0ssKqt66hGI6D%2FR%2B8ffmOoxKJ%2BEQn%2BWol%2BeKXy8kSa2OwMOFqY7byFwCuOfRw2OCL5Pf8qa6h2AnJfjPoHDPoN%2FwPunj9aqb8nGvoea8M3nZkXQvFSG5LXLiIHUPXoapllZyMekOWkXf%2FDsXCqDvT3inlgPpEv5Y6XtVHMgB72lGqMO96tyfaWmZEBnNycqJlHdKSRGr4zHiM5hlTPQWicYnRjm%2B69nsbp7plM6z3cDDVu%2Ba8BjqkAStNW2SwqvJYtJo6yw9SyYL47BNN7znON1L46kdHiLmp3DIvKejWSih3OLsA%2B6RFbxWPrYjgBi415KjBfQMNHm88iOOe0OsYGYSThng2HN2d9vIjtwTPJZuIfiAqTqsmWHJslQFSpnD8rt6GsKpvmq%2Bj%2BNH1rvcOJP1sS8Grnfzbn6qma4bY4oDsWhEX03t%2BRBeNRMkEuPr6OLV8KWidLPY4O6gg&X-Amz-Signature=801589d5b916d4f37bf2121062de9b07bca7525dad9ab23d5ec800d079127b2e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=cd5b9b3ed9aefdfdf3de494f77c987b54a85ffe1ca3fcc48145187797f32ccec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=b9597467d2c2e581c4dca553b49e810c3bfaa150fb71dcad4bfc81b3331bb55f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=80d37a07e6d0da961c39e70217ecfd97dfee79c8310c4e5ef93d8c7b84bd75d5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=139d99aeb6c1f8d5c66ab8c771d4bc7ce7f13a39b91ad7b716afc4637337e9a0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=7f88f0059e5f6905551b947434e3f69cddc3a9ef480862b0e0872310988f30fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBF2T77H%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCU9EB%2Ba35NF%2B2nOpHDSNQniQGOdDJnKruQVAGXJyxjxgIhAI%2F30dPecIGdhySKigSm7nV%2Fas%2B7UYor%2BkmyfiaJfBnYKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2B1T1ILgdivq0IxbUq3APgqaXuo4tXNSHmXHUjqS47VbEILYg6z5TBpO0WQ%2BBbf%2F2Ry%2FG%2B9rj1eBbrZaA2IbBdvDxf89keH8T%2BoGfL8UyuAMIp6O%2FOXc%2Fcc8FwVW%2F52fEBkp7%2FeqA9uKEbsWTr6XR%2Fq6Ltl0uzafTsEmYsGM8Ngt4%2Be0Lzf4LB8%2Fxl0vrrRdtAt%2F375qmQ9kAlJaq2KRf1of1%2F619UWpm4VxmAn60sTig97e99ubJMqgBLKeEWby%2B%2FNTeZ7BVFKo66sYpV5aMgxwPTOpjdcl1OsEKWUYH%2Fr%2F9yEjc%2BEBW3BKelYCNZnlEpKgHrx6LZ0phzYw%2B020FIsJJaUsoBM%2FZBoUlYzzzgbSA1TXzDD%2B2U3nbrMn9K%2FUmAAb%2Ftq%2BKpALQ6YWkN6vtmJ8%2BHykEM%2FpxTZ2cYVVrN26vBGLFTH9xTsDARdATr6Fd%2Bdd9nRyv1Un7cHbxmOzl33cQT2q3qkDVYwf%2BdF9GRM9jhYR0gWuM92Rk3pmogHGSw%2BwuFhFH4ZzZm5WcawTKULCLR9eURXhWM7zwuX5DhnCmEsjaIyk6dnuPQtRas1z%2Fqs2C%2Banev2%2B5eDoHntXXW650ZKzh51iKE3h1d%2FsX3MyUiLoXH7Q%2FkxRq9xwpjKCwTaAsw9lZpRRlbXTCIu%2Ba8BjqkASBFw4LZXDb%2B0jxekMmLfuppHFItoCc5KNMBillSeebTAI%2FY9Q0bdxUdddZO9HJpGwKMZrIGBCJlLhDbqd6dENP3SOk9BXDf8vsdMBq9huGdxgtqQK3wsoMvOchmlWHM2EkPd3fRtMLQAKR0XiePuqDzTb6M3HV9Osq%2BhYZ6su0B0LCSniodEBzOuyp8AnaK7wINfOFH2bx9U%2FHfQri9fgBW20sh&X-Amz-Signature=0aa72f8218ef2e8f3ab67e23f81f75dd81e0435dd0658342e8bc1be7fc76934c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JP3AMLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIGRh9KjxSu6F%2Fhy1VZB7fMrvWkQMV7Io%2BMXSKxA%2FEiUpAiEAye1NQH996mj73eldiYKwXgp4oX1wCby0Aru8OJiQg2QqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpGcVEILlIBNTzfSSrcA%2FiXZHwsRpQsCJz51VkdEOUmuw1mA%2Bvw0rvmNbYZzBFFkyx2rDCrKKb3d5%2Fxp5gjzQW1JcDQGAqOZ0cManf724T0bhqHjP6ntJvI71O4t%2B7W4W6lUW4Z%2Bky9y4dUQyJ7ZkxZLotTUh7PXBaEkowbnFwIIn%2B7pbIIOF1W%2FuAezQ%2Bl6tGcEUxkPEB08hYDz5lelyLrfHrxvcoTHI7napgOAfbAgRagu5lRQzALUZVPQ6X%2BZdzegQ5ILa%2BmYBpkGZzQHV1ffYN1N8Iz9byeobsEpFdo5QOXAqgFmvB6y5LlYQyc%2BzIwVKhlVzUQxB5CL%2BHO9WaGtRhXWkHQMD%2FUfx2ZtLsMakG22bRrwsvKcA36D8fPs3gl0XWmgtsus6%2BI9AXdtFR%2FC9cjJDF0ZRCcQeZuYKiOFNC9XzO64Kf7O1EqAW8M9IDjMC%2F4U4WbFf5SXSsKccnDb0gwCgB9F3%2BDFJitV8GZMqaeD7wJE6bJNIUQ4tBP0weoEsyPHjYzB6%2FYaemzx3jErhBj4bfIXmQ%2BETyZVdOdjTABNYLJ4Hn%2F7%2BZyVoHihLgPJ8K%2FWdarFBwxqUYo8jP%2BiRPe6NSvEVnTr%2FUGOGVOp3oR1pORFjIwo7CRFNWhuOT0rP5lMLvRh8H%2FMN275rwGOqUBGiOHVo1wobpKzLy5wTseHmwpFyWn4dCuauBHRAsOIrfPV5flUahIkzltTnRTdy8O2aA6%2FIYgC5Y6aDWooZH3kRs3ydoKH3xJBsqoKkB3nKSo0eyZsJ0zU0JuFSBg5K%2FkYp6vHrUGtO9TvS84E%2FM%2FquGZ%2BAxDN9qj6qfKdQz4ZrUoC0%2Bzg3YPHSuw4MynFxJ1FtkOMxuhA1a0GxmFw7zqZR%2FX%2FPCM&X-Amz-Signature=369d3bb4c9557cfeba867778862a6ddc3b547f50d35230f1b687c26485ff8b55&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JP3AMLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIGRh9KjxSu6F%2Fhy1VZB7fMrvWkQMV7Io%2BMXSKxA%2FEiUpAiEAye1NQH996mj73eldiYKwXgp4oX1wCby0Aru8OJiQg2QqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpGcVEILlIBNTzfSSrcA%2FiXZHwsRpQsCJz51VkdEOUmuw1mA%2Bvw0rvmNbYZzBFFkyx2rDCrKKb3d5%2Fxp5gjzQW1JcDQGAqOZ0cManf724T0bhqHjP6ntJvI71O4t%2B7W4W6lUW4Z%2Bky9y4dUQyJ7ZkxZLotTUh7PXBaEkowbnFwIIn%2B7pbIIOF1W%2FuAezQ%2Bl6tGcEUxkPEB08hYDz5lelyLrfHrxvcoTHI7napgOAfbAgRagu5lRQzALUZVPQ6X%2BZdzegQ5ILa%2BmYBpkGZzQHV1ffYN1N8Iz9byeobsEpFdo5QOXAqgFmvB6y5LlYQyc%2BzIwVKhlVzUQxB5CL%2BHO9WaGtRhXWkHQMD%2FUfx2ZtLsMakG22bRrwsvKcA36D8fPs3gl0XWmgtsus6%2BI9AXdtFR%2FC9cjJDF0ZRCcQeZuYKiOFNC9XzO64Kf7O1EqAW8M9IDjMC%2F4U4WbFf5SXSsKccnDb0gwCgB9F3%2BDFJitV8GZMqaeD7wJE6bJNIUQ4tBP0weoEsyPHjYzB6%2FYaemzx3jErhBj4bfIXmQ%2BETyZVdOdjTABNYLJ4Hn%2F7%2BZyVoHihLgPJ8K%2FWdarFBwxqUYo8jP%2BiRPe6NSvEVnTr%2FUGOGVOp3oR1pORFjIwo7CRFNWhuOT0rP5lMLvRh8H%2FMN275rwGOqUBGiOHVo1wobpKzLy5wTseHmwpFyWn4dCuauBHRAsOIrfPV5flUahIkzltTnRTdy8O2aA6%2FIYgC5Y6aDWooZH3kRs3ydoKH3xJBsqoKkB3nKSo0eyZsJ0zU0JuFSBg5K%2FkYp6vHrUGtO9TvS84E%2FM%2FquGZ%2BAxDN9qj6qfKdQz4ZrUoC0%2Bzg3YPHSuw4MynFxJ1FtkOMxuhA1a0GxmFw7zqZR%2FX%2FPCM&X-Amz-Signature=9eb15ce091daaf43a0ac5ec1fcebf3d3c6bcb1db9ac724642a4eab201f8de28b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXGPTGZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHLfhMnYu0VlVFN%2FOnsUGArUjkKuXypUD%2FRo9u%2F2Mv%2FKAiEAqmIvhelbjsEQU4mUHMnNTxMkEKJQuS%2FprJUHdDnDwy8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYnHB38OB2ZAsKimSrcA1OeqShDitO2N%2BAk2yxpzU5Zi5BjyhWwgX9Lp3%2FmjCjEUXdLxcsLkNUgdNjDE%2BjGIL%2F3jOlfN9NqxVtdWAyTHEKzilwiVhU2XiU3p6H2K54%2Fp7c3rK%2BC5JIHh%2B8nOntg3ojTD6vRBcD6UvR8GsrsV4YoVfWRdY40AavEFxVluCUMG21Y%2Bi1jQBex510jPZHwvjlbkt7E3xRHXVITbiVLBoCPWHBDqr4%2Fyd1BXsRBykMBgHdtieVjd7Hddvt6dJnHXNRyLNRUx9i9aGuDEy8hO1C8PuAPKPGEqHdQwbGaPxMTUBX9n0on4ekcLjAp%2B2yEBF27lm9Oz3Yy8nwNsFLgM8GDfp6Po5pPNqGEpFTWjnaO5sCbQwie%2Fxlyq%2Fz8S38ph2i2U%2FEQ9%2BUEeaGXXEeHTbP6uGObr8l61FtTHnGBBjq0A0E665kqmtA44erxCEnaF4zVJ%2FXb52KiS%2FlZB4LGH1LP73JTUkwUquB4wAD3jRRTAL3LoDVTVD3xaZe6sXeUavDLuyGkVvxO63T8gtO2WA8OVT66ch7NIucNm1trmcaf79RZr88pGfZDMFH%2BwHtgEFWfxo04Uh0qpQNfGSjuwOpXnDVEsWmmKsK%2FHskWNBzZKZKRlw8%2B92sUxlxeMP265rwGOqUBY6i%2BujfVUjFNr4PQKtRq0nX56ru4Hwr9mkGJZ7dySSjLIkxnuipUdqUCD%2FoXWZIjLKHln6UK18nQ55IUnM6o5Ixio3D3vWdCQo1t2tsZDD9Pb7M3AObpBUqoSHIzIwaQhZm0rwpSXQgyfs6jTxgea1dgBhEYti%2Buu8Zuq35X2d%2BGrlU3Y5sQyaHK8Uywr6lmf8vqzh8IkTjYdDX1K2xi3WUzg70f&X-Amz-Signature=c07b6357bb03ba67199cfe0747ed2b45f00a36a91a9dcf5590127cae38b20016&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV4ZXTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDSzrxTa3Pkap2d9ByKDZaDZCkFSE10SCOwN3nhos758QIgXj9RiIjYkhNZ2kWPKjUm3kPz3FKPavQ9INTt0a%2BN7K8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF3Y2rWkXaoATbhbyrcAwM41TplJeNh%2BV2sNOmFfX%2FPvobvNFEsAbF809hTVN%2FLAPFtMtUVu1%2BxJn1P8XaW6%2FLoS7AVTxbE014EnCCno6mwuz5SgvCPfAA20lEf2eN0KZB87vJ7kJ2sbF6jezOOO5Ka0AtS1YbUUVmObs6tHn3Hu1t1rrcbEzcq1iFNzbPKa9D1%2B4Wu5RMxv1U2MMuxe6qzMOoj1C%2FPZdydZwshL07X6KAibxXsdYxUJ0V9EiUUmSxKmrFyNZWNG032UUGt2Iv1U9TTQlvDNOsfIqvhnwH7LIkmaN5yoKil6m4SyjnwwBXmaQ%2BnavW%2BT64rbwOfEAVhEgxF6KKeXn7XxDRB8RyBPlIJZwPXHmjI5nN%2Fjr%2B1K8kmYXrMaoIkD7McRwMmALNAda5GaUlaqeSJ8oyG1Lpdl6jEVMl%2Fu%2BonZxNtNDcsOqWx77DPbC967VOaj6HeIs%2FtBR9oC0H7r01%2BnKPVnCS3AJW3TNNR%2F%2BAZMxQH6Z8dc%2F%2Fpd9xsPHgZU63KM33OWk7lYM7%2BQ2OLWBykZVs1y1q6B%2BePkC210wT77aGB1AHPie7IsoGuwyvqIXE2tfpFqbAAaIRb%2B3dbLZ9tQlqJ95zSQWwt3N4zN2wWk%2BKdppbpXRCZreJZfWMHTfIfMNu65rwGOqUBRea%2Fq7wORhO0GGiareUOjobmH5OOJTwlGxzEs%2BWWMry15LD6vItoNyLLgvSNbJBtgMJn72KC7FJD5HUXok%2FXOkXLD5SCO4oEi6cOjtzwMcjSLl0zzVVxaljkSYsS%2BCwWgCoEElcC7FSj9H83OHSupZWeAivvBb7N2mYOzSGeVoEiHriG03e1el4YficxvpceijdqRvshtxYbe4T0mGE1naBYLc%2Bl&X-Amz-Signature=893fed69af49eaa03d41b710b32155989a3ba34dc9b634141f642f0d0ae94a65&X-Amz-SignedHeaders=host&x-id=GetObject)
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