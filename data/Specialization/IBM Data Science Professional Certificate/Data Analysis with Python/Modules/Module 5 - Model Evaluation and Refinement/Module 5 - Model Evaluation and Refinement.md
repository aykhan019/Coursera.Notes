

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=13034786eaa2ff1ef76a3ca4849bbe1fbaf2b1daea2f0a381a022d6d75ef1b59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=925976cd00aaf1ab32cedbcc1516ce8ba968f00c2fff09588467c24d13cef370&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=68ec2374148615291d6e4401625f31d35aafea395e8596c3119468c0f3fbaa49&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=14b21175b1896c730ec2801a5b5b4332c92ce21ed3306254154f381e93879c7e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=e790fe4ff1a98f34fe1a3b1dcbd497848489fffa8553d88504a70ec2a492ac71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=9cc43064d2aa70dfda9aafdb1eefda196ef62ecdcffa68de66ff6b27a34e8bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=618c24f585855b79774fe06dda0ec5611d0e8dde6cdf77b9cbbe4740021c6bc2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=39ac7e06445e434d9848532b4f97bc7135e9862f5d63e129c3409bbec6ac78c9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=0a7ceb1da228a354b196ade949587d485316d48f745fb63701a98413dfd7277a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWNKMQFG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD840rfuB3YjLCox5EnaQya3YzAuIW26l3bm%2B5%2B0rUlaAIhAPHjZi79pDx0c8oBQw02xquZ2nqftLr2u55qfjOpKVzTKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC6NsLa9BSgJPi1Uoq3APpxIpTjWcGjbXoEMxCv2IPTLfx8eEMR4dWt%2BrJ1DLnCEiPF3LrCtDctpd69GgXzZtyeAyZ%2F3HxG9vEUrVD0kXHVFItgQbp%2F348j3BgXGdqXBDV9BRBZq9QVqzSY2ec458NlH8ETIU%2BFPgtMfuElW7rKeVpQ8WnlSsZMJ%2BM9FY6IybWwNIGJkUB%2FLIpNZlz1uKJxAJAzxANznehSNc4%2Bm3Fq6V9YB0Z8wPuCxC6TN4%2BHyD8B6vOP%2BqyACPBK25m3TwmMPq5po7UBFyr4eVmnktdZgEgU2HO2Jo5WRDkkGpdGLku3K7211QMKS2GP9uA0ReyhX1shl5oB%2B6QajzUmvG15O57kXu6K1qrnvj3cm%2FHNcLag358cMaQH0KcKMygcUlMuZ2KkNeRCXBx5ivf%2FMjV6q3u5drI55Nzq1ecvIguvDqwF7Yi0Gb6Ixa%2F64xaD8jGgIhApzP8Sj0zfotNUIIfslYyuyoI9tMx2gLciSIZzPuyxo6SonI8EP51CDTdvDDYA3JzQopA%2FrbOZO5DDX5uq0nm%2FZz3Hq0L7U0z615BWyBPzg1cA%2FnRpyo4PV1yfz%2BLzFKbZPyM0hxu%2B8XidqAiEsfImE6RqjGpr5DKMsYMdfBnsCb3gzD%2Br75f5DDXtvK8BjqkAbWbMXK%2Fz78Da6t4Pp0Wui98UGcYPmHhsz%2F%2F1z4S9ULNcPyItGkvnwju0Ow0BeIjW706KBkF1DuZtbYGPpdvPfly07AaPnOw739meLM5EHrqGKkh8NQQNM50rS5sDwRjlALUizkwRdAnqAtIOFlLCet1%2FdlYKz3V%2BlKWWzeK3na%2BwqMDdetDPwWQDSN5hc0GvZnDlZpq5wUDRGN%2BuZyI5SJwt%2F1J&X-Amz-Signature=f8c8af2f72cf21df88be069e7004b3e84b4a05a6e36f7a38c8e6ed2f19c50f5d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWNKMQFG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD840rfuB3YjLCox5EnaQya3YzAuIW26l3bm%2B5%2B0rUlaAIhAPHjZi79pDx0c8oBQw02xquZ2nqftLr2u55qfjOpKVzTKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC6NsLa9BSgJPi1Uoq3APpxIpTjWcGjbXoEMxCv2IPTLfx8eEMR4dWt%2BrJ1DLnCEiPF3LrCtDctpd69GgXzZtyeAyZ%2F3HxG9vEUrVD0kXHVFItgQbp%2F348j3BgXGdqXBDV9BRBZq9QVqzSY2ec458NlH8ETIU%2BFPgtMfuElW7rKeVpQ8WnlSsZMJ%2BM9FY6IybWwNIGJkUB%2FLIpNZlz1uKJxAJAzxANznehSNc4%2Bm3Fq6V9YB0Z8wPuCxC6TN4%2BHyD8B6vOP%2BqyACPBK25m3TwmMPq5po7UBFyr4eVmnktdZgEgU2HO2Jo5WRDkkGpdGLku3K7211QMKS2GP9uA0ReyhX1shl5oB%2B6QajzUmvG15O57kXu6K1qrnvj3cm%2FHNcLag358cMaQH0KcKMygcUlMuZ2KkNeRCXBx5ivf%2FMjV6q3u5drI55Nzq1ecvIguvDqwF7Yi0Gb6Ixa%2F64xaD8jGgIhApzP8Sj0zfotNUIIfslYyuyoI9tMx2gLciSIZzPuyxo6SonI8EP51CDTdvDDYA3JzQopA%2FrbOZO5DDX5uq0nm%2FZz3Hq0L7U0z615BWyBPzg1cA%2FnRpyo4PV1yfz%2BLzFKbZPyM0hxu%2B8XidqAiEsfImE6RqjGpr5DKMsYMdfBnsCb3gzD%2Br75f5DDXtvK8BjqkAbWbMXK%2Fz78Da6t4Pp0Wui98UGcYPmHhsz%2F%2F1z4S9ULNcPyItGkvnwju0Ow0BeIjW706KBkF1DuZtbYGPpdvPfly07AaPnOw739meLM5EHrqGKkh8NQQNM50rS5sDwRjlALUizkwRdAnqAtIOFlLCet1%2FdlYKz3V%2BlKWWzeK3na%2BwqMDdetDPwWQDSN5hc0GvZnDlZpq5wUDRGN%2BuZyI5SJwt%2F1J&X-Amz-Signature=812e1961ca83b5b013aa5adb7d6ea7dc6837f945e9b6bf0635d24e870858bf02&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWNKMQFG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD840rfuB3YjLCox5EnaQya3YzAuIW26l3bm%2B5%2B0rUlaAIhAPHjZi79pDx0c8oBQw02xquZ2nqftLr2u55qfjOpKVzTKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC6NsLa9BSgJPi1Uoq3APpxIpTjWcGjbXoEMxCv2IPTLfx8eEMR4dWt%2BrJ1DLnCEiPF3LrCtDctpd69GgXzZtyeAyZ%2F3HxG9vEUrVD0kXHVFItgQbp%2F348j3BgXGdqXBDV9BRBZq9QVqzSY2ec458NlH8ETIU%2BFPgtMfuElW7rKeVpQ8WnlSsZMJ%2BM9FY6IybWwNIGJkUB%2FLIpNZlz1uKJxAJAzxANznehSNc4%2Bm3Fq6V9YB0Z8wPuCxC6TN4%2BHyD8B6vOP%2BqyACPBK25m3TwmMPq5po7UBFyr4eVmnktdZgEgU2HO2Jo5WRDkkGpdGLku3K7211QMKS2GP9uA0ReyhX1shl5oB%2B6QajzUmvG15O57kXu6K1qrnvj3cm%2FHNcLag358cMaQH0KcKMygcUlMuZ2KkNeRCXBx5ivf%2FMjV6q3u5drI55Nzq1ecvIguvDqwF7Yi0Gb6Ixa%2F64xaD8jGgIhApzP8Sj0zfotNUIIfslYyuyoI9tMx2gLciSIZzPuyxo6SonI8EP51CDTdvDDYA3JzQopA%2FrbOZO5DDX5uq0nm%2FZz3Hq0L7U0z615BWyBPzg1cA%2FnRpyo4PV1yfz%2BLzFKbZPyM0hxu%2B8XidqAiEsfImE6RqjGpr5DKMsYMdfBnsCb3gzD%2Br75f5DDXtvK8BjqkAbWbMXK%2Fz78Da6t4Pp0Wui98UGcYPmHhsz%2F%2F1z4S9ULNcPyItGkvnwju0Ow0BeIjW706KBkF1DuZtbYGPpdvPfly07AaPnOw739meLM5EHrqGKkh8NQQNM50rS5sDwRjlALUizkwRdAnqAtIOFlLCet1%2FdlYKz3V%2BlKWWzeK3na%2BwqMDdetDPwWQDSN5hc0GvZnDlZpq5wUDRGN%2BuZyI5SJwt%2F1J&X-Amz-Signature=f8ec16c2683e4835cbc563ad31f1ae7aca5e1a223444540ea8f2752775aadf6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=0ec5ec0dc3f748156a32d2e03f483b655bcfbf4a63b5b96cbc970d6bfe5e4b34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=8e67a7ac7fea8444ff23dbcd805fc214422efae3d4f1b98c9d066cb988434303&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=7700b1ff16f18c9d5492db5077ed1a173b763ee7b63da1b3cdf86f087d720e23&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=acc4dff6bf2b63af9dcc17d3fadf091e7d6336b431dce7958736a48849f4c2d0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=7477c9afad10bce60db6c010be6919faeeb8619fadf0d172fcc4b432de41f920&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6LAP3CQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsKQICZdqFsCpjXrWmxPv0ALb82oZ1WGSr4ClF52%2BkqQIhAL9OgtLzMad77OLfE1Z%2F0MOhz5TDf9NxaNvy%2FKJXaZTtKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRaZ78c%2FRyiP6al0cq3AMDQ4810GTtsnugELYTfNDXKXbFPErUtaLTkcxFTSZ6VTtJ8VsyMaWF07BHTd96%2FuwGTHXv6Kz%2B4V58nGUj%2BZaVKvD5tthHwamZDcrXz3ZRjZWaR3Lcb35PGOYugKBYef24jZatsTlQa9rgOwcnEUkqfSHsm4kXvxewXSvD84w7lVJWbxNj4jDBcTyCCT8K5HfcNfYW1po%2FfNk%2Bg3qaE%2F48oICRJoZQKhxOTNiMs5f7Rax5p7wvopYlXsjPJln1oOn0lwwXG5qKyuwNXD91VOPoS83TsXY9p1ukz6yTy88mKbZEqmXs3mkMCbji5OxsHcZGpJmexE4uAeu9PSrhKiBBQ6bc8AJDigED%2F1Jtw5oewa9ceUXk5Jd%2BpbTw8WCeC5qpeimme%2Bser89uXWk1DGwqGD3AQoKsji%2F%2F7piQSTnnJDTKfT2GsN2bEt5f9q2Y0rpO4fToGoOR4DUPRayioVVyiN%2F%2FCxENmO0LDNM4N%2B%2B0dTZRcnIIo%2B26u1uzknPe8v5MLzYaXKxqrFHCNwXdB0hvIeteAFykEvZwOYpHbYJIUsrXPLC4Q1knwFIoISt8jWL%2BnKdE05cyZgq%2B2KNEVR2J7caMmTHb8IFdIwyesJcPYv66TvDeyI5epANqjjDPtvK8BjqkAY74gHuix%2FPgWSLfmEqbmf3TjY7L%2BaK4Sm7eteZve5ulSswoxc3dfdhquNGoas3bV5neHVHo6n4p96Dk9EEc%2FZ1%2BKLg72AfBWy%2BrHItcZNsZ%2BnIAsGqSZKt3W%2BC%2B1%2B0fUVLdAXfp%2FzOihDg2M%2FOqegmb1Lzs1jF4uoPsm%2B05kpR53sPtTwKf%2FJ%2BojhYaNtFOpKrD%2FRT1A7Pk4%2FNkWw5rRmW3wOl0&X-Amz-Signature=e84bca731e2eefe74d5aac3a8c53356385bce3a3589e3b8cc01e526a35d6b91f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKGABT6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcjyz%2F44ePf88O93rL8tfZhMe5pIiUppZePp7s5PqtawIgbTbslJsy9F%2BvR8M%2Ba6fpeLIBfXSubSZmiruLGYij4XUqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnC5UXWx0JBsH0kBSrcAxjGwXg8TeJ3xodm2MG%2F%2FX7o2gr3ISKhKBF5UBH%2BvXBksLc0XPrAJZBJNFPMLAhiF64z16i6EeRACe8uo2ReYLFz6GIkGWU9hkD%2F0jVmlE1rD3soJpSKc9rjIu9c4rn%2B3NvsJVym9W4nR8AF7rPxDvWCZ6dnGxMw%2BEnBB5xvM0AMT1QT2tcqi2%2BIrfT6F%2Bt%2BfC3i5YDar0X6ck1DXHM9JLhhj5KaXuXzPcV4PlefC63GjaSYQ02WoD8qU6OStdoANk%2BPPHY4bCUihej6En5gRqDYSLl%2FxW5RyhkmcwGnBe7ziI0siVM4jOC9b1E%2FdC6xBosBSdV4ZvSpuiLAih6Zmrm%2BTs4dy6eQSYOiHgfYYWIfnIgJ4jlOtaZz2u04cp4iS0qV8FGzA9aihzw9fvZ2wBRq%2BhK%2FU38xyKH0U34XZoIEJfaOxGfUnmpIpgTD8fxD3sfmRQe%2BhHsx7ezkRsj7R1Jh06EmZAzp%2BjM3XVS1lU0Yeyg3nhEEfvVOBlpVuzTDxofD47KTqPAdElm7gHmceAGvN6fu79dET%2FPVJKDFP%2B%2BqDb0qxInoiwbcxUhvCEBgf6iAGz0VnJi0leTdTguURx2ktZBWSMuDoJzc8yeUCW7BkYXsqNYON5XrqZmlMNW28rwGOqUB25DUND71Sm58wZtgHpGmZXQIAtliFDPPWhn3%2FzJB6zqAgBQlRbj%2F3b8JGw%2FAUfJunR%2FvKzHHHu7wQn3m7UA0TzuVzw3r%2FxWiba2tYlDIFyFJIHul107TqpakP47vyHLqOovIO1EzxK%2FqsH19BgoKVaSO2DuluMWtmIMxxoQTzwS0vs1kgL2nxNkkPXMAXTgsj7nhXKP1YjX8zpiD0rYtSLe5XzbK&X-Amz-Signature=5c092cb863d12201377442dbdbcbdb4c48f1dfad2718a7a075120618f2f155e2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKGABT6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcjyz%2F44ePf88O93rL8tfZhMe5pIiUppZePp7s5PqtawIgbTbslJsy9F%2BvR8M%2Ba6fpeLIBfXSubSZmiruLGYij4XUqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnC5UXWx0JBsH0kBSrcAxjGwXg8TeJ3xodm2MG%2F%2FX7o2gr3ISKhKBF5UBH%2BvXBksLc0XPrAJZBJNFPMLAhiF64z16i6EeRACe8uo2ReYLFz6GIkGWU9hkD%2F0jVmlE1rD3soJpSKc9rjIu9c4rn%2B3NvsJVym9W4nR8AF7rPxDvWCZ6dnGxMw%2BEnBB5xvM0AMT1QT2tcqi2%2BIrfT6F%2Bt%2BfC3i5YDar0X6ck1DXHM9JLhhj5KaXuXzPcV4PlefC63GjaSYQ02WoD8qU6OStdoANk%2BPPHY4bCUihej6En5gRqDYSLl%2FxW5RyhkmcwGnBe7ziI0siVM4jOC9b1E%2FdC6xBosBSdV4ZvSpuiLAih6Zmrm%2BTs4dy6eQSYOiHgfYYWIfnIgJ4jlOtaZz2u04cp4iS0qV8FGzA9aihzw9fvZ2wBRq%2BhK%2FU38xyKH0U34XZoIEJfaOxGfUnmpIpgTD8fxD3sfmRQe%2BhHsx7ezkRsj7R1Jh06EmZAzp%2BjM3XVS1lU0Yeyg3nhEEfvVOBlpVuzTDxofD47KTqPAdElm7gHmceAGvN6fu79dET%2FPVJKDFP%2B%2BqDb0qxInoiwbcxUhvCEBgf6iAGz0VnJi0leTdTguURx2ktZBWSMuDoJzc8yeUCW7BkYXsqNYON5XrqZmlMNW28rwGOqUB25DUND71Sm58wZtgHpGmZXQIAtliFDPPWhn3%2FzJB6zqAgBQlRbj%2F3b8JGw%2FAUfJunR%2FvKzHHHu7wQn3m7UA0TzuVzw3r%2FxWiba2tYlDIFyFJIHul107TqpakP47vyHLqOovIO1EzxK%2FqsH19BgoKVaSO2DuluMWtmIMxxoQTzwS0vs1kgL2nxNkkPXMAXTgsj7nhXKP1YjX8zpiD0rYtSLe5XzbK&X-Amz-Signature=9baa9def6f2f788f4c4c5ed714da10bc4918794cdbea7cb275c423ce9e97a96b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZAPENQG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFayuMpSA1hdZJ2IgV%2FMFsLkLHslvQQGbuP9rKrRHYhAiEA%2B3BOiDfvUp0JC4WZL%2BqHz8Vh%2Bq7qAIRyP9OkYO%2B8GIoqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFKpoq0u6DpCELOElSrcA8s6QiXsYEavPCpi0Z4z2hYISH%2FdndpRARQ2%2FDu643lUQmShqMD90tTzcTkq4G5ZRdOikdjCfNnBjFLUwV7xQ714U5p%2BEYbVHChW%2BDAEoTxxWRN8aMGPrh6VVgSV0vC4qB97vIVSyC7ZlxTiDHdgtkRkdTtCXaMlpZ37wkepA%2BwoI%2Fr81ngsZsdb%2FAVvgSBG%2FuRRwUwHL0n5ZUEUwEG4x7OULBbZESpxArI%2Fg5%2F5lvTO50e3%2F0rSjvzdCjQt5bJORbcih8tMcW78o5i5zPPuWK3iynPHDlipVDVvzCVC8V85i%2BhmlK5ENs%2B7tmrQ7K%2B9wTq3umLyymkVB0GY6LuUQCC5WzS44JiFRP87Kz5sMlocVuGRGxhFPJc7hQ8HNlQs579s%2B0Gg6eXPrXkxTBy%2BQ4WokRTkWvT2pZIutePMYatR3k%2Bf3o0gpFu7JoSiD43DbIicqvzJMq8WgnmOeE43VsHR9JI%2BwWMVdioiWpjpuO6B%2Fwj3vlcBqavJRQJPCcOcSMahnnWcoaH5dF2Ger17w5xgJpOP%2Br%2BDDbKd1LAFAGyd9eKjg%2FODSjUdtTdS9Si0UY5uAsirBX6DkNaDOQUDikt%2B9wsyKbeFz5OMxc1JE4f0qB%2B11YkoBnbo7V2TMOC28rwGOqUBH8TsDbVrBUgXJU13gHiUpIjJ3fyTrExoE%2BY2P5CxitKZbPmz6rNtoRqALJ7TacUMvZ1LaCJsJVhGIHOmuHPZaS6CbJ1olPgWToNw%2BaME9I5AMPHljFC9crrgyS3FP1cmm17M99y5pLAaQR4%2F0CyE90qK5LQA%2F0JSaqP3TR4Wul%2BCIMmW%2BZEE2Ce4w%2BaQKzBAlIIIMjFiKjkf0pDys9pNSMrE7LVY&X-Amz-Signature=fc4b1c21d02d1f7902340fa9dfb6c569454ab4648f78b188e7066bace42e7d3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFWY6ZNB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4eHmmKqck%2FNj51Y0TbKKff8u5oUoCYF7JoABCuhTXMgIhAN97ra0kBRchcFH5%2FonJygHVY6a2KxZ5KpsAUmM%2FqLi2KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGWXd5OBbnq29svsIq3AO%2BgOAVwazF3gog3ae1jw4x3ECYWOJahrz9tmV8rTTmJeBZRR1NJfvY6DFRDAD9bDK4xOtSG7S5HC0PCrixbH3ZudkCPVqz4vg%2BEBkjhl3UV5seAd4FVliM6VuCrrKHs40IqIS1e3mDvGJQdrMTWfzfUJLy6RzeICmGvueW4dvqT%2BiMV7OGV%2BatVczVnjIQP98APU0Kxjn3Ud68BMFTGYCgnZNu1XiwDCa%2BJU8x8sS%2BuGs%2Fn2EgamYudHKj5QCptDXjxSymYtQM8inIbMjKDEkZ%2Fxl0HH%2BbR0%2BNL%2Fm3jgslo%2BEOWk9VpGWIHM4JLH9%2FimGHe%2FYqKBNUCY4JB0L1gGNZtadLr28AdcIG%2Fgmp%2FEsLLqHQfmChjvbuU1LdeApzoH56vzEvu8AcS5OYQFNphAYUILE0Q0i1iWjaNc5OFKWZ9Lp1E%2Fmrc5G9gixt2HH%2BScx6E6zTjI3tZFtRpcjBRNWhvIaKLWJUgmbhVl2cz3ENfDTwEKBysi%2BmGuAs3citlneYfTLCodliZ3bsIJDtHganPv4Nj777J%2FlCmgutR4yapoS2IFouUTU1kXz8aA4GxuOmIlH%2Br%2FPcHLB7HkVEaSFH7%2BExyjrKK2ufvplcA%2FqQZUvCARca%2FDPcS1PSfzCwtvK8BjqkARNLQvYLizQs1Ym2eSlPntP8apPVUHB4PBa1BmIQ%2FmSyPbP221YV6D%2BMlDYhmsl%2BEgCzD8vyMhoM%2BzhTGFNO3%2F36tLg2kVEGaWHkeiLWVvyihL5LmnpUkjXAEWHpVzS4dPzLftV5zcifA6iaG1DYew6FIlP4o6QuSym8unZ9fA25SWh7CwM5WoJRuEZiInaw9NI3fFx89nESL%2Be6wDpNSdpEBr3t&X-Amz-Signature=daa8a09d1f1538557c6be9a52d975c30dad6efe0d2f2c8574a598f6fbb9e4d65&X-Amz-SignedHeaders=host&x-id=GetObject)
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