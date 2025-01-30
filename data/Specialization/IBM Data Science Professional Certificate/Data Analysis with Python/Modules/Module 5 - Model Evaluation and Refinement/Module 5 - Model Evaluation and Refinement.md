

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=4589d34511c71113a4c9b4c9b1ab2788cc0c36c74bb09b77e46a04ad79c80523&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=f2d9d204b94f8c12be6455f6860a62d1f5dbb4868682bacfb2e57150f8386211&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=4ea66de70670ebda775346da97abf96ca3936bc1f9169596f4fea9dd0d2dc802&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=57f71e7a141bf27b0d2c201ab15853d784a8d10274349f9faba4a9fb7372036f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=cd5d08e372f99a683acbb4f38719f88febdcfe886a89b548c8b42501e2b79f8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=81672e0a395c7cb07c0ffa6440ac3ed325b555d36b299b677e2724e94f058caa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=5c61f10735c13c00ff940dc2d890a0c57c6f2af7037894160bc7a8afbc1760f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=ae44360d20d0efd80921e7a101368d31d570288b28d5f4dae5865ac825ddd2ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=a744c22d34f65c31c0ed0d40014e996134547e067bc1197bdf85361bf02189cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67LL47M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAj7KR3%2FSf1midQVowsOOMrnG4fsPL%2BIpsklW9xxGCxnAiEAptGxx7kWjqEUGPNGBnlv4xMbagtx02TMy%2FWpRTasn50qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIKkFrg%2Bk1ZsGKb90SrcAzNWdp4LYNrZCTVURLQmEQYWOncB3vF%2FylTbYxHjGIHL1hK9YPB2tYA%2FLCXPm1A9mcn4TFkJNZLoN0kpNk%2BCUg4I2YSC%2BV2E5NFohAdIBzAYu56Wz4tH50MFtWacb1pgWv4nfKb5%2Fx6VkRHiOEzfz8BpEauAbETOr3jTCYgZMhSWxRdCUhduGw9gJZr9qQEgZA8B5%2B0MA7%2FNCAlr6gmYT76C0BwkLevRKv4k12hnxEZ0olmi1ctks7WIjnM85z2R0yjsPu2ZeI39GuYULym8JMAVD8qjKy49EGAzI9bX2YqgaHlBgQ76kpWFbHQ4emWpS3Qp%2FMf6s5pSpQrgZ61sjXbTOTu2e6eOoC2mlrg0G7GAxoPd1BSnzYBUbIq%2F8rjcCfPyQpMcw1D1QG7wYeMMA1ELeOY5EevQVNvGovEOsEzdmaXXFXk9%2Bfxt8h47xLMJz8ILZEVDFI7Sk5699hrHGIPWjEVMNIVZURXbJzKfoWMVp1uSStTS5fa5rbVsbwh6qzKC%2BMK5GvsdC5wvU3W1VjeZIXxX36PK9fZr9MzCmeemFVMsKndZXRUCQHC27FnO%2FFcWzLpDYBWGw7vTxvbbuu2K8Zba2jzuWLvW0EG7%2B7brp5SqqTh6uX%2BNJVz3MNzO67wGOqUB%2FbnTzA34ZCUCZ52ofx0ZpjOrpa%2FQX%2FpB3Cbd2ZXyTImQDx7VyqMI%2BpekT7rWgMsFrV%2BqYbmOxm9WWi4TCdlF%2BkVuMYO3J1536dbTMuG%2BBHNDqY4W759rRKvEVUmMmdlEF%2F1GqgpWB5YJzDurYXG%2BKPtBiuPAL%2FhJBvttqkzaebafH0EtaQw9RfpwDpwzZILMrwwxVIsevABBiVpDkY4m%2BKYnKkvQ&X-Amz-Signature=e31ce55ed3523ccbc25fd0e2dc0aa07213f1493e99be09bb4e8f9139fa509045&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67LL47M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAj7KR3%2FSf1midQVowsOOMrnG4fsPL%2BIpsklW9xxGCxnAiEAptGxx7kWjqEUGPNGBnlv4xMbagtx02TMy%2FWpRTasn50qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIKkFrg%2Bk1ZsGKb90SrcAzNWdp4LYNrZCTVURLQmEQYWOncB3vF%2FylTbYxHjGIHL1hK9YPB2tYA%2FLCXPm1A9mcn4TFkJNZLoN0kpNk%2BCUg4I2YSC%2BV2E5NFohAdIBzAYu56Wz4tH50MFtWacb1pgWv4nfKb5%2Fx6VkRHiOEzfz8BpEauAbETOr3jTCYgZMhSWxRdCUhduGw9gJZr9qQEgZA8B5%2B0MA7%2FNCAlr6gmYT76C0BwkLevRKv4k12hnxEZ0olmi1ctks7WIjnM85z2R0yjsPu2ZeI39GuYULym8JMAVD8qjKy49EGAzI9bX2YqgaHlBgQ76kpWFbHQ4emWpS3Qp%2FMf6s5pSpQrgZ61sjXbTOTu2e6eOoC2mlrg0G7GAxoPd1BSnzYBUbIq%2F8rjcCfPyQpMcw1D1QG7wYeMMA1ELeOY5EevQVNvGovEOsEzdmaXXFXk9%2Bfxt8h47xLMJz8ILZEVDFI7Sk5699hrHGIPWjEVMNIVZURXbJzKfoWMVp1uSStTS5fa5rbVsbwh6qzKC%2BMK5GvsdC5wvU3W1VjeZIXxX36PK9fZr9MzCmeemFVMsKndZXRUCQHC27FnO%2FFcWzLpDYBWGw7vTxvbbuu2K8Zba2jzuWLvW0EG7%2B7brp5SqqTh6uX%2BNJVz3MNzO67wGOqUB%2FbnTzA34ZCUCZ52ofx0ZpjOrpa%2FQX%2FpB3Cbd2ZXyTImQDx7VyqMI%2BpekT7rWgMsFrV%2BqYbmOxm9WWi4TCdlF%2BkVuMYO3J1536dbTMuG%2BBHNDqY4W759rRKvEVUmMmdlEF%2F1GqgpWB5YJzDurYXG%2BKPtBiuPAL%2FhJBvttqkzaebafH0EtaQw9RfpwDpwzZILMrwwxVIsevABBiVpDkY4m%2BKYnKkvQ&X-Amz-Signature=fd1b28cefb36b9593c2ed90692de96edf5b8a6a0a7d12ad6efbdf15fd51010e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67LL47M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAj7KR3%2FSf1midQVowsOOMrnG4fsPL%2BIpsklW9xxGCxnAiEAptGxx7kWjqEUGPNGBnlv4xMbagtx02TMy%2FWpRTasn50qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIKkFrg%2Bk1ZsGKb90SrcAzNWdp4LYNrZCTVURLQmEQYWOncB3vF%2FylTbYxHjGIHL1hK9YPB2tYA%2FLCXPm1A9mcn4TFkJNZLoN0kpNk%2BCUg4I2YSC%2BV2E5NFohAdIBzAYu56Wz4tH50MFtWacb1pgWv4nfKb5%2Fx6VkRHiOEzfz8BpEauAbETOr3jTCYgZMhSWxRdCUhduGw9gJZr9qQEgZA8B5%2B0MA7%2FNCAlr6gmYT76C0BwkLevRKv4k12hnxEZ0olmi1ctks7WIjnM85z2R0yjsPu2ZeI39GuYULym8JMAVD8qjKy49EGAzI9bX2YqgaHlBgQ76kpWFbHQ4emWpS3Qp%2FMf6s5pSpQrgZ61sjXbTOTu2e6eOoC2mlrg0G7GAxoPd1BSnzYBUbIq%2F8rjcCfPyQpMcw1D1QG7wYeMMA1ELeOY5EevQVNvGovEOsEzdmaXXFXk9%2Bfxt8h47xLMJz8ILZEVDFI7Sk5699hrHGIPWjEVMNIVZURXbJzKfoWMVp1uSStTS5fa5rbVsbwh6qzKC%2BMK5GvsdC5wvU3W1VjeZIXxX36PK9fZr9MzCmeemFVMsKndZXRUCQHC27FnO%2FFcWzLpDYBWGw7vTxvbbuu2K8Zba2jzuWLvW0EG7%2B7brp5SqqTh6uX%2BNJVz3MNzO67wGOqUB%2FbnTzA34ZCUCZ52ofx0ZpjOrpa%2FQX%2FpB3Cbd2ZXyTImQDx7VyqMI%2BpekT7rWgMsFrV%2BqYbmOxm9WWi4TCdlF%2BkVuMYO3J1536dbTMuG%2BBHNDqY4W759rRKvEVUmMmdlEF%2F1GqgpWB5YJzDurYXG%2BKPtBiuPAL%2FhJBvttqkzaebafH0EtaQw9RfpwDpwzZILMrwwxVIsevABBiVpDkY4m%2BKYnKkvQ&X-Amz-Signature=f033efe16bb32bd899916df3eb766e28c8f9bbb22d359b1cc5727291633e2f23&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=136069fa38ae0aa6d18af6e7a95b0be928ded6a0c71c07cbfb1e63311ad18f6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=f9f42e6be9f23a59d754eebbaa23b5045c88e6f790174e7df8d949443050502d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=db6c02a20551b29ae1f337d070fc81ac203dde69ce94ed42064742e1dc2aa0b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=6cd5e6635ab494b200bd8b0b556cc21ecf0f6a9d428092dced9784d843f8b2e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=5e02296e25b13cf6c305b83a57ef2ba32b77887dfafac372f681face1447a3d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IT2NX7A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDRhS1eVBN7hPbyQY%2F4Oe5Q52NdhyNuzfxR2%2Ff8uCMPUAiEA9GBs3dU1eiA%2FNtWJJcAglMmXib%2Feru47udyGmTstnfQqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEYR0freYOIweVCFJyrcA8AbyLpmpU4WIRtiORDgq0a8WVhwjrPQkgZlkXNUqWW%2FiGgVNv5xB316ROSYCu7Pcot%2Fk2xqYOJGq0BrLTjwNfD4zvY1qGlAaH%2B7xgCae1Hqi5qET4goQBvyYvEH%2Fjck36Me9nqV%2Bn%2FRmvft%2FssKMM%2B49KsyFGWuQFB9RcDaSr0%2BKpwf7p1OZsTZusUeuAezvozNnZZMVIIm9Y6CB2G0RA7PDKb8Np2NgsBCjW6fPwgLxAJwnGhLYSaG7kgM1didQ2PT3FeLhYvb74iWeoA1V9pFyUd7e1gLdBe%2B0VN1fU9uY77sCqgY4aPVl2Xjc0tcqAqu1Z2cHBiy%2FdrToRvFowRZOeuST2A9DGZXruWQEvLPGt5gnXVZ7kGVfGt99UV47JBmrvkXmx03ynVAUv5dDewN%2BELFjCpA5tAMOp7c2QXqvfCBoIhPBaz6cajaBX%2Fy6f4qeUhhRPOZc0Rcozvt%2BKl3y8EBccboC8KDyPh67Jd2hxwm2TeCQMLfac09zVHd%2F4MOif7%2FIycMG0P1RQEvluDmMlWJxQDDS6VRJIbYULp4TaubtaB0MTmoGFcKMmQZBQtLf5MVipwbLPZ2ojqa1xsZ%2Bfk5B281rRIbPhV7kx%2BO8MOTrIcxpSVeb2%2BAMIPP67wGOqUBUcdvBM5qhZ3osdYVWBtRjAHFooduosfoALKgcJijDeBdISdNHapAosYeu9AMsvD%2B%2B%2FgkoCLS8CplxxDYUbaO72FMa4PMlE6E1r8w8YA2cuo74zePltRBVyQ6DgY%2BMizNSY7poWll%2BralJpQ2AqD6MCPg2K1GOue4o3bJoQbNswqAsedkGr6gHBtFRHsa5PhtqDhYgwtBsZxVhpKNoJrGLITPw37d&X-Amz-Signature=80f5372ef80f24e3f79c5a71f6e47a59e90594d5cb89a6253c66d616ecaf5da5&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3W72QT4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2x41IIOqnnJTN58fyAvkpWoX9K6vVemfo5EKNYv9w0AiAvUJfYnovGlzgrqi7g5C4kfvfcLWkp0Jg36LKTxRoq8iqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTyOIb2HjSkGQc58KtwDs0h9iv4cCJ2VsxPeaZlk5W%2FdbNU9vtJqi76qvyOGOC%2FduD8OiDF6EbIrr483PLKaOWXGmYHp75OJxrPYX8TdRw8bPoW%2B48%2FUzNfLe2DMr4YT4vBje%2ForTuZjgLfwMWYz35kjDfnVSqyECJszQmxguqkZyRC7ZlLFDR9lU9l7NfPW09oy2DuvtlSmoamhtQHhbqP6Hmb012Jiqqll8nPm3gtUH36Y1M5%2BSYlQHdWIYzwNqENLFnqGRYsd3NbrmoeTOtnAl%2BP5JZsdtPTvAiYszJXJCfEzDWw6y8f4D3EYLb5T4FXmdMIpGd2QRiTjGt0OpleXfSfhFu4spjt5VERHxEZZHUGS5GxK7gIUfW3k6Gb1%2BCeColdeYr7dwsm3Mf9bW9TOYDRxp7R%2FKPW1S2yZH0Ab54%2BqXMIDnN6zkkQAhQupf%2F2kbExRGkOyNnHmsBV1s%2Fb1tNVD29qthwq96PsfEskBR8aLrC5BCtlRChP03OshhFlgMZGw5apIspc%2BkcCLayHPCTcpAo%2FzvV6NrN%2B6Ap2UA5JBF6JpWmNniiVOOnk7ytAaSqkuIO0qfAjC9dzsqY3GrtFdRk5ZLw9pr0yqXH2oZeqPFKjSOnTo7seFSLw20z1h95BE75TH1bownc%2FrvAY6pgHfSCg3%2BhTsB7rSZzwoyibDyEcyy17vHdOhSCu8sckYppYtiKBq0uSMD4qCYpJjuIKusLlCQGSCw9D8EuoiZEaq34CDqug%2FXEuIh%2Fdv6x4G1Pmy3SH6oCkmE5gXdC%2BVnIIN4KZvpxNAiL8jfPy36wLA%2BcloK2V7l6SuWU1k9wKHUmP%2FoTcPCefcmWOO22xBM8pxKiU2rpsbnyW6XJ95q50yGoIrHk29&X-Amz-Signature=683eddb6103676633f7451585f54e42654d1671ea2f78df42d5d51fa75655806&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3W72QT4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2x41IIOqnnJTN58fyAvkpWoX9K6vVemfo5EKNYv9w0AiAvUJfYnovGlzgrqi7g5C4kfvfcLWkp0Jg36LKTxRoq8iqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTyOIb2HjSkGQc58KtwDs0h9iv4cCJ2VsxPeaZlk5W%2FdbNU9vtJqi76qvyOGOC%2FduD8OiDF6EbIrr483PLKaOWXGmYHp75OJxrPYX8TdRw8bPoW%2B48%2FUzNfLe2DMr4YT4vBje%2ForTuZjgLfwMWYz35kjDfnVSqyECJszQmxguqkZyRC7ZlLFDR9lU9l7NfPW09oy2DuvtlSmoamhtQHhbqP6Hmb012Jiqqll8nPm3gtUH36Y1M5%2BSYlQHdWIYzwNqENLFnqGRYsd3NbrmoeTOtnAl%2BP5JZsdtPTvAiYszJXJCfEzDWw6y8f4D3EYLb5T4FXmdMIpGd2QRiTjGt0OpleXfSfhFu4spjt5VERHxEZZHUGS5GxK7gIUfW3k6Gb1%2BCeColdeYr7dwsm3Mf9bW9TOYDRxp7R%2FKPW1S2yZH0Ab54%2BqXMIDnN6zkkQAhQupf%2F2kbExRGkOyNnHmsBV1s%2Fb1tNVD29qthwq96PsfEskBR8aLrC5BCtlRChP03OshhFlgMZGw5apIspc%2BkcCLayHPCTcpAo%2FzvV6NrN%2B6Ap2UA5JBF6JpWmNniiVOOnk7ytAaSqkuIO0qfAjC9dzsqY3GrtFdRk5ZLw9pr0yqXH2oZeqPFKjSOnTo7seFSLw20z1h95BE75TH1bownc%2FrvAY6pgHfSCg3%2BhTsB7rSZzwoyibDyEcyy17vHdOhSCu8sckYppYtiKBq0uSMD4qCYpJjuIKusLlCQGSCw9D8EuoiZEaq34CDqug%2FXEuIh%2Fdv6x4G1Pmy3SH6oCkmE5gXdC%2BVnIIN4KZvpxNAiL8jfPy36wLA%2BcloK2V7l6SuWU1k9wKHUmP%2FoTcPCefcmWOO22xBM8pxKiU2rpsbnyW6XJ95q50yGoIrHk29&X-Amz-Signature=87ac5282d4fcdd5fde3a7fc0c056ab650cb34ee1ea7b5530c35cfd1fcf2c209f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHN5W2OP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7fZhPKJzLBXSG3n%2Blx4XYecc%2BL2YdBAV0931jIFbk9wIhAIaf9qdP9ERydlgt9gA1R4zCIUSJ5lYljuh1WF5OJic%2BKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYXFJl%2F4zWcvtwPuUq3APqZSpiS6Hk7VvuRkhjJGws21am6el%2FMv%2FIVdfnKl5%2FkNm%2FQQz0SsWbdzDF1djNGVrI6HY6mRf2kSx8bseeQ%2B8QJnhXAKc2R5lvhEPb%2BVv%2BuKsMKcFzFRgO6EVN0NEeDQ%2Fv5QSns3By5qnDYhQix2DKRcImm2VgkwHsmTetsYkdJR9g%2Ff8WvzA1qnxXjILzDOImpm2fyLopBeCko%2BgTrXJQ%2FdoYqidyaM9GzMH20%2Fgiqe%2BodeBwv7K5WqvhK1qNbpOmKKKL%2FHG5Bkv0sX8g1gOaZEHA9dS4W5YZwQ5J9XxnG9345e0AnActADkY665UboeK2SF83ggfrCRdKrFaPhy63usCi6Ngx23ktkVZpsgdpTJjU%2FLBuAcfS5gJ0dAaqOBYfNkue%2BR3BUTM5lFMmA6Jl5Km4767hUF4u0Vhyehs25yxWIfa70zGLnZ%2F%2BQZWGaTgDcn%2Foj9o5E0flCuPBHpsxiZ3UrWAFgdhnOiLVh4ouDLyd79CPNhecS9CNKmOhsw7GdEix33E3%2B389XnLxEyFQ9WZg00wt%2F75oGdkCzxTft7eXU2AIJC7XAX1tLUd86ZbcnBFb0KrzQ0uoCQZbehOmDUAT%2B7chiZj%2BDbrWuUTNuDWWfck%2BFQtkeqpxzCIzuu8BjqkAcV3eHvnHUPGevbzT2d1u66ZOuBx2U5lwe69bMRRBw9hiv2U7aoucm7klOjUnoM1TWfjGwcqbHGjrrqU7gbnYNLKD1EmJGdl2SLRfUypHNChABtgGRRvljiW1Hq1SWE28l6M%2BVsbevMCg%2FAdVFaazfdp0uVfp8b9Au37NVn%2Fs6KvZg7Pw1YH9X6VjU2OuJpxWjZIbKKfprnl2yb0shsro2v1prMt&X-Amz-Signature=098f094345c17137555b6bd25bd06cfbd143456a58f8fe95347a2b10522b8d83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7HPZFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFADtQ0f0f15ZnPFFMI8ybrudUsVOSOueUu8ZA2tYC6wAiB8NgpZXEC6ycCiH%2BnisA1ji0VZqp5DMv9kEsYt83hVVCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2ZSsI9Mn4%2FiaVUhXKtwDot1obDo8PGNxKQvkUELC5dmCo%2Fb39KYTFQi3Mjtb%2FN8Uo5EdzN5xOMSK3%2BW8yrt7Qgi10osStoBeiwXW4R%2BaQ7S2eKUmXzzIJin%2BPqvZAec8y430qec%2FNMBvS6A%2FHKeZziKNVtCDMrVipcQHmSzRwAQeZqU%2FSadc3LKvSgSW%2Bcf8R4UMcZBd71TMS6K0kDwqIgUfhtcAgCfrWugKoYTntNatr%2BkQFeD%2FRahbPhlWBog7HBhQp2Y4bnweKe6cNw1zBGYhjdGu4%2BL3XSipl3wK4CKbq9SHAmtdJgN399ua1BQj34CE3%2Bx5Mt5CaaYgkGbaTx2SwRSWr59zleRxCgbTUBW7pRFPoezkCFvNGjXsMPhl1mviB2jzauerY6XMXK5xDKlptbGV%2Fr8JSsGYSzmJjtkSNVwfs4RvoHHY5TG8ZONDyXTamuJolXcdJLCsNcTe%2B3ANs4gxtdXxh5q%2FoDYxtctFH6H%2Forfj5DZJuStlG7Td113g%2FpZ0PIOvZ%2B3s7BNZftp1NWNTVqA6MXA8B9v%2FBaKSjsPdv5XxjnKstQfnFWV5t2LKiI2%2FvxcIwcmDxIDFpd%2Fq5Tpa5IcthDL3NMSA8nwxvRSF53xJW2Zu2j3QvrHDss1le6GfFSkL4twwuM7rvAY6pgErF7TdEHhQVtuZTiDKgsUeGHL445ePEvkxP1xz4MLRrMaDf4tmfMsRv6x3%2FUxi91yqT46pGx1OhJt6jiZRAyNDndJEV0EgMep8vDV9tKNChDZ8OaP2z13o9BHBxmfUl9yJs8vkH5hidckcPGSlDZJW7kNnwmEUzESXlTShdN2Bt3xZNz%2BO2awWRt6txii8QJ6jxFigMMaUcMZhgkVxEW0pSBni2qhm&X-Amz-Signature=b1cdb770e329a414eae82dc5b95af8ec98c681beeffd879d0cfc09a432910540&X-Amz-SignedHeaders=host&x-id=GetObject)
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