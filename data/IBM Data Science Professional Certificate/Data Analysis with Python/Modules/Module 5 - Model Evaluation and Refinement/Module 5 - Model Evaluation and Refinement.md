

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=d1b1690135dd9f8fe0996ad748cea2234e04a7a1676824177fefd4a52a3c3fb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=43afd933ba1fc906fb7e79e1a33cd0270325beff03d54ddcf53d46154792bd12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=d8803aaa49051b1dcf9f4447b325cc8ae7dc9a04d7b5e7bb865442c25ebe6715&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=f6deed584c54a000eecd112f94fda8db3534c03ef421d80bbfe3206e14003f58&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=fd11292794319a4d01f2b536ea4bcae2b41814de67ed4eb50ab95d7ab8721c7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=95bf4facdc43248146d2f002b493d73ac7393307b321f5fff37a69cd171ce059&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=7ee8cbd8a4b3ab71f4552d51c31dcc5fbf96bda1c6aebb0b3e12c41220abc3cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=ac951d30f38aae35e96d8b07b557c7ef54d78ed4fb1c9099b7213e185ac89e3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=5d7c765174fefbea052a3bfd766f3905585288023a1d46c9a373784b7a89a64f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH5ERZRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRoRnX2x%2F9a2dbky%2BeI3%2BtqONz%2BAvLcxq2%2BxUoVCOhzwIhAMj92EpumpbMfYg3Uxn0VnFhrV0svIY9WuOfbkZbs1fpKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXyjw%2Fwa%2FCNLvIBCMq3AO7hn4oZIj9XtKVkFFts5fLxNcYu2fOBKxC8DCXN5JSCTN8DRnolQAYlomszUVoH6hx3LTM15yY03Q%2BuhKqgayBCOMafzy%2FMlSo3685AV4RJGXPJfS%2FbhR0J9PLgOkaXEYpqkBm2SYt%2FTrjOhEs6tCTNT074zld1MpLsabAz3zczrPmsC%2Bs24ub%2FjfXTQ0qfcD5eeaqaM%2FkqFcynjTqA5UQCzeXlIyUZPeeJ4a19zf%2FTkoUcSD9k5adSERamZ6i8UH%2FE0eQIp2iEeRfYAI1qeeFTnDFXWgYb8p0Ug2XgpQUnWzQLdm61WskyCa4Bi0Dkv9VXuxj9sma1otky55cniJGvussHS%2FJhJoRxY4bhW3eTyoieqSZdFny1Pwo9KVKrMLsUl2DN4GsH8FvZZW3vdI8mws4jcWih8YecW8IwpKqilmQnCV4xYvkVMvYzCdP94eEXbUfTE7w8WGuf9bHw%2Fw6YI7Nzm1BCWckBdysABpOoiOLPsZ4Xr2GEb1a9bta5UvljowOs9BhaSjQ2a5%2BfhlLMI2gtfpeQI9mB1lbNovnetZPQ%2B3O%2BIvvX%2BvadLNMFqIorS6BA9NTgOOnYp3FqizJakF0Ab2kIccXX%2BlyjmTOpuZBpME9b4VulMzPYDCAyvi8BjqkAeSfqrHQZdz4r3fGdQeUHFYG96kKpHJHBjbqOMleoh0zvi5DxGKPLUVaqbSKh%2BTyUcCtblZwpf39hmjx2L9Kb6EOTRgT4LvuuFnFtnsV%2B%2BtKyVYLIIT%2Bc1jpJMa%2B47hndF16JefAw0u%2BscsZsoXCsfapy89f7UBFqOSVEuGpVGsc8ncVe6q2sw6qXosDW6OUpcnP5B4VgSPMDukyctBSmgXc1D0M&X-Amz-Signature=899757a59dcb903036e439e14388e6250caa05a8ea445efb5185548e0fae8d10&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH5ERZRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRoRnX2x%2F9a2dbky%2BeI3%2BtqONz%2BAvLcxq2%2BxUoVCOhzwIhAMj92EpumpbMfYg3Uxn0VnFhrV0svIY9WuOfbkZbs1fpKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXyjw%2Fwa%2FCNLvIBCMq3AO7hn4oZIj9XtKVkFFts5fLxNcYu2fOBKxC8DCXN5JSCTN8DRnolQAYlomszUVoH6hx3LTM15yY03Q%2BuhKqgayBCOMafzy%2FMlSo3685AV4RJGXPJfS%2FbhR0J9PLgOkaXEYpqkBm2SYt%2FTrjOhEs6tCTNT074zld1MpLsabAz3zczrPmsC%2Bs24ub%2FjfXTQ0qfcD5eeaqaM%2FkqFcynjTqA5UQCzeXlIyUZPeeJ4a19zf%2FTkoUcSD9k5adSERamZ6i8UH%2FE0eQIp2iEeRfYAI1qeeFTnDFXWgYb8p0Ug2XgpQUnWzQLdm61WskyCa4Bi0Dkv9VXuxj9sma1otky55cniJGvussHS%2FJhJoRxY4bhW3eTyoieqSZdFny1Pwo9KVKrMLsUl2DN4GsH8FvZZW3vdI8mws4jcWih8YecW8IwpKqilmQnCV4xYvkVMvYzCdP94eEXbUfTE7w8WGuf9bHw%2Fw6YI7Nzm1BCWckBdysABpOoiOLPsZ4Xr2GEb1a9bta5UvljowOs9BhaSjQ2a5%2BfhlLMI2gtfpeQI9mB1lbNovnetZPQ%2B3O%2BIvvX%2BvadLNMFqIorS6BA9NTgOOnYp3FqizJakF0Ab2kIccXX%2BlyjmTOpuZBpME9b4VulMzPYDCAyvi8BjqkAeSfqrHQZdz4r3fGdQeUHFYG96kKpHJHBjbqOMleoh0zvi5DxGKPLUVaqbSKh%2BTyUcCtblZwpf39hmjx2L9Kb6EOTRgT4LvuuFnFtnsV%2B%2BtKyVYLIIT%2Bc1jpJMa%2B47hndF16JefAw0u%2BscsZsoXCsfapy89f7UBFqOSVEuGpVGsc8ncVe6q2sw6qXosDW6OUpcnP5B4VgSPMDukyctBSmgXc1D0M&X-Amz-Signature=4f461628471e1d6b991e2bb5b43a6be0dbf81415f5945e9240f476169379948e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH5ERZRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRoRnX2x%2F9a2dbky%2BeI3%2BtqONz%2BAvLcxq2%2BxUoVCOhzwIhAMj92EpumpbMfYg3Uxn0VnFhrV0svIY9WuOfbkZbs1fpKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXyjw%2Fwa%2FCNLvIBCMq3AO7hn4oZIj9XtKVkFFts5fLxNcYu2fOBKxC8DCXN5JSCTN8DRnolQAYlomszUVoH6hx3LTM15yY03Q%2BuhKqgayBCOMafzy%2FMlSo3685AV4RJGXPJfS%2FbhR0J9PLgOkaXEYpqkBm2SYt%2FTrjOhEs6tCTNT074zld1MpLsabAz3zczrPmsC%2Bs24ub%2FjfXTQ0qfcD5eeaqaM%2FkqFcynjTqA5UQCzeXlIyUZPeeJ4a19zf%2FTkoUcSD9k5adSERamZ6i8UH%2FE0eQIp2iEeRfYAI1qeeFTnDFXWgYb8p0Ug2XgpQUnWzQLdm61WskyCa4Bi0Dkv9VXuxj9sma1otky55cniJGvussHS%2FJhJoRxY4bhW3eTyoieqSZdFny1Pwo9KVKrMLsUl2DN4GsH8FvZZW3vdI8mws4jcWih8YecW8IwpKqilmQnCV4xYvkVMvYzCdP94eEXbUfTE7w8WGuf9bHw%2Fw6YI7Nzm1BCWckBdysABpOoiOLPsZ4Xr2GEb1a9bta5UvljowOs9BhaSjQ2a5%2BfhlLMI2gtfpeQI9mB1lbNovnetZPQ%2B3O%2BIvvX%2BvadLNMFqIorS6BA9NTgOOnYp3FqizJakF0Ab2kIccXX%2BlyjmTOpuZBpME9b4VulMzPYDCAyvi8BjqkAeSfqrHQZdz4r3fGdQeUHFYG96kKpHJHBjbqOMleoh0zvi5DxGKPLUVaqbSKh%2BTyUcCtblZwpf39hmjx2L9Kb6EOTRgT4LvuuFnFtnsV%2B%2BtKyVYLIIT%2Bc1jpJMa%2B47hndF16JefAw0u%2BscsZsoXCsfapy89f7UBFqOSVEuGpVGsc8ncVe6q2sw6qXosDW6OUpcnP5B4VgSPMDukyctBSmgXc1D0M&X-Amz-Signature=c967dcc4e33b4f4c7c8d754470a1106c29c8e28446d1b15dddf4bd017355f41e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=5da05e10386ea3deb729e1a6575bb02d0184d6413cd3cb28816733ecad7c1657&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=6e76c775bef723b7a54199ed141cd87b71b6a8a9cfb665d0cc120a576032190a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=72a15ac1ccfa9b13960e3982a6cabb4e7142855b4b3413380ba201b9fe99ab61&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=d4f096e200d2f9ad24b920a42e70979decdd3b895d01aa5cb85f6f389276e683&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=cc1f53629b122d51b8ab9667b8b0ea894bbb7ea613c8f3b1e357cba1c2d95056&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUCMUKCX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOvfYKDRNlgYZEtKYJouW2JsrdYvo47L1X7YQtctMacAIgJMSofTbupN%2BSs4LNcSxmvWhYFCe2SQaO1xQLazx6wEQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDIR8UGS7IsFDOeX1yrcA9eh9qoMuN9MFGPdoptP8rb5IZmEkzSjIkwDFpbGn2d%2F%2BSUY7CU9gYn%2B2Ib%2FbEXH3GWZeJRO8GDT5cL1lSwltEX8WJbD11rzkRv7gjW%2FbSZhCa%2Ba3D%2FPZG%2F%2FXTNZ6%2BfSlmWZsb1T4cCH4INWJ8XgvIKSX3JZPhVP2vZ2FMkLGac2wvd0NuKzXo4P4XmDvUnrpXbe5jTjOAJ%2BM1dcPXmfvbHrItDe%2FdY2mdUAlBsZXOS%2BHZjB%2FW7FPJMQTL4XBT5MF8m5lqM6MV5rEqmCrshVZAs8j19pVzoRMUXWruz53uiZ1mEuiXWtxEsAAOudjyE0JO7jnouBRLskxrU0JihEj5R%2BRvzNjKfEAcBERyZtNxWsIAu6pGBR31GNwlbYGNC6LRghrUw2fLtANsRpAy7bICAokcTUfMYtkoz%2FnpM0g%2BcIzw2NRhvw395XU%2BlJpPkg8C3Td0rJoESEd2hGbjlI1wmvXjyHzSgySFZcnl0kzuFD1qzAlivh1%2F2oNzEcRHomZtTgOyriaK%2BxkbwJpWhgQ45pSLLseH3Y%2Bo8RoTRIDXwKmNGCNvjnGQgyI%2BUPrQYNY9uf%2F40fGMA%2FelUnIzD%2Fj%2BM2X5FTfXoppjJYoWOIg1mJkelzLh%2FQ0jcaVNJIMNPG%2BLwGOqUBNsgXtgSKye%2Bc%2FbKrMcZnQMRZAf%2B0M8GwnYs1m9QFBMu%2BWuF7PlHYe6nHIckoW2lBsYMcYSxqIZISfL2UVJQrdmGdZYgkrzSgZZ%2BOdJAtbrKGgWC9Ok7xf15VIlyK3Qdm%2B5pR7cSPonmiufgcx%2FOcSCp7qeqWMHpsJRcKpZfCLsuFAg2a4%2BTkJ92spdxJ5dcRYrJjv2CSs1CoyrlU5kQp%2BGmp3aV1&X-Amz-Signature=80211a5216caf5eb81f3977c9cfa856e71c1ebafd75af1f78f56de14543c2c66&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX3LL4NJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC1S%2FuqiSOAI8Fi%2BoBjw33n%2BsKiqpIAp2%2BYNjJ1jAprQAiEAzkbwoWHscRhTHBGupkBCPnmBzDBWQGwl2AaFueLymDMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAR9XdeWfBCnT7WMaircA1929EMBmMrSSBo642FErYMw0U4pHCItc72qLbWx9Ss0OoNVhzMxW2xbGLgvoonZp4u0yMf7BX1DJKNF6VPbp%2FIRnF%2FQiacdiYWtlXdVN9gV5d9%2BqhxXmepgteOzu8z0QjEOpcl2BYXpEXG5AP5LxogZPOoNC9R5dnYLzivq3pTIVn7HyJg4Ys7VxBz147GrjTp%2FkIx2x%2B4b19jO1HMP%2FUBNW4qD4%2Bcsanyxhobb2f6lRjHHHpB2m00shTiga72OP%2F%2FwwHorL%2F%2FraMk%2FN3QZGfSwVoNYEqSN66nTeItZ%2BSCwXpfjuDe6VC5F%2Fj9rrbXJQ5gJWG1orgc9HJIxrxWssgYGWYHJ1pKn2mUe7AbPdaW1FE3pexZo9f%2Fhn%2Bb%2BnU41mu2o0os57rc794Hsc%2BRcnp6xa2G1qGF0NY%2B%2FJRbGBaUL1Ju%2FSRLcfPX5qObLAj5%2F01p8kHEBOVwjplcBZVgLhZoTJ14u07HdJYykPQIZXPmGdbQ1DYYg%2F6eBfHSbIgHltrc%2BpFyLCpnztRQ0xBvxrsQ0PPuCigsGebwDOMjCxPIOlrYRiv3lt9Q0ti1kET3ocVXSHGyfntuGA6A6FYoZSI3ZHiS%2B0ez5Usgu84PV95jvxeHOXMSdJom5rhXaMPnJ%2BLwGOqUB8h0pPcu9OqppBBINR6k6vudWWBX4sx4Wcuq2gurMl9bV3tl8oVtdVyNRSa3sFyuRU%2Bp6kuiUXUIhaZLslXU4%2BhvhkTtdR9GwQSndsUs9f%2FS5%2FPQ55LwWTJMMysq9GsFxxkHV9pEPaCcdDpLXwR9kYaIb7e9HyZ0S3ggCEhKbz1oauz%2FuILcUYla9PCz8qHUS0HAhlms6LR8VHkPUOS3fxErHk%2BgD&X-Amz-Signature=2f0a12f5d3110361acc2df5b66c847e0834dc785c10eeb1795e19bbf64f78b58&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX3LL4NJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC1S%2FuqiSOAI8Fi%2BoBjw33n%2BsKiqpIAp2%2BYNjJ1jAprQAiEAzkbwoWHscRhTHBGupkBCPnmBzDBWQGwl2AaFueLymDMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAR9XdeWfBCnT7WMaircA1929EMBmMrSSBo642FErYMw0U4pHCItc72qLbWx9Ss0OoNVhzMxW2xbGLgvoonZp4u0yMf7BX1DJKNF6VPbp%2FIRnF%2FQiacdiYWtlXdVN9gV5d9%2BqhxXmepgteOzu8z0QjEOpcl2BYXpEXG5AP5LxogZPOoNC9R5dnYLzivq3pTIVn7HyJg4Ys7VxBz147GrjTp%2FkIx2x%2B4b19jO1HMP%2FUBNW4qD4%2Bcsanyxhobb2f6lRjHHHpB2m00shTiga72OP%2F%2FwwHorL%2F%2FraMk%2FN3QZGfSwVoNYEqSN66nTeItZ%2BSCwXpfjuDe6VC5F%2Fj9rrbXJQ5gJWG1orgc9HJIxrxWssgYGWYHJ1pKn2mUe7AbPdaW1FE3pexZo9f%2Fhn%2Bb%2BnU41mu2o0os57rc794Hsc%2BRcnp6xa2G1qGF0NY%2B%2FJRbGBaUL1Ju%2FSRLcfPX5qObLAj5%2F01p8kHEBOVwjplcBZVgLhZoTJ14u07HdJYykPQIZXPmGdbQ1DYYg%2F6eBfHSbIgHltrc%2BpFyLCpnztRQ0xBvxrsQ0PPuCigsGebwDOMjCxPIOlrYRiv3lt9Q0ti1kET3ocVXSHGyfntuGA6A6FYoZSI3ZHiS%2B0ez5Usgu84PV95jvxeHOXMSdJom5rhXaMPnJ%2BLwGOqUB8h0pPcu9OqppBBINR6k6vudWWBX4sx4Wcuq2gurMl9bV3tl8oVtdVyNRSa3sFyuRU%2Bp6kuiUXUIhaZLslXU4%2BhvhkTtdR9GwQSndsUs9f%2FS5%2FPQ55LwWTJMMysq9GsFxxkHV9pEPaCcdDpLXwR9kYaIb7e9HyZ0S3ggCEhKbz1oauz%2FuILcUYla9PCz8qHUS0HAhlms6LR8VHkPUOS3fxErHk%2BgD&X-Amz-Signature=4ffcb56cecfdae30944a6f7342636080433a44999f7149df233be7466915f77b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2NUD2Q6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYq5awZv47hFGe3FAAMTwtt2b4uGjbpXkpoUi5l21ruwIhAP39alxbUZ2Z7NipAURJzulm%2BavSg1Bld9ldI6yH7b3LKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyyh8ZppdEbHeh7OYEq3APck7F1NKGwYIiqnTbwdDsJ%2F2Ge8usgsbcQuaauz8EQX6RXvI8P9FWQTTDFgMdK94TKpIkmtxNVEROC2KpiJvfedvOGZRFJ%2BHI9Ve7xCguhTBoVBSR8brqpWBMzCIuTBH4TbMYHlCtne5USqyoX4FWTfey64K%2BjQF5ClhSe0wDTVtu3%2FSUYkJirCtBYm7%2BDegq%2BwhJVb3x6h2%2F1yPAmqfQ4wooiPfuxRW3Dog51vPRV4BvDSfqBynLpuwsnJwJXShFEC4z0dPxARRGQJYOgMkfUoDU98bY6ysAhbZA7%2F0N%2FAW1m30n%2FWei3%2FXnZ6lviEC9gwDJbZNRaFEYYsrOI%2FR05igAU1Y65FBEiTAtBQSxhz4e4VBTjDxfzKp5qs39%2BTvRqW3v9uDn8%2BBJmyOoeGuKvg%2Bi7b4qkTP2FKc%2BDbAKmHH2XlzYJPtZKoYT5WdS%2BvFkjnTRysMqRFkZkV6m5WRNnyrVkon%2F473l9Uo1VKR8Q98NvKKcYmNcVDDP6RtnmRPlLgFU8Ster092yt8tafOHD%2BpWymaY1IkErmA1NnY4wLzX%2BXQdvaQfFD264YzsHzauDqQMEeTACwcS2GPyK%2BCe2Ya%2FwT9L4y%2BdoXNw9Pyft3y3mIZ7mktfKY35%2BmzDSyvi8BjqkAYOELq%2FvouxSzUOiKB7hIVPNqDdUVXrKFCxkdHvXh33qcsiF7Hgjow0lloFOk9LR%2BetQuf%2BNju2a9mN4rTMtl3lNCnEzrUE7fJDyVkNN7l9jUimQmx9dkAKw31JLP5%2BcdN%2BXZCDyByx%2BT8PO8JSO9x2Jh9lcx%2FqE0WxPP3sLAdJE4CiCQih0TngS1ygFIvCbhY7fp9aIIbMhStozHLnvL9KHc%2FFp&X-Amz-Signature=ac8eaf20090f33f5545e1655131ebe14a60eb15c1fcfa87b6668f91ee1365076&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=d929e11362429dcdfeed17fd92b993ddac9f25a50a2996b592fa37ca4a82c175&X-Amz-SignedHeaders=host&x-id=GetObject)
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