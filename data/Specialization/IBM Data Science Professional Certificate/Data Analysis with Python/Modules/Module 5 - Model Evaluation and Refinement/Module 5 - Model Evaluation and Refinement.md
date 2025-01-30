

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=689f57d59ff588f2a43fcddc233627881e4b71be1c1da442fc06b8dd350f7e5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=06dc6173fea481d39501002650e8a2b2ed8989036da5c6c69729db2580a9c696&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=41a4c7d7895f2e460ad3d22aba992bca9f6ab070ace732bb87e38492f9dc4622&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=718aaed092d81289e057aa0685632e044edacf719539d46fa7887e84d6970c6f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=0cab5cb9b3f233b46230e9f4f82753fcd305ea3952477eee19cbb1a88e8088d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=876bf2aa9e106768cc666e6c22d9c1edb30a2575f1da5665e54ec770a523baec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=829b3c7e72226769e449383a9a271ee9ce5664b746f7b6a0463bba879f375379&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=6ae357b1e119c415e6392d357c6c1c53592425221dde59c1731f21ddac7dadea&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=ec93d8ac019dbbe3f9070557e0a8037396685656ae0bf9cd5d9d2fc40bbbeccd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S267FFKD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpU6eCZIVSnGQlsEH51XL%2FudJYM2Q3HM7x01AIVpUsEAiEA4MexowdBataD%2B0r%2B0LDqr3C17TqHswbT2jgGFZd%2Bv5sqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCykHVIWmU0fqknXHircA6BvU5bjMQnTt%2By0x9SwdwAD0w29EjPe%2BdAFy1%2FFGSPFNKtOgznZfau%2FZ3Jp5peyvKW6JsmmK7wfjq8LigHi2fAuRu7Y8SZWxSAtYS6zTL67pzDCKmclAGR9Sz6ThcE6tGPb1wmX0nJ6JMYSxKYev1vAJgq1i5orWIBkOdgveh3zyzA7Hgx4QQoy8gL4%2B8vNmDZZC9bfn3zjC454F5ZBh1mnkubnEwRupUscYPDKj4RjpET2KMHDXyxJ1mioaSflMjJFF2kCnjEd4tADY9%2FVLWw2WU0oPf8S32sSBNNiLN87ZHe1o2VuSTs6pCMPntV34%2BsRjIH%2BAJjzhuL1nNK6NInva66XgJoaoVdqANpa5uAZThNnIyWH6lPTspHFGCIzDhFo2tvYEW8usbf3BZ53shOLo9iMDarkzO2cTwziJMhgcj1cmUTrGe3x2piN%2FVhGTFG4gdLpTT4lRGvphK5E5XnrJFrHHFqrC3hSjHtb%2FE%2FIYlPpmxrr5KNuJDYSIj4qCBQUwdLztj74rxwHAdkhcc14HV%2Bx7PiwT6%2FasGJG7FT3uJ7ZkiT2%2BriByRvNUpgoppUC4T2pKrA4IjobJzJs3DtSj5RVUqHhaQceb5JF%2FVfLOKUY0nrZA56lzzy9MO2x67wGOqUBm3to3Q9ESsLah41qWGs%2F5G2EOQ9Veg3c3gHjMEBAsrlRZg4i3veD7KL%2FjdT83nTbbSt5ua6Un7eVS5pliRbKO9Pa9m9i1gl7AFVS%2FJ%2FexPhCw6e1niSUuEJT9oCnDDBOYmdnALg7bVM9H3qXypoGoR4ulPsh7z6fqvXTpFR0EWqelIrSNffd%2BnnydruwWe6xfXjm7XUReMaGckH6%2B6o8wGvhrAOp&X-Amz-Signature=ecd9bd2eb3e36c304ac0e42aa100a07610dcfb274aaee75705e10efe175ed4c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S267FFKD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpU6eCZIVSnGQlsEH51XL%2FudJYM2Q3HM7x01AIVpUsEAiEA4MexowdBataD%2B0r%2B0LDqr3C17TqHswbT2jgGFZd%2Bv5sqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCykHVIWmU0fqknXHircA6BvU5bjMQnTt%2By0x9SwdwAD0w29EjPe%2BdAFy1%2FFGSPFNKtOgznZfau%2FZ3Jp5peyvKW6JsmmK7wfjq8LigHi2fAuRu7Y8SZWxSAtYS6zTL67pzDCKmclAGR9Sz6ThcE6tGPb1wmX0nJ6JMYSxKYev1vAJgq1i5orWIBkOdgveh3zyzA7Hgx4QQoy8gL4%2B8vNmDZZC9bfn3zjC454F5ZBh1mnkubnEwRupUscYPDKj4RjpET2KMHDXyxJ1mioaSflMjJFF2kCnjEd4tADY9%2FVLWw2WU0oPf8S32sSBNNiLN87ZHe1o2VuSTs6pCMPntV34%2BsRjIH%2BAJjzhuL1nNK6NInva66XgJoaoVdqANpa5uAZThNnIyWH6lPTspHFGCIzDhFo2tvYEW8usbf3BZ53shOLo9iMDarkzO2cTwziJMhgcj1cmUTrGe3x2piN%2FVhGTFG4gdLpTT4lRGvphK5E5XnrJFrHHFqrC3hSjHtb%2FE%2FIYlPpmxrr5KNuJDYSIj4qCBQUwdLztj74rxwHAdkhcc14HV%2Bx7PiwT6%2FasGJG7FT3uJ7ZkiT2%2BriByRvNUpgoppUC4T2pKrA4IjobJzJs3DtSj5RVUqHhaQceb5JF%2FVfLOKUY0nrZA56lzzy9MO2x67wGOqUBm3to3Q9ESsLah41qWGs%2F5G2EOQ9Veg3c3gHjMEBAsrlRZg4i3veD7KL%2FjdT83nTbbSt5ua6Un7eVS5pliRbKO9Pa9m9i1gl7AFVS%2FJ%2FexPhCw6e1niSUuEJT9oCnDDBOYmdnALg7bVM9H3qXypoGoR4ulPsh7z6fqvXTpFR0EWqelIrSNffd%2BnnydruwWe6xfXjm7XUReMaGckH6%2B6o8wGvhrAOp&X-Amz-Signature=3886a04b9c786acf8f3b3e48cd2031b52d87de15c54db26905f1b2c78c289491&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S267FFKD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpU6eCZIVSnGQlsEH51XL%2FudJYM2Q3HM7x01AIVpUsEAiEA4MexowdBataD%2B0r%2B0LDqr3C17TqHswbT2jgGFZd%2Bv5sqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCykHVIWmU0fqknXHircA6BvU5bjMQnTt%2By0x9SwdwAD0w29EjPe%2BdAFy1%2FFGSPFNKtOgznZfau%2FZ3Jp5peyvKW6JsmmK7wfjq8LigHi2fAuRu7Y8SZWxSAtYS6zTL67pzDCKmclAGR9Sz6ThcE6tGPb1wmX0nJ6JMYSxKYev1vAJgq1i5orWIBkOdgveh3zyzA7Hgx4QQoy8gL4%2B8vNmDZZC9bfn3zjC454F5ZBh1mnkubnEwRupUscYPDKj4RjpET2KMHDXyxJ1mioaSflMjJFF2kCnjEd4tADY9%2FVLWw2WU0oPf8S32sSBNNiLN87ZHe1o2VuSTs6pCMPntV34%2BsRjIH%2BAJjzhuL1nNK6NInva66XgJoaoVdqANpa5uAZThNnIyWH6lPTspHFGCIzDhFo2tvYEW8usbf3BZ53shOLo9iMDarkzO2cTwziJMhgcj1cmUTrGe3x2piN%2FVhGTFG4gdLpTT4lRGvphK5E5XnrJFrHHFqrC3hSjHtb%2FE%2FIYlPpmxrr5KNuJDYSIj4qCBQUwdLztj74rxwHAdkhcc14HV%2Bx7PiwT6%2FasGJG7FT3uJ7ZkiT2%2BriByRvNUpgoppUC4T2pKrA4IjobJzJs3DtSj5RVUqHhaQceb5JF%2FVfLOKUY0nrZA56lzzy9MO2x67wGOqUBm3to3Q9ESsLah41qWGs%2F5G2EOQ9Veg3c3gHjMEBAsrlRZg4i3veD7KL%2FjdT83nTbbSt5ua6Un7eVS5pliRbKO9Pa9m9i1gl7AFVS%2FJ%2FexPhCw6e1niSUuEJT9oCnDDBOYmdnALg7bVM9H3qXypoGoR4ulPsh7z6fqvXTpFR0EWqelIrSNffd%2BnnydruwWe6xfXjm7XUReMaGckH6%2B6o8wGvhrAOp&X-Amz-Signature=e6abb169ab13d332c0d6061be10892782cd3bd702a674e29158a4f4c1e4b9477&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=0854b12f0275b2fe72c8c023a880f66b43c57821810c609fbb01d5321df12212&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=3475751b3d972cb7e8092afc38ee44933cbc4830463e0565111ff5bf4e9fed40&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=911d275185a2d84d6e4107f4e39900b5f0b843d18738e36a3af8db39daddad45&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=a175a2f853d9077cd9d14b998d31399989d4855e721dd014259c693b508bf88a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=26c0a8f57f1b835cf27d66f9721e55af1001019497370b3245be5a26a91d7062&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDZG5AE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZmHONTw7kxL8AGvirk3Mmax%2BqlRqYwa0bjSUaTy6L9gIgM0dOBhpPPkxbDMrVEcMNpRxbJ05dCq4AJoBJMzqBwdwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZv4VTdCOvLv8FklCrcA%2BePBELXsYG%2FW3jtKkWaCC8f25BZZ%2FlQt3DED4vw%2BmdQDJf8Bk4iaugDYNzNsdM4EgPEBTnPYXRlH706nB3sd0Y6pE0lRCfr5pEHVtAZCVLuw%2B4iSmWSC9aHFkzia%2BcmFAYNzUjfjKXK2JXaCTCTbVdbJ7h8jr81EYXcVB7fRrliLs3FoLLOdQjMkDFAbMTN3HR%2F%2Fu9ts9VYJFmrELNcG2f67bNtJeqTlrEKx8czoqTfTMUZODU9mu%2Bhb4yCoaKDNfVjk2h9ZY3ML1sA3naSscl3a%2FAY4D93maWB7NgqGsPPbcSIv73TRAktZ%2FWpQyKxfoBMRiY8xI35O5UAWqjjq8Js4imaHA9PEAaji3FU5SnR39JY10%2Be9loDlsLf22vXfpnHSnkBeLBj%2Bi%2BXOnNp8UPxsEGPJt%2F0v7euEx2z1n0%2FzycYKfGJxmOMP11fJYRnY%2FKWxLTWOH8J%2BbzrBNG8QUaYi8SyIzXwON%2FDkHJ9YaYngXThSpmK6O2RP0%2BzMYGymnCNTcSCRO7r%2B35uRgZDWop%2FYMhmz1aMuPB%2FOlPjCOjqlGM7dGvtyF99LaUzcy1IrSq1WH%2FMxLjbPpc6oFbuVRX7X2MfulGAv%2FkMAfvPromBWlG2Hz0%2BDlpCnwRpMP%2Bx67wGOqUBuxf0eLtjkgs9OLLhJNezxQkmr0NKgUVcAXNRaUJO1Arsy4d0yaBqCMuJZnt8fzTl2rhiqUqhey6dvJTMUTEZyXCmmq2OAfdKSbSypQ9UkfmFkmz99YclTqwQIWrJLe%2FNJ7I5Cccw6P1fK975KUMNM190lkSxYBOAwX7tVIYWqSXGVRdnLETmwPFlMZXXfR10%2BNGBcqzn4s%2BSi9rez3stKZlVj6Ff&X-Amz-Signature=3a8768b5db337c0fe55e4361341bff4598513a1dee707d0e4fed875c00a86e60&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL2ULHNJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD98LPMBgX6trl5uKdZ3xSKFNCRfQBt8N53PEG1vs1X7AIgOu5BQ%2Fzs0INt9VeGcXXb6vyJNU4WMO3fQwGG2M%2BOPCUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBOqGmkJAWI6VTrFeircA5dt62W2oqnADImS7lg5GNFdPamNfHoExk%2F5LlkbXapTRX76rbY1FLjhEKANOpptv64ekQ4UrjiKN8yDhzl5bujQEdDObizd1CmMJuG%2FlIkCIJKoDMHXiE8VhoSkY3wD01%2FNB8mT10ofG2hos7by7pLsWZGFdz2lQ7Kz%2FHisNrONZ2B9%2B1AtdrcuJWHW4CtDXLApvjRB1ij9zk8NFI3qCD6VM1fTIFuqrTnwWINQ0H9b0MUX8TwVPcYea7YIDc8t7MM78d04WWDWK7FzKtm1Kj6GW5rH%2BDI8SOWLcTOIMJWPGeMeCDpCF6GANWe8M6CYE0RbIBzlEy0XsoiuVh71%2FpoaCGLUlQF7LdeY6EYniWjMTYVfcjDerW0Nwxn6tN1KMJQH4JEl8%2B%2FFNPGFGa5Q%2FAx%2B3TNm7WQM1ocwM6to9xnI9aNxqhzVulQOPQRZNfnhN1XH0G1KLn7rajSbg9fsPFOutuj6CU3RJTPY12iUvYAjrpOvX%2F3XmN35KRgLagWI5R%2BKdFl6bhams%2BxtyI%2Bh0V8XpU9IVaTBQ8xrAgudd2WXIGr7BJr8ZHg0EkU8QzXwnqSOclb88pHRia446wAo8hcJcSZwn97%2BeXU4Hwo9T2Xk0qDWpoCJzhFLzUGnMIWy67wGOqUBmZT%2FG6iiU6NGbsmM%2FUO1LeHUv88yqeScOJbeEFYWEsqZE37hA3zcw4pPzND%2ByVftEjX53Nnh8kY01bXf0sVicbqibR0zm1xjFai8oarf4l18HPKuVQwYw6ZnBKBz1QeP%2Fm%2B%2F89DPK9tETLfllaGrIhrI6TXFPuVafeMtPKnlILax66Amty%2F6kTRtnpafXnBruYiunqqzgO0zWtYKuEkmOJSwClYW&X-Amz-Signature=43030baa6bb3e3acbe4f167bba656c41e4165a87f7e8895fdcc672b25578060e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL2ULHNJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD98LPMBgX6trl5uKdZ3xSKFNCRfQBt8N53PEG1vs1X7AIgOu5BQ%2Fzs0INt9VeGcXXb6vyJNU4WMO3fQwGG2M%2BOPCUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBOqGmkJAWI6VTrFeircA5dt62W2oqnADImS7lg5GNFdPamNfHoExk%2F5LlkbXapTRX76rbY1FLjhEKANOpptv64ekQ4UrjiKN8yDhzl5bujQEdDObizd1CmMJuG%2FlIkCIJKoDMHXiE8VhoSkY3wD01%2FNB8mT10ofG2hos7by7pLsWZGFdz2lQ7Kz%2FHisNrONZ2B9%2B1AtdrcuJWHW4CtDXLApvjRB1ij9zk8NFI3qCD6VM1fTIFuqrTnwWINQ0H9b0MUX8TwVPcYea7YIDc8t7MM78d04WWDWK7FzKtm1Kj6GW5rH%2BDI8SOWLcTOIMJWPGeMeCDpCF6GANWe8M6CYE0RbIBzlEy0XsoiuVh71%2FpoaCGLUlQF7LdeY6EYniWjMTYVfcjDerW0Nwxn6tN1KMJQH4JEl8%2B%2FFNPGFGa5Q%2FAx%2B3TNm7WQM1ocwM6to9xnI9aNxqhzVulQOPQRZNfnhN1XH0G1KLn7rajSbg9fsPFOutuj6CU3RJTPY12iUvYAjrpOvX%2F3XmN35KRgLagWI5R%2BKdFl6bhams%2BxtyI%2Bh0V8XpU9IVaTBQ8xrAgudd2WXIGr7BJr8ZHg0EkU8QzXwnqSOclb88pHRia446wAo8hcJcSZwn97%2BeXU4Hwo9T2Xk0qDWpoCJzhFLzUGnMIWy67wGOqUBmZT%2FG6iiU6NGbsmM%2FUO1LeHUv88yqeScOJbeEFYWEsqZE37hA3zcw4pPzND%2ByVftEjX53Nnh8kY01bXf0sVicbqibR0zm1xjFai8oarf4l18HPKuVQwYw6ZnBKBz1QeP%2Fm%2B%2F89DPK9tETLfllaGrIhrI6TXFPuVafeMtPKnlILax66Amty%2F6kTRtnpafXnBruYiunqqzgO0zWtYKuEkmOJSwClYW&X-Amz-Signature=c989ed43d3ff4c80dbcb60e7441e8ac8db968786c230ad9122ecccc14cfb1364&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=ea5a7627cc963d6f2cd6c74bf210b2d02a3ee6a5b8ca915c55b89aa82b689c70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIUSWK4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaGx1iCSiir80Qw9s8A8rn4wsjWRb7KQFqmYxU0JSZQAiEA0Zt27XHh5tecBRYZxl%2FwYMmgZmzwXgqRie6DybXMOA0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0CPNU4djYr3Lk%2BESrcA6XUII3Xq6USjNXzM5E3VUSC4jbGCThWDCCGfnKDyn4W8Hq61YKxiPF6PT9XWp9V%2B0wowwbwKEOXcMIJn2BiCO6PosNr88WRN8wUPWkLQ2wSIptgy8kF3SNpdbuImy6WOwaLFiEJfz2Lvmcqes0jItPuQ6AsTY1l0SSbQs6Rmne4mS7WWLoHoz2bZiWlyMDqU21eyaH%2FDMbQugPAIlKYT0VtN3Hi7br0qfx%2B%2Br0acK02lZiMajLF49fZlkfUeDPgl47lwZx3E8If9E%2Bq84wM8SjhO1hd2G32WNmUrOFQte8BVi5sFct0%2BMvm8bXRjnBsg1Ls4VvsIlTqu%2Bzbz3zq9t%2Fx6BFE44a8cmIcfOMNFhIco52CzfLfsJDSREw%2FzFzxHr8L9o3ylQ%2FZngtDO76Uc5pU9A%2FS0p07tdJzJckPwRShNQroLSvEbUxRfkrZsTCsUfpz31SnrBA%2FdQGbKhREnWjHEIwnaUEpG9LppmdLgN56ETr7AI5Hjk8X2%2FHgxcuhOZajkmgz%2FIZdVPOoEUZwxjXsPflwn%2BGKmA0ch9aDfRbAjl9eElJ7ns39Mvjh6iJi5wLPIAtcV%2FaNNncQUdBbfMgUSgVn%2BBDUQ7JiV3%2F4hSphJ%2BIyRaKUYxG6MvtLMK6y67wGOqUBCM%2Bc3MSZpXbYCpyD5PnCmEuZyeh41U0%2F74ZSWuOcj0ypOR3XqQGsaZdx17vopBcRCnipdYYvu2CFCIHm%2FW06%2Ff%2F%2BK6lzWIR8rMBBrYpXVLpS%2F6I%2B1m3xbXC8SGcXLaoo0abIjM9f6AiN%2FCF64FaG5x4cn6I2NPyJITlS9b9G5dLz1VZmt1PuYOmobQ3ed6n8LZe3te7DAJye5tPNRUKI8QnNyCbV&X-Amz-Signature=5c9f21a90a8028554be7b86c76b320284d0205aa052db1a8c1612a6ee9dd4239&X-Amz-SignedHeaders=host&x-id=GetObject)
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