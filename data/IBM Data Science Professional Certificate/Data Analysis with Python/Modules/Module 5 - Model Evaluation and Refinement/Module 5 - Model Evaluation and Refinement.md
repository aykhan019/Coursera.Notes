

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=cb4e9612d7caa21feca12a0759735d4eb594ec10934123abd4a4341749725e6d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=e51c6e785f32cdaa636ee9f70a6f5b49baca7294773e8f774da8a9af436201f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=8b591815df3245d81375e8ee5d8a228bb1d8b49f14f57e9c32c3f1414482a7bc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=9dca326067c7e860ff0b0d4e7885315a9895d834a2bd79cd4fadb4a264f72c6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=1a33809972820e6037982f4eaea4684877e9b1a1de34643c91cb5422d044b850&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=731131695f76b0a1e23358848af1590c80f56dfa23dcd48ebf301986fb8f2676&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=1d888bddec17242f1033b7cff92ff18fc311dc1b2c6a4c79984f0ee7746d5d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=804f0a94b4aa4fc56b70c177d64e519ea26389c7a8ade0f92b27e81a896a6114&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=d0b0ccf0e06f37468f2f3309327381985945c3dde5bc6f70b715971e6ccd81ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPBUIFZX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIGyFTB67ROiRHW1uvQhGeHBDPOO9owb0DUdntsPg9DAiBoBKSrXJkABxy47%2FRifooIlqXPARnpmzSQPntzRwjf5iqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdfEkus%2BsncYu5Ao2KtwDyN%2FcGPAnuSoS8vxM33OpNbMO%2FWZSIWVPkj8r4PCdJ5IM0pd9DSAMBjCh%2FEslqxm%2FMpTAYWaZMc%2B453hP%2FBYamdr6oBU2ovookoITEBX9Tai83G4nieeWQE76c5W9n87Bz0vbQT9TD31Hcy1OI0KN77%2F%2B8OL5%2F5zr5xRMVKGHod5lGnBKvK5yfbeKlUoMpwkLkasTbQZvNfb%2F%2BiXbQNY%2FymbMgV46zSapP4cJWUqJdEhKps1A%2FhhjvHPoLQyx%2BqN1vyvKQVhy3QlocVX6a9Ym33ws0Ed19FF6Un5%2FSw53kbClcuGERpx5Ei6k%2FNs7xSiEM5Ju4UOAhas5vBUs4aXjMybRcw2Xy2KkMaxJ4MhVbbG0I2J%2F7diHehhZ7dJZZ9r16qgQGRDW5g7oQEdgySP4gQfpgOsAoqoyUveyZK4ulaMPPZU8jYFIeXxjne75L52V8joy46CPitKLWz7aLCmQrN0RCsT2faPkPjkDjAjHA2B1EkXpXo%2Btj%2FssvGJDFVq5D%2BQUyiu9jl2r4Q0nJ42EYbZZIPNg5y1BjuH63jC2a7NBRPiCAkahH2bq5W7r3ugNpH5egiX5E8ZS3%2FG2xoM1wYdEEsVHIz3hcvJyC2Xf4sm3Zse%2FIPX%2BEieH9ocw0Y%2FzvAY6pgESF4dWj91aytv5fAdr8xGOAwg9Ql2iBFU6fJvLzWHHVLykYqBCSoQ2CFI2PCkxEYdXJ1Ff%2BACJFIFLJ18KyReFwWxmrYOIKEVXQOlo8lgJzHln9u0z9zDSoq1JgJa4iyzrIzXbDtEQSduVeOyYgz4D%2F3394Twpnasc8L%2FYAlA3EoaYDx47qzVUE4r9%2BnqEXK5V6gO7iNELzDRO9Q69Y2SCVTfa6CWO&X-Amz-Signature=91a101135946545d4906ef86e4ed5d49db70fb243231fd948f0db40c39365860&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPBUIFZX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIGyFTB67ROiRHW1uvQhGeHBDPOO9owb0DUdntsPg9DAiBoBKSrXJkABxy47%2FRifooIlqXPARnpmzSQPntzRwjf5iqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdfEkus%2BsncYu5Ao2KtwDyN%2FcGPAnuSoS8vxM33OpNbMO%2FWZSIWVPkj8r4PCdJ5IM0pd9DSAMBjCh%2FEslqxm%2FMpTAYWaZMc%2B453hP%2FBYamdr6oBU2ovookoITEBX9Tai83G4nieeWQE76c5W9n87Bz0vbQT9TD31Hcy1OI0KN77%2F%2B8OL5%2F5zr5xRMVKGHod5lGnBKvK5yfbeKlUoMpwkLkasTbQZvNfb%2F%2BiXbQNY%2FymbMgV46zSapP4cJWUqJdEhKps1A%2FhhjvHPoLQyx%2BqN1vyvKQVhy3QlocVX6a9Ym33ws0Ed19FF6Un5%2FSw53kbClcuGERpx5Ei6k%2FNs7xSiEM5Ju4UOAhas5vBUs4aXjMybRcw2Xy2KkMaxJ4MhVbbG0I2J%2F7diHehhZ7dJZZ9r16qgQGRDW5g7oQEdgySP4gQfpgOsAoqoyUveyZK4ulaMPPZU8jYFIeXxjne75L52V8joy46CPitKLWz7aLCmQrN0RCsT2faPkPjkDjAjHA2B1EkXpXo%2Btj%2FssvGJDFVq5D%2BQUyiu9jl2r4Q0nJ42EYbZZIPNg5y1BjuH63jC2a7NBRPiCAkahH2bq5W7r3ugNpH5egiX5E8ZS3%2FG2xoM1wYdEEsVHIz3hcvJyC2Xf4sm3Zse%2FIPX%2BEieH9ocw0Y%2FzvAY6pgESF4dWj91aytv5fAdr8xGOAwg9Ql2iBFU6fJvLzWHHVLykYqBCSoQ2CFI2PCkxEYdXJ1Ff%2BACJFIFLJ18KyReFwWxmrYOIKEVXQOlo8lgJzHln9u0z9zDSoq1JgJa4iyzrIzXbDtEQSduVeOyYgz4D%2F3394Twpnasc8L%2FYAlA3EoaYDx47qzVUE4r9%2BnqEXK5V6gO7iNELzDRO9Q69Y2SCVTfa6CWO&X-Amz-Signature=5d7a86d20b1f06c8de98a578005fefe5480a01a1f2734e5294b7e47472972255&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPBUIFZX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIGyFTB67ROiRHW1uvQhGeHBDPOO9owb0DUdntsPg9DAiBoBKSrXJkABxy47%2FRifooIlqXPARnpmzSQPntzRwjf5iqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdfEkus%2BsncYu5Ao2KtwDyN%2FcGPAnuSoS8vxM33OpNbMO%2FWZSIWVPkj8r4PCdJ5IM0pd9DSAMBjCh%2FEslqxm%2FMpTAYWaZMc%2B453hP%2FBYamdr6oBU2ovookoITEBX9Tai83G4nieeWQE76c5W9n87Bz0vbQT9TD31Hcy1OI0KN77%2F%2B8OL5%2F5zr5xRMVKGHod5lGnBKvK5yfbeKlUoMpwkLkasTbQZvNfb%2F%2BiXbQNY%2FymbMgV46zSapP4cJWUqJdEhKps1A%2FhhjvHPoLQyx%2BqN1vyvKQVhy3QlocVX6a9Ym33ws0Ed19FF6Un5%2FSw53kbClcuGERpx5Ei6k%2FNs7xSiEM5Ju4UOAhas5vBUs4aXjMybRcw2Xy2KkMaxJ4MhVbbG0I2J%2F7diHehhZ7dJZZ9r16qgQGRDW5g7oQEdgySP4gQfpgOsAoqoyUveyZK4ulaMPPZU8jYFIeXxjne75L52V8joy46CPitKLWz7aLCmQrN0RCsT2faPkPjkDjAjHA2B1EkXpXo%2Btj%2FssvGJDFVq5D%2BQUyiu9jl2r4Q0nJ42EYbZZIPNg5y1BjuH63jC2a7NBRPiCAkahH2bq5W7r3ugNpH5egiX5E8ZS3%2FG2xoM1wYdEEsVHIz3hcvJyC2Xf4sm3Zse%2FIPX%2BEieH9ocw0Y%2FzvAY6pgESF4dWj91aytv5fAdr8xGOAwg9Ql2iBFU6fJvLzWHHVLykYqBCSoQ2CFI2PCkxEYdXJ1Ff%2BACJFIFLJ18KyReFwWxmrYOIKEVXQOlo8lgJzHln9u0z9zDSoq1JgJa4iyzrIzXbDtEQSduVeOyYgz4D%2F3394Twpnasc8L%2FYAlA3EoaYDx47qzVUE4r9%2BnqEXK5V6gO7iNELzDRO9Q69Y2SCVTfa6CWO&X-Amz-Signature=d6cec315bb262a4580b12f9d5f22a502d0b230cd00cf1b0c7846e261d1b186dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=aa6a544bec99d7dd6a9a6ee3bb8e4c7069c6306124e9dbc9b38c8416d6596e57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=58095ef9de9177909fef53317b841b13582c09a3ad0e0ff37c95a5aabd596761&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=e2c4e3c814176871ec2593accdf0f3edd8dceaee11386cced3272dcea71069e4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=3bfc345505ab3e1d46e84e8bdd38f02db2b85d8bf2acea1e002bddd22a2bbd38&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=9278dd3109f6a85a76faca195220968db57fb7153a8f2acefcccfa05cf3f037c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B22GOWQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBk8AnZ7fy82mxV6zg%2BcUehV%2FJiBDs0xbmmY5hXWUWQ4AiEAsHWTiQp%2Fc10Dm4HkVi9LzTX7khxXgprTiSyclU6LO2oqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2BekpV0FbcuX%2FrAwircAzzoQ%2FAkf5DB%2B3DH2GSKTgjSGlwtU32BWyCzWXCeAXnuAF0y6dkCtmXQojruapR2OQKnNr8c5AdXGcfJ7AEkSbCSPzgJ0Bf7ViHEVFY2w3SqV3b1lxxBLdkSqL8ewyqFAAORAhkYhAfPE6pqtw%2B4r6J4IQEv3VdleEbAG5bYZgZUVpHTd6TuqIi9ipj9ygq%2F9sOphszfciSL%2FnM5Srnkjp0JjMSg2UvnD%2BZndJxIwPKwSDjdWKf76iZTSaX8A7uPYUR2oprC47ZlunkTgwioLrIsw6DQ%2FXWTnUyvUnrVHFoFw4ZJLkg6asI3b5ERzN0WHD%2BOwpOdkfzdJnYr45AZ1TQCFeV8orhh1Y%2Fe%2BPm2BLtTBsk%2BN6Thz5%2B0HOMA3n1HHdXJccqaOcRC4F8GKZwW%2BtsAxdVKFqKgYfAZ5cmtMWGIQgJZeKekzIiMuQEFuK0DoW9tZN3l7wVeh%2FpFIPjnXIn15ySgeVbIbgQTaWlPVMetSFSM81SugJcNSQoqa9q2Uu4w2QRzdMBa0j2C4nC6fLS6p0Npuaz4C3hw7TgL0oUCB0qqqYQ6oCRYyRMDL1d6UWDZ0MlQEGaqRJTVCmsiPjFpWiuIrJRIhLXmJhZMgCcCOsZLsycs879AT8BQMJ2P87wGOqUBBlGUS2dMpNyJIgvWfADl8Gyo411GULg3QXTUTg6t2%2B2oU%2BYyA7gWTT7cWEVV9t3ltBhd24K4NjhJ%2BuTLea1iIAlBw1gXDulbzS0kxKZ6lFuQ7ho993f5Z8%2Bn1%2FhmkM6iQoX7MdbI5DFg%2B0yrbsq0vKH3sUOFK5UTuDPTJJQ7HsyoJJhgGGRjlpEWFj0tSZDj0uk9V0LjjfvsZUHGIwPBnuC7dWDB&X-Amz-Signature=8de07fa6e0ce0ec9ecce8eac385d4741938f9a01f447b14af6c9708eda16e93e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQMOCMAI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEoO%2BIaRuQQkMZstU2Qx4FR8Igp%2BE52%2B1eWicIZRIT3sAiArReLPFcXYd6MfT8wvQRTcZd4eCiMjRT0j4wpa2IbGhyqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lGJuz9D82%2FVjo5KtwDRwcTc%2BqASuXAeAwFxLTfDBc7dAfhoBu8g%2F%2FIEgTX3hBz1Nz%2BKkjDYWmOgwSRyOdo4BGMPUMRJMKXiVxPl9QweQaz4ZgSKXAHAX1AzthsdDHAdoTIm5qchK1DYZEQiDYfvDTHXSZv84dEjYVYBRpLGowYUc9RzqpAjb0cbuvMqXXl5NdFGK%2F4DgPXYlp493tMYGy5hsxfv1BOQHe9gR8PF5cbmCX%2FP7IPQ8wbbYL6ZwTt5VUmnja5NlHVOI%2F%2F%2FNnj9YTbnEraqOA1cBFgeCk2WAW8%2Fsxz132%2Fmo1p05kbHNjmaa5Pz4r375xQU7ELBtjvI56osDnnzrRI%2BCUKoOXfzWYPnqcUhqHqeVj28mWMRe9Q5E4ruSnPyEPrtq95wf6oV56EmQ6fFtpPryHAb6LLs%2BUz4qFe4tnx9gzSs8b4041PM2PCcduFkcDWj2SJPb2psXjc0Y9Gy0NDqI3k7%2BACDhoRvUyzEQljBCxsmTTriBCkyArl7tPkqdjD%2FqXwxFnyZujtMvsxOjqlKMAwFVq%2B228%2FtkC04%2FNXKBpPOnzJiU0npB7GMx6E5NwviOssCguOadNl%2Boa2OJ%2FD18%2ByEOT0UCtgQN3hbHtNDJDM4uH3SN7B78BJhKJyfb4%2FWhEw9Y%2FzvAY6pgHi9NJNAXEvr24r14o%2Bwogr4xMin1yOaA4892N%2FuGesJSNXweLd8k%2FEtm2nITBFdjVdhXXxkOQFsoM3UYgU%2B6VbB8XbG21EkbBn9y8sm7PRMzt1PNGJGoktaY7I8Qpvt1kN4K%2FTpr0fGoZLdw5xWebE711yMzEqkmVugVLt%2F2O6xm%2BgrlgrdQMFxaHPJo5qzK8KLhyO%2ByzDPWuA90quB9fmBDOpvSVJ&X-Amz-Signature=c2f1db8fb7ec79f61447f7c01fded81c160d67e1a8966cab69f9a321d390014e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQMOCMAI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEoO%2BIaRuQQkMZstU2Qx4FR8Igp%2BE52%2B1eWicIZRIT3sAiArReLPFcXYd6MfT8wvQRTcZd4eCiMjRT0j4wpa2IbGhyqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lGJuz9D82%2FVjo5KtwDRwcTc%2BqASuXAeAwFxLTfDBc7dAfhoBu8g%2F%2FIEgTX3hBz1Nz%2BKkjDYWmOgwSRyOdo4BGMPUMRJMKXiVxPl9QweQaz4ZgSKXAHAX1AzthsdDHAdoTIm5qchK1DYZEQiDYfvDTHXSZv84dEjYVYBRpLGowYUc9RzqpAjb0cbuvMqXXl5NdFGK%2F4DgPXYlp493tMYGy5hsxfv1BOQHe9gR8PF5cbmCX%2FP7IPQ8wbbYL6ZwTt5VUmnja5NlHVOI%2F%2F%2FNnj9YTbnEraqOA1cBFgeCk2WAW8%2Fsxz132%2Fmo1p05kbHNjmaa5Pz4r375xQU7ELBtjvI56osDnnzrRI%2BCUKoOXfzWYPnqcUhqHqeVj28mWMRe9Q5E4ruSnPyEPrtq95wf6oV56EmQ6fFtpPryHAb6LLs%2BUz4qFe4tnx9gzSs8b4041PM2PCcduFkcDWj2SJPb2psXjc0Y9Gy0NDqI3k7%2BACDhoRvUyzEQljBCxsmTTriBCkyArl7tPkqdjD%2FqXwxFnyZujtMvsxOjqlKMAwFVq%2B228%2FtkC04%2FNXKBpPOnzJiU0npB7GMx6E5NwviOssCguOadNl%2Boa2OJ%2FD18%2ByEOT0UCtgQN3hbHtNDJDM4uH3SN7B78BJhKJyfb4%2FWhEw9Y%2FzvAY6pgHi9NJNAXEvr24r14o%2Bwogr4xMin1yOaA4892N%2FuGesJSNXweLd8k%2FEtm2nITBFdjVdhXXxkOQFsoM3UYgU%2B6VbB8XbG21EkbBn9y8sm7PRMzt1PNGJGoktaY7I8Qpvt1kN4K%2FTpr0fGoZLdw5xWebE711yMzEqkmVugVLt%2F2O6xm%2BgrlgrdQMFxaHPJo5qzK8KLhyO%2ByzDPWuA90quB9fmBDOpvSVJ&X-Amz-Signature=5e71bcade0e39e11f847e20a63530575e678eb852c412f2d5e2fa40456312dad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWIM7OP6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfVuRmtaNVeQEtxZfscMY5gSXL1iJNMiWqlecwazQrLgIhANafbUpE9Tnu9IZCgEQ8krbYKJOtLzM4E29OWtihbhLiKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8w34dBdxFzToppXcq3AN791v5SFTm99dt1F68fo%2FCLRtF0mhMP1FtcmDKT%2FwJpxO5zeUFDm5fkDHu6Kg7IgFa8wk8Tr7iAbgv72l9VSyTZ36jkupGXwLpOMVDrBHxypEgC0QAsB8J1AcbEP0BNHP%2FaNsTNdzkk%2BCe6sH5yIQyQSJEaQuBEddU2VPQ%2BEq1twYajNk5DGjMO3yC%2Bo7gfUIMPESnKkQZNodawA0Yl0sSp8XqrC3NbSbtzPgach3NUhanZZn5lYqPEVWelK%2F8dt%2B4Vp8U9dTyMKKvnEEXkksXdYp7aYaCGNJ7n1pldYE0xsL1JLTanKHb2xLBx98g61qpGDrOEPNrgq%2FsoNOZg8F%2Bq3Mh1e64PVrSc5sHUeJQTcJwzqEqmFLfjDTrAsEoSAnVYubu711UpexQhcc57E5jKQbpMxt2S%2FxI5icsJr%2B6HLPXbzD6b0JzAqgiy97IfMi%2B4vn3cZptDHPm7w0x%2B9UL4616LPtmpUhxruoqY2c6Kbd8aJ7Q6Aiz6%2B%2Ft%2FRKPajiqEtlj8alYceCcdtwpYjRLKf0OJFUvkU4gaaBUJEhrq28yo%2BaX7jmRhipLlkydbVQd2Rc6YN1IXc1WrQ8y%2F23z26fguaY%2F0r35ToiXKNPujDtf0xh%2F99c61F9C2zD7j%2FO8BjqkAaAnPAKCXkz5OuEzw%2FZ9D4R7DTF2f4EtnLV4%2Bu7Dz%2BpuztDRHIZ9NOZ4luD%2B9Jlq8hv80xM%2BrXUVFP5fSPEh5WOrp4RmSMYE05l%2BFWnZT6O%2B7U7hZ6E1Sii%2BhlZ0fGsf94d9DuJJZ%2BhMXGBI32qoPwm9HgvACung3c04xpjPW1D6fdOk7Td1rOZdboFPJPgFkzc5Xm7uxU4LW50Qv55rWa7mVurc&X-Amz-Signature=0f1d5a4afaf30ac34a26d24e2c176fb4582183552c192104ee03e731cd12967f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OIWNA2I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnVQaCugp7aPxLzXQ15bp1m127o4QXG4j74CasYfU%2FaAiEA85VTtYI%2BZytJHfH7okMTWRxWsre2BuZBDOL693O3kbMqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwJvcF5Ldk9TeGmnCrcA0pQDoUz6hiAyi8mknx3uxgeftY%2FW6KQ1W8WuBYTEVA%2BT%2BotJYb1FgKlCC%2BJLIHJP5n399OL0vK3%2Fdk1tEOwAnlT5JsZ2tunNxkkHYonwoRL0fuvpTgLWyoIhXjX01cMoe79XElcP%2F9%2FJ3kBdIenA5wNsDQIuRkUyEUf5osM2jtH7jIlpY3%2FGF%2BgBmpw0wBR7%2BP1B7%2FbgqsAm%2B5jlsyK8Xm2kkl%2F4OWQn62QZYfSKs%2B2kh2OucWXFGj6zWaGy4E3t0SEOrQd7KvUcp%2BxbCZRKJYXL7Go7iwVdv4qA%2FyfvTBz%2BJJn3CM23NcWaAtXntiVctIkB%2FT8CTHtf5B95tobfs1zlGvnH8TGTEmzHH4TTcmfX1PiJxL%2FCvA01kmKzmlhZakJnAcWGhdaPigAmft2fVCT%2FpGLQb99yDRTxZoaXcnvNXrgzJ%2F0apMX6dDBSGjHcUjTHGLt46Wr%2F006MFVbsGm4yxjcn2monFIPDdqZm%2B7p8VjTj9DwQQWQjZGmyH8ZSH98Wvr%2BY9HZnVp0Hs1BzmdSRwN4fzUFlLxSJyEnYTMAmahxKOp2CAmVLmc4L0ThMUPCnx%2FowCEYVzc2WArgocrK1pS9FIL7EqFufB6FgktztxDd3bVJWv8KkS4lMKCP87wGOqUBtozB8TE1TOtZ8AvMb7ZodagiZGrYJiib8JMtImAmXoWKWKI6w3a5OVerqmadOgymdheQWY14AAGJ4OqXsTmL7U50NwceTyjUFwvPAAZyH8OcMfVy8R5MOretR%2FvGdN%2FC1i7rXRlm%2BhuvuwudAbZEvmv%2BjFzuGoP%2Fkoj%2B%2BPe8rrXK4D3Ib3kKkpIjTu2dAhDLJdrpS%2FT5F40KOjC%2Fhr5jIXUW316E&X-Amz-Signature=eb8e33334de0def62ea86fe5b7ad38138cf0011dfb69708a5c43df4fc83685fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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