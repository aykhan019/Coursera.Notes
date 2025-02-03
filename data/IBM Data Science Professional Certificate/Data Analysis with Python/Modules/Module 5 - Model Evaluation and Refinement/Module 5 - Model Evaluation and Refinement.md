

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=f89603abdde32734b7cafbd98bb5bbf11839461b06a062383325c964f27e7b04&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=56553f941aa42c5e567315c858ee1f9312f84f29e044d55282d0f57a6fe45fae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=cd77b050e4a37682387df3b4121fd80b437e397230b5e0f28a5b01339bdc8bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=2fcbdb7f59192b3359e45e28029b3b0bc2a06fd38f5c32754b7a33c7fdfed619&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=d2a1d0fa92267c73d06fdaac3d1c6e41091980ce4b5cd4081aee70f2ef1c2e45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=b5e65c3928b9be2fa60d21e62acdca31783a361de4a6810ddf1436218aba26e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=ba3db61d26f69370caf2bce961c3ae9b116ee21cf7f612e3a9090b4cdeffad0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=28a84c2730c079095249337baa20d624d2a5af8f9b775a92315ea81de3ae0470&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=a55f125da9bf79fae74f37521dbcc9491f4c4d4a31be1690c637591e0fec0b07&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4XVZFE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC30Cb2nYiblSJbgwNWa8UNrhhbBetOswDCAjaIPss6AAiAj5DsYso7%2FxyfXGvFb9IuQbEe2eFvOFhWtz%2FNTZUxGciqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTECFWHAS3OlCm5%2BzKtwDYs185kQNJvaa67lBMgiF2Ikf9tdxewsTrNCEXj1cSGhLBljC2TOkiSm5uO9MkY8R6afaYRYEVddt9%2BdvZ3I1Pajft1Nb4QBsmv7mDG70qau1AS2YuC8xdo92qekeIWwN1MJOt%2FDyxkcG1yaeAPb51Z%2Bcbsz0eJUiVGknMODxYTeWMQhQbpQuCDD3Z9mEU4m%2B7%2F46Nlrhn%2BF4gAdDLQm43iSbNBkPSU4dnSEjesqidtQKPSbuZQs5xLFuLq0ZwMDDk7pZEJuHrcP1lEU0XtPqUchMdtPBRaELHQD6x%2FyBcBg8vywP734RnmeqW1oy4HVuDLtWRZKObXClMk1Cz5U8w2a7nO1jC50hTD%2BEPprFHkL280lMt8bmQqzBnFGAxW2Kf1IMKc99U33XZIKkHJD%2FmpAxi4OvDlhR%2BBilVfabCCYOwixo083MM1d35wyYTDbpCBXlWn%2FdT4ZcrIgeoL7pOySRh%2F1LXfausXfNGHz3Z5cx6mGoG%2FB5w6DoLfGzhghl2k%2FtSnvAFSi9otczlovsa1WmyvzFS5Xu4hMaj1DBk%2Bm2%2F4atx3TmNEBu8pggt8VrNEJDechSgUs1gDqiJTCFfhuxXypc%2FHbST9vJnAu29ZMu14GszjJZXxgyhxMwp7qBvQY6pgEquQLN9ep6rRd8KvcLu2W9xxX664%2B4uvkeSUq5u55JSH9md%2BqXHVhn7H6ckoTe3Jm9MT%2B9YjKmu0evvR2PCCc0GrL11Rc16iC3Yr%2FpEhVz9Pe1ZM7DM4K6MbGnVcU1kRe4uRZsT2rq9g2doi9ofZ8ihlf2MNdbpnVjtSyMkBc7EbD23ZqiLbMWOFOeD2S0WgJc4ghamC9qvPO7FlZK58im5kkiQXbl&X-Amz-Signature=44140916d4bdfec2767df95b4a725d7dd738ca25a7e1f2733a7c6cd8a06bfd36&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4XVZFE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC30Cb2nYiblSJbgwNWa8UNrhhbBetOswDCAjaIPss6AAiAj5DsYso7%2FxyfXGvFb9IuQbEe2eFvOFhWtz%2FNTZUxGciqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTECFWHAS3OlCm5%2BzKtwDYs185kQNJvaa67lBMgiF2Ikf9tdxewsTrNCEXj1cSGhLBljC2TOkiSm5uO9MkY8R6afaYRYEVddt9%2BdvZ3I1Pajft1Nb4QBsmv7mDG70qau1AS2YuC8xdo92qekeIWwN1MJOt%2FDyxkcG1yaeAPb51Z%2Bcbsz0eJUiVGknMODxYTeWMQhQbpQuCDD3Z9mEU4m%2B7%2F46Nlrhn%2BF4gAdDLQm43iSbNBkPSU4dnSEjesqidtQKPSbuZQs5xLFuLq0ZwMDDk7pZEJuHrcP1lEU0XtPqUchMdtPBRaELHQD6x%2FyBcBg8vywP734RnmeqW1oy4HVuDLtWRZKObXClMk1Cz5U8w2a7nO1jC50hTD%2BEPprFHkL280lMt8bmQqzBnFGAxW2Kf1IMKc99U33XZIKkHJD%2FmpAxi4OvDlhR%2BBilVfabCCYOwixo083MM1d35wyYTDbpCBXlWn%2FdT4ZcrIgeoL7pOySRh%2F1LXfausXfNGHz3Z5cx6mGoG%2FB5w6DoLfGzhghl2k%2FtSnvAFSi9otczlovsa1WmyvzFS5Xu4hMaj1DBk%2Bm2%2F4atx3TmNEBu8pggt8VrNEJDechSgUs1gDqiJTCFfhuxXypc%2FHbST9vJnAu29ZMu14GszjJZXxgyhxMwp7qBvQY6pgEquQLN9ep6rRd8KvcLu2W9xxX664%2B4uvkeSUq5u55JSH9md%2BqXHVhn7H6ckoTe3Jm9MT%2B9YjKmu0evvR2PCCc0GrL11Rc16iC3Yr%2FpEhVz9Pe1ZM7DM4K6MbGnVcU1kRe4uRZsT2rq9g2doi9ofZ8ihlf2MNdbpnVjtSyMkBc7EbD23ZqiLbMWOFOeD2S0WgJc4ghamC9qvPO7FlZK58im5kkiQXbl&X-Amz-Signature=7538ea1ca26fee67f9e125714b650ac40c475659af941fdbbdcc0504fb337073&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4XVZFE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC30Cb2nYiblSJbgwNWa8UNrhhbBetOswDCAjaIPss6AAiAj5DsYso7%2FxyfXGvFb9IuQbEe2eFvOFhWtz%2FNTZUxGciqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTECFWHAS3OlCm5%2BzKtwDYs185kQNJvaa67lBMgiF2Ikf9tdxewsTrNCEXj1cSGhLBljC2TOkiSm5uO9MkY8R6afaYRYEVddt9%2BdvZ3I1Pajft1Nb4QBsmv7mDG70qau1AS2YuC8xdo92qekeIWwN1MJOt%2FDyxkcG1yaeAPb51Z%2Bcbsz0eJUiVGknMODxYTeWMQhQbpQuCDD3Z9mEU4m%2B7%2F46Nlrhn%2BF4gAdDLQm43iSbNBkPSU4dnSEjesqidtQKPSbuZQs5xLFuLq0ZwMDDk7pZEJuHrcP1lEU0XtPqUchMdtPBRaELHQD6x%2FyBcBg8vywP734RnmeqW1oy4HVuDLtWRZKObXClMk1Cz5U8w2a7nO1jC50hTD%2BEPprFHkL280lMt8bmQqzBnFGAxW2Kf1IMKc99U33XZIKkHJD%2FmpAxi4OvDlhR%2BBilVfabCCYOwixo083MM1d35wyYTDbpCBXlWn%2FdT4ZcrIgeoL7pOySRh%2F1LXfausXfNGHz3Z5cx6mGoG%2FB5w6DoLfGzhghl2k%2FtSnvAFSi9otczlovsa1WmyvzFS5Xu4hMaj1DBk%2Bm2%2F4atx3TmNEBu8pggt8VrNEJDechSgUs1gDqiJTCFfhuxXypc%2FHbST9vJnAu29ZMu14GszjJZXxgyhxMwp7qBvQY6pgEquQLN9ep6rRd8KvcLu2W9xxX664%2B4uvkeSUq5u55JSH9md%2BqXHVhn7H6ckoTe3Jm9MT%2B9YjKmu0evvR2PCCc0GrL11Rc16iC3Yr%2FpEhVz9Pe1ZM7DM4K6MbGnVcU1kRe4uRZsT2rq9g2doi9ofZ8ihlf2MNdbpnVjtSyMkBc7EbD23ZqiLbMWOFOeD2S0WgJc4ghamC9qvPO7FlZK58im5kkiQXbl&X-Amz-Signature=5302b2625a40155f57e248bee806473b1320f77df508f79f784234010cf5b465&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=afd34f928e6521a6b5295ccccd4c2c629ce5242db50487cac8df6e161c216ca8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=8c28c6882cf2918c79d5ad1736e9352440118b0138fc15f7ca180ddf0545963a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=3faa95e01e3883d7f87e809458b6c5c990f0df467d85c56c3314ceb9cfeea6fe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=bc8ef23b00a594a4710a6de3ae4eaa64b0f12c0f68e4ce6d6bc97fc595c2335d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=9ee8b13871888cfb95d49d4f178debe29b4fc4e0adeb2b42647838de5945d01b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYLZMCAL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUKB1noaBS96rMOIxFGeo1MVHvnllci1GYQW6RUi8agAIgfxzRliuhUNa0hrvpyYRWp7eofvX4vkuTBbk5vT%2FEgaIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2FbINAvhNWhjW581CrcA1ydVbwP5O9%2Bysm3SmbMI58WlIh0TqyeXt42X1bkMxDeUkbgHNzxEVq6o6BN5FgcYkmlEB9KNG%2FHMfZy1BzKhleWzXJ17ytMb3HbukAFl8I0KJCJgRnEHReBY%2BWMKzu%2BF%2FAgQdJSfTb2hmLTSrNhj0xlx6nHGtAzRv%2FQbW9Dq6Np%2FKun0KvxU5IzTs2gDB7cBQvceSZi9yuj8enS37C0JwL%2FqKg%2Ff7IhufxLkJcMCMG5q%2Fto7swTl7RgO3g3mxlaqM%2B27gEY3%2F%2BFBtdg5X6BUB3eGgW%2B9v1Su4AYRZSRR8LJpr9WGCRmHuQPLzeH%2FiDOFCrRwXILX3RYKz%2FbxiOZomsyRDFk1uHCJ%2FDYyzxjgcfn7e8L7awSqVycfFZtlU7KAuzeRIP5S57X5m7lgba9o1MTLZufcJdTL6Kpzl9VkExu38EbKJfIMOw4aQUt3vobYy%2BwqLaci%2FAqSBIHW4TG0Aeodi2ymm3TnS%2F7bUGEvVyKrHVmWQtBLWumLqbrE3kS0sy1AEBDO7ye7hpgQ9WMwUTenJ0dm1oGdn4wzmEOrk%2FiarzJKX55vntmIrfzRQvZ6DWpkBVtlAu4aimje4lmUT79SaLrll%2Fr5thOmspEex0L7o%2F3fcOl1wFrkRoaMIK6gb0GOqUBn1EBPdy7WESqapJzfPP3%2FyRFN0%2BLue7IWJQ58HmIoHRVtX00bNnaUowkEcILJGmYysCOcay8T45MxrKBCfTBbRB7FBVmGDXGoTY6sFJavHUXFY94BXHZJCBrswKGfMWYsRHDhO6e1Vl4wiZ4dIRHK7v%2BRUNdldfhZJDHkiYX5rsVGKwQYSFq%2FGTYxcDNY7HCtweBNK5LBZHZx6QrTikjjUQATmJ9&X-Amz-Signature=866376ee63f741e6f37d5a91eceb2ec16a047019e968642c13d02d4cb5f35581&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOCKBMR5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk8t3qnZbP66sB%2F5nrO9S7vrUJ8XSzOBSWtxEeT1GdqAIgPpSgho6SQZ0p%2FPbwqafRdl2ZDpbTC3m4wd9ZfoFcwKAqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIw7eCBkRflZY5AyrcA2bLyUtTjjjIv%2FDmFVXftZNy77alNmv6MQgMKNf4ASw5Nf157T%2FTgykmK3LWSX16rjFnTxnFIduIxW2rsx6474Apxstq%2FxBNL%2FbnqJYC9HoXIT6S13e5i9eqMC5U3kvyeKG6jm67J8VtC7beUsl97yY%2FuIXkdmSNsiZMqd4b859V8URD3E%2FkFkzMsrYnrmQcnB8Gh1NbWxR36b5A9k5swdsS85OAGbCOHP8aHc1%2F4zXy3Jr%2B1ZDaDOTbpJajJz5mM%2Be1S%2FFBvFGDSkmszdbb0rYzESfgaCpqCaW3SRx9F8Tlsh7gj4tJtJiIy%2BEg%2FxIsdc6DpVtKuT3DzJ0jo34msTq%2BP0miuEBWt%2BLH0a7lwwNvCs%2BlCCaVds3ZWBZ58jZOf%2BeTrdBiYIngDtXSlytkJgtoRYaDhtVSCXaPwLtf5SVNjzB1hVZBUPVpaB6Mqseqx6er6UFcVwgZ%2FZTMJZmFqzrOgqLmbJwvAgCMU%2BPCWASEWD9UDfrqhDdcl65gj%2FNCliiT4%2BCAn975NI31gafkOF0Z0p0zM1EmfnooCAWzJEyl4KRQH%2FyVgbsjYjQ%2BIbHzveJiBUWE%2B4wGbovf5MYB%2BHBQMOuOY8J%2BbCzZIX4OKfMaG0WFinu1npEt76jCMPu6gb0GOqUBDANbgN0YhebmjF0iq2BHMzu9mw8bmuYKLnkGS8Dpjd%2F%2BZKb8JetA9Mt5NQogoXpCYrw1JdH9hvoCh%2BGwnpcH7rjWsIMg%2Bn7zBo%2FQOVbdCoXKE1lVM%2FO2lT1kw8H2onr0Ujk%2FY2N2Hl8vcV76r06tnEYGyoPTnPcE%2FIbykU1O3DHYbn%2FAVnZzq0WOHCIhH3VV5fnIi%2Bbd6o%2FWbobbwlmug8xIqdc2&X-Amz-Signature=ac742b52dcf2fcb9cc598dcc0027a668860b99fcdadfa9388524e247d17877c4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOCKBMR5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk8t3qnZbP66sB%2F5nrO9S7vrUJ8XSzOBSWtxEeT1GdqAIgPpSgho6SQZ0p%2FPbwqafRdl2ZDpbTC3m4wd9ZfoFcwKAqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIw7eCBkRflZY5AyrcA2bLyUtTjjjIv%2FDmFVXftZNy77alNmv6MQgMKNf4ASw5Nf157T%2FTgykmK3LWSX16rjFnTxnFIduIxW2rsx6474Apxstq%2FxBNL%2FbnqJYC9HoXIT6S13e5i9eqMC5U3kvyeKG6jm67J8VtC7beUsl97yY%2FuIXkdmSNsiZMqd4b859V8URD3E%2FkFkzMsrYnrmQcnB8Gh1NbWxR36b5A9k5swdsS85OAGbCOHP8aHc1%2F4zXy3Jr%2B1ZDaDOTbpJajJz5mM%2Be1S%2FFBvFGDSkmszdbb0rYzESfgaCpqCaW3SRx9F8Tlsh7gj4tJtJiIy%2BEg%2FxIsdc6DpVtKuT3DzJ0jo34msTq%2BP0miuEBWt%2BLH0a7lwwNvCs%2BlCCaVds3ZWBZ58jZOf%2BeTrdBiYIngDtXSlytkJgtoRYaDhtVSCXaPwLtf5SVNjzB1hVZBUPVpaB6Mqseqx6er6UFcVwgZ%2FZTMJZmFqzrOgqLmbJwvAgCMU%2BPCWASEWD9UDfrqhDdcl65gj%2FNCliiT4%2BCAn975NI31gafkOF0Z0p0zM1EmfnooCAWzJEyl4KRQH%2FyVgbsjYjQ%2BIbHzveJiBUWE%2B4wGbovf5MYB%2BHBQMOuOY8J%2BbCzZIX4OKfMaG0WFinu1npEt76jCMPu6gb0GOqUBDANbgN0YhebmjF0iq2BHMzu9mw8bmuYKLnkGS8Dpjd%2F%2BZKb8JetA9Mt5NQogoXpCYrw1JdH9hvoCh%2BGwnpcH7rjWsIMg%2Bn7zBo%2FQOVbdCoXKE1lVM%2FO2lT1kw8H2onr0Ujk%2FY2N2Hl8vcV76r06tnEYGyoPTnPcE%2FIbykU1O3DHYbn%2FAVnZzq0WOHCIhH3VV5fnIi%2Bbd6o%2FWbobbwlmug8xIqdc2&X-Amz-Signature=da2133de7403c1605a69e99d986b2bb767ebf6b8518109b7a859c5942d66cebd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDRKGWKU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDTZJXP6ILXGOugVigDHGHNBaEpFg6V0EwL%2BQ2FPpCd4AiEA9kpsBR2PY4JthE7KGaqBDLO3IN%2FLAO7Nykbj%2Fb%2FQVZkqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMRZn5BNzUHxGnj%2BJCrcAwwPTFeva36sippEOsLfO9ma2SptQvNJE41wBQdbsUpG7oDhZZeJjhUmOqJLYSVAR4jisXju4Kiw0Lbaa9EdCrbuvSZgjt6HSVdfpTx9Hgmx4eSGBe59oBpGfF5ZxRj06WAhYQKsw0sihKWmOqghzHlPz0eKZ2bCLzjBep7mCRx%2BFNwXatzZDf7F5%2BifFow6jf1VTOF8uWfnnEHJxLVzeee2ibHlcNMOi%2BF37IzTKK3FNqiYNqe2ODeP1TFtwxmsLuMyU6cKTZRj4lKF5gerdx%2FetvL9t179iMkUGFnXlRLqaAb1qwrnjYrz05v3MQR7Z4P923akv4MFYDPb6LrXTR7T5yoPUHj5qngqGTvxIwR8TSK5jV0QzkDA4JlGtZ%2FjbvggZDbWFB8lk5gBkCADOCd8Gcda6Jh%2FaNqNBdfoaR12XBsuC6wXIfYLjuyflcjF7sn0MEWbykVGoP1xg1vz5ylINF1UJ4yJsY1RuwYVJHErpjHUpraEjvT8BjiPfZ5Y3MKnIcYlnkvoI3GCae%2BmlLPaZ67wzzmOa27scZvIwtYpbXh%2BYt8DkTounkaQCZjqQVq6wb8B8FCbJAhhlEsPxliZeZx3dt6b4A%2BugVBKMvyu3Eo%2BxCJBFcPa6bTSMNa6gb0GOqUBNkCgsId9x1aTh8kqqKbqiPn6YYfVShDgZPD0q2K0V2g5i0RbdLohQxhBnca25sA2wvjBGlEhMNzJJ5qk1wofb8nhu2cH5gtmnSqdUSyw4Ah1fRZQVU14GMZMYJYSJLmQehEExXN7fQYgTpqnLQFlSfi8%2FBVZXLVgrZ0UbkWet7QqZDXnsx8KbuZOrlR8eSgR5AAip9GiRGkYKUSXsL5REZ%2BnaG%2FH&X-Amz-Signature=1181d2902befb6eb990783d5bdc78042b4ac488802c40d8f5b69875352956d64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSXDCTBL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BCtXQ%2BqJFLfqVPpctUgAatf3NYBeR7nKxN9Q71OBFAiEA%2FVwxodJkjH2k7tVuDqo44w0GqA5DbDa3iXuIBYQqWIIqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnMei%2FfWAXr91KDmCrcA53BWFNgiKP09BeFOaFx5znXmiX3IVj5D2qzEe4zzHNJImfcOl4VMLp68J5Q%2B%2B9LeBjk2ERbmcUft4ry9LGlxWkzA9Spw5QDVMdiEvqF0B2ju2L8%2BZY%2BaohdWXsHjuQixznyS22QvLo4G5YwFMM3NaooSDx%2FVW1A4%2FDQ9gWiwiDVvm%2F1Z%2FDjweQavL84jraqfRQ4Wx5h7f9Hr1pH%2BQvIAOa%2F6j3zOizTG0L1k3WvBMl5rIOfymf7iftID3fr62e2xH%2FzFCxsiupTgkCGV2XxIbwUBz8cgn77vlPXqcXzfiQuzXRrM7%2BxM3HFJtMGjXg%2FQNgAfLXiB0oobtnmiHJmzY%2BsfX4WSWHdaZnCEoE2t67G%2BdwWMcyBIx2pA7%2FF0z3Joo5LtVJuhc7tAVWXpGkkaB0hx6BkP8kl%2Bk77E0AiIUs2b0wELVOuXzTWueswjInbihXGCkamrD3iUMpFzmobNtBuP4GeGMTVMdCGtmIHnaKZbJMQliGgbwL4C5ro1lTVZiqluC2KwGu%2FxeusBE2iEkJ5dz7%2FotUbruMxi%2BV3NbU2nrcbYYdZVYn6bKYKq%2FX4h6hAAZmRw2vpfnoQ%2B7JORvjxqg5e5wUGDwc8Bba21Kbp8SQjk2UtIgG9Ad9JMLe6gb0GOqUB3oHlHvBOfvZU3YLdqXiJiA%2FLgulwHiG1S0y6HXjgHx7MAXIuog84%2BkHY62keAfO8KT7CjFMRC6sM%2BRxa85FSBwGRoyWj9hgypGs0dLuEnXKJvcTJK0Orl8fcOV06NXYvAkSeTuopEDek2y6SUfPec%2FWffrsr4Ne3wcnsalLkcEUDb0scasp3RMXAKcBaWFKsAaMeox%2BC9yQV67CUldGYl0UmGzFe&X-Amz-Signature=2d77d6f679b16f1f60699bd1c70af90a6276b221557ae80d380947bc6208d38b&X-Amz-SignedHeaders=host&x-id=GetObject)
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