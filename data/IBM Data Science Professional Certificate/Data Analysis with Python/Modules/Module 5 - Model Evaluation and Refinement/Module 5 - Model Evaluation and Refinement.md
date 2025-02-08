

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=375bf89d35f7ab8d5b7aeba3e0d766f1860976968fed38ccf9aa7ec34ffa1541&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=1bc918944c8b042e56f28fa40efb1fe23edd1f4d1fa7dd044510f65061fc6235&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=0587331c1dbaefe0bf0735f1f338047d0f27b7dcf26b86426469d6aaaf84aa2a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=766d3c5b698f5e920b0c8a051239ce77a16c36ec593a01822a75249a823bc208&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=1bb7c6de68db5b96bbc78c18145f614948b192fcef3b47a250d0c988c95abd49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=55a509ed05b7e25c9ff92cce69cc11223c7b09750b0df6501575caca6e912fb5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=865cd3bab5e2caeb7a373b6da913f53c43390a8d4a31b1b71b01064af0554bf6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=0edf2e0a8bfc41bf6ff74236ee25b420980dcf30d3fea953cac5772949487a05&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=86e8402bf3a20179f7d832c143efef61b2be4ab9d5b774ca74f4e4f10852022a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q67X7S5L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFzLn7s0I9NcV24moUtHV%2FMCisijBuneXcPEr8BG9QOEAiAdHbI0hZ2qKSVdBys5FWeObICymOWs9yht94jgy7MfGCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtNa85mz067yxfRnPKtwDx7JKPNqy0fOT9re3HgqfMeZs1H00KPYUBOTeHgMsGKwGEkbRyFxHc73ohhAU0mKVUQww3EMDJrap8w4NVwA4w9Qz%2BVZDsNlFhkFf9QIXX4BOlhBnuwJbT2%2FJ45BaBClJvfHY28diPu%2BWqQfAZFPk05TF%2B0NDERppluUZZxYSHlP1%2BBHLmCmzQwW%2F4L0NQuPNKtQNRUX7EGEsJEnIitnPlCVSNZ%2FO0qxS3E4vX43HG5w5TxvNyRAbtc8ZpttAKW%2BWQ0xgyBaP3yNxv%2F4VszCBd4TAGRjCycYfaHuhoe437%2FU%2BoR%2BoIw1UPz9wGXjHYRlPpgHWZrV1Uu3k6L%2BoD4N7aYaXhi45KEBLi2PjVbMc6J2pBLYdBk4aSpECzy87cdjqCJ5ZE%2B%2BT6DRYE2IZwKCwghB44fuBJ6Z8wc4IFlxqjpOMXk6GGgxfHAlL1z0PpmU5SBGwSX6ePpDq6CJcQVva2321APa0C20klNgXnErDIEH0ZnyPSPA6oE1F91%2FmPQpCvb2U1svFo0uzzvOoiRAZlE5nHr8RgBRqpVY5rVVikFkq4bLYRKkqLCC0M%2FI52BcRssnyjxnFdLXDzzCywYqE%2F9VKyRXueRoFB%2F%2F2Mjd1cIb8GCGX%2BCcQ18RTc9gw75WbvQY6pgGAz4%2BsdJc%2BPbl36gRIGX9VPC6wktr8B8KldwjQBT3w3UnpEZ8gzqFp5eFlWMJUcCMM5WIZebghFNhS87C5GDW1opx9y6gklK37qK8T7UkNMamTi7x5A1Ekj4EaLh0KTYz4zqPhxfDVRVtiigQQdZAc7jO4v6E0jk6Psqb1M%2BiyYqZxpiaIJTrWHgwDhhgsTsdf9M7DpjiFb8KA0Ojo7rING5IQpGBg&X-Amz-Signature=16d7f9da9290a45eb1436b1bf9f9c5ae68e21e4930f89610d016dbceca86fa80&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q67X7S5L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFzLn7s0I9NcV24moUtHV%2FMCisijBuneXcPEr8BG9QOEAiAdHbI0hZ2qKSVdBys5FWeObICymOWs9yht94jgy7MfGCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtNa85mz067yxfRnPKtwDx7JKPNqy0fOT9re3HgqfMeZs1H00KPYUBOTeHgMsGKwGEkbRyFxHc73ohhAU0mKVUQww3EMDJrap8w4NVwA4w9Qz%2BVZDsNlFhkFf9QIXX4BOlhBnuwJbT2%2FJ45BaBClJvfHY28diPu%2BWqQfAZFPk05TF%2B0NDERppluUZZxYSHlP1%2BBHLmCmzQwW%2F4L0NQuPNKtQNRUX7EGEsJEnIitnPlCVSNZ%2FO0qxS3E4vX43HG5w5TxvNyRAbtc8ZpttAKW%2BWQ0xgyBaP3yNxv%2F4VszCBd4TAGRjCycYfaHuhoe437%2FU%2BoR%2BoIw1UPz9wGXjHYRlPpgHWZrV1Uu3k6L%2BoD4N7aYaXhi45KEBLi2PjVbMc6J2pBLYdBk4aSpECzy87cdjqCJ5ZE%2B%2BT6DRYE2IZwKCwghB44fuBJ6Z8wc4IFlxqjpOMXk6GGgxfHAlL1z0PpmU5SBGwSX6ePpDq6CJcQVva2321APa0C20klNgXnErDIEH0ZnyPSPA6oE1F91%2FmPQpCvb2U1svFo0uzzvOoiRAZlE5nHr8RgBRqpVY5rVVikFkq4bLYRKkqLCC0M%2FI52BcRssnyjxnFdLXDzzCywYqE%2F9VKyRXueRoFB%2F%2F2Mjd1cIb8GCGX%2BCcQ18RTc9gw75WbvQY6pgGAz4%2BsdJc%2BPbl36gRIGX9VPC6wktr8B8KldwjQBT3w3UnpEZ8gzqFp5eFlWMJUcCMM5WIZebghFNhS87C5GDW1opx9y6gklK37qK8T7UkNMamTi7x5A1Ekj4EaLh0KTYz4zqPhxfDVRVtiigQQdZAc7jO4v6E0jk6Psqb1M%2BiyYqZxpiaIJTrWHgwDhhgsTsdf9M7DpjiFb8KA0Ojo7rING5IQpGBg&X-Amz-Signature=d4e55764798c0433b02c2010fd469f63afbde881e9fe4df25677451feb2d6b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q67X7S5L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFzLn7s0I9NcV24moUtHV%2FMCisijBuneXcPEr8BG9QOEAiAdHbI0hZ2qKSVdBys5FWeObICymOWs9yht94jgy7MfGCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtNa85mz067yxfRnPKtwDx7JKPNqy0fOT9re3HgqfMeZs1H00KPYUBOTeHgMsGKwGEkbRyFxHc73ohhAU0mKVUQww3EMDJrap8w4NVwA4w9Qz%2BVZDsNlFhkFf9QIXX4BOlhBnuwJbT2%2FJ45BaBClJvfHY28diPu%2BWqQfAZFPk05TF%2B0NDERppluUZZxYSHlP1%2BBHLmCmzQwW%2F4L0NQuPNKtQNRUX7EGEsJEnIitnPlCVSNZ%2FO0qxS3E4vX43HG5w5TxvNyRAbtc8ZpttAKW%2BWQ0xgyBaP3yNxv%2F4VszCBd4TAGRjCycYfaHuhoe437%2FU%2BoR%2BoIw1UPz9wGXjHYRlPpgHWZrV1Uu3k6L%2BoD4N7aYaXhi45KEBLi2PjVbMc6J2pBLYdBk4aSpECzy87cdjqCJ5ZE%2B%2BT6DRYE2IZwKCwghB44fuBJ6Z8wc4IFlxqjpOMXk6GGgxfHAlL1z0PpmU5SBGwSX6ePpDq6CJcQVva2321APa0C20klNgXnErDIEH0ZnyPSPA6oE1F91%2FmPQpCvb2U1svFo0uzzvOoiRAZlE5nHr8RgBRqpVY5rVVikFkq4bLYRKkqLCC0M%2FI52BcRssnyjxnFdLXDzzCywYqE%2F9VKyRXueRoFB%2F%2F2Mjd1cIb8GCGX%2BCcQ18RTc9gw75WbvQY6pgGAz4%2BsdJc%2BPbl36gRIGX9VPC6wktr8B8KldwjQBT3w3UnpEZ8gzqFp5eFlWMJUcCMM5WIZebghFNhS87C5GDW1opx9y6gklK37qK8T7UkNMamTi7x5A1Ekj4EaLh0KTYz4zqPhxfDVRVtiigQQdZAc7jO4v6E0jk6Psqb1M%2BiyYqZxpiaIJTrWHgwDhhgsTsdf9M7DpjiFb8KA0Ojo7rING5IQpGBg&X-Amz-Signature=8b904683558e7f69809b9a881246dff7bc7d437aaf99cf43d597cfd03dff2e64&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=0c0459556d0ec1dbb61a14c5973be60c9727f449510a5b6f06976b8505634d9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=659d5cb5fec3af009bb40717d4d6d6af18db768ef381cff1571094b3a1476653&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=8a6e2984092f963d6533c7893c08d5d18255e8fc395beff3aaca31762a4bd914&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=faf37f63b738d8af6f0ca2ca749e117e356bf369e3cbd37c7997e2b823118b5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=b8b40dc63ebefbce0b3f295c75273dfecb30a1021d050962b53fb1f240b1b22a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCKKVT2B%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIDbJ6ysywcsjmiml9ZiJ1FhGB6p4IxRNBCJ7d4Jo%2FN4xAiEA%2F6omS8lrM0UCwN4%2FqH4m1AuDi0eYhZ2M79fy%2F5GVA74qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHG3%2FKmzLWs2VZqWpSrcA47i2qaozCjp7ju1tJbKk%2FuI5EKBq%2FYWnZXDpkm9R2A3qsBAxN4rykoZaJX%2FavVtRpLZf7h%2BFLvGp3NLu3aYw3MO8SeGOcvs8WzLptTzf%2F1io%2B4nGXE5iTFDtGX7ScXDqtiASkknZan4c6BzKO4iU5kyaBinqasD%2F8dGL5Hm%2BIO6JTSYcFcUahjkuYYm9lsEhjDE4OzOofCWZyQM7lbGwXIgwSiggMaPNadPUTLq6e9GlzUDVS%2BE8wri71pMwOVGQdxz7b3zDjhVdkuNsHkyGX21%2BzZcJebH3CoJ9nMJWaqv%2FqmHP80EL4QiQqcTfJ1kXzADZqutoQNFg8X0wc2wATYKwBIRVg4L0xxX421F0hT17hAR7IDnhVxdCP%2F5FOn3CtKIQZa4mRzrV0zRKZI6w4%2BVkRqBWYyhwMOBcQzjOLjp9PJkf5izhKdgKAzfkggouH%2Bw7%2F1SSnW8%2BfoGkhyBNSzPYfOys1SPrZvEbxErBFqoSJX8d9t1sSlSqMCrdW2wk35iki5EID7PMedR9bCeFNv86jKUn8J89Cttwru9qw55qlNs3B%2F0LC626uriAdlwXCuHNlsmA9WQE4LHASPE%2BalMKCkd5Eqt6ZZ%2FG3CIQVmvFXvNrlFrtAgwu7VuMI%2BWm70GOqUB9XaghBeYByDBPD6PzGYOpk7eDVLXqWj%2FZ3pYyYfpbl8Ro3I7oc0nQZzzutmIvdJkpJlH0SEeQ2hru9v6yCa5L0V9nE1rINYvXAbIhGzJer%2BE5BDuarJz2ByvvhGx8A%2B8x3OnP5T3yV9khdMvraSG7OVtoLavCKzFGCWRgSjWS7UrMsfZJpvga8LSUQgNI%2FyCnvCsb6tLVZ7QYBSkwp9s%2BdlEqUb%2F&X-Amz-Signature=d8152dd3117e1f903eee33c9114c79dd66389c53e8cdef14dc88d5ba40fe6e71&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXNV3NPZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDLb9pQie0dPCJ5WfrstlHakah3F8Zuz%2B5PXkrbJfTrpgIgIX9iOt3YqKtLMwOinyszyCsxNx%2F%2FxC1znCpgUUJSgisqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDw9vNHG20RJ2VYgSrcAxV0Lt9EhFarCoZEeawq8pUbIzzfdoSs8DZPTa6SIQV2ixF%2F20MrnLPeQYBntogDMS6NNFScJAt6qNGVNx%2BYzQowHdDOw3jBQ45NJvtlj3dosRnO7vuoLtXPskNNlFSMDLJEYeUn2WbxdxSPV5GmadOByKhxca3O2kqNHu7mx6hvQRJRCZ2u3JxZNbefj5kpMqOyimLIxsZs9xSn%2B%2BEaTjhDewlFMIh9ODgVpAa7%2BLdlJKFOSXO%2BucBMojN7nl2ZvylganuLGUkLlIAbll8PZF0fxuNfINinP4bgt6U2XTUpq7Wg0uwLiJzgrx9yR7Xd54X8%2BJ3niRmlpbk%2Bi54NdvNLmMKUAOePrfezIsoRuv3Z8nzkwigmWoTnCGnuuSQ%2FJPLbhAs0WXlh9kd83FiBD4Y2d40K5CluvgbkcTwM5o%2BzldAM2I3kefjRftGsmBdENK2mV0b5G8WVQFFDEJXyzhGTO3yY4RJGCPQLLyF9sqn5eGvrH0nA3b4bfkb3fRvuImnSrFOWsrffGoLSXOVGphnYHcR%2FJrvnKF3HA81QUdcnXoDIGy3Oj6BeOJwJBSP2qSxxsnGtLQcJr6z0bJbEEHSszSKouJYwdOqCyZv1c2l9J7o3%2FolNxkUJ11rfMI6Wm70GOqUBtwWyuYX0IUORmnApAkZ%2BRm%2FSZRoLO%2FoHtd4iMZ9h%2Fy1hVhK0ffz8RWG0OvI%2BKknS7Hq8b8%2FBMG8qeS%2FsZAc071PksqFFNW2BudoxrAS55C4DagzRJuE25cYMPpwA%2Fj3jPW8IsBS%2B4XYGvxIdhZq7sBA%2FNRyRqIwW51ZJNGJ7Rb9E%2FhENRom1f7j0JzpzEIrAkXs6O4lA359xFVKdQvqqcbuX22d0&X-Amz-Signature=9c5b993c03adc7be337cfb97c0ebd0b29fb846c4858285a01d22819129c9beb2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXNV3NPZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDLb9pQie0dPCJ5WfrstlHakah3F8Zuz%2B5PXkrbJfTrpgIgIX9iOt3YqKtLMwOinyszyCsxNx%2F%2FxC1znCpgUUJSgisqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDw9vNHG20RJ2VYgSrcAxV0Lt9EhFarCoZEeawq8pUbIzzfdoSs8DZPTa6SIQV2ixF%2F20MrnLPeQYBntogDMS6NNFScJAt6qNGVNx%2BYzQowHdDOw3jBQ45NJvtlj3dosRnO7vuoLtXPskNNlFSMDLJEYeUn2WbxdxSPV5GmadOByKhxca3O2kqNHu7mx6hvQRJRCZ2u3JxZNbefj5kpMqOyimLIxsZs9xSn%2B%2BEaTjhDewlFMIh9ODgVpAa7%2BLdlJKFOSXO%2BucBMojN7nl2ZvylganuLGUkLlIAbll8PZF0fxuNfINinP4bgt6U2XTUpq7Wg0uwLiJzgrx9yR7Xd54X8%2BJ3niRmlpbk%2Bi54NdvNLmMKUAOePrfezIsoRuv3Z8nzkwigmWoTnCGnuuSQ%2FJPLbhAs0WXlh9kd83FiBD4Y2d40K5CluvgbkcTwM5o%2BzldAM2I3kefjRftGsmBdENK2mV0b5G8WVQFFDEJXyzhGTO3yY4RJGCPQLLyF9sqn5eGvrH0nA3b4bfkb3fRvuImnSrFOWsrffGoLSXOVGphnYHcR%2FJrvnKF3HA81QUdcnXoDIGy3Oj6BeOJwJBSP2qSxxsnGtLQcJr6z0bJbEEHSszSKouJYwdOqCyZv1c2l9J7o3%2FolNxkUJ11rfMI6Wm70GOqUBtwWyuYX0IUORmnApAkZ%2BRm%2FSZRoLO%2FoHtd4iMZ9h%2Fy1hVhK0ffz8RWG0OvI%2BKknS7Hq8b8%2FBMG8qeS%2FsZAc071PksqFFNW2BudoxrAS55C4DagzRJuE25cYMPpwA%2Fj3jPW8IsBS%2B4XYGvxIdhZq7sBA%2FNRyRqIwW51ZJNGJ7Rb9E%2FhENRom1f7j0JzpzEIrAkXs6O4lA359xFVKdQvqqcbuX22d0&X-Amz-Signature=6ad899af709f91b7e29d76e6d4bfe9c3a48dbba57e69774ea2740ed87f07b177&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTWFM7LK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQC6q2oRR%2FIjJUO%2BaxwfFqgo4tz69IytNP4Y57RtLUyDlwIgWJUWm8ysfqTrBY4ycQrHZqvdSkK%2FMDfaGAVks8AwSnsqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcCKdH9suAOVuT2zircA5GS0bBVmZmgMzRZ66lmA1mjGRv%2BoXyLliTWdSk7AVfyf9k8mUhzrpDvBKsIeUVjJ%2BFLYpezwQNCLttnlsV9CU%2BPq6g2GjI0hrt6d9fxoGfrK%2FkXzz8%2B%2BxbDBS0GGkXonTsRFfgftYHid4HJ55wGPeHBLgY6n79hnGmxHvioBaIruohPeDCl4G%2FgbLN1FdUqQmUrlbizfMLpbli2FtKBSLos%2BmstE9oQD%2BEYl5I%2FGZo6VpYwkmmRwYDfhhAiYmDKwwNQU4HcpNb9usYVIpmOao5K3IPEaNkqNnbLCXi8s3XKN3BoENF9aNV8KjJgMNOWgzjEOknn%2FH4Nm95rtp5X7k4rE2GyNmlmMgjgB5YYoG6G3dLHcA2Q87FKkqXXdVsOUbTZ8I%2FlWzT6sEdNSot6Z9azS7P1lr7Orr5jxQX4RlBubKic9qoVj6sJdkWHdNYNTVmNvNjPQGCsbbRc03udhIa5z28tkgHRp7NIo2h8swU0DndUMrdT6nzyEYFziCLsKPBLV4MrjIEeWN9iMvSOhTXHZThRyRnnKZkH8nVTKv%2BeDqj4xxxBs6EQXsERYGLtdpe72hw77FvPPKBaCKR1YWforxLAHLXDfURTkOkJS5iq8BDgkX2wQaZbR03fMLWWm70GOqUBZyJGc6By5Nfeg02jVQqUNw%2F92E1dk%2FoZQpPp%2Fkt%2FgT6BO3ohyFWj6T03sOf%2Fsik6HYB62qOw2RhWGR6ULE%2FGk9zLiR9%2Fw8GNbiQZkxwRKg3nnnhzQ6XN7jo9JmxzyVzlIpH52enqUGfXczOOAYXoKtAGcOGjF4FdNJ1%2FUHMziYygMjIt9tO1XMi1OVF%2BgTldTzO8zv5LeNr7gBqqFH4rYWeza2vE&X-Amz-Signature=5434188a2182d14749e6dac2d0dd3bc3eea2c0f8064ac10805999339516a42b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFJUOJ4O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFdsPTZRFHRoa2BGnyGp5Qp2%2FLMUbwE4xwNLn52PZckWAiBddGeLR4RTIj7iFadXbST5JAzvAteIPgTbEjOvBZ0HFiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlUB9fgk1IGt4C8XjKtwDTLQq73he4Y2QXHoZFaZIF%2BXiqHk573SC0xRbjf5llmnML%2FF96GufsJvQ9CdO7TVRvTCYwK5PnoVSGGjycg004KRQ3eDUesbvCHDkgKiEu5h%2BpIE9QhrKggBZYw0JuodItz6HCNmwjg9V5WTTtMv%2BMnQVnJz%2BdUrZRSjUXdfHsi7AZLNLtEoUpRdhtogiLmPs6uSHaaBycaestrh3dcH3SDuYlXLmOTqaoSt59ciCkagtmKMAD%2B7Y3vZgSwK977AX6w0ySXowhg0AqPeo0vUGUOAGXFOeomtQ2JwVe%2FFIdz3lgLjpGZqRyK8QsfWlkFzXXaRIZzPErYE4ZDFmGqTnQQkkZUM%2BSl54hJR5Uorj38FcqrOXlJoddzL%2FWxAEd4ULx1jgBUSwxcFhP9w1xlQqmstE632aqjuDtGfH2juknKmPH%2BC3jRkODGt%2BPQN23nRFbaZg%2B5yQzzY6n%2FgdomYfaD1CA8dQ37ZleDIMJE%2FQsf00q4XaZuam0U4N57rcgqJ7UHEctbmLLgWSGXU2wSVqXSFkTF9D%2FsYz3fd6tj%2BoxIB87XJP%2BoAFpC6H1i10EW1zkN3IdiGzqGNlMB2Svnc12XCA%2B9fyYlMk1Qnog0%2FrAjTg8fqaTmlQgBq6%2BZEw8JWbvQY6pgF7ZyEkJvgzcxomh8CxrF1tqg58L8Nv6k%2BPCHfDqYhnlhfiSMOhOiuO87AaGVpW40uShNnc8AOwcYMiG2B1qK1kcKYHDoySwjjCyu47Ja8pGDS5mkK37ERRhBUP%2B5SqIL13EV2viXZWO8qs%2BqDDaNxGqwnHJoomFb3P4Xeo8a8GZtsK6P6aQlQfGdPP6Rwj7l1t9JJt40%2F8SQ%2F1DDu6M3RMeCmZKacX&X-Amz-Signature=f891753d4d200bfcd2de7d3cec2d9bf4eaaaf6178750e2e663485aea2bd6c4e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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