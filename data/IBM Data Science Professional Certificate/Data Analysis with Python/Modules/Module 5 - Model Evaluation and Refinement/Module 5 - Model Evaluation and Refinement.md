

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=d73f2518df53fee761be236c93c87643cc441599aa09b35a5cf759c51a8bc355&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=f8067b6d12fe094d114baba6716c0038fff560d1e039a5d105a869df91b1b873&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=c81a22f54c9043ba3f880a4332928fbad839cf88da3955753c87b086e398ffbe&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=dfc5aecedc51e8614b694be23b4a24bbe3ab49cb77fbeb900c71812eff4a11dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=e31f1ddc8fba8651012ae3eea4ed988052589f6b4cefe5989168bdbcb0fb40fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=766734ad68539cb4f669d529be5129448711e8ce5bdd0f5e64f26b5fa688a256&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=bd5fcf9452385a4e4d3a4dbaa136cd7bba6a2afec49477e8793c8b6cf9fb4570&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=352b4c6392faffbf028de45f13ca6e58240f73274320621a0f5c40d2cf8f1264&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=b23aabf136666a4bc9b8d6dd8ed7f23fb2b1b6d2e13012ceb8019ef4cdf453f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCTT7PFX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIF0q0jVH8VUpCyJVoydQLscRNrWfjTSe713%2Fyks9tWSNAiAsUGX%2Fpi9%2FVqlQYkNmvi1S9%2FD%2BTEKvC5PXWd67DNbC%2FSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMvA6my3hwiFnimtXzKtwDqYemH6Ev%2BQRHhzeomNuPRhVdesjf1hpcfM%2FR1V5%2FbV8ukUSeglTDQAdIMihVNIGiBF4T8GYEoTpSlQek6ddd2upC9FzndtNHOOI7y1Y3w1a7xY1agFTPAL0aOhqnJ1PSOwe5elCIEWqxZ0bSCzlte4bP7muCZrisy55efhcd2TVojg2KHpfjA5qBpL0aL9pgmIAMC1WWxqCEsfO%2FyyKGKTmz%2FjdvJ2RRW5N9vPM3segQB0rgDSre385I%2Bk6lhYYuuvG85gkEwRVIgbvnjbht4%2BS5d%2F6Kl5sNJPN5Rr%2BtPObEpEiCqnG%2FDCW6sfjYYIIJUcZjCEaM5U1DjW0Na6iEf04up1hTpYw202txCtcRZju3WcDX%2Byrxm1cgXjWF5Dkn7ji2neLQcryFtIp0uc%2FmvUESAVWPsCl4bVLZ02QZjmXnPEFLtYp9cDFN7dFbt62Rs81WcP7O3GgumIJgYSwenONTVxM3L6Gd6yCjNP3lZxqXh1yyANxcA7RHLi0N8I3nGa12lrz74DXCRs%2Bh%2B8H19ZLybsSrm7aP5Rb2QR%2Be8haHRid7RaQK65F2R29IRyBTOb9utgKn24cYleTpp3kAN830nBOcu7Jp3o1RBaBYMk4LM5TQBHmilvS0wHAwkYuNvQY6pgHtTHxGgKpydfom%2F1osJ5rT5knGlkdd%2B5mk6o58ZE1rx7jem42GQvhHBBZWxd4I53fZXUQjI9s2VYG%2FicdmGtgLCl0eXIQwcsxZBqZ5uwNkjtYjwD%2FRdZZEbeTDdb9yTWHslTxvp8WO4MrXl1N6JZNm5R8XYa%2F0GNJumA21LjIuCO27MlBxGVwvM35wRCVzPZbZi2k8xKeuX7K5umh9XtVTh6ylUXXb&X-Amz-Signature=eafd55d655696643bc0e70171b41383cf7da50f4be068fd99283969f9d0832ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCTT7PFX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIF0q0jVH8VUpCyJVoydQLscRNrWfjTSe713%2Fyks9tWSNAiAsUGX%2Fpi9%2FVqlQYkNmvi1S9%2FD%2BTEKvC5PXWd67DNbC%2FSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMvA6my3hwiFnimtXzKtwDqYemH6Ev%2BQRHhzeomNuPRhVdesjf1hpcfM%2FR1V5%2FbV8ukUSeglTDQAdIMihVNIGiBF4T8GYEoTpSlQek6ddd2upC9FzndtNHOOI7y1Y3w1a7xY1agFTPAL0aOhqnJ1PSOwe5elCIEWqxZ0bSCzlte4bP7muCZrisy55efhcd2TVojg2KHpfjA5qBpL0aL9pgmIAMC1WWxqCEsfO%2FyyKGKTmz%2FjdvJ2RRW5N9vPM3segQB0rgDSre385I%2Bk6lhYYuuvG85gkEwRVIgbvnjbht4%2BS5d%2F6Kl5sNJPN5Rr%2BtPObEpEiCqnG%2FDCW6sfjYYIIJUcZjCEaM5U1DjW0Na6iEf04up1hTpYw202txCtcRZju3WcDX%2Byrxm1cgXjWF5Dkn7ji2neLQcryFtIp0uc%2FmvUESAVWPsCl4bVLZ02QZjmXnPEFLtYp9cDFN7dFbt62Rs81WcP7O3GgumIJgYSwenONTVxM3L6Gd6yCjNP3lZxqXh1yyANxcA7RHLi0N8I3nGa12lrz74DXCRs%2Bh%2B8H19ZLybsSrm7aP5Rb2QR%2Be8haHRid7RaQK65F2R29IRyBTOb9utgKn24cYleTpp3kAN830nBOcu7Jp3o1RBaBYMk4LM5TQBHmilvS0wHAwkYuNvQY6pgHtTHxGgKpydfom%2F1osJ5rT5knGlkdd%2B5mk6o58ZE1rx7jem42GQvhHBBZWxd4I53fZXUQjI9s2VYG%2FicdmGtgLCl0eXIQwcsxZBqZ5uwNkjtYjwD%2FRdZZEbeTDdb9yTWHslTxvp8WO4MrXl1N6JZNm5R8XYa%2F0GNJumA21LjIuCO27MlBxGVwvM35wRCVzPZbZi2k8xKeuX7K5umh9XtVTh6ylUXXb&X-Amz-Signature=fae75745cebd748654a1b46572615f8fcb1f08b2df20e77dbe0c289b894cc546&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCTT7PFX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIF0q0jVH8VUpCyJVoydQLscRNrWfjTSe713%2Fyks9tWSNAiAsUGX%2Fpi9%2FVqlQYkNmvi1S9%2FD%2BTEKvC5PXWd67DNbC%2FSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMvA6my3hwiFnimtXzKtwDqYemH6Ev%2BQRHhzeomNuPRhVdesjf1hpcfM%2FR1V5%2FbV8ukUSeglTDQAdIMihVNIGiBF4T8GYEoTpSlQek6ddd2upC9FzndtNHOOI7y1Y3w1a7xY1agFTPAL0aOhqnJ1PSOwe5elCIEWqxZ0bSCzlte4bP7muCZrisy55efhcd2TVojg2KHpfjA5qBpL0aL9pgmIAMC1WWxqCEsfO%2FyyKGKTmz%2FjdvJ2RRW5N9vPM3segQB0rgDSre385I%2Bk6lhYYuuvG85gkEwRVIgbvnjbht4%2BS5d%2F6Kl5sNJPN5Rr%2BtPObEpEiCqnG%2FDCW6sfjYYIIJUcZjCEaM5U1DjW0Na6iEf04up1hTpYw202txCtcRZju3WcDX%2Byrxm1cgXjWF5Dkn7ji2neLQcryFtIp0uc%2FmvUESAVWPsCl4bVLZ02QZjmXnPEFLtYp9cDFN7dFbt62Rs81WcP7O3GgumIJgYSwenONTVxM3L6Gd6yCjNP3lZxqXh1yyANxcA7RHLi0N8I3nGa12lrz74DXCRs%2Bh%2B8H19ZLybsSrm7aP5Rb2QR%2Be8haHRid7RaQK65F2R29IRyBTOb9utgKn24cYleTpp3kAN830nBOcu7Jp3o1RBaBYMk4LM5TQBHmilvS0wHAwkYuNvQY6pgHtTHxGgKpydfom%2F1osJ5rT5knGlkdd%2B5mk6o58ZE1rx7jem42GQvhHBBZWxd4I53fZXUQjI9s2VYG%2FicdmGtgLCl0eXIQwcsxZBqZ5uwNkjtYjwD%2FRdZZEbeTDdb9yTWHslTxvp8WO4MrXl1N6JZNm5R8XYa%2F0GNJumA21LjIuCO27MlBxGVwvM35wRCVzPZbZi2k8xKeuX7K5umh9XtVTh6ylUXXb&X-Amz-Signature=1351f9e5fbd80862cc2f1c813f83bd29781742d452563bc21836721760fe0020&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=e26897a8aa90717594f6a729da4192f460320cee590f7c8d3e941b7772a0c839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=052483576a91cc11aa32c629d752ca81e3724ad7e04deb83d6cdd46115041342&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=3b57af7c2f47da0e88182154885d1dc1f53282cd5b8ff427c5a2a95df175a487&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=76c5e2c7b6a374e2ba3c7c7b4c37597e48474adb507aa7a97f85c42aa1d2c28e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=bbf126a1023dac02f685be55be3baa94dc067b748a144cb079131246c447996c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX2NXWRO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCKzFSrAxM3UrZoCtUR6Jp4aZurtnQUz8a0YbY1c%2BpaDAIhAJCDjGs8SCw4eJp%2FH4ym9gg9fNdOwVe%2BjrnC9733xLL7Kv8DCEQQABoMNjM3NDIzMTgzODA1Igwz45VRhLNUtKQxb0oq3AOhZwtOT3PtRypY91sXH4FN1YZYAmNPVIEuxRqzRd8gQwTfuisQvGHvENr3mUbX7Hjm4YXujbQ3dqrx4ybPdTGbpeB%2FvlB06Qfzfz6%2B7CS5d8zJZOTkVOkUMNEsvmYXjtFNBHmPBOp1LYGUDqR8HgsG1CSiMDl9iuGufoFF52uugnhf%2FgT5aXfAz0rErME5gK%2B0f9R5lf1jIaoqgIjIWzPFNjGBXuvqCfg7nj2SD6iR05cnq%2Ff2UGvXF2W27sfleOROWaQF87qg45ko%2FW4wb4M7u1UwHCPalYn77Hz2GXb%2FslwRlPjdv6VMiBw%2BAiGsA1AofaKn%2B%2FQe2s4s4YqzRZJ%2FC62WE7q1VVlGmJCu0Yr%2BHJ2QZUxjcIuKW0ZhkETP%2BXIDr41Xpo68sTEqR%2BnE0RFFQQcTJKus5IgCvO5M6u%2FsFzjEvXymVR9YL3vQ0sg4byPBY9%2FL0Y4M8LZZ1Ck%2BwH8NTp3m0vpQA5TjFrNgKLvh73Zs%2BJaC6gA5TpwMTRplVLxncEwJF%2FuL26FwjNsWVpB2Plk%2BPYOVWwjFZg5VogUi0eksOSxipJWBtc3Ti%2B9%2FGsMwwg5xrWpLtlWFDIPQafIoE3lMjSFv8mZyIdYyWM5%2FNuZ1PUNoyr9waIhQ8jCwi429BjqkAZfqKIcuqlvpapnTbhjZSB9PBpvfatxs7rZWYxx%2FGdppu0iyUStN5x39JZNRvLxjjGMorZQnqFVYTEA4LjB7Yd9JBYzlLQ4c6HkbI0TbqADH9iAU%2BhQ0bxhBfoYCd800YGyDTgqMAvCXsPpkeEReZtHvnUpYxXdlQra5BMAhjac%2BJ%2Fqe1B%2BAe4tpggP7estgfOyZYipivE14N%2B7mt%2FOklVr2mPvg&X-Amz-Signature=7a20790c614964eadaf172edb00dbf69efb3a48254ca260216e5b7aadcb88927&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYYTZD6B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQD6uv8y8%2FymTVCWxdQGhnrr4K5%2FAVyqpUKDw%2FhbAmpN4wIgKP8N3d8j3N43jdTCz7tYPThs%2FleKmvpF5rh2DLFJlKgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDDJeadMt7ldCUxUIwSrcA4RV5lru5UVt8CwRdpK4kk4CoX2TbgJWCGrEjbPGH%2FIv7vlZYEqU4mmmr4oDxKJT7oP0plC2FvMKKAeltTfUjj2pcRpxc6HG5PTUAnWwfyTIR%2BV%2BY9S2KW0rlrjCkl%2F8edWzlLcNQ%2B%2BArYgORG6T2Ez00JvmvqiUfaTE6MTRvMwaUvx5VGUZpFniR2dsKJFRl3dBhuXfA06ClfFGhGyoI1XTv42NvqVEoimwnAxLZxJm7KXS8uaJj9zJ9rXiObgNPjusbH3hRw5z6Pp2H63q%2F8j7eida2NXeFtVLLWpwxgCyklHB8mRrMXEHNSFYl%2FU%2BxwoV0%2B11hPz3NomXB3wFFh08Uu%2F39BWndcDagJFVoHB5GDKEPwwXuqEYF3mRHN3w6ekDA3evglx4Kt%2FpGLuHAnYZzTZNz6ZTrmSIPLyyt5yonXByhDOV2yP3Npapaejf8XdQOzYx4kP4HtBaop4RQeVsKuFXHkFxDSMzLNKla7n%2BQxPB0EwaaNGBrTTpRJXJjehqA2IkRU00lV7VayGVuY%2FUuMGSEhPXELEB9jYBxRdkEPb3lfuIC4GdwO7hCV82pNB%2B2LoG4yiU1tbKAfJ0SBo%2BWCrM24AdUibRYYhehvi%2FPP3%2F%2Bb8Rn38aWypyMLDjjb0GOqUBvvjHzyg29ukyBp29BXEaMDYmiu%2B0kmqJwrIuFQLUI3EeiWzXuxJ61fQwFbGSpy28YU7oUTkgi1LXpb3EdgnZgo5Y1OM9MZrGMas8yhFR%2F4i1jyWauAO4jOCUkcIr5BBQZ1jy9Qg19vzxc%2BFs4M9Ytijv83XNfPp3E47vvm4dO%2BPJsdAH%2FXKpgrJUPq7rwXwqYofUiMaGRuQ6rHp3BABBFes1PQao&X-Amz-Signature=631e6bb85dd20ccae3141353a5c708e6b0d0761a260ec86c826c25bad6a1626a&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYYTZD6B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQD6uv8y8%2FymTVCWxdQGhnrr4K5%2FAVyqpUKDw%2FhbAmpN4wIgKP8N3d8j3N43jdTCz7tYPThs%2FleKmvpF5rh2DLFJlKgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDDJeadMt7ldCUxUIwSrcA4RV5lru5UVt8CwRdpK4kk4CoX2TbgJWCGrEjbPGH%2FIv7vlZYEqU4mmmr4oDxKJT7oP0plC2FvMKKAeltTfUjj2pcRpxc6HG5PTUAnWwfyTIR%2BV%2BY9S2KW0rlrjCkl%2F8edWzlLcNQ%2B%2BArYgORG6T2Ez00JvmvqiUfaTE6MTRvMwaUvx5VGUZpFniR2dsKJFRl3dBhuXfA06ClfFGhGyoI1XTv42NvqVEoimwnAxLZxJm7KXS8uaJj9zJ9rXiObgNPjusbH3hRw5z6Pp2H63q%2F8j7eida2NXeFtVLLWpwxgCyklHB8mRrMXEHNSFYl%2FU%2BxwoV0%2B11hPz3NomXB3wFFh08Uu%2F39BWndcDagJFVoHB5GDKEPwwXuqEYF3mRHN3w6ekDA3evglx4Kt%2FpGLuHAnYZzTZNz6ZTrmSIPLyyt5yonXByhDOV2yP3Npapaejf8XdQOzYx4kP4HtBaop4RQeVsKuFXHkFxDSMzLNKla7n%2BQxPB0EwaaNGBrTTpRJXJjehqA2IkRU00lV7VayGVuY%2FUuMGSEhPXELEB9jYBxRdkEPb3lfuIC4GdwO7hCV82pNB%2B2LoG4yiU1tbKAfJ0SBo%2BWCrM24AdUibRYYhehvi%2FPP3%2F%2Bb8Rn38aWypyMLDjjb0GOqUBvvjHzyg29ukyBp29BXEaMDYmiu%2B0kmqJwrIuFQLUI3EeiWzXuxJ61fQwFbGSpy28YU7oUTkgi1LXpb3EdgnZgo5Y1OM9MZrGMas8yhFR%2F4i1jyWauAO4jOCUkcIr5BBQZ1jy9Qg19vzxc%2BFs4M9Ytijv83XNfPp3E47vvm4dO%2BPJsdAH%2FXKpgrJUPq7rwXwqYofUiMaGRuQ6rHp3BABBFes1PQao&X-Amz-Signature=866737c0f81266cebc8d105f4cffa5fff66833cb90cac4a1505f1884c3a46c65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKNTJMQY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDicE0u7GcnzoLBKwYdoG1P3t1noj9mm%2F6iTJ5r1dRjAQIgKKPkq8GULn9dOqjSuKc8uGsAu5MfrEp5ACPvZfaC11gq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDP6szmtkZfPgiaVyxyrcAzwjojasGDiAHRijLmZxiYO3L%2BVE%2FD8WR5eu81QfRiBfp8uxh%2BHSkaiypncHvJml56P3WqzjpD0Oc0YMO%2F232QP%2BnpuKwp2OiwrNFJzUCypMIkLz%2BI3%2FmS0SiIewuKJc%2BtHnfuMyMkJudmsqpGW56qfvqQIZzfxzotyg%2BAk1OD8e9Vrmfql6ZN4%2BGMyjIPLyrhI861TXVEfhnIgdFKBn6Sy3%2BM1qA0wjOmDylZTSywAt1B5qNLtp%2B42R2gZvXUvcNDTowXeMId%2FI2CcK4C2zZ5i1dWJDaBgoKhr06CvTPvKw36%2F6%2FD1bVmEQTduBedt1wTMbj5frB4Dr2JdJb4PLJ4CWGFkGbhmLbMlH1XoPdkDaw7hm501wjGBJN%2BJm6J4dA5Vx3USv%2BM9cGBLcLqLYqFB0vnfGtlCHTza%2B2YERG2Gr0Ryc3skeg2NpJCxeuY1M77lRLJ2f9%2Bv1bnLbyREvGw82IaFzO7Gg8NWVkgnXd75TfblUpK6MSuNrz32wUsgn3jssdsM4EF4vDXW5jg417wU0WujfUv0BQf0HGR1q1KRzvT9PFd5VoMyz0iS5mfNq1dCRN3zOjhEf3C3werCGfc4kYFhTkQrqIBHugrSIaqE3AN5N4brj3fJswUUQMO%2BKjb0GOqUBxnHiOG62F5S1u3acC3J2OqruuupSzBDkLX8rLwLww8LyJsX68uOUEojoQ2dZfa3u0aChTqHzl8Mja%2BHtdugpNVr2%2BH7j1LB7h4xwEge%2FJc22VQKSrODx9m3mNLKvUfrJvHIGvLL22KMZX788CKj7oLhVu7OCoNuI1RgSJm8QX4kyb9RFlc5poWIZbnHDAqLD8fc3sb%2F7nBlJ75ujsoxLhh1qCL%2F7&X-Amz-Signature=a6e5754606225aa4d572f0bf90370fe57464d71f08e04ca4d039a662f3952c6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2UV2VD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFFyiIaSbhYHzELl%2BBG%2BkuUAaWKbykmcRIPwDz38gfvcAiEA4cu8FW%2FfiVhrhCti%2FIaL%2FZwDvNepEIgM%2Bccpkd0pOVcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNqjoequTcUuDq3yUyrcA5ngposfAMMSIfnWylHNvkGMGq8dDFcijj%2BBbP6yrZdLoe%2FfabvZAUs2jjP1X3VNSBAwxx0kUTUDyXMmH%2F8xaDK1WbQQDo%2FB2N7Rk0GpCPYob2heo08S4lQ5cRirNcQTe6Rn0Jv%2FxdZ8FvbvugxLQ6u3AiJWarfuzJEyjv0tdUbuyvhBOegpkgeJfCVWm008v8eUOFXYhc4NR3rWPqSW9N4n45amkau7j%2BMJZ2HhCx0nSVM4hoWk2WlZxI3xE23DxHZ9pWaJkU7GMFzzeiCqvLUufNRqiMoLX7azeA%2F75Gn2M26SktKbLaFqjeRzhyaWMyUK4nV%2FWpVDea606S%2F%2Fp4ey4%2BsI7fbaAuEYzuo%2FprTv2SRUpfcBtjWTVIMxpSusTeIRI3YAaPdlPnMNqOkJCJDnySHNS3aabormf29h1CGyfQ5o1SmDQc%2BiV7bf7qzXK7jtWjTISIhwON576pPONEKnD3KcICHecw1CguAdHbebrpLw9gM66Uz1YMOQN9TB8QrEKDK0LFzK4gS65ZY0byljEI%2B4f0Gwyc2Re%2BI6wWJ9cPCnbKiaLArNmlokD4qH8gzc63JufEvlAdeM1AyDbKQ011D%2BKkMPQxslm5%2FYgIxG90FtbP9J5sIT6zTmMLGLjb0GOqUBkeVR0xHHtvnacg5kZ7qg5zE63AAD1JCvFyhh9Rypo%2FobTD1ex4mcUqxbTlqY%2FVV3mmoIIkFJnowFXZRMiW29rnzrlsW9ibSny%2BAGpHjBWi8wY0FuHO2t0DFa77TMYNLyj2aCun%2F1v64TYJi2ymfZQZdg%2BlrzTBqX5%2F8LnUw2%2F1xwtttW68ZlB8wWOJ6gsuT55OaeVbodmpv0QgWSOmZOfCctF8t%2F&X-Amz-Signature=d41141f5b98d34c7f2a5f9c286f1dafee564ab753ea9028db101f92d31904728&X-Amz-SignedHeaders=host&x-id=GetObject)
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