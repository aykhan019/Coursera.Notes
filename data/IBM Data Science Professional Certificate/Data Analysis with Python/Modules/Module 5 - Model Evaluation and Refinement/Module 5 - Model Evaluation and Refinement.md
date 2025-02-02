

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=c3b7bad81e8afdd7bb3a0a786df861a359c86cc2aaf3c54702bc3e2702e3cb8a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=7c9933ed219c674ba0e46a99f6f231f390003905bc985e839b0f81c6837e6925&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=3076c8d2f896445daafcfa69a8f11c7eef1c9b05d5e8ad0d9726930015b8fe27&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=b31247cb3a293566c999ae585f33146240e84262e92dca704395df60f088d528&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=4d150061c6fa32cd3ec94c219245427181e39082c17c648bd3830935fe896749&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=5a3b158ca38caf19473f85aa6d8e00463129a8c164d8493183b66b1325859eac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=e18dc8d9f1a004dd716b139b4b1a7525b05c50e8628dc82b35ef633fbfad218e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=e5877b38792588d7b4143ba8dc1fb4c7b19bddcca44804947f421ba97efcba2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=9284dd78de8bb917825561111c22d70a37f062a6324bebf3443f37588e844386&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNCTIWM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEDtsbIsDyFDZAFrwlYNIDAQVrJQE33ZlH3ZNvp6w0VsAiEA%2BmCCAFBAZ99IAE5n8k01Pv67QDMepXtXmNxiaH6hEOsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO022DijhZmsNNyd3SrcA5opCxumTlkhNmqdFwZeHj6cClv2aruV9Iq%2FUMQMANBS0Gn7BCyNtac9Jrn9WQ2l4Q3HCnpaadUGfH%2FDvklTFYgtUHRif3VD3YomenPQBnkHEqB3BFZrCks9FWhTZC0jIyr%2FfbmNWdmfF4%2BNLNeDBtjr%2B4uQDj%2F4a3LK%2BWLLaa%2BI2ogAcNOu527QCMXXMLs9Nb1WtjeqZ8Nwsm%2FWCjiNNTF2W43wKfHJK3MIThq8bR0KtQML2RER4iC9UiOMJ3B0jYLrotZtFTC%2Bol8QoGRxS2svn9rUT8TbbPzukiSUdVRObbtcQ3JgUbhLmCB5QUAhNsZElKSWBXxl1V2%2BKMxkrUABCYT59S%2BozMYbd5AiTg7pqLDkZ8CUp3KwaWtMf8l5gwvEbL9ZltrrPCTb2Zt550TozXgzLOnFGeHgZ8r1lWDbYBPnrdYjaiB86412OQL4XzGTU0J1O%2FBMkgyVF3eGjbd9xDAAXryunAajJ0cazQ7%2Be4BDtgopDBkBkvrsXOfuEGoSfHrAyZB1DNtXLguqnAZPvpgYLuZE92lBVASTyeCs9cZglIIonx0eC7iYYcZY0BGX8IzYqms%2FGfKB7rMYwWqpLWbaIf7JGMDXkxihMR%2BX4edTGaPIJffz9Q8EMNXn%2FrwGOqUBzHrkq4AjZOO7gQCqO141vmbfC7UO3txwzOXNeYOUaLdft3CYCyhAeld6tFwlN3IcSnsgaS%2FY9m41kRrBah4gePaOqSS0xmAoJS3jZ3%2Fv54edSLFh%2FaXB4y%2FQGAY%2FydDAzwa17wTsA3AjoBjZXA32So6TWI1hEoXGr0E%2F9sgQT9NcF8sWjpkZt204W%2B5vcowFbYAHky0qCGjzPR4zqgZYC0CHbYFu&X-Amz-Signature=03aaa335e13b2bff305b24e223928c95e64c47c978f3b59db11ae571e02f86b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNCTIWM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEDtsbIsDyFDZAFrwlYNIDAQVrJQE33ZlH3ZNvp6w0VsAiEA%2BmCCAFBAZ99IAE5n8k01Pv67QDMepXtXmNxiaH6hEOsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO022DijhZmsNNyd3SrcA5opCxumTlkhNmqdFwZeHj6cClv2aruV9Iq%2FUMQMANBS0Gn7BCyNtac9Jrn9WQ2l4Q3HCnpaadUGfH%2FDvklTFYgtUHRif3VD3YomenPQBnkHEqB3BFZrCks9FWhTZC0jIyr%2FfbmNWdmfF4%2BNLNeDBtjr%2B4uQDj%2F4a3LK%2BWLLaa%2BI2ogAcNOu527QCMXXMLs9Nb1WtjeqZ8Nwsm%2FWCjiNNTF2W43wKfHJK3MIThq8bR0KtQML2RER4iC9UiOMJ3B0jYLrotZtFTC%2Bol8QoGRxS2svn9rUT8TbbPzukiSUdVRObbtcQ3JgUbhLmCB5QUAhNsZElKSWBXxl1V2%2BKMxkrUABCYT59S%2BozMYbd5AiTg7pqLDkZ8CUp3KwaWtMf8l5gwvEbL9ZltrrPCTb2Zt550TozXgzLOnFGeHgZ8r1lWDbYBPnrdYjaiB86412OQL4XzGTU0J1O%2FBMkgyVF3eGjbd9xDAAXryunAajJ0cazQ7%2Be4BDtgopDBkBkvrsXOfuEGoSfHrAyZB1DNtXLguqnAZPvpgYLuZE92lBVASTyeCs9cZglIIonx0eC7iYYcZY0BGX8IzYqms%2FGfKB7rMYwWqpLWbaIf7JGMDXkxihMR%2BX4edTGaPIJffz9Q8EMNXn%2FrwGOqUBzHrkq4AjZOO7gQCqO141vmbfC7UO3txwzOXNeYOUaLdft3CYCyhAeld6tFwlN3IcSnsgaS%2FY9m41kRrBah4gePaOqSS0xmAoJS3jZ3%2Fv54edSLFh%2FaXB4y%2FQGAY%2FydDAzwa17wTsA3AjoBjZXA32So6TWI1hEoXGr0E%2F9sgQT9NcF8sWjpkZt204W%2B5vcowFbYAHky0qCGjzPR4zqgZYC0CHbYFu&X-Amz-Signature=204d0e31e2d39ce5359868e1e95dabf1b1be0e409fdcf100ad9ed2643354cc6e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNCTIWM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEDtsbIsDyFDZAFrwlYNIDAQVrJQE33ZlH3ZNvp6w0VsAiEA%2BmCCAFBAZ99IAE5n8k01Pv67QDMepXtXmNxiaH6hEOsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO022DijhZmsNNyd3SrcA5opCxumTlkhNmqdFwZeHj6cClv2aruV9Iq%2FUMQMANBS0Gn7BCyNtac9Jrn9WQ2l4Q3HCnpaadUGfH%2FDvklTFYgtUHRif3VD3YomenPQBnkHEqB3BFZrCks9FWhTZC0jIyr%2FfbmNWdmfF4%2BNLNeDBtjr%2B4uQDj%2F4a3LK%2BWLLaa%2BI2ogAcNOu527QCMXXMLs9Nb1WtjeqZ8Nwsm%2FWCjiNNTF2W43wKfHJK3MIThq8bR0KtQML2RER4iC9UiOMJ3B0jYLrotZtFTC%2Bol8QoGRxS2svn9rUT8TbbPzukiSUdVRObbtcQ3JgUbhLmCB5QUAhNsZElKSWBXxl1V2%2BKMxkrUABCYT59S%2BozMYbd5AiTg7pqLDkZ8CUp3KwaWtMf8l5gwvEbL9ZltrrPCTb2Zt550TozXgzLOnFGeHgZ8r1lWDbYBPnrdYjaiB86412OQL4XzGTU0J1O%2FBMkgyVF3eGjbd9xDAAXryunAajJ0cazQ7%2Be4BDtgopDBkBkvrsXOfuEGoSfHrAyZB1DNtXLguqnAZPvpgYLuZE92lBVASTyeCs9cZglIIonx0eC7iYYcZY0BGX8IzYqms%2FGfKB7rMYwWqpLWbaIf7JGMDXkxihMR%2BX4edTGaPIJffz9Q8EMNXn%2FrwGOqUBzHrkq4AjZOO7gQCqO141vmbfC7UO3txwzOXNeYOUaLdft3CYCyhAeld6tFwlN3IcSnsgaS%2FY9m41kRrBah4gePaOqSS0xmAoJS3jZ3%2Fv54edSLFh%2FaXB4y%2FQGAY%2FydDAzwa17wTsA3AjoBjZXA32So6TWI1hEoXGr0E%2F9sgQT9NcF8sWjpkZt204W%2B5vcowFbYAHky0qCGjzPR4zqgZYC0CHbYFu&X-Amz-Signature=8876691629c7651356eb0bb2d0163081ec21d8794c3986cbcb38231e9a994b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=a18dd1680868072a863628814d377c1667e063609df4c5523e863b0216022d42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=9834829044675008ad8e4ec69f79570c5d27b03769b1c8c442448f9f3e88bb20&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=8131f9a646a3cee5e1646bb4b037be0fbf8b4352036e944e567ea75f69cdcbc2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=b35bc33979ab0c40bd4675b45ffe23c8b93d46c35d0f0a050bb74d104a404eed&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=4273aed37332298df79c065b3eb42abbe145aabca1111b400fbaeaceb6111839&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGXKMT4Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCS31eoQ2UUGdz2EgluDnuAnK2FOeUCo10rNX1zjKasewIgWDQzkuVJSFeetnZeE00M5h8w42EWwh5j%2F6Ui7voutDgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAqUJBc2UBEZAaqL%2ByrcA8XAYWmIWdDqSBv%2F5QEfosB83VBpw2xZIKNJx6yefJ99t3dHiZiw93n%2Fcy4mBoD2Gkd5OBrj1asmdHdIqf8g40T%2FEnros4ljHXctC7T1e4ZDA1BreaNa%2B7awBfcIVmMuKfvIkgzIfpl3h%2BVbuz6O6PKA8QsmooZXEFyVQM7LHRbE5P5RIr7WPNo1IXIwe8ekppynNM4l8gh4zqTRTyUcxemh57kk8tI5muVngl2Uon7BZ3RmuauFDDZ9PHCYt1RbmkyCx1%2FvUzTArUy4V7jE5mVQmVYdU7ry0kz3AtT6MvMeBsL9wdxv1v9Jr3VbPf4WJcl1qy5IXC%2BCBoyUCyp03bwLj03pOjkzJ5Oj2bT50aBaNMwtt3uSNrDEvujw%2BSyJF0hjwAyaF1nQZ7ymRmjW0hOxRb%2BbcfVNfio5r1w7pvhfC0ZWUnY23VmOacckV%2F0AP3SKEdp1LX3NcT4rUydQxYbfeIKQ6ewK%2B2II%2FcSUVqQUI0r7I1n4%2FEb8Jqlk9dbrrNnJxarWHcin6%2BRder2jmKVHXIa0cUf6V0Lhs55bwYCIqUa6UzX6Q55g8b1RjprlhHF1LDeq%2Bo4ceu6YUWScqqILjBtt3hpD680FmMcGYevFnbv3IQaIrjexoxWGMILd%2FrwGOqUBOeGMuhGTzu3mx5g3t%2BClhlprPYdVQM%2FJu6er%2FAjtY9GdGwZk0FDBXp0rr3CSGIhF8xlRv8mPvvKIggvsqI3QYagntaAqAbcodiDMLRkPF0a7asth59NqtJHUukdPHs5iuf4pa53sDIjZMyp%2BBlY9ABJgM0CmY0k4DOXlv%2BX%2BnFYIxO9BhckQ4tg1OD1fGqwPBSgSvDVt8gtcbnyisko3jGTC2V1k&X-Amz-Signature=d46fe1e39b0231c7706d7acf5de24441b4c551846d143cdfe5eee947ad48b628&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635UGOAVU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDx%2F7RE10W7KlRMULFj4V1E3CyZIk7JxZmd8DWhJHVYUAiAVLaio4nuowFEXA2V2mlLz%2FZqvBlp%2BIgD5bCy1G%2BQF9SqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXSOTVgiWMjLV5G2mKtwDNiBMJCTCRERUS%2Br3w1UwvcAMgmp4ON35lI1gPKbZZw8mWeyTznAAHMJJKMVuQiGaZ5CsW%2F%2Ffc6qTad2nvISchQsTFdjXcikF0LdQiwz%2Bmw3mU8IUqMJBqNHrk3U9%2Bfu1gFU0Wvmqp2a4e%2Fs3%2BYVxMMgqsImcdNELyJRZ%2B3X5zodyBEyTps7Sfgx2pOG9FIZcyQFm9WA5C87nTX6%2BesB324KritJVwPmWjZZBlNUS%2Fjqi2VT9uMWY%2F8VX29IzP8o5mjuat2ySrnKwtRsGfAx1hw4R0QlVlHU7W4Sg4IecTZA4hmg5ymFwLFAvaGMsrWW0%2B65ZAsJYyL9HU2k1bWhxpfLJVBiuCDoc9GPEBIoOpgHBqY%2BOmNdz6GctcQfHziDkNnsk0N1AUJH1lTNCXAn%2BG87xBB0wodfcFJRpQo700Y2DMTDXvEbvZ5wCYUPVd%2BPeTd29r3zl2zO%2FEwuhHI72tSCrn1B0mQDYz6Te%2Bhxoj9ujRC3aePskZ57jXuTYZcHnIAl2cRhdepgfUJf%2B1naqr1OHBFEsMwGCEfN%2BoWdqiUQxRvo96dQ8U%2FVLt32jSCnmUbbOvBTR9GgOvcwXpej2A2%2B30W%2B1aqFbkXtlfmHzsA9yjUi3tzvOXLHv0rEwktP%2BvAY6pgFGsD1qaMTNxkhk8PoJe70MT9M65ekZ6bzjYrXzl72OHiUEQUDzos%2Bq9c%2B9Urmeg6%2BJwPFQW20tCrT9jWfqS9qlZk%2BB3rSu0pCgrkUW2lZRIvj4iIouu8JntqL9aExu6uZZhJ%2B8upORYFUHOXQeF7TKIz1%2BKfMD2ajUHyCBlKfmi%2B%2BolwvE2GKrkqk%2BjpcdBwMjqCLtmOJ7%2B4JI%2F2kQiwTkaf%2F77Kbs&X-Amz-Signature=57f4db421607248f43235ab737e4dbe5157f80ad1c548164df3e0545d78bfaff&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635UGOAVU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDx%2F7RE10W7KlRMULFj4V1E3CyZIk7JxZmd8DWhJHVYUAiAVLaio4nuowFEXA2V2mlLz%2FZqvBlp%2BIgD5bCy1G%2BQF9SqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXSOTVgiWMjLV5G2mKtwDNiBMJCTCRERUS%2Br3w1UwvcAMgmp4ON35lI1gPKbZZw8mWeyTznAAHMJJKMVuQiGaZ5CsW%2F%2Ffc6qTad2nvISchQsTFdjXcikF0LdQiwz%2Bmw3mU8IUqMJBqNHrk3U9%2Bfu1gFU0Wvmqp2a4e%2Fs3%2BYVxMMgqsImcdNELyJRZ%2B3X5zodyBEyTps7Sfgx2pOG9FIZcyQFm9WA5C87nTX6%2BesB324KritJVwPmWjZZBlNUS%2Fjqi2VT9uMWY%2F8VX29IzP8o5mjuat2ySrnKwtRsGfAx1hw4R0QlVlHU7W4Sg4IecTZA4hmg5ymFwLFAvaGMsrWW0%2B65ZAsJYyL9HU2k1bWhxpfLJVBiuCDoc9GPEBIoOpgHBqY%2BOmNdz6GctcQfHziDkNnsk0N1AUJH1lTNCXAn%2BG87xBB0wodfcFJRpQo700Y2DMTDXvEbvZ5wCYUPVd%2BPeTd29r3zl2zO%2FEwuhHI72tSCrn1B0mQDYz6Te%2Bhxoj9ujRC3aePskZ57jXuTYZcHnIAl2cRhdepgfUJf%2B1naqr1OHBFEsMwGCEfN%2BoWdqiUQxRvo96dQ8U%2FVLt32jSCnmUbbOvBTR9GgOvcwXpej2A2%2B30W%2B1aqFbkXtlfmHzsA9yjUi3tzvOXLHv0rEwktP%2BvAY6pgFGsD1qaMTNxkhk8PoJe70MT9M65ekZ6bzjYrXzl72OHiUEQUDzos%2Bq9c%2B9Urmeg6%2BJwPFQW20tCrT9jWfqS9qlZk%2BB3rSu0pCgrkUW2lZRIvj4iIouu8JntqL9aExu6uZZhJ%2B8upORYFUHOXQeF7TKIz1%2BKfMD2ajUHyCBlKfmi%2B%2BolwvE2GKrkqk%2BjpcdBwMjqCLtmOJ7%2B4JI%2F2kQiwTkaf%2F77Kbs&X-Amz-Signature=d4e486328645d73da36a020e6a07ffbf15664ad9318178ef02c94c0e375d5a08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PSC7MBL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkV7TEX1QOVpzBdJNiwNwQjfBr1somLrp8%2FsRi2WJlvQIhANAjznIS9%2B9z5LC9KKLJ1mho2vCjeVEzRDXgZ5RqNXKVKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxMAdH8IHYIFJQerMq3ANiTfmcM1ggn8%2F8ZMX2AeKDxUbxBpCpcS6z0hFzQHRLHbl0uiD%2B1n9n7suzP96949KPVA3BiEFIl8w3RG90USR7vUQtK8UrRoDg%2FnPs28mDrWypnHLzhwIwjGf8p1eX31ix57QTYLGcRfybxLV%2BS2RxBGQ5pMWoz%2FcGoNR5VtRk%2Fc8iNO4URcgMOSnJT3m%2BbROXAm%2Fd1w70p%2BI161qKMqMRgYSkR7nGgK9i%2FdW2mlw3tH9CIta84zNo0hTJ1k3lw8YVcBhDg5a29z9m2WhFxj%2FkrEmL0vEjwKASIAvOCmA4RXFJBcwrB7zI%2BDwGpkcazFZMrBqn9k5q2eEAuh1%2BNMK1UyfBX5GGhXu3dizTXtBXVTH6epZVtq%2FeY%2FDAJsOqnk%2FpcpBV51SwTeK6X9JUYkfmbXmj2sW5BbQK5yASBZLXiak0YpbkDEgGm%2BZgk33Fow8Ipbr5W0HePx%2Bo07rI2nQiWG0VjPY9zvprfBEWW9qa8FCpHfXuoH3zQOolq%2FbpZj0BznYpAF7sMNNqLq%2B0RTywL4DVmpU75NBHnPPZxlBOjFqv%2FIRKVVmWnYoOO9FAewk6sdE3Ul0%2Bbt41VbkzINzNDNYAmaBZV1wgWJq2DV9KPjeyMPEpsl8kErFMXzD%2B2%2F68BjqkAax0dH%2BZYxSzujTa2KPIOfEGqRgs%2BxPKQy7QLEJSaUcI7xkxcnzM%2BDOorJ1%2FnwidDFhYXfNOz81hYM%2B66QEJ%2BvBxfGX7uS2%2Bidx0XEK96FXYmgV%2FXoC1%2BwJmsk0ac91kwtbVX1Mkj8PzzkRVVbecFXCeGPN9ipgSxU7PhrzD7vGPqMyQp8XtrvFbdYZCwF3b3VKwy1ejnUnbBriUDEVWm5ARqENb&X-Amz-Signature=68c1a87afbccec5e6578e1c0a8967fad2bc020ad1f874c5e97bcaf5ad6d7f9de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EBQ43X3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQdTtB48YQhz%2FLsrrry2C9UytAdkW0k7Yw3%2B1CRzaF5wIgaLc7dbz%2B9pAk3Pk9zZx4vRhQulIhtP%2Fc5ivDucI5lpMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ6zU9DyNvseHPxLaSrcAzYRLcGbjtXZHO%2FFC74LxRxlwfUkUZRGDk%2FI%2FUj4zO6rZJ1xYw1pDLcrQntzPher0YSdATPidIk9Eg524F9WuWl5KcfZKBPPd813TuG%2BAMOJr457eHa2Ahx2If%2F6X68RKxT2MU5ybHWRYXVbWZeasdcYrygukAINnyyAXd1rDtXfxOOrAQPFqv6z3cBTqLc3WtOvFi4I0SSPux%2FOV34wJV0xomfCQB3J4cpH1lq0t6OoTDG32Xb9pYtS0Zc2vb873mp0JhgmCDrZxA69hwxBMeL0jX58Lg8iow5pxB2%2BwfmOpwFTlnxcyo%2FjZ71MGRXRWwTglKhVQs8fedpqG1Jj8nbRUcEscsVoTuJ%2BgmtHOxQY5x7LEhd5Czb2EczEx1n5D%2BeWDvzwww8qXgfhJjUz3pz%2FjAhqMSH2wHIL1NEmrWA868cVo4LkuyodMbkW%2B4OJRTnNFS5%2FVPMzQYNRtA%2BP3aXEGaP63tXfMZdg%2FvuxJ%2FHbkYTmHbxZPFtMkXxfYtb8UHZvqJlaoErzBNuRqCfGIAA9N6uAQKxmhEk%2FY%2BL4ieIZT7lGZHZvJCP7b8aGhUEFyXkoVTHMvk8lwF6iIBCr153si1ZCemAm99WLLANHat4PIanEHFhhWR32GX6OMOPh%2FrwGOqUB6tngh%2Fvesd0yHGq5ub%2BwnrIgaUXL7v0seiB5jBOTnQCfvostKu8ejBTLspbwFlmcZ3%2BnTYA1CQDgorD7WRUacgXUQrssCZWdhp8bALUKx0oVRRQvKlaJB1zHtvud1Z%2FA%2BsYrnBu21Os2shtko8stvR%2FFVPZ9g9Q4FX7nReygGwGJa3NC%2BLPL4rbdnPW7yxrj%2Fh%2F36NdrSt%2BGzJ6YU3H9mH9YOtah&X-Amz-Signature=55f060ecbf6b526793a5763539e9658df4e9aad55d71f278c51cfc78ec64bebc&X-Amz-SignedHeaders=host&x-id=GetObject)
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