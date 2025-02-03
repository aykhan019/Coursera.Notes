

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=0c2f791410315360d9d713691c42146d349eaaf2b28ea9e6506977738293ac82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=ddde35ebeb70d92b2b9bf6b779f37806d71ee9133b83a6321fa8cd3b4f80f17d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=4a436a7b53350146f485c9eedd99198c0b0c7b0518e3505d24c9e21542d525d5&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=107878fabb1ebe8f605ec93cffa78b8df45122fc5a241b2f799f089ce30e6f38&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=d2f17cd211e53eff70598740284699f235c4c718f38a4f4309cd1e0ab47c534b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=12b5b296890deae113e3e362ffd0e8fcbc06905d2ed38a6c807a0800454426ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=f196aa29dfcadf79a36de03178c82e68f5a0c7e433e718f037f086222b9992ea&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=8c781d4f66f8a655069cf7c58333c2f7093a5047942bd38e44657146d4f7177a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=3e2d76b1314668698cfa3910f17f9255afc464c2998addba70d90bfc07352fec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFV6BTSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTcd1XgGMUspWll9loBzvoj26X%2BdYh5Vkxn0T2iwDHiAiAn0%2B8Qh753YfBaX3kMUNLfj9HHI3Xx3WoyKJBAMH%2FlIyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMrYp8jfGN26zpNtnLKtwDT9DAQT5RZFlV9BAfrvKiIRFRGbjJV3zMG4RieXom1S%2FgO3JTWrv53yAF7VRrvsCmoX%2BHq04tMMcuxXWZGTxhPgm8jIlHLvLvPouxLSYmWxEk6A1dHPPlneH4uYBnw%2Fw%2FGBdxK8xC02mYbtZCa7ihPYLQxXqYex8WCF44JDi4A5wUUJxRPThPLcqiiXkRgzHFxvxrzOIi5pzAvsmDz5Xh2KmGcBioEUtlyYRltaZFWDDn3oAyRqc3h3cjX681GvmTQtsLbngp%2B7xERN4E8sZo6R3hE0mi9yVzrwNro7rEKt9f9P6TxqiJAsQK%2FXsxS2Fh%2Be3npWrMSnWmMVRXUdKDpik9pIRAdnGLmzX1JvMgHA9uM%2F2U2FbrTrGG1l97lU9lW3Jq9UMh7iY0XGw8ZqWX3uvlE5L%2FlTcPy75K7T9%2B65GLrid7jQfkZonF98oHN95GgcZAVgIJOOSc%2FekZtJLyQYbPwOvq%2FhQL%2FhKXd1uTr1EH2p65ZHiCd0JRaAbRCBbrqlI%2FIzaGZsZ1HOzBPKbtYiNL4RZZwo%2FssUtZ4It4xNebCl53WXgF1Bgad6%2FdA9KaG97OlAw%2BUiDgH62dK0MVE5n7Cu4Ww8Q0u74QnjSOnMOwCbnfWF1tZlv6IDEw%2BPCCvQY6pgFjtLMstZW1BtPEL6XAUjPJ10z25JcMjTd%2Fg0DCpzW63Pitn1v2s5oB%2BnpqEQnXts6%2F61XUAKlYBw8UWk65iiukgchwW6qpe63hPleRHr2ynSt%2Bpkhko2SziJR3UMlAntO4M3BD83i%2BDVJ8%2F7gciovq582HUo0xTNtR%2B6LuuNOGZx6mgOLWO9OrbNuJSz3QGG1%2F58HbgFPWvkc1CVGKUUG6nvX76Eut&X-Amz-Signature=7e694253add5069e013d74f75dffb98b3970d2a32985a45aa25686353d769176&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFV6BTSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTcd1XgGMUspWll9loBzvoj26X%2BdYh5Vkxn0T2iwDHiAiAn0%2B8Qh753YfBaX3kMUNLfj9HHI3Xx3WoyKJBAMH%2FlIyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMrYp8jfGN26zpNtnLKtwDT9DAQT5RZFlV9BAfrvKiIRFRGbjJV3zMG4RieXom1S%2FgO3JTWrv53yAF7VRrvsCmoX%2BHq04tMMcuxXWZGTxhPgm8jIlHLvLvPouxLSYmWxEk6A1dHPPlneH4uYBnw%2Fw%2FGBdxK8xC02mYbtZCa7ihPYLQxXqYex8WCF44JDi4A5wUUJxRPThPLcqiiXkRgzHFxvxrzOIi5pzAvsmDz5Xh2KmGcBioEUtlyYRltaZFWDDn3oAyRqc3h3cjX681GvmTQtsLbngp%2B7xERN4E8sZo6R3hE0mi9yVzrwNro7rEKt9f9P6TxqiJAsQK%2FXsxS2Fh%2Be3npWrMSnWmMVRXUdKDpik9pIRAdnGLmzX1JvMgHA9uM%2F2U2FbrTrGG1l97lU9lW3Jq9UMh7iY0XGw8ZqWX3uvlE5L%2FlTcPy75K7T9%2B65GLrid7jQfkZonF98oHN95GgcZAVgIJOOSc%2FekZtJLyQYbPwOvq%2FhQL%2FhKXd1uTr1EH2p65ZHiCd0JRaAbRCBbrqlI%2FIzaGZsZ1HOzBPKbtYiNL4RZZwo%2FssUtZ4It4xNebCl53WXgF1Bgad6%2FdA9KaG97OlAw%2BUiDgH62dK0MVE5n7Cu4Ww8Q0u74QnjSOnMOwCbnfWF1tZlv6IDEw%2BPCCvQY6pgFjtLMstZW1BtPEL6XAUjPJ10z25JcMjTd%2Fg0DCpzW63Pitn1v2s5oB%2BnpqEQnXts6%2F61XUAKlYBw8UWk65iiukgchwW6qpe63hPleRHr2ynSt%2Bpkhko2SziJR3UMlAntO4M3BD83i%2BDVJ8%2F7gciovq582HUo0xTNtR%2B6LuuNOGZx6mgOLWO9OrbNuJSz3QGG1%2F58HbgFPWvkc1CVGKUUG6nvX76Eut&X-Amz-Signature=790c1c5e5c475ab5ab3b9c7db194ed796f88487c535ac7d3e3e993f923b9b45f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFV6BTSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTcd1XgGMUspWll9loBzvoj26X%2BdYh5Vkxn0T2iwDHiAiAn0%2B8Qh753YfBaX3kMUNLfj9HHI3Xx3WoyKJBAMH%2FlIyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMrYp8jfGN26zpNtnLKtwDT9DAQT5RZFlV9BAfrvKiIRFRGbjJV3zMG4RieXom1S%2FgO3JTWrv53yAF7VRrvsCmoX%2BHq04tMMcuxXWZGTxhPgm8jIlHLvLvPouxLSYmWxEk6A1dHPPlneH4uYBnw%2Fw%2FGBdxK8xC02mYbtZCa7ihPYLQxXqYex8WCF44JDi4A5wUUJxRPThPLcqiiXkRgzHFxvxrzOIi5pzAvsmDz5Xh2KmGcBioEUtlyYRltaZFWDDn3oAyRqc3h3cjX681GvmTQtsLbngp%2B7xERN4E8sZo6R3hE0mi9yVzrwNro7rEKt9f9P6TxqiJAsQK%2FXsxS2Fh%2Be3npWrMSnWmMVRXUdKDpik9pIRAdnGLmzX1JvMgHA9uM%2F2U2FbrTrGG1l97lU9lW3Jq9UMh7iY0XGw8ZqWX3uvlE5L%2FlTcPy75K7T9%2B65GLrid7jQfkZonF98oHN95GgcZAVgIJOOSc%2FekZtJLyQYbPwOvq%2FhQL%2FhKXd1uTr1EH2p65ZHiCd0JRaAbRCBbrqlI%2FIzaGZsZ1HOzBPKbtYiNL4RZZwo%2FssUtZ4It4xNebCl53WXgF1Bgad6%2FdA9KaG97OlAw%2BUiDgH62dK0MVE5n7Cu4Ww8Q0u74QnjSOnMOwCbnfWF1tZlv6IDEw%2BPCCvQY6pgFjtLMstZW1BtPEL6XAUjPJ10z25JcMjTd%2Fg0DCpzW63Pitn1v2s5oB%2BnpqEQnXts6%2F61XUAKlYBw8UWk65iiukgchwW6qpe63hPleRHr2ynSt%2Bpkhko2SziJR3UMlAntO4M3BD83i%2BDVJ8%2F7gciovq582HUo0xTNtR%2B6LuuNOGZx6mgOLWO9OrbNuJSz3QGG1%2F58HbgFPWvkc1CVGKUUG6nvX76Eut&X-Amz-Signature=931ffe137282b0b4f79ad301222abad4229907311ec4e1f366309346175aa154&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=a4ae70b3962e10c19365c24092fa328a4a6005c4e8aff4375189fd8db7ef6652&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=833149d66322a319af788d7b5e2816c41adadb27714bb7e05dc05284a59eda4b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=d5040c71823c9da2e798723ec1d8cfda8b8a997e600db98c774299cd37d63f0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=bc69616757c223b97b2a2fc2ddba802ccc55689b13f779e80230694d63777863&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=bd81df238b3c4fa4d9531d833c346a41b7a540412f7460cac6a2a5e0dc0d7263&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7GSMVY5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFsdm0Ck28ZyElcNhxwhjx4prTDTDxX5z9LWw0ycBRhLAiEA6HsJJhKcwxmc2yW3kpyyOgE84NDIdjsKeze4k7RSrlAq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDO%2Bsz2y4X4Lz9v2ufyrcAw2MjhwSiUuF0P%2FUmz%2B1PEbqJv6O9iI6DHKEWOLmmcAgMrBZDz2IsjPI6puibpchkIK3sP9%2BNAw86uQs0%2F0Crvs6lUCWrAIlSLjgxGsUeJfo5R5C2ilt49opdp%2BmxIvmA5162A%2FvnSQMrq6gzemruIzZTRgy%2FcbmN7z06rnh1197LwmXQCDaqN4PebKr2DFheSNAxXZygSNFOo9K0bTrS3mW6EouladeIHbFaFuhTsrOnA878o8lcuQThVr2dBcMBk9PQ7rrMUai76uwcH8Yy%2BJPXOQxlj4fpcWVE1hV%2FwRRK%2Bg6IazSPErpCX6bXLCU3ymUfpFJDIlhbwFoaSe0L5LvnlSYV6iFcA1NDsSBt7hLjdHGT2Q4xUj7KJwZ4qbYD7rJzCwWAnSLv%2Bt%2BRDh6g%2BKAfhpx2AT9vfbe7m%2BBzyTs5cbhttooGG05uzc4e3%2FkgQoDYA3Q3GnGxb4ttXhUO7xmwA5yzPu9dow6iE7fKcfie2D4gwpcJ9m7k5lSM2owyjxbS5TxIlTLcV3IwfNuDeO0IKcE0bbI%2F4S52jiDvFm0p7ltXn%2Be9RubEpRozhjHTlv5cNu%2BPgOwy%2F6Ti4xl220TEKZV3pcNUDl6hY8sM0R90h2E4pdeVLqKId1MMKXxgr0GOqUB7N4AeLsvyGjcWZUHGpmc3IFv5jz%2ByI%2FKxg8%2FVhmcjM6ZFhneina0Vnm8qjfKbbY%2BhoqXRBM1wm9PF9jJ0a06UNkkR9r4l1dN%2F1f08JlApQ1Iuk%2BG5AEtLaebIaSsiFsNbM%2FIlhxhUbh7VDJw9LqFD8Ywm5uapZBuVVfL4xSAwkVTJQTpysv2W0OXD%2BjVnT2AvlNCWJTNcgR%2F0eoRtKbi5higKOtO&X-Amz-Signature=f485c833af502fbcc026a5c987e6ca1a15ca0b05d2dd5923f628f026810f5834&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EL2E5I4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGH4TEoIb3pVgGj42rdfB7kYMrPSB7b3uUtsmQzv1MUjAiEAlFsHFx5kclf9xEagV%2BwV7M%2Bwij%2FBY4D8VbG2IZOXnPYq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDAY5Ern5eJdi3ry8byrcAyuHayGO8rK5fEwElIDGmUdvmmB7jeHhP8elq%2BcBzRddWps3Xt%2Bztd27yC%2BVDjOEmecqPyWq3%2FDZbGk5GyVD376%2Fx6hCXpofCn9uAn760OEuwBTC%2BYxTtEwfvB4oGKrIXQIwxhFJ9KPaNZ3o5EjY%2BnFrDHWW3F4YOAv6y6hI0ow5QdBNj1XxVvvFyCXD1JNFrHC%2BhX6vP16YOmcjh%2BpnPpFoSRa1sm%2BRR6ziBldqaqfPyh1kK0Kwz%2FEfzrrtLETB1EtXxXnwvDZ9gdrLQTWEqg4u0EQFWX%2FPmMiYgTS5nc2BF1uNaOjqETaxUZaOWiqJmPs0nyZ0hTIIUaDjDHFbSccZBb6NTdr2knXIwYXV6N%2FnkoLbo8oOqeQkJA3sqAl4XC%2BZqfLF4lkI%2F198ZJ8B4g69xatK9rhlpScbdVedDkQEszEuK4v%2FL%2FFY%2B2aDvuLDBv%2FuvfC7pKJj189qvL8Yi4N%2FAJJYUdX5%2FyU3Z0H7LghT86WxAkOZE72caUhvjdCBYB4AmMdsHmUpHKcoO2mvohEpb2Mjyd2Yekx1v0piv6bGwcFb%2FNdITWzENoxOqS2ZXYRQ1YGfmnqDPe%2B7Zh6YbQq4MrX0%2BFOqGaQaZqSBoc%2FZ5WX54jFb6JZbe4lJMMzygr0GOqUBrdcFI935q1GP2dnW%2B7M6sl5OznLJs6P%2FTYySV%2Byp8QwGATemW5XniEklLLRGS7iQoneiTHxgb4Wx2ztgnPlEnXtzsn4B2l47b%2FtTCWnJymcBf9vxOGhTrWtIxzar8R7ihDafHhiB%2FCr%2Fnq7%2F7OWbEGcWlzj9VMeelYrsLqkMGzQAtlZrPNCkQSz3qDj%2FBnyHfByFsP4%2Bja1LFsvx%2FHTpHyhvRKCo&X-Amz-Signature=2093736c6c2d93d90ce19ee3609930fad251f4936f1a89b2425c4a2a00a3c431&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EL2E5I4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGH4TEoIb3pVgGj42rdfB7kYMrPSB7b3uUtsmQzv1MUjAiEAlFsHFx5kclf9xEagV%2BwV7M%2Bwij%2FBY4D8VbG2IZOXnPYq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDAY5Ern5eJdi3ry8byrcAyuHayGO8rK5fEwElIDGmUdvmmB7jeHhP8elq%2BcBzRddWps3Xt%2Bztd27yC%2BVDjOEmecqPyWq3%2FDZbGk5GyVD376%2Fx6hCXpofCn9uAn760OEuwBTC%2BYxTtEwfvB4oGKrIXQIwxhFJ9KPaNZ3o5EjY%2BnFrDHWW3F4YOAv6y6hI0ow5QdBNj1XxVvvFyCXD1JNFrHC%2BhX6vP16YOmcjh%2BpnPpFoSRa1sm%2BRR6ziBldqaqfPyh1kK0Kwz%2FEfzrrtLETB1EtXxXnwvDZ9gdrLQTWEqg4u0EQFWX%2FPmMiYgTS5nc2BF1uNaOjqETaxUZaOWiqJmPs0nyZ0hTIIUaDjDHFbSccZBb6NTdr2knXIwYXV6N%2FnkoLbo8oOqeQkJA3sqAl4XC%2BZqfLF4lkI%2F198ZJ8B4g69xatK9rhlpScbdVedDkQEszEuK4v%2FL%2FFY%2B2aDvuLDBv%2FuvfC7pKJj189qvL8Yi4N%2FAJJYUdX5%2FyU3Z0H7LghT86WxAkOZE72caUhvjdCBYB4AmMdsHmUpHKcoO2mvohEpb2Mjyd2Yekx1v0piv6bGwcFb%2FNdITWzENoxOqS2ZXYRQ1YGfmnqDPe%2B7Zh6YbQq4MrX0%2BFOqGaQaZqSBoc%2FZ5WX54jFb6JZbe4lJMMzygr0GOqUBrdcFI935q1GP2dnW%2B7M6sl5OznLJs6P%2FTYySV%2Byp8QwGATemW5XniEklLLRGS7iQoneiTHxgb4Wx2ztgnPlEnXtzsn4B2l47b%2FtTCWnJymcBf9vxOGhTrWtIxzar8R7ihDafHhiB%2FCr%2Fnq7%2F7OWbEGcWlzj9VMeelYrsLqkMGzQAtlZrPNCkQSz3qDj%2FBnyHfByFsP4%2Bja1LFsvx%2FHTpHyhvRKCo&X-Amz-Signature=d37360101372babef124b65ce3921b60b6e2d143e1c533028e3c7f1937a85e06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N3UEEQD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfw%2BqBoCj%2BB%2FfOsAVGUjwZolasG7SsfOhMO5IigOn4%2FwIgK15B0SL9iIcTbMCRlHGcER7QMm%2F9%2BJ6EtClK3%2Bqn9WEq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDOt6Klq5t2eebhWeIircA0eSoSNifTeeGmHQMyy7QoVlI9Kl10heua1TWFcLuhzLxaBSfQNaiU%2BoCMsD%2BJumf4LX2VJ2MrOa9vrBHFb6%2BhgY6%2Fidwm3nwtkYfg4OSr2eSyM15pVp9LEQs1vLc%2BVyBCS%2F5lzla0mulMqlAWwkh8YDUhbbwUG%2BoCMLXzMf%2BajEgPJ6RhCePaVMOesej7enRTWzd2pbhYGbETP2wkDpxf8OGg399PIiySg7qZmUkbGGAH35%2BbIFnp52CxNUZQ1FJh%2FAmXSpQv6y4iM%2F5L9F247pDQ7g%2FjVDU%2Fy6T6RN4i4iF2tOxGldoHow26T%2BZWQ2WBY%2BSCG6HfKKBQvHByeaJIoNMQBLrH3F3Ug7Tb3FmUi5hcpqx%2F5FiYHp%2BvrSt2P%2BQDUW07%2Bw%2Bjn3nV1d364pGh26jXq84UyCtG1kAW6MNsliY1eLuUCPyNs7HClk0IkVijyq61BT6Tu1OpHme7T%2BpMp6zG33NE39IEEfqHNJ1uHJjklIrR83FyVfEROyf0eq9iMzI4Kt5PAKGwkpyRimEjTWCpx9ns11wRMPM8NAatpyctj%2Faei9JLf3D%2FjQAlrZSDOLpLL8Tcc0paEgcJmWTChovvbfmjj6oRiD1Ghl1FZy2YUsrM5biXgBQHTrMLjxgr0GOqUBmcNjIKGSQ78TNqRF5TJQHUuC1ykpVJy4uv8kFOq898Bl81tWHFbJfWDxtyiEXIMyP2mATjseWlloDUHsTVDBdvJg7WAIBG6%2F%2FZlHGJH69RTt7FgL7DGbE7eVlfMtpV5JbaKd02WVDQKy42HKQyiVzDj6UqtdAiILukn3A58cmvKraGrdxvPRR%2BRHEU4tZtL5%2FmtO67DAYOVtLcSuzz9cB0YOU4qZ&X-Amz-Signature=6fc565a6b7eecde16707d7d7d126d7e3f51072c1a4312cd7ef5f2453c7a14845&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHSNBYG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFi6hIQN3dFJWpPzyp4mOfzcdyrfIlavfCdh%2BDuFPfnVAh9I3MPovGZSBbZck2ysUSfis5%2FuIqUcnlnaXkH9ezWZKv8DCBYQABoMNjM3NDIzMTgzODA1Igw%2BMIQ3j7SU%2Fl0Crc0q3ANA27ZzZo9I0PEvn7SbRzahrubrk2swp3n%2F%2BLHFmQjUor%2FlqrH1D%2B2D12YLK0fpD1Vex85xXZHwV%2FCemjHGU1gC1C0jSm%2ByTJ%2B0q5T5B0ysmDBthNT%2ByiUB5rEPkUvQPXqySjzys6C9v%2FO6Kpq%2Be5o6Qs3gfbEPFLNsdWftxU%2FVBQIxvT3aVhe328oznugVqVTZtjiiNliq83iz8pQWuS782gjw016OdIz2iEeQ%2BeyaybZ29EG9KpoGFYw4jyeioKtoxeG8LcVvEUWmr8%2FRigQf2pSEI6MXUIm6eEixIQOyNxErnqmZxMmj8N0loxaEBo3in2jZsEOU4B%2FoDVju9L74rUZhqvk3mVIkEOQWsINn0Z031IeNINky%2FdrOAHHgEdnIwxiRvKMVtzUsSBqD%2FhxeDiGv9ioG9KPwNSC90fQeKlKCJ3YhFd7ZoLnj69fkGJU5KueDVENn5%2F4etirWUHtG1GCQRqlfnwtkcEgSkH%2FKye5aP7LH41OGOWwknYIvB8q1YHojfpKH%2FvMtdYXMOCgwk9kVW5NHnoUvXJc9eWczcoH0Hes9dXHsc5I1nosDFMcM%2FUH0OdeDCpgnCS%2BR7X90O1N18q21kp82sq178haQhVDUfvftr5%2BQSuscoTC28YK9BjqnAW2UglXHD8NFibeiEHja6%2FkUn0WVzaJyQILIY72g5r4ss0UNxdLItkxpGhVuHLt16y5kwuFMkGaBUbi57n2O10JaP3gpkIISGes2cu8BaaMssHW5LN7%2BwDdCqnHkECBMB1LsRjmFFuUZFaKgDWhM53H8JtxcVqChFHcVO4hxNVKsTzTG8xwDK9y7szIy0W53kSJm4e4oeK%2Bmz6%2F9yQmKOKpNVPXRSDLz&X-Amz-Signature=4144ceef0dca9c70cd13abff791b1255e0a7e8f875c97f0435fa118d5e86c852&X-Amz-SignedHeaders=host&x-id=GetObject)
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