

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=4a26d045ad91ba9a3007344a251ab055409f0a9a5068d33bbd8bda0f2f1b5e80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=815e657a297b17ba40ec4b01632a528f3baf1dcdbd843b53939c62ac618699b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=246eb4b72632a3924cdcb65ee91521e4ddd5dabf347441f37f4312c7c7fe375b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=4d420c86f5613883bdeb5c1a086373ee591a3ce319b50800f881940467be10e2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=97503f0eff6db62feed967f35f50e506a497bc294b7c365e1759ceee24b55b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=d610ada1d432a9a0ee732bf67c4dda1c7d038f240c4f8376a4a5a01d0134343d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=b2c2ec4a8fe94505623f246939003246df25309b5b0df075a0621a07a9ab84aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=45daa318fe33b71af01d2c8fc761aecf2a37127a34fcbd8840affe15203ffd01&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=08e9546e84b30659d4a6f5905cdcbb8c7d19b26736ee27f379550a524d55ab00&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3YVQ7WU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQDrZ37n5OG6yuDezgwKdpDxm7SIwB5gW0Jes3rm7hVlZgIhAOqLbdahuLSBYsoYL3cuSqH36Vxg7mk0m4H0sXNYApFUKv8DCG4QABoMNjM3NDIzMTgzODA1IgzFLVxU5zO99JIWMSgq3ANk%2F8g2H8xtwQknyVpwj7UWuiNpdfj6L5HeHaXLZRxSc9LgBJTpfALFFX7cwgq2MtP91FZTACOUt1iJwT0dNibX0cMltjWk6ixpi09Lcn2DpTfdjiolt%2Fv%2BpSiHxuKwh9tdtDvaOLEFf74XolyVwfXSYYxs3aREtfphhUE2hfjcKx5IGu%2BE3u%2FJokbJPhwZJaNSzJy0RfuoG1F%2BZ2b6e98qY5MdvizuOvv%2B4ofQcSDFZpwyKYZQRn%2B6qzWk0bLCAyQiFPDJpvhPWWoZPlEy69T4CBgSJxkIe%2Fy0aLOIDOqxWCwfR20xqJhX8p5ej35VTU1Rwb99PuqXp6nKFI7%2BXDRI7qxfO7LBVCamegGg1fapLWz3bTRnoMtv%2BICQ0wdv%2By3wNnA4AU7gkHxTskZd4RUaVwviHK8h7Rs47kGP2rxIgXQFYlGMZG5xl17X9eH35Rg9p28gUJOv5rq2l9BkSSzNIfrv81hP%2FJE9qyjjGYz4u%2F3kpJx3efNvRZgMvOA%2FW611VRu%2Bg4eb8GMIgsGO73aqcu%2FtsNcoTBOEss0UbBjsWgwMc774J05AvCteMfMHtOH843uL%2BUp7cXSU%2F9WHyLAFuGI3MIa7tJ0eeVu%2BnuPFdkjLFUyUGy9lUnDmHTCFoZa9BjqkATr1onCdHTAroE18Fp73iGXHyqcGUD6tQ8Fq%2BMsGwztSK3cYK5z1UX%2FPFKqV%2BoI1v1Ze5XPRc1mzFksHHLx143NPcXjTKKuzeBoBtfGt8StsvHIdDzByw3CxDME60oueUaMf8AynpVQtnkHyLQTSopWdUktt7FOK7ep8s5A%2BUJUS7uw72ViJqVGt7%2BcelYTu7JuWseTBUxaq7%2F62L57pIhoCMaTk&X-Amz-Signature=be18290872f3b1836e757a4cefad9bd89007a39fe3550494848e03948eaacd07&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3YVQ7WU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQDrZ37n5OG6yuDezgwKdpDxm7SIwB5gW0Jes3rm7hVlZgIhAOqLbdahuLSBYsoYL3cuSqH36Vxg7mk0m4H0sXNYApFUKv8DCG4QABoMNjM3NDIzMTgzODA1IgzFLVxU5zO99JIWMSgq3ANk%2F8g2H8xtwQknyVpwj7UWuiNpdfj6L5HeHaXLZRxSc9LgBJTpfALFFX7cwgq2MtP91FZTACOUt1iJwT0dNibX0cMltjWk6ixpi09Lcn2DpTfdjiolt%2Fv%2BpSiHxuKwh9tdtDvaOLEFf74XolyVwfXSYYxs3aREtfphhUE2hfjcKx5IGu%2BE3u%2FJokbJPhwZJaNSzJy0RfuoG1F%2BZ2b6e98qY5MdvizuOvv%2B4ofQcSDFZpwyKYZQRn%2B6qzWk0bLCAyQiFPDJpvhPWWoZPlEy69T4CBgSJxkIe%2Fy0aLOIDOqxWCwfR20xqJhX8p5ej35VTU1Rwb99PuqXp6nKFI7%2BXDRI7qxfO7LBVCamegGg1fapLWz3bTRnoMtv%2BICQ0wdv%2By3wNnA4AU7gkHxTskZd4RUaVwviHK8h7Rs47kGP2rxIgXQFYlGMZG5xl17X9eH35Rg9p28gUJOv5rq2l9BkSSzNIfrv81hP%2FJE9qyjjGYz4u%2F3kpJx3efNvRZgMvOA%2FW611VRu%2Bg4eb8GMIgsGO73aqcu%2FtsNcoTBOEss0UbBjsWgwMc774J05AvCteMfMHtOH843uL%2BUp7cXSU%2F9WHyLAFuGI3MIa7tJ0eeVu%2BnuPFdkjLFUyUGy9lUnDmHTCFoZa9BjqkATr1onCdHTAroE18Fp73iGXHyqcGUD6tQ8Fq%2BMsGwztSK3cYK5z1UX%2FPFKqV%2BoI1v1Ze5XPRc1mzFksHHLx143NPcXjTKKuzeBoBtfGt8StsvHIdDzByw3CxDME60oueUaMf8AynpVQtnkHyLQTSopWdUktt7FOK7ep8s5A%2BUJUS7uw72ViJqVGt7%2BcelYTu7JuWseTBUxaq7%2F62L57pIhoCMaTk&X-Amz-Signature=65689718f74917d50f754c48551785196af2c5086dcf16c9c229cca4b9f4785a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3YVQ7WU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQDrZ37n5OG6yuDezgwKdpDxm7SIwB5gW0Jes3rm7hVlZgIhAOqLbdahuLSBYsoYL3cuSqH36Vxg7mk0m4H0sXNYApFUKv8DCG4QABoMNjM3NDIzMTgzODA1IgzFLVxU5zO99JIWMSgq3ANk%2F8g2H8xtwQknyVpwj7UWuiNpdfj6L5HeHaXLZRxSc9LgBJTpfALFFX7cwgq2MtP91FZTACOUt1iJwT0dNibX0cMltjWk6ixpi09Lcn2DpTfdjiolt%2Fv%2BpSiHxuKwh9tdtDvaOLEFf74XolyVwfXSYYxs3aREtfphhUE2hfjcKx5IGu%2BE3u%2FJokbJPhwZJaNSzJy0RfuoG1F%2BZ2b6e98qY5MdvizuOvv%2B4ofQcSDFZpwyKYZQRn%2B6qzWk0bLCAyQiFPDJpvhPWWoZPlEy69T4CBgSJxkIe%2Fy0aLOIDOqxWCwfR20xqJhX8p5ej35VTU1Rwb99PuqXp6nKFI7%2BXDRI7qxfO7LBVCamegGg1fapLWz3bTRnoMtv%2BICQ0wdv%2By3wNnA4AU7gkHxTskZd4RUaVwviHK8h7Rs47kGP2rxIgXQFYlGMZG5xl17X9eH35Rg9p28gUJOv5rq2l9BkSSzNIfrv81hP%2FJE9qyjjGYz4u%2F3kpJx3efNvRZgMvOA%2FW611VRu%2Bg4eb8GMIgsGO73aqcu%2FtsNcoTBOEss0UbBjsWgwMc774J05AvCteMfMHtOH843uL%2BUp7cXSU%2F9WHyLAFuGI3MIa7tJ0eeVu%2BnuPFdkjLFUyUGy9lUnDmHTCFoZa9BjqkATr1onCdHTAroE18Fp73iGXHyqcGUD6tQ8Fq%2BMsGwztSK3cYK5z1UX%2FPFKqV%2BoI1v1Ze5XPRc1mzFksHHLx143NPcXjTKKuzeBoBtfGt8StsvHIdDzByw3CxDME60oueUaMf8AynpVQtnkHyLQTSopWdUktt7FOK7ep8s5A%2BUJUS7uw72ViJqVGt7%2BcelYTu7JuWseTBUxaq7%2F62L57pIhoCMaTk&X-Amz-Signature=c135dfb555cfd4fe06439e6a5d30608fb15ba964cde127d97b652b5f14000724&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=1bef39649f6b5863a4d13e9dfa1d77f18228707fd1173913f1959014890d34c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=6bbbfeeaac917bb7af3c618374acb5a50de86a13405708ebefaf5d7460669741&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=d89f8e712215737bb2687ba126a46e1bd378805aedadc8fb6b5d9f9f76f908f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=09e040b9605f67f1ba2aa29fde661bf7677111e9386c867029005ca7517a099b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=4c6b6067c4c83ac1bbdde993da5a25dacc5c1f81d2a9164b41979b5f988e295b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXMFZ5XY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDb7%2BV6f1SF4rznFDcNvIAyxYAWQtcs6hjfc256NKJmEAiEArh0o0yXLrEcBz8T3GfO3IY6sPh8xcHgrJApb3WzVZ9Mq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDO6jUskC91VL2FTKrCrcA%2F4x1giT3rJ46qz0L8ghgCopqpOHwdklUcvDl4CkSBoW5UHJjDNm0DUK3HvSmrj7DUyHYHwfkzGB%2BpSgXQviEZcbI6LQpGxDPo6YhocPVuw2euTfmQeJo85zYXpfr2t7f3VOwaDj9vNTHHU7hfumgJfJvKN7kKh4JQcW2xKith4z7VzA%2FTiUhb9GRpb839DwAMyzQ%2F%2BKc4ZF0tEngKSPiPLQl76Z%2FstMYbLqdSi%2F828mtx96z5SyMlf7XiR1Qt5%2BdlnhVxmOBlVssY%2BHgNET45TWyC3cHHNypmkdgei7CmXZ8y0oqUd1FLL6iz0Q4keOkIOzXQFZZR9nldswGeANo9cxCDERLIKBzVco7KeX47m%2F34c3nNU5WOMLDE0bP6eDMRZsmWKpqrEsyrxNutS3FfFG0UNTx3HouUvJoOLOySkUvey%2Fe7aOcP3zqulZLU7rCV0A9AW1aGrbNhi3l9pnO3jl0XS8ygJIv77dHH8bTn1mgboIe8yTC3l2y7a%2FNGQ0AU9%2FWaiedG273S%2F0%2Bu6NGYX8D3Sz6kbKN9WgBDqVcxxh5mDkU%2FmfAgzr0rqFV85Dcg0VXQMLd28k%2B%2F582PdZwKgEfJC7ebZoaLEMhERQ2rkIW3l7hs5ea4146AfNMJailr0GOqUBYUHQbUuCIiMgvn4GV4UxpcaDnduvxUQ2X6H1sYx%2FG2kCn0hEhmSaTGJwasAs0hRA6WnFE24td3Go2krKMPNyLhFGzp0AcgF88TvETw9GC12OPA4j4D3GJ5gyaqwaMLX41meeS1uP2Z6QLeRQrO3sHU8QVjsly5qRp%2F9SgN8qfomUJKLUENvklthOLuKHIZK%2FpEcJhQoT1YGo3Ucl8aysuHGWAppO&X-Amz-Signature=39c7f82580fb0e2ab1f57a3bbf2bfef3c1a08b60a5a3de81bf4ade85c9d0dc7c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U57W3X4W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIFwNM7yq09%2BvroWhx1jgkkYdy7oMGHbLou8v65syzRxyAiEA4CqZf2Kad2xS6H5Vjg5bLA%2BoeREqzHTRVVpgDfM%2FhEUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDDYUN2iGWHULjlBMoCrcA2hQBAwYW%2FdpOh0wq12TPkc0nTz9odkkILggKH34bcZyv56CzIRH1DpyT3UTvT4N4BqURvnVg%2BKql8xssqMWsinrvdj4m6cHcdEgFU%2B4LB90uBf2nBi5OUWa4If1UHwq1PyFU2LxpUskZjkPr%2B4xXSOSvqD8011FNFjl548zEKrOg6VFKEBthUuw7CqE%2BIJ6pOjLPMLj%2Ft4%2B9u6BXjcP40K6duvY1vq%2FQkQjCq0hEtxb7DoIgMIctZyQ7%2B0QAwW04ZzdOYTyqsmAma5bkxp1LmrvbeSPLFXFD3%2BExAdrCAjoIpneSJ8QES%2BAFHLYZgf4uXqUK%2BJMHr%2FzUzPIpbjcWBAT%2Fz2t6KKLK%2B0tdIGvOEZubfFsbJDW1iAzzwjcWQIcBo9bAe1gdRrVy%2BjV8Rxm5TS7zeFiiXSfirihLxIATtCuVdR95ffdqAKEEj4pykh0swlGD8by6nIWuv4bUGnU1FJPonYKQ9ZOk%2BXixA%2BqUPf7oUdatVQpNer5cK7tasbJJiWtWwEnWPf8kwwFLOnY1IKCnWNtiK2cJ%2F4M%2F%2BUdoD8TkzeMlTnRXiTn0VVWZaGpm%2FjTOMp5KDCPJMRdFs3Y0yybwOd2AapY6%2B5lHyJHBaW0nh8nN5hRKmO5rrwEMOqhlr0GOqUBs6wYz%2B6ZA%2FnlA0t1YU6iWbxVvAVLksr0Upk%2BzLkih5nnkvp%2B8Nvh61tsrkNKfbs%2BUkLGKLNkYyvPIaqMZyKgPagVu10O5haHOGa4ktvrGz2RSfckRqcJw4ToY0%2FN9tNwF%2FLEZi3MYOKruIqm4iCjvS7r%2F4vc7zU3RKn0PJipJZHJJMmSTTAzO8uQo7QT1e9e8wJiVUfxT1bBY5VY5oZw%2FElGdjxm&X-Amz-Signature=5334b301accd94f8a51cdc008bb9b20de8d6f0f627da4aea5fd5ab36c47155aa&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U57W3X4W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIFwNM7yq09%2BvroWhx1jgkkYdy7oMGHbLou8v65syzRxyAiEA4CqZf2Kad2xS6H5Vjg5bLA%2BoeREqzHTRVVpgDfM%2FhEUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDDYUN2iGWHULjlBMoCrcA2hQBAwYW%2FdpOh0wq12TPkc0nTz9odkkILggKH34bcZyv56CzIRH1DpyT3UTvT4N4BqURvnVg%2BKql8xssqMWsinrvdj4m6cHcdEgFU%2B4LB90uBf2nBi5OUWa4If1UHwq1PyFU2LxpUskZjkPr%2B4xXSOSvqD8011FNFjl548zEKrOg6VFKEBthUuw7CqE%2BIJ6pOjLPMLj%2Ft4%2B9u6BXjcP40K6duvY1vq%2FQkQjCq0hEtxb7DoIgMIctZyQ7%2B0QAwW04ZzdOYTyqsmAma5bkxp1LmrvbeSPLFXFD3%2BExAdrCAjoIpneSJ8QES%2BAFHLYZgf4uXqUK%2BJMHr%2FzUzPIpbjcWBAT%2Fz2t6KKLK%2B0tdIGvOEZubfFsbJDW1iAzzwjcWQIcBo9bAe1gdRrVy%2BjV8Rxm5TS7zeFiiXSfirihLxIATtCuVdR95ffdqAKEEj4pykh0swlGD8by6nIWuv4bUGnU1FJPonYKQ9ZOk%2BXixA%2BqUPf7oUdatVQpNer5cK7tasbJJiWtWwEnWPf8kwwFLOnY1IKCnWNtiK2cJ%2F4M%2F%2BUdoD8TkzeMlTnRXiTn0VVWZaGpm%2FjTOMp5KDCPJMRdFs3Y0yybwOd2AapY6%2B5lHyJHBaW0nh8nN5hRKmO5rrwEMOqhlr0GOqUBs6wYz%2B6ZA%2FnlA0t1YU6iWbxVvAVLksr0Upk%2BzLkih5nnkvp%2B8Nvh61tsrkNKfbs%2BUkLGKLNkYyvPIaqMZyKgPagVu10O5haHOGa4ktvrGz2RSfckRqcJw4ToY0%2FN9tNwF%2FLEZi3MYOKruIqm4iCjvS7r%2F4vc7zU3RKn0PJipJZHJJMmSTTAzO8uQo7QT1e9e8wJiVUfxT1bBY5VY5oZw%2FElGdjxm&X-Amz-Signature=0c993c141807b0adcacd3823b40b748bd5ab9cc4ac543718c077fda87d4e2a55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY4ZD6ZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIAdh%2BhSuxFC1%2BjMQILeNZXzt%2FkJs5I8J0OxwAPpOhFrvAiEAuJz7CoFnJddXX49oYzoXB%2BXJNYyTJICam5MgpCYRE5Qq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDGrCJBpXz7kS3sHSESrcA7%2Bah4uAiZeJQwczUCLRbPFjJMkUEbjek8ioEZBtZTGzjI%2FHIGr%2F2OC2SgdIQ6Hc8SVZT8bVV%2BL2h1%2BJQ1A236ZNKl68ccfBH9KyDF5fBYU%2FkwQsa1I33Wq09W0xnBjvb%2Bxt6zsmgodnWwyVI3pVZmL%2B0FeD3jmpb38PJaFws2pPt7oE7AlPh%2FvDfwW9V5t%2BJt%2B%2BBP9tcsLYpvvoeySvnanPhah4kMd5uGHT4rB%2FxHY6cUK%2BYrN9brawtZQ4yBejA5Xux%2FTCz5lwSD1aqPeH2fiCKQljbGQyAYlSEVzOXoUaUSc%2FmJ1VwrA6MKDYIe%2BSlztoPRzVu7pPQceJDOJ8cJDKQyoXjjZivo6x0P9VLfHfm%2BJbpESTDLHo4hefxeqBUEvQPBLiAmlwUGsMUpHAWgeuIr4baiclmVjvWb1lU1Ntz5nE56fm%2BImCC5mOOVYk2i0TVVW%2FVR627HzD84NRx1197yCEOBPx11yP5JR9ELFx2zAl6jzG1l7D%2FXQajKYWtQKItV8qDAViZGmes64M2RExPLvZwViRBVGfer065G8JvPWS0nTzVdYK9FgLXWCZwcrk0l%2FSzwNpeLiX9crgyBu3kQsazVomoP5RPcB94bx%2Frv%2FqLwBZe3F7gpsBMKyhlr0GOqUB9BFGZ61oJOqO80F%2BGO%2BXxkDqC%2FxoYVPnGjWDFIIW0rYF4cZnlLrQN%2BY0fE9XG0%2Fk%2Bq%2BNsSharAB8xZZXtOfqFhiZwHFz%2B1G%2FDuIZFJLLzUoVnLvBgjIqs4%2FYGPI0QKGK8u7HP0fm1n8Sy0XNJXmO7cEfVoRqZxVzEZw18QUNhQy1rFBgoVWE7xdBWkJNNyAVAT%2B4GTT7eN8o7rvmkKyn680M5yJB&X-Amz-Signature=b6a333d78ab5a6db2219e7d0235c506bf17c571d319c82721a8d5c8ba74cbefe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHRABHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIArSjPUZ812WzqPcI%2F0f4zNn%2FK%2Bo%2FIdzzWlv3d7vywjPAiBqYrmvRBamSYyEDzEsn69aaRj9HLy%2FG4UR0jBSx1gTnir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM3pxYKt3c1Ooe5y5kKtwDIEwdAVQmP3nYDKLifqDUJ7zFmQvAIb%2Ba01%2FoBEz7R0vIxaIPRhDSEZzjy0blotwgZPKaOF5jfUPMP0x%2BqmMadvajQQvuCWkX7yuK7kePuDNy5Hhldfsh3lEO%2B4aOEKALHkKiE2pKwpnSDaGHZyAtALKnx8r1Asa5a02ZcAQLclHpUZrKVRNHv9ZLPWv%2FHroILRnReZGQRqv%2BITsj4ncuszAv6bp3STIAYKotLtdrww4ePZq%2Bph98w%2Btw75kDpUnb%2FYozp4SOr6s%2B9dlKwY4Wijm2qyhHQbjRXcAEBPiVTjQ01n5KAIh5uLbKMrPrjv3AgSsYOx5Sgd%2FBY%2FWw1XzK4IlmSAB5Hd8VLVaOUY2%2BZF7SktfEeAdjDiDS5zP0PdQq1pSJEvGMwxhFzsmAcuyJ0GwVJ4GXbscqRwn7g1iCpwaVUfoxeZWdkFMdDWJZ5ItcJLIq8uxjA%2FJNmcGwTlqDDI%2FZRDvmPzyvkOLQtIgT%2BYtzj4WIjiG2UmGuHq33ITVxkT8HTaw8rDqlsI7OtCUg8cWFvCm5jJ6sFoGMGMAzDVqRDwyKf6xLHP1auHEFNBz31oArmlkg3Bm0W2VFajFJWRU9VSOud%2FPg%2Bz2YcgJfdGH8DEvMaQvm0MAo4V0wpKGWvQY6pgEDHY6QhbfU3z71pa9DNw0k9Q02wxUWVtua4RlVqwxNfS%2BGQqHthqPO58gjUqdwwFw5yEZ0oriJCyYKGVOkeFyZ91xBD%2FkGFPcM1I1LAk%2FPKQ6PmbAio3aE3EbpPIoR5LQO%2FqvFnz5E8rgppKC%2F8DcSjXaFHjRnCjKc785EvljLT0P6QlwKcU%2Fr7BnFdhKpcv3Qpm0es6ET2QNtJleQ6%2BaFti%2Fqr%2BgR&X-Amz-Signature=4028bd611152c3e3921fb41fc1af73169ae3704f7ab6a9fd4d24664c234e89c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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