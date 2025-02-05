

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=10f04c02953f714b0bbe1a2e2d1167a3d0653e4b9e8a267e6f2c1e10888c9780&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=956e765df42b38a0e174a44c36453f8484165d730f27fdfe5e9adf8f19f01947&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=e9c511922b2bbf33b0e33ff73d6a20dcaf5aa19ce861e13d4968ce03c7b734c6&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=8789c77d47a6fc9325cf8e0997c9204e68275546aae4ca419691e950a40e5a2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=e994c661872455a4c54c6fa08818e290517b149418bae04ad809358bf07bcc3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=b17633cd1bb88de9aa0af03b363dd4fdc21de7e62a593a77f5f62a33fbf074dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=33ed9415c1cebb7f7c5ff8c08d44d1a8f5c730db66f88b7cfbb426ea4fa7c90f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=b9417937701ea603a9f3f0566d40e11eb75aa2c7b26b4284461562840cf1eea9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=eed1440441bd7dd01191d1c426c3a75c88668daaa9b84208394bc8c619532a2b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IT7YEPL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCBMEmG7xaZ0K7wmXfkQRhBdAjLCJjGCSOJnYeyDf%2F9kwIgSKlLOyKtVWp6He15O75Z9WuIir7xUeMIbSrMJqFAC3Yq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOwTo9rabtcaKBiqeircA18t3dS8sMS9u0D2i6%2B4jbKj2pek53wZGfiiyxS%2FSR6emJTbYcNHYjmw640%2BSYaoB6P%2FXaIUXkRIm9T8YfpsFAV0YHGd0CsbTknnyI8WIhIAmhGckiYlB6MwoD59EuLCmyKkp85H1HJ%2BuVbZ5sOJ4Q36OHmK0Ucc4%2Btwt7cZVDu4ougT%2FUrwcOXlaLSovmXsF0PJ6%2F%2FG5bQ6XroBwFLWdsb9dtb17Et10r7ULR%2FcFHNlyG%2FnfIwNIFLX5%2BtzUz48eFw5NQe%2FlR6a9rdfajD8uXcffu2b%2FwufMIIi%2FVRFwwiarX7O%2FGrCEokrQZMueUsS0HajD7t%2FGgZzceUdd6jbgG9DFSpUXp2dA%2BypA0BvlsviM0j%2FaP8PEQ1v4LLQkBlkDqND6SF07BoXEkpKisaPjJFHMdXZSvjMVTk%2FLLbyADliY%2FkHWtpqsxN7vi79knoqO0QroJnpjEI8p1HapNHjyrBAdfAKBcyIvKyHf8kGvidLht7Bkw4Xt08LNUSdRlb5%2FLUItQnQm3lS7vT8O6Iyr0E1tZzLY3Wn38DW9G1lhcmTeTA3ZkETbce1XnxJULZskfqk31XZ4O%2FOxSkQtQvaP0QOMsic%2F5iKSNt6PmIsm361gwfVUcD6Io2oc7NkMIHQjL0GOqUBODAe7r0CN5a6ksz8EU1D%2BecsEjY0%2F5cfaJF3KHnTvo2D4X1eocYWJpxAX4w2%2BN8JiGUGutUIoVGiHwzUAlSxbVx7JMD%2B0aZRmAUUYpWTPjSPRAMMyqP7lVlAysDDPHkmJaT15tBuyC9QIzzR7MnI07AsGIyFNeDTCZYAqEOln0zTSrObfpiVvR3BB4gM%2BOasCCERzDk5oU97c%2BGsypNJDFA5xu2p&X-Amz-Signature=6424c4f7e2ad8367dde642b9f80b004c87d0b29d19b16f9eb57c563552b934c6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IT7YEPL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCBMEmG7xaZ0K7wmXfkQRhBdAjLCJjGCSOJnYeyDf%2F9kwIgSKlLOyKtVWp6He15O75Z9WuIir7xUeMIbSrMJqFAC3Yq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOwTo9rabtcaKBiqeircA18t3dS8sMS9u0D2i6%2B4jbKj2pek53wZGfiiyxS%2FSR6emJTbYcNHYjmw640%2BSYaoB6P%2FXaIUXkRIm9T8YfpsFAV0YHGd0CsbTknnyI8WIhIAmhGckiYlB6MwoD59EuLCmyKkp85H1HJ%2BuVbZ5sOJ4Q36OHmK0Ucc4%2Btwt7cZVDu4ougT%2FUrwcOXlaLSovmXsF0PJ6%2F%2FG5bQ6XroBwFLWdsb9dtb17Et10r7ULR%2FcFHNlyG%2FnfIwNIFLX5%2BtzUz48eFw5NQe%2FlR6a9rdfajD8uXcffu2b%2FwufMIIi%2FVRFwwiarX7O%2FGrCEokrQZMueUsS0HajD7t%2FGgZzceUdd6jbgG9DFSpUXp2dA%2BypA0BvlsviM0j%2FaP8PEQ1v4LLQkBlkDqND6SF07BoXEkpKisaPjJFHMdXZSvjMVTk%2FLLbyADliY%2FkHWtpqsxN7vi79knoqO0QroJnpjEI8p1HapNHjyrBAdfAKBcyIvKyHf8kGvidLht7Bkw4Xt08LNUSdRlb5%2FLUItQnQm3lS7vT8O6Iyr0E1tZzLY3Wn38DW9G1lhcmTeTA3ZkETbce1XnxJULZskfqk31XZ4O%2FOxSkQtQvaP0QOMsic%2F5iKSNt6PmIsm361gwfVUcD6Io2oc7NkMIHQjL0GOqUBODAe7r0CN5a6ksz8EU1D%2BecsEjY0%2F5cfaJF3KHnTvo2D4X1eocYWJpxAX4w2%2BN8JiGUGutUIoVGiHwzUAlSxbVx7JMD%2B0aZRmAUUYpWTPjSPRAMMyqP7lVlAysDDPHkmJaT15tBuyC9QIzzR7MnI07AsGIyFNeDTCZYAqEOln0zTSrObfpiVvR3BB4gM%2BOasCCERzDk5oU97c%2BGsypNJDFA5xu2p&X-Amz-Signature=8ab60db655f9c4e65077d4dce2090e94ac455213db210994008a78fe12b44ca1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IT7YEPL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCBMEmG7xaZ0K7wmXfkQRhBdAjLCJjGCSOJnYeyDf%2F9kwIgSKlLOyKtVWp6He15O75Z9WuIir7xUeMIbSrMJqFAC3Yq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOwTo9rabtcaKBiqeircA18t3dS8sMS9u0D2i6%2B4jbKj2pek53wZGfiiyxS%2FSR6emJTbYcNHYjmw640%2BSYaoB6P%2FXaIUXkRIm9T8YfpsFAV0YHGd0CsbTknnyI8WIhIAmhGckiYlB6MwoD59EuLCmyKkp85H1HJ%2BuVbZ5sOJ4Q36OHmK0Ucc4%2Btwt7cZVDu4ougT%2FUrwcOXlaLSovmXsF0PJ6%2F%2FG5bQ6XroBwFLWdsb9dtb17Et10r7ULR%2FcFHNlyG%2FnfIwNIFLX5%2BtzUz48eFw5NQe%2FlR6a9rdfajD8uXcffu2b%2FwufMIIi%2FVRFwwiarX7O%2FGrCEokrQZMueUsS0HajD7t%2FGgZzceUdd6jbgG9DFSpUXp2dA%2BypA0BvlsviM0j%2FaP8PEQ1v4LLQkBlkDqND6SF07BoXEkpKisaPjJFHMdXZSvjMVTk%2FLLbyADliY%2FkHWtpqsxN7vi79knoqO0QroJnpjEI8p1HapNHjyrBAdfAKBcyIvKyHf8kGvidLht7Bkw4Xt08LNUSdRlb5%2FLUItQnQm3lS7vT8O6Iyr0E1tZzLY3Wn38DW9G1lhcmTeTA3ZkETbce1XnxJULZskfqk31XZ4O%2FOxSkQtQvaP0QOMsic%2F5iKSNt6PmIsm361gwfVUcD6Io2oc7NkMIHQjL0GOqUBODAe7r0CN5a6ksz8EU1D%2BecsEjY0%2F5cfaJF3KHnTvo2D4X1eocYWJpxAX4w2%2BN8JiGUGutUIoVGiHwzUAlSxbVx7JMD%2B0aZRmAUUYpWTPjSPRAMMyqP7lVlAysDDPHkmJaT15tBuyC9QIzzR7MnI07AsGIyFNeDTCZYAqEOln0zTSrObfpiVvR3BB4gM%2BOasCCERzDk5oU97c%2BGsypNJDFA5xu2p&X-Amz-Signature=2a42888594fba8f0d0b3b1ebfd1b2c9c2e4382665641bfcdad0ad8588736d8b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=42a4a55f88f674b16ab3361699c5c2ca8e18dc0fdd663560a30607f9a83c2a48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=81190b66ddcea10c9d59d8243f074b7b894e39d2844cf0d5374ff235d502a020&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=587a6e586474057f59898eb275338162b2c05aeca0f0d0c745d93b21eaa44c02&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=751fcc6913adead8c981ab8650adf5338f499c39a9cdba0f08d1ba890ad88588&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=8f9cc78ad4972983d0453d60048814bb32326657abc4c22919b62585ddb3fba1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDRTOVRS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIDvkyTZQUFVtXJs7UQfIhIsdscCK97r7QvARtkl06T5nAiBe1gBnUpnI13Bugu83sKL%2BDCOXETWauzeRlq4dT6l9Pyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMw4qMwc5jLvFdaEeHKtwDe%2B73oAwQ2hgtHXswCUfwebdY45t9ZoyWtbhWZyWReguaaOU4UbEgHJ9xuQ7cxUfWblo11%2BPej7yyMOLSQkW33qYbqQYOtwb3y1agKFtqZDjnBJ26QmDo%2B3GF3TnkYifVYQg1RVkByfd2XOfIKLu3nGgtaU4e3H%2FoPcuedxB81eTCQLkX7y7Z8Bs%2BcKQkNeIt6cME7wWwl1p4F%2B%2B%2B%2Bxcdtndsbrk%2B1Z9I%2BcHIXaunEISOJHQeRO9qlg1XoRGOECpzdeIkHG37hL4HvrwexjQIoGaTj8uhnqfevNlgF13M3kBJSFf%2BdOHmds%2FTMsZ%2F4a0cCnfQsjJw3c2ppeTlA7jQt5SaNi%2F0XxFhnYjTje9lpmTX2RCdMeFVYxj0ptdwKXiBuZ16QRPWesG%2B0%2BPITSC6xYZgpZptjmlpV7fRF2xzaB%2BoS43MZYFQq%2BuHI1R2yE1oGR%2FEpLqSNJi4Xxb97ooGcKreF%2Bw%2BD1H1BUKAdCiI45UC1rUUduZN%2Fie3SszJvcihpbavP5pzacsKDqtzRUVusb0KJIIduNYk8lUqFhsLLith2cye%2BjwuyvoYspxJJz8m8a4%2FdPOWdqPc69H89SJMd7cHRx5mcYK47zQnyyRg0wJnk2QVvNKJwZroO3swi8%2BMvQY6pgG5bzrPHjcjwezRcv4MQiuDg4USczxhLbAsCeKdKC2NNdgfERaB4maGgK2VzBH56IJGgob%2BH0KmnWuDEddTU3ZBFkW7Mlg0Ctp0ulOB6IucCloe%2B0zWdlT3w0O6LmjmgP2fJ4D%2B%2B3M2Kd8rdiMVAMh7EbhqBeqn%2FSLwqSRQ5T%2FHJt2YO%2FY2cAW5PNpAQoiAgcIcP8h4RrUf3%2B%2FJDZQ4tONnBRHvR75q&X-Amz-Signature=2f145d45bd44c0c814c8e7302ab0ff916231519204b9a3f00ea46cbf1755edf1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUH6M2HT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDjqfUF%2BlxbAGxdfklSphzcJDzxf5jS1KGk3AwT49jHgAiEAkx1BXcFVpxvGvHcargJRy7JriTOCTNcLc%2BF%2FJTv8Xqwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFvQnIVq8rUDiH4GpSrcA4hxZ%2FfwzmGbpO8Q8Y%2BeGZP6SMNzxaORtGlnDkHyLvyTLk0bQ%2F%2FZ3IdZef6DhNbLYiQARld0%2Fi%2BBx6BUWOWU750OWigEh%2BzdrjwE0m8JLoun3046uXL%2BaxED6j5bs%2BzYwHuQxLOriCVZY6HkEw5ynaZ5gTsaDUDb%2F7w%2BMMVQmiS5idDPFJNpDcHmXFUbj1xNFgpLxzhq%2FhYIhVZk%2F9ifXaDt9gUKXruGqV7XBWrLRRXu%2BJMTPOWbkM%2BAkTsnWaq2D9rqfET9%2BSH9KkMgTmUsbONwt5cuaNd6pyFFvFYRnvJDjQLwnbelTvWEXhxuLdgXJ3RRXzqZYtLRrbZqPJ9Z3iBag2svsPgkMgTfJhvHJuFQfCisLU%2BUaWSXALWwcKkIwttKb6PPmHLGzEfqU2Ek4%2FZJ8s3Z%2FrXyHsKL4DphgYGUBIm6QjLUWeUN%2BDWaBjAjNkywzNmMkw3v5hYFRGfhppYTIh0DhJo0fAdysfDE4raB2T%2FCUFdj6oWpqlOvp0Oz4zJgI4rj9rg2W8IbEBVZhqCrHzVvUI9soDm0TBfOTQd59AJn1TY428TYh29rg00Bw%2FICE6Q9vVYeOzWOgLYKgV8X%2BaGrTuuB69PaaSrprEt%2FbRx%2FTAY%2FyHfjaiV%2FMLHPjL0GOqUBoFTHmxnMUkCcDWPGEfwsdzYPRFLyf5S6KLBvbe2eY%2FPbLwzkyVKBb5A3r4c0b2givKlAhiFvuvWnDfVYgHvzsto5h7BfUmX47yZdSq9JFYUBFc2ZM0w%2F84KuEPNM2houx0SnH9Eiz94k2SMATm5%2Bp0OsG24g5Fk4ok7eh1SR4vz7vHrq0YsorRSLSabZzGGKbvl54iV9HMuRGzRnW0HETf0QLnUd&X-Amz-Signature=4cc895e78db6bd30bb69c294e825866d1f51ecc47ef3b0c985376dc6b5acc867&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUH6M2HT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDjqfUF%2BlxbAGxdfklSphzcJDzxf5jS1KGk3AwT49jHgAiEAkx1BXcFVpxvGvHcargJRy7JriTOCTNcLc%2BF%2FJTv8Xqwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFvQnIVq8rUDiH4GpSrcA4hxZ%2FfwzmGbpO8Q8Y%2BeGZP6SMNzxaORtGlnDkHyLvyTLk0bQ%2F%2FZ3IdZef6DhNbLYiQARld0%2Fi%2BBx6BUWOWU750OWigEh%2BzdrjwE0m8JLoun3046uXL%2BaxED6j5bs%2BzYwHuQxLOriCVZY6HkEw5ynaZ5gTsaDUDb%2F7w%2BMMVQmiS5idDPFJNpDcHmXFUbj1xNFgpLxzhq%2FhYIhVZk%2F9ifXaDt9gUKXruGqV7XBWrLRRXu%2BJMTPOWbkM%2BAkTsnWaq2D9rqfET9%2BSH9KkMgTmUsbONwt5cuaNd6pyFFvFYRnvJDjQLwnbelTvWEXhxuLdgXJ3RRXzqZYtLRrbZqPJ9Z3iBag2svsPgkMgTfJhvHJuFQfCisLU%2BUaWSXALWwcKkIwttKb6PPmHLGzEfqU2Ek4%2FZJ8s3Z%2FrXyHsKL4DphgYGUBIm6QjLUWeUN%2BDWaBjAjNkywzNmMkw3v5hYFRGfhppYTIh0DhJo0fAdysfDE4raB2T%2FCUFdj6oWpqlOvp0Oz4zJgI4rj9rg2W8IbEBVZhqCrHzVvUI9soDm0TBfOTQd59AJn1TY428TYh29rg00Bw%2FICE6Q9vVYeOzWOgLYKgV8X%2BaGrTuuB69PaaSrprEt%2FbRx%2FTAY%2FyHfjaiV%2FMLHPjL0GOqUBoFTHmxnMUkCcDWPGEfwsdzYPRFLyf5S6KLBvbe2eY%2FPbLwzkyVKBb5A3r4c0b2givKlAhiFvuvWnDfVYgHvzsto5h7BfUmX47yZdSq9JFYUBFc2ZM0w%2F84KuEPNM2houx0SnH9Eiz94k2SMATm5%2Bp0OsG24g5Fk4ok7eh1SR4vz7vHrq0YsorRSLSabZzGGKbvl54iV9HMuRGzRnW0HETf0QLnUd&X-Amz-Signature=438fd93520d9a73f6f616eb654f3a3744c01f3c1c9a82d6c93c5a6bfd8b60612&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4DA4Z3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIBgGfE6FoBhGIupxfhip4YibbXImqh%2BUDAq%2FRO8OCwC4AiAahqLHA8N8%2Fwa48HiPZ%2FcAmEe%2FL0B3OpsFszhkV%2FKC9Sr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIM308KZLDShNYnq%2FXsKtwDieYKftHmCrJp7nKeQBJE3CMKgNTTkBa3KG1osa3%2B1qnW2AwM00qOb4QsIn5TDAqLog8Wg43qFsNSC1UdyrX%2BJVr3iE%2BPb2uap%2FOe9zynNmowWwXXf2gG7iChIifg1QzF%2BP2uG5k1Y%2BTngZ1qOqiQzqoYZ91ahwOk%2FDE9gUZxJzYe%2FQZJ9HBqw6Cd9ACQsDLH7hn3RxHx73yG6RZNP6wqg%2BuoazWgrpVYwt4PibUi9snflUNE%2Fzi6%2Bd5Et9sZgeFJpa%2FngW1jfv4fJpWZPjg5o2eI6YXfm4O9%2FQrGxKeZt3h3coj45qjQ60Odh1Az5g2nnrwKwP8kHa%2BezMiL%2FqaqxxTmQASFkYSXJHifUCp18FrF1ra5uc7TbcbNQJopFIyqDACxbAEueZiD2sIU2hRmp2ypAOdKH5j%2BOc0T5BLZVjFJ6aL9guZyCEF8Fltn99htEYr3zuXE94ZzRdSY0gNzab6l5iGawS6nauFGaSAUrnpGUnEuJO7iZ5bXhSLZBIOKFxNZajswMre3K1ITN6zhVrSV4Q4lj0vqdqVnneMWau2IrRLtvOmBvH1bFaALR%2Bvx%2BgeRV7Kf4HDwIh7pCxrBUUat%2FMUoYt%2BNQC15yosFdlpLgWt5zwnYka2iyXAwt8%2BMvQY6pgEjKxwNwtTdsvgrgWWV7O45YMG8PBLTO51dOqklMosGNYagz8zwVcJP%2BLfW83%2B9Ji06%2B947rYQvbTWmez%2B8XnFvQccR%2FXJQd0O3l%2B377t7fvIoi0maUSv13oDYsillhN6062dKpnEybZAOESPK%2Bh3GNfkbiEnQX7sDja8nJn3VZFxJ44UFVkurGzq2EtU6cElHEZGcv1WA18S5dk0ykX6ZLuiIK%2BSVV&X-Amz-Signature=7f9f664040d5ff30f96d9b580a8ebc000ff5fe343252c89e29e569aec608d661&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVK5CJZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIE2pVPjjYGkq9c%2FyJdUbuZt2nz5lw1bfN80BlZoNF5acAiB0hZOJBmqWLfJNVXH2uoK2azW51HxU6rrIK2jHFTZhWir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMRktBfykir0IQqRFEKtwDsU9NdC9DoYHr%2FPXYyfArtB2Mpwok%2BqHnlJZ628RYuEg37obZG3iV3CDOzh8k3izO6yXnDKHsv31Mt3225PaOAfYcKmhyFayZ%2BGVOC1zK6cPvkIY5AyB%2FKfORREj9LzSQcfekUw1tc2%2FZzVgIKNlcJ4OEMpzIB8jR2HyEHdU1mzy4rH09KbPpH9DFII0ySHAge916DULPpHWqxORymo3CL4MxWOlBjYhwIU39W8jP6hEPH2V%2F4gX6Q3xB%2BNYP%2F62U%2BvGpB%2B6rmt9vDXjQYnOPqkbu2fAzRkFLO3012TU1vBE7f3O3vo7DZNLAhyEWMeYQUJxifF9psPHGJj96XtnAPE%2BL5T9Ig5LU8dfB3agHhQt8A%2BMgzfFS5JhxCdGD91KcT9f6gYmKvzVvemoll%2B4IoE4YRoVyOceEVigVHo9hxqNbm%2FjfPM%2BPqCAhZdkPaadZ72O4MmRE7SHyAJrJNGi4yXXN26C7gpE4CWbx%2BzFg2zCMeUugu%2B8ySNwD2wPR4bS8nbLAhTDwe3xKMv8rC28JgRCUBUfb0oQrVdJJTjsAl3IUT5ACb%2FL9BN29fkVUrvVyIHITFYja3AXk9CBxE5ym9AKoqu02A6m1B9gdTdbFIjb4Ikl%2Bt46fg%2Bszz6Awsc%2BMvQY6pgEu4AX2J4a%2BegqgMIhF7cPw8ia5XgHqouGHIfhRz4U9xct8cm7ut4lzWog27wYANEOWtToBUpablpyS88vM3EdmJZoVcqF620z2AZk%2Bri2mW%2FovALka8RW0WN6SXxV42nrEP%2BQg%2FJTDUOdkGoKrRQnAgAlklVXGczTAhEXWAzDtt%2Byyg9rjaLIoIPZ2uRKmzG%2FKFO1aSmmkvKDWMXLpGsJyXyG88dGt&X-Amz-Signature=ababcafcff150db1f403fa4b1aaedff5805991d2bef6ded9db3398c1a037aee2&X-Amz-SignedHeaders=host&x-id=GetObject)
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