

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=b1634b0b7cc207d5ac4e0e0069a8b3976a5b2016528e6bc36363237176c7bc1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=ddf55019da7f14687a1c46f59cef1c5c5e4a02df6b652c5a6b0f51cd911d60a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=0c1d5f48f82ce318ccae957b09840f52f25751d082d9178238763a9bf79b2be4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=ad5a880a8ff0d97d74de1c04e160c00ad261c8464f9cbe0d262af167d521a544&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=959b0d5cb5401fa65b469e09f1d92bf22ac57be82e4e176a2608e9cf1501e7d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=7eb404acd8ff4ba6565d4db464332057a472effbdcebbfff65451f03e3f6f138&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=8b3bfe099e45e99e5d9aff9b916dffc9841ef7ba410e411dfc9c4ca0a143da32&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=f627a5c36db656d14ad0ddf31596131ccf0ccbc502aa6aa2e8d45cdb7364214b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=7df45c442ef59c7a04037aa40210b89ed9b2e4500e5a64121811d40cdcf57ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXGWD7V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIB5bLDOrRoZcxNsGw%2B20enY%2F8cE5ujRQbalazI2akuoKAiEAnzASyh75r8DiegnWqzC3BbyaRw3jBpTDgdeo1FVcEfoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDOIpWbbiS2N97kEgWSrcAzMd2Z3p73T3KidTxSi2qquL3lRpUPDBQsEq2aCqQNqvMRWOkLZjk74nWFDk%2BgTPNuRVFbrzYaixHQfdqEU4xxOZbnqh9vXKVP0Ol5xS%2FKA5GQ771mt0tJtnuEQN9yrl%2BTOxB67LFhmaBUgaACcIo9PQQ%2F0xBYSNDLy80Q0imo1mm3riHAqFUuuLDNuao7wFXsyXnnWQK34GIdVdYVz7Mg%2BOzrg9Fwm6In2gDtG1XdSWkOMm8iWxxcCjF84iw40ivKLJNd6Gdpp1Xl37ifTK7YuK6SpDG10hrL9fJiyqaNuknK8YQv7OYsq8GMLrl%2BeY3OkkkH4ViDzeBacwSafQ5bOfRQ4hmgUnK3Xg%2FePXmD90EfqKdi%2Fi9pQ0hgdnFSgZxeX8Q0K%2FgZQZgvVIyTD7AWg6bBibqsSgB88lFtj2rJbMcm1zDAjlCFV2qoNdsoMq%2Fi%2FuJx%2F9o2HyJlNbLpUNRdEEROP88Qi705m3lQbEivjB0bv7z0s%2B3PQDUaUHi1B%2BoXPiIvjyJLSlWEFnsqjTQjshRTUecfkUM4hRk37R8hR3Z%2Fn5QffbNjzk14wBJkJXuZC2Q4Wj0eK5Fsu2y7s6bK8mjHgQ7%2Bg1Ki0um0cPsFxukGsapVbXCkSeYlJqMPq8ib0GOqUBmQV0BBixKPifNGWG17%2BDuFp7bV60UmHFpoEf42mNbmAStYzsGhYuRh9o70neySOtDCvmR9kzTLwdmAL4Im4ebIEw9QMKmjHfjul6NBfZ12P2vFo28omTMy2bEG%2FJnYSjpiBVn1ZDwiFF0hdjQBz3h9Io8xznWJ9QEGv1ugqxOGr8G%2BB5Z54oXibMl2ERkrffbM8h7gYspM3pFgad%2Fi02dFtwDFxV&X-Amz-Signature=c6a8560b5090958ffe3253f1f334b4eb5197865ca72e4c444e93ee023ec37fb5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXGWD7V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIB5bLDOrRoZcxNsGw%2B20enY%2F8cE5ujRQbalazI2akuoKAiEAnzASyh75r8DiegnWqzC3BbyaRw3jBpTDgdeo1FVcEfoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDOIpWbbiS2N97kEgWSrcAzMd2Z3p73T3KidTxSi2qquL3lRpUPDBQsEq2aCqQNqvMRWOkLZjk74nWFDk%2BgTPNuRVFbrzYaixHQfdqEU4xxOZbnqh9vXKVP0Ol5xS%2FKA5GQ771mt0tJtnuEQN9yrl%2BTOxB67LFhmaBUgaACcIo9PQQ%2F0xBYSNDLy80Q0imo1mm3riHAqFUuuLDNuao7wFXsyXnnWQK34GIdVdYVz7Mg%2BOzrg9Fwm6In2gDtG1XdSWkOMm8iWxxcCjF84iw40ivKLJNd6Gdpp1Xl37ifTK7YuK6SpDG10hrL9fJiyqaNuknK8YQv7OYsq8GMLrl%2BeY3OkkkH4ViDzeBacwSafQ5bOfRQ4hmgUnK3Xg%2FePXmD90EfqKdi%2Fi9pQ0hgdnFSgZxeX8Q0K%2FgZQZgvVIyTD7AWg6bBibqsSgB88lFtj2rJbMcm1zDAjlCFV2qoNdsoMq%2Fi%2FuJx%2F9o2HyJlNbLpUNRdEEROP88Qi705m3lQbEivjB0bv7z0s%2B3PQDUaUHi1B%2BoXPiIvjyJLSlWEFnsqjTQjshRTUecfkUM4hRk37R8hR3Z%2Fn5QffbNjzk14wBJkJXuZC2Q4Wj0eK5Fsu2y7s6bK8mjHgQ7%2Bg1Ki0um0cPsFxukGsapVbXCkSeYlJqMPq8ib0GOqUBmQV0BBixKPifNGWG17%2BDuFp7bV60UmHFpoEf42mNbmAStYzsGhYuRh9o70neySOtDCvmR9kzTLwdmAL4Im4ebIEw9QMKmjHfjul6NBfZ12P2vFo28omTMy2bEG%2FJnYSjpiBVn1ZDwiFF0hdjQBz3h9Io8xznWJ9QEGv1ugqxOGr8G%2BB5Z54oXibMl2ERkrffbM8h7gYspM3pFgad%2Fi02dFtwDFxV&X-Amz-Signature=84ca617230af521f16203dc439a3f90e8daf75a129918358f08d0258de0991ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXGWD7V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIB5bLDOrRoZcxNsGw%2B20enY%2F8cE5ujRQbalazI2akuoKAiEAnzASyh75r8DiegnWqzC3BbyaRw3jBpTDgdeo1FVcEfoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDOIpWbbiS2N97kEgWSrcAzMd2Z3p73T3KidTxSi2qquL3lRpUPDBQsEq2aCqQNqvMRWOkLZjk74nWFDk%2BgTPNuRVFbrzYaixHQfdqEU4xxOZbnqh9vXKVP0Ol5xS%2FKA5GQ771mt0tJtnuEQN9yrl%2BTOxB67LFhmaBUgaACcIo9PQQ%2F0xBYSNDLy80Q0imo1mm3riHAqFUuuLDNuao7wFXsyXnnWQK34GIdVdYVz7Mg%2BOzrg9Fwm6In2gDtG1XdSWkOMm8iWxxcCjF84iw40ivKLJNd6Gdpp1Xl37ifTK7YuK6SpDG10hrL9fJiyqaNuknK8YQv7OYsq8GMLrl%2BeY3OkkkH4ViDzeBacwSafQ5bOfRQ4hmgUnK3Xg%2FePXmD90EfqKdi%2Fi9pQ0hgdnFSgZxeX8Q0K%2FgZQZgvVIyTD7AWg6bBibqsSgB88lFtj2rJbMcm1zDAjlCFV2qoNdsoMq%2Fi%2FuJx%2F9o2HyJlNbLpUNRdEEROP88Qi705m3lQbEivjB0bv7z0s%2B3PQDUaUHi1B%2BoXPiIvjyJLSlWEFnsqjTQjshRTUecfkUM4hRk37R8hR3Z%2Fn5QffbNjzk14wBJkJXuZC2Q4Wj0eK5Fsu2y7s6bK8mjHgQ7%2Bg1Ki0um0cPsFxukGsapVbXCkSeYlJqMPq8ib0GOqUBmQV0BBixKPifNGWG17%2BDuFp7bV60UmHFpoEf42mNbmAStYzsGhYuRh9o70neySOtDCvmR9kzTLwdmAL4Im4ebIEw9QMKmjHfjul6NBfZ12P2vFo28omTMy2bEG%2FJnYSjpiBVn1ZDwiFF0hdjQBz3h9Io8xznWJ9QEGv1ugqxOGr8G%2BB5Z54oXibMl2ERkrffbM8h7gYspM3pFgad%2Fi02dFtwDFxV&X-Amz-Signature=2fa5b219efa0481f1eaf8737e6e317a3cc79bd39e51e8e2c261177190493bcac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=1b9b1220ff1d455d5f07e43a1cc18e2feb01bcf4de73287892115b3662a537df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=7d50056259a8ba50cd35109d64f1b329fb0d4570525144e0c8b4c737572892b9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=8bb52b6d0dd2fbd427f8de7bb7bad4dac0a7ddd468529d926def7656aa7e588f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=5b255346bf3d7cb5ab8e0810f02211942ab821ff83e7db3776b866f543625be4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=7ec37ff189c140ab9f89902bf3ae1d380c3a18fc31f47dd2978b24791de353d3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UMZKX2J%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQDgEzvrsk60Y5M7aMVdvIX2pYgMfQE7AEjXqB1ABV1%2FuQIgU76fLNbf8vRWK4sUVzL41b5w7oqaFfi%2FsVPrI%2FwqAtUq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDENkqADjfqhBUOP9oCrcAw2MBk%2FIHymvdpUqwmGWZNbpkrHqXjryH%2F4O%2Bfd%2F5XkP%2Fs0pRKqag5TFv1w7gGZrLYDnW6Spy5yvx9zOc6uuP9p3gWmzVlrjO%2B12lbYldjRCOVPUgdaLTwnitbu8vNgYegmw4Moz%2FctJkvgdU%2FNuxOYLhrdx3c9dPX7d7m3AxDXYRYUseTpbUkSb8jHR%2FgPmNKaNyc4XEQSDzf0qqiKpfQ%2FZ%2FWXVNWB6Q9g1%2FRmxgvwVOH6uB13vqsEmWV2ifIYpU0ekSW2PuIFEl6Hfg6kLICKAB%2FD7kBF4t3zS0oW88V%2FlEvsL%2BG0PLNicLZ0R7dZzt72dcH3waspyMj9WC4XK90kxBypbNieuxHbAYpyBjRnhKNiKDkUSCMsF29vUYsyRvrgAuYL9gw9DHV1xemCuPOHttLd6CaMehNEfHWNKJoeiIHMAfESChriB98e1WeIiUDLvtYDcHaqjX0Gfa1Ptty7tEVe6FFGZQiC9G3MfNBwPkFHE3nOV45RWZxvxuUpagVx%2BKv3wj8QkheZG57OlF%2Bk253q1JXqQ2x8%2BGUxrkkree5HMQcKYncBe2LRcf%2FsMDdGifZxh1JZQEF%2B9ubmfIeAQCn9230%2B1HMAu5vCIUQCQ%2FVZXetj94%2FIzvGTSMKW9ib0GOqUBh%2BLhEX44fjqqlvxRFIRffjuoHgGVfsR%2F7BKQY0sOJefzG2hL8I5k5bPQZYPTbZQTm97JcqslyI3PDUhHAXY3pqfLmwwk3bWBjIbhruhBE44ojCK9dic26dvgzDavYxKVzM6fj9Pj%2FV80Y779KZXjWREqYJPcEQLvLWjzZMx2N8itzFSdv%2Bqi9I2cI%2Fu5V6IVt%2FU%2BzgwSQjYoQwjRctKMoO54u8r%2B&X-Amz-Signature=15526564a91ae06a626b08a162a947bc532c9433382ad40b91848dba78f65bfe&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URP4Y3BS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCgr4o1iZeS4EnDyjlvsu5%2BD5OsRJ2I0yqqT8yrl31VYwIgechU7jTB4SoQ%2FbqfnTNozNWUGVtaBgsfF6aIAjYD7%2B8q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDLLrseRld%2BhDCYqQkCrcA1EPGGLa5GbWMpaAXd8xI1yHUY7G7GaqEGJhFoVQmOJDVf0pm%2FJunjwo9G8k2MZp7OBdmG7EJHjONqePU%2BWci%2BJ2Hu1FwqR1rzWgivSA8xCtgoJYmMUEt2x71MjZYhqbe5GAm7dRZrKe0yxK2vYEB1H9zw%2Fww0uT4V1kKykBY9zXirD%2FUSfwMp5VcIWCz3YNh0jmXaSWZw8opgV%2FrNOstkCzR1aFK8lc0R%2FN16kM15d3OgNOhmjydLQDELJLMyH60l1orwc0vADqgUxbo5fm7QqERC%2Fmaj5TjF1p0lJRgwmXhQt5Wh%2Fh2nBjnKYJIdMzM9Bw%2FTD%2FJdpiby%2Fw3Z9IVkE6LolmYHr6inV2vxcvlJGTanuj2yMaw4lhCPqxKD1qIgGEMNEDh6l6ffGcSMmf3wetTX7EtizPLVbHFI7CxQjmaIgxh%2FhobXQvMe8FMRgjPFiJAGT9oZrTFYuvVjikX5fmMPC8FqGFXi3ancK8tTl9Eg4t8aiq9faM7kZD%2BJO9ddioIN28H5sUrd4mIJ%2F26DzCJxTbeKCPjEjGt96y8iQZ7EHL%2BBcrqykXNYN%2FIuzGUOaaP9rBi%2FlwiLyRo3cFl3RtLEA9uXQqHGPcZy0%2Byg4n4OEmeGa2UONmaaetMKS9ib0GOqUBjunQRU5p%2Fkm%2BK0DQhESzGXhIYXDJZJHYINk%2Br7VXSMGw8h7l%2BdR2dPOwV3UaVDkGqwR8m%2BYKFGUcy%2FiHdp5qw%2FVFf3qEDq84y2MCUJByi%2BvnzeMca4fx3N2BWj0veWitV%2BAak%2BNqx6%2BibCp0WA%2BUSJRaZ9%2FF3nR311I7JkjdD4JYk5ghqAmHZrVIO%2BOdV8me7BbFRBCi14KmTOC9qgxuWZwWt%2FtO&X-Amz-Signature=c8f818b9b75b3f6a884420a5ad386381a2371583690b21e2c683efc43d6f2bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URP4Y3BS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCgr4o1iZeS4EnDyjlvsu5%2BD5OsRJ2I0yqqT8yrl31VYwIgechU7jTB4SoQ%2FbqfnTNozNWUGVtaBgsfF6aIAjYD7%2B8q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDLLrseRld%2BhDCYqQkCrcA1EPGGLa5GbWMpaAXd8xI1yHUY7G7GaqEGJhFoVQmOJDVf0pm%2FJunjwo9G8k2MZp7OBdmG7EJHjONqePU%2BWci%2BJ2Hu1FwqR1rzWgivSA8xCtgoJYmMUEt2x71MjZYhqbe5GAm7dRZrKe0yxK2vYEB1H9zw%2Fww0uT4V1kKykBY9zXirD%2FUSfwMp5VcIWCz3YNh0jmXaSWZw8opgV%2FrNOstkCzR1aFK8lc0R%2FN16kM15d3OgNOhmjydLQDELJLMyH60l1orwc0vADqgUxbo5fm7QqERC%2Fmaj5TjF1p0lJRgwmXhQt5Wh%2Fh2nBjnKYJIdMzM9Bw%2FTD%2FJdpiby%2Fw3Z9IVkE6LolmYHr6inV2vxcvlJGTanuj2yMaw4lhCPqxKD1qIgGEMNEDh6l6ffGcSMmf3wetTX7EtizPLVbHFI7CxQjmaIgxh%2FhobXQvMe8FMRgjPFiJAGT9oZrTFYuvVjikX5fmMPC8FqGFXi3ancK8tTl9Eg4t8aiq9faM7kZD%2BJO9ddioIN28H5sUrd4mIJ%2F26DzCJxTbeKCPjEjGt96y8iQZ7EHL%2BBcrqykXNYN%2FIuzGUOaaP9rBi%2FlwiLyRo3cFl3RtLEA9uXQqHGPcZy0%2Byg4n4OEmeGa2UONmaaetMKS9ib0GOqUBjunQRU5p%2Fkm%2BK0DQhESzGXhIYXDJZJHYINk%2Br7VXSMGw8h7l%2BdR2dPOwV3UaVDkGqwR8m%2BYKFGUcy%2FiHdp5qw%2FVFf3qEDq84y2MCUJByi%2BvnzeMca4fx3N2BWj0veWitV%2BAak%2BNqx6%2BibCp0WA%2BUSJRaZ9%2FF3nR311I7JkjdD4JYk5ghqAmHZrVIO%2BOdV8me7BbFRBCi14KmTOC9qgxuWZwWt%2FtO&X-Amz-Signature=3221b726b7f5f5e957573fa7cde9a09f21951d2f955e59a3b22d498c475e627c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNL57EWK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIGQlOIQ66gcLYrkj10DkNK2tSavg2ZGVQmTWcQ5Fh1xlAiBr464zxqdHC1IyEEeezEQ3GXRsEo9k4Z1OoHaKf910HSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMqME%2FEoaAbtNE9JmBKtwDlbe0cUbFdJow2RyhlPIphHXXnmgQCp1Wkalbdn0I340P2fYghsqpv6PTJuSLg8eUk74GmbNe%2BK%2Fezsmv7IvMdbykN%2BqRPARB0ht2Qptz8ZG9MDSP7uyKyF8HoXua3PamM38LBtr8DFbgBvQMej8ccwxstkysAROwwAn0tcI2KkAfXd15Cq9lRjTzHkKNmue0R4TMv6r%2F8RdTzbCBmTFA96bsj0fRrbx2pn%2BwcgUUCF%2FLkjMlS8WUQpydcubd9%2BMzix1Kz2%2FO1iFniiSf0Sqe6t5fAq1P9inqfx5OvfG7fnz4cxxRzrdke7ftcwQhVzvRmDEy1RFXEyWKSWQaKWdqKJrzma8yduYpxkYfg2i4idDGhJbQ9RiHp%2Fzd%2FhMMosepb%2FbrHGLZLlnk9fL2SCtftVVW8bZerwZ1sIjsWF8xRRW5u4BIqzUcEpW2tmDu75mQKrxU7wKgpjjKvFYpRrfgWgYg8lJY5Ndhl3zQwxwKtqOCU2R3Co4gzHLHwtDW%2F%2FfrVs7to9MmRmjLU%2FXaSQaNVcmVLhs94Ynlalti3Y8eevEuVsfLOk20tyxBOOXLHScL2lLpATW1cEn3yEa3KEKTpKjFeokVlYBRCGIb55pl5LlygNUDQfibTxIOpH8wur2JvQY6pgExUcs28W44L83Ci5K2277Xa6v1gCAsR40w4sAKTLTB8K3zmRkO4D5I6d8bk1x4BgeurFTpAu8lhnjwP4QsDnOoE5js7saEd921MGjGeh7cjC%2Fl6VAzRHCjwGuACW6BajvAi37Ss4y0HEuaLUcTK0JErTIXwU4nFb3eErGrrma1RPKvcwUc1jS3WdusFtjl%2BH2dSGeTQr3aVFmkfvL1ewm39kEQbTPv&X-Amz-Signature=b459073455de3d8cf958b2136e3459b41c2744a73d314c57fcc6cf77267c9976&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WZ33UF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQCwKvfRYT2SAERPG0Dh2M5p9TazaIzq%2BtjsJ%2FIYo8iUpwIhAN%2FthrSo2gsG3GV5t7CW4KoCsQ4ZSFzTKcoCM%2FxExCWbKv8DCDQQABoMNjM3NDIzMTgzODA1Igyrh1VpOYyu9C1THPkq3APNW7Ky4NlnqUsU%2BCee1rKUBJvMa1OpT56BjNqJc862SiC0aMF1VJVN39PD83L8DGLKbcZTq%2BrqJMUni7%2BMkfn9uE24J%2FCIKZUM1eJT9W9zD9KCvvQCdxfm9LbDhOO3VR7ivfnJLnAOntF9H6skLhSH45bXrvVbX97HHyr7ucBbYWqx%2B%2BxCcKPX95sxJXLbk4qwYZR0aDGDAjnSuEwCkAmgW3yBtbZF5dchf3Xd2pPnYbiAlvyaYYLh5FyW3KD1GfDeUx2SPKEG5ql4TSD8OACQUoGCID%2B9SfObL%2B%2FIX%2FNZrdHbH3Y%2F1T5ltd8Fql5e%2FDb0T56a88yjVj%2Bx%2FhodY%2FD8V28wqjf60Ov7eng80UuzFYe8JdbqejTvBnb22L46%2FHiqRXC7cX2PH%2Fc%2FPZrqABey62ZqSOsunHrJJQ%2FG5cWozKQ3IXTxSkAb1E2n%2Ba%2Fq68qND3U0K0bczflyU6%2FD%2FcyVBxNXrXOm0ZZfOrPehPkjyf1FNv%2BAU23zf9KmuJKkaGprQ4osJ2x8elEv1dZn1b9b1cS2crdXjXVwadcNDdfYuKvbNh%2BdBBLQA4fUYdsx%2FnrOwOJm3B2frSTlVl6Ptv%2B4arRbDWnLVQWvr6mZ7eP%2FVUrHNlFk71OxiMPCLjCSvYm9BjqkAYJ%2F%2FqK1FYOhIr3cIbdtjdgVAMN%2FR%2FwCt75KvG7Wi7osgRjdWZtg4uy0nk6aH6SgFB9TzBuylzY4A2O01I4dmXdeodcxS%2Fxik7SPdU%2BJ3R0O6N%2FWOs%2BoWQ%2BcEGu9ZGhZyPooCXerKA2mV7d%2FigscJMlDjjiHZmqA%2FHFE0i5kzfyhQI17UHnxrPudvThY%2FJEBolQezdH2Pr0mGyzOgm6RWgwFQB0%2F&X-Amz-Signature=6707740d4c7a95208aa8091681765e59bc9164b582594f14393c524120668dc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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