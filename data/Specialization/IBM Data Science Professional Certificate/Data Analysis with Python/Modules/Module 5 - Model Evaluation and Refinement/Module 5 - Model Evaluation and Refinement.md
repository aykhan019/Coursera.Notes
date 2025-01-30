

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=20edee3e6057dd0de46e806cbe19691e4cf471df3608f1b2b1e920697bfbcc34&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=daaf7a33ab7ec5834ee84e2a5d9996c6752f288cc714abe4361b9a1f7d1867f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=9445379b1c7c4a7309dfb928a852b527e14a8d635982c66763c9d939748fa5ca&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=ce6bc51dbfe4a72693050fcfb5bcb417ddc413d1d184da4a3effeb024cb0c891&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=6b1ca7bdc9ebfb10418e25d5754f56ce6f0f5d9ce574ef09131584bf25928b91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=b77f83a52cbbd28c8a69a16c80be48c535e80eff329efdb7139f235d1c4f7d33&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=c3e03778529579dc2793221478d0af08555193a19c9d1a26e48f74fdadb9ecbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=f063c2d96f0b06fef50dc8001440672ec677beaf9b5c5b4b48fb7e37d0f5ffaa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=fd111c2676f1d9341f346ad4379682ad099d2f7d490da83ec9ed84255a83f61a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R35SXODC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BBuGf47xaqOnZrFMqqkPgS2zk8BDYaZQ2fbZwB11UgQIhAPTD0G%2FjQGfe24BlTlsPQ1eYFVhuca6S1P5yoS5Jz95hKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrCdwXJEvUhzxbQkkq3AMmKZJW4tlNONMam8nbKQSAXYoEB40FeW0FWZuqOPJUEHpjr2Xf1oRvY7KAAMVdX0fI20ZcvzPiiiizqr%2F4tsaxX8hfxFLFhuniLD5myciiuEjUs7mMfwq8%2BEK6XrLhBNQ3Qjkk5XSfB%2BHeLrWNRAz%2F0kHA%2BtKZdMzExElqOv6OhoCsr7Ao%2BBDUclNtBV0jV5L666QPvU4AVWjDSbS07v5CEptyh08U3cNaaCV%2FUUTEm0nnmDSejMHNXDXHUznNSiNIbe%2Fhhp0ZzamimTW9MLDsQe6DpGzaxlVKx6QcfvVA9LivSuhCNAVAS92WerVwx9mcJtY%2BVCc%2Fkf5aZR%2F2Raxblzb9p7tT3XPJz2KF0DPjz9is5PyIIlg9pA%2Fx8cKP7bBaK3CEE7HG29QKN5KSdyRgNHbFN%2FmBalEhNyDckaRO9Ut5tRN26MRgXlMsrxAB3X1zu4occPMsERP2T%2FX7obFlH3i%2FWCSxG9O8Y3GuXzpk7kca1nILgdMndDAAopetrSadHtPAgrcwPLbZYDS%2FezSY5nOvUij8I6y%2Bb%2FzfTr1saOWhPHDfzAIGVrb1NaHpSvjg%2FQkRAEqdw3G34%2BvsEkgEKf5DY6KyoN9XZyHG4Q919HLX0Ej7ViJd6US6EzDJ1u68BjqkAfpPj8GguC8W916yaoVG6fmvwYYAw7HpEBQshnxxQ9YVweUl9EgKMHMzCgVH183OHKnTsAaihX5G35cTgW8CEyLYTnAvBbMmvkaZr7%2F3cyszwaUGnQ%2FkiC5z8Nu3tE1wH4VUj0L1Gz1k3NKmnf3bBti%2FE%2FA0M08Ww%2FBsLHTf3%2FmcBz1hS9KNUMw%2FYGGLhWH6r4LYAVkGx5p0SPWcNycVsgS8rqhk&X-Amz-Signature=838d4dc4dce0c43eab9c83afcea46d9ca62bc717bb900b7682c7eeafed7b7564&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R35SXODC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BBuGf47xaqOnZrFMqqkPgS2zk8BDYaZQ2fbZwB11UgQIhAPTD0G%2FjQGfe24BlTlsPQ1eYFVhuca6S1P5yoS5Jz95hKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrCdwXJEvUhzxbQkkq3AMmKZJW4tlNONMam8nbKQSAXYoEB40FeW0FWZuqOPJUEHpjr2Xf1oRvY7KAAMVdX0fI20ZcvzPiiiizqr%2F4tsaxX8hfxFLFhuniLD5myciiuEjUs7mMfwq8%2BEK6XrLhBNQ3Qjkk5XSfB%2BHeLrWNRAz%2F0kHA%2BtKZdMzExElqOv6OhoCsr7Ao%2BBDUclNtBV0jV5L666QPvU4AVWjDSbS07v5CEptyh08U3cNaaCV%2FUUTEm0nnmDSejMHNXDXHUznNSiNIbe%2Fhhp0ZzamimTW9MLDsQe6DpGzaxlVKx6QcfvVA9LivSuhCNAVAS92WerVwx9mcJtY%2BVCc%2Fkf5aZR%2F2Raxblzb9p7tT3XPJz2KF0DPjz9is5PyIIlg9pA%2Fx8cKP7bBaK3CEE7HG29QKN5KSdyRgNHbFN%2FmBalEhNyDckaRO9Ut5tRN26MRgXlMsrxAB3X1zu4occPMsERP2T%2FX7obFlH3i%2FWCSxG9O8Y3GuXzpk7kca1nILgdMndDAAopetrSadHtPAgrcwPLbZYDS%2FezSY5nOvUij8I6y%2Bb%2FzfTr1saOWhPHDfzAIGVrb1NaHpSvjg%2FQkRAEqdw3G34%2BvsEkgEKf5DY6KyoN9XZyHG4Q919HLX0Ej7ViJd6US6EzDJ1u68BjqkAfpPj8GguC8W916yaoVG6fmvwYYAw7HpEBQshnxxQ9YVweUl9EgKMHMzCgVH183OHKnTsAaihX5G35cTgW8CEyLYTnAvBbMmvkaZr7%2F3cyszwaUGnQ%2FkiC5z8Nu3tE1wH4VUj0L1Gz1k3NKmnf3bBti%2FE%2FA0M08Ww%2FBsLHTf3%2FmcBz1hS9KNUMw%2FYGGLhWH6r4LYAVkGx5p0SPWcNycVsgS8rqhk&X-Amz-Signature=d708e53ee8ff8eab488dca7f5011c6b3f63d6fcbf7cc13e7fe4e61fd5c471b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R35SXODC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BBuGf47xaqOnZrFMqqkPgS2zk8BDYaZQ2fbZwB11UgQIhAPTD0G%2FjQGfe24BlTlsPQ1eYFVhuca6S1P5yoS5Jz95hKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrCdwXJEvUhzxbQkkq3AMmKZJW4tlNONMam8nbKQSAXYoEB40FeW0FWZuqOPJUEHpjr2Xf1oRvY7KAAMVdX0fI20ZcvzPiiiizqr%2F4tsaxX8hfxFLFhuniLD5myciiuEjUs7mMfwq8%2BEK6XrLhBNQ3Qjkk5XSfB%2BHeLrWNRAz%2F0kHA%2BtKZdMzExElqOv6OhoCsr7Ao%2BBDUclNtBV0jV5L666QPvU4AVWjDSbS07v5CEptyh08U3cNaaCV%2FUUTEm0nnmDSejMHNXDXHUznNSiNIbe%2Fhhp0ZzamimTW9MLDsQe6DpGzaxlVKx6QcfvVA9LivSuhCNAVAS92WerVwx9mcJtY%2BVCc%2Fkf5aZR%2F2Raxblzb9p7tT3XPJz2KF0DPjz9is5PyIIlg9pA%2Fx8cKP7bBaK3CEE7HG29QKN5KSdyRgNHbFN%2FmBalEhNyDckaRO9Ut5tRN26MRgXlMsrxAB3X1zu4occPMsERP2T%2FX7obFlH3i%2FWCSxG9O8Y3GuXzpk7kca1nILgdMndDAAopetrSadHtPAgrcwPLbZYDS%2FezSY5nOvUij8I6y%2Bb%2FzfTr1saOWhPHDfzAIGVrb1NaHpSvjg%2FQkRAEqdw3G34%2BvsEkgEKf5DY6KyoN9XZyHG4Q919HLX0Ej7ViJd6US6EzDJ1u68BjqkAfpPj8GguC8W916yaoVG6fmvwYYAw7HpEBQshnxxQ9YVweUl9EgKMHMzCgVH183OHKnTsAaihX5G35cTgW8CEyLYTnAvBbMmvkaZr7%2F3cyszwaUGnQ%2FkiC5z8Nu3tE1wH4VUj0L1Gz1k3NKmnf3bBti%2FE%2FA0M08Ww%2FBsLHTf3%2FmcBz1hS9KNUMw%2FYGGLhWH6r4LYAVkGx5p0SPWcNycVsgS8rqhk&X-Amz-Signature=f27d451a124007e606cbe24a3a3abbf62c039c0417ef5d4fe79f995a0238efb3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=ea1f5a6b04de5a9660df96dff5be59f568f2dd03e5fd62059384bc3e560dee8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=31dcfe54a2c2af6409f246694c0ed03b13a8a78fbaeba2dfbcbabbe50a3d3d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=42f369634185eba511f8f559d49191d51a00881b37d735a15b4c2ade0d0537ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=18e67fefaf65448754265c8587c48400f9db066fab19465247e7a1d41f6e48ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=2436d6e36a29671a4facc54f0be78f7844831e42539bd1949b092000cb5e0fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFTC3LED%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVrtK%2FzmCX81zALVAtyv40XyFSblppJlk72%2F%2BMpPkyfAiAGmGJGLW9nGP%2FltRuXoW3QLQBZS9hXECnjUon97o03eSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU%2Bu3L8EPigDuKjMfKtwDa4LtLWoyRb448V5U08XNLzstM2JoSeVWUaD2LcmfYGvP0UxgS0xQwdTXclz8J9jpOhqdE471nlXmsK2cAXw%2Fs9h%2FRoxqR0eaVtT7fuSzJWmFS1hy2%2Be4YOudzeU1ysjkJ1%2B3rU57cfRlGkTTB3v9gobgo9OJ4OUQwr9xYGHZw4E9G4iEWHObODn3WKnx1vw1DNcz5l5p09UnNi4kFI7fhguhD1af0SiHSk87QHoj%2FLQJLvAVSCfs%2BjG1YhzNv79DBkqMpQfaJS3vS4df34MQksj9nwOxEaYVTNwiYMrDBlu4p1cbU5GvhDYSYmZtGN%2B42Uh9yV6D3ruxnHz%2F%2FWGgxPoqH3%2FHKrSzRahwbVCAJVef%2BzC%2Fpi25WoJnLPSoLEO1hEhuvWCXNaVr6iKiLgngeyTRFP%2BGBVaw6VeTi%2BT99sr%2F3qc4NqwzhA4PiR%2F9ZRzrGuKLftqkrZgKSyB%2B%2FJd%2FlLBa0e2gp%2F7wwook4PPZyrqzKcy%2BgrQrozLVgD5JY%2F3iH4GqxfXY7KJiEzvwM1FrE%2F9ItMVAtX6b3uahDuqz4WrQviQqCedrPmpOh56D7069EvgApR9pVtRq8zwOAfrOsl%2F%2BNQICCezz5bHUA1wSfwB8f81%2FIVO5LlrgIPQw0NbuvAY6pgEEX7GVVwc1q9RyANuAMq7G1NPcXIv36Poc%2F5tFl9rltzt92rNz2v%2FvC1tboLxyvaXPaFA%2BYvYZJfDzt3jJWSNKs8R9ePyXiS7dN9oANpht4GBHqVaU6htmncbePfxtuYE7uW387Auy3tKvuPoZjWqfjwx6awU5Pa3omyJRv0w1KDTwwO3eSjptZzeHtzGLBUz6gd4gv1FlkVD3AI4bD0YG9%2FW7rH7H&X-Amz-Signature=45216df01828aa076f92e53bd52056469a11740e67ea5ebd601edd4220c8721f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCGBTSEN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2RFujK8mZg3UI2NX9g6Ph0DZyEljTDvmWVc1klqvOsAIgPy7FvM9yKeUznCuFVOSHbpi%2FRLOsgNsS7gwouHfZMOwqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAp%2FUlF8QkUsHGpWircA2otYaynBhFh63%2Bj7wiNvPU%2B9MwBprda%2Bm6Cd29HScVPYoBgw723IqrHB8IOG4qhNX6%2FuEunIUoynsUw%2BdvuF5blNGcV0EXDwIXDSZfag5rz41TKWkskhP6Nh%2BO3GEmaNRpAsQv2cP4FbA48CTukKkAY8fuVHFvWbZORt27akBpe%2B3ViUIEWfzoi7wYlmbrdFHEFcurYz61f1UoJKRmUYTcdAfxmNDvwZq4uCVV2OQ1laNKgOdGcmpdMPKdweHGgEpAykjLZ5xJT5nTnW0rSDOSd0nNIk%2B4ycjBS2HU2aziqjmnswWVm1cZvwsnkTjDXyD63Dqe72ZDcxWBCXhaHRRPv5kUp2B08tbhw8dYkiH94gVxhIOrTRwplZTLCXN6cKFaIlRIVnK2ZFMRkRwPyFhNLZhop%2FD%2FZeDKy4f%2FMryjyuHPQiE7UBY%2FXDUG18rXdQ%2B1P1Y7PmeinBYK6ZU0Wo8QLBHyS1cr7UjlV3ACscs58LvqM%2B2BLF%2BFwU4QA1Zdx3duNQOsqVAOGesvYB2grGCgwJvU7e1%2F%2FgT3lNnar5xvAmYdS%2F36DZW6cMdmOUQEfu9W%2FAnFJczgoEx0gp0N7UxnOOWhlFWeg1h1Ji7QzSkSnLgK43%2BMK1nVTgaUCMOjW7rwGOqUBtar3sYDn2Z1SlKuNzx8M6CP8tUvX4HWRgyatd5rJrGPH9v9tQqjByqMEh0kWYD8YzNEAqJiM1vMpQ2UqlCFzRpLbZgizoL2KNQXPARvqjOz5Jvkhb%2B3lO8R7xjR9bInU39LEdLHFKWj2CJyY9OJC7iJVaFbWUegHgywJVORZr1UhVh3hi4kKNlVbzfUfZoQLgh7RWG673QfcpByvwQz5aZuRBKA3&X-Amz-Signature=85bbf65525ba49d1c20219413c86f172afa17508baf1a23c5440c347c16c5134&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCGBTSEN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2RFujK8mZg3UI2NX9g6Ph0DZyEljTDvmWVc1klqvOsAIgPy7FvM9yKeUznCuFVOSHbpi%2FRLOsgNsS7gwouHfZMOwqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAp%2FUlF8QkUsHGpWircA2otYaynBhFh63%2Bj7wiNvPU%2B9MwBprda%2Bm6Cd29HScVPYoBgw723IqrHB8IOG4qhNX6%2FuEunIUoynsUw%2BdvuF5blNGcV0EXDwIXDSZfag5rz41TKWkskhP6Nh%2BO3GEmaNRpAsQv2cP4FbA48CTukKkAY8fuVHFvWbZORt27akBpe%2B3ViUIEWfzoi7wYlmbrdFHEFcurYz61f1UoJKRmUYTcdAfxmNDvwZq4uCVV2OQ1laNKgOdGcmpdMPKdweHGgEpAykjLZ5xJT5nTnW0rSDOSd0nNIk%2B4ycjBS2HU2aziqjmnswWVm1cZvwsnkTjDXyD63Dqe72ZDcxWBCXhaHRRPv5kUp2B08tbhw8dYkiH94gVxhIOrTRwplZTLCXN6cKFaIlRIVnK2ZFMRkRwPyFhNLZhop%2FD%2FZeDKy4f%2FMryjyuHPQiE7UBY%2FXDUG18rXdQ%2B1P1Y7PmeinBYK6ZU0Wo8QLBHyS1cr7UjlV3ACscs58LvqM%2B2BLF%2BFwU4QA1Zdx3duNQOsqVAOGesvYB2grGCgwJvU7e1%2F%2FgT3lNnar5xvAmYdS%2F36DZW6cMdmOUQEfu9W%2FAnFJczgoEx0gp0N7UxnOOWhlFWeg1h1Ji7QzSkSnLgK43%2BMK1nVTgaUCMOjW7rwGOqUBtar3sYDn2Z1SlKuNzx8M6CP8tUvX4HWRgyatd5rJrGPH9v9tQqjByqMEh0kWYD8YzNEAqJiM1vMpQ2UqlCFzRpLbZgizoL2KNQXPARvqjOz5Jvkhb%2B3lO8R7xjR9bInU39LEdLHFKWj2CJyY9OJC7iJVaFbWUegHgywJVORZr1UhVh3hi4kKNlVbzfUfZoQLgh7RWG673QfcpByvwQz5aZuRBKA3&X-Amz-Signature=13d08dacc77297843ad71bc9bf3a2bda38529d85ed522feff2b6f9c2a6f85736&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB4XFGUG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjHhkVkPxacs3ckYgGSuRkqC05eIHeekmi2cwEyRjffAiEAgKqUblVbYHazouN%2BnszYa21CCLCxER7GTyEoQV2J9QMqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6a97waZyPhofs5ICrcA3KYRhK7ulp0lihRRTwODpNbeb8ebCRYtRps0%2BHqJn93X0xQoYN7n7lXma8JMvljY7Z1I7P%2BcDorTybA2oLBT4OT%2Ba8jqC9gsLlYoFJephbdp38wbfx8vw5M%2BG0MGGeo9oN3x8MqXJjBYB5Rw7o2vuV4V5bMgTtEm%2Bpyze2UYBmL8owMYlsBDK40IuDrFeAP16HyGr7GyLA3se1IQSgIL5HHD%2BTU%2BqxuFN%2Fts97s9RamDmfvIa%2BNaDIwM3mh6mVPJ6DMrOJOgiGfufi%2BTeM2OEpsIxY38lgfLzIXNBmK1dkLhbgjeAQX%2FYXQLYWM1YAP7YnnfPXUMa8COMza3x3GxSWeBEvyto9MmPZF14lfZLiCSH7NjMrynwX2tSoQljYawdYj9ioXnFC%2BT8Nbb%2FsxD2qmXdUfaWc7nhMs1%2Bm94TuQAjJ1T4Uq1ZTxhQsADirsiPhlR48Wq2XrifP%2BDpPQTGZDfFck69SpReMK3FFirqx7KiNQ163%2BMqLWcdsWHwwnS6KESn6UNDIWcNruTWog5nJ4TWHz25puo9dBYlQS6sJU8WcDVQ4V%2FskAeClVPgp7iUUOwdD8SoTfSe9KFf9cqHI9wxpIe6MgpSdT8yQtiHoyu%2B%2FP2XPmjlw6ARhDMJrY7rwGOqUBuwWC2Vg44nM8PvZrzXBcby7Hrey4VozKRH62NEftkpFfmNSPVoubHnPyvE%2FS9%2BbPFgqd%2FeT3udNvvNp0nZQPYNzePgdlSwN7VLNEtJOkuE2nc7c%2BBYvefFbFNzkzHvGWDHItu5lm5q3D%2FSk%2Fkq7AxNoxwp45zO4i%2BRCeg2MbKYtYfhEEqcL5tk5lZtSAOGYrkONTbqjfQako%2Bg2LOW0%2F5IKS41FC&X-Amz-Signature=3976553096fc0dac3459f5b3cca51461a29c62c2e8927dc2e0ce502dd3bdade7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZG65TW7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPmwdZIiuXUVtWlJ34Zxn0kvccDjDbWRD6ojj%2BzyD2FAiB6vpZ5zVp7UOEKjv3s1f7JHaFYYWAMhhieb3Ye%2BskxwyqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowt5tniDOBDauVQhKtwDjZyUBHCkub9UaHwuM3%2FC5fh%2F4YOCvwzolEECFGuyz16lSnLS0mvjTG7mZhYTNGH8ty7jPBlPEQgQ5fJc64hifaeW8fv6RB5SSnfPzf3iXXCGfcbCKX3%2FxZ8REYBTQQp3nrkjqi1L7g%2BS3KyNBNFQJkYPo24P1Iere75gseIdE9EP8RtUK9SSyc2MdDNnBzciEy3POMkATDPAIjfwdEBc2qjV3UJKjPOswpje0yyJwhT%2FTA9zL5s3n%2FNDz91fs7YpmLan5vsZVgpjlY8ELndIgGs0mzVa0Etz8zUTftIUj3ZwliIileGVZhLz6sQzM5M%2BllP4DA%2FufA%2BBhtSIqP1DJmLvHAU2Ke1ouHSRfEeF5mU0%2F8iE2uu93wpvH04MVKDYDPipOsfwt0B6wgDxWE%2FOroOeUqlFu9CwDbNnDyoCDMet8rrI%2F1L5HC%2F70a1%2B2AQLZ40BpNtTtRLioZLJ48AGLgJV1Be7pahuFdmfpQA1f7vdXh%2F%2BF1GRphOlTanEylIGrVtbqzA0zDRjgIIpq57zaBacyjAUKMf4b9WkI%2BQDrSj%2BK010g2AKzGCDaIaAKiGas7nDAhcPXAtXCcKURrwi73utO%2FOhwUqrG%2Fmbn4OsW8g14904AycRhKB5uuEw89buvAY6pgFA3HFaXOK7XdId1yyAb3ewJ6pqvMaRZOaGc15IWoj1pu6Qdh4D5K8zCQ3Soj%2BmySOTZiq395X%2BHrqmEyAj2oguu4HEiN2BPWQX4zA8jZqQ6k9iViEMpWDuwx9vmdmm6ucSKDWWa3g6HfbFSxnSLAPB7%2B%2B9pe%2BBHjNzMCTlHursm6of6fdOL3DBmQkA8kB%2FN4d79J4yNFibnOy9FoEhSlGJ%2FWyEa%2Fq9&X-Amz-Signature=f0e260b507b6874d2e19db51e460878e5c467f7d73a9ed7a1a75cade6265ea52&X-Amz-SignedHeaders=host&x-id=GetObject)
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