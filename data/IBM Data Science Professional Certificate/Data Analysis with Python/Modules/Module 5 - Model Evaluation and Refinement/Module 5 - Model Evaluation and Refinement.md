

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=51a7d5c641e5aeaedac3a1559c8afe9463eb008b81ae9bbb0e86c016373cb3b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=b758237b7b2cd937cd3d3893c98507e4c8e401b1d192ec7cd62b9c0ba39aea08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=dcf10e455b58e678c52b84e2d678fd50421d975e9688c9005d428b0bba6f6cac&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=e0af3fd24615d7842d9bbeac95480eed2d1f5a8f13084738d2080bf91140e7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=60ee9c597039638e3809f53b569668761f3e0efac13405a17316f79651ee4992&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=5d883eaa896d28aeb5b4cb588963bb64af85fd57f950bd0987a7b201a68cf2b7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=28c01f1d4d6d453708dc5d816ff8dfe3f31faedd0089207b2290c3b1f36959f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=b0d8e489363927254ba668271d25a66df79f52430dd9c815ee4f98767c08c3c0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=d30623303daf52abd24c7f126947c9bc3a7a888633f86473bb326ca5ea902197&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3MXUCL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEM1RBVxp0sshtAHaOPDaJ8y6b%2BnQRh1ZEXn1c6b7edTAiBVYR%2BSoRmsHpNOdd6XOiXCCqaYIqXQuakypz50gDyaaSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNBCZXJjrEy2dYd10KtwDo2TyOjmfTqpzRENbYrsgdF0RWOzOuCHsn%2FqjpnBU0VQ1kpA%2Ft8FvZDypKYHXZQSyVFYATK%2BB34JKEosIYEWcguN%2Fg07n2IphZqHoNoRT0PiOzMgAacWXQq%2BVllulGHaKPKwxufVgTPBaHy8mS12JyLtduL42ZB%2FA%2FZdCmtyY3RaGTrrgS1P0RupIrPot8BASK0a5PmoJD1T4GI761wOReOR5omhaQpJWHcRPEVETnlnXp7x%2B2%2FgbHYMma%2BPvTIRsYMS9En6kbKjxrBBW45InJ8sP%2Bm8GuH%2Br2cQKmirxcMuFJWyHrtxtJhCqFHvKafYiutSm8SXLjRz4htHGUS6meU6oKj8dkODI9E3Tem8O56Y%2F3YzOEEpGlqWCBo6LynVVg%2BlTy5Gsyh5Qv4Qht8cspzqrOBAcw7IG%2F5M1e%2BCS%2B2R0NiQ3sV69BXJ4MWBptznXkF%2BHd316a20vdDgGY%2BjfBLR1fdFih%2BNVFZn5aalzFwe%2BwQ2egL%2BFaSYPd7GzBjdEbCXHMgN4AmjlJx7543v8CSC%2BI0yYdMV2VKPLazwD1npop4dPvDoTVfMvWStwe4RdXopMXkJuB76HhnkWBal9k605g0ciXdKDms8%2FB5e7LR%2BJUGCVzTNaUOq496sw%2Fo2cvQY6pgEuxBVUZq3nvdxMS2K0%2BYdLI76uKhNky6SAndBXFp5rb%2FCbagHqunbmaTqYJMSxPcxzcE5oR9Sp7XTr%2FpsOH%2ByZqVet%2F9i8PP3oI0Wv2le2D6JGZZ1NCJ7%2Bkx3bBHHXpGCO547%2BMna0MH6W9aHqcnJ14yrlxStQbrG2maPMdNfTrBJGInO10nNxmc%2Fg4YEJcJSQ%2BovantaLuRmyWWy%2BrcYKoozXlBTU&X-Amz-Signature=8686a06186e68426025ba88eb4debc0c7a69ff64c16fad3286ca568737865396&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3MXUCL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEM1RBVxp0sshtAHaOPDaJ8y6b%2BnQRh1ZEXn1c6b7edTAiBVYR%2BSoRmsHpNOdd6XOiXCCqaYIqXQuakypz50gDyaaSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNBCZXJjrEy2dYd10KtwDo2TyOjmfTqpzRENbYrsgdF0RWOzOuCHsn%2FqjpnBU0VQ1kpA%2Ft8FvZDypKYHXZQSyVFYATK%2BB34JKEosIYEWcguN%2Fg07n2IphZqHoNoRT0PiOzMgAacWXQq%2BVllulGHaKPKwxufVgTPBaHy8mS12JyLtduL42ZB%2FA%2FZdCmtyY3RaGTrrgS1P0RupIrPot8BASK0a5PmoJD1T4GI761wOReOR5omhaQpJWHcRPEVETnlnXp7x%2B2%2FgbHYMma%2BPvTIRsYMS9En6kbKjxrBBW45InJ8sP%2Bm8GuH%2Br2cQKmirxcMuFJWyHrtxtJhCqFHvKafYiutSm8SXLjRz4htHGUS6meU6oKj8dkODI9E3Tem8O56Y%2F3YzOEEpGlqWCBo6LynVVg%2BlTy5Gsyh5Qv4Qht8cspzqrOBAcw7IG%2F5M1e%2BCS%2B2R0NiQ3sV69BXJ4MWBptznXkF%2BHd316a20vdDgGY%2BjfBLR1fdFih%2BNVFZn5aalzFwe%2BwQ2egL%2BFaSYPd7GzBjdEbCXHMgN4AmjlJx7543v8CSC%2BI0yYdMV2VKPLazwD1npop4dPvDoTVfMvWStwe4RdXopMXkJuB76HhnkWBal9k605g0ciXdKDms8%2FB5e7LR%2BJUGCVzTNaUOq496sw%2Fo2cvQY6pgEuxBVUZq3nvdxMS2K0%2BYdLI76uKhNky6SAndBXFp5rb%2FCbagHqunbmaTqYJMSxPcxzcE5oR9Sp7XTr%2FpsOH%2ByZqVet%2F9i8PP3oI0Wv2le2D6JGZZ1NCJ7%2Bkx3bBHHXpGCO547%2BMna0MH6W9aHqcnJ14yrlxStQbrG2maPMdNfTrBJGInO10nNxmc%2Fg4YEJcJSQ%2BovantaLuRmyWWy%2BrcYKoozXlBTU&X-Amz-Signature=18ea56ef4bc9f54215ea1ef3b26d491ff75b6fd6ef655d696ff5506242e1396c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3MXUCL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEM1RBVxp0sshtAHaOPDaJ8y6b%2BnQRh1ZEXn1c6b7edTAiBVYR%2BSoRmsHpNOdd6XOiXCCqaYIqXQuakypz50gDyaaSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNBCZXJjrEy2dYd10KtwDo2TyOjmfTqpzRENbYrsgdF0RWOzOuCHsn%2FqjpnBU0VQ1kpA%2Ft8FvZDypKYHXZQSyVFYATK%2BB34JKEosIYEWcguN%2Fg07n2IphZqHoNoRT0PiOzMgAacWXQq%2BVllulGHaKPKwxufVgTPBaHy8mS12JyLtduL42ZB%2FA%2FZdCmtyY3RaGTrrgS1P0RupIrPot8BASK0a5PmoJD1T4GI761wOReOR5omhaQpJWHcRPEVETnlnXp7x%2B2%2FgbHYMma%2BPvTIRsYMS9En6kbKjxrBBW45InJ8sP%2Bm8GuH%2Br2cQKmirxcMuFJWyHrtxtJhCqFHvKafYiutSm8SXLjRz4htHGUS6meU6oKj8dkODI9E3Tem8O56Y%2F3YzOEEpGlqWCBo6LynVVg%2BlTy5Gsyh5Qv4Qht8cspzqrOBAcw7IG%2F5M1e%2BCS%2B2R0NiQ3sV69BXJ4MWBptznXkF%2BHd316a20vdDgGY%2BjfBLR1fdFih%2BNVFZn5aalzFwe%2BwQ2egL%2BFaSYPd7GzBjdEbCXHMgN4AmjlJx7543v8CSC%2BI0yYdMV2VKPLazwD1npop4dPvDoTVfMvWStwe4RdXopMXkJuB76HhnkWBal9k605g0ciXdKDms8%2FB5e7LR%2BJUGCVzTNaUOq496sw%2Fo2cvQY6pgEuxBVUZq3nvdxMS2K0%2BYdLI76uKhNky6SAndBXFp5rb%2FCbagHqunbmaTqYJMSxPcxzcE5oR9Sp7XTr%2FpsOH%2ByZqVet%2F9i8PP3oI0Wv2le2D6JGZZ1NCJ7%2Bkx3bBHHXpGCO547%2BMna0MH6W9aHqcnJ14yrlxStQbrG2maPMdNfTrBJGInO10nNxmc%2Fg4YEJcJSQ%2BovantaLuRmyWWy%2BrcYKoozXlBTU&X-Amz-Signature=0ed7b89ca9211d260729f2bf727167d7e7daa88947ce54bbdc7d9313e5261ffa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=24301407291cf2c5ec30a6f8e572f8ddf497e7e8ab603ef862538a818355dc8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=01ccf630bd17d718b4d489324d4abc1aea34aa72755453cccaf054d4ee9c14e0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=3af3b361cac6a2dd92c88bba507e5fe6f9a948d0685361aa35d353a3f37988ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=7662b6ebc8dd1f546a502356a553593c2103e4bdad73693acef3b11d681d73d0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=eb5a957bc0b96b423e2e1680ee9e5707095efc43d9c46364a340e10c253d3846&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGGWDT6O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCLQusJX4G3vVvVt0EA%2FMqGuEL5Io7f%2F0FsxEubdz2n6AIgQ1U5UpudsvCrmCUtQLFRmh1BP%2BnGkILnLNGZTAi78RQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnixNT2L%2BHm9njNfSrcAyPt%2B6UCZwCN9E1T5GOhQ8CrYqo3LtSfSYHmmXD4LnAmck1FMjWn2DI5rjECEgvKFjpFFi3AuQx%2BlNzwUeMqA%2BEUdvQzB8R5Sah9UepmGwIH1beriidA1hIjlaoNKIu97jlJLBVm5VYRdDdvshAIejUyGR6OXxo0HbpwI%2Fvj1tAWNvK5BtcrF5x%2Bq5vOwtBNUIwiusXeC4voa1PhzhgDD3JaynrbYXvmO%2B9kdPaLBOAdQyRc7uRevEJIsGTQBuISctjebKaCJCTKTfitOsP5eCzGz6hi1NlJO%2FBWVj1z%2BFDv4F4eA%2FhCOP%2BNFriOYXT8AasSczb9GafBPYHugqibZinWLU1rnrlgtaw9OPGqggH2MUsLr%2B4rcEcIWUM%2Fiegc9kHZ4%2Fouhm5sv2Z4UCjwdUj8M2%2Fc%2B%2Fv8hUQuKexuNCZYoHjBh4kOVhOoebd7NLgSdgQ0cAd%2Ft1YYqJwNAiUy9AJQ1tACqdJ0%2F10AkR76i0pmljUpPBAAss1t7ETd%2FQTiRxT5CGIMQrnEDDMvoZLIjVjsWk56JACbKX9Vih4qIZbd9EzSVJZYhsEa2lesBXnH2UG44mVTXwcAYYCEvZDxr8nB5XUBQjWrKjoSINNdIERRqA%2Fy73nME29XAoObMIuOnL0GOqUBMOEdS3KZPW02dCLl%2BSImkByUiRQSnV2vT5RJmsQfDKV2kbHg9Ymh%2BUUFZ%2FKgSTBZ8Tknvg138Ske%2FDSVjSeH4myr3hp2D%2FntsRaeqv2tpjqQhj9KwY%2F7817NgFUqEaCqiDKMesLsrL6txfGPJjO4SJlaCBGQdFJ%2BQLTseSjJFHy%2FiLDul4r8BR0kw6EYpgax135EACuw88zzHD8AdxS8h%2F56JpUy&X-Amz-Signature=a7397770dec490b40ccfeda56cd72273e44d4ff6b4f89e23f69b37c9f04faa13&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VZNYIQH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIDgfHEgYf8QIg%2FA8di6YYSq3WUEMWUSIbj7YLnyR0%2B7DAiAQFC%2BCHq6sP23x3CHeXN15qweHhTVVGYuAHiNEn0%2FRvSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPJanM66uUfAWP%2B2yKtwDNPEkoDjwFacg1m3bE5MXHw0svhw9GtEsILSErl8h7RH4eMfUxEGXfS2kAUB24fgHMkw2I5qIXht6btb32Grw2KYHZi4kwipBC%2FKRe1FRzm5ix%2B6kPeloXU%2Bex0gXm7h4dRuHtIK8134A1z0jsmftIA2es0PrxJh90uXbr0x8Q57MX8yCoCnvw2cEVrcwlI0WE8m9YWQi667H9O6h74EwbALWX7DJytyd09QnuUo5UudeA4JqrYasrOnCWCaNqlxj55ozgCw3vGkxAhDrqCUfnEMKyEY6oPnH%2FuYFmD0KMr79W3vZ94VbyZtRsiyqhlwIK7TA08n7SyNSKtzgPogrFGrOczFgUMbR1rturKFfTNdnA5EFKTDT%2Fp86Uj5trZaPMm7Zi7i8G3qJUjSOkl3GWV1v8GGktGkUzoT5yrqAl%2FgLsbGwQvHdwKPv8tOSz2ZjKjZ6cfWpuH661UGLLzhaqautDvkGkgUv8FesxSJPGqLtcUXDIRvRvH1AxELZhIkhklv3KpPl3qtD7obQf9aawEtxNPIbTPcvC53j2M5fIUB26E9dJrnLHzEUBd%2Fj%2FmJM8KU%2BykAc6WP5G1LafgBE3f%2Fk2TxDgJmSWIorzMqxJpuksKK75LGJjxhqUOww246cvQY6pgEiVGV%2B7mEE%2Bq3n71mJ2WnlFFhBwxqZITafBXC4yHKyUwzHvFMstb6gG%2FfchpnBnX4PQOvSJhtCzqjL9YpmjjIpPTL5ujzVczqIux9z6hvIE2Enw2jORmphKbJ1vqCchJaAIX%2BzS1eTMNFFqUk%2F8W53gcsw1l%2FL%2BsWQagp1gESFdyDHkkKga%2BXNNzWcsv7fBmbfuJPlqpg5oJ0HLV8bR%2FfcTnt6rW7n&X-Amz-Signature=0488183f3f16085f874a61bd20bc6b167d76360bca3a59e7097077fee121d4c8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VZNYIQH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIDgfHEgYf8QIg%2FA8di6YYSq3WUEMWUSIbj7YLnyR0%2B7DAiAQFC%2BCHq6sP23x3CHeXN15qweHhTVVGYuAHiNEn0%2FRvSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPJanM66uUfAWP%2B2yKtwDNPEkoDjwFacg1m3bE5MXHw0svhw9GtEsILSErl8h7RH4eMfUxEGXfS2kAUB24fgHMkw2I5qIXht6btb32Grw2KYHZi4kwipBC%2FKRe1FRzm5ix%2B6kPeloXU%2Bex0gXm7h4dRuHtIK8134A1z0jsmftIA2es0PrxJh90uXbr0x8Q57MX8yCoCnvw2cEVrcwlI0WE8m9YWQi667H9O6h74EwbALWX7DJytyd09QnuUo5UudeA4JqrYasrOnCWCaNqlxj55ozgCw3vGkxAhDrqCUfnEMKyEY6oPnH%2FuYFmD0KMr79W3vZ94VbyZtRsiyqhlwIK7TA08n7SyNSKtzgPogrFGrOczFgUMbR1rturKFfTNdnA5EFKTDT%2Fp86Uj5trZaPMm7Zi7i8G3qJUjSOkl3GWV1v8GGktGkUzoT5yrqAl%2FgLsbGwQvHdwKPv8tOSz2ZjKjZ6cfWpuH661UGLLzhaqautDvkGkgUv8FesxSJPGqLtcUXDIRvRvH1AxELZhIkhklv3KpPl3qtD7obQf9aawEtxNPIbTPcvC53j2M5fIUB26E9dJrnLHzEUBd%2Fj%2FmJM8KU%2BykAc6WP5G1LafgBE3f%2Fk2TxDgJmSWIorzMqxJpuksKK75LGJjxhqUOww246cvQY6pgEiVGV%2B7mEE%2Bq3n71mJ2WnlFFhBwxqZITafBXC4yHKyUwzHvFMstb6gG%2FfchpnBnX4PQOvSJhtCzqjL9YpmjjIpPTL5ujzVczqIux9z6hvIE2Enw2jORmphKbJ1vqCchJaAIX%2BzS1eTMNFFqUk%2F8W53gcsw1l%2FL%2BsWQagp1gESFdyDHkkKga%2BXNNzWcsv7fBmbfuJPlqpg5oJ0HLV8bR%2FfcTnt6rW7n&X-Amz-Signature=ef0cf7a6b61142c0e610195b01d5c43f5dd6e7dbe4eb12a04bf85fa895d944fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFERXFFQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQC2zoNtNVl66lKgGC8ehvjAciGfTm5Mu7MhOCb1ygl8IwIhAPYZa3RGyRE8fZ8Hq9IAmbk1VjBM1IcaPI4pGu6MLx68KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwW8dd8jFCjNWW56zgq3AMFcSXPkngIVDDOsJKs25jQfJUKy%2FXC1NhsGGpG8uRZAbyWmBNOv9UVgzJZWMTS49eVnWShsrhWCJO8sTwLqn%2FHg0j2Av87K%2Fzac%2Bj2O7bMofZ7H2%2FkHWHYfav1OR42o2E54j4uad4xRtO4MUbk9XmDBOTLICoCC%2B3eFzCY37R9lRU2fMck5kZrdFecmMDq9bCs5OumWBFOkSgr7y%2F59%2BsB4EHaxeMmuMvBk9QZ%2Bt0JtSx%2BXm1Mu6EOEunouhW8E94ar%2F6iJeTmQkpT8CS9XhnSjN0mVzYdq%2FiPYNkces2lEothFLIb%2FWnOXRGwkxZ6fKINAfHesa1ah0OyP66hhNP0O%2F5O76SEwZ4MsE%2B00DzG2iEwzOrdqjFTUnOBXByma%2BDMs5fl1GSzXUm2sxXY4sFhEgUmcP5unWmAdlc0gQWBM5cf%2BZcjzL2ZrDlSDIaBGeKjrK%2B0hoe79JS2L%2FDJUfzUSlsW6psbbs7058Ksm0nc9S9FkH1JqUM%2FekgqORntvobm0QM7tpPK5v8farBRCVzCOdlzW35o9hGSrsGkSogTx%2BYwieFn3bk3RCbK3shP53thvlCTQn8H27dkhr5etOlvtQFBY9obh6hZi5Y73nT2ABn6DlIHqqQnNvE6zTDKtZy9BjqkAT4poT9ZQSW1brFRZD2H9hFolrtVspiY9HLPVRw08yiKKz0X74Yv%2FBw5dNLqm%2F9hHbGx%2FybKO50b%2BzXxA7MkkTYZuB1YpkHrhfCz69UzBD%2FNMyktLjz2WDkFLUmNebeHSiWsCTZfLmlHivb3naDLI%2FFbT9goMdktyM8pQrMLoyZWLk1XMV2l9yLy6AhzRIVbPFnFFx8tul%2FO4yMe73ksyDgnsnY%2B&X-Amz-Signature=fb566dcce8a6a7d7f952408ba3aa0acab7b1ba456d23660710ebb2787f47a01c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=4b94ab9eeceefbc5d7f48c753362ee2ffe9a2d7344fe77cb96a2060ba9abd1d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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