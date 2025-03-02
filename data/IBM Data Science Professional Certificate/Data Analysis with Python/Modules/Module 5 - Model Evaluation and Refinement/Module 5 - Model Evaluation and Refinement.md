

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=f217abb240a42b340b7aa6361156707079c399e63ee41f7ef050b5147471df7c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=af38fa1e08341b6800a12d39c8f88b1010a295bb0056e61d55f4b5da36645411&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=e82fe9694d2cec33994daa1b7f702c32488a73730d1c59014520892b3ccbe2bd&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=6473fa794968949e3ed08721708383ccee8fe291f0e73e8f949f1383adfbba39&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=c7e08ffc4ead13e0b38a61858efdb62bf391c703212b3e33a261813623fb822e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=bd4374eaa795217e9caffc064ff4923de48d36222de40629b0902a1a48d8c550&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=c2ef4e747457237525febeb274995330f574f8bf50bfe57038203d01c8b09820&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=ab6abc59923a3b779cd4d12f1a89d3b613256c55d1b2a0cf742f2c5ff9241e75&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=30a7e0882773c06eec1305f6f45cef9433686e864019fe4bfc1c486355021c57&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K35OJDV%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCICTMBmAAw6WYy5ThBou4A85960XR9AkOp003l29c1omZAiB%2BU0jBTOF%2Bpj4FGqquzhLq5lnDc8UeAjCkVjnXGGVFuSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4ERRh1f1uBaQmbJVKtwDG4TgREIKJ8jq71yrjLdao4GOmDuvn3EGI9Zcs7YEjiXEbPunDP8I3P8ZayBPNhRQzA8f4U4rWqyCNeGNF8SNudzha7hQdcfKPV2zGeXG48ULj4O803rlXS9Uqx6infyzNZYIqJoc1BLSA%2F%2B8UNq5tjE6lEnMP5XTrgyRWSJQU%2BdQAwEm%2FjmTtwhSPYW2nURwOP6d66zF7GyrQ8SNlIb4SwSIyeMMMqsFj7%2FwV7%2FLaEgCuijVRjQNRJHAWbM5yzI4X3aXGuK%2FCdXB5PqnfPpAFGtCxSwFGnPT2HG1v6f73DD3tcEitASoxxBVkORfDIoO52q6SqQX1ZLAUj1qHzxar3VLqCqZKYWDbpbz%2FbE4F%2Bey1vl9qXfLQ0AVwnCNjH2sdHJ8VKTHqWJVupdT3dHcuA7TD0eeDd9JaA%2FOxh05Vk2B2toE6f5Y0SJBF8z7gwSAjYjQtOKW3eaAZ%2F0%2FexOuI6T%2BvvkWKKjWys%2BhHK%2BYgjr8gcHlX0Ci9qhjp4EGTjo0qbQ5Hl6WybA94gMl1HD1F4JrC439kB%2B8kiFwAKqHTtX7DlvucRrUvWXdCIExrc6Y3eS0Llk0rwXlk9hmXj0RBo3y%2BmzOe13rxe958UYbCueya4U63cCJPEh96mMw0beOvgY6pgEliAeoaogiSTDOgSWX%2FzORTYSlEw4hZ96t7vZBLTSiyHyKcmytGDrqTNDMvkzd8MSaLkNyH%2FdFOhPlsPfLXeOnekvrh2sm9noUT3mQRuMv9ONHvK6hq5LUbT9Nt5eXAYNC2sgav1mLwD16Jwhmwa46fSrerGU4v39yOgZ8871e3A36NsGwGmY7hBrA6d%2Bu0yj9QK66rzgALH4%2BFtY2vc144QAEGYoT&X-Amz-Signature=7b264919215a3cf5415a6ced8c047ac2cba4952dd3c50f60ab269354d7b51b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K35OJDV%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCICTMBmAAw6WYy5ThBou4A85960XR9AkOp003l29c1omZAiB%2BU0jBTOF%2Bpj4FGqquzhLq5lnDc8UeAjCkVjnXGGVFuSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4ERRh1f1uBaQmbJVKtwDG4TgREIKJ8jq71yrjLdao4GOmDuvn3EGI9Zcs7YEjiXEbPunDP8I3P8ZayBPNhRQzA8f4U4rWqyCNeGNF8SNudzha7hQdcfKPV2zGeXG48ULj4O803rlXS9Uqx6infyzNZYIqJoc1BLSA%2F%2B8UNq5tjE6lEnMP5XTrgyRWSJQU%2BdQAwEm%2FjmTtwhSPYW2nURwOP6d66zF7GyrQ8SNlIb4SwSIyeMMMqsFj7%2FwV7%2FLaEgCuijVRjQNRJHAWbM5yzI4X3aXGuK%2FCdXB5PqnfPpAFGtCxSwFGnPT2HG1v6f73DD3tcEitASoxxBVkORfDIoO52q6SqQX1ZLAUj1qHzxar3VLqCqZKYWDbpbz%2FbE4F%2Bey1vl9qXfLQ0AVwnCNjH2sdHJ8VKTHqWJVupdT3dHcuA7TD0eeDd9JaA%2FOxh05Vk2B2toE6f5Y0SJBF8z7gwSAjYjQtOKW3eaAZ%2F0%2FexOuI6T%2BvvkWKKjWys%2BhHK%2BYgjr8gcHlX0Ci9qhjp4EGTjo0qbQ5Hl6WybA94gMl1HD1F4JrC439kB%2B8kiFwAKqHTtX7DlvucRrUvWXdCIExrc6Y3eS0Llk0rwXlk9hmXj0RBo3y%2BmzOe13rxe958UYbCueya4U63cCJPEh96mMw0beOvgY6pgEliAeoaogiSTDOgSWX%2FzORTYSlEw4hZ96t7vZBLTSiyHyKcmytGDrqTNDMvkzd8MSaLkNyH%2FdFOhPlsPfLXeOnekvrh2sm9noUT3mQRuMv9ONHvK6hq5LUbT9Nt5eXAYNC2sgav1mLwD16Jwhmwa46fSrerGU4v39yOgZ8871e3A36NsGwGmY7hBrA6d%2Bu0yj9QK66rzgALH4%2BFtY2vc144QAEGYoT&X-Amz-Signature=5c08cebe454c1419f5bc4f91381f7386aaaa0979055b1164fad53f16855a646d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K35OJDV%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCICTMBmAAw6WYy5ThBou4A85960XR9AkOp003l29c1omZAiB%2BU0jBTOF%2Bpj4FGqquzhLq5lnDc8UeAjCkVjnXGGVFuSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4ERRh1f1uBaQmbJVKtwDG4TgREIKJ8jq71yrjLdao4GOmDuvn3EGI9Zcs7YEjiXEbPunDP8I3P8ZayBPNhRQzA8f4U4rWqyCNeGNF8SNudzha7hQdcfKPV2zGeXG48ULj4O803rlXS9Uqx6infyzNZYIqJoc1BLSA%2F%2B8UNq5tjE6lEnMP5XTrgyRWSJQU%2BdQAwEm%2FjmTtwhSPYW2nURwOP6d66zF7GyrQ8SNlIb4SwSIyeMMMqsFj7%2FwV7%2FLaEgCuijVRjQNRJHAWbM5yzI4X3aXGuK%2FCdXB5PqnfPpAFGtCxSwFGnPT2HG1v6f73DD3tcEitASoxxBVkORfDIoO52q6SqQX1ZLAUj1qHzxar3VLqCqZKYWDbpbz%2FbE4F%2Bey1vl9qXfLQ0AVwnCNjH2sdHJ8VKTHqWJVupdT3dHcuA7TD0eeDd9JaA%2FOxh05Vk2B2toE6f5Y0SJBF8z7gwSAjYjQtOKW3eaAZ%2F0%2FexOuI6T%2BvvkWKKjWys%2BhHK%2BYgjr8gcHlX0Ci9qhjp4EGTjo0qbQ5Hl6WybA94gMl1HD1F4JrC439kB%2B8kiFwAKqHTtX7DlvucRrUvWXdCIExrc6Y3eS0Llk0rwXlk9hmXj0RBo3y%2BmzOe13rxe958UYbCueya4U63cCJPEh96mMw0beOvgY6pgEliAeoaogiSTDOgSWX%2FzORTYSlEw4hZ96t7vZBLTSiyHyKcmytGDrqTNDMvkzd8MSaLkNyH%2FdFOhPlsPfLXeOnekvrh2sm9noUT3mQRuMv9ONHvK6hq5LUbT9Nt5eXAYNC2sgav1mLwD16Jwhmwa46fSrerGU4v39yOgZ8871e3A36NsGwGmY7hBrA6d%2Bu0yj9QK66rzgALH4%2BFtY2vc144QAEGYoT&X-Amz-Signature=089d3e25c7a44447e4c6b85680ee69d43fbe3c8b0d49366ae7d199b7424b1807&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=03bdbb6249ff7e30e5d943f3c18e18de95572a8fe31b68466bd8f924d6e24067&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=ac33a25d38eaf3c7598eeaccaaf0141b2902334834669d4a32a64e3908826700&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=0b249cc78cd797ccd2a49bc2b4325f4e12b9efe92f8782e795d82ee739c4260b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=619c269e89e6757d238b5f426ca1fd88eadbd085e157d6d7a52ab71a6723cf7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=0c09424f0b9ef9d8be12f8b8f808ac414bd3ef67c2d76b0f45f2fbea7f839602&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=fecae1d06b19c7294a261a1254e3209a7de48de0a6e1b4cf07fa4bdbe01a1cff&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC6XM7XS%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIFS6vXYVcpgHxpMAVBk7MWRh8K8e5skDCbmfMrXAvR6%2BAiB7GCy87iKmuXVDuGh%2F%2Fo9h5mLbtkDEYZymlHY2SKt2aSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhohkBing6C83IAeRKtwDuvPd%2FBGcJVZCiykYIzS%2B7qNFzZU95OAJ5RqK8NCklhwEp4Oivki2QdhSAdNizh%2Fj%2BdtjUQA5r5sPrfaYyWB7FbDMVnI5rhBXwTyfILjhP%2BlR9FGJ%2BPvX%2FX7mp%2FD%2FK10gwZuWhmMr8B%2BW57fJF6%2BfsfGXax%2Be3evZK39YIQAFeUjD0itaA4Ftm6JBc0T2b0VdxiHZ7L2VcpZySeeiAW2llN%2FTrRvfLrBGYgeStbxElkxW3fA63IKOTftdSk99%2FHO3oHmxB1IaFp5t8PIJVHSzdLYl2j%2BVUDsfO2YHeStUM%2BDDmZhwErCtDanbdiZ8yBqlRJkSoIyXJTjX83gQmZIoFEOOz1mcPXQ%2F79I7xnL%2Bp59hu7FmTf46XHKU58qPPbiHN7pKi79gNUBQjdyjxJHlxsKlFHrEd8mn%2BpyWETX4en9yRuxjs8Tq%2BzwhX9tr6mKo7bTep%2B7rBWlppDhBn91rItIWPdSM5Qiw2lAZF3dE8Z1%2BjjIoM49JL1Y6WojrcZWorSRxT5NPapAiZ6yn0v7Xn8amcdjTfOSKQ1yQKPni%2F9scHbvbw4q4VlQ0B99O8OOeKFuBeTl1mqu92mOvaa5RK6D2gNWVQsi%2BzUdDd3dcCNqEXx2B4RQQ3D4zHSAw%2BreOvgY6pgF5rSbOykS88xJMcKl43sCrK%2FBtfWCFedE%2B1QqxG%2FR3UbG9b4C%2F3ko%2FpWwKX%2BAo9CXsRRNEw0F0jYQ%2BnxSUhMlRTIEt4Ti%2FeQvmid7jVcO3osyKi1oNj3ODmZYYWDAtgGZEhag21HEJrfkzaPgcTY1lFwhX4kkE5YkPYGwikaF%2BX67E8jt9IxrIejrpN0MXj8SJHk2CPmVoMefROcCQoo%2Fw5Phe8m0C&X-Amz-Signature=1e46384585416f9954e9c858b390b7de09972309e3f648ee93df027232d58e79&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC6XM7XS%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIFS6vXYVcpgHxpMAVBk7MWRh8K8e5skDCbmfMrXAvR6%2BAiB7GCy87iKmuXVDuGh%2F%2Fo9h5mLbtkDEYZymlHY2SKt2aSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhohkBing6C83IAeRKtwDuvPd%2FBGcJVZCiykYIzS%2B7qNFzZU95OAJ5RqK8NCklhwEp4Oivki2QdhSAdNizh%2Fj%2BdtjUQA5r5sPrfaYyWB7FbDMVnI5rhBXwTyfILjhP%2BlR9FGJ%2BPvX%2FX7mp%2FD%2FK10gwZuWhmMr8B%2BW57fJF6%2BfsfGXax%2Be3evZK39YIQAFeUjD0itaA4Ftm6JBc0T2b0VdxiHZ7L2VcpZySeeiAW2llN%2FTrRvfLrBGYgeStbxElkxW3fA63IKOTftdSk99%2FHO3oHmxB1IaFp5t8PIJVHSzdLYl2j%2BVUDsfO2YHeStUM%2BDDmZhwErCtDanbdiZ8yBqlRJkSoIyXJTjX83gQmZIoFEOOz1mcPXQ%2F79I7xnL%2Bp59hu7FmTf46XHKU58qPPbiHN7pKi79gNUBQjdyjxJHlxsKlFHrEd8mn%2BpyWETX4en9yRuxjs8Tq%2BzwhX9tr6mKo7bTep%2B7rBWlppDhBn91rItIWPdSM5Qiw2lAZF3dE8Z1%2BjjIoM49JL1Y6WojrcZWorSRxT5NPapAiZ6yn0v7Xn8amcdjTfOSKQ1yQKPni%2F9scHbvbw4q4VlQ0B99O8OOeKFuBeTl1mqu92mOvaa5RK6D2gNWVQsi%2BzUdDd3dcCNqEXx2B4RQQ3D4zHSAw%2BreOvgY6pgF5rSbOykS88xJMcKl43sCrK%2FBtfWCFedE%2B1QqxG%2FR3UbG9b4C%2F3ko%2FpWwKX%2BAo9CXsRRNEw0F0jYQ%2BnxSUhMlRTIEt4Ti%2FeQvmid7jVcO3osyKi1oNj3ODmZYYWDAtgGZEhag21HEJrfkzaPgcTY1lFwhX4kkE5YkPYGwikaF%2BX67E8jt9IxrIejrpN0MXj8SJHk2CPmVoMefROcCQoo%2Fw5Phe8m0C&X-Amz-Signature=56ce886065a06e1a28ecc737f427d9711015309b01ac68bc8397502668618fed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAMQ5XJR%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIE5VDSfIzCiuoU1xyGA0T6RCswrb99K%2BtWDKLcRKb32jAiB97gIcQ1zpGEnJFhVDYDOg1fdvX2cq28Yvhfg6%2FvQ2%2BiqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3xywajvBsWZVAxERKtwDkUTkMboLWec8Ytf6Sek2QXfeqEdAGlWu3ONu2BVW3gEGIsiRi%2BgxtHGv18hhW142Rlhf5ht0Kx6%2Fu%2B3MvGBhQRCYR0%2BstjRfHA48guMfmqrJNYVDavw1wPtSWZqiU1kVVi3e5hbck%2F4jzTakqoPVwfS2uPE3kgOe1%2FSWqijBc60Pfs1M4uzvtuN8tYF6cceczw96rBMvtOFlaef7iB5FjzAO8y5%2B5TwH%2B72I9CkcQd8el3qCLASTg4YiByCGHYmIro%2FrHbkJhLT%2F5nn1VAAG7XdSPrugOw1%2BCw%2BTAytm6qVKplFTjRrGZaMFsmkOh61e3YpnmJm9ebK09wodnJIDCbWLEzRbRrTEn37C0arLWj%2Fj6hLBy2gTdpJpG%2FtW1xQiCzzcxWpFkQyjJCxGqx7VozaIfHiNa%2BRs40qGi68HBhlpkMLJUvyZPG5XZp4kc4pqaFk%2BFR66CwQXtxR7dq3H6KWEXW5yLyjpDDopGFPKBj5No5kFlTRvsIyQZ4sGnzB8P1pABMpvhXKT9P%2F6RZ277O2jnX5uf8gCMZU0MEZBHZwu%2BDV6cyq3HJR9Y3x1R2noJMF8aPw98chlrFBF1CIjPrn0ZmPzNktEUPI2RqvSWDIpbrvBD8KILysw3qgw%2BbeOvgY6pgFU72KsgQb5faFykEYeRb42Uwm7od8WIfchi6RB%2FQJZP49WPm2GqTmtzpl6Sa1ENvm5baNyy30QBiC7LMXQx131wMgQH4LQab3iI0ffou9g2PvUFT5XEypPpJqShCVLNEBZKs59VROr6wNbMgxFuPosLMFduGD%2Fa9F4s2P%2FlTMtMoPMTl8KOjkOlydPtgOTnOxXw6S84PB%2B2lDrRjjZTbeSCdpoPRUU&X-Amz-Signature=23ee64ca56e5d0ec0e94dbf0aea7f3eebe7695727f8dbb50cb5ff6034ce0b680&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRO4XSS7%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB3B%2B7sX%2Fr56Xk3OAbUGURlihG7PcampY0dCecc2KtcsAiEAkwxEM5jp96B87RDTdm6M8zaUpEU8uG9UOrr%2BDfv%2Fhg4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ1CyXSj5mW9w31wCrcA4UUyO4797gRILSL%2FVZbgLbHlAjTJH9WBBn%2FqwFAseQbAYteO%2BfEtmAmdWYIn56LML1IitgISl09scmB2PNEEpPtcm0pBW%2F585ukE%2BUeEwMgemZGfcWeNTIYHbBT41r1vKtIGd%2BcGuuKt6B5XVMrDuvteDd7lzLWngh7D%2BCDWohY%2FQvVv03%2FocwQUiVsUXT7dvzk8tYe6zB7Nno5KJHjg4ntu%2BnBUT2Eg12YtqcfL0c1oQGQLHbY5pK6mPw%2FDDYBlY1widpNNuwGXN6fhDCTwDO1r6cQqIHALEiol7sFWu7axyZqx4vbKbuG70OvZ%2BGk0AeIJ1aUMgVARcbM5ZF6iayBcdK9%2Fc4DbfcWsReH%2Fi0ih9cqLCi7sIdYz4BPMUFH3%2BO4vK2MLkLup00fB0ZJoFIPqoOnYvyM051sLk%2BI1vKxN3Iv78bs93J0v7nzN1vMHC6LF5WsvyhuqPGnyIiHiu8xzMeBvWq7Jkzq7Wour1u5rDM%2BuzFw3YoK9Up4Af4Y0QAcLoJBQVtJaCSnynzdZj1%2B4Ij913PfF1fbPlmMUBOs3Gf7NeE2cuEUtqCB%2BF3TEgVPGFIBZcoRYkb0lYAHQzThLA%2Bf3jAoVO86bb3RfDCr0Ce%2F7m5s42W2jv3gMLm3jr4GOqUBIidwweVlHFMgs3eV3EuBJKSUgzkGoY6WGpopdtn8%2BKr300Zwl4V8DIPOrJ2inxVd5QNonEQPRP4NDtPVL5iz3zlMkEirnQIJxcq8bpVqtvYwCM40BfAZ%2BK%2B0blc0kT2pr58haeuUqnrWqRyBYQFNeviBd9K4f35chV43e3IUwTU2Jq%2BOLWp8ZS9uOpzYaqsskshdat2X3jvKyJf%2FbASYqc34%2BnON&X-Amz-Signature=03c1758af6d6c49c2e79714e0931c9f2ebdca23b07037e33ae7de9aa8fb18751&X-Amz-SignedHeaders=host&x-id=GetObject)
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