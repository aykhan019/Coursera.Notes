

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=770f34b42f1c06abd5a4ce276f78dbd59e7c0059eba23316b91c962f111f87f3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=7223f1d4877cf650b25e35b8c105c69d11cc2311ccfa80fd2af8de0a97ac2777&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=e1f09c46820d102c1f0c650104235dae850447f621d94d23e5ca67232c4f74c0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=b7acf0d5b02f362803a2fede2ebca2736230503730d05bc87af1f90779e77ff8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=121d38436cc4e10beaa6689862bdd8c7b36372f9f944e67543009dc9ab7034ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=a5159c180eb8f936f9249a2838f3f2bf0d92bcd56e55b6ebd7aab57afcafa473&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=531203448f732f997f51c101c378c36477a81bfaf74af145e63850c85e1401af&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=877f531c0eb718976f6667e5efeeb736a544310e0817af51a94b745734b8a35c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=e4028091d80c18f01b40021135b1e8466955af89d1ec39ed5ff583b32bcc0f2c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNAEEJIF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDZGVIkzO15N0SSCCvfWvL99FgwSPpxlPKf9r0AZp7ccQIhAJ1J7Ks5Ff0JK8Y2FfuXvwPOC5aR5ZMTIqc6C7UyNd4yKv8DCCwQABoMNjM3NDIzMTgzODA1IgxAmCpjM%2BufXfOITkoq3APPegQLZsri5wNc%2F%2BTlBgxT0sjICKZ%2FI5PySQUAm2fshfZcA3PmT5ghKwcIhm34lW3lzaZmTG0E5JUe5JAn0jybCWrjwUYp%2BzIdZ%2BwKVpdc9k6nTg5nC5LGNyc68%2BV2fOKltluH%2FQEEDIKZXONWL6c9Kv%2FwMyu8%2BANqqd58%2Fxl4%2B62VeqZiI5k738NYjse6%2FoStfudsCR3kfXZb9Bh8nLr4B917Y7YSZLL0GkMe7DNBB8eSxoiddFhnF%2BpigrP0pONeOow%2Bb0GHSPll%2BKOgvTYbmx0krTqgz5onuQUlYO5HoCZWTa0M4n9CtdbPiJkT91%2FDNk2MuL6LZcqJFzFmth088CNtqWua5crhLaCgx08evoY8J5TRsbwwgKPuflNbO%2B0lf3csuRlChGgWO7av0nlfh5GYSc3wxsY75qGfXZpXauK%2BAIpBgKeS3Ew9rT8tdH6wlPa%2FiSuzzlp7XR94BK%2FPN%2FjSXADeWDw8aFGp2D4HQwUucUVp98dAb2OdYWJb8MF29T3h5Qp2BjMynS1djqw3%2FLagRIFoiMFl0%2FPN9ZrhpnawPGenGGYWZU5NSQkNyXP9yF8eworA%2B0x7n9YP5zaBZyzqD664EsCMocN5G3YUCx1UMHILi3JVxab6SjCh5oe9BjqkAS2mok%2BgtJ3aSSynHASWfK%2BCyO8TFT9GVZrIWbBSnRgc2mGqyjmnUg9vu2xszcq70SQWyfYvYSmNQumUt1D9zi8fEDmqJHpgmd7eYpaXjgCTBQZx7wVfLE4ZEPkQcpcA4lZfgfkL6WyuF9MrS1yjREzlGgjjJZ0aBE3oOGqSezCNHac6eNM4ykIYUpy6Q32uSBrNZZRGzLbkYXEUGQlZmXTiSJCY&X-Amz-Signature=51b8bc18ebb4bd75bf60dbea2f6770ec99043a71d0ad39fc1347d8e25255713e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNAEEJIF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDZGVIkzO15N0SSCCvfWvL99FgwSPpxlPKf9r0AZp7ccQIhAJ1J7Ks5Ff0JK8Y2FfuXvwPOC5aR5ZMTIqc6C7UyNd4yKv8DCCwQABoMNjM3NDIzMTgzODA1IgxAmCpjM%2BufXfOITkoq3APPegQLZsri5wNc%2F%2BTlBgxT0sjICKZ%2FI5PySQUAm2fshfZcA3PmT5ghKwcIhm34lW3lzaZmTG0E5JUe5JAn0jybCWrjwUYp%2BzIdZ%2BwKVpdc9k6nTg5nC5LGNyc68%2BV2fOKltluH%2FQEEDIKZXONWL6c9Kv%2FwMyu8%2BANqqd58%2Fxl4%2B62VeqZiI5k738NYjse6%2FoStfudsCR3kfXZb9Bh8nLr4B917Y7YSZLL0GkMe7DNBB8eSxoiddFhnF%2BpigrP0pONeOow%2Bb0GHSPll%2BKOgvTYbmx0krTqgz5onuQUlYO5HoCZWTa0M4n9CtdbPiJkT91%2FDNk2MuL6LZcqJFzFmth088CNtqWua5crhLaCgx08evoY8J5TRsbwwgKPuflNbO%2B0lf3csuRlChGgWO7av0nlfh5GYSc3wxsY75qGfXZpXauK%2BAIpBgKeS3Ew9rT8tdH6wlPa%2FiSuzzlp7XR94BK%2FPN%2FjSXADeWDw8aFGp2D4HQwUucUVp98dAb2OdYWJb8MF29T3h5Qp2BjMynS1djqw3%2FLagRIFoiMFl0%2FPN9ZrhpnawPGenGGYWZU5NSQkNyXP9yF8eworA%2B0x7n9YP5zaBZyzqD664EsCMocN5G3YUCx1UMHILi3JVxab6SjCh5oe9BjqkAS2mok%2BgtJ3aSSynHASWfK%2BCyO8TFT9GVZrIWbBSnRgc2mGqyjmnUg9vu2xszcq70SQWyfYvYSmNQumUt1D9zi8fEDmqJHpgmd7eYpaXjgCTBQZx7wVfLE4ZEPkQcpcA4lZfgfkL6WyuF9MrS1yjREzlGgjjJZ0aBE3oOGqSezCNHac6eNM4ykIYUpy6Q32uSBrNZZRGzLbkYXEUGQlZmXTiSJCY&X-Amz-Signature=fb7239c8c905cb55fb2917a9ffdc48709ff8f391d4ab73f4b435c8ae20614cbe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNAEEJIF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDZGVIkzO15N0SSCCvfWvL99FgwSPpxlPKf9r0AZp7ccQIhAJ1J7Ks5Ff0JK8Y2FfuXvwPOC5aR5ZMTIqc6C7UyNd4yKv8DCCwQABoMNjM3NDIzMTgzODA1IgxAmCpjM%2BufXfOITkoq3APPegQLZsri5wNc%2F%2BTlBgxT0sjICKZ%2FI5PySQUAm2fshfZcA3PmT5ghKwcIhm34lW3lzaZmTG0E5JUe5JAn0jybCWrjwUYp%2BzIdZ%2BwKVpdc9k6nTg5nC5LGNyc68%2BV2fOKltluH%2FQEEDIKZXONWL6c9Kv%2FwMyu8%2BANqqd58%2Fxl4%2B62VeqZiI5k738NYjse6%2FoStfudsCR3kfXZb9Bh8nLr4B917Y7YSZLL0GkMe7DNBB8eSxoiddFhnF%2BpigrP0pONeOow%2Bb0GHSPll%2BKOgvTYbmx0krTqgz5onuQUlYO5HoCZWTa0M4n9CtdbPiJkT91%2FDNk2MuL6LZcqJFzFmth088CNtqWua5crhLaCgx08evoY8J5TRsbwwgKPuflNbO%2B0lf3csuRlChGgWO7av0nlfh5GYSc3wxsY75qGfXZpXauK%2BAIpBgKeS3Ew9rT8tdH6wlPa%2FiSuzzlp7XR94BK%2FPN%2FjSXADeWDw8aFGp2D4HQwUucUVp98dAb2OdYWJb8MF29T3h5Qp2BjMynS1djqw3%2FLagRIFoiMFl0%2FPN9ZrhpnawPGenGGYWZU5NSQkNyXP9yF8eworA%2B0x7n9YP5zaBZyzqD664EsCMocN5G3YUCx1UMHILi3JVxab6SjCh5oe9BjqkAS2mok%2BgtJ3aSSynHASWfK%2BCyO8TFT9GVZrIWbBSnRgc2mGqyjmnUg9vu2xszcq70SQWyfYvYSmNQumUt1D9zi8fEDmqJHpgmd7eYpaXjgCTBQZx7wVfLE4ZEPkQcpcA4lZfgfkL6WyuF9MrS1yjREzlGgjjJZ0aBE3oOGqSezCNHac6eNM4ykIYUpy6Q32uSBrNZZRGzLbkYXEUGQlZmXTiSJCY&X-Amz-Signature=0b03bf50becb812e088a40326f27eafa06274eafedae7fd326c28d7fc7c8e3b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=901b6a44e0442821ff69a5337e1b525e9784950b43e19bc8e69a351790f8660c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=0bb837d6769288ff348c16d679962a60adbd3bfc876c2f1121c1299d4d7bf6e3&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=3c9108cd8504f84018afdf9e738053ead294763f7a395ba8f9e79072a860dda3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=5f2c263aeca736bb70ca19a1add6024ded4990f12edf98c37fbe5496c8c71513&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=31b0184ae5723cfe3cd0b0c2d38d80484303952a6af0af914f6765b34682dae4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SDXYZFJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCojrcSgbYHjZAYbeChwN0QdZBMjn8ERGhs99qzIJpJlwIhALjPp2srONTvn3n5I97a2%2BNMbekynBFlEkYCNhb6vRe6Kv8DCCwQABoMNjM3NDIzMTgzODA1IgyIbjDaVeVyuxmC03sq3AM7aQyhtFtfvJVDIFlMBClvRQL%2BqnHWapQL1%2F4nm1Q3hAI0%2FqIl5T89MmgWZ9tKaYUqsSok4NKee0bvdVMD%2Bdkzzxku198j4rblA2rmkAyW6ObiDdt63yG%2FCydILw%2FN82GxkSOBgn0Xya%2BoRAh5NWIUIPV8SgW7XkjL%2FdmMSegOEtHXvTMG6t9XwtdiLma0DMA4hJEomvQCZVv78ZaCwAl7YT0VhdDnBzS%2FJNqIVxPxldYld6vUbWb6tANWZiIaDypdUGGgEpD9wIQHuvDUulBby4Kd%2BWMDoYO1RH1DLdeXNiEEdRDlnPasJFAsKE2AdEgqWYeAXncAyLfyULuZoZ1wZJAC5OU96SFnGheBkJMKAOhnRR5BkEdxw10rXLx0qTjxLLXu%2FK4FmiGcbr%2BP030PHkE2zGoof%2BeORxc6XeZb6oTqO7UWLBktS4cdV6PIs1A%2FJ%2FJ%2FxAV2jFn5R4dNnfenoUDzPhhTkiuKZf5wfk4TJE6QOiSjB7gcvLKso%2B3WKiEQ5VmVZ%2F5t%2BET4jndDAc5DpJ9W315Tx0JkMtgE3jAzaxU1rFHGkM1HKnPidh5UPUhamc7n3fcXyenarxeic8uKLgJaBG%2BmOu%2Bgvy4hHjosKeMnaX2eSGb4YdST2TDr5Ye9BjqkAUmI2OGOvYyoqRXKbxiv29xZMTslCIQV1PiU84CDoVAroqgz8aYk2CRGp2lbKU7DDo1aL7rDvdkNeAHXJOFVXZ4g4b3M%2FnQbfJvGQok3g%2F68vUij67ARHfyXl8hJhqpDSJHhz4axhiK2RG08lVh6XXZIdaXJsb1865Ip2EfQzH3zP%2Bjffn0mx%2BIfStGGpxQIVL4NcV1n4SfhQcQ%2B2kwftwhiFPIS&X-Amz-Signature=22fb68192f1bc46df783978b93953543f8a1a82d10f7e9b90fe5e64266c92f06&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD5WX2UZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCSKdWBI9TymYi38EjBGXhluHHM6r%2FRH%2FYTuBAsqwscAgIhALG7KVRDw7mbGbEY2E4bjmyXC4KaL8vWYCBtjIuKHOvmKv8DCCwQABoMNjM3NDIzMTgzODA1IgxhvEoU8w9oLjNIaeQq3ANW%2FKAk4V9dd7QCItxJIVr5Ref9proLR%2BF631r%2FprSyyT7DTQeTg3nEicggoN79Kw4ZOeTXpHtTeA%2BDJr9zPMf7ASbJZCLkRs2b7a5pp3dbIpWfg%2Belmmr7pUxO42J%2FgbFF%2FRshs9xHRFjLRYGYWyh3i5PpHf6F0cliFhCir13Ddoe6QUxJOBtm%2BPdq8Heian4yFrlJ2CKx%2Fs7G5ShyP6qc04L9M4QgrfVUMUzxJQqvjO7GT8CSzA5xTd%2FoyOp%2FhGoeRFxoY9OAaic6xxOVpndio6TAdVbbIbKKRQKOomStPxg2UVh3uwPKO%2FCdkoEBuDGwVj3TfXGNND%2BBv4VtCLM%2BQ1w8sN5%2BQJiJ6uA1bNvFhdgwWk6Dv%2FFnnUD07unOfYkwPCxsGwjUvvtPk8PiWNnmSn7t0ZyTFRB9LGAcU2nfWlvKBWHKbwbo%2FfkqOoQD8PeUFYLym37RrPZytuQgNGp5c%2FV%2Bl%2FN40wZ5zCCnJMrjVyvXWKsqveQvcDJKBbPFx%2BqgMeUmxZc7x3yM2o%2Fx%2BdTlujqZiTLdodOcHk8vD9O42r6BT4GSSlNAxq%2FolENmjBn7wHS3PA4fRhq6iPsXhyHiAwIUnHgRof7grUSaoH%2F07CDEKPEF5hQiPWoYczCd5oe9BjqkAbw%2FRzIUnr%2BBtFi278WQRtxzg8KT88ymNA5x0irfJ69C%2BQS0Bb0aK6ZNaaLBPcPAnqD0DiSF%2FmEnKfWs9rk0zaEb9Axlzl8zqz1FFbM0s4tBYq8995uNU5SBzvc%2FM0iWvzSc7dIHh1Ori%2B5ZH056DWkdv7GvUelO8BIfiXQ5u6nFIJKdW9TxFp2nEPfCP1jigHmdbUcXpvqSTRlv90ZPFHrl8W4j&X-Amz-Signature=923435cb3c7a11bd5a66ec736a020173c9e8cc3067f7e4d6c37a0d8017491384&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD5WX2UZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCSKdWBI9TymYi38EjBGXhluHHM6r%2FRH%2FYTuBAsqwscAgIhALG7KVRDw7mbGbEY2E4bjmyXC4KaL8vWYCBtjIuKHOvmKv8DCCwQABoMNjM3NDIzMTgzODA1IgxhvEoU8w9oLjNIaeQq3ANW%2FKAk4V9dd7QCItxJIVr5Ref9proLR%2BF631r%2FprSyyT7DTQeTg3nEicggoN79Kw4ZOeTXpHtTeA%2BDJr9zPMf7ASbJZCLkRs2b7a5pp3dbIpWfg%2Belmmr7pUxO42J%2FgbFF%2FRshs9xHRFjLRYGYWyh3i5PpHf6F0cliFhCir13Ddoe6QUxJOBtm%2BPdq8Heian4yFrlJ2CKx%2Fs7G5ShyP6qc04L9M4QgrfVUMUzxJQqvjO7GT8CSzA5xTd%2FoyOp%2FhGoeRFxoY9OAaic6xxOVpndio6TAdVbbIbKKRQKOomStPxg2UVh3uwPKO%2FCdkoEBuDGwVj3TfXGNND%2BBv4VtCLM%2BQ1w8sN5%2BQJiJ6uA1bNvFhdgwWk6Dv%2FFnnUD07unOfYkwPCxsGwjUvvtPk8PiWNnmSn7t0ZyTFRB9LGAcU2nfWlvKBWHKbwbo%2FfkqOoQD8PeUFYLym37RrPZytuQgNGp5c%2FV%2Bl%2FN40wZ5zCCnJMrjVyvXWKsqveQvcDJKBbPFx%2BqgMeUmxZc7x3yM2o%2Fx%2BdTlujqZiTLdodOcHk8vD9O42r6BT4GSSlNAxq%2FolENmjBn7wHS3PA4fRhq6iPsXhyHiAwIUnHgRof7grUSaoH%2F07CDEKPEF5hQiPWoYczCd5oe9BjqkAbw%2FRzIUnr%2BBtFi278WQRtxzg8KT88ymNA5x0irfJ69C%2BQS0Bb0aK6ZNaaLBPcPAnqD0DiSF%2FmEnKfWs9rk0zaEb9Axlzl8zqz1FFbM0s4tBYq8995uNU5SBzvc%2FM0iWvzSc7dIHh1Ori%2B5ZH056DWkdv7GvUelO8BIfiXQ5u6nFIJKdW9TxFp2nEPfCP1jigHmdbUcXpvqSTRlv90ZPFHrl8W4j&X-Amz-Signature=9c6a1db23865f78ac4a4911cd71d9b2e3fcff63bd20dd1f2487f75024eeb9181&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BJ7CJD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDfinYoJBRiS4OBFzX2wyBnf8cwYSgq7HxCgofG6CVbEgIhANAXbXa4Wo3v3V%2FGNLw8HGDwF5fqwYDRM%2FJrLhEkFgdCKv8DCCwQABoMNjM3NDIzMTgzODA1IgwyDXLQyrR1RdE1IRoq3AM2SDXaXuNCNgcW2rJMBcOzd3kwCNetAAZqWn8fR3nUF3zYvRhVtPz9nfW2%2BYr95w3wzBZgj2FMaJ8GDrz2HNZhWWzfvJkgMDB0vuSCiJKU0Pp1yij4ncRSrCmCdyjeEisuLabduh68I30Wqj%2Bui4KzSL4eHaDX601ms0lbJojhI47hP9G2OhFiEauFPN9PVtJoyM%2FR7i%2FrxmwMfYRBvVdMAvpVkYhxXwQ1qQBMU9zAqX%2BUXLKzQ%2Fzns8iUCQc9MKZbbsSt8ka2RhYlKt4BHFwHOtPGldcLoGzF3%2F5YHeCirT5F%2Fpvdnh8eEb9FmheYExHzSCB7tzBydiRRcqaqqd6MJQNeIWN3MjFPhcGm34smgpJx8LPs1qba0N2oTFGaPqR6oZc03yr8%2F%2B7DFARaHMnqjE7Kc2q40PTJI5KRgeL1%2BQZUHG2KCx7VIRAwQdAXn0zwYhBcQvhbftFjx569u7VZTO8Hig5hZOC06i1RagpOg8bKY7hiWL4%2B3ui%2FFGC0MinenGSN66duaS7UXOLg%2BTNeTRA%2BLw992g1KZ96exujUlup4TIoy0JxyXTaPjPvfiU%2BfpCqYrNJYmHfRuSY%2Fap0ETapmjUzLe9WxikRhrqjMLStWXW3R0PJ6Plis3TD05Ye9BjqkAaFW3KGICPVWPkRlKFkOv4GZ0mONcHadPVppyUtgRLJ9RQwT%2FkDf5bjUmOdV387mcv6FnXYcGQL9PalpL46cvGWJhUnLSIglKgbSPW%2FdInrAvNQOjwJ0yUrRlEc2t72M494ff7il2Rd9USz4zG3NnIruDaME3leH3LLxWHxcMFAuHd9FlX6lrAmJ5iv5PMsGr13DlIycFMcuAIihdXZlxXGswsM9&X-Amz-Signature=3597960d4b0bd27fd8e479f1480c12f2a81d786e211a9643cd53980e28602864&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KNCILR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIHBmoKanwq13qndx2tQ8rVOBd7evWvH0QPf7Nb%2FocvTzAiEAvzgp2j1rmvBdENETqSKZI7XRWPTHhtS8w%2BHYMWk7atsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDD1cC5hJbNyyFkT48CrcA%2BhJ6ho0o59DVKwNt8jtfTNQmNjJcUizBAlRmp0hJnphrKr%2FloeIbSY55PwFntuSNYkwGtCmZppExzt86oE8zrAiihFInZNmac9yr48nkPEznqu8LI5BoOlYkE4I%2BPQ%2Fya3mr1q0GxqSHwySKVnEII4ch4%2FHyKWOlWUJOf5%2FOQrDL28vgNdaXA7tfi%2BdTT1Ok4dvxjUWt1%2FVBdsjIHCrd%2BuCuodD6gUKEtkSNonw9%2Bv8VAi7S%2BEhX5HPdK2oF1ssAK%2FDQOpJSzxJs5vrY2Eqc3PcXShYRs0oUYYGdI%2F1Dtrk%2B8NxHNLwSogVU8SmlFmc3J2iMCZ2%2F1hjf0vx8TthwFHtzm0kuXb9i8Uejbr7aTLdGHSm%2BYWoFZyfp7Xl2q6pEK7Q1suQvXT8PLzwtTQd5gEESK779lAzFmUU2YXT%2BIyg46bc9e1g6hHvY%2Br7gp1o0ZVgJ9k5WB6jUBEqTxy8L0ke4saDkDgyJUH4iWeTIeF0AbnbQWxpotWIUxwEhiLgVGVOgKrHyg%2BQxnmbxeXmbj%2F7o4hrzFva7WN9b7VLCmgbeDTWYZR4O0N1xGXCUglEuHh2m7R0hduXRr3%2Fc4HMtb1UnJvlK%2Fw6LWZMPZwGaVZ9%2F%2FMzzQWwsGyeEv3MMOjlh70GOqUBdNvjnb7%2BklLaNCG7gka16pj02fVdomuUb6%2BWBdpgbO%2BEeXg0SPjYfhbZkCrOq4OjEyela9JZwUVG2iDb6XCPBYc5laorGfn81HANu6SE2uwnPDYHKCFcKMKuLJw4Ft0P2TRDI3BjLZQcti7a%2FnD2iWWMHbzDCbfYb5MZNBcdtD%2BW9gNfbN6KfIt8t5wZJF1xwcjsJ1MQ6ZlkxKefnktD%2FwXRAT8O&X-Amz-Signature=3c0bf310f067fbb34e8dfcc881db7db86631a0313f7a65b9ac9b42c2db6bd306&X-Amz-SignedHeaders=host&x-id=GetObject)
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