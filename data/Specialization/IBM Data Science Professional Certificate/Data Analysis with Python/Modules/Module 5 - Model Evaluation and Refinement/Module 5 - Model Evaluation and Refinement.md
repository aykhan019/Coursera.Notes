

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=b3fb96e6ff8034d2bea0114ccbf5324771177463db6d7224b32a8fa15f26fc81&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=8d39ab3e70813b18bbebf97594f86ea07838869522f069d70b07122d91bc3847&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=f5d3cc04e6a03aba0565d09f924aeca58ac0323c342a790c6d5c012339704321&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=756004e48ad1bbef6ebf8fab528588295fab743b4dbe7574c2abe84c59592b04&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=4acfda4f779b7591af194f5d7102f12ea2994308b9767bfe62202cbe59403104&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=71c49744c21eb1d4a53d38276888675a4599bbbe6b63b44e5b0131516b26475b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=f8b5d79c4c1ece967360ad6c14ebdc8cea9eee31f0695005dbec16e9ff29342d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=c7738ced9ff014b876434b17a9191428ea2e7cac92ad0aea1177fa06af88b14f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=642993c86cf363007070a61a6884ef90f312c6d6c3b7ce0ca6c340a7f74ad538&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZTSFL3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDVJcfyJixTDWk9XPq1Bw6sYuszmZ12sKuc1iyMUuN4wIhALkRmolc6S01YJJW2WbW84GOShvXYhQnsBWkf%2FWb3shTKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAur6YBIdgwrJnP0cq3AMMhGUxr0T%2BE3eF7OOv%2B0PUpeenrMjDh5AlASeeJZ399ySyUUWQruB4UMKydUdwNwb1p9EWn8gXTpep%2BDFt0%2FLDeVSXK7mGbSa53sUWBWxO0QL8HarOdg77xM3x4PnQg2HRBmXqWtEwo9IILYw6T1cYR%2BGG9Ki7VYyJgJIYIt9zHxsr%2BHH7I1XW%2BqokRqVaqfa1Ji4d83%2B%2F9eY9ShN8JjvMEUoPfoWLceSG%2FfydWcfrZIz5ACbHJdLgIvoopvtp0LEKPcu%2Bf%2BjWcDsmgv76ERQ9MihzwdFUzMZ2NW13pnDVbyDyB2ESkZYJUFmhc8wqkA89mGN8a8MZwaeDXWfCd9qLdVGsQYLtyqvr68rEjkiMhl44oz2mVeXGKTVZEykHHD9JUIf9fWZGXSiiGV6wmGWJ6kCFYYBC2DPA4pr4VJXHZNXR%2FcgcNeHB24e0bSm7Zb46HpkGUeYlXeULXH92Pv2MyYWU69mZOB8P9ub%2FmiqEnmm8MK4fHOLGRABreOvumQ5nVecj1r6UaJqOZfERgnbgOZggAk5Imj%2F1kySHwvNN5Zy%2FAynrXC6hfYyGWu5JE4F6OO0Fyhzd1O5exXXBkMGfwrwq5P2rPhl9XbvCmGGigT5tacXsDhTGSeYX0DC%2Fx%2Be8BjqkAWk5cwIqntM8A1YUcIbBPnyHP0mF3G%2Fd3kV7G7yS%2FadB1tnKluMC4elpnbgkJe1hv87aB00I0uhrx1ZorNk8tOOFfkCkeCz5%2F2iVDx290mp9ql9CuIn7ruHOEe5a%2BUXzMvtShaPQTRLwqeY6MFNIXHxPBDjdreAmxUxsKwwLBS6Q9fQyHzj0yaxbgKjJqYjp5VNRM%2FsCgWozmJYZKR85n2Ran71Z&X-Amz-Signature=dafa4cbdaa9ec2372b920859b8efe7978fa05d8f0db404e41c50c9eef6e38087&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZTSFL3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDVJcfyJixTDWk9XPq1Bw6sYuszmZ12sKuc1iyMUuN4wIhALkRmolc6S01YJJW2WbW84GOShvXYhQnsBWkf%2FWb3shTKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAur6YBIdgwrJnP0cq3AMMhGUxr0T%2BE3eF7OOv%2B0PUpeenrMjDh5AlASeeJZ399ySyUUWQruB4UMKydUdwNwb1p9EWn8gXTpep%2BDFt0%2FLDeVSXK7mGbSa53sUWBWxO0QL8HarOdg77xM3x4PnQg2HRBmXqWtEwo9IILYw6T1cYR%2BGG9Ki7VYyJgJIYIt9zHxsr%2BHH7I1XW%2BqokRqVaqfa1Ji4d83%2B%2F9eY9ShN8JjvMEUoPfoWLceSG%2FfydWcfrZIz5ACbHJdLgIvoopvtp0LEKPcu%2Bf%2BjWcDsmgv76ERQ9MihzwdFUzMZ2NW13pnDVbyDyB2ESkZYJUFmhc8wqkA89mGN8a8MZwaeDXWfCd9qLdVGsQYLtyqvr68rEjkiMhl44oz2mVeXGKTVZEykHHD9JUIf9fWZGXSiiGV6wmGWJ6kCFYYBC2DPA4pr4VJXHZNXR%2FcgcNeHB24e0bSm7Zb46HpkGUeYlXeULXH92Pv2MyYWU69mZOB8P9ub%2FmiqEnmm8MK4fHOLGRABreOvumQ5nVecj1r6UaJqOZfERgnbgOZggAk5Imj%2F1kySHwvNN5Zy%2FAynrXC6hfYyGWu5JE4F6OO0Fyhzd1O5exXXBkMGfwrwq5P2rPhl9XbvCmGGigT5tacXsDhTGSeYX0DC%2Fx%2Be8BjqkAWk5cwIqntM8A1YUcIbBPnyHP0mF3G%2Fd3kV7G7yS%2FadB1tnKluMC4elpnbgkJe1hv87aB00I0uhrx1ZorNk8tOOFfkCkeCz5%2F2iVDx290mp9ql9CuIn7ruHOEe5a%2BUXzMvtShaPQTRLwqeY6MFNIXHxPBDjdreAmxUxsKwwLBS6Q9fQyHzj0yaxbgKjJqYjp5VNRM%2FsCgWozmJYZKR85n2Ran71Z&X-Amz-Signature=c9cc6204be46d99d97e1235c2c9856a70d832066eefb7de737292160af5b2b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZTSFL3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDVJcfyJixTDWk9XPq1Bw6sYuszmZ12sKuc1iyMUuN4wIhALkRmolc6S01YJJW2WbW84GOShvXYhQnsBWkf%2FWb3shTKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAur6YBIdgwrJnP0cq3AMMhGUxr0T%2BE3eF7OOv%2B0PUpeenrMjDh5AlASeeJZ399ySyUUWQruB4UMKydUdwNwb1p9EWn8gXTpep%2BDFt0%2FLDeVSXK7mGbSa53sUWBWxO0QL8HarOdg77xM3x4PnQg2HRBmXqWtEwo9IILYw6T1cYR%2BGG9Ki7VYyJgJIYIt9zHxsr%2BHH7I1XW%2BqokRqVaqfa1Ji4d83%2B%2F9eY9ShN8JjvMEUoPfoWLceSG%2FfydWcfrZIz5ACbHJdLgIvoopvtp0LEKPcu%2Bf%2BjWcDsmgv76ERQ9MihzwdFUzMZ2NW13pnDVbyDyB2ESkZYJUFmhc8wqkA89mGN8a8MZwaeDXWfCd9qLdVGsQYLtyqvr68rEjkiMhl44oz2mVeXGKTVZEykHHD9JUIf9fWZGXSiiGV6wmGWJ6kCFYYBC2DPA4pr4VJXHZNXR%2FcgcNeHB24e0bSm7Zb46HpkGUeYlXeULXH92Pv2MyYWU69mZOB8P9ub%2FmiqEnmm8MK4fHOLGRABreOvumQ5nVecj1r6UaJqOZfERgnbgOZggAk5Imj%2F1kySHwvNN5Zy%2FAynrXC6hfYyGWu5JE4F6OO0Fyhzd1O5exXXBkMGfwrwq5P2rPhl9XbvCmGGigT5tacXsDhTGSeYX0DC%2Fx%2Be8BjqkAWk5cwIqntM8A1YUcIbBPnyHP0mF3G%2Fd3kV7G7yS%2FadB1tnKluMC4elpnbgkJe1hv87aB00I0uhrx1ZorNk8tOOFfkCkeCz5%2F2iVDx290mp9ql9CuIn7ruHOEe5a%2BUXzMvtShaPQTRLwqeY6MFNIXHxPBDjdreAmxUxsKwwLBS6Q9fQyHzj0yaxbgKjJqYjp5VNRM%2FsCgWozmJYZKR85n2Ran71Z&X-Amz-Signature=8dba7b7a97dfd302ebc399070e21d94f58014af5a540e9c0767b51147cef13d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=861a605dc635e2fc24491552fd2639d4036a77f2336ecd0cfe10b90fe3e33eba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=29eb19d3c5acb74453845a8cc90e178304b553f3ae73fbdcb9f325ae69c9146a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=33756a61d884441705114cf6943b11dac9328c9680a13a51bf3f8460545edbbd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=694073be302c8db58c84151c054eab941ca758157e08ecafd601c3ef7a1f743b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=32b38466c957addec5caba014677c77b50fb4c9c93bab39603a9dcf771997c81&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLX473YR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5Leimq1sCDIULFKUFnz2sdI6vMKrLeJBu93N0iLBMigIhAIcJCyjT5Dumxhk8EaknckA%2FMYr6wk9nq8hqk7P1RMwlKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxowpnh18hRnm4bTREq3AP%2BOn4d9D%2BDOJyq%2FB1dlTv3Rg7wX6WjQXCTj3uB6v%2BVAqa2%2B39yvM5ma9P5I9VrFVbtqvBlK5IeS5kiI0%2BnngUWLMPsdLukzPhT2Bcm3MFg7sCuOHjBiMsAJS8dsHE%2BVIe6LZCDyl1SIsSJpFtLyuIgAv%2FvfVy9dSjMLPIGhOqKM3BCgG%2F0xsu86ScUu41DpExHpCMdFI3EXNcDOucbmDOROp5iqX39SkxxHxlDqLd644Ambb6oSEe%2BkXc72GD2dnAVEhbLHGWoTA3xACeHfCOdEGyZ82PIP2PESv%2BglgaIcv3RK2%2F%2BNih5WmiupWtvaNFME8RcvUsbo8Vk5Ee%2BL3EmF%2BW733OkEPEeVuDWGjUAhsUhXEcAMu07IeZrzp%2F0oIWujGcVgJLg96ypsbA58Scz4Ruyl2tRV9tJ4Bhb6v4fu%2Fro9UQZwdO5CCsizRGRkZCxGa4%2B3TCk2v%2Fbj74OEYJHg6iaL%2FMAI2nkW6wQDn7LyC3gVI%2BE8TUln9p9XwO7HijICZMLNfDgCRb7q6w0wmMGJh6Axb1SWoAv%2BXaqb1cZaffVJLz1vyHtZ%2Fj7VQxQuTZYrWJ3qZHkQ4KSmv5%2BT6GFgQUtp3k4OjmoZWrZc36Y3XzE5E0rzI%2BrMyHA8TDLx%2Be8BjqkAWKyWffa0hoQEEW8ipFN9Ckyb8phwpx3y3rtnnrRgJEuaiwy1LM6bE3o%2F7MnR4QEhrQ8%2Fbn9UhTpR0HoXJydXhc8nFO%2F6cW%2FtXUXBP3cEtInd0tewu8JuW0qFekgANnBS77eyuAR0HCnSvQQZU0xsrf9dfpY8rpNBR73S4Dz%2Bcx7TgOC4%2FN6v2Mw7JVNqFfTEADK%2BMc4fNSi7fY8NBtCZiAZABWl&X-Amz-Signature=d69989085d25704e73259eba1b6569fd7fd8936ffb91e202f9f0e9e870f58290&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P6EZHQT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZYYyPX3PwNs%2FXOHmJLVU4ELar9tTGUIx0IEHZteWazAiEAxjlI%2B%2B8zkZoAhmwVRNv6EDscpkSF1MgM7BxrKf%2FwDdUqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCs5hTVuxJBnTX7dICrcA6SH6ltAKW3JRb6glJzcT8Jjc%2Fxc5pOjC%2FVeUV%2FE1vbAfz%2BWKs3Rv2wpMdnvKnfVOTn%2FsphD%2F3nS%2BxnC8NF0EvpghD32qRz74xWrbyVbYDalJqM9MdKnNZNCq4JS3Vvip6BycgaAK9uKBDq0zmzLqbBbr7JgAY3qDZXUndWuKwSMbYiuyHQI9pZmM%2BuGCZfsn75aB%2FzFHUA8b0OUK2b%2BnKuqMaGlN3CDtzGSh0vkNfStFnrRuK3l%2BGY7Q4zh%2BmGIVDszRuDtpRsZUWiWWhqh3ps526b7iKjp2qlHp5lryVKwoMKoVQlfaRK4G1fxlz6HHqn4CyNc2QsVZiRRnnAi0EHZ0BifVGYvRI0IIBa9wUk28zZKkVJr5v7sxri2NuxQ8JY4vZEfsOojIAVukDPnbpUY7sCDz77SamgCj9IIq36afjK7vC2O55aYxWDUrIpFjNOBo9na51UHuVOHci6cc%2FLFtUJ7apxk%2B13LLprPM203N25o36euC5K8oblTF%2BNEZYFYEEDKD0xeLVmSy3BiuOXXPbTrQval57osvWRK6OVuUnSBdf%2B%2FkQfpeCCYm%2BouB7v47QbQB%2FmVr9GmZjLype14ONzaje%2BohUnTQI2uuKzzPzIWpQ6y6Wxlvg6cMPms57wGOqUBAfyzeqdCvcWcdy5bd7PvzUPsqXCobftaDD0GSHcImk9NCKJ4g1%2BUF3d%2F56gc%2F1H2hIfkbh7f%2F7aGEu7euzOrU173SX23T9TVtAyLxNNsMZsAPOYOPANTDI%2BqoaKJF%2BIfXZWxHkZocg%2BJNnD1mMq2IoSEZJgbiD7ng43ztaWaFlit2V8eLCoqp7F1JgKV6U6wnyt%2FGQMAVB3HwdcFf7XVySbohvCP&X-Amz-Signature=9afe0fdc0bba6fa9030b55ef84ac3dc68041ecf51f7877a4f1e503dd47cbd4cd&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P6EZHQT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZYYyPX3PwNs%2FXOHmJLVU4ELar9tTGUIx0IEHZteWazAiEAxjlI%2B%2B8zkZoAhmwVRNv6EDscpkSF1MgM7BxrKf%2FwDdUqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCs5hTVuxJBnTX7dICrcA6SH6ltAKW3JRb6glJzcT8Jjc%2Fxc5pOjC%2FVeUV%2FE1vbAfz%2BWKs3Rv2wpMdnvKnfVOTn%2FsphD%2F3nS%2BxnC8NF0EvpghD32qRz74xWrbyVbYDalJqM9MdKnNZNCq4JS3Vvip6BycgaAK9uKBDq0zmzLqbBbr7JgAY3qDZXUndWuKwSMbYiuyHQI9pZmM%2BuGCZfsn75aB%2FzFHUA8b0OUK2b%2BnKuqMaGlN3CDtzGSh0vkNfStFnrRuK3l%2BGY7Q4zh%2BmGIVDszRuDtpRsZUWiWWhqh3ps526b7iKjp2qlHp5lryVKwoMKoVQlfaRK4G1fxlz6HHqn4CyNc2QsVZiRRnnAi0EHZ0BifVGYvRI0IIBa9wUk28zZKkVJr5v7sxri2NuxQ8JY4vZEfsOojIAVukDPnbpUY7sCDz77SamgCj9IIq36afjK7vC2O55aYxWDUrIpFjNOBo9na51UHuVOHci6cc%2FLFtUJ7apxk%2B13LLprPM203N25o36euC5K8oblTF%2BNEZYFYEEDKD0xeLVmSy3BiuOXXPbTrQval57osvWRK6OVuUnSBdf%2B%2FkQfpeCCYm%2BouB7v47QbQB%2FmVr9GmZjLype14ONzaje%2BohUnTQI2uuKzzPzIWpQ6y6Wxlvg6cMPms57wGOqUBAfyzeqdCvcWcdy5bd7PvzUPsqXCobftaDD0GSHcImk9NCKJ4g1%2BUF3d%2F56gc%2F1H2hIfkbh7f%2F7aGEu7euzOrU173SX23T9TVtAyLxNNsMZsAPOYOPANTDI%2BqoaKJF%2BIfXZWxHkZocg%2BJNnD1mMq2IoSEZJgbiD7ng43ztaWaFlit2V8eLCoqp7F1JgKV6U6wnyt%2FGQMAVB3HwdcFf7XVySbohvCP&X-Amz-Signature=c31eaae2b94440eae78ff20f4e0f4d34f5027ac7bc4e3f40343cc33db9e59052&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662PQNJ4Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmzaD%2B6ZXorlCoX1P%2BRO7%2BnNvv2088pVSQKmP7SkCMnAIhAPDIopZ%2FZwFeTB9DT6cfAqTCPD8RA9JDmeOXdYQwhDQSKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTJ7CjdqhheRXlrk0q3AMPR5CEEo7uydCDH%2BRnb9N%2FSU8Y1QSyQWm783qkbIoTfwkgZp%2FSD9qDm8T8d3kyOmF1T125thLTPgOlcLBcstODi1GANjIFYokbGZxoTX2wTqts%2FwSj9pIT%2BHfzPekOEgOR9dL8sDfI7qFIm3uRjDda4oOUNV15m53DQ9p1XdSFL9GOebnTvH8LkY4X30v7Nm%2Bq4X5u%2F4Aw09sx2luQ%2BofH%2BMnWSCDdl9w3h0tYKebdaST7Dg7r0VNLESTOTyzhJ430LjjsqESsmVEz%2FgQP2tReQgZiQZoTuVlT695MQ0DqIEMv4JCxbhyKVkB3V6raOwf5vIyGA%2FLzSboINvsOmr0AoFg29GfMG7PsNFxceMNZWzR20vC6ljsgT2x1cVxQlnuyexv0B%2FFRpYm4s9TbmxhKARxnvEi8P%2BRudvE5BKiWhd9CkzJlPsUCksT049zQsP8E%2BHa3PdyTIMlhkc8p09Qc4pol%2BbKI5sA3w2UhCbPPeD%2B6j8GAH6lQy9DhnkQ%2Fj6WQqTAD0uekJ7kn4o%2ByrXe2vU5JbWZMpZet%2BjTDoHD6kjOFwl8BLQgF%2FtAnnxBDBpXEz06L9tJ06zH5RfNNVQVp2d3%2BCRxFfq2Mr551iQ7Kmd2B3K4R%2FPUX9f3A5jC2ree8BjqkATZa2cVpfKHsWO9ShcO%2F4PX%2B34HiFIv8SQafZx0Vlz2ACsFQQ5xSD3%2BDBYbdqoJ%2FMIZIkS6tPGm8LwdkIyfBC43bv96lFT7pBUHBLX5VjEG%2Bcu%2FrBawjImcBeI9AlTDxiHTrYZCJe41qj3PySk7cOX8dtgmcLeOrZb%2F7SzArSJvnyERDRULtn2iXjSuEbQ61%2Bvl%2FbFHaowXXTbXKuj6S9SmJ8t9R&X-Amz-Signature=335cdafe2146424f9d1dd6df382c6aea2500adca216a6c5344d64ad3e4a0f24f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEHNBRO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhVqKi5t2OCA%2BskEqNiqxROtWnzs4GKZv2fmeME0QGxAiEA1wl3uyptC2%2Fx0TqvbhX8x31A%2BcLolJg0bnrtk84pFJ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKce7niwqMv8zzsiCrcAz7ZoGbvLhAzrQUGXpvm8040JGfWZjgceCSeCFb0s8u5QUie0BZqk4NudNGLMXQLN0IV93OolOBenaaaNkcKm1ZLkuAW2LsAwoZjyaDsC1jFu89Myt0lMzTuJV9Ok9j2%2B6BO6He70DS89Laqj0RO%2BGIAfyOSYmFfg0WhuWfAsXaHJ2vr2HCm625fvLyaXBpZ%2B5coqnbWp5DPFtRTPk0u7YAQHYooUs87dNmygFEZamxeIHqc4A9p2xXzcdT4GOoF1mEqC27jW088ve284pZzSqtcpgO5LhWAAXUVCDPlt9nKV0ivDTkec5umui7IcHrrZknfZUWH6G1T8HRqatT7124rUeuzFicD99%2F2eB2skrtOIcvqbQC1PHyVXCBRWDdHJBhXtdR%2BDX85gKFENZIGDl5TynM%2BekfkmXMAdptGeu0Iu6ORIeuO%2Bm0p1AypxtQoQ1BwPVzmGcfFV6ZhPHAfxdANYuqc1qrWG%2B526qM26yOGC6K34xOsXR%2FoLBdw%2Fz1iHwFSxs5Ci4RVlltruUS2gIjCvhTeOUJNtxkREJrlgtnERwgrBNLHf1JmhaFajR9ToTDnprssXolNMzJgwoJxkosJ4w%2FcW7VoH1%2F%2FCQp2vxr9bkNT5CDjhUfaEC0TMMPH57wGOqUB5MBLyZNHJILi%2B7AXFuTJ4YyaqKIj4mtKywVKTe7iDBe4kKSwj19ZkeuqFtco7z2PChjLtHUMHeq4W8hh6dXwqS47EqcWOCyWxZrZAyZRUXPYwRnnoa%2FjETuZ6tn5WzvLdERGrmfiQTUlIhGMXVOMlkFXv%2FDHzqDj1WcBprFDNgAssWPiC246GXVl5d7%2BoVVhpk76HnglGvAT3S36%2BV20VpympiNn&X-Amz-Signature=831316333dddfd4e56ddedf4c579134e3e4d4ca3445e783783b3d2af05e04633&X-Amz-SignedHeaders=host&x-id=GetObject)
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