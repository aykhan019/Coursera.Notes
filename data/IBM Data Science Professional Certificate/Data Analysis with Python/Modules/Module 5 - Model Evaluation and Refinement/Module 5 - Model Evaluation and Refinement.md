

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=a1891014dfef9533c3ef092314557956de6110145e823d64a2b9471446bdfa83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=8aee7d267804ec0972db200e22a07eb585d4d53fade2ac07e63de6985a1570c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=3bed4806d6b7714b3eadde3fb42d725115bcd2a372e1e514d2c6fec06df12817&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=5cb5facf73e59a9d7aa988f53b6e8e03180acbec3dd9e6081f607198f8e1182a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=b2f4d0f2b451391cb3259690de543dff0a595f64f85bcd5231da64a0c4c236cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=d59d453e7bf870c8883f52eb1145c01db45cc573e756f7b8f000f4d1ee6303d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=8d29b91e371c35bc78b0351d181d1df8045b4b4b87cad2f632f2e5def3daff46&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=82a3b598883d09cffd564f01ac34c9a4e7f91838424f159e741e4262db94c214&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=5d2f39fc9170cf3d302fa18198e5d65e86bd3441704f15ca0842d25eb3a70229&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YADUS2W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBWRg5s362RMh%2BtLH9gKKuHORLCh1alNjhwsfuSRRQ48AiEAzJNGBeRl%2FlCmKWrdWKfHwcYlgm3ksOQQh3gCAaVC7PYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDCfL9aa5BWT6f9M6eircAwvuAkafqPMLlT7OgM2YU0Bw9Wy068cysDdq2suiMAJz9FIyPVZgSrSHZ9FEqfZTnxaJBmXeUbOVKgV6eEEUr27p%2BTvqPn4dt%2BtevQSfvY9NTlc32vgE3FPdeu3SanSnUh1jf7k9kCZSeZ28aZvPyy%2FMSEo1MAnaOlOUZvDXuoepdYD74Bqww9t8T0nCZCC3Wbp8mnwFa4zmsiV9GXiFeLLnQ4twIl%2FmGEjECWEERKUMz6SzzluMzfBvcCQirPqUOqRiF2WPEh4fMsA0XmiQEOaxVBBXsk0PxOYehm%2BCjMc9RV6UQH2g%2BPuwpGcPThbvG3Fd97bJrXb%2FSRQfbmlskLZzDXyass9aODblOIjy2QGdkvt1YFbAL%2FRKMCRW9gQP7V9L0aj%2FGiwbfdI6nKa3DI%2FQgWEdA3p%2Be5J6O5BVIrOocUDnvnetTclBl05r9qyTZHXr8pb4ZfZsTXLuCZktk7LDJYpFZ6%2FrO16jIqydXIzNaRcrjtWih%2FKAL97Dn0Lwm953ci5bKFNcxsxez8VQNrgRo8A94EQxsWQpysbTNgsEAPJ8InAdbxCs33qCXZZTQAybIGxifqwBbc3jBN1Q8RMugcWblqMcK%2BEAADar3GX8933fy6xLP213LRBoMNmZlb0GOqUBaht1kCDt0q4t5zoouBTwlWqNjUh6uEsxtdeKSPtKr8jRQ1VznhTcOS6%2B8o31CV4OzwNBFC%2BTiCGH0RWHxIvcszJpuoMbluWmHXRIUIUnZzOfjQIKUP%2FCqRtp4VXCZ7ZmxTt%2F4oOjLLLzB8e7Qop0cH64jxSdEv3jhkJdcvYfjUy90H2jYmwUJBAQ27wpLRFIP3v1QawLYYo2rSI2lXeVt2iAymes&X-Amz-Signature=6b8a19493fc5f05a67cdd4b3ea789698e5efd827fca676040b666ed0e499af49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YADUS2W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBWRg5s362RMh%2BtLH9gKKuHORLCh1alNjhwsfuSRRQ48AiEAzJNGBeRl%2FlCmKWrdWKfHwcYlgm3ksOQQh3gCAaVC7PYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDCfL9aa5BWT6f9M6eircAwvuAkafqPMLlT7OgM2YU0Bw9Wy068cysDdq2suiMAJz9FIyPVZgSrSHZ9FEqfZTnxaJBmXeUbOVKgV6eEEUr27p%2BTvqPn4dt%2BtevQSfvY9NTlc32vgE3FPdeu3SanSnUh1jf7k9kCZSeZ28aZvPyy%2FMSEo1MAnaOlOUZvDXuoepdYD74Bqww9t8T0nCZCC3Wbp8mnwFa4zmsiV9GXiFeLLnQ4twIl%2FmGEjECWEERKUMz6SzzluMzfBvcCQirPqUOqRiF2WPEh4fMsA0XmiQEOaxVBBXsk0PxOYehm%2BCjMc9RV6UQH2g%2BPuwpGcPThbvG3Fd97bJrXb%2FSRQfbmlskLZzDXyass9aODblOIjy2QGdkvt1YFbAL%2FRKMCRW9gQP7V9L0aj%2FGiwbfdI6nKa3DI%2FQgWEdA3p%2Be5J6O5BVIrOocUDnvnetTclBl05r9qyTZHXr8pb4ZfZsTXLuCZktk7LDJYpFZ6%2FrO16jIqydXIzNaRcrjtWih%2FKAL97Dn0Lwm953ci5bKFNcxsxez8VQNrgRo8A94EQxsWQpysbTNgsEAPJ8InAdbxCs33qCXZZTQAybIGxifqwBbc3jBN1Q8RMugcWblqMcK%2BEAADar3GX8933fy6xLP213LRBoMNmZlb0GOqUBaht1kCDt0q4t5zoouBTwlWqNjUh6uEsxtdeKSPtKr8jRQ1VznhTcOS6%2B8o31CV4OzwNBFC%2BTiCGH0RWHxIvcszJpuoMbluWmHXRIUIUnZzOfjQIKUP%2FCqRtp4VXCZ7ZmxTt%2F4oOjLLLzB8e7Qop0cH64jxSdEv3jhkJdcvYfjUy90H2jYmwUJBAQ27wpLRFIP3v1QawLYYo2rSI2lXeVt2iAymes&X-Amz-Signature=317376247a8defb6135cc223c9185b8a05f83569a67c7c705ae187381dc760d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YADUS2W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBWRg5s362RMh%2BtLH9gKKuHORLCh1alNjhwsfuSRRQ48AiEAzJNGBeRl%2FlCmKWrdWKfHwcYlgm3ksOQQh3gCAaVC7PYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDCfL9aa5BWT6f9M6eircAwvuAkafqPMLlT7OgM2YU0Bw9Wy068cysDdq2suiMAJz9FIyPVZgSrSHZ9FEqfZTnxaJBmXeUbOVKgV6eEEUr27p%2BTvqPn4dt%2BtevQSfvY9NTlc32vgE3FPdeu3SanSnUh1jf7k9kCZSeZ28aZvPyy%2FMSEo1MAnaOlOUZvDXuoepdYD74Bqww9t8T0nCZCC3Wbp8mnwFa4zmsiV9GXiFeLLnQ4twIl%2FmGEjECWEERKUMz6SzzluMzfBvcCQirPqUOqRiF2WPEh4fMsA0XmiQEOaxVBBXsk0PxOYehm%2BCjMc9RV6UQH2g%2BPuwpGcPThbvG3Fd97bJrXb%2FSRQfbmlskLZzDXyass9aODblOIjy2QGdkvt1YFbAL%2FRKMCRW9gQP7V9L0aj%2FGiwbfdI6nKa3DI%2FQgWEdA3p%2Be5J6O5BVIrOocUDnvnetTclBl05r9qyTZHXr8pb4ZfZsTXLuCZktk7LDJYpFZ6%2FrO16jIqydXIzNaRcrjtWih%2FKAL97Dn0Lwm953ci5bKFNcxsxez8VQNrgRo8A94EQxsWQpysbTNgsEAPJ8InAdbxCs33qCXZZTQAybIGxifqwBbc3jBN1Q8RMugcWblqMcK%2BEAADar3GX8933fy6xLP213LRBoMNmZlb0GOqUBaht1kCDt0q4t5zoouBTwlWqNjUh6uEsxtdeKSPtKr8jRQ1VznhTcOS6%2B8o31CV4OzwNBFC%2BTiCGH0RWHxIvcszJpuoMbluWmHXRIUIUnZzOfjQIKUP%2FCqRtp4VXCZ7ZmxTt%2F4oOjLLLzB8e7Qop0cH64jxSdEv3jhkJdcvYfjUy90H2jYmwUJBAQ27wpLRFIP3v1QawLYYo2rSI2lXeVt2iAymes&X-Amz-Signature=fc56a8da36c8d90ebb5183c6bb53e615d25f62ddf7379acdf422fdf49b2587a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=352add8d9389eb3016fc69a4e440f4a07056e02de4f50110bd5946a06a6fba5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=ebe45dc591e23d65a7cac12b91e59ce5ad8dddff5e1471109df537f99ac39353&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=8c667a2efe434ef890cc71b366701049b916a6f9a56cf2ac963863a56387fca2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=1dd13042ceace451ed99f980e1498b5b7bb83af592c1e7a9942502912c9b76ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=1551e13c537b1a3b0280166027ff532bbc22f1b807bb452b8d37c582bfb4eb54&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ROYEOOH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIESO4ryqEM%2FdMGITjBaLSoN8KW05R1UXfl1oVhx7RfTCAiAiQBJb8MSanx8o1GKRKOw3%2FoJ%2BDrrhStng9bjOtNuBWSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMR88v7Qw2J9J%2FrPO0KtwD0Cn8nu%2F1d3PHGtWTYq4cL0JPI8%2Bq17p6dcnxpzGpV57ShzHRmKuWq8S5KSiz1eu8EkflRT7oQowLtZvkA8jTfc%2BoM11PUVsFZktLnTkNCKU7qTYTmDWeLDfrp5qt4ASUjNkwjPPiNPfm88Jr3IBuNqrwXmWmwsFkCxwyOHbo8HW%2BGlO08BFQtmMtCRJhFMeY6Es2Jp7RyvmQXUZBXWbhNkjW00vdF8Yz0KwMrVSoZFmnhuQ86MhUqBABlna7FSrH0tb9jhfZ8YncpSBQzyGmWmf320DfvRdk3NhQCTMk3wyhQQFFZNT8N3VeaVaBMr5i5v%2BC0Xb7gHA1nv6UFq0OWxAFkjxW7wTFYQIWmrEifHmZWYvIdCYJ7AYk5eXhVDiX56rWLs2a2eUygiuGII%2BgNpT5si%2F4PhFPBXLs3G%2BFpqLvNYocQbh2CaZQ%2BDnJt9x8eRb%2BtmgJxUaoaw5%2BDrkpm%2BQUYe4AHcZn0dIJne7mbfnO48Gy9bJmSFh8bA%2F8gINvIHK48vorYOUew59m4IjR1jvCvVmSlidP5LYrll2Hl49EcBl65Ksp3CBoES8dys4M4dQdVXG29av%2BBtbEoDLMNu%2B1UNEWYf4FcSqGzFmVGIsRzmFlJeTzmZjY8%2B4w7pmVvQY6pgFEmdRM%2FFJbJf6wHocNeTlCFbXxHkOfg1tfboREV%2BggSjo78DZJMBFLRjKnVjXh5O%2Fylq1NiZMm8U3Q10oiEPaQvdmpujEgSOAV6Ddke4n3UwP5%2FzgNbz9wc1C3dAJeOvpqUOcxSqYpolJNLtH1F8Dd%2BPaOpymOvxAnvoBTGL8D5WC%2FPCoI2UsUf%2FmzG3WGimc%2FJw3gxaBAsSPlKbDP2cgmu8t1l16K&X-Amz-Signature=056aac19f1e6fa51577274758495faba7b741f89c8ae28d4a0b694de4cea8659&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V72IZ4RZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD72%2BO6QTkAwIGCsfFGp11kOG8YawOB1RD7qg%2FiFS4acQIhAP2dPsUjRBwAAQf%2FDaIqULyTfllCvmD2RnC4j99DCvKAKv8DCGkQABoMNjM3NDIzMTgzODA1Igwk8NSz25wBnKM8vR8q3AMwRtYsytoApl1P9ZpKPg%2FKb3f%2FE5WOhfCMnu2Q%2Bk9AZIL2Twy07iU2cuItPxjkUT4AApSuS2QOfvZGa7CDpSZzMARWqQ2nQkSdKuphtT%2FPNEt1EwEjXILWRJDkxrVPv28XGerpRepETbnAwLbKBh%2FV56HS2Hxw21ldPDMBjXEOolo5qeqTlS6Ib%2FISgwDgD03LMlzRBEOXIsry8iF8U2ATMRzdQvHWtzAgHg3ESOp95qZGzoTASBhusJM2Q3OSqMuKd%2F4atjPrwbK1ni1G%2B3P5JAyrNrvdictXL9CtMZju9yAacQgYuzVR0JoRxDuUdqO4CHAdOmqMDJ3FsxtQ0unR6WzHN%2BhdcohFNKQ5fUdtK0f5%2BaAZR9FBhGTJymGcIiF%2BR1%2FX1EdhikoHYK1uvvt875%2F5Jl0huzA3pdT6dSyDvEG3IY6vBQIy2nkPBkmyoxJSI8IDQHBu4UyOrhZElW80vVVSv4jMnUKCstPkxILXwiXaz3lsGxRY0HGLcau3bKnhsniG2WMPcYfr%2Bjhj4KEedXLZW2hcNwcpz8I5Zf4ezHgP6SmK0KMqCiPIgbPWUi9blKKmqZRrTesuXgsuu0LyIkURXkFB1cfIcD2Gn%2B1nLnVtyKySS0dcuV7RxDD2mZW9BjqkAZy9tgvCP8jSzPRzGCY8rrobKcgfWV8bR26ytADOhD1ngTLone1EoWiFjC75332mRAsCKnLFn6gemes0kf0EG3D9oSruT%2FwLAOlMpBf0nbJ%2FuH03KWG2ZCMJJmJ6rMbss4eYL%2Bnd2j6mgCJ6AkIVwwGmyPWRn5kX5vAK%2FUqxPZvkikPbJHULNh7wXdZkM9qi6Qz%2FR5whUnVMyNyOhtQd2%2BXlieGX&X-Amz-Signature=352dd0dec6ea00b001efd077af8c34d211f9e90a2135014fbde387cd8c0b2b59&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V72IZ4RZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD72%2BO6QTkAwIGCsfFGp11kOG8YawOB1RD7qg%2FiFS4acQIhAP2dPsUjRBwAAQf%2FDaIqULyTfllCvmD2RnC4j99DCvKAKv8DCGkQABoMNjM3NDIzMTgzODA1Igwk8NSz25wBnKM8vR8q3AMwRtYsytoApl1P9ZpKPg%2FKb3f%2FE5WOhfCMnu2Q%2Bk9AZIL2Twy07iU2cuItPxjkUT4AApSuS2QOfvZGa7CDpSZzMARWqQ2nQkSdKuphtT%2FPNEt1EwEjXILWRJDkxrVPv28XGerpRepETbnAwLbKBh%2FV56HS2Hxw21ldPDMBjXEOolo5qeqTlS6Ib%2FISgwDgD03LMlzRBEOXIsry8iF8U2ATMRzdQvHWtzAgHg3ESOp95qZGzoTASBhusJM2Q3OSqMuKd%2F4atjPrwbK1ni1G%2B3P5JAyrNrvdictXL9CtMZju9yAacQgYuzVR0JoRxDuUdqO4CHAdOmqMDJ3FsxtQ0unR6WzHN%2BhdcohFNKQ5fUdtK0f5%2BaAZR9FBhGTJymGcIiF%2BR1%2FX1EdhikoHYK1uvvt875%2F5Jl0huzA3pdT6dSyDvEG3IY6vBQIy2nkPBkmyoxJSI8IDQHBu4UyOrhZElW80vVVSv4jMnUKCstPkxILXwiXaz3lsGxRY0HGLcau3bKnhsniG2WMPcYfr%2Bjhj4KEedXLZW2hcNwcpz8I5Zf4ezHgP6SmK0KMqCiPIgbPWUi9blKKmqZRrTesuXgsuu0LyIkURXkFB1cfIcD2Gn%2B1nLnVtyKySS0dcuV7RxDD2mZW9BjqkAZy9tgvCP8jSzPRzGCY8rrobKcgfWV8bR26ytADOhD1ngTLone1EoWiFjC75332mRAsCKnLFn6gemes0kf0EG3D9oSruT%2FwLAOlMpBf0nbJ%2FuH03KWG2ZCMJJmJ6rMbss4eYL%2Bnd2j6mgCJ6AkIVwwGmyPWRn5kX5vAK%2FUqxPZvkikPbJHULNh7wXdZkM9qi6Qz%2FR5whUnVMyNyOhtQd2%2BXlieGX&X-Amz-Signature=abcd9be08741f44f0379dc4cc6cfa25c15e2966f5138c60a3bf0553eea992ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652O5VV2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBY%2BmM3Ccj9mW%2Fa1GqeshutuxJ7nd5vRICn2pR%2F3sTXjAiEAtP%2BaCZAe82KaMs0zCJBNKQj2dL4%2FzqZeVnPx%2BhZd3rEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDJGkXqcgRMNCvm8svCrcA63FnPU%2FrTGvwb0bxGAy0v0VtLUAEpJSUJNzT0AvJVDaQmfTLfJjyNjvQEpIkNHTfBMktpgpptD2u78tkRrzK021nMKrI7%2B8GURnAUS0avJhBJbKpeMMk8oQ3Ob1c3Zio%2B%2F7BypiP11mRLnfS%2FuSw%2Fn8Reno46B9FnC9iCozMMwU0gGm3e%2BUTM%2F4zOkDn9RpH4CHSJpktCkByD%2BHqErx4NhX0F3jQpHn%2FcqzFBs6y35NYLIGMKAdOga3n6ZW3HApAXrWBlYVezZjncRWTDlDb4KcNqwEWOGOaM%2FxulpjPhdyNIm4m731u4seBSCYOuBDzM1UYhvJrD85vpwdbls2AY1Oag5OWXqciMNnNWdBCM6xpiwoy6VWqNpYS25oeeGNWYzOOSOE3oy1N3m6O97Pwi3X6PWPY7BEXkEezntfiNB0%2B0pGuK2u96ka4JuYQUpDXlTX9MkrMmIMJ6lTvWAzgKW70Mvs6XLGgl3Gt7LrgrNGBwSTprmZvn089BXsx%2B%2F0249mCWQwim6pVesMPJXY5dPOIKo0r12%2BxxeMjkOnzQGFrBkb0nBQkJORTAODWUh6pwSGTnmRqtAsWNGY%2BDFdqOXVtG%2FHfkaQUit66MRoz3k33ga2UwjNoUeM8b%2BIMISalb0GOqUBgoGq%2Fv3j57X%2BecYiV7KbiDIZKCLkkURXM0VqZpny1cOxm%2BpRe7y7H55J%2F4gDBO%2BgyezGghddBrJ8MSFuPYDb77eUy42qOdw0by2d%2FmYzcAe9n8mgH%2BCCRsY6glHwfZsjh3mpNRqqKa0JmulMJVWoIqqpsP9sUhPjBlRbTQEVUZ4UTL2vNkrUkudOlGHaK2v0iiGq5F5XnAOgQBScIrOUP1shMzGt&X-Amz-Signature=b4ce1858ecee4ec43f7788d8b4724374037ea4515c6c69d70308e7159eecb790&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624RZISCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCABA6ywbiJ%2B1pYWX84oxfYwqE44%2FITUgohOVDohy8sTAIhAJCZIUT1FeQ0rUhHzHe1l9RorWUbLHPnTOUF5cZd4592Kv8DCGkQABoMNjM3NDIzMTgzODA1IgwQTTe2ZtnJYD0iZGoq3ANPXOrNgaWwDP7PR67Vbk%2FOFDeG%2B8BQ0e7P5DTnQzzNFpQNCUNY7ZVPtmR0j60btebUAiPzK3CojgTDKLFm8JFhT3%2Bhg82nKP0oGvPuadC%2Bet9jgeuganuBgBbZRW5ArE4ZThMlfXXYzGXZxt4X7KdD1a5BbIsXBtvseynAH6lb7Ukwry%2B0z8bHW2rBR%2FGvvHIdsvqxJDpJmPKnupu5vsBFjhRjfxEKTh7h%2Bz2ZUXiwJh38tf0gfehOEZ%2FgNenvvHzkracyrA07yoAy%2BimbuSrTotv5L7Hn2UZxWvoshAbcF1%2FBq%2Fje2LtvDvrRhHYiFcvnt8UnWBBpQNoXRxkEDC0xY4P81FCwHIMCHa8NiGC89SL%2BELIgyFXD78y5dDDehEJwzdpcs0c9quebD7hvr8YpE71MD8PraF3X4G3JudIw%2Bjpd7INHd8qHwQz7xkBVe7qq6q8BgOAntvOy5HLgxnGdLk5uVSJ%2FsTOROmCwz%2Bxq0YNLAeM9izZmwVedfC4b%2Fm0PA0jgM9pi2jtIByq42gRNHsHy%2Fq6QWgLvoLuNAirCmllCXH46SL%2ByNQmczuGadTnTIaWMOaSm4KaFCraoFsOgNzoxg%2F0MuRoKGRGaWsDiZPXmcry%2FbnBZ7G6GZDCampW9BjqkATykrqO7AL3O%2FP6VoyQx4lY1hpWqwYmMD3UEumR1Ta2hQLPdAox43X4u3LbR8eiHM%2B88o0K1mSmgo8v3q4oyGTs57Uj9KBVjZ7bBNtJpqfxnS7PeIt8wklIFX%2Fn4TNcZggS%2B2Mr3VFvfQQ%2F0KWLNFxJjRFI%2F5BmrW1lfVOJrjwXxEu3otxEGRUmRevdYZZfIh25hpZI0L0bg86B6MLVfYqsKI%2FPo&X-Amz-Signature=14866ca4fed5aa9dae5a17e7134b355570f14a8f43286aab18120275caa8ecee&X-Amz-SignedHeaders=host&x-id=GetObject)
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