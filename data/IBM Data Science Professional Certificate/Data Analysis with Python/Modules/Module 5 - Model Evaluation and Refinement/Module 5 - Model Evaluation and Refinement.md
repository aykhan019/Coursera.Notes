

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=e5ef9a2d99105354b1bff58d724bd703a1cf483748ca95a6a56501fdf9fdf494&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=3f2a399328f5f92227848f6dc59819bf837775d273b5e01723c81a93ce9e81a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=1a4fd1cfb2faf2ac0431381f322c3b435d5a4f970447fd30342369991b9eb747&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=cd47a1e581b14cf5a85ad5dfc6302e91893d310026afdad35ed30d197d44ab81&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=ebac1fa838e1fd1aa55953176b07d4cbd89748d1d64e70cf4272a3591af53994&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=2bebf7e882638e8d14fe44b348afbb82d9b5531e0238afa918305f77b1583eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=0f243c4662c3e73923c114e124155f50a9529c2677fff547d1b876eab4f71a2e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=8e5f18996fadd2f7644c24c265f285b819fdca63a5ba4e4f8d84b6d151fa33a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=24352398acf564c059a00aeaee54117310cc76ce0c1b9a59c07d1dcd7eced5e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AFPR5YQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnCGJNMpe%2BeUZN0%2FQRNRZJzBByCflPSFeUxbqkQvZuxAiBnH8iYOopCmZonU%2BLq8nWg6UGQpqrDyISK0JIqXOYaMyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRifqqADeg4akAgdvKtwD%2FQOa32RMCRDNw%2Bqg4%2FYoZGxUYC6Fj7vEPDtK%2BM2FCQd5kgD3mc2LTINnbhRbJA1DTE0zGHim8%2Ft0sfAVMHPEzH9T3LOZ5JpOue49aFbtv0d1ony43POeyQQTepoLk3SWLZMZ0hWyBIvqA0x8acS%2BTYV96XWUqk06EtQjna2t4g9lKElkQMtncKazIdZa%2B3zjLZHFUu453PqJJg%2BG%2B8l2U6SX6mtNqcexHU6PDoF0j4S7%2BTOFmFUau%2BeEESn9vFHR3Vrn0jkJH%2Fl1de7Fx2BKp%2Fr2F3qoDNgQU8Yjwa%2B%2FDbc0y3LPbmqeg1sTxqP62ArUXXH2hf15hbafSZLhRkosZ5lj2vTWMjtM2Y1xdwnj5pNyZehgIByC4gR8XPTJvAUHlXdThW%2BglYIYem6MfWqgAGhfJ9Zynxu7PXvtl2zlR70W2x6VDxT2QOM9yu3RrLstgemi8An0aWSf5jbhwlEfWUP8XaUBtuAQi49t5hKuX7beCar9fn53SkM2hb9QIsXPH1NK7LmhhhLRQfQlWtquxYTYPh1b81jvweUBFTmfD2twh5Q%2FExeiSLAlw3pwYMptZGfAuJiV%2F95pkynBTokbmcyVHLpOVppfeUPtsbkRzhFRuWMr72T%2BqO8GhA8wo5z8vAY6pgG0NZqx8kyhfQcC3dkwh%2Ffo1mIbOoPLPIkNGMrv%2FQmNd92qY15ViDf87FcoNSyoZWv22m8OBD97QuCxDdZDIeDV6uUJJyyvmqipVS8WothzgzVi9Fsf%2B4ye4167gyAf1TOJ3pTLxOyKnQLliNwdrEHXqkgva%2FyhxLL17Kevo8xHhWhQ0JHnCFcUuOvp5U3RJ7HMXUdhhXbpM7kg94iWjGhgC790zsVk&X-Amz-Signature=19be92b383869edde7f40fd53c2bfd55b3cfac870d6ff41eb83d366a486b140f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AFPR5YQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnCGJNMpe%2BeUZN0%2FQRNRZJzBByCflPSFeUxbqkQvZuxAiBnH8iYOopCmZonU%2BLq8nWg6UGQpqrDyISK0JIqXOYaMyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRifqqADeg4akAgdvKtwD%2FQOa32RMCRDNw%2Bqg4%2FYoZGxUYC6Fj7vEPDtK%2BM2FCQd5kgD3mc2LTINnbhRbJA1DTE0zGHim8%2Ft0sfAVMHPEzH9T3LOZ5JpOue49aFbtv0d1ony43POeyQQTepoLk3SWLZMZ0hWyBIvqA0x8acS%2BTYV96XWUqk06EtQjna2t4g9lKElkQMtncKazIdZa%2B3zjLZHFUu453PqJJg%2BG%2B8l2U6SX6mtNqcexHU6PDoF0j4S7%2BTOFmFUau%2BeEESn9vFHR3Vrn0jkJH%2Fl1de7Fx2BKp%2Fr2F3qoDNgQU8Yjwa%2B%2FDbc0y3LPbmqeg1sTxqP62ArUXXH2hf15hbafSZLhRkosZ5lj2vTWMjtM2Y1xdwnj5pNyZehgIByC4gR8XPTJvAUHlXdThW%2BglYIYem6MfWqgAGhfJ9Zynxu7PXvtl2zlR70W2x6VDxT2QOM9yu3RrLstgemi8An0aWSf5jbhwlEfWUP8XaUBtuAQi49t5hKuX7beCar9fn53SkM2hb9QIsXPH1NK7LmhhhLRQfQlWtquxYTYPh1b81jvweUBFTmfD2twh5Q%2FExeiSLAlw3pwYMptZGfAuJiV%2F95pkynBTokbmcyVHLpOVppfeUPtsbkRzhFRuWMr72T%2BqO8GhA8wo5z8vAY6pgG0NZqx8kyhfQcC3dkwh%2Ffo1mIbOoPLPIkNGMrv%2FQmNd92qY15ViDf87FcoNSyoZWv22m8OBD97QuCxDdZDIeDV6uUJJyyvmqipVS8WothzgzVi9Fsf%2B4ye4167gyAf1TOJ3pTLxOyKnQLliNwdrEHXqkgva%2FyhxLL17Kevo8xHhWhQ0JHnCFcUuOvp5U3RJ7HMXUdhhXbpM7kg94iWjGhgC790zsVk&X-Amz-Signature=d8f255b307694d001725835606fcc836091884388d0487f4a8c515a3c6692b03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AFPR5YQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnCGJNMpe%2BeUZN0%2FQRNRZJzBByCflPSFeUxbqkQvZuxAiBnH8iYOopCmZonU%2BLq8nWg6UGQpqrDyISK0JIqXOYaMyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRifqqADeg4akAgdvKtwD%2FQOa32RMCRDNw%2Bqg4%2FYoZGxUYC6Fj7vEPDtK%2BM2FCQd5kgD3mc2LTINnbhRbJA1DTE0zGHim8%2Ft0sfAVMHPEzH9T3LOZ5JpOue49aFbtv0d1ony43POeyQQTepoLk3SWLZMZ0hWyBIvqA0x8acS%2BTYV96XWUqk06EtQjna2t4g9lKElkQMtncKazIdZa%2B3zjLZHFUu453PqJJg%2BG%2B8l2U6SX6mtNqcexHU6PDoF0j4S7%2BTOFmFUau%2BeEESn9vFHR3Vrn0jkJH%2Fl1de7Fx2BKp%2Fr2F3qoDNgQU8Yjwa%2B%2FDbc0y3LPbmqeg1sTxqP62ArUXXH2hf15hbafSZLhRkosZ5lj2vTWMjtM2Y1xdwnj5pNyZehgIByC4gR8XPTJvAUHlXdThW%2BglYIYem6MfWqgAGhfJ9Zynxu7PXvtl2zlR70W2x6VDxT2QOM9yu3RrLstgemi8An0aWSf5jbhwlEfWUP8XaUBtuAQi49t5hKuX7beCar9fn53SkM2hb9QIsXPH1NK7LmhhhLRQfQlWtquxYTYPh1b81jvweUBFTmfD2twh5Q%2FExeiSLAlw3pwYMptZGfAuJiV%2F95pkynBTokbmcyVHLpOVppfeUPtsbkRzhFRuWMr72T%2BqO8GhA8wo5z8vAY6pgG0NZqx8kyhfQcC3dkwh%2Ffo1mIbOoPLPIkNGMrv%2FQmNd92qY15ViDf87FcoNSyoZWv22m8OBD97QuCxDdZDIeDV6uUJJyyvmqipVS8WothzgzVi9Fsf%2B4ye4167gyAf1TOJ3pTLxOyKnQLliNwdrEHXqkgva%2FyhxLL17Kevo8xHhWhQ0JHnCFcUuOvp5U3RJ7HMXUdhhXbpM7kg94iWjGhgC790zsVk&X-Amz-Signature=196ca0f87f56a1fa5c3217bdafadf59ee06480433063ddef98f46523d1c4a371&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=2957a5e5669e3e69b9c3b8ca7c24eb94a6bbb1890218d2590fe7b66320b71881&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=85fb3c70bfad6670986af4b053f4bc98433ec1a07e158a68d5f6127efd6627ef&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=31168ae8725e30d6ba82c6edd54d74c96a98ea21262e85094e63fe84e5f883bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=ad7fcfc70e25a8a1a0b6c3443242e2e6da7c1cf25546eb5174e43087f9303a53&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=6cff19effa8083a7d9d639270ad05ef41784e6864ab3511d2c53ceebfe0a9529&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626JS3K3M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDP0%2BrbooyVbWayhJFRalB6b3nmEC3mnMrJF8cxbBJVfgIgEy3p4aXZUxohUjdaSTh6dOqoO%2BPd1hmbLdGeEQg0KgwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCcle0hqnkcCSOEDmyrcA%2BxwzWQm9jSDdSpjierDEiBzkxuXrGcVl0vHMGNJ2iGFHIEzGCaHCrnNXEBtsnwB2kSWEGCZ8DjlqkSRVpGSHcR53QUP91h2GN%2Fthlg7O7vLo5IG3rgRtjzcXYg5R11m096XahDD7xlySjFKwhRFfXNqyUNTruEFAWtPlcWiupTqVkMGd%2FCcQRdK81hFqXr25MvtARP2lcPv58RPKbVYg9mMi1aJGoqdFlaZqcho30OXPBv0p7Y3h6R2moHbM1A90sAwpeRX736BpQA8C1JMWSlUnedLnCTSOeeckSL6Vt5sM9fxcq%2BrI0bwYRAZMauBmmwgKptso6EPClnqgo0iWrW2E5OmgeFJ9zYNUNFYjQYc1%2FzbAO4S3kzid2thGkwvA2BwVK4BwqAPnVp%2FhdJPgH%2BJMkhC%2FagbPntVbavtPngO2cJI0MGYBIGlyVCYQRSjhpqqhdIPhqA24IYykfR6a6bozqvBH1w4K7hiMidtI3Ui7inTAfRrSwxAyn7%2F2jUuEKAdeZNTIgEPlxQOcvdxNEZQZInTsOzfyvUnW0XUoGig6Sbvm02%2B4SonoVbzztqYEoahOSKPNDVM6SJ%2FWIzHadakNbKq6U9XjdJsk4bHTLS1iFQmCfdD81Ym%2FRX0MJSc%2FLwGOqUBUHF1ZqUR3Rtak5w%2FeSxCLblS8dUiJosjN5Eja1tUcfA96bccdKRwEBXlUF%2F49ErMiJg6QxoFtDhGhWOw3DYraOCMaPV43HM9mUM0G6KrQd5q%2FkCcKTJmdSsA%2BYudbQ4n%2Bq18Cpvwq07fMZNqj4G4Sclg%2FSXIuNQSUF3pC6IytHPXVqz9z5wTAPGXC41l8b96ZNg4haJmFRuS4nk%2Fu7cpqHvaLGBi&X-Amz-Signature=2270078eb0698778562f4cda76885349ceccb3e700230db3ff0ed52645487215&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLMTL53D%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFYp%2BEzQetoOvtDwCVBnl9cW%2FWFs0Egqg9OAQIelDECAiBpWWiZEiCfMlCMCFj9zBp83B5a0Z81wuiB0OF1kRQnUSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUiJ3%2BiAgNj2lq6vLKtwDYQDAOTryJwLSIYmhMzYv%2F98FGj8fk1nxBMIxrsi%2BsAXteQlwTFt5ys0Z8Qlcp7zdQFTgdgPQKzSvzWNaLL2VHcbV%2Bu8JszCIJO0f9p6FR7KFPryFSD5Mk0NaUPanWKhwNPkIa17Z5kviot0IthPpH2o9cdFqic6J6tZhQTykWE8J4zfHztJ2eCMnb7%2FcBhPd%2FjVT4zs7OwiJk7QJdgUFSYqVzIWUeIgmLxy2zvCWQTCK7N2KNU7jg2R%2B375xSzNJtTpa1s0eGeaudz8LRzUPJUzg7Lj65s1Vrd0vWoOdAInV5MDfDdJFhoIY33kovUpQn2SnGth77Y%2BKg53jTldhf8DD4q3333w96pPyk0SF3T679bmlD2vgewWr78DuzJX%2F2rdkp3v9LMCRgd%2FlxPl6M6EPoDApgRO4uO01lf4yUygidDQWGccwypwoHq2duAzAP6xV0f0W%2FvPAXR02EPsOU%2BVWIb%2FvvWroEtgGyTVy3pwboZdH6P6hjYnmmAW7CObi2FIdSAGnI12eFykW6hKpGSZhc4thuOhPPKh9rG%2FMvRd4yMH0rSFOTUYLb7ZdhxVM8E7BlbxDS7z%2B7hqjEW1XoM76gcPeXNoyRr%2FE%2Fq0GwCoEmdgANTGFWOawUAMw%2BZv8vAY6pgE85fYlB5mt%2BfB%2BpK3VLGSdqaMl%2FGug9YEgqMPBeYtf2yEh5j%2FSITG01DWUXIp2qVkLBjB92dI1X3nWBIO3dBhVK2zh660X4ERbjNa%2FBsuWgPp0sUJITBaeNSQQX%2FqLaahPR8ADthuB36RBamvBi3%2FO48v7KMz%2F3ozpIMA5bwo9R4lJ19m7utOi0StTZtBufHjv5owhu7yZStumVq19WV3G9H7yWjCN&X-Amz-Signature=830ea0bc961369acf77c4673774c6b4ca2657424de6e494884c98cc37f5f1470&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLMTL53D%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFYp%2BEzQetoOvtDwCVBnl9cW%2FWFs0Egqg9OAQIelDECAiBpWWiZEiCfMlCMCFj9zBp83B5a0Z81wuiB0OF1kRQnUSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUiJ3%2BiAgNj2lq6vLKtwDYQDAOTryJwLSIYmhMzYv%2F98FGj8fk1nxBMIxrsi%2BsAXteQlwTFt5ys0Z8Qlcp7zdQFTgdgPQKzSvzWNaLL2VHcbV%2Bu8JszCIJO0f9p6FR7KFPryFSD5Mk0NaUPanWKhwNPkIa17Z5kviot0IthPpH2o9cdFqic6J6tZhQTykWE8J4zfHztJ2eCMnb7%2FcBhPd%2FjVT4zs7OwiJk7QJdgUFSYqVzIWUeIgmLxy2zvCWQTCK7N2KNU7jg2R%2B375xSzNJtTpa1s0eGeaudz8LRzUPJUzg7Lj65s1Vrd0vWoOdAInV5MDfDdJFhoIY33kovUpQn2SnGth77Y%2BKg53jTldhf8DD4q3333w96pPyk0SF3T679bmlD2vgewWr78DuzJX%2F2rdkp3v9LMCRgd%2FlxPl6M6EPoDApgRO4uO01lf4yUygidDQWGccwypwoHq2duAzAP6xV0f0W%2FvPAXR02EPsOU%2BVWIb%2FvvWroEtgGyTVy3pwboZdH6P6hjYnmmAW7CObi2FIdSAGnI12eFykW6hKpGSZhc4thuOhPPKh9rG%2FMvRd4yMH0rSFOTUYLb7ZdhxVM8E7BlbxDS7z%2B7hqjEW1XoM76gcPeXNoyRr%2FE%2Fq0GwCoEmdgANTGFWOawUAMw%2BZv8vAY6pgE85fYlB5mt%2BfB%2BpK3VLGSdqaMl%2FGug9YEgqMPBeYtf2yEh5j%2FSITG01DWUXIp2qVkLBjB92dI1X3nWBIO3dBhVK2zh660X4ERbjNa%2FBsuWgPp0sUJITBaeNSQQX%2FqLaahPR8ADthuB36RBamvBi3%2FO48v7KMz%2F3ozpIMA5bwo9R4lJ19m7utOi0StTZtBufHjv5owhu7yZStumVq19WV3G9H7yWjCN&X-Amz-Signature=da9696fbe39e73fb71133c99e7a204546c559245aba4b86a0b650207c1b98941&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7YIKBW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICM24IqHgZHdU5T9rji41VOr5jGJszkCVNcozqWdFopmAiBn80MJskyNJiWPIzeCX3MxfJtCJ9vmY7k1LnLVYcj%2FKyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeerm7JQX7df%2F5eN9KtwDzoCnhC6cmPf7SQoz7Qc50welg%2B12dEOo%2BYFGPQx80MuQ3nz8GbiB6kktF%2Bk0NOljdT9N1pYWXHsbKwE5tmH0KUUz5IfDs4Imx76unS7MeVMz0tC5GPlei%2FvgMuZG3fPcRF5Quej6VaWrKvpxTsNRkS8trHFrvfm0Y7X%2BNyCXRElCNnC8ssCrFsSDrcE1j0H1ARtfFa6agmNlz%2BR7kXV8Pb0YFsFF1CXJNogd663rz0KccCL8vfpV6k8qQpbGLc7oofAoCQnWXzKyKpRj5AgN4aPaemf3%2FCFgQYkjP%2FpdL5kUpSHvmmDNuc%2BAqewnh93efknWtXFZjPdOqYDZw7deEfs8AIBJ%2BlkLJAi9tkI9peDoJrJ5zuwWLq8akyzWYBOBxYZguor%2FCF4sZAuhbgSSuNAiFCPJ4dr8hbv22nfGu2IXjriW38LbXhIGt9likiWEWRaQYgNG2LySIJkXsm2Yrol%2FwDkNYFVf45d3LmsPhv648LXbZwNccfwA76%2FFoBYghHzyM%2Feu%2FEgM3qC3v%2FevM7%2BA5b7wZm%2F09OCEeF5ZvWp8Qvyqrsq8%2BafbOM%2F%2FnBVvbfvrd9igBj8KgQM%2B8fYox4fryicVtpeUeo7Yo70CIbpZ6AIONUQBPQUzcpQwzpv8vAY6pgFTD3k8RZ7ZNYsolxIkWktIRDozJGwEan6fpghMCTroQTY4OyhDYchzrxsbamViJ8xODrHeRpB9lwoAAQ7VFDJAOMNh22fpEU6lHkStKsuETGOsbSxWyMP3PdjmjpR3cZVL6bhc815h%2FDsh12a7k6axjE0e2zO1FyIKAZ7jF938xM94tbAUc1CUrJju4OarIDzNlL%2Bct4VY%2FWJkuypXhw1WTl0k%2F1gg&X-Amz-Signature=d75c55257c86318e0e650d5dc1e7aa35daf5db654b9cbedb51f4f40cb2f70acc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROG7KM7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL%2FVMExpDo5%2BL69QTCqn8%2BLuTnCWqoTLEAp6uX6VFpWwIhAKipllx5yAZ3VMHte7bYg8WmTtpzV9GjrxJA%2Bs4JGibGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxztqflP0q6Fx80tuUq3AN%2BqvDqbzkJqZry9dmJ6NaMK2rm8WacVprbYMvps6sWZGi%2FC1IbBZcdOBdWRZ47YPQ7vR3pcJJ0pemi9a6XRAuCRtToho6MVU%2BB9TZpeqdls%2FrMstJLfqiegto8Y0KwPNYy2r%2BoI%2FqSu2pt8C%2Fyp1u2B%2BMXNxsi%2FYEtyWxdsyFeZ6rD9thEEvI4kC2JEtH0UE1la5SsLjWFUtCOIz%2BZXsFHIg7Keta3mosp9ViM%2B9GEk4gHWtO1PHzpbDq%2BsbmKu3ILIvXOCSUMku0AxBD7oMLm7kpe9He98C8N%2F7j4QWiPclA1K5xRWoVeptCRR47Dzym1Liz5bzr40YjVVb%2FHMcEvvgtT%2B8%2F0RafNYLSX2WotLel5aTlQM5DiQp0XxvDh6u2ZTXrOcxljdmAINrp0Wik6xN2z2vJgIhL7WEV%2F%2B%2BaQcPtrcNh5SIJuXp81kv9dOLUJpM0cejzhe8uGaxkGQUSFpgmXlJY4GsQWsVw%2BAqwpLAesoPxBM%2Fqbb8vZGmK%2FdIRmdmej7a2kMmiHwckD9IbxyOOdR0qUqskiKD99Ag2z9%2F3ftIKhJP8BunvuVzveM3S%2B3Bh7cjH6nMhG6KaWag8x7SvZaf7NOHd1T3vr%2FPXfL%2FpFATG8ms%2B5PmXuwDChnPy8BjqkAVk4wYiZdfGDYlZM6rMQNh0PnIKDk8iJp%2BpuhSsGl7Z94wU2XSBpGQ%2FbD4aDOk7vB%2BAN8kEWTsbrKl1bc2aD7oVdArkBwXWgr1x%2B5UTQl8tlFFuhGQHj%2FGAHYB0JJ1hF7VavvlLvcjAnFHOVVoSjmSusf5YXy3xrvRozMcB5vmPt18Wu118kQQMGwXWtLqpjpKGuv1vZXGjjoYKfuhx4zJ5Hk3ok&X-Amz-Signature=7eae21790b3699469f5c026f69fbc4d5919c2838e2170bbd8ca4ad1c9100cfbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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