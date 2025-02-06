

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=360672ae6bc6f721e8b38c6d22d14266825ef78b270f2060a04ac4aa31868bb3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=a0cecbb11aad959c77c684aa5f74045b34f26e7faf9cf706fa72fd49db590967&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=16aedb8066de136a616829ab3706fdbf4d1175fcb097fa5342f616e4a10152d1&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=148c0bf653de7cf98263a5aba2544687c89b696a5bf2b6cb935c36c09dbfafc8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=53b617afca5b3336ebd674afd3a33d448babff682006a840511864e906a917b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=a12030541c33686eb1e3eb84614a6d4cfaed6893a30f1a5da3b9962161cffc20&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=26604b6d520f6fd253f339aeaa810eb501504dada225e3ac201ae72775ff6a69&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=be7fd728571b3702cec3e3fa7c279b7472440b15d2a31141066b19f53645bf3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=77978e28fa66bbb6f6ec97f2463808bef71daa9d08e565bf2c90ace47b2668d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSIX5OIM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIESXVWNXj4lGz8uV74uJvJqGY9TZH1Y1if7odYHmTyfJAiAGcAMrrqpcQ5LjL%2BlpuGL5oM1UXH3qmal61xurrq6NJCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM6nbFrhAEBRxhdJN7KtwD3LQuZaPPKBXFQTDIqYaX%2B2F7U8KDbuEIIP2SSXhmtvn%2BElB41UFXXbE1XFxk7DuRVFuvuBL%2Bzj3zVOPPjOY29U3D6L9N8BZ2yyF3QN7pmwmQzY1zQ6yWnYLP0y9zIsJXChSVqe5qS1l4tqecocqDZYjkPdOS7%2B7zw1hPLx2jxN3ig0D3EbFKW1RlNlK2DLKP8eJlEaaCQRnsrqXT52GXlSnXqnzLpLKb4MExnWKya8inCuLX%2FsUfzp%2FeF2eYHD51AqmcR8rUl%2F1n%2F%2Fq4BIzOEm6KTY0roLYrr96UbquxXQxbSjDkgV63AbHgyqENXp%2FdA7nwdhkaBq60ap4g%2BiYmjcHYsFR8aihILQBn5a5X3xUf79LYLFr86xxskAVQ7BV3p8yiMfG%2FJFZIV6DpKrggNt70aDtOHnDTezauyQn3Qpgv96rMa46AB%2FFHojDx2x%2BAQanmCzwj0RGgNeCunCBM75d9ppigeqvPc9tVs6XMU4CAWr5PY5rscDM3hlMD6ZjLuW8AMi6ERyiJEcTtdLrAyT8Calaj3VZ9Q6qkkPKNVsKv4j2ztfsy%2BjGz0VYKH62Y78LkAmORZ%2BJdkNhdKYU3IoeqP6dwS%2BKOaGYe%2B8wIbP0hSW2Ux0CC%2Be0rssIwz%2BqPvQY6pgGuKKgNZIwbtcY1WuFH4X%2F%2Fh9sSLcOspZgABAXON6a%2FRHLhVyFH0vYZda4x3Ge1x6lOa1cKuSsy4z0sxP80ujZbu52Rq3ONQUWN4U0kqDQYDx18lwpfIPmBmiPaqtcjLRVqpVkJpVMylgLC9qhWIHCwsB8Ft7a0qtDoOOZIPgMWsGpTcJYjfcWjdhdbUMl%2BjDlAmu8t7EtbDhFcIrgUi6qCG7NhbBdF&X-Amz-Signature=685c1dccc02a85cfc874134ba58682f34c55fb5394dea081e862374bf6d5ebbc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSIX5OIM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIESXVWNXj4lGz8uV74uJvJqGY9TZH1Y1if7odYHmTyfJAiAGcAMrrqpcQ5LjL%2BlpuGL5oM1UXH3qmal61xurrq6NJCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM6nbFrhAEBRxhdJN7KtwD3LQuZaPPKBXFQTDIqYaX%2B2F7U8KDbuEIIP2SSXhmtvn%2BElB41UFXXbE1XFxk7DuRVFuvuBL%2Bzj3zVOPPjOY29U3D6L9N8BZ2yyF3QN7pmwmQzY1zQ6yWnYLP0y9zIsJXChSVqe5qS1l4tqecocqDZYjkPdOS7%2B7zw1hPLx2jxN3ig0D3EbFKW1RlNlK2DLKP8eJlEaaCQRnsrqXT52GXlSnXqnzLpLKb4MExnWKya8inCuLX%2FsUfzp%2FeF2eYHD51AqmcR8rUl%2F1n%2F%2Fq4BIzOEm6KTY0roLYrr96UbquxXQxbSjDkgV63AbHgyqENXp%2FdA7nwdhkaBq60ap4g%2BiYmjcHYsFR8aihILQBn5a5X3xUf79LYLFr86xxskAVQ7BV3p8yiMfG%2FJFZIV6DpKrggNt70aDtOHnDTezauyQn3Qpgv96rMa46AB%2FFHojDx2x%2BAQanmCzwj0RGgNeCunCBM75d9ppigeqvPc9tVs6XMU4CAWr5PY5rscDM3hlMD6ZjLuW8AMi6ERyiJEcTtdLrAyT8Calaj3VZ9Q6qkkPKNVsKv4j2ztfsy%2BjGz0VYKH62Y78LkAmORZ%2BJdkNhdKYU3IoeqP6dwS%2BKOaGYe%2B8wIbP0hSW2Ux0CC%2Be0rssIwz%2BqPvQY6pgGuKKgNZIwbtcY1WuFH4X%2F%2Fh9sSLcOspZgABAXON6a%2FRHLhVyFH0vYZda4x3Ge1x6lOa1cKuSsy4z0sxP80ujZbu52Rq3ONQUWN4U0kqDQYDx18lwpfIPmBmiPaqtcjLRVqpVkJpVMylgLC9qhWIHCwsB8Ft7a0qtDoOOZIPgMWsGpTcJYjfcWjdhdbUMl%2BjDlAmu8t7EtbDhFcIrgUi6qCG7NhbBdF&X-Amz-Signature=c56983cdd02a529d1d1a4795310189cd0271d1b67e766f3f24fa44fa84d83128&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSIX5OIM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIESXVWNXj4lGz8uV74uJvJqGY9TZH1Y1if7odYHmTyfJAiAGcAMrrqpcQ5LjL%2BlpuGL5oM1UXH3qmal61xurrq6NJCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM6nbFrhAEBRxhdJN7KtwD3LQuZaPPKBXFQTDIqYaX%2B2F7U8KDbuEIIP2SSXhmtvn%2BElB41UFXXbE1XFxk7DuRVFuvuBL%2Bzj3zVOPPjOY29U3D6L9N8BZ2yyF3QN7pmwmQzY1zQ6yWnYLP0y9zIsJXChSVqe5qS1l4tqecocqDZYjkPdOS7%2B7zw1hPLx2jxN3ig0D3EbFKW1RlNlK2DLKP8eJlEaaCQRnsrqXT52GXlSnXqnzLpLKb4MExnWKya8inCuLX%2FsUfzp%2FeF2eYHD51AqmcR8rUl%2F1n%2F%2Fq4BIzOEm6KTY0roLYrr96UbquxXQxbSjDkgV63AbHgyqENXp%2FdA7nwdhkaBq60ap4g%2BiYmjcHYsFR8aihILQBn5a5X3xUf79LYLFr86xxskAVQ7BV3p8yiMfG%2FJFZIV6DpKrggNt70aDtOHnDTezauyQn3Qpgv96rMa46AB%2FFHojDx2x%2BAQanmCzwj0RGgNeCunCBM75d9ppigeqvPc9tVs6XMU4CAWr5PY5rscDM3hlMD6ZjLuW8AMi6ERyiJEcTtdLrAyT8Calaj3VZ9Q6qkkPKNVsKv4j2ztfsy%2BjGz0VYKH62Y78LkAmORZ%2BJdkNhdKYU3IoeqP6dwS%2BKOaGYe%2B8wIbP0hSW2Ux0CC%2Be0rssIwz%2BqPvQY6pgGuKKgNZIwbtcY1WuFH4X%2F%2Fh9sSLcOspZgABAXON6a%2FRHLhVyFH0vYZda4x3Ge1x6lOa1cKuSsy4z0sxP80ujZbu52Rq3ONQUWN4U0kqDQYDx18lwpfIPmBmiPaqtcjLRVqpVkJpVMylgLC9qhWIHCwsB8Ft7a0qtDoOOZIPgMWsGpTcJYjfcWjdhdbUMl%2BjDlAmu8t7EtbDhFcIrgUi6qCG7NhbBdF&X-Amz-Signature=9c33187e65d1cc117de08bc127dd89b6c49e91c29fd9f5a71f087590bed2cac3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=091b5683f5a689d06fe763eb008ec054cbe79f64f486b24458039624bda1d70f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=2fec5cc970beabb1d6f15816a5d6e274f877c8129f4573644516541bdd45140d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=83793ea0075db5acb614a1e38f0c429cb7e84c79d2181661ac393d03ddf08229&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=f68d1e4b55b0adbe78a2816b0e144a676c007638c2852d161f1fbe3294d18ea3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=ca8651a81bf847155a2f622fdf466568d7b6d33f16081abedc8cac0e2025e3b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y77Y2DMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIHMXVxcAzY7phbJn1uUHqVP1t7bQh4AwrqByvu59tgfpAiEA2IWKhz%2F5OcLK%2FPelLZfC0YvcsoJSUMmjlhk9l8YYrWUq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB7PeIyzPA6koFKg1yrcAx8sGeiYBcar%2FXRpHGvK5GOx16F1o%2FuZiuETpcr%2BIIiO9xwwjYA6UUoE3lCPBquoi4aux8N8FVWUVxvEdXfga9lBj8G3eqIrObIlg5jmbR4%2BlhVTTnkcSRbhfBhqBjkWMm2mvABm8uRtZgXvrCZPKR2HxQrMjazLe5xA%2BMy8oR%2BnDlQSsbAT6g0Z0%2Fjk4%2BLiM%2Bfh6x6fShdbHQChcSko0ePxjsaD7tL5UHgo7QHut%2F5hljnKVmrVlIwwvoqNUdgctCxi7RJ0lR1mtY8HMjoSsIn9xxQXxsWxQbHDcVR6FYchxXgEp1ju4vsInK2YWrg8zhkLGpJK%2BI%2FyXKDKa7EEpybZy273y3OmQh2YNvtlgMIsbNrm38Q7tvT%2FghnqYyjj8jqvT1M%2B7NKDXh%2FZmQpKT7aebLoaTaPXoWi%2FASpnKt1o2WvZSe9fuE%2BdSZ2O5%2BwL5Z7ZFT9Vy1w6gbOSgcp97AXcwJ30IeYTlHhAcvc%2Ff%2F99Z5BIjzDAeoZ%2BDgiljZwWb9zXx1ErIbSTiJ14hdvHq8yaSICxnl35o%2BFnJDSnKeedUic8wzoTjN46myqHWzrhB9HgF5j06%2BdNr1s3ggfqyEXTY9SOEXlAT1E4IQPYfktNeeXWywODE1hsTw%2B3MMrqj70GOqUBw020DOAutOAqCGV3IPPQlfmf5%2BScq4c1ptWip7J4wxH7m8f5AzPYkIj%2FiARltmdKV6UV%2FTwMEjbLs9uwKfXTLeJcmxd%2FyALGSyWcUDtX6qAa7WK0ee%2BdqZTBkO%2BkECUxNPi8wbv%2FfCtxZLn4rVcgzShSkkcI8G28OlH05w1XUzTz%2FUmyzkxF%2BmUe1JjCX6xyGItkWLrGpFgHbmPG1b4yb0w9TnoI&X-Amz-Signature=5ced43e401539f7940ac59f0a237f251ca0505ced7beb5b9aaef25197f5601fa&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU32KJAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQD8lpXQmXV2TKr36uGN3jpXnNMyfDc7xfvQFVVRhToejwIgGpIKlhYCyBbzyhQG99bZxYE1sO%2BsAe%2FxbOfdBgwdKdgq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDDvAig8fg%2B7%2Fc7NwbircAzVqv99k41AFDzqW2CvAa2EaJMPFkRoHupL5xc5DZTU98GXY4Bn8MOdbx35mj5zSKn7BsBlenE22v5XTKM%2FFPoPk7avZ9RKm9OtHAMDOkpxNHLZKeQDzujIoJhBGxceenoXaKp4XnCUBn2QJTxONdGXv2NH%2Fi2ei7IBAPayBtf9SMRg90P449fYn1%2Bb5ycRym4A1C5DepxBlsyp0XS5M9P9AwfGeHLovEFi4%2F%2FRfRpOvZeweWl5kToZkM8B138bUxig9n71EANLL0YS0yu2fquWvGP7R%2BAktoVgOwgxwEvIDdLIHUk%2BnL6OzNGgFUIrrj%2F1gPwkwxVrw5bpsS147DA9t%2BsaxUaGs2ryxAlzB4hAKb6UjNoA4zlg9rYv4SXkkmQgqSdKFhE4qbmt0ZD20UukH7sahZg1%2BFfVT%2FB1jWKuPWDt%2FIYb6W7kK%2FSxc%2B1pFPvu4MTDNtxFjiN9NzmMoKbeGcSlQp0I%2F7bmEnjjazTrxHXJndo8YeWgKneeBioO3pUFIno9zA85TWW7X7rYUFbgsMWP4xtyqZ%2FWy8l0WvbOIKGgA1%2BSkhXjG0hoDPsr1cmpGI4A6pRVzI29RoS3RV%2F%2FtHqzXmHU3QbVU60m8IdJ4JqBvO8wekq4L%2FXsLMOjqj70GOqUBChEOhcjvOVdRkCu3GWofIJTPbOrtQHupMmy9bAKpOHgT8G7NCikU4PZnDOpEr%2FEVELK4xydIWgawf0HnfxC%2BUNDXy7dN9nk%2FJkoJgl29EQe8WxwaJFn4Dvy2f88ID3jnBi58wf81ag3lCzXN%2B9yMN%2BypwvkAMI0Mo45kJTUzBwIBDRCuQkqBhU8jg%2FqXo2%2FN05DRS9TBZ8sB1EfDCy8ATu4g9PZA&X-Amz-Signature=ad32e7df4838ab7fd9b7aecc0f26d5f1478bcfc3a30512053a961071ee2130b8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU32KJAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQD8lpXQmXV2TKr36uGN3jpXnNMyfDc7xfvQFVVRhToejwIgGpIKlhYCyBbzyhQG99bZxYE1sO%2BsAe%2FxbOfdBgwdKdgq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDDvAig8fg%2B7%2Fc7NwbircAzVqv99k41AFDzqW2CvAa2EaJMPFkRoHupL5xc5DZTU98GXY4Bn8MOdbx35mj5zSKn7BsBlenE22v5XTKM%2FFPoPk7avZ9RKm9OtHAMDOkpxNHLZKeQDzujIoJhBGxceenoXaKp4XnCUBn2QJTxONdGXv2NH%2Fi2ei7IBAPayBtf9SMRg90P449fYn1%2Bb5ycRym4A1C5DepxBlsyp0XS5M9P9AwfGeHLovEFi4%2F%2FRfRpOvZeweWl5kToZkM8B138bUxig9n71EANLL0YS0yu2fquWvGP7R%2BAktoVgOwgxwEvIDdLIHUk%2BnL6OzNGgFUIrrj%2F1gPwkwxVrw5bpsS147DA9t%2BsaxUaGs2ryxAlzB4hAKb6UjNoA4zlg9rYv4SXkkmQgqSdKFhE4qbmt0ZD20UukH7sahZg1%2BFfVT%2FB1jWKuPWDt%2FIYb6W7kK%2FSxc%2B1pFPvu4MTDNtxFjiN9NzmMoKbeGcSlQp0I%2F7bmEnjjazTrxHXJndo8YeWgKneeBioO3pUFIno9zA85TWW7X7rYUFbgsMWP4xtyqZ%2FWy8l0WvbOIKGgA1%2BSkhXjG0hoDPsr1cmpGI4A6pRVzI29RoS3RV%2F%2FtHqzXmHU3QbVU60m8IdJ4JqBvO8wekq4L%2FXsLMOjqj70GOqUBChEOhcjvOVdRkCu3GWofIJTPbOrtQHupMmy9bAKpOHgT8G7NCikU4PZnDOpEr%2FEVELK4xydIWgawf0HnfxC%2BUNDXy7dN9nk%2FJkoJgl29EQe8WxwaJFn4Dvy2f88ID3jnBi58wf81ag3lCzXN%2B9yMN%2BypwvkAMI0Mo45kJTUzBwIBDRCuQkqBhU8jg%2FqXo2%2FN05DRS9TBZ8sB1EfDCy8ATu4g9PZA&X-Amz-Signature=b5d75e4aa15677f735176007cd87cadb8185869c68a146275dd9164ea1a2bc6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I4AJRWU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF715gtq%2BikCFqC0vK5bpGPSJRCrIvjAtVgMOLQTI3ucAiAt8LOJBqDAiKId%2FlRErcI5z0Tn4CiJHgalwp2deqE80ir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlObAsZOiuSGeHpTIKtwDyzsBpGo5e%2FkdwxetrfLKdZxtxtJXFrxbfDqfAKPe4%2B1EuKKHsfaNPv75%2FRyno%2BIlJDRLd1C1Pslq6tm9a%2Fay8ThBYvwN3a9j8cMLG46N5kjklgfCDziqtFatiuhE7AFt9Tu%2Fn4oq7hT1XQZhqlH3Q%2B%2F1oI8WraGFMl7Xuhp2FU4AGc%2B0cN43A3U8b7ixj%2Fe7pko8YrKPgNdAE3mw0fNQ3GAs%2BZzPhblfNPUyITyl7nLLso8Jz4frYa7PthbC8s%2F3lHofcSr58UgLhEL1ygoyQSuC73ooY1Spp5yki8bLYswPK3l1svl1P1zt5wAXaHL9Ss1s%2B1rBJVKjAPWjJibhc5e4ZyXK37jvnmmeGt8P4dRQVAOb09RrVHgtnOsmf30rfm93laeVn%2B3tLMFu0PMWTDE0IaT0rtYvzQ6twPfK6q3u0pY%2BAU1zALRwWz8LXU3P5ytL5My78pRVf8s%2Bk1j0Kv1OL3Ifch9EHQxzNRLsyrFyvdLtyX6oAfstWRBAoCy%2FwtgrdGKEzfhYFPYk1%2BMr7KgSBDpOLceTmK25usGImLgkScBKfMOPzc5TQV5zUbYHyF%2FLOEURKgUWqDSeFWwDVagjXXvmHyyy%2FdfGsagFWC0WyLC1opmT1OWAJaIw5eqPvQY6pgG%2FZzCtrn3kiFaViVrVUwN2ojPQ%2Bsi3CS%2FDlbKXNRkGq%2BOWbQl7cDB9nSYBt8MdH%2FunAyMrd6a2qqx0itqm2G9gkxBGx4GrkBhvQT6As2mrjI4%2BhRNA%2FQSux8fWGUTfNp5%2FjbboiJFNUQ7%2B7jq0y%2BP8x6U3aOg9nBjsuNtfAiSvZJ%2Fc%2BjyIHXStiPVEnP8vYqbfwVUEDlCWPu84pWIG1eBA6m%2FL2Ru3&X-Amz-Signature=f017b0224ada3c3cb4410e171d18a72bdaa867a63457ae8424a395d0ae49df87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6GBVJ3U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDGTB65MUo9uxCmyWJD0rZXIG9Yb3suh59ayX6T3h0zHAIgeU600JTBAKRCS2Nix9VuJaF0Urneozs%2BV85y6hTbw8cq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDNFWJ9BkeknBboVYHCrcA28lljpz19InhE4oMRYtrnMn77Qia4CS8roiIMYUVMlqFcaf%2BaBOvsOwSfLwfxBa9HHGJnDzPsz6BfeVug11fckhY5T3i7uLlLx4Ouw7GmEYTkYXr5lwNkaW%2FQz4mcswqM2EDHOxzSxH0xPMioWqcV6NSI9k%2FYQCnHSV%2BQUVwe1Cd5RD0R1aJfaHh2Cn0jbSvqiIln11N%2B%2FvJwe%2B%2F772e04ufF5Nn9bODilZcZ7DGBvAp4GgPpOrnLzU2tw6cJZPV6L3wiA1WMMF061g8VsxWvikI66taAKaI%2B4vrAPTkLv%2Fh5ZxGJabWVPePaiNOdu4xtJyVSSMyMrgIVBCrDl%2BU4HRQw%2BUKOEHJFSjK7Lcx0neJc8dl1RsG9BIkbsAR6WF%2B5jDU68O%2FI8BJQJ3kqDI53P%2Fas02V3zE1NFHgt3J%2Bbe7pPnxOYzkIuVCm%2Bq7vV2BmcDrpn4x2j8LoOdHK4G651v%2FaLUrW%2FnVuhJGgZViSWxgIWgyXXKERkVUB%2FikTMRp4SzWzPmLC4LiwmrafmJufFqjqR1WJSz4yGyp4VzGsmhfJJGgfIk%2BZ9FQC7DfSNoqPWksdv1vv5b3nE7B2U6cSp%2F5%2FNlgm0kDVaN1EsPHxgPRsCtp4D%2FKxF4g0QXqMNTqj70GOqUBS5ye3t1qZkcYmDpJmyoM9UDhWeQv0xnv5zRvr%2BjHJAwR4qrAMtTQpklV3ctzOOCk7f2fwQqkS06Nftk7UIUE%2FGMnLwmc97VOcOPIzRCMZoFgijTJoFFtNC3mhonV44ztkUgLpzHO3%2FsiPERUnge0ZKxqlh4NrrVBAi8WHD2xQ9kPZv30wgAXXvvNsETVa%2BH6ZGqnKiIUQpDXk7lM3kufPr25tHYe&X-Amz-Signature=520626fa3f3070db6d1e6be974afeeea21150e0336a997fd815845d50da9f638&X-Amz-SignedHeaders=host&x-id=GetObject)
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